# Mathematical Specification of the Sparse-Local Attention Operator

## Purpose

This document specifies the mathematical behavior of the sparse-local attention operator evaluated by the Lanzarini Validation Suite.

Its purpose is to describe the observable semantics of the operator independently of any specific software implementation.

The proprietary implementation is intentionally not included in this repository. Consequently, this document specifies the mathematical operator rather than implementation details.

---

## Scope

This specification defines:

- the mathematical sparse-local attention operator;
- the causal local attention mask;
- the expected numerical semantics;
- computational characteristics;
- correctness criteria;
- the scope of experimental validation.

This document intentionally does **not** disclose proprietary implementation details.

---

## Design Goals

The operator is designed to:

- preserve deterministic sparse-local attention semantics;
- restrict attention computation to a causal local window;
- support reproducible experimental validation;
- remain compatible with the standard scaled dot-product attention formulation used in Transformer architectures.

Implementation-specific optimization strategies are outside the scope of this specification.

---

## Document Status

**Current version:** Draft 2

The current document includes:

- purpose;
- scope;
- design goals;
- formal mathematical definition.

Future revisions may include:

- implementation-independent pseudocode;
- computational complexity analysis;
- numerical properties;
- correctness discussion;
- validation methodology;
- documented limitations.

Future additions will remain consistent with the objective of documenting the mathematical behavior of the operator without disclosing proprietary implementation details.

---

# Mathematical Definition

Let

\[
Q \in \mathbb{R}^{N \times d}, \qquad
K \in \mathbb{R}^{N \times d}, \qquad
V \in \mathbb{R}^{N \times d_v}
\]

denote the query, key and value matrices of a Transformer attention layer, where:

- \(N\) is the sequence length;
- \(d\) is the attention head dimension;
- \(d_v\) is the value dimension.

For each query position \(i\), the sparse-local attention operator considers only keys contained within a causal local attention window.

Define the admissible key set

\[
\Omega(i)
=
\left\{
j
\;\middle|\;
0 \le j \le i,\;
i-j \le W
\right\},
\]

where:

- \(W\) denotes the local attention window;
- causal ordering is preserved;
- positions outside the admissible window are excluded from attention computation.

The attention score is defined as

\[
s_{ij}
=
\frac{Q_i K_j^{T}}
{\sqrt d},
\qquad
j \in \Omega(i).
\]

The normalized attention weights are

\[
\alpha_{ij}
=
\frac{\exp(s_{ij})}
{\sum\limits_{k\in\Omega(i)}
\exp(s_{ik})}.
\]

Finally, the attention output is

\[
O_i
=
\sum_{j\in\Omega(i)}
\alpha_{ij}V_j.
\]

This operator corresponds to the standard scaled dot-product attention restricted to a causal local neighborhood defined by the window parameter \(W\).

No attention weights are computed for positions outside the admissible set \(\Omega(i)\).

This specification defines only the mathematical behavior of the operator and is independent of any particular software implementation or hardware-specific optimization.
