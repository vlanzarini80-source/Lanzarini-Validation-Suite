# Experimental Results

## Scope

This document reports only experimental results obtained during the Lanzarini project.

Only measurements produced by the benchmark scripts are reported.

No estimated, reconstructed, interpolated or fabricated benchmark values are included.

Whenever the original JSON or CSV artifacts are not currently available, the corresponding checkpoint is explicitly identified as a preserved numerical summary.

No unsupported performance claim should be inferred from this document.

---

# V52D-R2-FIX

## Purpose

Canonical head-to-head comparison between Lanzarini G4 and FlashAttention after removing the FlashAttention transpose and contiguous operations from the timed benchmark section.

The objective of this experiment was to compare the execution time of both implementations under the same benchmark protocol after eliminating preprocessing overhead from the timed region.

## Hardware

- GPU: NVIDIA A100-SXM4-80GB
- Precision: FP16
- Batch size (B): 1
- Attention heads (H): 4
- Head dimension (D): 64

## Tested Shapes

| Sequence Length (T) | Window (W) | Winner | Correctness |
|--------------------:|-----------:|---------|-------------|
| 16384 | 128 | Lanzarini G4 | PASS |
| 65536 | 512 | FlashAttention | PASS |

## Measured Result — T = 16384, W = 128

Measured median latency:

- Lanzarini G4 = **0.0770589467 ms**
- FlashAttention = **0.0903861 ms**

Measured result:

- Lanzarini G4 was approximately **14.74% faster** than FlashAttention for this tested configuration.

## Measured Result — T = 65536, W = 512

Measured outcome:

- Winner = FlashAttention
- Correctness = PASS

The exact median latency for this configuration is not currently preserved in the available archived benchmark outputs and is therefore intentionally omitted.

## Experimental Notes

These measurements apply only to the tested configuration reported above.

They must not be interpreted as evidence of universal performance superiority.

The benchmark compared the two implementations after moving FlashAttention transpose and contiguous operations outside the timed benchmark loop.

---

The following sections report progressively larger benchmark campaigns, router validation experiments, and transition-band analyses obtained from subsequent validation checkpoints.
