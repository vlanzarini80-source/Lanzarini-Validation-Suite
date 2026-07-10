# V56H-LOCK — Boundary Validation

## Purpose

This checkpoint investigated the boundary region identified after the corrected V56G-R blind validation.

The objective was to determine where the backend-selection rule stopped matching the experimentally observed fastest backend.

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Tested Boundary Shapes

| T | W |
|---:|---:|
|14336|192|
|15360|192|
|16384|96|
|16384|128|
|17408|64|
|17408|96|

---

## Preserved Summary

| Metric | Value |
|--------|------:|
| Accuracy | 83.33% |
| Mean regret | 0.695% |
| Failures | 1 |

---

## Observed Failure

| T | W | Router Choice | Actual Winner | Flash Advantage |
|---:|---:|---------------|---------------|----------------:|
|16384|96|Lanzarini G4|FlashAttention|4.17%|

---

## Interpretation

The boundary experiment demonstrated that the remaining routing error was concentrated around the sequence length:

```
T = 16384
```

Within the tested boundary region, FlashAttention became the experimentally observed fastest backend.

This observation motivated the corrected routing rule introduced in the following V56I-LOCK checkpoint.

---

## Scope

These conclusions apply only to the tested boundary configurations.

They do not establish:

- a universal routing rule;
- hardware-independent behavior;
- correctness outside the evaluated operating region.

---

## Archived Runtime Path

```
/workspace/lanzarini_v35/runtime_results/
v56h_lock_boundary_validation/
```

The runtime path records the original execution location.

It does not by itself prove that the original byte-identical JSON artifact is currently included in the public repository.
