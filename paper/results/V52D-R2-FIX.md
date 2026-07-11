# V52D-R2-FIX — Corrected Lanzarini vs FlashAttention Benchmark

## Scope

This document reports the preserved experimental results of the V52D-R2-FIX benchmark.

Only experimentally preserved results are included.

No missing runtime measurements have been reconstructed.

---

## Purpose

V52D-R2-FIX corrected the benchmarking methodology used in the previous V52D-R2 comparison.

FlashAttention tensor preparation (transpose and contiguous conversion) was performed before entering the timed benchmark loop.

This removed preparation overhead from the measured FlashAttention runtime.

The corrected experiment supersedes the original V52D-R2 benchmark for the tested configurations.

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB
- Precision: FP16
- Batch size: 1
- Attention heads: 4
- Head dimension: 64

---

## Compared Backends

- Lanzarini G4
- FlashAttention

---

## Tested Configurations

| Sequence Length | Window | Correctness | Winner |
|----------------:|--------:|------------|--------|
| 16384 | 128 | PASS | Lanzarini G4 |
| 65536 | 512 | PASS | FlashAttention |

---

## Preserved Runtime Result

For

```
T = 16384
W = 128
```

the preserved median runtimes were

| Backend | Median Runtime |
|---------|---------------:|
| Lanzarini G4 | 0.0770589467 ms |
| FlashAttention | approximately 0.0903861 ms |

Relative improvement:

```
≈ 14.74%
```

Lanzarini G4 was therefore approximately **14.74% faster** for this tested configuration.

---

## Large Sequence Result

For

```
T = 65536
W = 512
```

the preserved experiment reported:

- Correctness: PASS
- Measured winner: FlashAttention

The exact corrected latency values are not preserved and are therefore intentionally omitted.

---

## Interpretation

The corrected benchmark shows that performance depended on the tested configuration.

Observed results:

- Lanzarini G4 won at T=16384, W=128.
- FlashAttention won at T=65536, W=512.
- Correctness passed in both experiments.

These preserved results support configuration-dependent backend selection.

They do not establish universal superiority of either backend.

---

## Methodological Importance

The original V52D-R2 benchmark included FlashAttention tensor preparation inside the timing path.

V52D-R2-FIX removed that overhead by preparing tensors before timing.

For this reason V52D-R2-FIX should be considered the canonical benchmark for these two tested configurations.

---

## Limitations

This report does not establish:

- universal superiority;
- performance outside the tested configurations;
- behavior on other GPU architectures;
- behavior for different head dimensions;
- behavior for different batch sizes;
- behavior for different numerical precisions.

Only preserved experimental results are reported.

---

## Archived Runtime Path

```
/workspace/lanzarini_v52d_r/runtime_results/
v52d_r2_fix/
```

---

## Strict Conclusion

The preserved evidence supports only the following conclusions:

1. Correctness passed for both tested configurations.
2. Lanzarini G4 was approximately 14.74% faster at T=16384, W=128.
3. FlashAttention was the measured winner at T=65536, W=512.
4. Backend performance depended on the tested configuration.
