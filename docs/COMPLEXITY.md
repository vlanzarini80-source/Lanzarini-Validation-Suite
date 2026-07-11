# Computational Complexity

This document defines the canonical computational complexity analysis of the sparse-local attention operator evaluated by the Lanzarini Validation Suite.

It should be interpreted together with:

- `docs/SPECIFICATION.md`
- `paper/METHOD.md`
- `docs/BENCHMARK_SCOPE.md`

The analysis presented here concerns only the mathematical operator and must not be interpreted as a guarantee of runtime performance on any particular implementation or hardware platform.

## Purpose

This document describes the computational complexity of the sparse-local attention operator specified in `docs/SPECIFICATION.md`.

The analysis refers to the mathematical operator only.

It does not describe proprietary implementation details, GPU kernel architecture, tiling strategy, memory scheduling, compiler optimization or hardware-specific implementation choices.

---

## Operator Recap

For a sequence of length **N**, head dimension **d**, value dimension **d_v**, and local attention window **W**, the sparse-local attention operator restricts each query position **i** to the admissible key set:

```text
Ω(i) = { j ∈ {0,...,i} : i − j ≤ W }
```

Each query attends only to keys inside the causal local window.

---

## Dense Attention Complexity

Standard dense causal attention evaluates attention over all previous positions.

For sequence length **N**, the number of score evaluations is approximately:

```text
O(N²)
```

Including head dimension **d**, the score computation complexity is:

```text
O(N² · d)
```

This quadratic scaling becomes expensive for long sequences.

---

## Sparse-Local Attention Complexity

Sparse-local attention restricts each query to at most **W + 1** admissible keys.

Therefore, the number of score evaluations is approximately:

```text
O(N · W)
```

Including head dimension **d**, the score computation complexity is:

```text
O(N · W · d)
```

When **W << N**, this reduces the asymptotic attention computation from quadratic in sequence length to linear in **N** for fixed **W**.

---

## Output Accumulation Complexity

The attention output requires accumulating value vectors over the admissible local window.

For value dimension **d_v**, the output accumulation complexity is:

```text
O(N · W · d_v)
```

When **d = d_v**, the total operator-level complexity is commonly summarized as:

```text
O(N · W · d)
```

---

## Memory Considerations

The mathematical operator does not require materializing the full dense attention matrix of size:

```text
N × N
```

The local attention structure only requires attention over the causal window.

At the mathematical level, the active attention domain has size:

```text
O(N · W)
```

instead of:

```text
O(N²)
```

Actual GPU memory usage depends on implementation-specific choices and is outside the scope of this document.

---

## Comparison with Dense Attention

| Attention Type | Active Attention Domain | Score Complexity |
|---|---:|---:|
| Dense causal attention | O(N²) | O(N² · d) |
| Sparse-local causal attention | O(N · W) | O(N · W · d) |

For fixed **W**, sparse-local attention scales linearly with sequence length **N**.

For **W ≈ N**, sparse-local attention approaches dense causal attention complexity.

---

## Scope of This Analysis

This document analyzes the mathematical complexity of the sparse-local attention operator.

It does **not** claim:

- universal runtime speedup;
- universal energy reduction;
- hardware-independent performance advantage;
- superiority over FlashAttention or other optimized backends;
- end-to-end serving improvement.

Runtime performance depends on hardware, software stack, tensor layout, kernel implementation, memory bandwidth, sequence length, attention window and benchmark methodology.

---

## Interpretation

The mathematical advantage of sparse-local attention comes from reducing the active attention domain from **O(N²)** to **O(N · W)**.

However, practical performance depends on whether an implementation can exploit this reduced domain efficiently on the target hardware.

For this reason, the Lanzarini Validation Suite treats performance as an experimental property rather than a theoretical guarantee.
