# Evidence Matrix

## Purpose

This document maps the major public statements of the Lanzarini Validation Suite to their corresponding publicly available evidence.

Its purpose is to distinguish clearly between:

- experimentally supported results;
- documented methodology;
- repository documentation;
- future work;
- proprietary components intentionally excluded from the public repository.

No unpublished measurements or proprietary implementation details are referenced in this document.

---

# Public Evidence Matrix

| Public Statement | Public Evidence | Status |
|------------------|-----------------|--------|
| The public validation workflow is reproducible | README, Quick Start, V1 scripts | Supported |
| Environment validation is publicly available | V1A Environment Report | Supported |
| The adapter interface is publicly documented | ADAPTER_INTERFACE.md, V1B | Supported |
| Artifact integrity is verified using SHA-256 manifests | V1E Artifact Manifest | Supported |
| Public validation report generation is reproducible | V1F Report Generator | Supported |
| The validation methodology is documented | VALIDATION_METHOD.md | Supported |
| The mathematical specification is publicly documented | SPECIFICATION.md | Supported |
| Computational complexity is documented | COMPLEXITY.md | Supported |
| Benchmark scope and limitations are explicitly documented | BENCHMARK_SCOPE.md, LIMITATIONS.md | Supported |
| The public repository excludes the proprietary implementation | README, Public Mode | Supported |

---

# Claims Intentionally Not Made

This public repository does **not** claim:

- universal runtime superiority;
- universal energy superiority;
- improved model quality;
- lower perplexity;
- state-of-the-art benchmark performance;
- replacement of FlashAttention in every deployment scenario;
- superiority on downstream language-model evaluation tasks.

Such claims require additional experimental evidence and therefore remain outside the scope of the public Validation Suite.

---

# Proprietary Components

The proprietary sparse-local Triton implementation is intentionally excluded from this repository.

The public Validation Suite verifies:

- validation methodology;
- execution workflow;
- reproducibility process;
- artifact integrity;
- documentation consistency.

It does **not** expose proprietary implementation details or source code.

---

# Future Public Evidence

Future public releases may include additional experimentally verified evidence, including:

- benchmark comparisons;
- additional hardware platforms;
- extended runtime validation;
- downstream model evaluations;
- additional public datasets.

Only experimentally measured and publicly verifiable results will be added.

---

# Strict Interpretation

Every public statement in this repository should be traceable to publicly available documentation or validation artifacts.

Statements that cannot currently be supported by public evidence are intentionally excluded from the repository.
