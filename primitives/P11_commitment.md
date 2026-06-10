# P11 — Commitment with environmental phase-randomization, irreversible

**Canonical primitive of the ED Generative System.**
**Position paper reference:** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1.4.

---

## Canonical statement

Discrete substrate-level events at which a chain's multi-channel participation collapses to a single channel, with phase-randomization on a uniform $U(1)$ distribution. Commitment is **irreversible** — no substrate-level dynamics maps a post-commitment state back to its pre-commitment superposition.

P11 supplies:
- The directional content of time (kernel-level arrow, Theorem T18 / Paper 093).
- The retardation property of the V1 kernel (substrate-operational compositional closure, Paper 089 + Paper 093 §5–§6).
- The substrate-level analog of quantum-measurement collapse (Paper 005 projective measurement).
- The second-law-like structure of substrate entropy (via P-T18-Arrow-Inheritance + DCGT coarse-graining).

## Honest framing of arrow-of-time redundancy

The arrow of time is supplied **jointly** by P11 + P13 + V1's retardation property. Whether these three are minimally independent commitments, or whether some are derivable from the others, is structurally open. P11 + P13 alone do not force V1 retardation (the structural-exclusion argument in Paper 093 §5–§6 requires both); but V1 retardation also follows from substrate-operational compositional closure on P02 + P05 + P11. The corpus has not formalized which of these three is the minimal foundational arrow-source.

## Clarification (content decomposition; resolves the redundancy note above)

P11 bundles three separable contents: **(a)** the *directional arrow* of time; **(b)** *irreversibility proper* — the many-to-one multiplicity collapse / non-invertibility ("no substrate operation maps post-commitment back to pre-commitment"); and **(c)** U(1) *phase-randomization*. Only **(b)** is primitive. The directional arrow **(a)** is *derived*, not posited: T18 (Paper 093) obtains the kernel-level arrow from P11 + P13 (+ V1 admissibility), and advanced V1 is *refuted by* P11. So V1 retardation is **downstream** of P11, not a basis for reducing it.

This resolves the redundancy note above. An arrow cannot be obtained from a symmetry: P13 (time-translation invariance + event-discreteness) is time-reversal-compatible and supplies no direction, so the temporal asymmetry must originate in content **(b)**. Reducing P11 to P13 + V1-retardation would therefore be circular — V1-retardation is one of P11's own downstream expressions (both corpus derivation routes take P11 as a premise). The reducible/derived member of the trio {P11, P13, V1-retardation} is **V1-retardation**, not P11; P11 (via content **b**) and P13 remain independent primitives.

This is a clarification of what is primitive versus derived within P11's existing content, not an ontology change: the canonical statement, the audit verdict, and all downstream derivations are unaffected.

## Audit verdict

LOAD-BEARING. Foundational dynamical-direction commitment.

## Underlying concept treatments

- `concepts/commitment.md` — the discrete event in which a chain selects one channel; the process-level treatment of how a commitment occurs.
- `concepts/individuation.md` — the threshold concept of when a sub-structure counts as distinct identity. Commitment is the substrate-level mechanism that produces individuation; the individuation file develops the threshold-dynamics side.
