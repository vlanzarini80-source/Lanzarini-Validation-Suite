# Contributing to Lanzarini Validation Suite

Thank you for your interest in contributing to the Lanzarini Validation Suite.

This repository contains the public validation and reproducibility framework of the Lanzarini research project.

The goal of the project is to support transparent, reproducible and integrity-verified sparse-local attention research.

---

## Scope of Contributions

Contributions are welcome in the following areas:

- documentation improvements;
- reproducibility instructions;
- validation script improvements;
- reporting improvements;
- artifact verification tools;
- issue reports;
- benchmark methodology discussion.

---

## What is Outside the Scope

This repository intentionally does not include proprietary kernel implementations.

Please do not submit:

- proprietary Triton kernel source code;
- private optimization code;
- unpublished internal benchmark data;
- confidential research material;
- unrelated machine learning experiments.

---

## Scientific Standards

All contributions should follow these principles:

- do not invent benchmark results;
- do not modify reported results without clear provenance;
- clearly distinguish measured data from interpretation;
- preserve reproducibility;
- preserve SHA-256 integrity checks when modifying artifacts;
- avoid unsupported claims of universal performance superiority.

---

## Reporting Issues

When opening an issue, please include:

- operating system;
- Python version;
- CUDA version if applicable;
- PyTorch version if applicable;
- exact command used;
- full error message;
- relevant logs or report files.

---

## Pull Requests

Before opening a pull request:

1. Ensure the change is relevant to the public validation framework.
2. Avoid modifying generated artifacts unless necessary.
3. Explain why the change is needed.
4. Document any effect on reproducibility.
5. Do not include proprietary implementation code.

---

## Reproducibility

If your contribution affects validation outputs, please describe:

- which stage is affected;
- which files are generated or modified;
- whether hashes or manifests must be regenerated;
- whether previous artifacts remain valid.

---

## Code Style

The project favors:

- readable Python;
- explicit validation checks;
- clear failure messages;
- minimal hidden assumptions;
- deterministic outputs when possible.

---

## Research Integrity

The Lanzarini Validation Suite is intended to support rigorous experimental reporting.

Contributions should improve clarity, correctness or reproducibility.

They should not weaken scientific caution or introduce claims not supported by measured evidence.
