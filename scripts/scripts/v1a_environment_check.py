import json
import platform
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "json"
OUT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUT_DIR / "v1a_environment_report.json"


def run_cmd(cmd: str) -> dict:
    try:
        out = subprocess.check_output(
            cmd,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=30,
        )
        return {"ok": True, "output": out.strip()}
    except Exception as e:
        return {"ok": False, "error": repr(e)}


def get_env_report() -> dict:
    report = {
        "stage": "V1A_ENVIRONMENT_ADAPTER_CHECK",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "cuda_available": None,
        "gpu": None,
        "torch": None,
        "triton": None,
        "flash_attn": None,
        "selected_forward_q2_available": False,
        "selected_forward_q2_callable": False,
        "nvidia_smi": run_cmd("nvidia-smi"),
        "pass_v1a": False,
        "errors": [],
        "strict_note": (
            "V1A checks the CUDA/PyTorch/Triton environment and adapter availability. "
            "It performs no benchmark and does not expose private kernel source code."
        ),
    }

    try:
        import torch

        report["torch"] = torch.__version__
        report["cuda_available"] = torch.cuda.is_available()

        if torch.cuda.is_available():
            report["gpu"] = torch.cuda.get_device_name(0)
            report["cuda_device_count"] = torch.cuda.device_count()
            report["cuda_version_torch"] = torch.version.cuda
            report["cuda_capability"] = list(torch.cuda.get_device_capability(0))

    except Exception as e:
        report["errors"].append(f"torch_error: {repr(e)}")

    try:
        import triton

        report["triton"] = triton.__version__
    except Exception as e:
        report["errors"].append(f"triton_error: {repr(e)}")

    try:
        import flash_attn

        report["flash_attn"] = getattr(
            flash_attn,
            "__version__",
            "installed_unknown_version",
        )
    except Exception as e:
        report["flash_attn"] = None
        report["errors"].append(f"flash_attn_error: {repr(e)}")

    if "selected_forward_q2" in globals():
        report["selected_forward_q2_available"] = True
        report["selected_forward_q2_callable"] = callable(globals()["selected_forward_q2"])

    required_ok = (
        report["cuda_available"] is True
        and report["torch"] is not None
        and report["triton"] is not None
    )

    report["pass_v1a"] = bool(required_ok)
    return report


def main() -> None:
    report = get_env_report()

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1A ENVIRONMENT CHECK")
    print("=" * 80)
    print(json.dumps(report, indent=2))
    print("=" * 80)
    print("REPORT:", REPORT_PATH)
    print("PASS_V1A:", report["pass_v1a"])
    print("=" * 80)

    if not report["pass_v1a"]:
        raise SystemExit("V1A FAILED: environment incomplete")

    print("V1A PASSED")


if __name__ == "__main__":
    main()
