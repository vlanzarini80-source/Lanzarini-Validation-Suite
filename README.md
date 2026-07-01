> **Public Validation and Reproducibility Framework for Sparse-Local Attention Research**

![Validation](https://img.shields.io/badge/Validation-PASS-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CUDA](https://img.shields.io/badge/CUDA-Tested-green)
![Triton](https://img.shields.io/badge/Triton-Tested-orange)
![Research](https://img.shields.io/badge/Research-Reproducible-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)

---

# Overview

The **Lanzarini Validation Suite** is a public validation and reproducibility framework developed to rigorously evaluate sparse-local attention research.

The suite provides a complete validation workflow covering:

- numerical correctness
- runtime benchmarking
- runtime stability
- artifact generation
- public package creation
- SHA-256 integrity verification
- reproducibility reporting

The framework was designed to separate **public scientific validation** from **proprietary kernel implementations**, allowing experimental results to be independently verified without exposing private implementation details.

---

# Motivation

High-performance attention kernels are often evaluated using different benchmarks, datasets and experimental methodologies, making independent comparison difficult.

The objective of this project is to provide a transparent validation workflow that documents:

- how experiments were executed;
- how results were verified;
- how artifacts were generated;
- how integrity was preserved after publication.

---

# Validation Pipeline

The current public validation pipeline consists of thirteen validated stages.

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

# Current Validation Status

Validation pipeline status:

- Completed validation stages: **13**
- Public reproducibility package generated
- ZIP package generated
- SHA-256 manifest generated
- Integrity verification completed

Package integrity verification results:

| Item | Result |
|------|--------|
| Manifest rows | **70** |
| SHA-256 verified files | **69** |
| Self-referential manifest | **1** |
| Missing files | **0** |
| Size mismatches | **0** |
| Hash mismatches | **0** |

---

# Repository Contents

This repository contains the complete public validation infrastructure.

Included:

- Validation Suite source code
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

validation_suite/
artifacts/
reports/
examples/
docs/
paper/
figures/
```

---

# Scientific Scope

The Validation Suite validates:

- numerical correctness
- runtime measurements
- runtime stability
- artifact generation
- package integrity
- reproducibility workflow

The suite does **not** attempt to validate theoretical properties of attention algorithms.

---

# Relationship to the Lanzarini Research Project

The Validation Suite represents the **public reproducibility component** of the broader Lanzarini research project.

The complete research program includes additional experimental studies on:

- sparse-local attention kernels
- backend selection
- runtime frontiers
- adaptive routing
- long-context evaluation

Those research components are intentionally maintained separately from this public validation repository.

---

# What is NOT Included

This repository intentionally does **not** include:

- proprietary Triton kernel implementations;
- proprietary sparse-local attention source code;
- proprietary routing implementations;
- internal development notebooks;
- private optimization code.

The purpose of the repository is validation and reproducibility rather than distribution of proprietary implementations.

---

# Scientific Claims

The Validation Suite supports claims regarding:

- correctness validation;
- benchmark execution;
- artifact generation;
- package integrity;
- reproducibility.

The Validation Suite does **not** support claims of:

- universal superiority over FlashAttention;
- universal superiority over SDPA;
- universal superiority over any attention implementation;
- performance outside experimentally evaluated configurations.

Performance conclusions remain limited to the benchmark domains documented in the associated research.

---

# Reproducibility

The project automatically produces:

- JSON reports
- CSV reports
- Markdown reports
- HTML reports
- SHA-256 manifests
- ZIP reproducibility packages

allowing independent verification of all published public artifacts.

---

# Intended Audience

The repository is intended for:

- researchers
- machine learning engineers
- systems researchers
- GPU kernel developers
- reviewers
- reproducibility studies

---

# Future Development

Planned future work includes:

- additional benchmark domains;
- validation on additional GPU architectures;
- expanded documentation;
- public datasets;
- integration with future scientific publications.

---

# Citation

If this repository contributes to academic work, please cite the associated publication.

Citation metadata will be provided through the included `CITATION.cff` file.

---

# License

The Validation Suite is distributed under the repository license.

The proprietary sparse-local attention kernel is **not** distributed as part of this repository.

---

# Author

**Valentino Lanzarini**

Independent Research Project

---

# Disclaimer

This repository contains a public validation and reproducibility framework together with experimentally generated public artifacts.

Its purpose is to improve transparency, reproducibility and independent verification of sparse-local attention research.

The repository should **not** be interpreted as evidence that any attention implementation is universally superior.

Experimental conclusions remain restricted to the evaluated benchmark domains documented in the associated research.
