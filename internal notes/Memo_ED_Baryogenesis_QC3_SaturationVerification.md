# Memo_ED_Baryogenesis_QC3_SaturationVerification

**Series:** Wave-3 Verification Memo (Baryogenesis closure pathway)
**Date:** 2026-05-17
**Status:** Verification-only. Does not modify Paper_ED_Baryogenesis_Open. Does not draft the upgrade memo. Determines which of Case 1 / Case 2 / Case 3 holds re: Q-C3 chain-class admissibility under uniform-Ψ saturation, and the consequence for the M2 → M3 upgrade pathway.

**Anchors (papers consulted directly):** Paper_ED_Inflation (Cos_01, M3 — Preamble item 5 + audit-row content for Q-C3 cascade); Paper_ED_Cos_05 (M3 — saturation-regime inheritance pattern); Paper_ED_Baryogenesis_Open (current M2 — Preamble + §3.4 + §3.5 + Memo cross-references); Update_Paper_095_LabelClasses_2026_05_17 (§3.2.1 sub-label conventions).

---

## 0. Access caveat (important)

The verification task specified six upstream files: `Memo_ED_ChainClass_C3_Audit`, `Memo_ED_BinaryChirality`, `Memo_ED_V5CrossBoundary_ChiralityPreference`, `Memo_ED_CCC_Realizability_SubConstruct`, `Update_Paper_ED_Cos_05_M3_Unconditional`, `Update_ED_SC_4x_Arc_M3`.

**None of these exist as separate files in the working repository.** They are cited as anchors throughout the Cosmology / Dynamics arcs (most prominently in Paper_ED_Inflation Preamble item 5 and §2 substrate-research-support block, and in Paper_ED_Baryogenesis_Open §2.2 + §3.5) but their text is not accessible for direct read.

**Verification pathway used.** Memo content was inferred from in-line claims in the papers that cite them — specifically Paper_ED_Inflation (which lifts out the five Q-C3 qualifications by name in Preamble item 5) and Paper_ED_Baryogenesis_Open (which describes Memo_ED_BinaryChirality's three failed reduction paths R1/R2/R3 in Preamble item 2 + §3.3 closing paragraph). The verification is **indirect** in this strict sense; a direct memo-text read would tighten or weaken the determination by at most one case (e.g., Case 3 → Case 2 if a memo claim turns out stronger than the in-line summary suggests).

Without that caveat the memo would overclaim. With it, the verification below is the strongest defensible determination from what is on disk.

---

## 1. Summary of the question

The Baryogenesis paper sits at M2 with two OPEN load-bearing items:

- **P-BinaryAdmission** (§2.3) — paper-specific postulate that Paper_072 individuation in the post-SCBU ignition regime admits only $\chi_C \in \{0, \pi\}$ binary. Substrate-graph derivation OPEN per `Memo_ED_BinaryChirality` (three reduction paths R1/R2/R3 all fail).
- **Asymmetric admission cost in saturation** (§3.5) — OPEN substrate-graph derivation of *which* of the two admitted chirality classes wins under saturation. Two candidate mechanisms flagged (kernel-arrow asymmetry — audited as overclaim, not adopted; V5-cross-boundary — substrate-graph derivation OPEN).

The user's proposed reframing: under Cos_01 saturation regime + Q-C3 admissibility, the substrate supports a **single-template admission** (not two competing chirality classes with one cost-suppressed); the "first dislodged event" seeds whichever chain-class it happens to be; the coherence functional + uniform-Ψ background forces that pattern to tile globally; the anti-aligned chirality has *no template* to instantiate. Post-saturation slack restores symmetric admission, but the asymmetry is already globally locked in.

The question: **Is Q-C3 chain-class admissibility under uniform-Ψ saturation already single-template (Case 1), multi-template with dynamical-stability selection (Case 2), or unconstrained at the multiplicity level (Case 3)?**

---

## 2. Findings from each accessible source

### 2.1 Paper_ED_Inflation (Cos_01) — Q-C3 cascade content

Preamble item 5 lifts out the five qualifications carried by the C3 audit. Verbatim:

- **Q-C3-1a:** Branch (b) Lagrangian-degeneracy exclusion via V1 + V5 primitive-set consistency.
- **Q-C3-1b:** Sign-definite kinetic structure in $\mathcal{L}_{\mathrm{sub}}$ assumed.
- **Q-C3-2:** Subleading $O(\varepsilon)$ fluctuations admissible; not load-bearing for leading-order phenomenology.
- **Q-C3-2b:** Measure-zero kernel-balance exception class in converse direction; not load-bearing for generic configurations.
- **Q-C3-3:** Uniform-Ψ substrate-graph realizability is IC-INHERITED framework-neutrally — supplied by either Paper_ED_CCC §3.7 (cyclic framing) or R3 single-aeon framing.

§2 substrate-research-support block describes `Memo_ED_ChainClass_C3_Construct` as: *"saturation chain-class identification; **biconditional uniform-Ψ ↔ saturation**."*

**Direct relevance to the verification question:**

- The biconditional `uniform-Ψ ↔ saturation` is about the *substrate state* at leading order (the saturation regime IS uniform Ψ, and vice versa). This is the **load-bearing closure** for Cos_01's M3 verdict.
- **Q-C3-2 admits "subleading $O(\varepsilon)$ fluctuations"** — note plural "fluctuations". The claim is admissibility of the fluctuation content; it does **not** specify that the admissible fluctuation set is single-template.
- Cos_01 explicitly treats the fluctuation content as not load-bearing for its M3 phenomenology — fluctuations are admitted, but their template multiplicity is not constrained by Q-C3 as cited in the Cos_01 Preamble.

**Inference about `Memo_ED_ChainClass_C3_Audit`'s position on template multiplicity:** the in-line characterization gives no evidence that the audit closes single-template admission under saturation. It closes uniform-Ψ as the substrate state under saturation, and admits subleading fluctuations on top. The chirality content of those fluctuations is not the C3 audit's subject matter as cited.

### 2.2 Paper_ED_Baryogenesis_Open — Memo_ED_BinaryChirality content

Preamble item 2 verbatim: *"Three reduction paths attempted in `Memo_ED_BinaryChirality` (alignment-sign R1, edge-composition parity R2, continuous-to-binary collapse R3) all fail to close. Binary admission is declared as paper-specific postulate **P-BinaryAdmission**; substrate-graph derivation is OPEN."*

§3.3 closing paragraph verbatim: *"The corpus has event-direction binary (P11) but Paper_089 T18 forecloses its use at chain level, and continuous P09 polarity does not collapse to binary under SC-4.x. P-BinaryAdmission encodes the binary-restriction structurally pending substrate-graph closure."*

**Direct relevance to the verification question:**

- **R3 specifically failed** — and R3 is the "continuous-to-binary collapse" path, which is *precisely* the substrate-side mechanism by which saturation would collapse the continuous P09 chirality content to a single (or binary) template. The Baryogenesis paper authors already attempted this reduction and it did not close.
- This is the strongest single piece of evidence against Case 1. If R3 had closed, the corpus would already have substrate-graph derivation of single-template admission under saturation, and P-BinaryAdmission would not need to be declared.
- The §3.3 closing observation that "continuous P09 polarity does not collapse to binary under SC-4.x" is direct evidence that scale-collapse machinery (which includes saturation-regime entry) does not — at least at the level the corpus has analyzed it — collapse the chirality content to a single or binary admissible set.

### 2.3 Paper_ED_Baryogenesis_Open — V5-cross-boundary candidate

§3.5 verbatim on the V5-cross-boundary candidate: *"V5 cross-boundary memory at SCBU carries phase-bearing content from pre-aeon substrate. Post-boundary new chains have access to V5-delivered pre-aeon phase content as alternative phase reference distinct from $\pi_K^{\mathrm{post}}$. Asymmetric admission may emerge as substrate-graph inheritance of pre-aeon chirality preference. Substrate-graph derivation OPEN; structurally newer candidate worth pursuing in future work."*

**Direct relevance:** the V5-cross-boundary candidate is a *different* mechanism than the user's proposed first-arrival template lock-in. V5-cross-boundary appeals to pre-aeon phase content as the symmetry-breaking source. The user's reframing appeals to the saturation-regime structure itself (single-template admission). The two mechanisms are not equivalent.

This means: the user's proposed mechanism is **not currently in the corpus's catalogued candidate list**. It is a third distinct candidate, structurally newer than either kernel-arrow asymmetry or V5-cross-boundary.

### 2.4 Paper_ED_Cos_05 (Dark Energy) — saturation-regime inheritance pattern

Cos_05's M3 unconditional verdict inherits the same Cos_01 + Q1A + Q2A + C3 + IC-INHERITED chain as the Inflation paper. The inheritance pattern is: *saturation regime = uniform Ψ at substrate level → continuum stress-energy collapses to vacuum-energy form with $w = -1$ via Q1A + Q2A composition → late-LDE expansion behavior at continuum level.*

**Direct relevance:** Cos_05 does not address chirality content or chain-class template multiplicity. Its M3 inheritance from saturation regime is at the substrate-state level (uniform Ψ), not at the fluctuation-template level. This corroborates §2.1: Q-C3 saturation closure operates at the substrate-state level, not at the chain-class multiplicity level.

### 2.5 Cross-corroboration: `Memo_ED_CCC_Realizability_SubConstruct`

Cited in Cos_01 Preamble item 5 as supplying *"Q-C3-3 verified at IC-INHERITED level framework-neutrally"* — i.e., uniform-Ψ realizability is supplied by either CCC §3.7 cyclic framing OR R3 single-aeon framing, with the choice between them outside scope.

This addresses the initial-condition supply for the saturation regime (the *substrate state*), not the chain-class admissibility of fluctuations on top of it.

---

## 3. Determination — Case 3 (with one important nuance)

**Case 1 is ruled out** by §2.2 finding: R3 ("continuous-to-binary collapse") in `Memo_ED_BinaryChirality` was explicitly tried and explicitly failed. If Q-C3 closed single-template admission under saturation, R3 would have closed via that pathway. R3's failure is direct corpus-level evidence that single-template admission is not derivable from existing Q-C3 + SC-4.x machinery as analyzed.

**Case 2 is partially in play** but weakly. Q-C3-2 admits "subleading $O(\varepsilon)$ fluctuations" (plural) — meaning the admissible-fluctuation set is non-trivial. A coherence-functional-driven stability-selection argument could in principle pick one template from the admissible set. But: (a) the corpus has no current constructive derivation of such a coherence-functional argument for chirality content specifically; (b) the V5-cross-boundary candidate (the corpus's current candidate stability mechanism) appeals to pre-aeon inheritance, not to coherence-functional dynamics on the post-SCBU substrate. The Case 2 pathway is open but not currently constructed.

**Case 3 is correct as the honest determination.** Q-C3 closes saturation = uniform Ψ at the substrate-state level (Q-C3-1a/1b/2/2b/3 cascade). It does **not** constrain template multiplicity of the fluctuation content. The user's first-arrival single-template-lock-in mechanism is a **plausible third candidate** for closing the OPEN, structurally cleaner than the kernel-arrow and V5-cross-boundary candidates already on file, but it requires its own constructive substrate-graph derivation.

**Important nuance — the OPEN is sharply reframed, not just relocated.** Even though Case 3 holds, the user's reframing materially improves the Baryogenesis paper's framing of its OPEN:

- **Before:** "Two chirality classes admitted by P-BinaryAdmission; asymmetric admission cost between them OPEN; which one wins, OPEN; why the cost is asymmetric, OPEN."
- **After (under user reframing):** "Single-template admission under saturation; first-arrival selects the template; asymmetry is framework-neutral first-arrival, not asymmetric cost between two admitted classes."

The reframed OPEN has one substrate-graph derivation to construct (single-template admission via coherence-functional under saturation) rather than three (asymmetric cost function existence + asymmetry + sign-selection). It is **substantially more tractable** even if not yet closed. And it eliminates the awkward "binary admission + cost-suppression" picture that the current paper carries as a paper-specific postulate plus an OPEN load-bearing item.

---

## 4. Consequences for the Baryogenesis verdict

**Current verdict:** M2 (Intermediate Path C) with P-BinaryAdmission paper-specific postulate + asymmetric-admission-cost OPEN.

**Post-reframing verdict (without new substrate-graph derivation):** M2 tightened — same tier, sharper OPEN. The reframing reduces from "two competing chain-classes + asymmetric cost" to "single-template admission + first-arrival selection." Tractability of the OPEN improves substantially; the verdict tier does not change because the substrate-graph closure of single-template admission has not been constructed.

**Post-reframing verdict (with successful single-template constructive derivation):** **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED)** via Cos_01 saturation + Q-C3 + single-template admission + IC-INHERITED first-arrival per `Memo_ED_CCC_Realizability_SubConstruct` framework-neutrality. This would parallel Cos_05's M3 unconditional structure exactly. $\eta_B$ would remain INHERITED; the *structural origin* of the asymmetry would close at M3.

**Upgrade pathway clarity:** the upgrade is **not fully supported** from existing corpus content. It is **conditionally supported pending construction of one substrate-graph derivation** — the single-template-admission constructive argument from coherence functional under uniform-Ψ saturation.

This is exactly Case 2's "one constructive stability argument needed" outcome in spirit, but routed through Case 3's honest acknowledgment that Q-C3 itself does not currently constrain template multiplicity.

---

## 5. Recommended next action

**Recommend: option (c) from prior conversation — draft a scoping memo, not the paper upgrade.**

Specifically: produce `Memo_ED_Baryogenesis_SingleTemplate_Scoping` that:

1. **Articulates the user's first-arrival single-template mechanism** in corpus formalism (Cos_01 saturation + Q-C3 admissibility + coherence functional + IC-INHERITED first-arrival per `Memo_ED_CCC_Realizability_SubConstruct`).
2. **States the constructive substrate-graph derivation needed** to close single-template admission: a coherence-functional argument operating on the Q-C3-2 subleading-fluctuation set under uniform-Ψ saturation, deriving that only one chain-class template is dynamically admissible (others fail Paper_072 individuation under saturation-regime no-slack conditions).
3. **Compares the three candidate mechanisms** (kernel-arrow asymmetry — Path-A overclaim, not adopted; V5-cross-boundary — pre-aeon phase inheritance, OPEN; first-arrival single-template — user's reframing, OPEN). Argues that the first-arrival mechanism is structurally cleaner because it (i) requires no additional paper-specific postulate beyond what Q-C3-2 already admits, (ii) inherits IC framework-neutrality from `Memo_ED_CCC_Realizability_SubConstruct` at zero new content cost, (iii) routes the asymmetry through framework-neutral first-arrival rather than asymmetric cost between admitted classes.
4. **Sets the closure condition** for the eventual Baryogenesis M2 → M3 upgrade: successful construction of the single-template-admission derivation. Until that derivation lands, the upgrade is conditional.
5. **Does not modify the Baryogenesis paper.** The paper's M2 verdict + P-BinaryAdmission paper-specific postulate + §3.5 OPEN remain as-is, with the scoping memo cross-referenced as a sharper candidate-mechanism direction.

**Do not proceed to the paper-level upgrade until the constructive derivation is in place.** Premature upgrade would either (i) require declaring the single-template admission as a *new* paper-specific postulate (strictly increasing the corpus's declared substrate content — net worse than the current P-BinaryAdmission situation), or (ii) overclaim M3 with the same OPEN structure as Cos_03/Cos_04 inherit via continuum-Friedmann — which doesn't apply here because there's no analogous continuum-side machinery for chirality admission to inherit through DCGT.

**Estimated effort for the scoping memo:** ~1500 words, Wave-3 format, parallels Memo_ED_BinaryChirality's R1/R2/R3 reduction-path structure with a new "R4: First-arrival single-template lock-in via coherence functional" pathway laid out.

**Estimated effort for the constructive derivation (if pursued):** substrate-research-frontier scope; likely requires a `Memo_ED_CoherenceFunctional_SingleTemplate_Construct` working memo deriving the dynamical-stability claim from Paper_072 individuation + Q-C3-2 subleading-fluctuation admissibility + uniform-Ψ no-slack conditions. Not estimable from current corpus content.

---

## 6. Verification status summary

| Element | Status |
|---|---|
| Case 1 (Q-C3 single-template under saturation) | **Ruled out** by R3 failure in `Memo_ED_BinaryChirality` (continuous-to-binary collapse explicitly tried, did not close) |
| Case 2 (multi-template + dynamical stability selection) | **Partially in play, not constructed** — coherence-functional stability-selection pathway is admissible in principle but no current substrate-graph derivation exists for chirality content |
| Case 3 (Q-C3 does not constrain template multiplicity; OPEN reframed) | **Correct determination** — Q-C3 closes uniform-Ψ at substrate-state level; chain-class template multiplicity is not the C3 audit's subject matter |
| User reframing (first-arrival single-template lock-in) | **Plausible third candidate mechanism**, structurally cleaner than the two on file (kernel-arrow asymmetry, V5-cross-boundary); requires constructive substrate-graph derivation; not currently in corpus catalogue |
| M2 → M3 upgrade pathway | **Conditionally supported pending one substrate-graph derivation** (single-template admission via coherence functional under saturation) |
| Recommended next action | **Draft scoping memo** (`Memo_ED_Baryogenesis_SingleTemplate_Scoping`); do not modify Baryogenesis paper or draft upgrade memo until constructive derivation is in place |
| Honesty caveat on this verification | **Indirect** — primary upstream memo files not accessible as separate files; memo content inferred from in-line claims in citing papers (Inflation Preamble item 5; Baryogenesis Preamble item 2 + §3.3 + §3.5). Direct memo-text read would tighten or weaken this determination by at most one case classification. |

---

**End Memo_ED_Baryogenesis_QC3_SaturationVerification.**
