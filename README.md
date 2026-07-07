# Lanzarini Validation Suite

![Validation](https://img.shields.io/badge/Validation-PASS-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CUDA](https://img.shields.io/badge/CUDA-Tested-green)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.1-orange)
![Triton](https://img.shields.io/badge/Triton-3.0.0-orange)
![Research](https://img.shields.io/badge/Research-Reproducible-purple)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Current Status

**Repository status:** Stable

### Public Validation Progress

| Validation Stage | Status |
|------------------|--------|
| V1 | ✅ Complete |
| V2 | ✅ Complete |
| V3 | ✅ Complete |

### Current Repository Features

- ✅ Public validation reports
- ✅ Reproducibility documentation
- ✅ Artifact package builder
- ✅ Package integrity verification
- ✅ GitHub Actions continuous validation

---

This repository provides an open validation and reproducibility framework for the Lanzarini Validation Suite.

The repository intentionally excludes proprietary Triton kernel source code.

Only validated public reports, measured experimental results, and reproducibility artifacts are included.

---

# Public Validation and Reproducibility Framework for Sparse-Local Attention Research

The **Lanzarini Validation Suite** is an open scientific validation framework designed to evaluate the correctness, reproducibility and experimental integrity of sparse-local attention research.

Rather than introducing a new attention algorithm, this repository provides a transparent validation workflow that verifies publicly reproducible experimental artifacts while intentionally separating public validation from proprietary implementation details.

The Validation Suite enables researchers to inspect validation procedures, reproduce published experiments, verify generated artifacts and audit package integrity without requiring access to proprietary GPU kernel implementations.

---

# Objectives

The Validation Suite has the following goals:

- provide a transparent validation workflow;
- verify numerical correctness of public experiments;
- benchmark runtime execution under controlled conditions;
- evaluate runtime stability;
- generate reproducible experimental artifacts;
- produce machine-readable validation reports;
- verify artifact integrity through SHA-256 manifests;
- support independent scientific verification.

The repository is designed to maximize reproducibility while preserving the confidentiality of proprietary implementation details.

---

# Motivation

Experimental evaluation of GPU attention kernels is often difficult to reproduce because implementations, benchmark protocols and validation procedures are rarely published in a consistent form.

The Validation Suite addresses this problem by providing a structured validation pipeline that documents:

- execution environment;
- validation methodology;
- numerical correctness;
- runtime measurements;
- generated artifacts;
- integrity verification.

This repository focuses on scientific reproducibility rather than algorithm implementation.

---

# Problem

Modern AI systems increasingly rely on Transformer architectures for inference.

As sequence length grows, attention computation becomes one of the primary contributors to GPU execution time, memory traffic and energy consumption.

The Lanzarini Validation Suite does not introduce a new foundation model or claim a universally superior attention implementation.

Instead, it provides a transparent and reproducible experimental framework for evaluating sparse-local attention implementations under controlled benchmark conditions.

Its objective is to determine, through experimentally validated evidence, under which configurations different attention backends provide measurable advantages.

---

# Why It Matters

Even modest improvements in inference efficiency can translate into meaningful infrastructure savings when AI systems are deployed at scale.

Potential application domains include:

- Large Language Models (LLMs)
- AI inference infrastructure
- GPU inference engines
- Edge AI
- Vision Transformers
- Speech AI
- Robotics
- Long-sequence scientific computing
- Time-series AI
- Scientific AI workloads

Rather than promoting a specific implementation, the Validation Suite emphasizes transparent measurement, reproducibility and independent verification.

---

# Repository at a Glance

The public repository provides a transparent validation and reproducibility framework designed to facilitate independent scientific verification of sparse-local attention research.

Current public capabilities include:

- ✅ Public validation and reproducibility framework
- ✅ Reproducible validation workflow
- ✅ Machine-readable validation artifacts (JSON, CSV, Markdown and HTML)
- ✅ SHA-256 artifact integrity verification
- ✅ Continuous validation through GitHub Actions
- ✅ Configuration-specific experimental evidence
- ✅ Public documentation and reproducibility reports

The proprietary sparse-local attention kernel implementation and backend-selection logic are intentionally excluded from the public repository.

The Validation Suite focuses on reproducibility, transparency and independent verification of experimentally validated public artifacts rather than distribution of proprietary implementation details.

---

# Quick Start

The public Validation Suite can be executed in only a few minutes.

Clone the repository:

```bash
git clone https://github.com/vlanzarini80-source/Lanzarini-Validation-Suite

cd Lanzarini-Validation-Suite
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the public validation workflow:

```bash
python scripts/v1a_environment_check.py
python scripts/v1b_adapter_contract.py
python scripts/v1c_micro_correctness.py
python scripts/v1d_runtime_benchmark.py
python scripts/v1e_artifact_manifest.py
python scripts/v1f_report_generator.py
```

The Validation Suite automatically generates reproducible public artifacts including:

- JSON validation reports
- CSV benchmark tables
- Markdown reports
- HTML reports
- SHA-256 integrity manifests

Generated artifacts are written to:

```text
results/json/
results/csv/
results/reports/
```

The public repository intentionally excludes the proprietary sparse-local attention implementation.

Instead, it enables independent verification of the published validation workflow, benchmark methodology, reproducibility pipeline and artifact integrity.

---

# Experimental Highlights

The Validation Suite summarizes experimentally validated benchmark campaigns performed on the corresponding hardware configurations.

Representative experimentally validated observations include:

| Experiment | Representative Result |
|------------|----------------------|
| Energy per token vs FlexAttention | Up to **22.6% lower** in the tested configuration |
| Throughput vs FlexAttention | Up to **25.5% higher** in the tested configuration |
| FlashAttention comparison | **Backend selection is experimentally regime-dependent** |
| Long-context evaluation | **Different scaling behaviour observed across tested backends** |
| Validation Suite | Reproducible JSON, CSV, Markdown, HTML reports and SHA-256 integrity manifests |

### What Can Be Independently Verified?

Using the public Validation Suite, researchers can independently verify:

- execution environment detection;
- software configuration;
- public validation workflow;
- public benchmark execution;
- validation artifact generation;
- report generation;
- SHA-256 integrity verification;
- reproducibility of the published validation pipeline.

The proprietary sparse-local attention implementation remains intentionally private and is therefore outside the scope of the public repository.

> **Important**
>
> All reported measurements are configuration-specific and limited to the experimentally validated benchmark conditions.
>
> Performance depends on factors including sequence length, attention window, hardware platform and software stack.
>
> Different attention backends may perform better under different experimentally evaluated regimes.
>
> The Validation Suite provides reproducible experimental evidence and does **not** claim universal performance, energy or cost superiority of any implementation.

### Experimental Summary

The repository contains experimentally generated validation artifacts, benchmark summaries and reproducibility reports intended to facilitate independent scientific verification.

All performance conclusions should be interpreted together with the corresponding benchmark configuration, validation reports and published experimental artifacts.

---

# Design Philosophy

The Validation Suite follows four guiding principles:

1. **Transparency** — every published validation artifact is generated by documented validation scripts.

2. **Reproducibility** — experiments are designed to be repeatable under comparable hardware and software configurations.

3. **Integrity** — generated artifacts are tracked through SHA-256 manifests to support verification after publication.

4. **Separation of Concerns** — public validation infrastructure is intentionally separated from proprietary kernel implementations.

---

# Scope

This repository provides the public validation component of the broader Lanzarini research project.

Included in this repository:

- validation scripts;
- validation reports;
- benchmark summaries;
- reproducibility artifacts;
- integrity manifests;
- documentation.

Not included:

- proprietary Triton kernels;
- proprietary sparse-local attention implementations;
- proprietary backend routing logic;
- internal development code.

The public validation framework is designed so that published experimental evidence can be independently verified without exposing proprietary source code.

---

# Validation Pipeline

The Validation Suite follows a sequential validation workflow.

Each stage verifies a specific aspect of the experimental pipeline before the next stage is executed. This staged approach helps ensure that published artifacts are internally consistent, reproducible and integrity checked.

```text
V1A
 │
 ▼
V1B
 │
 ▼
V1C
 │
 ▼
V1D
 │
 ▼
V1E
 │
 ▼
V1F
```

Each stage produces public artifacts that are stored inside the repository and can be independently inspected.

---

# Current Validation Stages

| Stage | Purpose | Public Status |
|--------|---------|---------------|
| V1A | Environment and software validation | ✅ Published |
| V1B | Adapter interface validation | ✅ Published |
| V1C | Micro numerical correctness validation | ✅ Published |
| V1D | Runtime smoke benchmark | ✅ Published |
| V1E | Artifact manifest and SHA-256 integrity audit | ✅ Published |
| V1F | Automatic validation report generation | ✅ Published |


## Current Development Status

**Version 1 — Completed**

Version 1 established the public validation framework, documentation, reproducibility pipeline, and continuous integration.

**Version 2 — In Progress**

Current work focuses on extending validation planning, structured reporting, reproducibility documentation, artifact traceability, and repository quality.

Only experimentally verified work is presented as completed.

---

# Stage Descriptions

## V1A — Environment Validation

Validates the execution environment before any benchmark is executed.

Checks include:

- Python version
- CUDA availability
- GPU detection
- PyTorch version
- Triton installation
- FlashAttention availability
- Adapter availability

This stage performs **no benchmark execution**.

---

## V1B — Adapter Contract Validation

Verifies that the public validation interface correctly communicates with the private implementation without exposing proprietary source code.

The adapter contract is validated independently of runtime performance.

---

## V1C — Micro Correctness Validation

Performs numerical correctness validation using small controlled test configurations.

Outputs include:

- JSON summary
- CSV validation rows
- CSV error report

The objective is to verify numerical agreement against the selected public reference implementation.

---

## V1D — Runtime Smoke Validation

Runs lightweight runtime measurements to verify that benchmark execution is functioning correctly.

This stage is intentionally limited and **does not represent a complete performance benchmark**.

Outputs include:

- runtime summary
- CSV measurements
- runtime error report

---

## V1E — Artifact Integrity Audit

Generates a complete inventory of public validation artifacts.

For every published artifact the suite records:

- file type
- size
- modification timestamp
- SHA-256 checksum

This stage supports long-term reproducibility and integrity verification.

---

## V1F — Validation Report Generator

Automatically generates consolidated validation reports from previously validated public artifacts.

Generated reports include:

- Markdown report
- HTML report
- JSON summary

The report generator does **not** execute new benchmarks.

---

# Repository Structure

```text
lanzarini-validation-suite/

README.md
LICENSE
CHANGELOG.md
CITATION.cff
requirements.txt
pyproject.toml

scripts/
artifacts/
results/
docs/
examples/
figures/
```

---

# Public Artifacts

The repository publishes machine-readable validation artifacts including:

- JSON reports
- CSV reports
- Markdown reports
- HTML reports
- SHA-256 manifests

These artifacts allow independent inspection of the published validation workflow without requiring access to proprietary implementation details.

---

# Validation Outputs

Validation results are written to the following directories:

```text
results/json/
results/csv/
results/reports/
```

Integrity manifests are stored separately to facilitate long-term verification of published artifacts.

---

# How to Run

Clone the repository and execute the validation stages sequentially from the repository root.

```bash
python scripts/v1a_environment_check.py
python scripts/v1b_adapter_contract.py
python scripts/v1c_micro_correctness.py
python scripts/v1d_runtime_benchmark.py
python scripts/v1e_artifact_manifest.py
python scripts/v1f_report_generator.py
```

Generated public artifacts are written to:

```text
results/json/
results/csv/
results/reports/
```

The Validation Suite is designed so that the public validation workflow can be executed independently of the proprietary kernel implementation.

---

# Scientific Scope

The Validation Suite validates:

- execution environment;
- numerical correctness;
- runtime benchmark execution;
- runtime stability;
- validation artifact generation;
- SHA-256 integrity verification;
- reproducibility workflow.

The Validation Suite **does not** validate:

- theoretical optimality;
- universal algorithmic superiority;
- mathematical proofs;
- performance outside experimentally evaluated configurations.

Any performance conclusions remain limited to the benchmark domains represented by the published validation artifacts.

---

# Backend Evaluation Scope

The Validation Suite evaluates experimentally measured performance under specific benchmark configurations.

Different attention backends may perform better under different experimentally evaluated regimes depending on sequence length, attention window, hardware platform and software stack.

The purpose of the Validation Suite is to provide reproducible measurements and validation artifacts rather than to demonstrate universal performance superiority of any implementation.

Whenever backend comparisons are published, conclusions remain limited to the measured benchmark configurations represented by the associated validation artifacts.

---

# Reproducibility

Every published validation stage generates machine-readable artifacts.

Depending on the stage, these may include:

- JSON reports;
- CSV measurement tables;
- Markdown reports;
- HTML reports;
- SHA-256 manifests.

These artifacts allow independent verification of the published validation workflow.

---

# Intended Audience

This repository is intended for:

- machine learning researchers;
- GPU systems researchers;
- kernel developers;
- reproducibility studies;
- academic reviewers;
- engineers interested in experimental validation methodologies.

---

# Relationship to the Research Project

The Validation Suite represents the **public validation component** of the broader Lanzarini research project.

The broader research effort includes additional work on sparse-local attention, runtime optimization and backend-selection strategies.

Those research components are intentionally maintained separately from this repository.

---

# Repository Status

Current public release:

**Version 1.0.0**

Current development phase:

- ✅ Version 1 — Completed
- 🚧 Version 2 — In Progress

Current repository capabilities:

- public validation workflow;
- validation artifacts;
- reproducibility documentation;
- SHA-256 integrity verification;
- GitHub Actions continuous integration.

Future releases will extend the Validation Suite through additional publicly reproducible validation stages and documentation.

---

# Citation

If this repository contributes to academic work, please cite the associated publication when available.

Citation metadata is maintained through the included `CITATION.cff` file.

---

# Guiding Principle

Every public statement in this repository is evidence-based.

Measured results are clearly separated from planned work.

Future work is explicitly identified as future work.

Only experimentally verified results are presented as completed. 

---

# License

This repository distributes the public Validation Suite only.

The proprietary sparse-local attention implementation is **not** included in this repository.

Please refer to the repository license for usage conditions.

---

# Author

**Valentino Lanzarini**

Independent Research Project

GitHub:
https://github.com/vlanzarini80-source

Contact:

valentino.lanzarini80@gmail.com

---

# Disclaimer

This repository provides a public scientific validation and reproducibility framework together with experimentally generated validation artifacts.

Its purpose is to improve transparency, reproducibility and independent verification of sparse-local attention research.

Nothing in this repository should be interpreted as demonstrating universal superiority of any attention implementation.

Scientific conclusions remain limited to the benchmark configurations documented by the published validation artifacts.

---

© 2026 Valentino Lanzarini. All rights reserved.
