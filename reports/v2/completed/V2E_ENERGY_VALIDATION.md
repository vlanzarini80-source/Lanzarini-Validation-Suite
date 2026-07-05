# V2E Energy Validation

## Experiment Name

V2E — Energy Validation

---

## Source Artifact

This report is derived from the public validation artifact:

`results/json/v1d_lite_energy_report.json`

---

## Source Stage

`V1D_LITE_ENERGY`

---

## Status

Completed

---

## Validation Suite

Lanzarini Validation Suite v1.0

---

## Timestamp

2026-06-29 16:51:41 UTC

---

## Hardware

GPU:

- NVIDIA A100-SXM4-80GB

Driver:

- 580.159.04

Power limit:

- 400 W

Total GPU memory:

- 81920 MB

---

## Software Environment

- PyTorch: 2.4.1+cu124
- FlashAttention available: true
- Data type: `torch.float16`

---

## Compared Backends

The energy validation included the following backends:

- Lanzarini
- SDPA_local_mask
- FlashAttention_window

---

## Validation Configuration

The validation used:

- Batch size (B): 1
- Heads (H): 4
- Head dimension (D): 64

Sequence lengths:

- 2048
- 4096
- 8192

Window sizes:

- 64
- 128
- 256

Measurement configuration:

- Warmup iterations: 20
- Inner repeats: 300
- Power sampling interval: 0.005 seconds

---

## Results

The validation processed:

- Total rows: 54
- Valid rows: 54
- Errors: 0

Reported backend rows:

- Lanzarini: 54

Execution time:

- 41.22992253303528 seconds

Overall validation result:

**PASS**

The source artifact reports:

- `pass_v1d_lite`: true

---

## Pass / Fail Criteria

The validation is considered successful when:

- all configured energy validation rows execute successfully;
- the number of valid rows matches the executed rows;
- no execution errors are reported;
- the source artifact reports `pass_v1d_lite = true`.

---

## Known Limitations

This report documents the execution of the public energy validation stage.

The summary artifact does not include detailed per-shape energy measurements.

Accordingly, this report does not present per-configuration energy values.

No claims are made regarding universal energy superiority beyond the information contained in the public validation artifact.

---

## Conclusion

The V2E Energy Validation confirms that the public energy validation stage completed successfully on the documented NVIDIA A100-SXM4-80GB platform.

The validation completed **54 valid validation rows**, reported zero execution errors, and recorded an overall **PASS** status.

This report reproduces only the information contained in the public validation artifact and does not introduce additional experimental claims.

---

## Guiding Principle

This report documents only the information contained in the referenced public validation artifact.

No experimental results have been added, reconstructed, inferred, or modified.

Scientific conclusions remain limited to the validated data contained in the source artifact.
