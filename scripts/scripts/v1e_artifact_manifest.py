# ============================================================
# Split timestamp: 2026-06-30 14:05:29
#
# NOTE:
# ============================================================

# V1E - Artifact Manifest + SHA256 Audit
#
# Goal:
# - Inventory all public Validation Suite artifacts
# - Compute SHA256 hashes
# - Verify expected reports exist
# - Do NOT read or hash private kernel source
# - Do NOT expose private kernel code
# - No benchmark
# - No hardcoded benchmark results
# ============================================================

import os
import csv
import json
import time
import hashlib
from pathlib import Path

ROOT = Path("/workspace/lanzarini_validation_suite_v1")
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

# Expected public artifacts from V1A-V1D
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

# Private directories are explicitly excluded from manifesting.
EXCLUDED_PATH_PREFIXES = [
    "/workspace/private_kernel",
]

# Only public validation-suite artifacts are scanned.
SCAN_DIRS = [
    JSON_DIR,
    CSV_DIR,
]


def is_excluded(path: Path):
    p = str(path.resolve())
    for prefix in EXCLUDED_PATH_PREFIXES:
        if p.startswith(prefix):
            return True
    return False


def sha256_file(path: Path, chunk_size=1024 * 1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def file_type(path: Path):
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

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue

        for path in sorted(scan_dir.rglob("*")):
            if not path.is_file():
                continue

            if is_excluded(path):
                continue

            # Avoid self-referential inconsistency:
            # Do not include V1E outputs while they are being generated.
            if path.resolve() in {
                REPORT_PATH.resolve(),
                MANIFEST_JSON_PATH.resolve(),
                MANIFEST_CSV_PATH.resolve(),
            }:
                continue

            stat = path.stat()

            artifacts.append({
                "relative_path": str(path.relative_to(ROOT)),
                "absolute_path": str(path),
                "type": file_type(path),
                "size_bytes": stat.st_size,
                "mtime_unix": stat.st_mtime,
                "mtime_readable": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
                "sha256": sha256_file(path),
            })

    return artifacts


def main():
    missing_expected = [
        str(p) for p in EXPECTED_FILES
        if not p.exists()
    ]

    unexpected_private_exposure = []
    for scan_dir in SCAN_DIRS:
        if scan_dir.exists():
            for path in scan_dir.rglob("*"):
                if is_excluded(path):
                    unexpected_private_exposure.append(str(path))

    artifacts = collect_artifacts()

    manifest = {
        "stage": "V1E_ARTIFACT_MANIFEST_SHA256",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(ROOT),
        "scan_dirs": [str(x) for x in SCAN_DIRS],
        "excluded_path_prefixes": EXCLUDED_PATH_PREFIXES,
        "n_artifacts": len(artifacts),
        "artifacts": artifacts,
        "strict_note": (
            "V1E inventories only public validation-suite artifacts and computes SHA256 hashes. "
            "Private kernel directories are excluded and private kernel source is not read or exposed."
        ),
    }

    with open(MANIFEST_JSON_PATH, "w") as f:
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

    with open(MANIFEST_CSV_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=csv_fields)
        w.writeheader()
        for a in artifacts:
            w.writerow({k: a[k] for k in csv_fields})

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
            "V1E verifies that expected public artifacts exist and records SHA256 hashes. "
            "This is an integrity audit, not a benchmark. Private kernel source is excluded."
        ),
    }

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)

    print("=" * 80)
# print("LANZARINI VALIDATION SUITE v1.0 - V1E ARTIFACT MANIFEST + SHA256")
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


# ---- source cell 85 from Untitled1.ipynb ----
# ============================================================
# Lanzarini Validation Suite v2.0
#
