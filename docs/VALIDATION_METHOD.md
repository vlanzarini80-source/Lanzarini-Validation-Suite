# Validation Method

## Purpose

This document complements `paper/METHOD.md`.

The canonical methodological description of the Lanzarini Validation Suite is maintained in:

- `paper/METHOD.md`

This document focuses on the practical execution of the public validation workflow.

## Public Validation Workflow

Typical execution stages include:

1. Environment verification
2. Adapter availability check
3. Correctness validation
4. Runtime benchmarking
5. Artifact generation
6. Integrity verification
7. Report generation

## Related Documentation

- `paper/METHOD.md`
- `docs/SPECIFICATION.md`
- `docs/CORRECTNESS.md`
- `docs/BENCHMARK_SCOPE.md`
- `docs/ADAPTER_INTERFACE.md`
- `docs/LIMITATIONS.md`

---

## Validation Objectives

The public validation workflow aims to:

- verify mathematical correctness;
- evaluate numerical consistency;
- measure runtime characteristics under documented experimental conditions;
- document reproducible experimental evidence;
- provide publicly inspectable validation artifacts.

---

## Validation Environment

Validation is performed using documented hardware and software configurations.

Depending on the validation stage, experiments may include:

- NVIDIA GPUs;
- CUDA;
- PyTorch;
- Triton.

The exact hardware configuration, software versions, and execution environment are reported in the corresponding validation artifacts whenever applicable.

---

## Experimental Protocol

Each validation stage follows a documented experimental protocol.

Typical validation steps include:

1. environment verification;
2. correctness evaluation;
3. runtime measurement;
4. artifact generation;
5. integrity verification;
6. publication of validation reports.

Each validation stage is documented independently and may define additional stage-specific procedures when required.

---

## Correctness Evaluation

Correctness is evaluated by comparing the observable outputs of the evaluated operator against the corresponding documented reference implementation.

The numerical comparison methodology is described in the corresponding validation reports.

---

## Performance Evaluation

Performance evaluation may include:

- execution time;
- throughput;
- runtime comparison;
- other documented metrics, when applicable.

Performance comparisons are reported only for the documented experimental configurations.

No performance result should be interpreted beyond the tested conditions.

---

## Reproducibility

The Validation Suite is designed to maximize experimental reproducibility.

Public validation artifacts may include:

- validation reports;
- configuration summaries;
- CSV datasets;
- JSON summaries;
- integrity manifests;
- reproducibility documentation.

---

## Scope of Validation

Validation results apply only to the documented experimental conditions.

They should not be interpreted as universal correctness or performance guarantees.

---

## Limitations

The Validation Suite validates only the configurations that have been experimentally evaluated.

Untested hardware platforms, software versions, workloads, model architectures, and execution environments are outside the scope of the reported validation results.

---

## Future Extensions

Future revisions may include additional validation protocols, benchmark methodologies, statistical analyses, reproducibility procedures, and other documentation supported by new experimental evidence.
