# V3D-R Package Integrity Verifier

## Experiment Name

V3D-R — Package Integrity Verifier Revised

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v3d_r_package_integrity_verifier_report.json`

---

## Source Stage

`V3D_R_PACKAGE_INTEGRITY_VERIFIER_REVISED`

---

## Status

Completed

**PASS**

---

## Timestamp

2026-06-30 20:26:38

---

## Purpose

This stage verifies the integrity of the V3C-R artifact-only reproducibility package after ZIP extraction.

It checks package completeness, file sizes, and SHA-256 hashes.

---

## Verified Package

ZIP package:

`/workspace/lanzarini_validation_suite_v1/package/lanzarini_validation_suite_v3c_artifact_package.zip`

ZIP SHA-256:

`ddf33533d153d54eee7238117d51a295d3019007d8a69ad1151b48be8a999e44`

Extraction directory:

`/workspace/lanzarini_validation_suite_v1/package/v3d_r_verify_extracted_package`

Manifest:

`/workspace/lanzarini_validation_suite_v1/package/v3d_r_verify_extracted_package/MANIFEST_SHA256.csv`

---

## Verification Results

Manifest rows:

- 70

Files verified by exact SHA-256:

- 69

Manifest special verification:

- 1

Missing files:

- 0

Size mismatches:

- 0

Hash mismatches:

- 0

Overall result:

**PASS**

The source artifact reports:

- `pass_v3d_r = true`

---

## Manifest Handling

The file `MANIFEST_SHA256.csv` is self-referential.

For this reason, its SHA-256 self-match was intentionally skipped.

It was verified by:

- existence;
- nonzero size.

All other package files were verified using exact SHA-256 comparison.

---

## Output Artifact

CSV rows:

`results/csv/v3d_r_package_integrity_verifier_rows.csv`

---

## Strict Note

The source artifact states that V3D-R verifies the V3C-R ZIP package after extraction.

All files except `MANIFEST_SHA256.csv` are verified by exact SHA-256.

`MANIFEST_SHA256.csv` is self-referential, so its SHA-256 self-match is intentionally skipped and it is verified by existence and nonzero size.

---

## Known Limitations

This stage verifies package integrity only.

It does not run benchmarks.

It does not validate numerical correctness beyond the packaged artifacts.

It does not import private kernel code.

It does not claim one-command reproducibility.

---

## Conclusion

The V3D-R Package Integrity Verifier completed successfully.

The extracted V3C-R artifact package contained all expected files, with zero missing files, zero size mismatches, and zero hash mismatches.

The source artifact reports an overall **PASS** status.

This report reproduces only the information contained in the public source artifact and does not introduce additional experimental claims.
