# V2H Extended Correctness Validation

## Experiment Name

V2H — Extended Correctness Validation

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v2a_extended_correctness_report.json`

---

## Source Stage

`V2A_EXTENDED_CORRECTNESS_AUDIT`

---

## Status

Completed

---

## Timestamp

2026-06-30 06:30:00

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB
- Device: cuda

---

## Software Environment

- PyTorch: 2.4.1+cu124
- Data type: `torch.float16`

---

## Validation Configuration

The audit used:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64

Sequence lengths:

- 1024
- 2048
- 4096

Window sizes:

- 64
- 128
- 256
- 512

Seeds:

- 301
- 302
- 303
- 304
- 305

Tolerance configuration:

- Relative tolerance: 0.001
- Cosine similarity threshold: 0.999

---

## Results

The validation processed:

- Total rows: 60
- Passed rows: 60
- Failed rows: 0
- Errors: 0

Measured numerical values:

- Maximum absolute error: 0.0009765625
- Maximum relative L2 error: 0.0001927358567573038
- Minimum cosine similarity: 0.9999998807907104

Overall validation result:

**PASS**

The source artifact reports:

- `pass_v2a`: true

---

## Public CSV Artifacts

The source artifact reports the following CSV outputs:

- `/workspace/lanzarini_validation_suite_v1/results/csv/v2a_extended_correctness_rows.csv`
- `/workspace/lanzarini_validation_suite_v1/results/csv/v2a_extended_correctness_errors.csv`

---

## Strict Note

The source artifact states that V2A extends the V1C correctness audit to larger shapes.

It performs no speed benchmark and does not expose private kernel source code.

---

## Known Limitations

This report validates extended numerical correctness only.

It does not validate:

- runtime performance;
- energy consumption;
- production readiness;
- universal correctness outside the evaluated grid.

---

## Conclusion

The V2H Extended Correctness Validation confirms that the extended correctness audit completed successfully on the documented NVIDIA A100-SXM4-80GB platform.

The validation completed 60 rows, with 60 passes, zero failures, and zero errors.

This report reproduces only the information contained in the source artifact and does not introduce additional experimental claims.
