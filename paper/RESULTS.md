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

---

# V56A — Blind Router Validation

## Purpose

V56A evaluated a frozen backend-selection router on blind sparse-local attention shapes.

The router was not modified during evaluation.

The comparison included:

- FlashAttention sliding-window attention;
- Lanzarini G4;
- numerical correctness against the reference implementation;
- router accuracy;
- latency regret relative to the per-row oracle winner.

This checkpoint evaluates only the tested blind grid and does not establish universal router generalization.

## Recorded Environment

The archived runtime output reports:

- GPU: NVIDIA A100-SXM4-80GB
- PyTorch: 2.8.0+cu128
- Triton: 3.4.0
- FlashAttention available: true
- Sequence lengths: `T = [12288, 24576, 49152]`
- Target ratios: `[0.004, 0.006, 0.008, 0.012]`

## Correctness

All 12 evaluated rows passed the numerical correctness check.

Observed correctness metrics across the reported rows included:

- maximum absolute error between `0.00048828125` and `0.0009765625`;
- relative L2 error between approximately `0.00011083` and `0.00032729`;
- cosine similarity between `0.9999999404` and `1.0000001192`;
- `n_errors = 0`;
- `pass_v56a = true`.

These values apply only to the reported V56A configurations.

## Row-Level Results

The latency values below are the values reported in each archived `ROW SUMMARY`.

A positive delta means Lanzarini G4 was faster than FlashAttention.

A negative delta means FlashAttention was faster than Lanzarini G4.

| T | W | W/T | FlashAttention ms | Lanzarini G4 ms | Delta vs Flash (%) | Router choice | Actual winner | Router correct |
|---:|---:|---:|---:|---:|---:|---|---|---|
| 12288 | 64 | 0.0052083333 | 0.0902579091 | 0.0508670099 | 43.6426 | FlashAttention | Lanzarini G4 | No |
| 12288 | 64 | 0.0052083333 | 0.0802200027 | 0.0517491177 | 35.4910 | FlashAttention | Lanzarini G4 | No |
| 12288 | 96 | 0.0078125000 | 0.0789550692 | 0.0587596968 | 25.5783 | FlashAttention | Lanzarini G4 | No |
| 12288 | 160 | 0.0130208333 | 0.0799549222 | 0.0584283061 | 26.9234 | FlashAttention | Lanzarini G4 | No |
| 24576 | 96 | 0.0039062500 | 0.0794438161 | 0.1109926067 | -39.7121 | FlashAttention | FlashAttention | Yes |
| 24576 | 160 | 0.0065104167 | 0.1031091213 | 0.1110148281 | -7.6673 | FlashAttention | FlashAttention | Yes |
| 24576 | 192 | 0.0078125000 | 0.1032369174 | 0.1111468561 | -7.6619 | FlashAttention | FlashAttention | Yes |
| 24576 | 288 | 0.0117187500 | 0.1289892793 | 0.1592712551 | -23.4764 | FlashAttention | FlashAttention | Yes |
| 49152 | 192 | 0.0039062500 | 0.1898082569 | 0.2069715448 | -9.0424 | FlashAttention | FlashAttention | Yes |
| 49152 | 288 | 0.0058593750 | 0.2441903539 | 0.3002423421 | -22.9542 | FlashAttention | FlashAttention | Yes |
| 49152 | 384 | 0.0078125000 | 0.2451369278 | 0.3925677612 | -60.1422 | FlashAttention | FlashAttention | Yes |
| 49152 | 576 | 0.0117187500 | 0.3529980034 | 0.4764474183 | -34.9717 | FlashAttention | FlashAttention | Yes |

## Duplicate Shape Note

`T = 12288, W = 64` appears twice because two different target ratios, `0.004` and `0.006`, rounded to the same effective integer window size.

The rows are retained separately because they were separately executed benchmark cases in the archived V56A output.

## Winner Distribution

The archived summary reports:

| Backend | Number of wins |
|---|---:|
| Lanzarini G4 | 4 |
| FlashAttention | 8 |
| Parity | 0 |

The frozen router selected FlashAttention for all 12 rows.

Therefore:

- router selections of Lanzarini G4: 0;
- router selections of FlashAttention: 12;
- correct selections: 8;
- incorrect selections: 4;
- binary router accuracy: **66.67%**;
- parity-allowed accuracy: **66.67%**.

## Aggregate Latency Results

The archived V56A summary reports:

| Metric | Value |
|---|---:|
| Total router latency | 1.7763005793 ms |
| Total always-FlashAttention latency | 1.7763005793 ms |
| Total always-G4 latency | 2.0884587429 ms |
| Total oracle latency | 1.6667168066 ms |
| Router speedup vs always FlashAttention | 0.00% |
| Router speedup vs always G4 | 14.9468% |
| Router regret vs oracle | 6.5748% |
| Mean row regret | 16.9724% |
| Maximum row regret | 77.4390% |

## Interpretation

V56A passed numerical correctness, but the frozen router did not generalize successfully across the complete blind grid.

The router always selected FlashAttention.

This choice was correct for all tested rows at:

- `T = 24576`;
- `T = 49152`.

It was incorrect for all four evaluated rows at:

- `T = 12288`.

For those four rows, Lanzarini G4 was faster by between approximately **25.58%** and **43.64%**, using the delta definition reported by the benchmark output.

The router therefore achieved a measured accuracy of **8/12**, while incurring a total latency regret of approximately **6.57%** relative to an oracle that selected the faster backend independently for each row.

## Strict Interpretation

V56A is evidence of both numerical correctness and router generalization failure on the tested blind set.

It must not be presented as a successful final router result.

Its scientific value is that it identifies a specific failure mode:

- a rule biased toward FlashAttention missed the Lanzarini-preferred regime at `T = 12288`.

Later router checkpoints should be interpreted as attempts to correct this observed failure.

## Archived Runtime Path

The original runtime output reported the following path:

```text
/workspace/lanzarini_v35/runtime_results/
v56a_router_blind_validation/
v56a_router_blind_validation.json
```

The path documents the original runtime location.

It does not prove that the original byte-identical JSON artifact is currently present in this public repository. 

---

# V56B-LITE — Transition-Band Sweep

## Purpose

V56B-LITE evaluated the transition region between Lanzarini G4 and FlashAttention using a fixed benchmark protocol and a small grid of sequence lengths and local-window ratios.

The purpose was to determine whether the faster backend changed across the tested operating region.

This checkpoint reports only the measured grid and does not establish a universal backend-selection rule.

## Recorded Environment

The preserved checkpoint records:

- GPU: NVIDIA A100-SXM4-80GB
- PyTorch: 2.8.0+cu128
- Triton: 3.4.0
- FlashAttention available: true
- Sequence lengths: `T = [12288, 16384, 20480, 24576]`
- Target ratios: `[0.006, 0.012]`
- Number of evaluated rows: 8
- Number of execution errors: 0
- `pass_v56b_lite = true`

## Row-Level Results

A positive delta means Lanzarini G4 was faster than FlashAttention.

A negative delta means FlashAttention was faster than Lanzarini G4.

| T | W | W/T | FlashAttention ms | Lanzarini G4 ms | Delta vs Flash (%) | Winner |
|---:|---:|---:|---:|---:|---:|---|
| 12288 | 64 | 0.0052083333 | 0.0811349265 | 0.0537525602 | 33.7492 | Lanzarini G4 |
| 12288 | 160 | 0.0130208333 | 0.0790898502 | 0.0584674291 | 26.0747 | Lanzarini G4 |
| 16384 | 96 | 0.0058593750 | 0.0809719563 | 0.0771322884 | 4.7420 | Lanzarini G4 |
| 16384 | 192 | 0.0117187500 | 0.0795073435 | 0.0771279149 | 2.9927 | Lanzarini G4 |
| 20480 | 128 | 0.0062500000 | 0.0799075589 | 0.0930313095 | -16.4237 | FlashAttention |
| 20480 | 256 | 0.0125000000 | 0.0849486478 | 0.1310458928 | -54.2648 | FlashAttention |
| 24576 | 160 | 0.0065104167 | 0.1027208343 | 0.1111833192 | -8.2383 | FlashAttention |
| 24576 | 288 | 0.0117187500 | 0.1297893934 | 0.1591762938 | -22.6420 | FlashAttention |

## Winner Distribution

The preserved summary reports:

| Backend | Number of wins |
|---|---:|
| Lanzarini G4 | 4 |
| FlashAttention | 4 |
| Parity | 0 |

The winner changed between the tested sequence-length regions:

- Lanzarini G4 won all tested rows at `T = 12288`;
- Lanzarini G4 won all tested rows at `T = 16384`;
- FlashAttention won all tested rows at `T = 20480`;
- FlashAttention won all tested rows at `T = 24576`.

## Aggregated Results by Sequence Length

### T = 12288

- Tested windows: `W = [64, 160]`
- Lanzarini G4 wins: 2
- FlashAttention wins: 0
- Mean reported delta: **29.9119%**
- Largest tested window won by Lanzarini G4: `W = 160`

### T = 16384

- Tested windows: `W = [96, 192]`
- Lanzarini G4 wins: 2
- FlashAttention wins: 0
- Mean reported delta: **3.8673%**
- Largest tested window won by Lanzarini G4: `W = 192`

### T = 20480

- Tested windows: `W = [128, 256]`
- Lanzarini G4 wins: 0
- FlashAttention wins: 2
- Mean reported delta: **-35.3443%**
- Smallest tested window won by FlashAttention: `W = 128`

### T = 24576

- Tested windows: `W = [160, 288]`
- Lanzarini G4 wins: 0
- FlashAttention wins: 2
- Mean reported delta: **-15.4402%**
- Smallest tested window won by FlashAttention: `W = 160`

## Interpretation

The measured winner changed across the tested `(T, W)` region.

For the tested shapes:

- Lanzarini G4 was faster at `T = 12288` and `T = 16384`;
- FlashAttention was faster at `T = 20480` and `T = 24576`.

The measured advantage of Lanzarini G4 decreased substantially near `T = 16384`:

- `4.7420%` at `T = 16384, W = 96`;
- `2.9927%` at `T = 16384, W = 192`.

At the next tested sequence length, `T = 20480`, FlashAttention became faster:

- `16.4237%` advantage at `W = 128`;
- `54.2648%` advantage at `W = 256`.

These observations support the existence of a transition region in the tested grid.

They do not prove that the transition occurs at one exact universal sequence length, nor that a single threshold generalizes to untested hardware, software versions, dimensions, or window sizes.

## Strict Interpretation

V56B-LITE provides measured evidence that neither backend was universally faster across the tested grid.

The result supports a regime-dependent backend-selection problem.

It does not establish:

- a universal frontier;
- a hardware-independent rule;
- performance outside the tested configurations;
- generalization to different head dimensions, data types, batch sizes, or GPU architectures.

## Archived Runtime Path

The preserved runtime location was:

```text
/workspace/lanzarini_v35/runtime_results/
v56b_lite_transition_band_sweep/
v56b_lite_transition_band_sweep.json
```

This path records the original runtime location.

It does not by itself prove that the original byte-identical JSON artifact is currently included in the public repository. 
