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

- **Q ∈ ℝ^(N × d)** denote the query matrix;
- **K ∈ ℝ^(N × d)** denote the key matrix;
- **V ∈ ℝ^(N × d_v)** denote the value matrix,

where

- **N** is the sequence length;
- **d** is the attention head dimension;
- **d_v** is the value dimension.

For each query position **i**, the sparse-local attention operator evaluates attention only over a causal local neighborhood.

---

## Admissible Key Set

For every query position **i**, the admissible key set is defined as

```text
Ω(i) = { j ∈ {0,...,i} : i − j ≤ W }
```

where

- **W** denotes the local attention window;
- causal ordering is preserved;
- keys outside the admissible set are excluded from the attention computation.

---

## Attention Score

For every admissible key position **j ∈ Ω(i)**, the attention score is defined as

```text
s(i,j) = (Q[i] · K[j]^T) / sqrt(d)
```

where

- **Q[i]** denotes the query vector at position **i**;
- **K[j]** denotes the key vector at position **j**.

---

## Attention Weights

The normalized attention weights are defined as

```text
α(i,j) = exp(s(i,j))
         ------------------------------------
         Σ_{k∈Ω(i)} exp(s(i,k))
```

where the normalization is performed only over the admissible key positions contained in **Ω(i)**.

---

## Attention Output

The output vector associated with query position **i** is defined as

```text
O(i) = Σ_{j∈Ω(i)} α(i,j) · V(j)
```

where **V(j)** denotes the value vector associated with key position **j**.

---

## Operator Semantics

The sparse-local attention operator computes the standard scaled dot-product attention restricted to a causal local neighborhood defined by the window parameter **W**.

Only keys belonging to the admissible set **Ω(i)** participate in the attention computation. No attention scores or attention weights are computed for positions outside this set.

This specification defines the mathematical behavior of the sparse-local attention operator independently of any software implementation.

It does **not** define:

- implementation details;
- GPU kernel architecture;
- compiler optimizations;
- hardware-specific optimization strategies;
- proprietary implementation details.

The mathematical operator specified above is the reference semantics evaluated by the Lanzarini Validation Suite.
