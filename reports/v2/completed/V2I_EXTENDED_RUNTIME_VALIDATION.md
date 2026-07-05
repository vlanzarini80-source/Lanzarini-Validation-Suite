# V2I Extended Runtime Validation

## Experiment Name

V2I — Extended Runtime Validation

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v2b_runtime_extended_report.json`

---

## Source Stage

`V2B_RUNTIME_BENCHMARK_EXTENDED`

---

## Status

Completed

---

## Timestamp

2026-06-30 09:45:11

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB
- Device: cuda

---

## Software Environment

- PyTorch: 2.4.1+cu124
- Data type: `torch.float16`
- FlashAttention available: true
- FlashAttention error: null

---

## Validation Configuration

The benchmark used:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64
- Warmup iterations: 10
- Runs: 50

Sequence lengths:

- 1024
- 2048
- 4096
- 8192

Window sizes:

- 64
- 128
- 256
- 512

Seeds:

- 401
- 402
- 403

---

## Results

The validation processed:

- Total rows: 48
- Correct rows: 48
- Failed rows: 0
- Errors: 0
- Shape summaries: 16

Reported row counts:

- Lanzarini rows: 48
- SDPA rows: 0
- FlashAttention rows: 0

Reported shape-summary winners:

- Lanzarini: 16
- SDPA: 0
- FlashAttention: 0

Median runtime ranges reported by the artifact:

- Lanzarini median min: 0.05338108167052269 ms
- Lanzarini median max: 0.1535206101834774 ms
- SDPA median min: 0.26206113398075104 ms
- SDPA median max: 3.138445783406496 ms
- FlashAttention median min: 0.18971855752170086 ms
- FlashAttention median max: 0.49513159319758415 ms

Overall validation result:

**PASS**

The source artifact reports:

- `pass_v2b`: true

---

## Public CSV Artifacts

The source artifact reports the following CSV outputs:

- `/workspace/lanzarini_validation_suite_v1/results/csv/v2b_runtime_extended_rows.csv`
- `/workspace/lanzarini_validation_suite_v1/results/csv/v2b_runtime_extended_shape_summaries.csv`
- `/workspace/lanzarini_validation_suite_v1/results/csv/v2b_runtime_extended_errors.csv`

---

## Strict Note

The source artifact states that V2B is an extended runtime benchmark, but not a full frontier or commercial performance claim.

It verifies runtime behavior across a moderate grid and preserves all measured rows.

---

## Known Limitations

This report documents the extended runtime benchmark only.

It does not claim:

- universal runtime superiority;
- commercial production performance;
- full backend frontier coverage;
- energy efficiency;
- scalability outside the tested configuration grid.

---

## Conclusion

The V2I Extended Runtime Validation confirms that the extended runtime benchmark completed successfully on the documented NVIDIA A100-SXM4-80GB platform.

The validation completed 48 correct rows, zero failed rows, zero errors, and reported an overall **PASS** status.

This report reproduces only the information contained in the source artifact and does not introduce additional experimental claims.

---

## Guiding Principle

This report documents only the information contained in the referenced public validation artifact.

No experimental results have been added, reconstructed, inferred, or modified.
