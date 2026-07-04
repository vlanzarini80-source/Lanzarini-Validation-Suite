# Contributing to Lanzarini Validation Suite

Thank you for your interest in contributing to the **Lanzarini Validation Suite**.

This repository contains the **public validation and reproducibility framework** of the Lanzarini research project. Its purpose is to support transparent, reproducible and scientifically rigorous validation of sparse-local attention research while keeping proprietary kernel implementations separate.

---

# Guiding Principles

Contributions should improve one or more of the following:

- scientific reproducibility;
- numerical correctness;
- validation methodology;
- documentation quality;
- artifact integrity;
- code readability;
- maintainability.

All contributions should preserve the transparency and reproducibility goals of the project.

---

# Scope of Contributions

Contributions are welcome in areas such as:

- documentation improvements;
- reproducibility instructions;
- validation script improvements;
- reporting improvements;
- artifact verification tools;
- issue reports;
- benchmark methodology discussions;
- bug fixes related to the public validation framework.

---

# Out of Scope

This repository intentionally excludes proprietary implementation details.

Please do **not** submit:

- proprietary Triton kernel source code;
- proprietary sparse-local attention implementations;
- proprietary backend routing logic;
- confidential research material;
- unpublished internal benchmark data;
- unrelated machine learning experiments.

---

# Scientific Standards

All contributions should follow these principles:

- never invent benchmark results;
- never modify reported measurements without clear provenance;
- clearly distinguish measured data from interpretation;
- preserve reproducibility whenever possible;
- preserve SHA-256 integrity verification for generated artifacts;
- avoid unsupported claims of universal performance superiority.

Scientific rigor is more important than optimistic conclusions.

---

# Reporting Issues

When opening an issue, please include whenever applicable:

- operating system;
- Python version;
- CUDA version;
- GPU model;
- PyTorch version;
- Triton version;
- exact command executed;
- complete error message;
- relevant logs;
- relevant JSON or CSV reports.

Providing complete information helps reproduce and resolve issues more efficiently.

---

# Pull Requests

Before submitting a pull request, please ensure that:

- the proposed change is relevant to the public validation framework;
- generated artifacts are modified only when necessary;
- the motivation for the change is clearly explained;
- any impact on reproducibility is documented;
- proprietary implementation code is not included.

Whenever possible, keep pull requests focused on a single topic.

---

# Reproducibility

If a contribution changes validation outputs, please document:

- which validation stage is affected;
- which files are generated or modified;
- whether SHA-256 manifests must be regenerated;
- whether previously published artifacts remain valid.

Maintaining reproducibility is a primary objective of the project.

---

# Code Style

The project favors:

- readable Python code;
- explicit validation checks;
- deterministic behavior whenever practical;
- informative failure messages;
- minimal hidden assumptions;
- well-documented code.

Code clarity is preferred over unnecessary complexity.

---

# Research Integrity

The Lanzarini Validation Suite is intended to support rigorous experimental reporting.

Contributions should improve:

- clarity;
- correctness;
- reproducibility;
- transparency.

Contributions should **not** introduce claims or conclusions that are not supported by experimentally validated evidence.

---

# Questions

If you are unsure whether a proposed contribution fits the scope of the project, please open an issue before starting significant development.

Early discussion helps maintain the scientific consistency and long-term quality of the repository.
