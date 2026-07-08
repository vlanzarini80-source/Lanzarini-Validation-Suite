import csv
import importlib
import json
import os
import statistics
import sys
import time
import traceback
from pathlib import Path

import torch
import torch.nn.functional as F


try:
    ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ROOT = Path.cwd()

OUT_JSON_DIR = ROOT / "results" / "json"
OUT_CSV_DIR = ROOT / "results" / "csv"
OUT_JSON_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUT_JSON_DIR / "v1d_runtime_smoke_report.json"
ROWS_PATH = OUT_CSV_DIR / "v1d_runtime_smoke_rows.csv"
ERRORS_PATH = OUT_CSV_DIR / "v1d_runtime_smoke_errors.csv"

PRIVATE_KERNEL_DIR = Path(
    os.environ.get("LANZARINI_PRIVATE_KERNEL_DIR", ROOT / "private_kernel")
)

ADAPTER_MODULE = os.environ.get("LANZARINI_ADAPTER_MODULE", "adapter")
EXPECTED_FUNCTION = "selected_forward_q2"

DEVICE = "cuda"
DTYPE = torch.float16

B = 1
H = 4
D = 64

SHAPES = [
    {"T": 512, "W": 32},
    {"T": 512, "W": 64},
    {"T": 1024, "W": 64},
    {"T": 1024, "W": 128},
]

SEEDS = [201, 202, 203]

WARMUP = 5
RUNS = 20

REL_TOL = 1e-3
COS_TOL = 0.999


PUBLIC_MODE_NOTE = (
    "The proprietary adapter is intentionally not included in the public repository. "
    "V1D is skipped in public-only mode unless LANZARINI_PRIVATE_KERNEL_DIR points "
    "to a local proprietary adapter. This is expected behavior and does not indicate "
    "a failure of the public validation framework."
)


def load_adapter_function():
    adapter_path = PRIVATE_KERNEL_DIR / "adapter.py"

    if not PRIVATE_KERNEL_DIR.exists():
        return None, {
            "status": "SKIPPED_PUBLIC_MODE",
            "public_mode": True,
            "reason": f"Private adapter directory not found: {PRIVATE_KERNEL_DIR}",
        }

    if not adapter_path.exists():
        return None, {
            "status": "SKIPPED_PUBLIC_MODE",
            "public_mode": True,
            "reason": f"Private adapter file not found: {adapter_path}",
        }

    sys.path.insert(0, str(PRIVATE_KERNEL_DIR))
    adapter = importlib.import_module(ADAPTER_MODULE)

    if not hasattr(adapter, EXPECTED_FUNCTION):
        raise AttributeError(f"{ADAPTER_MODULE}.py does not expose {EXPECTED_FUNCTION}")

    fn = getattr(adapter, EXPECTED_FUNCTION)

    if not callable(fn):
        raise TypeError(f"{EXPECTED_FUNCTION} exists but is not callable")

    return fn, {
        "status": "ADAPTER_AVAILABLE",
        "public_mode": False,
        "reason": None,
    }


try:
    from flash_attn import flash_attn_func

    FLASH_OK = True
    FLASH_ERROR = None
except Exception as e:
    FLASH_OK = False
    FLASH_ERROR = repr(e)


def make_local_additive_mask(T, W, device, dtype):
    idx = torch.arange(T, device=device)
    valid = (idx[:, None] >= idx[None, :]) & ((idx[:, None] - idx[None, :]) <= W)
    mask = torch.zeros((T, T), device=device, dtype=dtype)
    return mask.masked_fill(~valid, float("-inf"))


def sdpa_local_reference(q, k, v, W):
    T = q.shape[2]
    mask = make_local_additive_mask(T, W, q.device, q.dtype)
    return F.scaled_dot_product_attention(
        q,
        k,
        v,
        attn_mask=mask,
        dropout_p=0.0,
        is_causal=False,
    )


def flash_local(q, k, v, W):
    qf = q.transpose(1, 2).contiguous()
    kf = k.transpose(1, 2).contiguous()
    vf = v.transpose(1, 2).contiguous()

    out = flash_attn_func(
        qf,
        kf,
        vf,
        dropout_p=0.0,
        softmax_scale=None,
        causal=True,
        window_size=(W, 0),
    )

    return out.transpose(1, 2).contiguous()


def correctness_metrics(candidate, reference):
    candidate = candidate.detach().float()
    reference = reference.detach().float()

    finite_candidate = bool(torch.isfinite(candidate).all().item())
    finite_reference = bool(torch.isfinite(reference).all().item())

    if not finite_candidate or not finite_reference:
        return {
            "finite_candidate": finite_candidate,
            "finite_reference": finite_reference,
            "max_abs": None,
            "relative_l2": None,
            "cos": None,
            "pass": False,
        }

    diff = candidate - reference
    max_abs = diff.abs().max().item()

    diff_norm = torch.linalg.norm(diff.reshape(-1)).item()
    ref_norm = torch.linalg.norm(reference.reshape(-1)).item()
    relative_l2 = diff_norm / (ref_norm + 1e-12)

    cos = F.cosine_similarity(
        candidate.reshape(-1),
        reference.reshape(-1),
        dim=0,
    ).item()

    passed = bool(relative_l2 < REL_TOL and cos > COS_TOL)

    return {
        "finite_candidate": finite_candidate,
        "finite_reference": finite_reference,
        "max_abs": max_abs,
        "relative_l2": relative_l2,
        "cos": cos,
        "pass": passed,
    }


def time_fn(fn, q, k, v, W):
    for _ in range(WARMUP):
        _ = fn(q, k, v, W)

    torch.cuda.synchronize()

    times_ms = []

    for _ in range(RUNS):
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        _ = fn(q, k, v, W)
        torch.cuda.synchronize()
        t1 = time.perf_counter()
        times_ms.append((t1 - t0) * 1000.0)

    return times_ms


def summarize_times(times_ms):
    mean_ms = statistics.mean(times_ms)
    median_ms = statistics.median(times_ms)
    min_ms = min(times_ms)
    max_ms = max(times_ms)
    std_ms = statistics.stdev(times_ms) if len(times_ms) > 1 else 0.0
    cv_pct = 100.0 * std_ms / mean_ms if mean_ms > 0 else float("inf")

    return {
        "mean_ms": mean_ms,
        "median_ms": median_ms,
        "min_ms": min_ms,
        "max_ms": max_ms,
        "std_ms": std_ms,
        "cv_pct": cv_pct,
        "runs": len(times_ms),
    }


def write_empty_csv_files() -> None:
    row_fields = [
        "stage",
        "T",
        "W",
        "B",
        "H",
        "D",
        "seed",
        "dtype",
        "lanz_correct",
        "lanz_max_abs",
        "lanz_relative_l2",
        "lanz_cos",
        "lanz_median_ms",
        "lanz_mean_ms",
        "lanz_min_ms",
        "lanz_cv_pct",
        "sdpa_median_ms",
        "sdpa_mean_ms",
        "sdpa_min_ms",
        "sdpa_cv_pct",
        "flash_available",
        "flash_correct",
        "flash_median_ms",
        "flash_mean_ms",
        "flash_min_ms",
        "flash_cv_pct",
    ]

    with open(ROWS_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row_fields)
        writer.writeheader()

    with open(ERRORS_PATH, "w", newline="", encoding="utf-8") as f:
        fields = ["T", "W", "seed", "error", "traceback"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()


def main() -> None:
    rows = []
    errors = []

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1D RUNTIME SMOKE BENCHMARK")
    print("=" * 80)

    if not torch.cuda.is_available():
        summary = {
            "stage": "V1D_RUNTIME_SMOKE_BENCHMARK",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "FAILED_NO_CUDA",
            "public_mode": False,
            "pass_v1d": False,
            "errors": ["CUDA is not available"],
            "strict_note": (
                "V1D requires CUDA because runtime smoke benchmarking is performed "
                "on CUDA tensors. No runtime result is produced when CUDA is unavailable."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        raise SystemExit("V1D FAILED: CUDA is not available")

    try:
        selected_forward_q2, adapter_status = load_adapter_function()
    except Exception as e:
        summary = {
            "stage": "V1D_RUNTIME_SMOKE_BENCHMARK",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "FAILED_ADAPTER_LOAD",
            "public_mode": False,
            "pass_v1d": False,
            "adapter_module": ADAPTER_MODULE,
            "expected_function": EXPECTED_FUNCTION,
            "private_kernel_dir": str(PRIVATE_KERNEL_DIR),
            "errors": [repr(e)],
            "traceback": traceback.format_exc(),
            "strict_note": (
                "V1D is a runtime smoke benchmark only. It verifies that the private "
                "adapter can be timed on small shapes. It is not a full performance claim "
                "and does not expose private kernel source code."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        raise SystemExit("V1D FAILED: adapter could not be loaded")

    if adapter_status["status"] == "SKIPPED_PUBLIC_MODE":
        summary = {
            "stage": "V1D_RUNTIME_SMOKE_BENCHMARK",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "SKIPPED_PUBLIC_MODE",
            "public_mode": True,
            "pass_v1d": None,
            "adapter_module": ADAPTER_MODULE,
            "expected_function": EXPECTED_FUNCTION,
            "private_kernel_dir": str(PRIVATE_KERNEL_DIR),
            "reason": adapter_status["reason"],
            "public_mode_note": PUBLIC_MODE_NOTE,
            "FLASH_OK": FLASH_OK,
            "FLASH_ERROR": FLASH_ERROR,
            "n_rows": 0,
            "n_correct": 0,
            "n_fail": 0,
            "n_errors": 0,
            "rows_csv": str(ROWS_PATH),
            "errors_csv": str(ERRORS_PATH),
            "strict_note": (
                "V1D requires a locally available proprietary adapter to time "
                "selected_forward_q2. The proprietary adapter is intentionally not "
                "included in the public repository. Therefore V1D is skipped in "
                "public-only mode."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        print("=" * 80)
        print("REPORT:", REPORT_PATH)
        print("ROWS:", ROWS_PATH)
        print("ERRORS:", ERRORS_PATH)
        print("STATUS_V1D:", summary["status"])
        print("PASS_V1D:", summary["pass_v1d"])
        print("=" * 80)
        print("V1D SKIPPED: public-only mode")
        print("REASON:", adapter_status["reason"])
        print("This is expected behavior for public validation.")
        return

    print("DEVICE:", DEVICE)
    print("GPU:", torch.cuda.get_device_name(0))
    print("TORCH:", torch.__version__)
    print("DTYPE:", DTYPE)
    print("B,H,D:", B, H, D)
    print("SHAPES:", SHAPES)
    print("SEEDS:", SEEDS)
    print("WARMUP:", WARMUP)
    print("RUNS:", RUNS)
    print("FLASH_OK:", FLASH_OK)
    print("=" * 80)

    for shape in SHAPES:
        T = shape["T"]
        W = shape["W"]

        for seed in SEEDS:
            try:
                torch.manual_seed(seed)
                torch.cuda.manual_seed_all(seed)
                torch.cuda.empty_cache()

                q = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)
                k = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)
                v = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)

                with torch.no_grad():
                    out_ref = sdpa_local_reference(q, k, v, W)
                    out_lanz = selected_forward_q2(q, k, v, W)
                    torch.cuda.synchronize()

                cm_lanz = correctness_metrics(out_lanz, out_ref)

                if not cm_lanz["pass"]:
                    raise RuntimeError(
                        f"Lanzarini correctness failed before timing: {cm_lanz}"
                    )

                lanz_times = time_fn(selected_forward_q2, q, k, v, W)
                sdpa_times = time_fn(sdpa_local_reference, q, k, v, W)

                lanz_summary = summarize_times(lanz_times)
                sdpa_summary = summarize_times(sdpa_times)

                flash_summary = None
                flash_correctness = None

                if FLASH_OK:
                    with torch.no_grad():
                        out_flash = flash_local(q, k, v, W)
                        torch.cuda.synchronize()

                    flash_correctness = correctness_metrics(out_flash, out_ref)

                    if flash_correctness["pass"]:
                        flash_times = time_fn(flash_local, q, k, v, W)
                        flash_summary = summarize_times(flash_times)

                row = {
                    "stage": "V1D_RUNTIME_SMOKE",
                    "T": T,
                    "W": W,
                    "B": B,
                    "H": H,
                    "D": D,
                    "seed": seed,
                    "dtype": str(DTYPE),
                    "lanz_correct": cm_lanz["pass"],
                    "lanz_max_abs": cm_lanz["max_abs"],
                    "lanz_relative_l2": cm_lanz["relative_l2"],
                    "lanz_cos": cm_lanz["cos"],
                    "lanz_median_ms": lanz_summary["median_ms"],
                    "lanz_mean_ms": lanz_summary["mean_ms"],
                    "lanz_min_ms": lanz_summary["min_ms"],
                    "lanz_cv_pct": lanz_summary["cv_pct"],
                    "sdpa_median_ms": sdpa_summary["median_ms"],
                    "sdpa_mean_ms": sdpa_summary["mean_ms"],
                    "sdpa_min_ms": sdpa_summary["min_ms"],
                    "sdpa_cv_pct": sdpa_summary["cv_pct"],
                    "flash_available": FLASH_OK,
                    "flash_correct": flash_correctness["pass"]
                    if flash_correctness
                    else None,
                    "flash_median_ms": flash_summary["median_ms"]
                    if flash_summary
                    else None,
                    "flash_mean_ms": flash_summary["mean_ms"]
                    if flash_summary
                    else None,
                    "flash_min_ms": flash_summary["min_ms"]
                    if flash_summary
                    else None,
                    "flash_cv_pct": flash_summary["cv_pct"]
                    if flash_summary
                    else None,
                }

                rows.append(row)

                print(
                    f"T={T:4d} W={W:4d} seed={seed} | "
                    f"Lanz={row['lanz_median_ms']:.4f} ms "
                    f"SDPA={row['sdpa_median_ms']:.4f} ms "
                    f"Flash={row['flash_median_ms'] if row['flash_median_ms'] is not None else 'NA'} "
                    f"| correct={row['lanz_correct']}"
                )

            except Exception as e:
                err = {
                    "T": T,
                    "W": W,
                    "seed": seed,
                    "error": repr(e),
                    "traceback": traceback.format_exc(),
                }
                errors.append(err)
                print("ERROR:", err)

    n_rows = len(rows)
    n_errors = len(errors)
    n_correct = sum(1 for row in rows if row["lanz_correct"])
    n_fail = n_rows - n_correct

    pass_v1d = bool(n_rows > 0 and n_errors == 0 and n_fail == 0)

    summary = {
        "stage": "V1D_RUNTIME_SMOKE_BENCHMARK",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "PASSED" if pass_v1d else "FAILED_RUNTIME_SMOKE",
        "public_mode": False,
        "device": DEVICE,
        "gpu": torch.cuda.get_device_name(0),
        "torch": torch.__version__,
        "dtype": str(DTYPE),
        "B": B,
        "H": H,
        "D": D,
        "SHAPES": SHAPES,
        "SEEDS": SEEDS,
        "WARMUP": WARMUP,
        "RUNS": RUNS,
        "FLASH_OK": FLASH_OK,
        "FLASH_ERROR": FLASH_ERROR,
        "n_rows": n_rows,
        "n_correct": n_correct,
        "n_fail": n_fail,
        "n_errors": n_errors,
        "lanz_median_ms_min": min(
            [row["lanz_median_ms"] for row in rows],
            default=None,
        ),
        "lanz_median_ms_max": max(
            [row["lanz_median_ms"] for row in rows],
            default=None,
        ),
        "sdpa_median_ms_min": min(
            [row["sdpa_median_ms"] for row in rows],
            default=None,
        ),
        "sdpa_median_ms_max": max(
            [row["sdpa_median_ms"] for row in rows],
            default=None,
        ),
        "flash_median_ms_min": min(
            [
                row["flash_median_ms"]
                for row in rows
                if row["flash_median_ms"] is not None
            ],
            default=None,
        ),
        "flash_median_ms_max": max(
            [
                row["flash_median_ms"]
                for row in rows
                if row["flash_median_ms"] is not None
            ],
            default=None,
        ),
        "pass_v1d": pass_v1d,
        "strict_note": (
            "V1D is a runtime smoke benchmark only. It verifies that the private "
            "adapter can be timed reproducibly on small shapes. It is not a full "
            "performance claim and does not expose private kernel source code."
        ),
        "rows_csv": str(ROWS_PATH),
        "errors_csv": str(ERRORS_PATH),
    }

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    row_fields = [
        "stage",
        "T",
        "W",
        "B",
        "H",
        "D",
        "seed",
        "dtype",
        "lanz_correct",
        "lanz_max_abs",
        "lanz_relative_l2",
        "lanz_cos",
        "lanz_median_ms",
        "lanz_mean_ms",
        "lanz_min_ms",
        "lanz_cv_pct",
        "sdpa_median_ms",
        "sdpa_mean_ms",
        "sdpa_min_ms",
        "sdpa_cv_pct",
        "flash_available",
        "flash_correct",
        "flash_median_ms",
        "flash_mean_ms",
        "flash_min_ms",
        "flash_cv_pct",
    ]

    with open(ROWS_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    with open(ERRORS_PATH, "w", newline="", encoding="utf-8") as f:
        fields = ["T", "W", "seed", "error", "traceback"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for err in errors:
            writer.writerow(err)

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1D COMPLETE")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print("=" * 80)
    print("REPORT:", REPORT_PATH)
    print("ROWS:", ROWS_PATH)
    print("ERRORS:", ERRORS_PATH)
    print("STATUS_V1D:", summary["status"])
    print("PASS_V1D:", pass_v1d)
    print("=" * 80)

    if not pass_v1d:
        raise SystemExit("V1D FAILED: runtime smoke benchmark did not pass")

    print("V1D PASSED")


if __name__ == "__main__":
    main()
