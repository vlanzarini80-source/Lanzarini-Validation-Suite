import csv
import hashlib
import json
import time
from pathlib import Path


try:
    ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ROOT = Path.cwd()

RESULTS_DIR = ROOT / "results"
JSON_DIR = RESULTS_DIR / "json"
CSV_DIR = RESULTS_DIR / "csv"

OUT_JSON_DIR = JSON_DIR
OUT_CSV_DIR = CSV_DIR
OUT_JSON_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = OUT_JSON_DIR / "v1e_artifact_manifest_report.json"
MANIFEST_JSON_PATH = OUT_JSON_DIR / "v1e_artifact_manifest.json"
MANIFEST_CSV_PATH = OUT_CSV_DIR / "v1e_artifact_manifest.csv"

EXPECTED_FILES = [
    JSON_DIR / "v1a_environment_report.json",
    JSON_DIR / "v1b_adapter_contract_report.json",
    JSON_DIR / "v1c_micro_correctness_report.json",
    JSON_DIR / "v1d_runtime_smoke_report.json",
    CSV_DIR / "v1c_micro_correctness_rows.csv",
    CSV_DIR / "v1c_micro_correctness_errors.csv",
    CSV_DIR / "v1d_runtime_smoke_rows.csv",
    CSV_DIR / "v1d_runtime_smoke_errors.csv",
]

EXCLUDED_DIR_NAMES = {
    "private_kernel",
    "__pycache__",
    ".git",
}

SCAN_DIRS = [
    JSON_DIR,
    CSV_DIR,
]


def is_excluded(path: Path) -> bool:
    resolved_parts = set(path.resolve().parts)
    return any(name in resolved_parts for name in EXCLUDED_DIR_NAMES)


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def file_type(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix == ".json":
        return "json"
    if suffix == ".csv":
        return "csv"
    if suffix == ".txt":
        return "text"
    if suffix == ".py":
        return "python"

    return suffix.replace(".", "") if suffix else "unknown"


def collect_artifacts():
    artifacts = []

    self_outputs = {
        REPORT_PATH.resolve(),
        MANIFEST_JSON_PATH.resolve(),
        MANIFEST_CSV_PATH.resolve(),
    }

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue

        for path in sorted(scan_dir.rglob("*")):
            if not path.is_file():
                continue

            resolved = path.resolve()

            if resolved in self_outputs:
                continue

            if is_excluded(path):
                continue

            stat = path.stat()

            artifacts.append(
                {
                    "relative_path": str(path.relative_to(ROOT)),
                    "absolute_path": str(path),
                    "type": file_type(path),
                    "size_bytes": stat.st_size,
                    "mtime_unix": stat.st_mtime,
                    "mtime_readable": time.strftime(
                        "%Y-%m-%d %H:%M:%S",
                        time.localtime(stat.st_mtime),
                    ),
                    "sha256": sha256_file(path),
                }
            )

    return artifacts


def main() -> None:
    missing_expected = [str(p) for p in EXPECTED_FILES if not p.exists()]

    unexpected_private_exposure = []

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue

        for path in scan_dir.rglob("*"):
            if is_excluded(path):
                unexpected_private_exposure.append(str(path))

    artifacts = collect_artifacts()

    manifest = {
        "stage": "V1E_ARTIFACT_MANIFEST_SHA256",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(ROOT),
        "scan_dirs": [str(x) for x in SCAN_DIRS],
        "excluded_dir_names": sorted(EXCLUDED_DIR_NAMES),
        "n_artifacts": len(artifacts),
        "artifacts": artifacts,
        "strict_note": (
            "V1E inventories only public validation-suite artifacts and computes "
            "SHA256 hashes. Private kernel directories are excluded and private "
            "kernel source is not read or exposed."
        ),
    }

    with open(MANIFEST_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    csv_fields = [
        "relative_path",
        "absolute_path",
        "type",
        "size_bytes",
        "mtime_unix",
        "mtime_readable",
        "sha256",
    ]

    with open(MANIFEST_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()

        for artifact in artifacts:
            writer.writerow({key: artifact[key] for key in csv_fields})

    pass_v1e = (
        len(missing_expected) == 0
        and len(unexpected_private_exposure) == 0
        and len(artifacts) > 0
    )

    report = {
        "stage": "V1E_ARTIFACT_MANIFEST_SHA256_AUDIT",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(ROOT),
        "results_dir": str(RESULTS_DIR),
        "manifest_json": str(MANIFEST_JSON_PATH),
        "manifest_csv": str(MANIFEST_CSV_PATH),
        "expected_files": [str(p) for p in EXPECTED_FILES],
        "missing_expected": missing_expected,
        "unexpected_private_exposure": unexpected_private_exposure,
        "n_artifacts": len(artifacts),
        "artifact_types": sorted(set(a["type"] for a in artifacts)),
        "total_size_bytes": sum(a["size_bytes"] for a in artifacts),
        "sha256_algorithm": "SHA256",
        "pass_v1e": pass_v1e,
        "strict_note": (
            "V1E verifies that expected public artifacts exist and records SHA256 "
            "hashes. This is an integrity audit, not a benchmark. Private kernel "
            "source is excluded."
        ),
    }

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=" * 80)
    print("LANZARINI VALIDATION SUITE v1.0 - V1E ARTIFACT MANIFEST + SHA256")
    print("=" * 80)
    print(json.dumps(report, indent=2))
    print("=" * 80)
    print("MANIFEST JSON:", MANIFEST_JSON_PATH)
    print("MANIFEST CSV:", MANIFEST_CSV_PATH)
    print("REPORT:", REPORT_PATH)
    print("PASS_V1E:", pass_v1e)
    print("=" * 80)

    if not pass_v1e:
        raise SystemExit("V1E FAILED: artifact manifest audit did not pass")

    print("V1E PASSED")


if __name__ == "__main__":
    main()
