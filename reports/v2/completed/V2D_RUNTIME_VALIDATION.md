# V2D Runtime Validation

## Experiment Name

V2D — Runtime Validation

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v1c_lite_runtime_report.json`

---

## Source Stage

`V1C_LITE_RUNTIME`

---

## Status

Completed

---

## Validation Suite

Lanzarini Validation Suite v1.0

---

## Timestamp

2026-06-29 16:48:05 UTC

---

## Hardware

- GPU: NVIDIA A100-SXM4-80GB

---

## Software Environment

- PyTorch: 2.4.1+cu124
- FlashAttention available: true
- Data type: `torch.float16`

---

## Compared Backends

The runtime validation included the following backends:

- Lanzarini
- SDPA_local_mask
- FlashAttention_window

---

## Validation Configuration

The runtime validation used:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64
- Warmup iterations: 20
- Measured runs: 100

Sequence lengths:

- 2048
- 4096
- 8192

Window sizes:

- 64
- 128
- 256

---

## Results

The runtime validation processed:

- Total rows: 54
- Valid rows: 54
- Errors: 0

Reported backend row count:

- Lanzarini: 54

Execution time:

- 37.70713663101196 seconds

Overall validation result:

**PASS**

The source artifact reports:

- `pass_v1c_lite`: true

---

## Pass / Fail Criteria

This validation is considered successful when:

- all configured runtime validation rows execute successfully;
- the number of valid rows matches the expected executed rows;
- no runtime errors are reported;
- the source artifact reports `pass_v1c_lite = true`.

---

## Known Limitations

This report documents a runtime validation stage only.

It does not claim:

- universal runtime superiority;
- production throughput;
- energy efficiency;
- scalability outside the tested configuration grid.

The report does not include per-shape timing values because only the summary fields provided in the source artifact are reported here.

---

## Conclusion

The V2D Runtime Validation confirms that the public runtime validation stage executed successfully on the documented A100 validation platform.

The validation completed 54 valid rows with zero errors and reported an overall PASS status.

This report reproduces only the information contained in the source artifact.
