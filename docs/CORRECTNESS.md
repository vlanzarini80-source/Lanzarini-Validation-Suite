# Correctness Criteria

## Purpose

This document defines what "correctness" means for the sparse-local attention operator evaluated by the Lanzarini Validation Suite.

Correctness refers exclusively to the mathematical operator specified in `docs/SPECIFICATION.md`.

It does not imply correctness of any particular implementation strategy, GPU kernel optimization, compiler transformation or hardware-specific execution.

---

## Mathematical Reference

The reference operator is the sparse-local causal attention operator defined in:

```text
docs/SPECIFICATION.md
```

The operator is fully determined by:

- the admissible key set;
- the attention score;
- the softmax normalization;
- the attention output equation.

All correctness evaluations refer to this mathematical specification.

---

## Definition of Correctness

An implementation is considered mathematically correct when it computes the same observable operator semantics as the reference specification.

Specifically, correctness requires that:

- identical inputs produce equivalent outputs;
- the causal local attention mask is respected;
- positions outside the admissible key set never contribute to the output;
- numerical differences remain consistent with expected floating-point behavior.

---

## Floating-Point Arithmetic

The Validation Suite evaluates floating-point implementations.

Therefore, numerical equality is interpreted according to standard floating-point arithmetic.

Small numerical differences caused by:

- rounding;
- accumulation order;
- compiler optimization;
- hardware implementation;
- floating-point precision;

are expected and do not necessarily indicate incorrectness.

---

## Reference Comparison

Correctness is evaluated by comparing an implementation against a reference implementation of the same mathematical operator.

The Validation Suite does not compare sparse-local attention against dense attention semantics.

Instead, both implementations must compute the same sparse-local operator under identical masking rules.

---

## Validation Outputs

Depending on the validation stage, correctness evaluation may include:

- maximum absolute error;
- relative error;
- cosine similarity;
- numerical consistency reports;
- JSON summaries;
- CSV validation tables.

The exact metrics depend on the validation stage.

---

## Scope

Correctness evaluation verifies that an implementation reproduces the mathematical behavior of the specified sparse-local attention operator.

It does not evaluate:

- runtime performance;
- energy efficiency;
- memory efficiency;
- implementation quality;
- optimization strategy.

Those properties are evaluated independently.

---

## Non-Goals

This document does **not** claim:

- universal numerical superiority;
- mathematical optimality;
- proof of implementation correctness;
- proof of hardware correctness;
- proof of software reliability outside the validated configurations.

Correctness remains limited to the mathematical operator and the experimentally validated configurations documented by the Validation Suite.

---

## Relationship to Experimental Validation

Correctness is one component of the overall validation workflow.

The Validation Suite separates:

- mathematical correctness;
- runtime evaluation;
- artifact generation;
- reproducibility;
- integrity verification.

Each property is evaluated independently to avoid conflating numerical correctness with implementation performance.

---

## Interpretation

Within the Lanzarini Validation Suite, correctness means agreement with the mathematical specification of the sparse-local attention operator.

It should not be interpreted as a guarantee of runtime performance, implementation quality, or superiority over alternative attention implementations.
