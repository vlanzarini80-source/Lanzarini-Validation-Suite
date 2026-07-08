# Method

## Purpose

This document describes the methodological structure of the Lanzarini Validation Suite.

The method focuses on public validation, reproducibility, correctness evaluation, benchmark documentation, artifact generation, integrity verification, and evidence tracking.

It does not disclose proprietary implementation details.

---

## Overview

The Lanzarini Validation Suite is organized as a staged public validation workflow.

Each stage evaluates a specific aspect of the validation process, including:

- environment detection;
- adapter interface availability;
- numerical correctness;
- runtime behavior;
- artifact generation;
- report generation;
- integrity verification.

The workflow is designed to separate:

- mathematical specification;
- implementation interface;
- correctness evaluation;
- runtime measurement;
- reproducibility artifacts;
- documented limitations;
- evidence-based claims.

---

## Mathematical Operator

The evaluated operator is the sparse-local causal attention operator specified in:

```text
docs/SPECIFICATION.md
```

The operator follows the standard sparse-local sliding-window causal attention formulation.

This work does **not** claim the introduction of a novel mathematical attention operator.

---

## Public Validation Interface

The public validation workflow interacts with the evaluated implementation through the adapter interface described in:

```text
docs/ADAPTER_INTERFACE.md
```

The proprietary implementation is intentionally not included in the public repository.

The adapter interface defines the boundary between the public Validation Suite and any locally available private implementation.

---

## Correctness Methodology

Correctness is evaluated by comparing the observable output semantics of the evaluated operator against the corresponding documented reference implementation.

Correctness criteria are described in:

```text
docs/CORRECTNESS.md
```

Numerical differences are interpreted in the context of floating-point arithmetic and documented validation tolerances.

Correctness validation should not be interpreted as a guarantee of performance, scalability, or universal applicability.

---

## Runtime and Benchmark Methodology

Runtime and benchmark evidence is reported only for experimentally evaluated and documented configurations.

Benchmark scope is described in:

```text
docs/BENCHMARK_SCOPE.md
```

Performance-related results should be interpreted only within the documented experimental conditions.

No universal performance advantage is claimed.

---

## Reproducibility Methodology

The Validation Suite generates public artifacts intended to support inspection and reproducibility.

These artifacts may include:

- JSON reports;
- CSV files;
- Markdown reports;
- HTML reports;
- configuration summaries;
- SHA-256 integrity manifests.

The exact artifacts depend on the validation stage being executed.

---

## Integrity Verification

Artifact integrity is supported through SHA-256 manifests and documented artifact inventories.

Integrity verification confirms that generated artifacts can be tracked and checked after publication.

It does **not** by itself guarantee scientific validity of the underlying experimental claims.

---

## Evidence Tracking

Scientific claims are interpreted according to the evidence documented in the repository.

Claim-level interpretation is tracked in:

```text
paper/CLAIM_LEDGER.md
```

The claim ledger separates supported claims, limitations, validation status, and future work.

---

## Limitations of the Method

The method validates only the configurations that have been experimentally evaluated and documented.

It does not establish:

- universal correctness;
- universal performance superiority;
- universal energy reduction;
- applicability to all Transformer models;
- applicability to all GPU architectures;
- reproducibility outside documented environments.

Known limitations are documented in:

```text
docs/LIMITATIONS.md
```

---

## Summary

The method of the Lanzarini Validation Suite is based on staged validation, documented experimental evidence, reproducibility artifacts, integrity verification, and explicit limitation tracking.

The public method is designed to improve transparency and independent inspection of reported results while preserving the confidentiality of proprietary implementation details.
