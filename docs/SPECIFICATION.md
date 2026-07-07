# Mathematical Specification of the Sparse-Local Attention Operator

## Purpose

This document specifies the mathematical behavior of the sparse-local attention operator evaluated by the Lanzarini Validation Suite.

Its purpose is to describe the observable semantics of the operator independently of any specific software implementation.

The proprietary implementation is intentionally not included in this repository. This document therefore specifies the operator mathematically rather than implementation details.

---

## Scope

This specification defines:

- the mathematical attention operator;
- the local attention mask;
- the expected numerical behavior;
- computational properties;
- correctness criteria;
- experimental validation scope.

It does **not** disclose proprietary implementation details.

---

## Design Goals

The operator is designed to:

- preserve deterministic sparse-local attention semantics;
- reduce unnecessary attention computation outside the local window;
- support reproducible experimental validation;
- remain compatible with standard Transformer attention formulations.

Implementation-specific optimization strategies are outside the scope of this specification.

---

# Mathematical Definition

Let

\[
Q \in \mathbb{R}^{N \times d},
\qquad
K \in \mathbb{R}^{N \times d},
\qquad
V \in \mathbb{R}^{N \times d_v}
\]

denote the query, key and value matrices, where \(N\) is the sequence length.

For each query position \(i\), attention is restricted to a causal local window defined by

\[
\mathcal{W}(i)=
\left\{
j
\;\middle|\;
0\le j\le i,\;
i-j\le W
\right\},
\]

where \(W\) denotes the local attention window.

The attention output is defined as

\[
O_i
=
\sum_{j\in\mathcal{W}(i)}
\alpha_{ij}V_j,
\]

with

\[
\alpha_{ij}
=
\frac{
\exp
\left(
Q_iK_j^\top/\sqrt d
\right)
}{
\sum_{k\in\mathcal{W}(i)}
\exp
\left(
Q_iK_k^\top/\sqrt d
\right)
}.
\]

This specification defines the mathematical operator only.

It does not prescribe any particular implementation strategy or GPU optimization.

---

## Document Status

Current version: Draft 1

Future revisions will progressively include:

- formal mathematical definition;
- pseudocode;
- computational complexity analysis;
- numerical properties;
- correctness proofs where applicable;
- validation methodology references.Mathematical Specification of the Sparse-Local Attention Operator
