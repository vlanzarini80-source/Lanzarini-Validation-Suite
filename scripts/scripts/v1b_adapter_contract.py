import importlib
import inspect
import json
import os
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "json"
OUT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUT_DIR / "v1b_adapter_contract_report.json"

PRIVATE_KERNEL_DIR = Path(
    os.environ.get("LANZARINI_PRIVATE_KERNEL_DIR", ROOT / "private_kernel")
)

EXPECTED_MODULE = os.environ.get("LANZARINI_ADAPTER_MODULE", "adapter")
EXPECTED_FUNCTION = "selected_forward_q2"


def main() -> None:
    adapter_path = PRIVATE_KERNEL_DIR / "adapter.py"

    report = {
        "stage": "V1B_PRIVATE_ADAPTER_CONTRACT_CHECK",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "private_kernel_dir": str(PRIVATE_KERNEL_DIR),
        "adapter_path": str(adapter_path),
        "adapter_file_exists": adapter_path.exists(),
        "expected_module": EXPECTED_MODULE,
        "expected_function": EXPECTED_FUNCTION,
        "function_available": False,
        "function_callable": False,
        "signature": None,
        "pass_v1b": False,
        "errors": [],
        "strict_note": (
            "This stage checks only the public adapter contract. "
            "It does not expose or print private kernel source code. "
            "The proprietary kernel implementation is not included in this repository."
        ),
    }

    try:
        if not PRIVATE_KERNEL_DIR.exists():
            raise FileNotFoundError(
                f"Missing private adapter directory: {PRIVATE_KERNEL_DIR}. "
                "Set LANZARINI_PRIVATE_KERNEL_DIR to the local adapter directory."
            )

        if not adapter_path.exists():
            raise FileNotFoundError(f"Missing adapter file: {adapter_path}")

        sys.path.insert(0, str(PRIVATE_KERNEL_DIR))

        adapter = importlib.import_module(EXPECTED_MODULE)

        if not hasattr(adapter, EXPECTED_FUNCTION):
            raise AttributeError(f"{EXPECTED_MODULE}.py does not expose {EXPECTED_FUNCTION}")

        fn = getattr(adapter, EXPECTED_FUNCTION)

        report["function_available"] = True
        report["function_callable"] = callable(fn)

        if not callable(fn):
            raise TypeError(f"{EXPECTED_FUNCTION} exists but is not callable")

        sig = inspect.signature(fn)
        report["signature"] = str(sig)

        params = list(sig.parameters.keys())

        required_names = ["q", "k", "v"]
        missing = [name for name in required_names if name not in params]

        has_window = "window" in params or "W" in params or "w" in params

        if missing:
            raise TypeError(f"Missing required parameters in signature: {missing}")

        if not has_window:
            raise TypeError("Missing window parameter: expected window/W/w")

        report["pass_v1b"] = True

    except Exception as e:
        report["errors"].append(repr(e))
        report["pass_v1b"] = False

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1B ADAPTER CONTRACT CHECK")
    print("=" * 80)
    print(json.dumps(report, indent=2))
    print("=" * 80)
    print("REPORT:", REPORT_PATH)
    print("PASS_V1B:", report["pass_v1b"])
    print("=" * 80)

    if not report["pass_v1b"]:
        raise SystemExit("V1B FAILED: adapter contract incomplete")

    print("V1B PASSED")


if __name__ == "__main__":
    main()
