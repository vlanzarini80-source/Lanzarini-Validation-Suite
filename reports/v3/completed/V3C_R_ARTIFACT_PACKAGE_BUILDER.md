# V3C-R Artifact Package Builder

## Experiment Name

V3C-R — Artifact-Only Reproducibility Package Builder

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v3c_r_artifact_package_builder_report.json`

---

## Source Stage

`V3C_R_ARTIFACT_ONLY_REPRODUCIBILITY_PACKAGE_BUILDER`

---

## Status

Completed

**PASS**

---

## Timestamp

2026-06-30 20:23:55

---

## Purpose

This stage builds an artifact-only public reproducibility package from validated public reports and measured rows.

It does not run benchmarks.

It does not import private kernel code.

It does not claim one-command reproducibility.

---

## Package Output

Package directory:

`/workspace/lanzarini_validation_suite_v1/package/lanzarini_validation_suite_v3c_artifact_package`

ZIP package:

`/workspace/lanzarini_validation_suite_v1/package/lanzarini_validation_suite_v3c_artifact_package.zip`

ZIP SHA-256:

`ddf33533d153d54eee7238117d51a295d3019007d8a69ad1151b48be8a999e44`

---

## Package Inventory

Packaged files:

- 70

Generated package manifest:

`/workspace/lanzarini_validation_suite_v1/package/lanzarini_validation_suite_v3c_artifact_package/MANIFEST_SHA256.csv`

Public manifest CSV:

`/workspace/lanzarini_validation_suite_v1/results/csv/v3c_r_artifact_package_manifest.csv`

---

## Upstream Validation Status

The package builder verified that the following upstream public validation stages existed and passed:

- `pass_v1a`
- `pass_v1b`
- `pass_v1c`
- `pass_v1d`
- `pass_v1e`
- `all_pass_v1a_to_v1e`
- `pass_v2a`
- `pass_v2b`
- `pass_v2c`
- `pass_v2d`
- `pass_v3a_r`

The source artifact reports:

- `all_stage_pass = true`
- `pass_v3c_r = true`

---

## Excluded Artifact

The source artifact records the following non-passing stage as not included in the package validation path:

- `v3b_3_automatic_stage_splitter`

This is consistent with the strict note that V3C-R excludes broken V3B-3 splitter artifacts.

---

## Packaged Artifact Types

The package includes public artifacts such as:

- JSON validation reports
- CSV measurement rows
- Markdown reports
- HTML reports
- README file
- SHA-256 manifest

---

## Strict Note

The source artifact states that V3C-R builds an artifact-only package from validated public reports and measured rows.

It does not run benchmarks.

It does not import private kernel code.

It excludes broken V3B-3 splitter artifacts.

It does not claim one-command reproducibility.

---

## Known Limitations

This stage validates package construction only.

It does not validate:

- numerical correctness beyond the upstream artifacts;
- runtime performance beyond the upstream artifacts;
- energy measurements beyond the upstream artifacts;
- semantic correctness of generated scripts;
- one-command reproducibility;
- production readiness.

---

## Conclusion

The V3C-R Artifact Package Builder completed successfully.

The stage created an artifact-only reproducibility package containing 70 public files, generated a SHA-256 package manifest, created a ZIP package, and recorded the ZIP SHA-256 hash.

The source artifact reports an overall **PASS** status.

This report reproduces only the information contained in the public source artifact and does not introduce additional experimental claims.
