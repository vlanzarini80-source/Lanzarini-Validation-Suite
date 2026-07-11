# Limitations

This document defines the canonical limitations of the Lanzarini Validation Suite.

It should be interpreted together with:

- `paper/METHOD.md`
- `paper/RESULTS.md`
- `docs/SPECIFICATION.md`
- `docs/CORRECTNESS.md`

Only experimentally documented evidence contained in this repository should be used to interpret the reported validation results.

## Purpose

This document summarizes the known limitations of the Lanzarini Validation Suite.

Its purpose is to define the boundaries of the reported validation results and to avoid interpretations beyond the available experimental evidence.

---

## Experimental Scope

The reported validation results apply only to the documented experimental configurations.

No claim is made for configurations that have not been experimentally evaluated.

---

## Hardware Coverage

Validation has been performed only on the hardware platforms documented in the corresponding validation reports.

The reported results should not be interpreted as representative of GPU architectures or hardware platforms that have not been experimentally evaluated.

---

## Software Coverage

Validation applies only to the documented software environment, including the reported versions of CUDA, PyTorch, Triton, and related dependencies.

Different software versions may produce different numerical or performance results.

---

## Model Coverage

Validation has been performed only on the documented workloads and model configurations.

The reported results should not be interpreted as applying to arbitrary Transformer architectures, machine learning models, or inference frameworks.

---

## Performance Results

Performance measurements are valid only for the documented experimental conditions.

No universal performance advantage is claimed.

Runtime characteristics may vary depending on hardware, software configuration, compiler behavior, workload, and execution environment.

---

## Mathematical Scope

This repository specifies and validates the mathematical behavior of the documented sparse-local attention operator.

It does not claim novelty for the general concept of sparse-local attention.

The scope of this repository is the public validation and reproducibility of the documented operator.

---

## Proprietary Implementation

The proprietary implementation is intentionally not included in this repository.

Consequently, this repository validates only the observable behavior of the operator through the documented public validation workflow.

No implementation-specific optimization strategy is disclosed.

---

## Reproducibility

The repository provides documentation and validation artifacts intended to support reproducibility.

Successful reproduction of the reported results may still depend on matching the documented hardware, software environment, and experimental configuration.

---

## Interpretation of Results

The reported validation results should not be interpreted as universal guarantees of correctness, performance, scalability, or applicability beyond the documented experimental scope.

---

## Future Work

Future revisions may extend this documentation and the associated validation evidence as additional experimental results become available.

Such extensions may include additional hardware platforms, software environments, workloads, benchmark protocols, and experimental configurations.
