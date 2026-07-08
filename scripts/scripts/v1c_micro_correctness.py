import csv
import importlib
import json
import os
import sys
import time
import traceback
from pathlib import Path

import torch
import torch.nn.functional as F


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON_DIR = ROOT / "results" / "json"
OUT_CSV_DIR = ROOT / "results" / "csv"
OUT_JSON_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUT_JSON_DIR / "v1c_micro_correctness_report.json"
ROWS_PATH = OUT_CSV_DIR / "v1c_micro_correctness_rows.csv"
ERRORS_PATH = OUT_CSV_DIR / "v1c_micro_correctness_errors.csv"

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

T_GRID = [128, 256, 512]
W_GRID = [16, 32, 64, 128]
SEEDS = [101, 102, 103]

REL_TOL = 1e-3
COS_TOL = 0.999


PUBLIC_MODE_NOTE = (
    "The proprietary adapter is intentionally not included in the public repository. "
    "V1C is skipped in public-only mode unless LANZARINI_PRIVATE_KERNEL_DIR points "
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
            "mse": None,
            "relative_l2": None,
            "cos": None,
            "pass": False,
        }

    diff = candidate - reference
    max_abs = diff.abs().max().item()
    mse = (diff * diff).mean().item()

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
        "mse": mse,
        "relative_l2": relative_l2,
        "cos": cos,
        "pass": passed,
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
        "max_abs",
        "mse",
        "relative_l2",
        "cos",
        "finite_candidate",
        "finite_reference",
        "pass",
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
    print("LANZARINI VALIDATION SUITE v1.0 - V1C MICRO CORRECTNESS AUDIT")
    print("=" * 80)

    if not torch.cuda.is_available():
        summary = {
            "stage": "V1C_MICRO_CORRECTNESS_AUDIT",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "FAILED_NO_CUDA",
            "public_mode": False,
            "pass_v1c": False,
            "errors": ["CUDA is not available"],
            "strict_note": (
                "V1C requires CUDA because correctness is evaluated on CUDA tensors. "
                "No benchmark or correctness result is produced when CUDA is unavailable."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        raise SystemExit("V1C FAILED: CUDA is not available")

    try:
        selected_forward_q2, adapter_status = load_adapter_function()
    except Exception as e:
        summary = {
            "stage": "V1C_MICRO_CORRECTNESS_AUDIT",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "FAILED_ADAPTER_LOAD",
            "public_mode": False,
            "pass_v1c": False,
            "adapter_module": ADAPTER_MODULE,
            "expected_function": EXPECTED_FUNCTION,
            "private_kernel_dir": str(PRIVATE_KERNEL_DIR),
            "errors": [repr(e)],
            "traceback": traceback.format_exc(),
            "strict_note": (
                "V1C compares selected_forward_q2 against an SDPA local-window reference "
                "on small shapes only. It performs no speed benchmark and does not expose "
                "private kernel source code."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        raise SystemExit("V1C FAILED: adapter could not be loaded")

    if adapter_status["status"] == "SKIPPED_PUBLIC_MODE":
        summary = {
            "stage": "V1C_MICRO_CORRECTNESS_AUDIT",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "SKIPPED_PUBLIC_MODE",
            "public_mode": True,
            "pass_v1c": None,
            "adapter_module": ADAPTER_MODULE,
            "expected_function": EXPECTED_FUNCTION,
            "private_kernel_dir": str(PRIVATE_KERNEL_DIR),
            "reason": adapter_status["reason"],
            "public_mode_note": PUBLIC_MODE_NOTE,
            "n_rows": 0,
            "n_pass": 0,
            "n_fail": 0,
            "n_errors": 0,
            "rows_csv": str(ROWS_PATH),
            "errors_csv": str(ERRORS_PATH),
            "strict_note": (
                "V1C requires a locally available proprietary adapter to compare "
                "selected_forward_q2 against the SDPA local-window reference. "
                "The proprietary adapter is intentionally not included in the public repository."
            ),
        }

        write_empty_csv_files()

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        print(json.dumps(summary, indent=2))
        print("=" * 80)
        print("REPORT:", REPORT_PATH)
        print("STATUS_V1C:", summary["status"])
        print("PASS_V1C:", summary["pass_v1c"])
        print("=" * 80)
        print("V1C SKIPPED: public-only mode")
        print("REASON:", adapter_status["reason"])
        print("This is expected behavior for public validation.")
        return

    print("DEVICE:", DEVICE)
    print("DTYPE:", DTYPE)
    print("B,H,D:", B, H, D)
    print("T_GRID:", T_GRID)
    print("W_GRID:", W_GRID)
    print("SEEDS:", SEEDS)
    print("=" * 80)

    for T in T_GRID:
        for W in W_GRID:
            if W >= T:
                continue

            for seed in SEEDS:
                try:
                    torch.manual_seed(seed)
                    torch.cuda.manual_seed_all(seed)

                    q = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)
                    k = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)
                    v = torch.randn(B, H, T, D, device=DEVICE, dtype=DTYPE)

                    with torch.no_grad():
                        out_ref = sdpa_local_reference(q, k, v, W)
                        out_lanz = selected_forward_q2(q, k, v, W)
                        torch.cuda.synchronize()

                    metrics = correctness_metrics(out_lanz, out_ref)

                    row = {
                        "stage": "V1C_MICRO_CORRECTNESS",
                        "T": T,
                        "W": W,
                        "B": B,
                        "H": H,
                        "D": D,
                        "seed": seed,
                        "dtype": str(DTYPE),
                        "max_abs": metrics["max_abs"],
                        "mse": metrics["mse"],
                        "relative_l2": metrics["relative_l2"],
                        "cos": metrics["cos"],
                        "finite_candidate": metrics["finite_candidate"],
                        "finite_reference": metrics["finite_reference"],
                        "pass": metrics["pass"],
                    }

                    rows.append(row)

                    print(
                        f"T={T:4d} W={W:4d} seed={seed} | "
                        f"pass={metrics['pass']} "
                        f"rel_l2={metrics['relative_l2']} "
                        f"cos={metrics['cos']} "
                        f"max_abs={metrics['max_abs']}"
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
    n_pass = sum(1 for r in rows if r["pass"])
    n_fail = n_rows - n_pass
    n_errors = len(errors)

    pass_v1c = bool(n_rows > 0 and n_fail == 0 and n_errors == 0)

    summary = {
        "stage": "V1C_MICRO_CORRECTNESS_AUDIT",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "PASSED" if pass_v1c else "FAILED_CORRECTNESS",
        "public_mode": False,
        "device": DEVICE,
        "gpu": torch.cuda.get_device_name(0),
        "torch": torch.__version__,
        "dtype": str(DTYPE),
        "B": B,
        "H": H,
        "D": D,
        "T_GRID": T_GRID,
        "W_GRID": W_GRID,
        "SEEDS": SEEDS,
        "REL_TOL": REL_TOL,
        "COS_TOL": COS_TOL,
        "n_rows": n_rows,
        "n_pass": n_pass,
        "n_fail": n_fail,
        "n_errors": n_errors,
        "max_abs_max": max(
            [r["max_abs"] for r in rows if r["max_abs"] is not None],
            default=None,
        ),
        "relative_l2_max": max(
            [r["relative_l2"] for r in rows if r["relative_l2"] is not None],
            default=None,
        ),
        "cos_min": min(
            [r["cos"] for r in rows if r["cos"] is not None],
            default=None,
        ),
        "pass_v1c": pass_v1c,
        "strict_note": (
            "V1C compares selected_forward_q2 against an SDPA local-window reference "
            "on small shapes only. It performs no speed benchmark and does not expose "
            "private kernel source code."
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
        "max_abs",
        "mse",
        "relative_l2",
        "cos",
        "finite_candidate",
        "finite_reference",
        "pass",
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
    print("LANZARINI VALIDATION SUITE v1.0 - V1C COMPLETE")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print("=" * 80)
    print("REPORT:", REPORT_PATH)
    print("ROWS:", ROWS_PATH)
    print("ERRORS:", ERRORS_PATH)
    print("STATUS_V1C:", summary["status"])
    print("PASS_V1C:", pass_v1c)
    print("=" * 80)

    if not pass_v1c:
        raise SystemExit("V1C FAILED: correctness audit did not pass")

    print("V1C PASSED")


if __name__ == "__main__":
    main()
