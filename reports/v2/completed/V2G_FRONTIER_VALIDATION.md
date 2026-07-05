# V2G Frontier Validation

## Experiment Name

V2G — Frontier Validation

---

## Source Artifacts

This report is derived from the public validation artifacts:

`results/json/v1f_r_frontier_report.json`

`results/json/v1f_fast_frontier_report.json`

---

## Source Stages

`V1F_R_FRONTIER`

`V1F_FAST_FRONTIER`

---

## Status

Completed with mixed outcomes

---

## Validation Suite

Lanzarini Validation Suite v1.0

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Software Environment

- PyTorch: 2.4.1+cu124
- Data type: `torch.float16`
- FlashAttention available: true

---

## V1F_R_FRONTIER Results

Timestamp:

- 2026-06-29 17:09:25 UTC

Configuration:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64
- Warmup iterations: 10
- Runs: 50
- SDPA maximum sequence length: 8192

Sequence lengths:

- 2048
- 4096
- 8192
- 12288
- 16384
- 20480
- 24576

Window sizes:

- 64
- 96
- 128
- 160
- 192
- 256
- 384
- 512

Reported results:

- Total rows: 336
- Valid rows: 272
- Errors: 64
- Configuration winners: 112
- Lanzarini winners: 101
- FlashAttention winners: 11
- Elapsed time: 210.41709899902344 seconds

Overall result:

**FAIL**

The source artifact reports:

- `pass_v1f_r`: false

---

## V1F_FAST_FRONTIER Results

Timestamp:

- 2026-06-29 17:14:37 UTC

Configuration:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64
- Warmup iterations: 3
- Runs: 8

Sequence lengths:

- 8192
- 12288
- 16384
- 20480
- 24576

Window sizes:

- 64
- 128
- 256
- 512

Reported results:

- Total rows: 40
- Errors: 0
- Winners: 20
- Lanzarini winners: 16
- FlashAttention winners: 4
- Elapsed time: 9.312972784042358 seconds

Overall result:

**PASS**

The source artifact reports:

- `pass_v1f_fast`: true

---

## Interpretation

The frontier validation produced mixed results.

The reduced fast frontier validation completed successfully with zero errors and reported `pass_v1f_fast = true`.

The broader R frontier validation did not pass, reporting 64 errors and `pass_v1f_r = false`.

Therefore, this report should not be interpreted as a complete frontier validation pass.

---

## Known Limitations

This report documents the frontier validation artifacts exactly as reported.

It does not claim:

- complete frontier validation success;
- universal backend-selection correctness;
- production readiness;
- generalization outside the tested configurations.

The failed R frontier artifact must remain visible in the public record.

---

## Conclusion

The V2G Frontier Validation documents both a successful fast frontier validation and a failed broader R frontier validation.

The correct public status is:

**Completed with mixed outcomes**

This report reproduces only the information contained in the public validation artifacts and does not introduce additional experimental claims.

---

## Guiding Principle

Failed or mixed validation outcomes must be reported explicitly.

No failed validation artifact should be hidden, reclassified, or presented as a pass.
