# P10 — Rule-type primitive

**Canonical primitive of the ED Generative System.**
**Position paper reference:** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1.4.

---

## Canonical statement

The substrate supports multiple structurally distinct rule-types $\tau_\bullet$, each with its own participation measure. Matter and gauge are *different rule-types*, not different states of the same one.

The V1 (finite-width retarded vacuum kernel, Paper 089) and V5 (cross-chain finite-memory correlation kernel, Paper 090) are rule-types in this sense — distinguishable substrate-level dynamical objects, not states of a single underlying kernel.

## Audit verdict

LOAD-BEARING. Supplies the structural distinction between matter and gauge content (Paper 015 T17), the multi-rule-type composition for non-Abelian gauge theory (Paper 016, Paper 018), the rule-type bundle on which gauge connections live, and the V1 / V5 kernel-hierarchy distinction underlying the entire kernel-arc structure.

## Underlying concept treatments

- `concepts/multiplicity.md` — the count of distinct channels available to a chain; the integer-valued aspect of rule-type instantiation. Closely related to the Q-Compute multiplicity-cap $\mathcal{M}_{\mathrm{cap}}$ (Paper 053).

Note: "multiplicity" in `concepts/multiplicity.md` is primarily about *channel* count rather than *rule-type* count. P10 is about the rule-type primitive (allowing multiple kernel-class rule-types like V1, V5); the concept file is closer to Q-Compute $\mathcal{M}_{\mathrm{cap}}$ structure. The two share the integer-valued cardinality-of-options theme but refer to different substrate features.
