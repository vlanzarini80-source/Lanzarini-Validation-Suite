# Abstract

Sparse-local attention is widely used to reduce the computational cost of long-context Transformer inference and training.

This paper presents the Lanzarini Validation Suite, a public validation and reproducibility framework designed to support transparent experimental evaluation of a sparse-local attention operator.

The Validation Suite provides a mathematical specification of the evaluated operator together with a publicly documented validation methodology, correctness criteria, computational complexity analysis, benchmark scope, experimental limitations, reproducibility documentation, and validation artifacts.

The mathematical operator follows the standard sparse-local (sliding-window) causal attention formulation. This work does **not** claim the introduction of a novel mathematical attention operator or attention formulation.

Instead, the primary contribution of this work is the development of an evidence-based validation framework intended to improve transparency, reproducibility, and independent inspection of experimentally reported results.

The proprietary implementation evaluated by the Validation Suite is intentionally not included in this public repository. Consequently, all reported validation results apply only to the experimentally evaluated configurations and should not be interpreted beyond the documented experimental evidence.
