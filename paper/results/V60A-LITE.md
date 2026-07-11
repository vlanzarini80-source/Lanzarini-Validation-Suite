# V60A-LITE — Dense Frontier Sweep

## Purpose

This checkpoint performed a dense experimental sweep to characterize the measured backend frontier between Lanzarini G4 and FlashAttention.

The objective was to identify the experimentally observed operating regions where each backend was faster.

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Preserved Results

| Metric | Value |
|--------|------:|
| Validation | PASS |
| Measured rows | 141 |
| Errors | 0 |

---

## Measured Winners

| Backend | Count | Percentage |
|---------|------:|-----------:|
| Lanzarini G4 | 115 | 81.56% |
| FlashAttention | 26 | 18.44% |

---

## Important Implementation Note

The benchmark required moving the `NEG_INF` constant inside the Triton kernels to ensure successful execution.

---

## Interpretation

Within the evaluated measurement grid:

- Lanzarini G4 was the experimentally observed fastest backend in 115 measured configurations.
- FlashAttention was the experimentally observed fastest backend in 26 measured configurations.

The reported percentages describe only the evaluated grid.

They are **not** probabilities and should not be interpreted as evidence of universal superiority.

---

## Scope

These observations apply only to the tested configurations.

They do not establish:

- universal backend dominance;
- performance outside the measured frontier;
- correctness on different hardware platforms.
