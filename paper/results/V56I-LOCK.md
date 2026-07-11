# V56I-LOCK — Corrected Boundary Router Validation

## Purpose

This checkpoint evaluated the corrected backend-selection rule after the boundary analysis performed in V56H-LOCK.

The objective was to verify whether the remaining routing error could be eliminated within the tested boundary configurations.

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Corrected Router Rule

```text
if T <= 15360 and W <= 192:
    use Lanzarini G4

elif T == 16384:
    use FlashAttention

elif 16384 < T <= 19456 and W == 64:
    use Lanzarini G4

else:
    use FlashAttention
```

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

## Preserved Results

| Metric | Value |
|--------|------:|
| Validation | PASS |
| Correctness | PASS |
| Accuracy | 100% |
| Mean regret | 0.0% |
| Median regret | 0.0% |
| Maximum regret | 0.0% |
| Failures | 0 |

---

## Runtime Summary

| Metric | Value |
|--------|------:|
| Router total time | 0.412186 ms |
| Always Flash | 0.451132 ms |
| Always G4 | 0.425675 ms |

---

## Measured Speedup

| Comparison | Improvement |
|------------|------------:|
| vs Always FlashAttention | 8.63% |
| vs Always Lanzarini G4 | 3.17% |

---

## Interpretation

Within the evaluated boundary configurations, the corrected routing rule matched the experimentally observed fastest backend for every tested shape.

No routing failures were observed on this validation set.

---

## Scope

These results apply only to the tested boundary configurations.

They do not establish:

- universal router correctness;
- performance outside the tested operating region;
- correctness on different GPUs or head dimensions.

---

## Archived Runtime Path

```text
/workspace/lanzarini_v35/runtime_results/
v56i_lock_corrected_boundary_validation/
```

The runtime path records the original execution location.

It does not by itself prove that the original byte-identical JSON artifact is currently included in the public repository.
