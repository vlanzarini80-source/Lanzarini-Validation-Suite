# Lanzarini Validation Suite

## Overview

The Lanzarini Validation Suite is an independent validation and benchmarking framework for sparse local-window attention kernels.

Its purpose is to provide a reproducible methodology for evaluating correctness, runtime performance, energy consumption and empirical backend-selection frontiers.

This repository contains only the validation infrastructure.

The proprietary Lanzarini kernel is **not included**.

---

## Scope

The suite currently validates:

- Environment compatibility
- Numerical correctness against PyTorch SDPA local-mask
- Runtime benchmarking
- Energy benchmarking
- Backend frontier mapping
- Automatic report generation

---

## Design Principles

- No hardcoded benchmark results
- Runtime-only measurements
- Reproducible experiments
- Hardware-aware evaluation
- SHA-256 artifact verification
- Modular validation pipeline

---

## Repository Structure

```
validation_suite.py
configs/
modules/
docs/
examples/
results_example/
private_kernel/
```

---

## Proprietary Components

This public repository intentionally excludes the proprietary Lanzarini kernel.

The folder

```
private_kernel/
```

contains only the adapter interface.

Users may connect their own implementation without modifying the validation framework.

---

## Validation Workflow

```
Environment
↓

Correctness

↓

Runtime

↓

Energy

↓

Frontier Mapping

↓

Final Report
```

---

## Supported Hardware

Current validation has been developed and tested primarily on NVIDIA A100 GPUs.

Results should be interpreted only for the tested hardware, software stack and benchmark configurations.

No universal performance claims are made.

---

## License

See LICENSE.

---

## Citation

Citation information is available in CITATION.cff.
