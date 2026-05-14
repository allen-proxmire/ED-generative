# Paper_093 — The Kernel-Level Arrow of Time (Theorem T18)

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the kernel arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: §5.3 compositional-closure clarification; §10.3 Wheeler–Feynman engagement)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/wedges/Paper_093_KernelArrow.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_008_KernelArrow_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops the **kernel-level arrow of time (Theorem T18)** as a downstream structural consequence of the postulated primitives. Given P11 (commitment irreversibility), V1's finite-width structure (Paper #18), and the **substrate-operational compositional-closure requirement** of substrate kernel rule-types, the V1 vacuum response kernel is structurally constrained to have **strictly retarded temporal support**:

$$
K_{V1}(x, x') \propto \theta(t - t') \cdot G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).
$$

The argument proceeds by structural exclusion of the two alternatives. **Advanced V1** is refuted by P11 — no substrate dynamics can map post-commitment states back to their pre-commitment coherent superpositions. **Symmetric V1** is non-constructible — backward chain contributions do not exist in the substrate's primitive inventory. The retarded V1 is the unique admissible kernel-support structure consistent with the postulated primitives.

The arrow of time produced is at the **kernel level** — a substrate-level structural commitment — *not* thermodynamic, *not* statistical, *not* boundary-condition-imposed. Cross-domain consequences: V5 cross-chain correlation (Paper #20) inherits retardation; black-hole horizons (Paper_039) decouple with substrate-level forward-causal direction; decoherence and entanglement flow forward in time at the substrate level. The paper makes no claim to derive P11 from a deeper layer, no claim that the kernel-level arrow is identical to thermodynamic or causal arrows, no claim that ED forces the primitives, and no claim that V1 is the only possible kernel in all ontologies. The empirical case rests on cross-domain reach.

---

## 1. Introduction

### 1.1 What this paper does

This paper develops **Theorem T18** — the kernel-level arrow of time — as a downstream structural consequence of the ED 13-Primitive Generative System. The structural argument proceeds in three steps:

1. **V1 admissible-class structure (Paper #18).** The substrate's vacuum response kernel V1 is constrained to a finite-width, Lorentz-covariant, UV-FIN-compatible admissible class. The *temporal-support* property of V1 is left open by Paper #18 — it could in principle be retarded (forward-only), advanced (backward-only), or symmetric (both).

2. **Refutation of advanced V1 (§5).** Advanced V1 would require substrate-level mechanism propagating content backward in time. P11 commitment irreversibility forbids this.

3. **Non-constructibility of symmetric V1 (§6).** Symmetric V1 would require both forward-propagating *and* backward-propagating chain contributions. Chains in ED are forward-causal by construction; backward-causal chain contributions do not exist as substrate-level primitive content.

The unique survivor: **retarded V1**, with $K_{V1}(x, x') \propto \theta(t - t') \cdot G(\sigma(x, x')/\ell_{\mathrm{ED}}^2)$.

### 1.2 Why the kernel-level arrow is a wedge

Standard physics has multiple accounts of the arrow of time — thermodynamic, radiative, cosmological, quantum-measurement, CP-violation. None is fundamental in the substrate-ontological sense; each is emergent or boundary-condition-imposed within a fundamentally time-symmetric framework.

ED supplies a **structural arrow at the kernel level**: the substrate's V1 vacuum kernel is *structurally* retarded because the substrate's primitive structure (P11) makes advanced and symmetric alternatives non-constructible. This is structurally deeper than any standard account.

This matters for three reasons:

- **Foundational unification.** Standard time-asymmetric phenomena inherit from the kernel-level arrow.
- **No initial-condition requirement.** Unlike thermodynamic-arrow accounts.
- **Cross-domain consistency.** V5's retardation, horizon forward-causality, decoherence directionality, entanglement-flow direction all inherit from T18.

### 1.3 How this fits into the kernel arc

The ED kernel arc:

- **Paper #18:** V1 finite-width admissible class (Theorem N1).
- **Paper #19:** V1 retarded support (pre-pivot forcing version).
- **Paper_093 (this paper):** Wave-2 generative rewrite of T18.
- **Paper #20 / Paper_090:** V5 cross-chain correlation kernel (inheriting retardation).
- **Paper #21–#23 (in queue):** Memory-kernel cascade, Lindblad limit, kernel hierarchy.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

- **P02 (Participation as primitive relation).**
- **P04 (Bandwidth as non-negative additive scalar).**
- **P05 (Polarity-transport along edges).**
- **P07 (Channel structure as ontological primitive).**
- **P09 ($U(1)$-valued polarity).**
- **P10 (Rule-type primitive).**
- **P11 (Commitment irreversibility).** Load-bearing for this paper.
- **P13 (Time homogeneity).**

**V1 inheritance (Paper #18):** finite-width, Lorentz-covariant, UV-FIN-compatible admissible class.

**Upstream paper dependencies:** Papers #1, #18, #20, Paper_039.

**No primitive forcing is invoked.**

---

## 3. V1 Kernel Structure

### 3.1 The V1 admissible class

From Paper #18 (Theorem N1), V1 is constrained to the admissible class:

$$
K_{V1}(x, x') = G(\sigma(x, x')/\ell_{\mathrm{ED}}^2) \cdot \Theta_{\mathrm{support}}(t - t').
$$

The temporal-support function $\Theta_{\mathrm{support}}$ has three candidates:

- **Retarded:** $\Theta_{\mathrm{ret}}(t - t') = \theta(t - t')$.
- **Advanced:** $\Theta_{\mathrm{adv}}(t - t') = \theta(t' - t)$.
- **Symmetric:** $\Theta_{\mathrm{sym}}(t - t') = (1/2)[\theta(t - t') + \theta(t' - t)]$.

### 3.2 Gauge compatibility

V1's gauge compatibility under $U(1)$ phase rotations (P09) and polarity-transport (P05) holds in all three candidate support structures; the temporal-support question is independent.

### 3.3 The question of temporal support

The structural question: which of $\Theta_{\mathrm{ret}}, \Theta_{\mathrm{adv}}, \Theta_{\mathrm{sym}}$ is consistent with the substrate primitives + V1 admissible class + **substrate-operational compositional closure**?

---

## 4. Commitment Irreversibility (P11)

### 4.1 Definition

P11 is a substrate primitive: at commitment events, a chain's multi-channel participation collapses to a single channel. The collapse is discrete, environmentally-phase-randomizing, and **irreversible** — no substrate-level dynamics maps post-commitment state back to pre-commitment coherent superposition.

### 4.2 Why irreversibility is forward-causal

The substrate primitive P11 specifies that commitment events have a fixed temporal direction. Pre-commitment $\to$ commitment event $\to$ post-commitment phases randomized $\to$ post-commitment state. There is no substrate-level operation $T_{\mathrm{reverse}}$ such that $T_{\mathrm{reverse}}(\mathrm{post}) = \mathrm{pre}$. The substrate's primitive operations (P02, P04, P05, P07, P09) preserve or randomize phases — none *unrandomizes*.

### 4.3 Implication: no backward substrate propagation

Commitment-event-content propagates only forward in substrate time. A substrate channel at $(u_1, t_1)$ that has been the target of a commitment event has its post-commitment information transported only to $(u_2, t_2)$ with $t_2 > t_1$. There is no substrate-level mechanism for backward propagation.

### 4.4 What P11 does NOT say

Not entropy-increase, not preferred temporal origin (P13 forbids), not Lorentz violation, not mathematical impossibility of backward propagation (it is *non-constructible* at substrate level — different statement).

---

## 5. Refutation of Advanced V1

### 5.1 What advanced V1 would require

Advanced V1 with $\Theta_{\mathrm{adv}}(t - t') = \theta(t' - t)$ would mean V1 propagates substrate vacuum-response content from $x'$ to $x$ when $t < t'$ — from later to earlier time.

### 5.2 Why P11 refutes advanced V1

Advanced V1 would require the substrate to carry information about future commitment events in earlier-time content. But P11 says no substrate operation maps pre-commitment to post-commitment outcome. The substrate cannot simultaneously satisfy:

- No substrate operation maps pre-commit to post-commit outcome (P11).
- V1 carries post-commit outcome content to pre-commit substrate loci (advanced V1).

These are contradictory. **Advanced V1 is structurally refuted by P11.**

### 5.3 Advanced V1 breaks substrate-operational compositional closure

This is the load-bearing structural-closure section, rewritten in the revision to distinguish two distinct notions of compositional closure that the original draft conflated.

**Two notions of compositional closure.**

(a) **Mathematical compositional closure.** A set of integral operators is mathematically closed under composition if their formal-integral composition $\int K_2(x, x'')K_1(x'', x')\,dx''$ is well-defined as a distribution or operator on the appropriate function space. In standard QFT, the Feynman propagator $G_F = \frac{1}{2}(G_{\mathrm{ret}} + G_{\mathrm{adv}}) - \frac{i}{2}(\text{symmetric sum})$ involves both retarded and advanced support, and its mathematical compositional structure is perfectly well-defined: time-ordered products, contour integration, $i\varepsilon$ prescriptions, and Wick rotation all produce mathematically-coherent compositions of retarded and advanced kernels. **Mixed-support kernels are mathematically compositionally closed in standard QFT.** This is not in dispute.

(b) **Substrate-operational compositional closure.** A set of substrate-level kernel rule-types is substrate-operationally closed under composition if their composition, *executed as a sequence of substrate-level operational steps on chains and channels*, produces a substrate-level kernel that is again a member of the rule-type set. The substrate-level operational steps are: participation (P02), bandwidth allocation (P04), polarity-transport (P05) along forward-causal chain edges, channel-structure access (P07), $U(1)$-polarity evolution (P09), and commitment (P11). **A substrate-level composition is operationally valid only if each step is constructible from these primitive operations.** Substrate-operational composition is distinct from mathematical integral-composition because the substrate primitives do not provide an "$i\varepsilon$ prescription" or a "Wick rotation" operation — these are mathematical tools applicable to integral operators, not substrate primitives.

**The structural-closure argument is operational, not mathematical.**

Compose $K_1 = K_{V1}^{\mathrm{ret}}$ (retarded) with $K_2 = K_{V1}^{\mathrm{adv}}$ (advanced) as substrate operations. The first step ($K_1$) transports substrate content forward in time via forward-causal polarity-transport along chain edges. The second step ($K_2$) would require transporting that content *backward* in time. Backward transport along chain edges is not a substrate-level operation: P05 polarity-transport operates along forward-causal chain edges only, and the substrate's primitive operational inventory contains no "reverse polarity-transport" or "backward chain edge" operation. The substrate-level execution of the composition has no operational step corresponding to the advanced-segment.

**Therefore mixed-support compositions are mathematically possible (in standard QFT they are routine) but substrate-operationally non-executable in ED.** The substrate cannot perform a "first forward then backward" sequence of kernel-mediated operations because the backward step has no operational realization in the substrate primitives. This is structurally distinct from saying mixed compositions are "ill-defined" — they are mathematically perfectly well-defined; they are just not *operationally constructible* from the substrate's primitive inventory.

**Why ED requires operational closure, not just mathematical closure.** ED is a substrate-ontological framework: its load-bearing claim is that substrate-level operations on chains and channels are the *primitive operational content* of the framework. A kernel rule-type that does not correspond to a substrate-level operational sequence is not a substrate-level entity; it is a mathematical structure that the framework can describe externally but cannot *generate from substrate primitives*. The substrate framework's compositional-closure requirement is therefore operational: every kernel in the substrate kernel rule-type space must correspond to a substrate-operational sequence.

Mathematically, QFT freely uses Feynman propagators, time-ordered products, and analytic-continuation tricks because QFT is a mathematical framework operating on Hilbert-space objects, not a substrate-operational framework. ED's compositional-closure requirement is one step deeper: it requires substrate-level operational executability, which excludes mixed-support kernels even though they are mathematically coherent.

**Conclusion.** Advanced V1 + retarded V1 in the same substrate kernel space is substrate-operationally non-closed. Either retarded only or advanced only — not both. Combined with §5.2 (P11 refutes advanced), the substrate-operational outcome is retarded only.

---

## 6. Non-Constructibility of Symmetric V1

### 6.1 What symmetric V1 would require

Symmetric V1 with $\Theta_{\mathrm{sym}}(t - t') = 1/2$ for all $t, t'$ would propagate substrate content equally in both temporal directions. The structural content is the sum of (forward-propagating retarded V1) + (backward-propagating advanced V1) weighted equally.

### 6.2 The backward contribution requires backward chain contributions

Symmetric V1's backward-propagating contribution requires the substrate to support **backward chain contributions** — sequences $\{(u_i, t_i)\}$ with $t_{i+1} < t_i$. These would be substrate-level objects propagating from later times to earlier times.

Chains in ED are forward-causal by construction. The substrate's primitive participation relation (P02) is between chains and channels, with the chain's temporal direction set by the substrate's primitive time orientation. There is no substrate-level operational content for backward chain contributions.

### 6.3 Why backward chain contributions are non-constructible

The substrate's primitive operations on chains and channels are participation (P02), bandwidth allocation (P04), polarity content (P09), polarity-transport (P05) along forward-causal chain edges, and commitment (P11). None *generate* backward chain content. The substrate primitive operational content is forward-causal by structural construction.

Adding backward chain contributions would require a new substrate primitive — a "backward chain primitive" or analogous structure. The current 13-primitive set does not contain such a primitive; adding one would change the substrate ontology.

**Backward chain contributions are non-constructible** in the 13-primitive substrate framework.

### 6.4 Symmetric V1 breaks substrate-operational compositional closure

Even if backward chain contributions could be constructed (hypothetically), composing symmetric V1 with itself produces kernel-content with mixed temporal-support, breaking substrate-operational compositional closure for the same reason as §5.3.

### 6.5 Summary: symmetric V1 is excluded

Two independent structural arguments exclude symmetric V1:

1. **Non-constructibility** of backward chain contributions in the substrate primitive inventory.
2. **Substrate-operational compositional non-closure** of mixed-support kernels.

---

## 7. Retarded V1 as the Unique Admissible Kernel Support

### 7.1 The structural argument

Given:

- V1 admissible class constrained per Paper #18.
- Advanced V1 refuted by P11 (§5.2) and substrate-operational non-closure (§5.3).
- Symmetric V1 non-constructible (§6).
- The substrate's primitive structure must produce *some* temporal-support structure for V1.

The unique remaining admissible support is **retarded**:

$$
\Theta_{\mathrm{support}}(t - t') = \theta(t - t').
$$

Retarded V1 properties: forward-causal, all chain content constructible from primitives, substrate-operationally compositionally closed (retarded $\circ$ retarded = retarded), gauge compatible, satisfies V1 admissible class.

### 7.2 Theorem T18 (generative form)

**Theorem T18 (kernel-level arrow of time).** *Given the postulated primitives P02 + P04 + P05 + P07 + P09 + P10 + P11 + P13 of the ED Generative System and the V1 admissible class of Paper #18, the V1 vacuum response kernel is structurally constrained to have strictly retarded temporal support:*

$$
K_{V1}(x, x') = \theta(t - t') \cdot G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).
$$

*Equivalent statements:*
- *V1 advanced support is refuted by P11.*
- *V1 symmetric support is non-constructible.*
- *V1 retarded support is the unique admissible structure.*

### 7.3 Why this is "the" kernel-level arrow

Distinguishing features: substrate-primitive level (not derived from boundary conditions); universal at kernel level (all kernel rule-types inherit); independent of thermodynamics, cosmology, measurement.

### 7.4 The arrow is not what it is sometimes mistaken for

Not thermodynamic; not statistical; not boundary-condition-imposed; not cosmological-initial-condition.

---

## 8. Cross-Domain Context

### 8.1 V5 cross-chain correlation (Paper #20 / Paper_090)

V5 inherits retarded support from V1 via substrate-operational compositional inheritance:

$$
K_{V5}(u_A, t_A; u_B, t_B) = \theta(t_A - t_B) \cdot F_{V5}(\sigma/\ell_{V5}^2, (t_A - t_B)/\tau_{V5}).
$$

### 8.2 Decoherence directionality

In ED, decoherence is forward-causal at the substrate-kernel level via T18. Thermodynamic and measurement-theoretic arguments are downstream consequences.

### 8.3 Entanglement flow

Lieb–Robinson-type bounds on entanglement propagation are forward-causal at substrate level via T18 + V5 retardation.

### 8.4 Black-hole horizon decoupling (Paper_039)

The horizon's information-blocking is forward-causal via T18.

### 8.5 Cosmic decoupling surface (Paper_029)

The cosmic decoupling surface at $R_H = c/H_0$ is forward-causal at substrate kernel level via T18.

### 8.6 Standard arrows are downstream

All standard arrows (thermodynamic, radiative, cosmological, decoherence, measurement) are downstream consequences of T18 + V5 + bandwidth-conservation.

---

## 9. What This Paper Does NOT Claim

### 9.1 No derivation of P11

P11 is a postulated substrate primitive.

### 9.2 No claim that thermodynamic irreversibility is derived here

The thermodynamic arrow inherits via DCGT + coarse-graining; not derived in this paper.

### 9.3 No claim that macroscopic arrows are identical to the kernel arrow

Each downstream arrow has its own specific operational definition.

### 9.4 No claim that ED forces the primitives

The 13 primitives are postulated.

### 9.5 No claim that V1 is the only possible kernel in all ontologies

T18 holds within the 13-primitive ED ontology; other ontologies could allow different structures.

### 9.6 No claim of CPT violation or Lorentz violation

T18 is consistent with Lorentz invariance and CPT.

### 9.7 No claim that T18 is testable at substrate scale

Direct test is not currently feasible; empirical content is via cross-domain inheritance.

### 9.8 No claim about quantum-gravity quantum-time

Outside ED's scope.

---

## 10. Falsification Criteria

### 10.1 Any observation of backward kernel propagation

**Direct empirical observation of substrate-level kernel propagation with backward-causal support** would falsify T18. Wheeler delayed-choice and similar effects are forward-causal substrate phenomena under appropriate analysis (§10.3 below).

### 10.2 Any substrate-consistent model with symmetric V1

**Demonstration that a 13-primitive substrate model with symmetric V1 is structurally consistent** would falsify T18's non-constructibility argument.

### 10.3 Wheeler–Feynman absorber theory and the symmetric-electrodynamics objection

This section is revised to engage Wheeler–Feynman directly, rather than dismissing it indirectly.

**The Wheeler–Feynman position.** Wheeler and Feynman (1945, 1949) developed an action-at-a-distance electrodynamics in which charged particles interact via a *time-symmetric* combination of retarded and advanced potentials. The resulting theory is **mathematically consistent**: it reproduces all standard electrodynamic results (Coulomb force, Lienard–Wiechert fields, radiation reaction) provided certain boundary conditions ("absorber" conditions on future infinity) are imposed. In their treatment, the *apparent* arrow of time in electromagnetic radiation arises from boundary conditions on the absorber rather than from any time-asymmetry in the equations of motion.

Wheeler–Feynman absorber theory is a serious, structurally-developed position. Its mathematical consistency is not in dispute. Naively, it might appear to challenge T18: if symmetric electrodynamics is mathematically consistent, why does ED exclude advanced propagation?

**The substrate-operational response.** T18's exclusion of advanced propagation is **substrate-operational, not algebraic**. The Wheeler–Feynman result establishes that *as algebraic structures on Hilbert space or as integral operators on spacetime*, symmetric combinations of retarded and advanced kernels are mathematically coherent and reproduce empirical electrodynamics. ED accepts this fully — at the level of mathematical Hilbert-space structure, symmetric kernels are allowed.

T18's claim operates one level below: at the level of *substrate-operational kernel execution*. Even if symmetric electrodynamics is algebraically consistent, the substrate-level question is whether the underlying kernel composition is executable as a sequence of substrate-level operations on chains and channels. The substrate's primitive operational inventory (P02, P04, P05, P07, P09, P11) supplies only forward-causal chain transport along forward-oriented edges. The advanced segment of a Wheeler–Feynman-style kernel has no operational realization in the substrate primitives — there is no substrate operation that performs backward chain transport.

**Therefore Wheeler–Feynman absorber theory is mathematically consistent but substrate-operationally non-constructible in ED.** A Wheeler–Feynman universe in which advanced propagation is physically real would require either (a) a substrate primitive set including backward chain content (which the 13-primitive ED ontology does not contain), or (b) a different ontological framework in which advanced propagation is operationally executable without backward chain transport. ED's 13-primitive ontology rules out (a) by primitive inventory; alternative frameworks (b) are not addressed by ED's substrate-operational argument.

**The empirical content of T18 vs. Wheeler–Feynman.** Wheeler–Feynman absorber theory predicts the same empirical electrodynamics as standard retarded electrodynamics — the absorber boundary condition effectively converts the symmetric combination into apparent retardation. The empirical content of T18 distinguishes from Wheeler–Feynman only through downstream-cross-domain content: V5 retardation (Paper #20 / Paper_090), substrate-level KMS structure at horizons (Paper_039), and substrate-level finite-memory cutoffs at near-Planck-scale (which Wheeler–Feynman absorber theory does not predict). If empirical observations consistent with substrate-level finite-memory cutoffs (e.g., analog-Hawking experiments showing UV cutoff, Page-curve substrate signatures) emerge, the substrate-operational mechanism is supported over Wheeler–Feynman-style algebraic-symmetric treatments.

**The structural distinction.** ED accepts the Wheeler–Feynman mathematical result while disputing its substrate-operational realization. The arrow of time in ED is *not* derivable from boundary conditions (the Wheeler–Feynman route); it is *primitive* at the substrate-operational level via P11 + the forward-causal chain-edge structure. This is the substrate-operational refinement of the philosophical claim that the arrow of time has a structurally-deeper origin than boundary conditions in time-symmetric equations of motion.

**Clarification: ED's exclusion is not an algebraic claim.** T18 does not assert that symmetric or advanced kernels are mathematically inconsistent — they are not. T18 asserts that within the substrate-operational framework of the 13-primitive ED ontology, only retarded V1 is constructible from substrate primitives. Whether *physical reality* admits advanced propagation is an empirical question; ED's answer is "no within this substrate ontology," but the answer is conditional on the ontology rather than derived from algebra.

### 10.4 V5 cross-chain correlation with advanced or symmetric support

Discovery that V5 (Paper #20 / Paper_090) has advanced or symmetric temporal support empirically would falsify the V1 → V5 retardation-inheritance argument.

### 10.5 Time-reversal symmetry of substrate-level kernel dynamics

If empirical evidence emerges that substrate-level dynamics is genuinely time-reversal-symmetric at the substrate-kernel level, T18 is falsified.

### 10.6 P11 modification or substitution

If future structural analysis identifies a substrate primitive that replaces P11 with a time-symmetric alternative reproducing all downstream content, the argument requires revision.

---

## 11. Position Statement

Theorem T18 — the kernel-level arrow of time — is a downstream structural identification in the ED Generative Primitives System:

> *Given the postulated primitives + V1 admissible class + substrate-operational compositional closure of the kernel rule-type space, V1 vacuum response is structurally constrained to have strictly retarded temporal support. Advanced V1 is refuted by P11 commitment-irreversibility and substrate-operational non-closure. Symmetric V1 is non-constructible from substrate primitives. Retarded V1 is the unique admissible structure.*

The arrow produced is at the **kernel level** — a substrate-primitive structural commitment — *not* thermodynamic, *not* statistical, *not* boundary-condition-imposed. **Wheeler–Feynman absorber theory is engaged directly (§10.3):** ED accepts the mathematical consistency of symmetric electrodynamics while excluding its substrate-operational realization within the 13-primitive ontology. The distinction is substrate-operational, not algebraic.

What this paper claims:

- Given the postulated primitives + V1 admissible class + substrate-operational compositional closure, T18 is the unique downstream structural identification.
- The substrate-level kernel arrow is structurally distinct from all standard accounts.
- V5 and downstream cross-domain phenomena inherit retardation from T18.
- The substrate-operational compositional-closure requirement is distinct from mathematical compositional closure (which allows mixed-support kernels in standard QFT and Wheeler–Feynman absorber theory).

What this paper does *not* claim:

- P11 is not derived; it is postulated.
- Thermodynamic and macroscopic arrows are not identical to the kernel arrow.
- ED does not force the primitives.
- The argument is conditional on the 13-primitive ontology.
- T18 does not algebraically refute Wheeler–Feynman or symmetric-kernel mathematical structures; it excludes their substrate-operational realization in ED.

**Series context.** Paper_093 of the wedges / kernel arc. The arc continues with Papers #21–#23 (in queue).

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Primitive load-bearing audit:** `PRIMITIVE_LOAD_BEARING_AUDIT.md` — P11 audit.
- **Paper #18 (V1 N1), #19 (V1 retarded pre-pivot):** V1 admissible-class structure.
- **Paper #20 / Paper_090 (V5):** retardation inheritance §8.1.
- **Paper_039 (Horizon Decoupling):** cross-domain context §8.4.
- **Paper_029 (Cosmic decoupling):** cross-domain context §8.5.
- **Papers #21–#23 (in queue):** memory-kernel cascade, Lindblad, kernel hierarchy.

### Glossary

- **Theorem T18.** Retarded V1 as unique admissible substrate kernel support.
- **Retarded V1.** $K_{V1} \propto \theta(t - t') \cdot G(\sigma/\ell_{\mathrm{ED}}^2)$.
- **Advanced V1.** Hypothetical kernel with backward-light-cone support. Refuted by P11.
- **Symmetric V1.** Hypothetical kernel with both support cones. Non-constructible.
- **Backward chain contributions.** Hypothetical substrate sequences with $t_{i+1} < t_i$. Non-constructible from 13 primitives.
- **Mathematical compositional closure.** Closure under formal-integral composition; standard QFT property; allows mixed-support kernels.
- **Substrate-operational compositional closure.** Closure under sequences of substrate-level primitive operations (P02, P04, P05, P07, P09, P11) on chains and channels; does not allow mixed-support kernels because advanced segments are not operationally constructible.
- **Wheeler–Feynman absorber theory.** Action-at-a-distance electrodynamics with time-symmetric retarded + advanced kernels; mathematically consistent; substrate-operationally non-realizable in ED.
- **P11 commitment irreversibility.** Substrate primitive forbidding post-commit → pre-commit substrate dynamics.
- **Synge function $\sigma(x, x')$.** Lorentz-scalar spacetime-separation measure.

---

**End of Paper_093.**

*Wave-2 Generative Paper — Kernel Arc, Foundation. Round-2 revision: §5.3 now distinguishes mathematical vs. substrate-operational compositional closure and explains why ED requires the operational variety; §10.3 engages Wheeler–Feynman absorber theory directly, accepting its algebraic consistency while excluding its substrate-operational realization within the 13-primitive ontology.*
