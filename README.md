Lanzarini Validation Suite

Independent Validation and Benchmarking Framework for Sparse Local-Window Attention Kernels

---

Overview

The Lanzarini Validation Suite is an independent validation and benchmarking framework designed for sparse local-window attention kernels.

The framework was developed during the experimental validation of the proprietary Lanzarini Triton kernel and later generalized into a modular validation infrastructure that can be applied to different sparse attention implementations.

The objective of this repository is not to publish a new attention kernel.

Instead, it provides a reproducible methodology for validating numerical correctness, runtime behavior, energy consumption and empirical backend-selection strategies.

The optimized Lanzarini kernel is intentionally not included in this public repository.

---

Motivation

GPU kernel benchmarking is significantly more complex than comparing average execution times.

Reliable conclusions require:

- reproducible experiments
- numerical correctness verification
- runtime-only measurements
- blind validation
- statistical analysis
- automatic report generation
- hardware-aware evaluation

The Validation Suite was created to standardize this process.

---

Validation Scope

The current framework supports validation of:

- Environment compatibility
- Adapter contract verification
- Numerical correctness against PyTorch SDPA local-mask
- Runtime benchmarking
- NVML energy benchmarking
- Backend-selection frontier mapping
- Automatic JSON report generation
- Automatic CSV generation
- SHA-256 artifact verification
- Reproducible experiment configuration

---

Experimental Methodology

The framework follows strict engineering principles.

- No hardcoded benchmark results
- Runtime-only measured data
- No manually selected favorable cases
- Reproducible benchmark protocol
- Hardware-aware evaluation
- Blind validation whenever possible
- Automatic report generation
- Evidence-based conclusions only

Experimental conclusions are derived exclusively from measured results.

---

Current Experimental Status

Current public validation has been performed primarily on:

Hardware

- NVIDIA A100-SXM4-80GB

Precision

- FP16

Reference implementation

- PyTorch SDPA Local Mask

Comparison backends

- Proprietary Lanzarini Kernel
- FlashAttention
- PyTorch SDPA

The validation framework has been used to perform:

- correctness validation
- runtime benchmarking
- energy benchmarking
- empirical backend frontier analysis

Experimental evidence obtained on the tested configurations indicates that backend selection is better described by an empirical multi-region frontier than by a single global threshold.

These observations apply only to the tested hardware, software stack and benchmark configurations.

No universal performance claims are made.

---

Validation Pipeline

Environment Validation
        │
        ▼
Adapter Contract Verification
        │
        ▼
Numerical Correctness
        │
        ▼
Runtime Benchmark
        │
        ▼
Energy Benchmark
        │
        ▼
Backend Frontier Analysis
        │
        ▼
Automatic Reports

---

Repository Structure

validation_suite.py

configs/

modules/

docs/

examples/

results_example/

private_kernel/

---

Proprietary Components

This repository intentionally excludes the proprietary Lanzarini Triton kernel.

The directory

private_kernel/

contains only the adapter interface.

Users may connect their own sparse attention implementation without modifying the validation framework.

This design allows the validation methodology to remain public while preserving proprietary kernel implementations.

---

Generated Outputs

Typical outputs include:

- JSON reports
- CSV benchmark tables
- validation summaries
- frontier maps
- SHA-256 manifests
- reproducible experiment artifacts

---

Research Applications

The Validation Suite has been designed for research involving:

- Sparse Attention
- GPU Kernel Engineering
- Runtime Optimization
- Performance Benchmarking
- Energy-aware Evaluation
- Backend Selection
- Reproducible AI Systems Research

---

Collaboration

Research collaborations, industrial evaluations and academic discussions are welcome.

The proprietary Lanzarini kernel is available only for qualified technical evaluations under appropriate confidentiality agreements (NDA) when applicable.

---

Citation

Citation metadata is provided through:

CITATION.cff

Future scientific publications associated with this project will be referenced here.

---

License

The validation framework is distributed independently from the proprietary kernel implementation.

See the LICENSE file for repository licensing information.
