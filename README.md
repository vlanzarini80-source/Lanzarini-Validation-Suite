# Lanzarini Validation Suite

![Validation](https://img.shields.io/badge/Validation-PASS-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CUDA](https://img.shields.io/badge/CUDA-Tested-green)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.1-orange)
![Triton](https://img.shields.io/badge/Triton-3.0.0-orange)
![Research](https://img.shields.io/badge/Research-Reproducible-purple)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Table of Contents

- [Current Status](#current-status)
- [Repository Scope](#repository-scope)
- [Documentation](#documentation)
- [Scientific Positioning](#scientific-positioning)
- [Research Claims](#research-claims)
- [Evidence Policy](#evidence-policy)
- [Objectives](#objectives)
- [Motivation](#motivation)
- [Repository at a Glance](#repository-at-a-glance)
- [Quick Start](#quick-start)
- [Experimental Results and Checkpoints](#experimental-results-and-checkpoints)
- [Validation Pipeline](#validation-pipeline)
- [Repository Structure](#repository-structure)
- [Scientific Scope](#scientific-scope)
- [Backend Evaluation Scope](#backend-evaluation-scope)
- [Reproducibility](#reproducibility)
- [Citation](#citation)
- [License](#license)

---

## Current Status

**Repository Status:** Stable

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
- ✅ SHA-256 integrity verification
- ✅ GitHub Actions continuous validation

---

## Repository Scope

This repository is exclusively dedicated to the public validation and reproducibility framework for sparse-local attention research conducted within the Lanzarini Validation Suite.

It documents the mathematical operator, public validation methodology, experimental evidence, reproducibility workflow, and validation artifacts associated with this research.

This repository does **not** include, describe, validate, or support unrelated research projects, mathematical models, or experimental hypotheses that may exist in separate repositories maintained by the same author.

Any reference to other repositories should be considered independent unless explicitly stated in this repository. 

---

## Documentation

The technical documentation for the public Validation Suite is available in the `docs/` directory.

| Document | Purpose |
|----------|---------|
| [`SPECIFICATION.md`](docs/SPECIFICATION.md) | Mathematical specification of the sparse-local attention operator. |
| [`COMPLEXITY.md`](docs/COMPLEXITY.md) | Computational complexity of the documented operator. |
| [`CORRECTNESS.md`](docs/CORRECTNESS.md) | Correctness criteria used during validation. |
| [`ADAPTER_INTERFACE.md`](docs/ADAPTER_INTERFACE.md) | Public adapter interface specification. |
| [`VALIDATION_METHODOLOGY.md`](docs/VALIDATION_METHODOLOGY.md) | Public validation methodology. |
| [`BENCHMARK_SCOPE.md`](docs/BENCHMARK_SCOPE.md) | Scope of reported benchmark evidence. |
| [`LIMITATIONS.md`](docs/LIMITATIONS.md) | Known limitations and interpretation boundaries. |

---

## Experimental Results and Checkpoints

The repository includes public summaries of selected experimental checkpoints from the Lanzarini sparse-local attention research program.

These reports document preserved measurements, correctness outcomes, benchmark observations, methodological corrections, and known limitations.

The proprietary Triton implementation is not included.

### Consolidated Results

- [`paper/RESULTS.md`](paper/RESULTS.md) — consolidated experimental results, including V52D-R2-FIX, V56A blind-router validation, and V56B-LITE transition-band measurements.
- [`paper/VALIDATION_OVERVIEW.md`](paper/VALIDATION_OVERVIEW.md) — high-level overview of the public validation workflow.

### Individual Checkpoint Reports

| Checkpoint | Experimental topic | Public report |
|---|---|---|
| V42D-A-R | Native vLLM integration validation | [`V42D-A-R.md`](paper/results/V42D-A-R.md) |
| V43A | End-to-end adapter performance and reconstruction bottleneck | [`V43A.md`](paper/results/V43A.md) |
| V44A-2M | Micro paged-native reference correctness audit | [`V44A-2M.md`](paper/results/V44A-2M.md) |
| V48A-2R | NVML sparse-local energy repeat-loop audit | [`V48A-2R.md`](paper/results/V48A-2R.md) |
| V52D-R2-FIX | Corrected Lanzarini G4 vs FlashAttention benchmark | [`V52D-R2-FIX.md`](paper/results/V52D-R2-FIX.md) |
| V56G-R | Corrected blind-router validation | [`V56G-R.md`](paper/results/V56G-R.md) |
| V56H-LOCK | Boundary validation | [`V56H-LOCK.md`](paper/results/V56H-LOCK.md) |
| V56I-LOCK | Corrected boundary-router validation | [`V56I-LOCK.md`](paper/results/V56I-LOCK.md) |
| V57C | FlashAttention correctness validation against SDPA | [`V57C.md`](paper/results/V57C.md) |
| V58A | FlashAttention vs Lanzarini head-to-head benchmark | [`V58A.md`](paper/results/V58A.md) |
| V58B | Measured backend-winner extraction | [`V58B.md`](paper/results/V58B.md) |
| V59A | Interpretable backend-router learning | [`V59A.md`](paper/results/V59A.md) |
| V60A-LITE | Dense empirical frontier sweep | [`V60A-LITE.md`](paper/results/V60A-LITE.md) |
| V61B | Two-dimensional frontier interpretation | [`V61B.md`](paper/results/V61B.md) |

### Interpretation

The checkpoint reports contain different levels of preserved evidence.

Some reports include row-level numerical measurements, while others contain only preserved experimental summaries because the original byte-identical JSON or CSV artifacts have not yet been recovered or published.

Each report states its own evidence scope and limitations.

The reported results:

- apply only to the documented experimental configurations;
- do not establish universal performance or energy superiority;
- do not demonstrate generalization to untested hardware or workloads;
- do not expose the proprietary kernel implementation.

---

## Scientific Positioning

This repository documents a public validation and reproducibility framework for a sparse-local attention operator.

The mathematical operator documented in this repository follows the standard sparse-local (sliding-window) causal attention formulation.

This repository does **not** claim the introduction of a novel sparse-local attention operator or mathematical formulation.

Instead, the primary contribution of this repository is the development of a public framework for:

- rigorous validation;
- experimental reproducibility;
- correctness evaluation;
- benchmark documentation;
- transparent reporting of experimentally observed results.

The proprietary implementation remains outside the scope of this public repository.

No claim is made that the mathematical formulation presented in this repository is novel.

---

## Research Claims

This repository makes only limited, evidence-based claims.

### What this repository claims

This repository claims that it provides:

- a public validation and reproducibility framework for sparse-local attention research;
- a documented mathematical specification of the evaluated operator;
- public validation scripts and artifacts;
- documented correctness, complexity, benchmark scope, and limitation statements;
- a reproducibility-oriented workflow for inspecting reported experimental evidence.

### What this repository does not claim

This repository does **not** claim:

- a novel mathematical attention formulation;
- universal performance superiority;
- universal energy savings;
- correctness outside documented validation conditions;
- benchmark validity outside experimentally evaluated configurations;
- disclosure of the proprietary implementation.

All performance, correctness, and reproducibility statements should be interpreted only within the scope documented in the validation artifacts and technical documentation.

For a claim-by-claim mapping between scientific statements, supporting evidence, limitations, and validation status, see [`paper/CLAIM_LEDGER.md`](paper/CLAIM_LEDGER.md).

---

## Evidence Policy

This repository follows an evidence-based documentation policy.

Scientific claims are made only when supported by publicly documented experimental evidence.

Accordingly, the repository adopts the following principles:

- benchmark results are reported only for experimentally evaluated configurations;
- undocumented experiments are not used to support scientific claims;
- theoretical expectations are clearly distinguished from experimental observations;
- future work is explicitly distinguished from validated results.

The absence of a claim should not be interpreted as evidence against a particular result. It indicates only that no publicly documented experimental evidence is currently provided in this repository for that specific claim.

---

# Public Validation and Reproducibility Framework for Sparse-Local Attention Research

The **Lanzarini Validation Suite** is an open scientific validation framework designed to improve transparency, reproducibility and independent verification of sparse-local attention research.

Rather than introducing a new attention algorithm or a new foundation model, the repository provides a structured validation workflow that enables publicly reproducible experimental validation while intentionally separating public validation infrastructure from proprietary implementation details.

The Validation Suite enables researchers, engineers and reviewers to inspect validation procedures, reproduce published validation artifacts, verify benchmark outputs and audit package integrity without requiring access to proprietary GPU kernel implementations.

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

The Validation Suite addresses this problem by providing a structured validation pipeline documenting:

- execution environment;
- validation methodology;
- numerical correctness;
- runtime measurements;
- generated artifacts;
- integrity verification.

The repository focuses on scientific reproducibility rather than algorithm implementation.

---

# Problem

Modern AI systems increasingly rely on Transformer architectures for inference.

As sequence length grows, attention computation becomes one of the primary contributors to GPU execution time, memory traffic and energy consumption.

The Lanzarini Validation Suite does **not** introduce a new foundation model and does **not** claim a universally superior attention implementation.

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

## Quick Start

Clone the repository:

```bash
git clone https://github.com/vlanzarini80-source/Lanzarini-Validation-Suite.git
cd Lanzarini-Validation-Suite
```

Run the public validation stages:

```bash
python scripts/scripts/v1a_environment_check.py
python scripts/scripts/v1b_adapter_contract.py
python scripts/scripts/v1c_micro_correctness.py
python scripts/scripts/v1d_runtime_benchmark.py
python scripts/scripts/v1e_artifact_manifest.py
python scripts/scripts/v1f_report_generator.py
```

Expected public-mode behavior:

- **V1A** → PASS
- **V1B** → PASS or SKIPPED_PUBLIC_MODE (depending on whether a proprietary adapter is available)
- **V1C** → SKIPPED_PUBLIC_MODE (without the proprietary adapter)
- **V1D** → SKIPPED_PUBLIC_MODE (without the proprietary adapter)
- **V1E** → PASS
- **V1F** → PASSED (`PUBLIC_VALIDATION_COMPLETE: True`)

> **Public Repository Note**
>
> The proprietary sparse-local attention kernel and its adapter are intentionally excluded from the public repository.
>
> Therefore:
>
> - **V1A** can be executed directly.
> - **V1B** validates the public adapter contract against the proprietary implementation and therefore requires a locally available private adapter.
> - If the private adapter is not available, V1B may be skipped or report that the adapter is missing. This behaviour is expected for the public repository.
> - The remaining public validation stages operate exclusively on publicly available validation artifacts and documentation.

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

# Public Mode

The public repository validates the validation framework itself.

The proprietary Triton kernel is intentionally excluded.

When the proprietary adapter is not available:

• V1A and V1E execute normally.
• V1B may PASS or SKIPPED_PUBLIC_MODE.
• V1C and V1D are expected to report SKIPPED_PUBLIC_MODE.
• V1F reports the public validation workflow as complete.

The public repository validates the public validation framework and its reproducibility workflow.

---

# Visual Overview

The following diagrams summarize the public Validation Suite.

*(Figures can be added as the repository evolves.)*

```text
figures/

repository_architecture.png
validation_pipeline.png
public_vs_private.png
experimental_results_overview.png
backend_evaluation_scope.png
```

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

---

## What Can Be Independently Verified?

Using the public Validation Suite, researchers can independently verify:

- execution environment detection;
- software configuration;
- public validation workflow;
- benchmark execution methodology;
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

---

## Experimental Summary

The repository contains experimentally generated validation artifacts, benchmark summaries and reproducibility reports intended to facilitate independent scientific verification.

All performance conclusions should always be interpreted together with the corresponding benchmark configuration, validation reports and published experimental artifacts.

---

# Design Philosophy

The Validation Suite follows four guiding principles:

1. **Transparency** — every published validation artifact is generated through documented validation scripts and reproducible procedures.

2. **Reproducibility** — experiments are designed to be repeatable under comparable hardware and software configurations.

3. **Integrity** — generated artifacts are tracked through SHA-256 manifests to support long-term verification.

4. **Separation of Concerns** — the public validation infrastructure is intentionally separated from proprietary implementation details.

These principles ensure that published evidence can be independently verified without exposing proprietary GPU kernel source code.

---

# Scope

The Validation Suite represents the **public validation component** of the broader Lanzarini research project.

### Included

- Public validation scripts
- Validation reports
- Benchmark summaries
- Machine-readable artifacts
- Reproducibility documentation
- SHA-256 integrity manifests

### Not Included

- Proprietary Triton kernel implementations
- Proprietary sparse-local attention kernels
- Proprietary backend-selection logic
- Internal research code
- Experimental development branches

The repository is intentionally designed so that scientific validation remains reproducible while proprietary implementation details remain confidential.

---

# Validation Pipeline

The Validation Suite follows a staged validation workflow.

Each validation stage verifies one component of the experimental pipeline before the following stage is executed.

```text
Environment
     │
     ▼
V1A ─ Environment Validation
     │
     ▼
V1B ─ Adapter Contract Validation*
     │
     ▼
V1C ─ Micro Correctness Validation
     │
     ▼
V1D ─ Runtime Smoke Validation
     │
     ▼
V1E ─ Artifact Integrity Audit
     │
     ▼
V1F ─ Validation Report Generator
```

\*V1B requires a locally available proprietary adapter and is optional in the public repository.

Each stage generates reproducible validation artifacts that can be independently inspected.

---

# Current Validation Stages

| Stage | Purpose | Public Status |
|--------|---------|---------------|
| V1A | Environment and software validation | ✅ Published |
| V1B | Public adapter contract validation* | ✅ Published |
| V1C | Micro numerical correctness validation | ✅ Published |
| V1D | Runtime smoke benchmark | ✅ Published |
| V1E | Artifact integrity audit | ✅ Published |
| V1F | Automatic report generation | ✅ Published |

\*Requires a locally available private adapter.

---

# Current Development Status

## Version 1 — Completed

Version 1 established the public validation framework including:

- reproducible validation workflow;
- documentation;
- validation reports;
- artifact generation;
- integrity verification;
- GitHub Actions automation.

## Version 2 — In Progress

Current work focuses on:

- improving validation coverage;
- extending reproducibility documentation;
- improving artifact traceability;
- repository quality improvements;
- additional public validation stages.

Only experimentally verified work is presented as completed.

---

# Stage Descriptions

## V1A — Environment Validation

Verifies the execution environment before benchmark execution.

Checks include:

- Python version
- CUDA availability
- GPU detection
- PyTorch installation
- Triton installation
- FlashAttention availability
- Adapter availability

This stage performs **no benchmark execution**.

---

## V1B — Adapter Contract Validation

Validates the public adapter interface used to communicate with the proprietary implementation.

When a local proprietary adapter is available, this stage verifies that the adapter exposes the expected public interface.

The proprietary implementation itself is never exposed.

In the public repository, the adapter may be absent, which is expected.

---

## V1C — Micro Correctness Validation

Performs numerical correctness validation using controlled benchmark configurations.

Outputs include:

- JSON reports
- CSV validation tables
- CSV error reports

Its objective is to verify numerical agreement with the selected reference implementation.

---

## V1D — Runtime Smoke Validation

Runs lightweight runtime measurements to verify correct benchmark execution.

This stage verifies benchmark functionality only.

It **does not** represent a comprehensive performance evaluation.

Outputs include:

- runtime summaries;
- CSV measurements;
- runtime reports.

---

## V1E — Artifact Integrity Audit

Builds an inventory of generated validation artifacts.

For every published artifact the suite records:

- filename;
- file type;
- size;
- modification timestamp;
- SHA-256 checksum.

This stage supports long-term reproducibility.

---

## V1F — Validation Report Generator

Automatically generates consolidated reports from previously validated artifacts.

Generated outputs include:

- Markdown reports;
- HTML reports;
- JSON summaries.

This stage does **not** execute new benchmarks.

---

# Repository Structure

```text
Lanzarini-Validation-Suite/

README.md
LICENSE
CHANGELOG.md
ROADMAP.md
CITATION.cff
requirements.txt
pyproject.toml

.github/
scripts/
docs/
paper/
reports/
artifacts/
results/
examples/
figures/
json/
```

---

# Public Artifacts

The repository publishes machine-readable validation artifacts including:

- JSON reports
- CSV reports
- Markdown reports
- HTML reports
- SHA-256 integrity manifests

These artifacts allow independent inspection of the published validation workflow without requiring access to proprietary implementation details.

---

# Validation Outputs

Generated public artifacts are stored under:

```text
results/json/
results/csv/
results/reports/
```

Integrity manifests are stored separately to facilitate long-term verification and reproducibility.

---

# Scientific Scope

The Validation Suite experimentally validates:

- execution environment;
- numerical correctness;
- runtime benchmark execution;
- runtime stability;
- validation artifact generation;
- SHA-256 integrity verification;
- reproducibility workflow.

The Validation Suite does **not** validate:

- theoretical optimality;
- universal algorithmic superiority;
- mathematical proofs;
- performance outside experimentally evaluated configurations.

Any scientific conclusion remains limited to the benchmark domains represented by the published validation artifacts.

---

# Backend Evaluation Scope

The Validation Suite evaluates experimentally measured performance under specific benchmark configurations.

Measured results demonstrate that different attention backends may perform better under different experimentally evaluated regimes depending on factors including:

- sequence length;
- attention window;
- hardware platform;
- software stack;
- benchmark methodology.

Accordingly, the purpose of the Validation Suite is to provide reproducible measurements and validation artifacts rather than demonstrate universal performance superiority of any implementation.

Whenever backend comparisons are presented, conclusions remain limited to the experimentally validated benchmark configurations represented by the associated public validation artifacts.

---

# Reproducibility

Every published validation stage generates machine-readable artifacts.

Depending on the stage, these may include:

- JSON reports;
- CSV measurement tables;
- Markdown reports;
- HTML reports;
- SHA-256 integrity manifests.

These artifacts enable independent verification of the published validation workflow.

---

# Intended Audience

This repository is intended for:

- machine learning researchers;
- GPU systems researchers;
- kernel developers;
- reproducibility studies;
- academic reviewers;
- AI infrastructure engineers;
- engineers interested in experimental validation methodologies.

---

# Relationship to the Research Project

The Validation Suite represents the **public validation component** of the broader Lanzarini research project.

The broader research effort includes additional work on:

- sparse-local attention;
- runtime optimization;
- backend-selection strategies;
- proprietary GPU kernel engineering.

Those research components are intentionally maintained separately from this public repository.

---

# Repository Status

Current public release:

**Version 1.0.0**

Current development phase:

- ✅ Version 1 — Completed
- 🚧 Version 2 — In Progress

Current repository capabilities include:

- public validation workflow;
- validation artifacts;
- reproducibility documentation;
- SHA-256 integrity verification;
- GitHub Actions continuous integration.

Future releases will extend the Validation Suite through additional publicly reproducible validation stages and documentation.

---

## Scientific Claims

For a claim-by-claim mapping between scientific statements, supporting evidence, limitations and validation status, see [`paper/CLAIM_LEDGER.md`](paper/CLAIM_LEDGER.md).

---

# Citation

If this repository contributes to academic work, please cite the associated publication when available.

Citation metadata is maintained through the included **CITATION.cff** file.

---

# Guiding Principle

Every public statement contained in this repository is evidence-based.

Measured experimental results are clearly separated from planned work.

Future work is explicitly identified as future work.

Only experimentally validated results are presented as completed.

---

# License

This repository distributes the **public Validation Suite only**.

The proprietary sparse-local attention implementation, backend-selection logic and GPU kernel source code are intentionally excluded.

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

Nothing contained in this repository should be interpreted as demonstrating universal superiority of any attention implementation.

All reported measurements are configuration-specific and limited to the experimentally validated benchmark conditions documented by the published validation artifacts.

The proprietary sparse-local attention implementation is intentionally excluded from the public repository.

---

© 2026 Valentino Lanzarini. All rights reserved.
