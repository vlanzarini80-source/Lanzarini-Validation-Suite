# Claim Ledger

## Purpose

This document maps the principal scientific claims made by the Lanzarini Validation Suite to the publicly documented evidence available in this repository.

Its purpose is to distinguish:

- supported claims;
- explicit limitations;
- open questions;
- future work;

while avoiding interpretations beyond the available experimental evidence.

The evidence referenced in this document is limited to publicly available documentation and validation artifacts contained in this repository.

---

# Claim Mapping

| Claim | Supporting Evidence | Status | Scope |
|--------|---------------------|--------|-------|
| The repository provides a publicly documented validation and reproducibility workflow. | README.md, docs/VALIDATION_METHOD.md, public validation artifacts | Supported | Public Validation Suite |
| The proprietary implementation is intentionally excluded from the public repository. | README.md, docs/ADAPTER_INTERFACE.md | Supported | Public repository |
| The evaluated operator is mathematically specified independently of its implementation. | docs/SPECIFICATION.md | Supported | Public documentation |
| The mathematical specification is implementation-independent. | docs/SPECIFICATION.md | Supported | Public documentation |
| Computational complexity of the documented operator is publicly described. | docs/COMPLEXITY.md | Supported | Public documentation |
| Correctness evaluation follows documented validation criteria. | docs/CORRECTNESS.md, validation reports | Supported | Experimentally evaluated configurations |
| Benchmark results are reported only for experimentally evaluated configurations. | docs/BENCHMARK_SCOPE.md, validation reports | Supported | Experimentally evaluated configurations |
| Runtime validation documents observed behavior under documented benchmark conditions. | paper/RESULTS.md, validation reports | Supported | Documented benchmark configurations |
| Backend performance is experimentally observed to be regime-dependent. | paper/RESULTS.md, validation reports | Supported | Documented experimental configurations |
| The public repository does not independently validate the proprietary implementation. | docs/LIMITATIONS.md | Explicit limitation | Public repository |
| Universal performance superiority is not claimed. | README.md, docs/LIMITATIONS.md, docs/BENCHMARK_SCOPE.md | Supported | All public claims |
| Universal energy reduction is not claimed. | README.md, docs/LIMITATIONS.md | Supported | All public claims |
| End-to-end production benefit has not yet been publicly established. | docs/LIMITATIONS.md, paper/DISCUSSION.md | Open | Requires additional public evidence |
| Standard long-context downstream benchmarks remain outside the current public validation scope. | docs/BENCHMARK_SCOPE.md | Future work | Future validation |

---

# Interpretation

The public repository should be interpreted as a validation and reproducibility framework supported by publicly documented experimental evidence.

It should not be interpreted as:

- an open-source release of the proprietary implementation;
- proof of universal backend superiority;
- proof of universal runtime improvement;
- proof of universal energy reduction.

---

# Current Evidence-Based Position

Public experimental evidence indicates that backend performance depends on the evaluated configuration.

The Lanzarini Validation Suite therefore emphasizes:

- evidence-based benchmarking;
- reproducible experimentation;
- transparent reporting;
- explicit documentation of limitations;

rather than claims of universal superiority.

---

# Future Evidence

Future revisions of the Validation Suite may strengthen the available public evidence through:

- benchmark tables directly linked to public validation artifacts;
- LongBench or equivalent long-context evaluations;
- Needle-in-a-Haystack evaluations;
- downstream quality evaluation (for example, perplexity);
- end-to-end serving benchmarks;
- additional hardware platforms;
- additional software environments.

Future scientific claims should remain supported by publicly documented experimental evidence.

---

# Canonical Status

This document is the canonical ledger for interpreting the scientific claims made by the public repository.

Whenever differences in wording exist across documentation files, this ledger should be interpreted together with:

- paper/METHOD.md
- paper/RESULTS.md
- documented validation artifacts

before drawing scientific conclusions.

---

# Consistency

This document should be interpreted together with:

- README.md
- docs/SPECIFICATION.md
- docs/VALIDATION_METHOD.md
- docs/BENCHMARK_SCOPE.md
- docs/LIMITATIONS.md
- paper/METHOD.md
- paper/RESULTS.md
- paper/DISCUSSION.md
- paper/CONCLUSION.md

In case of inconsistency, the documented experimental evidence and validation artifacts take precedence over summary statements.
