# Claim Ledger

This document lists the scientific claims currently supported by the Lanzarini Validation Suite and the broader experimental work.

The purpose is to separate validated evidence from future work and to avoid unsupported performance claims.

| Claim | Evidence | Status | Scope |
|---|---|---|---|
| The public repository provides a reproducible validation workflow | V1A–V1F public validation stages, JSON/CSV/HTML reports, SHA-256 manifests | Supported | Public Validation Suite |
| The proprietary kernel is intentionally excluded from the public repository | Repository structure and README scope | Supported | Public release |
| Numerical validation is performed only under defined benchmark configurations | V1C correctness artifacts | Supported | Tested configurations only |
| Runtime smoke validation verifies benchmark execution, not universal performance | V1D runtime smoke reports | Supported | Smoke-test scope |
| Energy/token reduction up to 22.6% was observed vs FlexAttention | NVML energy campaign, tested configuration | Supported | Specific tested configuration |
| Throughput improvement up to 25.5% was observed vs FlexAttention | Runtime benchmark, tested configuration | Supported | Specific tested configuration |
| Backend performance is regime-dependent | FlashAttention comparison campaigns including V52D-R2-FIX | Supported | Tested A100 configurations |
| Lanzarini G4 was faster than FlashAttention at T=16384, W=128 in the clean benchmark | V52D-R2-FIX | Supported | A100, FP16, D=64, tested shape |
| FlashAttention was faster than Lanzarini G4 at T=65536, W=512 in the clean benchmark | V52D-R2-FIX | Supported | A100, FP16, D=64, tested shape |
| The project supports backend-selection research rather than universal replacement claims | Combined benchmark evidence | Supported | Experimental interpretation |
| The public repository does not independently validate the proprietary kernel implementation | Scope limitation | Explicit limitation | Public repository |
| Universal speedup is not claimed | README disclaimer and benchmark evidence | Supported | All public claims |
| Universal energy saving is not claimed | README disclaimer and limited NVML evidence | Supported | All public claims |
| End-to-end production benefit is not yet established | vLLM integration overhead observations | Open / limited | Requires further work |
| Standard long-context task benchmarks are future work | LongBench, NIAH, perplexity not yet public in this repository | Future work | Future validation |

## Interpretation

The public repository should be interpreted as a reproducibility and validation framework for published experimental artifacts.

It does not claim to provide a complete open-source implementation of the proprietary sparse-local attention kernel.

The strongest current scientific position is:

> Different attention backends perform better under different experimentally validated regimes. The project therefore supports backend-selection and reproducible benchmarking rather than universal superiority claims.

## Future Evidence Required

To strengthen the scientific contribution, future work should add:

- mathematical specification of the sparse-local operator;
- pseudocode independent of proprietary source code;
- complexity analysis;
- benchmark tables tied to public artifacts;
- LongBench or equivalent long-context evaluations;
- Needle-in-a-Haystack evaluations;
- perplexity or downstream quality checks;
- end-to-end serving benchmarks;
- expanded hardware coverage.
