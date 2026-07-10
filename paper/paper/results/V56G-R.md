# V56G-R — Corrected Blind Router Validation

## Purpose

This checkpoint reran the blind router validation using the same timing methodology as V56F-F2 in order to remove the timing-path mismatch that invalidated the original V56G experiment.

## Hardware

- GPU: NVIDIA A100-SXM4-80GB
- Timing: perf_counter
- Warmup: 5
- Runs: 10
- Inner repeats: 1000

## Preserved Results

| Metric | Value |
|--------|------:|
| Accuracy | 91.67% |
| Mean regret | ~0.419% |
| Correctness | PASS |

## Observed Failure

One tested configuration selected the wrong backend.

| T | W | Actual winner | Approximate advantage |
|---:|---:|---------------|----------------------:|
|16384|128|FlashAttention|~5%|

## Interpretation

The corrected timing methodology substantially improved router accuracy compared to the original V56G experiment.

The remaining failure identified the boundary around T=16384, motivating the dedicated boundary validation performed in V56H-LOCK.

## Limitations

The complete row-level JSON artifact is not currently available in the public repository.

Only the preserved numerical summary is reported here.

## Archived Runtime Path

```
/workspace/lanzarini_v35/runtime_results/
v56g_r_router_validation/
```
