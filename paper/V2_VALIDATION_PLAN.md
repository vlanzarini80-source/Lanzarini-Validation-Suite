V2 Validation Plan

Purpose

This document defines the planned scope of Version 2 of the Lanzarini Validation Suite.

The goal of V2 is to extend the public validation framework while keeping a strict separation between public reproducibility artifacts and proprietary implementation details.

No proprietary kernel implementation is included in this repository.

V1 Public Baseline

Version 1 established the public validation framework for sparse-local attention research.

The public V1 repository includes:

- repository organization;
- public documentation;
- validation scripts;
- JSON reports;
- CSV reports;
- Markdown reports;
- HTML reports;
- SHA-256 artifact manifest;
- GitHub Actions continuous integration;
- GitHub Release v1.0.0.

V1 is considered the public organizational and reproducibility baseline.

Primary Public Validation Platform

The public Validation Suite is centered on the following validated platform:

- NVIDIA A100-SXM4-80GB;
- Python 3.11;
- PyTorch 2.4.1+cu124;
- Triton 3.0.0;
- FlashAttention 2.8.3.post1;
- CUDA-enabled Linux environment.

Previous internal validation also included NVIDIA H100 and Tesla T4, but the public V2 documentation should remain centered on the published A100 validation workflow unless additional public artifacts are released.

V1 Public Validation Stages

The public validation workflow includes:

- environment verification;
- adapter contract verification;
- micro correctness validation;
- runtime smoke benchmark;
- artifact manifest generation;
- automatic validation report generation;
- repository integrity checks through GitHub Actions.

Current public V1 status:

Stage| Status
V1A| PASS
V1B| PASS
V1C| PASS
V1D| PASS
V1E| PASS
V1F| PASS

V2 Objective

V2 is planned as a documentation and extended validation phase.

V2 should improve:

- validation planning;
- structured report generation;
- artifact traceability;
- reproducibility documentation;
- public evidence organization;
- separation between completed results and future work.

V2 is not yet complete.

Planned V2 Work

1. Structured Validation Reports

V2 should define a standard report format for future validation results.

Each report should include:

- experiment name;
- validation status;
- date;
- hardware;
- software environment;
- benchmark configuration;
- validation type;
- public artifacts;
- pass/fail criteria;
- known limitations.

2. Evidence-Based Public Results

Only experimentally verified results may be marked as completed.

Unverified work must be clearly labeled as:

- planned;
- in progress;
- experimental;
- not yet validated.

3. Artifact Integrity

V2 should continue using:

- SHA-256 manifests;
- artifact inventories;
- public integrity audits;
- GitHub version control;
- release-based archival.

4. Documentation Improvements

V2 should update the public documentation to make clear:

- what has already been validated;
- what remains planned;
- which artifacts are public;
- which implementation details are intentionally excluded;
- how external readers can interpret the validation reports.

5. GitHub Actions Improvements

V2 may extend GitHub Actions to check:

- required documentation files;
- report templates;
- JSON syntax;
- Python syntax;
- repository structure;
- artifact directory consistency.

These automated checks support repository quality, but they should not be presented as scientific validation by themselves.

Public Evidence

Public evidence may include:

- GitHub repository history;
- GitHub Actions logs;
- validation reports;
- release notes;
- artifact manifests;
- public documentation.

Only non-sensitive logs and artifacts should be published.

Known Limitations

Current public limitations include:

- validation is limited to published benchmark configurations;
- no claim of universal superiority over FlashAttention or SDPA;
- proprietary Triton kernel implementation is intentionally excluded;
- V2 and later validation stages remain under development;
- performance conclusions are limited to experimentally validated configurations;
- independent external review is still required.

Out of Scope for V2

V2 does not require publishing proprietary Triton kernel source code.

V2 does not claim production readiness.

V2 does not claim universal performance superiority.

V2 does not replace peer review.

V2 does not convert planned experiments into completed results.

Completion Criteria

V2 can be marked as completed only when:

- V2 documentation exists;
- validation report templates exist;
- README and ROADMAP correctly reference V2;
- GitHub Actions checks remain passing;
- public claims are aligned with available evidence;
- no proprietary implementation details are disclosed.

Current Status

V2 status: planned / in progress.

V2 is not yet complete.
