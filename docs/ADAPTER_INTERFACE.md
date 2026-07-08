# Adapter Interface

## Purpose

This document defines the public adapter interface used by the Lanzarini Validation Suite.

The adapter provides the software boundary between the public validation workflow and a locally available proprietary sparse-local attention implementation.

The proprietary implementation is intentionally not included in this repository.

---

## Scope

This document specifies:

- the role of the public adapter;
- the expected public interface;
- the expected input and output semantics;
- the relationship between the adapter and the mathematical specification;
- the expected behavior of the public Validation Suite when the proprietary adapter is unavailable.

This document does **not** disclose:

- proprietary kernel source code;
- implementation details;
- GPU optimization strategies;
- backend-selection logic.

---

## Adapter Role

The adapter acts as the interface between:

- the public Validation Suite;
- the proprietary sparse-local attention implementation.

Public validation scripts communicate exclusively through this interface.

The validation workflow never requires direct access to the proprietary implementation.

---

## Current Public Interface

The current public Validation Suite expects an adapter exposing a function named:

```text
selected_forward_q2
```

The function name is part of the current public interface and may evolve in future repository versions.

The adapter is expected to compute the sparse-local attention operator defined in:

```text
docs/SPECIFICATION.md
```

The internal implementation remains outside the scope of the public repository.

---

## Expected Inputs

The adapter is expected to receive tensors representing:

- query tensor (**Q**);
- key tensor (**K**);
- value tensor (**V**);
- local attention window (**W**).

Additional implementation-specific parameters may exist in the proprietary implementation.

The exact tensor layout, batch dimensions, head dimensions, supported data types and supported devices depend on the implementation and on the validation stage being executed.

Whenever benchmark artifacts are generated, the tested configuration should be documented by the corresponding validation report.

---

## Expected Output

The adapter is expected to return an output tensor representing the sparse-local attention operator defined in:

```text
docs/SPECIFICATION.md
```

The observable output semantics are evaluated during correctness validation.

---

## Public Repository Behavior

The proprietary adapter is intentionally excluded from this repository.

Therefore, when the adapter is unavailable:

- adapter availability checks may report the adapter as missing;
- interface validation may fail or be skipped depending on the validation stage;
- this behavior is expected for the public repository;
- the absence of the proprietary adapter does not invalidate the public documentation or validation artifacts.

In public-only mode, V1B may report `pass_v1b: false` when the private adapter is not available. This is an expected outcome of the public repository configuration and should not be interpreted as a failure of the public validation framework.

---

## Environment Configuration

Private validation environments may provide the adapter through the environment variable:

```text
LANZARINI_PRIVATE_KERNEL_DIR
```

When defined, the Validation Suite may use this path to locate the proprietary adapter.

When undefined, the repository should be interpreted as operating in public validation mode.

---

## Interface Stability

The public adapter interface may evolve across repository releases.

Interface changes are documented through repository versioning and the project CHANGELOG.

---

## Error Conditions

Adapter validation may report failures when:

- the adapter directory is missing;
- the adapter file is missing;
- the expected public function is unavailable;
- the expected public function is not callable;
- input tensors do not satisfy the expected interface;
- the execution environment does not satisfy the required software or hardware prerequisites.

Such failures should be interpreted according to the corresponding validation stage.

---

## Non-Goals

This document does **not** define:

- proprietary source code;
- Triton kernel implementation details;
- GPU memory layout;
- tiling strategies;
- compiler optimizations;
- backend routing logic;
- production serving architecture;
- runtime performance guarantees.

---

## Related Documentation

- `docs/SPECIFICATION.md`
- `docs/COMPLEXITY.md`
- `docs/CORRECTNESS.md`
- `paper/CLAIM_LEDGER.md`

---

## Interpretation

The adapter interface defines the public software contract used by the Validation Suite.

Its purpose is to specify how the public validation workflow interacts with a proprietary implementation while preserving implementation confidentiality.

The adapter interface should be interpreted as a software interface specification rather than a disclosure of the proprietary sparse-local attention implementation.
