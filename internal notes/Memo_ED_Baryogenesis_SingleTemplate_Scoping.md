# Memo_ED_Baryogenesis_SingleTemplate_Scoping

**Series:** Wave-3 Scoping Memo (Baryogenesis closure pathway)
**Date:** 2026-05-17
**Status:** Scoping memo. Does not modify Paper_ED_Baryogenesis_Open. Does not draft the M2 → M3 upgrade memo. Defines a new candidate reduction path **R4 — Single-template admissibility under saturation** as a fourth pathway alongside the R1/R2/R3 reductions audited in `Memo_ED_BinaryChirality` (all failed). Identifies the exact substrate-graph constructive step required to close R4 and the verdict consequence chain.

**Anchors:** Paper_ED_Inflation (Cos_01, M3 — Q-C3 cascade Preamble item 5; saturation = uniform Ψ at substrate-state level); Paper_ED_Cos_05 (M3 unconditional — saturation-regime inheritance pattern); Paper_ED_Baryogenesis_Open (M2 current — P-BinaryAdmission paper-specific postulate; §3.5 asymmetric-admission-cost OPEN; two candidate mechanisms catalogued); Memo_ED_Baryogenesis_QC3_SaturationVerification (2026-05-17 verification pass — Case 3 determination); Paper_038_5 (M3 retroactive — Route A4 substrate-parameter inheritance template); `Memo_ED_BinaryChirality` (R1/R2/R3 failure record, accessed via in-line citations); `Memo_ED_ChainClass_C3_Audit` (Q-C3-2 subleading fluctuation admissibility, accessed via in-line citations); `Memo_ED_CCC_Realizability_SubConstruct` (Q-C3-3 framework-neutral IC supply, accessed via in-line citations); Paper_095 §3.2.1 (sub-label conventions).

**Purpose:** Define R4 formally. Identify the closure condition. Prepare the ground for the eventual M2 → M3 upgrade of the Baryogenesis paper without prematurely modifying it.

> ⚠️ **Correction (2026-07-06):** §"Property R4-B" below refers to "the P12 ED-threshold" as the crossing event that seeds first-arrival. That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7, itself now flagged. This does not change this memo's tier reasoning — it only corrects the primitive citation. See `event-density/docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## §1 Problem restatement

The Baryogenesis paper currently carries verdict **M2 (Intermediate Path C; form-IDENTIFIED + value-INHERITED)** with two load-bearing OPEN items:

1. **P-BinaryAdmission** (§2.3): paper-specific postulate that Paper_072 individuation in the post-SCBU ignition regime admits only $\chi_C \in \{0, \pi\}$ binary. Substrate-graph derivation is OPEN per `Memo_ED_BinaryChirality` — three reduction paths (R1 alignment-sign; R2 edge-composition parity; R3 continuous-to-binary collapse under SC-4.x) all failed.
2. **Asymmetric admission cost in saturation** (§3.5): OPEN substrate-graph derivation of *which* of the two admitted chirality classes wins under saturation. Two candidate mechanisms catalogued — kernel-arrow asymmetry (audited as overclaim, not adopted) and V5-cross-boundary phase inheritance (substrate-graph derivation OPEN, structurally newer).

The proposed reframing: the current "binary admission with asymmetric cost between two admitted classes" picture is structurally awkward and likely misframed. Under Cos_01 saturation regime (uniform Ψ + V1/V5/individuation reactivated + Q-C3 admissibility) the substrate may admit only a **single template**, not two competing chirality classes. The "first dislodged event" — the symmetry-breaking event at BBB ignition — seeds whichever chain-class it instantiates; the coherence functional + uniform-Ψ background then forces that template to tile globally; the anti-aligned chirality has *no template* to instantiate during saturation. Post-saturation slack restores symmetric admission, but the asymmetry is already globally locked.

**Verification result** (per `Memo_ED_Baryogenesis_QC3_SaturationVerification`, 2026-05-17): Case 3 — Q-C3 closes uniform-Ψ at substrate-state level (biconditional uniform-Ψ ↔ saturation per `Memo_ED_ChainClass_C3_Construct`), but does **not** constrain chain-class template multiplicity of fluctuations on top of that state. The user's reframing is a plausible third candidate mechanism (alongside kernel-arrow asymmetry and V5-cross-boundary), not currently in the corpus catalogue, requiring its own constructive substrate-graph derivation to close.

This scoping memo defines that candidate mechanism formally as **R4** and identifies the closure condition.

---

## §2 Corpus framing

The relevant corpus content for R4's candidacy:

**Cos_01 saturation framework (Paper_ED_Inflation, M3).** Q-C3 cascade closes the biconditional uniform-Ψ ↔ saturation at substrate-state level via the five-qualification chain (Q-C3-1a/1b/2/2b/3) with `Memo_ED_ChainClass_C3_Audit` ACCEPTED. Saturation IS uniform Ψ; uniform Ψ IS saturation. The substrate-state-level closure is M3 unconditional and corresponds to the global attractor of the substrate-action functional under post-SCBU ignition conditions.

**Q-C3-2 admits subleading-order fluctuations.** Verbatim from Cos_01 Preamble item 5: *"Q-C3-2: Subleading $O(\varepsilon)$ fluctuations admissible; not load-bearing for leading-order phenomenology."* The plural "fluctuations" matters: the admissible-fluctuation set is non-trivial; multiplicity is not fixed at the audit's level of resolution. This is the substrate-side admission of $\Psi$-density perturbations around the uniform-$\Psi$ saturation background — the same content that Cos_06 uses for the inflationary perturbation spectrum.

**R1/R2/R3 from `Memo_ED_BinaryChirality` (all failed) — the relevant lessons.**

- **R1 (alignment-sign):** attempted reduction of binary chirality to a substrate-graph alignment-sign quantity. Failed because Paper_089 T18 forecloses chain-level use of event-direction binary (P11).
- **R2 (edge-composition parity):** attempted reduction via edge-composition parity arguments. Failed for structural reasons not load-bearing here.
- **R3 (continuous-to-binary collapse under SC-4.x):** the *most relevant failure for R4's design*. R3 attempted to derive binary admission as a consequence of scale-collapse machinery collapsing continuous P09 polarity to a binary admissible set. It failed: continuous P09 does not collapse to binary under SC-4.x as analyzed.

The R3 failure is informative. It says: **scale-collapse alone does not collapse chirality content to a single (or binary) admissible set.** The corresponding inference for R4 is that R4 cannot rest on scale-collapse machinery alone — it must invoke the *coherence functional* + the *no-slack boundary condition* of saturation as the additional substrate-graph mechanism beyond what SC-4.x provides.

**Need for R4.** R1/R2/R3 collectively exhaust the substrate-side reductions attempted in `Memo_ED_BinaryChirality` for the binary-admission claim. R4 is structurally different from all three: it does not attempt to derive binary admission from primitives. Instead, it argues that the binary framing itself is wrong — the substrate admits one template, not two, and "binary" is a misreading of the substrate-graph admissibility structure. This is a category shift from R1/R2/R3, not a fourth reduction along the same axis.

---

## §3 Define R4: Single-template admissibility under saturation

### R4 hypothesis (formal statement)

> **R4 — Single-template admissibility under saturation.** Under Cos_01 saturation regime (uniform Ψ at substrate-state level, established biconditionally via Q-C3 cascade per `Memo_ED_ChainClass_C3_Audit`), the coherence functional governing Paper_072 individuation admits exactly one chain-class template on the Q-C3-2 subleading-fluctuation set. The substrate cannot support two distinct stable chain-class templates simultaneously during saturation because the no-slack boundary condition (capacity = demand at admission frontier) forecloses the second template's instantiation: any candidate chain-class outside the first-admitted template fails Paper_072 individuation under uniform-Ψ no-slack conditions.

Three properties follow from R4:

**Property R4-A (single template, not binary).** The substrate does not admit a "binary" chirality content $\chi_C \in \{0, \pi\}$ during saturation. It admits exactly one chain-class template, structurally. The "binary" framing was an artifact of analyzing the post-saturation regime (where both chirality classes are symmetrically admissible per §3.6 of the current paper) and projecting that symmetric-admission structure backward onto the saturation phase, where it does not hold.

**Property R4-B (asymmetry is first-arrival, not asymmetric cost).** Which chain-class template wins is not determined by an asymmetric admission cost between two pre-admitted classes. There is only one admitted class at any given moment during saturation. *Which* class that is depends on the first-arrival content — the chain-class instantiated by the first dislodged event after BBB ignition crosses the P12 ED-threshold. First-arrival is framework-neutral per `Memo_ED_CCC_Realizability_SubConstruct` (cyclic-CCC framing supplies pre-aeon inheritance content; R3 single-aeon framing supplies a structural-initial-condition assumption; the choice between these is outside scope, and either supplies the first-arrival selection).

**Property R4-C (post-saturation symmetric admission restoration).** Post-saturation, as substrate event-density relaxes below capacity, the no-slack boundary condition is lifted; the coherence functional no longer forecloses the second template. Both chain-class templates become symmetrically admissible. Symmetric pair-production resumes (as the current paper's §3.6 already identifies). The asymmetry from the saturation phase persists because the matter content accumulated during saturation is already globally instantiated and bound; the post-saturation antimatter content can only form locally and cannot tile back to overturn the global lock-in.

### How R4 absorbs P-BinaryAdmission (no new postulate)

P-BinaryAdmission as currently written declares: *"In the post-SCBU ignition regime, Paper_072 individuation admits only chain-arrow chirality values $\chi_C \in \{0, \pi\}$ (binary)."* Under R4, this postulate is absorbed into Q-C3-2 admissibility + coherence-functional no-slack collapse — no new postulate beyond what the corpus already carries. Specifically:

- The "binary" content $\{0, \pi\}$ is reinterpreted as the *post-saturation* symmetric-admission set (where both classes are admissible without restriction).
- During saturation, R4 says the admissibility collapses to a single template via the coherence functional under uniform-Ψ no-slack conditions.
- The chirality content of the admitted template is whichever class first-arrival selects; both $\chi_C = 0$ and $\chi_C = \pi$ are equally probable a priori (framework-neutral); the actual selection is by IC, not by asymmetric cost.

This eliminates P-BinaryAdmission as a paper-specific postulate: the corpus carries Q-C3-2 admissibility + Paper_072 individuation + coherence functional + IC-INHERITED first-arrival per `Memo_ED_CCC_Realizability_SubConstruct`. Nothing new declared.

### How R4 dissolves the asymmetric admission cost OPEN

The current §3.5 OPEN requires three substrate-graph derivations: (i) a cost function $C_{\mathrm{admit}}(\chi_C)$, (ii) a derivation that $C_{\mathrm{admit}}(0) \neq C_{\mathrm{admit}}(\pi)$, and (iii) a determination of which class has lower cost. Under R4, none of these are required: there is no asymmetric cost between two admitted classes because **only one class is admitted at any moment during saturation**. The asymmetry is structural (single-template admission) + framework-neutral IC (first-arrival selection), not dynamical-cost-driven.

### How first-arrival IC produces global chirality lock-in

Under R4, the post-SCBU ignition substrate enters saturation with uniform Ψ. The first dislodged event (the symmetry-breaking event that establishes the first admitted chain-class template) instantiates a chain-class with a specific chirality value (either $\chi_C = 0$ or $\chi_C = \pi$, framework-neutrally selected). The coherence functional under uniform-Ψ no-slack conditions forecloses subsequent admission of any chain-class outside the first-admitted template. V1 retarded propagation + V5 cross-chain coupling on the uniform-Ψ background then carry the first-admitted template across cosmic-scale loci; the substrate tiles globally with one chirality class.

This is the substrate-side substrate-ontology analog of spontaneous symmetry breaking, but with a *stronger* mechanism than the continuous-order-parameter case in standard QFT: the substrate-graph admissibility structure forces single-template admission *structurally*, not by selection from a degenerate vacuum manifold. The "spontaneous" character is preserved (framework-neutral selection of which chirality class) but the "symmetry breaking" character is sharpened (only one admitted, not one selected from a manifold of equally-vacua).

---

## §4 Required substrate-graph derivation

R4 closure requires **one** constructive substrate-graph derivation:

> **Constructive step.** Show that coherence-functional minimization on the Q-C3-2 admissible-fluctuation set, under uniform-Ψ no-slack boundary conditions of the saturation regime, yields a unique chain-class template. Equivalently: show that any candidate second template (a chain-class outside the first-admitted one) fails Paper_072 individuation under the same conditions, with the failure mechanism traced to the no-slack admission frontier.

**What must be shown to close R4 affirmatively:**

1. A well-defined coherence functional $\mathcal{F}_{\mathrm{coh}}[\chi_C; \Psi^{\mathrm{const}}]$ acting on the Q-C3-2 admissible-fluctuation set with the chain-class chirality as argument.
2. The functional is bounded below on the Q-C3-2 admissible set under uniform-Ψ no-slack conditions.
3. The minimum is attained at a unique chain-class template (not a degenerate manifold of templates).
4. The uniqueness traces structurally to the no-slack boundary condition — i.e., the same functional admits multiple stable minima when slack > 0 (post-saturation regime), recovering the §3.6 symmetric-admission restoration.

**What would falsify R4:**

- **Direct falsification:** explicit construction of two distinct chain-class templates, both stable on the Q-C3-2 admissible set, both satisfying Paper_072 individuation, both under uniform-Ψ no-slack saturation conditions. This would refute single-template admissibility and reduce R4 to the same status as R1/R2/R3 (failed reduction path).
- **Indirect falsification:** demonstration that the coherence functional is not well-defined on the Q-C3-2 admissible set (e.g., unbounded below; ill-posed boundary value problem); or demonstration that no-slack does not act as a structural admission-frontier constraint at substrate level (e.g., capacity-demand framing is not load-bearing on individuation).

**Estimated difficulty.** The constructive step requires substrate-graph machinery similar to Cos_01's Q-C3 audit cascade — i.e., a substrate-action functional analysis on the Q-C3-2 fluctuation content under specified boundary conditions. The corpus already has the substrate-action functional structure (per Paper_ED_SC_4_9) and the Q-C3-2 admissibility content; what is missing is the coherence-functional analysis specifically under no-slack conditions. This is substrate-research-frontier work but is bounded — it has a specific functional to construct and a specific boundary condition to impose, not an open-ended exploration.

---

## §5 Consequences for the Baryogenesis verdict

Three outcomes, each with a clear verdict consequence:

**Outcome A — R4 derivation succeeds (single-template admission constructively shown).**

Baryogenesis upgrades from M2 to **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) per Paper_095 §3.2.1**, via the inheritance chain:

- Cos_01 saturation (M3 unconditional) → uniform Ψ at substrate-state level
- Q-C3-2 admissibility → subleading fluctuation set
- Coherence functional under no-slack → single-template admission (R4 construction)
- `Memo_ED_CCC_Realizability_SubConstruct` → framework-neutral first-arrival IC

P-BinaryAdmission is absorbed into Q-C3-2 + R4 + coherence functional (no new paper-specific postulate). The §3.5 asymmetric-admission-cost OPEN is dissolved (no asymmetric cost; single-template admission). $\eta_B$ remains INHERITED via empirical matching. The structural origin of matter–antimatter asymmetry closes at M3, paralleling Cos_05's M3 unconditional structure exactly.

**Outcome B — R4 derivation fails (two distinct stable templates constructible under no-slack).**

Baryogenesis remains **M2** but with a sharper OPEN framing. P-BinaryAdmission stays declared. The §3.5 OPEN reframes — the structural picture is now confirmed to be "two admitted classes + asymmetric cost," which kicks the closure responsibility back to either the kernel-arrow asymmetry route (currently overclaim, not adopted) or the V5-cross-boundary route (currently OPEN). R4's status moves from "candidate mechanism" to "failed reduction path R4" alongside R1/R2/R3 in `Memo_ED_BinaryChirality`.

**Outcome C — R4 derivation yields partial closure (stability selection but not unique single template).**

The coherence-functional minimization may yield a unique template under one set of boundary conditions and a near-degenerate manifold under another. In that case, R4 provides a **dynamical stability-selection mechanism** that picks one chain-class with high probability without strictly excluding the second. This would partially close the Baryogenesis OPEN — the asymmetric admission cost is dissolved (no cost between two admitted classes; instead, stability-selection probability difference between near-degenerate templates), but the closure tier sits between M2 and M3. Likely outcome: **M2 with significantly sharpened OPEN** + a quantitative substrate-graph identification of the stability-selection probability (which could be empirically tested against $\eta_B$ but not derive its specific value).

---

## §6 Recommended next steps

**Recommend a three-phase plan, conditional on early findings:**

**Phase 1 (immediate, ~2 weeks scope): Constructive R4 derivation attempt.** Draft a working substrate-graph construction memo titled `Memo_ED_CoherenceFunctional_SingleTemplate_Construct` that attempts the closure step in §4 directly. The construction is bounded (coherence functional on Q-C3-2 admissible set under no-slack) and the corpus has the needed machinery (Paper_ED_SC_4_9 substrate-action functional + Q-C3-2 admissibility content from `Memo_ED_ChainClass_C3_Audit`). Outcome determines verdict path per §5.

**Phase 2 (conditional on Phase 1 outcome): Audit and paper-level integration.**

- *If Phase 1 yields Outcome A:* Draft `Memo_ED_CoherenceFunctional_SingleTemplate_Audit` confirming the construction. Then draft the Baryogenesis M2 → M3 upgrade memo (`Update_Paper_ED_Baryogenesis_M3_via_R4`) applying the upgrade to the paper — Preamble items revised (P-BinaryAdmission absorbed, asymmetric-admission-cost OPEN dissolved), audit table updated with R4 closure row, §1 / §3.5 / §6 verdict-sync updated.
- *If Phase 1 yields Outcome B:* Add R4 to `Memo_ED_BinaryChirality` as a fourth failed reduction path. Baryogenesis paper unchanged. Refocus closure attempts on the V5-cross-boundary candidate or look for entirely new candidate mechanisms.
- *If Phase 1 yields Outcome C:* Decide whether partial closure is sufficient for the current corpus state or whether to push for stricter single-template uniqueness. Likely outcome: keep paper at M2 with sharpened OPEN; record R4 as partial-closure candidate; revisit when adjacent substrate-research-frontier work (Route A4 tightening; SC-4.x deeper analysis) opens additional pathways.

**Phase 3 (independent of R4 outcome): Verify with direct memo access.** The current verification and scoping work are indirect — based on in-line memo citations rather than direct memo text. If `Memo_ED_BinaryChirality`, `Memo_ED_ChainClass_C3_Audit`, `Memo_ED_CCC_Realizability_SubConstruct`, and `Memo_ED_V5PhaseContent` can be brought onto disk (or located in an archive), a direct-read verification should confirm the Case 3 determination in `Memo_ED_Baryogenesis_QC3_SaturationVerification`. Direct-read might also reveal R4-relevant content not visible to the indirect verification (e.g., if any memo already contains coherence-functional analysis under no-slack conditions, that content would directly accelerate Phase 1).

---

**End Memo_ED_Baryogenesis_SingleTemplate_Scoping.**
