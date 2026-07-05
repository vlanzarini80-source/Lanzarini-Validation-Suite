# V2F Artifact Integrity Validation

## Experiment Name

V2F — Artifact Integrity Validation

---

## Source Artifacts

This report is derived from the public validation artifacts:

`results/json/v1e_artifact_manifest_report.json`

`results/json/v1e_artifact_manifest.json`

---

## Source Stage

`V1E_ARTIFACT_MANIFEST_SHA256_AUDIT`

---

## Status

Completed

---

## Timestamp

2026-06-30 05:16:29

---

## Validation Type

Artifact manifest and SHA-256 integrity audit.

---

## Root Directory

`/workspace/lanzarini_validation_suite_v1`

---

## Results Directory

`/workspace/lanzarini_validation_suite_v1/results`

---

## Manifest Outputs

Generated manifest files:

- `/workspace/lanzarini_validation_suite_v1/results/json/v1e_artifact_manifest.json`
- `/workspace/lanzarini_validation_suite_v1/results/csv/v1e_artifact_manifest.csv`

---

## Artifact Inventory

The audit recorded:

- Total public artifacts: 23
- Artifact types: CSV and JSON
- Total artifact size: 279401 bytes
- Hash algorithm: SHA256

The manifest includes public validation artifacts from:

- `results/json/`
- `results/csv/`

Private kernel directories are excluded.

---

## Integrity Result

The source artifact reports:

- `pass_v1e`: true

Overall result:

**PASS**

---

## Public Artifact Examples

The manifest includes SHA-256 records for public artifacts such as:

- `results/json/v1a_environment_report.json`
- `results/json/v1b_adapter_contract_report.json`
- `results/json/v1b_r_correctness_report.json`
- `results/json/v1c_lite_runtime_report.json`
- `results/json/v1d_lite_energy_report.json`
- `results/csv/v1b_r_correctness_rows.csv`
- `results/csv/v1c_lite_runtime_rows.csv`
- `results/csv/v1d_lite_energy_rows.csv`

Each listed artifact includes:

- relative path;
- absolute path;
- file type;
- size in bytes;
- modification timestamp;
- SHA-256 hash.

---

## Pass / Fail Criteria

The validation is considered successful when:

- expected public artifacts are present;
- public artifacts are inventoried;
- SHA-256 hashes are computed;
- private kernel source files are excluded;
- the source artifact reports `pass_v1e = true`.

---

## Known Limitations

This report validates artifact inventory and hash generation only.

It does not validate:

- numerical correctness;
- runtime performance;
- energy efficiency;
- scientific superiority;
- proprietary kernel implementation details.

---

## Strict Note

The source artifact states that V1E verifies expected public artifacts and records SHA-256 hashes.

This is an integrity audit, not a benchmark.

Private kernel source is excluded.

---

## Conclusion

The V2F Artifact Integrity Validation confirms that the public Validation Suite generated a SHA-256 artifact manifest for the public validation outputs.

The audit recorded 23 public artifacts, covering JSON and CSV outputs, with a total recorded size of 279401 bytes.

The source artifact reports an overall **PASS** status.

This report reproduces only the information contained in the public validation artifacts and does not introduce additional experimental claims.

---

## Guiding Principle

This report documents artifact integrity validation only.

No experimental results have been added, reconstructed, inferred, or modified.
