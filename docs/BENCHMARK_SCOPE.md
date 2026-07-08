# Benchmark Scope

## Purpose

This document defines the scope of the experimental benchmarks reported by the Lanzarini Validation Suite.

Its purpose is to clarify which publicly reported benchmark results are supported by experimental evidence and to avoid interpretations beyond the documented validation results.

---

## Scope

The Validation Suite publicly reports only benchmark results that have been experimentally executed and documented.

No publicly reported benchmark result is inferred from analytical models, theoretical estimates, or undocumented experiments.

---

## Benchmark Categories

Depending on the validation stage, benchmark categories may include:

- mathematical correctness;
- numerical consistency;
- runtime characteristics;
- reproducibility verification;
- validation artifact generation;
- integrity verification.

Each benchmark category is documented independently.

---

## Experimental Configurations

Benchmark results apply only to the documented experimental configurations.

These configurations may include:

- hardware platform;
- GPU architecture;
- software environment;
- CUDA version;
- PyTorch version;
- Triton version;
- documented benchmark parameters.

The exact configuration is reported by the corresponding validation artifacts whenever applicable.

---

## Performance Benchmarks

Performance benchmarks evaluate only the documented experimental conditions.

Reported metrics may include:

- execution time;
- throughput;
- runtime comparison;
- other documented performance metrics.

No performance claim should be interpreted beyond the tested configurations.

---

## Correctness Benchmarks

Correctness benchmarks compare the observable outputs of the evaluated operator with the corresponding documented reference implementation.

The comparison methodology is documented by the associated validation reports.

---

## Reproducibility Benchmarks

Reproducibility benchmarks verify that the documented validation workflow can generate publicly inspectable validation artifacts.

These artifacts may include:

- validation reports;
- configuration summaries;
- CSV files;
- JSON summaries;
- integrity manifests;
- reproducibility documentation.

---

## Benchmark Limitations

The reported benchmark results apply only to the documented experimental conditions.

Untested hardware platforms, software versions, workloads, model architectures, compiler configurations, or execution environments are outside the scope of the reported benchmark evidence.

---

## Out of Scope

This repository does not claim benchmark results for configurations that have not been experimentally evaluated and documented.

In particular, no claim is made regarding:

- all GPU architectures;
- all Transformer architectures;
- all software versions;
- all compiler implementations;
- all workloads;
- universal performance behavior.

---

## Future Benchmark Extensions

Future revisions of the Validation Suite may include additional benchmark categories, hardware platforms, software environments, workloads, and experimental protocols as new experimental evidence becomes available.
