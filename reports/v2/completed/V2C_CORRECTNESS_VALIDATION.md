# V2C Correctness Validation

## Experiment Name

V2C — Correctness Validation

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v1b_r_correctness_report.json`

---

## Source Stage

`V1B_R_CORRECTNESS_AUDIT`

---

## Status

Completed

---

## Validation Suite

Lanzarini Validation Suite v1.0

---

## Timestamp

2026-06-29 15:05:25 UTC

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Software Environment

- PyTorch: 2.4.1+cu124
- Kernel: `selected_forward_q2`
- Kernel signature: `(q, k, v, window)`
- Detected call pattern: `positional_window`
- Data type: `torch.float16`

---

## Validation Configuration

The audit evaluated the following parameter grid:

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

Tolerance configuration:

- Absolute tolerance (atol): 0.002
- Relative tolerance (rtol): 0.002
- Maximum relative L2 threshold: 0.005
- Minimum cosine similarity threshold: 0.999

---

## Results

The audit processed:

- Total rows: 27
- Passed: 27
- Failed: 0
- Errors: 0

Measured values:

- Maximum absolute error: 0.0009765625
- Mean absolute error: 0.000009702460374683142
- Maximum relative L2 error: 0.0001925159493029039
- Minimum cosine similarity: 0.9999998807907104

Execution time:

- 12.391262769699097 seconds

Overall validation result:

**PASS**

---

## Pass / Fail Criteria

The validation is considered successful when:

- all evaluated rows satisfy the numerical tolerances;
- no execution errors occur;
- the cosine similarity remains above the configured threshold;
- the validation artifact reports `pass_v1b_r = true`.

---

## Known Limitations

This report validates numerical correctness for the evaluated configuration only.

It does not measure:

- runtime performance;
- energy consumption;
- scalability outside the tested parameter grid;
- production inference throughput.

---

## Conclusion

The V2C Correctness Validation confirms that the `selected_forward_q2` kernel satisfied the configured numerical correctness criteria across the tested evaluation grid.

The validation completed with 27 successful evaluations, zero failures, zero execution errors, and all measured numerical metrics remained within the configured acceptance thresholds.

This report reproduces only the information contained in the public validation artifact.
