# Public Validation and Reproducibility Framework for Sparse-Local Attention Research

![Validation](https://img.shields.io/badge/Validation-PASS-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CUDA](https://img.shields.io/badge/CUDA-Tested-green)
![Triton](https://img.shields.io/badge/Triton-Tested-orange)
![Research](https://img.shields.io/badge/Research-Reproducible-purple)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

# Overview

The **Lanzarini Validation Suite** is a public scientific validation and reproducibility framework developed to rigorously evaluate sparse-local attention research.

Rather than introducing a new attention algorithm, this repository provides a transparent validation workflow capable of verifying numerical correctness, benchmark execution, runtime stability, artifact generation and public reproducibility.

The framework intentionally separates **public scientific validation** from **proprietary kernel implementations**, allowing independent verification of published experimental evidence without exposing private implementation details.

---

# Project Goals

The primary objectives of the Validation Suite are to:

- provide a transparent validation workflow;
- verify numerical correctness;
- benchmark runtime performance;
- evaluate runtime stability;
- generate reproducible experimental artifacts;
- build publicly verifiable packages;
- verify package integrity using SHA-256 manifests;
- enable independent verification without exposing proprietary kernel implementations.

---

# Motivation

High-performance attention kernels are frequently evaluated using different benchmarks, datasets and experimental methodologies, making direct comparison difficult.

The purpose of this project is to provide a consistent scientific validation methodology documenting:

- how experiments were executed;
- how numerical correctness was verified;
- how runtime measurements were collected;
- how artifacts were generated;
- how integrity was preserved after publication.

---

# Validation Pipeline

The Validation Suite is organized as a sequential validation workflow.

Each stage validates a specific aspect of the project before the next stage is executed, ensuring that every published artifact is numerically correct, reproducible and integrity verified.

```text
V1A → V1B → V1C → V1D → V1E → V1F
                     ↓
           V2A → V2B → V2C → V2D
                     ↓
          V3A-R → V3C-R → V3D-R
```

## Validation Stages

| Stage | Description | Status |
|--------|-------------|--------|
| V1A | Environment Check | ✅ PASS |
| V1B | Adapter Contract Validation | ✅ PASS |
| V1C | Micro Correctness Validation | ✅ PASS |
| V1D | Runtime Smoke Test | ✅ PASS |
| V1E | Artifact Manifest Generation | ✅ PASS |
| V1F | Validation Report Generator | ✅ PASS |
| V2A | Extended Correctness Validation | ✅ PASS |
| V2B | Extended Runtime Benchmark | ✅ PASS |
| V2C | Runtime Stability Audit | ✅ PASS |
| V2D | Stable Runtime Report | ✅ PASS |
| V3A-R | Public Package Audit | ✅ PASS |
| V3C-R | Artifact Package Builder | ✅ PASS |
| V3D-R | Package Integrity Verification | ✅ PASS |

---

# Stage Groups

### V1 — Foundation Validation

- Environment setup
- Adapter validation
- Numerical correctness
- Runtime smoke testing
- Artifact generation

### V2 — Experimental Validation

- Extended correctness evaluation
- Runtime benchmarking
- Runtime stability analysis
- Stable runtime reporting

### V3 — Public Reproducibility

- Public package auditing
- Artifact package generation
- SHA-256 integrity verification

Each validation stage depends on the successful completion of the previous stages before public artifacts are generated.

---

# Latest Validation Status

Current public validation results:

- ✅ 13 validation stages completed
- ✅ Public reproducibility package generated
- ✅ ZIP reproducibility package generated
- ✅ SHA-256 manifest generated
- ✅ Package integrity verification passed

Package verification summary:

| Item | Result |
|------|--------|
| Manifest rows | **70** |
| SHA-256 verified files | **69** |
| Self-referential manifest | **1** |
| Missing files | **0** |
| Size mismatches | **0** |
| SHA-256 mismatches | **0** |

The current release represents the **first validated public reproducibility package** of the Lanzarini Validation Suite.

---

# Scientific Scope

The Validation Suite validates:

- numerical correctness;
- runtime measurements;
- runtime stability;
- benchmark methodology;
- artifact generation;
- package integrity;
- reproducibility workflow.

The Validation Suite does **not** attempt to validate theoretical properties of attention algorithms.

---

# Repository Contents

This repository contains the complete public validation infrastructure.

Included:

- Validation Suite source code
- Validation scripts
- JSON reports
- CSV reports
- Markdown reports
- HTML reports
- SHA-256 manifests
- Public reproducibility package
- Documentation

---

# Repository Structure

```text
lanzarini-validation-suite/

README.md
LICENSE
CITATION.cff
CHANGELOG.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
requirements.txt
pyproject.toml

scripts/
results/
package/
docs/
papers/
figures/
examples/
```

---

# Relationship to the Lanzarini Research Project

The Validation Suite represents the **public reproducibility component** of the broader Lanzarini research project.

The complete research program includes additional work on:

- sparse-local attention kernels;
- backend selection;
- runtime frontiers;
- adaptive backend routing;
- long-context evaluation.

These research components are intentionally maintained separately from this public validation repository.

---

# What is NOT Included

This repository intentionally does **not** include:

- proprietary Triton kernel implementations;
- proprietary sparse-local attention source code;
- proprietary backend routing implementations;
- internal development notebooks;
- private optimization code.

Its purpose is scientific validation and reproducibility rather than distribution of proprietary implementations.

---

# Scientific Claims

The Validation Suite supports claims regarding:

- correctness validation;
- benchmark execution;
- runtime stability;
- artifact generation;
- package integrity;
- reproducibility.

The Validation Suite does **not** support claims of:

- universal superiority over FlashAttention;
- universal superiority over SDPA;
- universal superiority over any attention implementation;
- performance outside experimentally evaluated configurations.

All performance conclusions remain limited to the benchmark domains documented by the published validation artifacts.

---

# Reproducibility

The Validation Suite automatically generates:

- JSON reports;
- CSV reports;
- Markdown reports;
- HTML reports;
- SHA-256 manifests;
- ZIP reproducibility packages.

These artifacts allow independent verification of all published experimental evidence.

---

# Intended Audience

This repository is intended for:

- researchers;
- machine learning engineers;
- GPU kernel developers;
- systems researchers;
- reproducibility studies;
- academic reviewers.

---

# Future Development

Planned future work includes:

- additional benchmark domains;
- validation on additional GPU architectures;
- expanded documentation;
- public datasets;
- integration with future scientific publications.

---

# Research Philosophy

The Validation Suite separates **scientific validation** from **proprietary implementation**.

Its purpose is to enable transparent, reproducible and independently verifiable GPU systems research while allowing proprietary kernel implementations to remain private.

---

# Public Validation Package

The complete public reproducibility package generated by the Validation Suite includes:

- JSON reports
- CSV reports
- Markdown reports
- HTML reports
- SHA-256 integrity manifests
- Reproducibility package

The package is generated directly from validated execution artifacts and is intended to support independent verification of the published experimental workflow.

Future releases of this repository will include updated public validation packages corresponding to new validated versions of the Validation Suite.

---

# Repository Status

Current public release: **Version 1.0.0**

Status:

- ✅ Validation pipeline completed
- ✅ Public reproducibility package generated
- ✅ SHA-256 integrity verification completed
- ✅ Documentation completed
- ✅ Repository prepared for public scientific use

The repository will continue to evolve with additional validation stages and reproducibility artifacts as the research project progresses.

```

# Citation

If this repository contributes to academic work, please cite the associated publication.

Citation metadata will be maintained through the included **CITATION.cff** file.

---

# License

The Validation Suite is distributed under the repository license.

The proprietary sparse-local attention kernel is **not** distributed as part of this repository.

---

# Author

**Valentino Lanzarini®**

Independent Research Project

---

# Disclaimer

This repository contains a public validation and reproducibility framework together with experimentally generated public artifacts.

Its purpose is to improve transparency, reproducibility and independent verification of sparse-local attention research.

The repository should **not** be interpreted as evidence that any attention implementation is universally superior.

Experimental conclusions remain strictly limited to the evaluated benchmark domains documented by the associated validation reports.

```
CONTAC:
vlanzarini80-source

```
