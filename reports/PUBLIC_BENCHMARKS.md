# Public Benchmarks

## Overview

This page summarizes the public validation results and benchmark-related information available in the Lanzarini Validation Suite.

Only experimentally verified and publicly available information is reported.

No simulated, estimated, or unpublished performance results are included.

---

# Public Validation Summary

| Stage | Expected Public Status | Description |
|-------|------------------------|-------------|
| V1A | PASS | Environment validation |
| V1B | PASS or SKIPPED_PUBLIC_MODE | Adapter interface validation |
| V1C | SKIPPED_PUBLIC_MODE | Public correctness workflow |
| V1D | SKIPPED_PUBLIC_MODE | Public runtime workflow |
| V1E | PASS | Artifact integrity (SHA-256) |
| V1F | PASS | Public validation report generation |

---

# Public Validation Environment

The public validation workflow has been verified using:

- NVIDIA A100-SXM4-80GB
- CUDA-compatible environment
- PyTorch 2.4.1
- Triton 3.0
- FlashAttention 2

---

# Public Validation Coverage

The public Validation Suite verifies:

- Environment configuration
- Adapter interface contract
- Public validation workflow
- Artifact generation
- SHA-256 artifact integrity
- Validation report generation

The proprietary sparse-local Triton kernel is intentionally excluded from the public repository.

---

# Repository Scope

This repository provides an open and reproducible validation framework.

It does not contain the proprietary sparse-local Triton implementation.

The public repository validates the methodology, reproducibility workflow, artifact generation, and integrity verification.

---

# Reproducibility

The public validation workflow can be reproduced by executing the validation stages described in the README.

When the proprietary adapter is unavailable, stages marked `SKIPPED_PUBLIC_MODE` represent the expected public behavior and do not indicate a validation failure.

---

# Future Public Releases

Future public releases may include additional experimentally verified material, such as:

- Validation on additional hardware platforms
- Extended public benchmark reports
- Additional validation artifacts
- Additional reproducibility studies

Only experimentally verified public results will be added.
