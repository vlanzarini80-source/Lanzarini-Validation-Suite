# V42D-A-R: Native vLLM Integration Validation

## Scope

This document reports the preserved experimental results of the V42D-A-R native vLLM integration checkpoint.

Only experimentally observed results are reported.

No estimated, reconstructed or fabricated values are included.

Whenever the original JSON or CSV artifacts are not currently available, only preserved numerical summaries are reported.

---

## Purpose

The objective of this checkpoint was to evaluate the integration of the Lanzarini sparse-local attention implementation inside the vLLM inference engine.

The validation focused on functional replacement and output agreement rather than benchmark performance.

---

## Experimental Summary

The preserved validation results are:

| Test | Result |
|------|--------|
| Long prompts | 49 / 50 PASS |
| Boundary tie | 1 |
| Single-prompt replacement | PASS |
| Ten-prompt replacement | PASS |
| Long generation | 9 / 10 exact |
| Near-tie generation | 1 |

---

## Observed Bottleneck

The preserved benchmark identified the dominant performance bottleneck as:

- paged-to-contiguous cache reconstruction

The preserved analysis estimated this overhead to be approximately:

- 15× the kernel execution cost

This observation refers only to the tested implementation.

---

## Interpretation

Within the evaluated configuration:

- native integration was successfully validated;
- almost all long-prompt evaluations passed;
- output agreement was observed for the tested replacement cases;
- one remaining case was documented as a near-tie rather than a correctness failure.

These observations apply only to the evaluated experimental configuration.

---

## Limitations

This checkpoint does not establish:

- universal compatibility with every vLLM version;
- correctness for every transformer architecture;
- performance improvements for complete inference pipelines;
- grouped decode validation beyond the tested scope.

---

## Archived Runtime Status

The preserved project documentation records this checkpoint as a completed validation stage.

The currently preserved numerical summary documents the experimental outcome.

It does not by itself demonstrate that the original byte-identical runtime artifacts are currently included in the public repository.
