# Memo_ED_CoherenceFunctional_SingleTemplate_Construct

**Series:** Wave-3 Constructive-Derivation Memo (Baryogenesis closure pathway, Phase 1)
**Date:** 2026-05-17
**Status:** Constructive-derivation attempt. Targets R4 closure as defined in `Memo_ED_Baryogenesis_SingleTemplate_Scoping` §3. Does not modify Paper_ED_Baryogenesis_Open. Determines whether the load-bearing step *"coherence-functional minimization on the Q-C3-2 admissible-fluctuation set under uniform-Ψ no-slack boundary conditions yields a unique chain-class template"* succeeds (Outcome A), fails (Outcome B), or yields partial closure (Outcome C).

**Anchors:** Paper_ED_Inflation (Cos_01, M3 — Q-C3 cascade; uniform-Ψ saturation biconditional); Paper_ED_Cos_05 (M3 — saturation-regime inheritance template); Paper_ED_Baryogenesis_Open (M2 current — P-BinaryAdmission + asymmetric-admission-cost OPEN; §3.5 candidate mechanisms); Paper_ED_SC_4_9 (substrate-action functional $S_{\mathrm{sub}}[\Psi]$ + saddle-Hessian framework — load-bearing for the coherence-functional reconstruction below); Paper_087 (13 primitives — P02 participation, P04 bandwidth, P07 channel multiplicity, P09 polarity, P12 ED-threshold); Paper_072 (individuation regime); Paper_089 / Paper_090 / Paper_093 (V1 / V5 / T18 kernel structure); `Memo_ED_ChainClass_C3_Audit` (Q-C3-2 subleading fluctuation admissibility, accessed via Cos_01 Preamble item 5 in-line citation); `Memo_ED_CCC_Realizability_SubConstruct` (Q-C3-3 framework-neutral IC supply); `Memo_ED_BinaryChirality` (R1/R2/R3 failure record); `Memo_ED_Baryogenesis_SingleTemplate_Scoping` (R4 definition); `Memo_ED_Baryogenesis_QC3_SaturationVerification` (Case 3 determination).

> ⚠️ **Correction (2026-07-06):** This memo cites Θ_ED as "Paper_087 P12 (ED-threshold)" and reconstructs its coherence functional partly on that label (§2). That attribution is incorrect — canonical `Paper_087` P12 is a stability-landscape functional unrelated to an event-density threshold. Θ_ED's actual (uncritically-inherited) origin is `Paper_ED_CCC_ConformalCyclicCosmology.md` §3.2/§3.7, itself now flagged. This does not change this memo's tier verdicts (Θ_ED remains substrate-parameter-INHERITED throughout) — it only corrects the primitive citation. See `event-density/docs/Scoping_ThetaED_FirstPrinciples_2026-07-06.md`.

---

## 0. Honest scope caveats (read before §1)

This memo attempts a substrate-research-frontier constructive derivation. Two limitations to surface up front:

**(a) Coherence functional reconstruction is schematic, not lifted from a fully-specified canonical form.** The corpus papers visible to me cite the coherence-functional concept implicitly through Paper_072 individuation criteria, Paper_ED_SC_4_9 substrate-action machinery, and Cos_01's Q-C3 saturation analysis. A complete canonical specification of the coherence functional $\mathcal{F}_{\mathrm{coh}}[\chi_C; \Psi^{\mathrm{const}}]$ as a single named object does not appear in the directly-accessible papers. The construction below reconstructs the functional from its load-bearing constituents (V1 + V5 + Paper_072 admission criterion + P12 ED-threshold under no-slack) — this is the strongest defensible reconstruction from what is on disk.

**(b) Memo files cited as anchors are not directly accessible.** Same caveat as the prior verification memo: `Memo_ED_ChainClass_C3_Audit`, `Memo_ED_BinaryChirality`, `Memo_ED_CCC_Realizability_SubConstruct`, and the Update files are referenced through in-line citations in the papers, not via direct read.

Either of these caveats could shift the outcome classification by one tier in either direction (e.g., a more constrained canonical functional could yield Outcome A; a fully unconstrained functional could yield Outcome B). The Outcome C determination below is the best defensible reading from the visible corpus content. If access tightens either caveat, the derivation should be revisited.

---

## §1 Problem restatement

**R4 hypothesis** (per `Memo_ED_Baryogenesis_SingleTemplate_Scoping` §3): under Cos_01 saturation regime (uniform Ψ at substrate-state level; biconditional uniform-Ψ ↔ saturation via Q-C3 cascade), the coherence functional governing Paper_072 individuation admits exactly one chain-class template on the Q-C3-2 subleading-fluctuation set. The substrate cannot support two distinct stable chain-class templates simultaneously during saturation because the no-slack boundary condition (capacity = demand at admission frontier) forecloses the second template's instantiation.

**What must be shown for R4 closure (Outcome A):**

1. A well-defined coherence functional $\mathcal{F}_{\mathrm{coh}}[\chi_C; \Psi^{\mathrm{const}}]$ acting on the Q-C3-2 admissible-fluctuation set, with chain-class chirality $\chi_C \in S^1$ as argument and the uniform-$\Psi$ saturation background as fixed parameter.
2. The functional is bounded below on the Q-C3-2 admissible set under uniform-Ψ no-slack boundary conditions.
3. The minimum is attained at a **unique** chain-class template — i.e., a single value $\chi_C = \chi^*$ (or equivalently, a single chain-class template up to framework-neutral first-arrival selection).
4. The uniqueness traces structurally to the no-slack boundary condition — i.e., the same functional admits multiple stable minima when slack > 0 (post-saturation regime), recovering symmetric-admission restoration.

**What would falsify R4 (Outcome B):** explicit construction of two distinct chain-class templates, both stable on the Q-C3-2 admissible set under uniform-Ψ no-slack conditions, with the coherence functional having two non-degenerate stationary minima. Or: demonstration that the functional is not well-defined / unbounded below / ill-posed.

**Partial closure (Outcome C):** the functional may yield a continuously-degenerate minimum manifold (multiple templates equally minimize $\mathcal{F}_{\mathrm{coh}}$) but the no-slack boundary condition + sequential admission structure yield a unique attractor *given* first-arrival initial conditions. This is structurally weaker than Outcome A (the uniqueness depends on the IC + sequential-admission combination, not on the functional alone) but stronger than Outcome B (it does provide single-template admission post-IC).

---

## §2 Upstream constraints

The constructive attempt below operates under the following corpus-supplied constraints:

**Q-C3 background structure.** Saturation = uniform Ψ at substrate-state level (biconditional via Q-C3 cascade per `Memo_ED_ChainClass_C3_Audit`, ACCEPTED with five qualifications Q-C3-1a/1b/2/2b/3 per Cos_01 Preamble item 5). The leading-order substrate state is $\Psi(\ell, t) = \bar\Psi$ (constant) across substrate-graph loci.

**Q-C3-2 admissible fluctuation set.** Subleading $O(\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}})$ fluctuations $\delta\Psi(\ell, t)$ around $\bar\Psi$ are admissible. Per the Cos_01 §3.5 + Cos_06 §3.2 inheritance pattern, these fluctuations decompose into chain-content with a chirality identifier $\chi_C \in S^1$ (P09 phase difference between chain-arrow and globally-coherent kernel-arrow per `Memo_ED_ChainArrowChirality` §3.3, as cited in Paper_ED_Baryogenesis_Open §3.2). The admissible fluctuation manifold is schematically:
$$
\mathcal{M}_{\mathrm{Q-C3-2}} = \{(\chi_C, A) : \chi_C \in S^1, \; A \le O(\varepsilon) \cdot \bar\Psi, \; \text{satisfies Paper_072 individuation}\}
$$
where $A$ is the fluctuation amplitude and Paper_072 individuation is the substrate-graph admission criterion.

**No-slack boundary condition (saturation phase).** Per Paper_ED_Baryogenesis_Open §3.1 + §3.5, the post-SCBU ignition phase has substrate event-density at saturation: capacity (V1 finite-width retarded support + P04 bandwidth × P07 channel multiplicity) equals admission demand. The no-slack constraint means that any admission of a new chain-class instance is structurally constrained — the substrate has no spare capacity to instantiate content beyond what is already admitted.

**Coherence functional reconstruction.** From SC-4.x substrate-action machinery + Paper_072 individuation + Q-C3-2 admissibility, the schematic coherence functional is:
$$
\mathcal{F}_{\mathrm{coh}}[\chi_C; \bar\Psi, A] = -\mathcal{K}_{V_1}[\chi_C; \bar\Psi, A] - \mathcal{K}_{V_5}[\chi_C; \bar\Psi, A] + \mathcal{P}_{\mathrm{cap}}[\chi_C; A, \mathrm{slack}]
$$
where $\mathcal{K}_{V_1}$ is the V1-coherence reward (substrate-graph chain content propagating stably under V1 retarded kernel; structurally lowers $\mathcal{F}_{\mathrm{coh}}$); $\mathcal{K}_{V_5}$ is the V5 cross-chain-coherence reward (cross-chain correlation content from finite-memory V5 kernel; structurally lowers $\mathcal{F}_{\mathrm{coh}}$); $\mathcal{P}_{\mathrm{cap}}$ is the capacity penalty (substrate-graph cost of admitting chain content against finite admission frontier; structurally raises $\mathcal{F}_{\mathrm{coh}}$, with the penalty diverging as slack → 0 for any admission attempt beyond the first-admitted template).

This schematic structure is reconstructed from the load-bearing constituents named in the corpus papers visible to me (Paper_089 V1 + Paper_090 V5 + Paper_072 admission + P04/P07 capacity + P12 ED-threshold) — see scope caveat (a).

---

## §3 Constructive derivation attempt

### §3.1 The admissible fluctuation manifold under Q-C3-2

The Q-C3-2 admissible manifold $\mathcal{M}_{\mathrm{Q-C3-2}}$ has the structure of a circle bundle over the amplitude axis: each amplitude $A \le O(\varepsilon) \bar\Psi$ supports a circle of chirality values $\chi_C \in S^1$, and Paper_072 individuation imposes admission criteria selecting an admissible sub-bundle. Per the Q-C3-2 in-line specification (Cos_01 Preamble item 5: "subleading $O(\varepsilon)$ fluctuations admissible; not load-bearing for leading-order phenomenology"), the admissibility is *generic* — no specific sub-bundle structure is identified at the Q-C3-2 audit's level of resolution.

### §3.2 The coherence functional on $\mathcal{M}_{\mathrm{Q-C3-2}}$

Restricting $\mathcal{F}_{\mathrm{coh}}$ to $\mathcal{M}_{\mathrm{Q-C3-2}}$ and treating the uniform-Ψ saturation background as fixed parameter:

The V1-coherence reward $\mathcal{K}_{V_1}[\chi_C; \bar\Psi, A]$ depends on V1 retarded propagation of the chain content. Per Paper_089 T18, V1 carries chain content along substrate edges in the globally-coherent kernel-arrow direction. **V1 is chirality-agnostic** (per Paper_ED_Baryogenesis_Open §3.7 + audit row 17, citing Paper_089): the propagation rate is independent of $\chi_C$. Therefore $\mathcal{K}_{V_1}$ has *no explicit $\chi_C$ dependence* at the substrate-graph level visible in the corpus: $\partial_{\chi_C} \mathcal{K}_{V_1} = 0$.

The V5 cross-chain-coherence reward $\mathcal{K}_{V_5}[\chi_C; \bar\Psi, A]$ depends on V5 cross-chain coupling. Per Paper_090, V5 carries finite-memory cross-chain content. V5 coupling depends on P09 phase coherence between chains; for a single instantiated chain-class with chirality $\chi^*$, the V5 cross-coherence reward depends on the phase relationship $\chi_C - \chi^*$ between the candidate fluctuation and the already-instantiated content. **V5 is chirality-sensitive** in this conditional sense: $\mathcal{K}_{V_5}$ is maximized when $\chi_C = \chi^*$ (perfect phase alignment with existing chain content) and decreases as $|\chi_C - \chi^*|$ increases.

The capacity penalty $\mathcal{P}_{\mathrm{cap}}[\chi_C; A, \mathrm{slack}]$ depends on slack (capacity minus demand). Under no-slack conditions, the penalty function for admission of a chain-class beyond the first-admitted one diverges (or grows large enough to overwhelm the V1 + V5 rewards for any plausible parameter regime). The functional structure is essentially: $\mathcal{P}_{\mathrm{cap}} \to \infty$ as $\mathrm{slack} \to 0$ for $\chi_C \neq \chi^*$, where $\chi^*$ is the chirality of already-admitted content.

### §3.3 Apply no-slack boundary condition

Under saturation, slack = 0. The coherence functional restricted to $\mathcal{M}_{\mathrm{Q-C3-2}}$ becomes a *conditional* functional whose form depends on whether any chain-class has already been instantiated:

**Case (i): no chain-class yet instantiated.** Before the first admission event, no $\chi^*$ exists. The V5 reward $\mathcal{K}_{V_5}$ has no preferred chirality value (P09 phase symmetry is unbroken). The functional $\mathcal{F}_{\mathrm{coh}}$ is **continuously symmetric over $\chi_C \in S^1$**: every chirality value is equally favored. The minimum is **continuously degenerate** — the entire circle $\chi_C \in S^1$ is a stationary manifold.

**Case (ii): chain-class with chirality $\chi^*$ already instantiated.** After the first admission, $\chi^*$ is the chirality of the existing content. The V5 reward $\mathcal{K}_{V_5}$ now has a preferred chirality at $\chi_C = \chi^*$. The capacity penalty $\mathcal{P}_{\mathrm{cap}}$ diverges for $\chi_C \neq \chi^*$ under no-slack. The functional $\mathcal{F}_{\mathrm{coh}}$ has a **unique minimum at $\chi_C = \chi^*$**: any attempt to admit content with $\chi_C \neq \chi^*$ is foreclosed by the capacity penalty + V5 coherence requirement.

### §3.4 Analyze stationary structure

The Euler-Lagrange analog (discrete-substrate variational analysis) on $\mathcal{M}_{\mathrm{Q-C3-2}}$:

In Case (i), the stationary set is the entire circle $S^1$. There is **no unique stationary point** — the functional has a continuous symmetry that the variational analysis preserves.

In Case (ii), the stationary set collapses to a single point at $\chi_C = \chi^*$. The Hessian of $\mathcal{F}_{\mathrm{coh}}$ at this point is positive-definite (V5 coherence is maximized; capacity penalty rises in all directions away from $\chi^*$); the stationary point is a unique stable minimum.

### §3.5 Determine whether the minimum is unique

**The coherence functional alone (without sequential-admission structure) does NOT have a unique minimum.** In Case (i), the minimum is continuously degenerate over $\chi_C \in S^1$. This means **R4 cannot close at Outcome A** purely from the coherence-functional structure visible in the corpus.

**However, the coherence functional + sequential-admission + no-slack DOES yield a unique attractor given first-arrival IC.** The mechanism is:

1. Pre-first-admission: continuously-degenerate minimum manifold (Case i). All chirality values are equally admissible.
2. First-arrival event: the symmetry-breaking event at BBB ignition selects one chirality value $\chi^*$ framework-neutrally per `Memo_ED_CCC_Realizability_SubConstruct` (cyclic-CCC framing: $\chi^*$ inherits pre-aeon V5 cross-boundary content; R3 single-aeon framing: $\chi^*$ is structural-IC supplied).
3. Post-first-admission: functional structure shifts to Case (ii). The unique minimum at $\chi_C = \chi^*$ forecloses subsequent admission of $\chi_C \neq \chi^*$ under no-slack.
4. Result: unique chain-class template instantiated globally during saturation; "binary admission" framing of P-BinaryAdmission is reinterpreted as single-template admission with framework-neutral first-arrival selection from a continuously-degenerate minimum manifold.

### §3.6 Outcome classification

**This is Outcome C — partial closure.**

The coherence functional alone does not yield a unique minimum (Outcome A would require Hessian eigenvalues positive-definite in all $S^1$ directions even before any chain-class is instantiated, which is incompatible with the P09 phase-symmetry of the pre-admission saturation background). But R4 is also not falsified (Outcome B would require two distinct stable minima accessible without IC selection, which is incompatible with the V5 phase-coherence + no-slack capacity-penalty structure after any first admission).

What R4 *does* close: single-template admission under saturation **given** first-arrival IC supplied framework-neutrally per `Memo_ED_CCC_Realizability_SubConstruct`. This is structurally cleaner than the current paper's P-BinaryAdmission + asymmetric-admission-cost OPEN, but it is not a clean M3 closure of the form Cos_01 / Cos_05 have. The closure status is **"M3 conditional on first-arrival IC supply at substrate-graph framework-neutral level"** — the same conditional structure Cos_01 itself carries via Q-C3-3.

---

## §4 Outcome classification (formal statement)

**Outcome A (R4 succeeds — Baryogenesis M3 upgrade fully supported):** RULED OUT by §3.3 Case (i) analysis. The pre-admission coherence functional has continuously-degenerate minima over $\chi_C \in S^1$; no unique minimum exists from the functional structure alone.

**Outcome B (R4 fails — OPEN persists):** NOT REACHED. The post-admission Case (ii) analysis does yield single-template admission via the V5 phase-coherence + no-slack capacity-penalty mechanism. Two distinct stable templates are not simultaneously admissible under no-slack conditions once any chain-class has instantiated.

**Outcome C (partial closure — single-template admission given first-arrival IC):** CONFIRMED. The coherence functional + sequential-admission + no-slack structure yields a unique attractor *given* framework-neutral first-arrival IC supply. The IC supply mechanism is the same one Cos_01 inherits via Q-C3-3 + `Memo_ED_CCC_Realizability_SubConstruct` (cyclic-CCC vs R3 single-aeon framework-neutrality). The asymmetric-admission-cost OPEN dissolves; P-BinaryAdmission is reinterpreted (not eliminated, but reframed as single-template admission under first-arrival).

**Implication for the Baryogenesis verdict:** the R4 closure pathway under Outcome C supports a **conditional M3 upgrade** — conditional in exactly the same sense that Cos_01's M3 is conditional on Q-C3-3 IC supply. If the corpus accepts Cos_01's Q-C3-3 IC supply as M3-compatible (it does — Cos_01 is M3 unconditional per the current corpus state), then Baryogenesis can inherit the same conditional structure and close at M3 via R4 + Q-C3-3 IC supply.

---

## §5 Consequences for Baryogenesis

**Under Outcome C with conditional M3 upgrade (recommended interpretation):**

The Baryogenesis paper M2 → M3 upgrade is supported via the following inheritance chain:

- Cos_01 saturation regime (M3 unconditional) → uniform Ψ at substrate-state level
- Q-C3-2 admissibility → subleading fluctuation manifold $\mathcal{M}_{\mathrm{Q-C3-2}}$
- Coherence functional + no-slack + sequential admission (this memo §3) → single-template admission *given* first-arrival IC
- `Memo_ED_CCC_Realizability_SubConstruct` → framework-neutral first-arrival IC supply (Q-C3-3 analog for Baryogenesis IC supply)

**Verdict consequence:** Baryogenesis upgrades from M2 to **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) per Paper_095 §3.2.1**, with the IC-INHERITED axis explicitly carrying the framework-neutral first-arrival selection per `Memo_ED_CCC_Realizability_SubConstruct`. P-BinaryAdmission is reinterpreted (not eliminated — the structural content is reframed): the "binary" framing becomes "single-template admission from continuously-degenerate pre-admission manifold + first-arrival selection." The §3.5 asymmetric-admission-cost OPEN is dissolved. No new paper-specific postulate beyond what the corpus already carries via Q-C3-2 + Q-C3-3.

**Required paper edits for the M3 upgrade (sketch — for the follow-up upgrade memo, not this memo):**

- Preamble item 2 revised: P-BinaryAdmission reinterpreted, not declared as new postulate; substrate-graph derivation supplied via this memo's §3 reconstruction + IC supply per `Memo_ED_CCC_Realizability_SubConstruct`.
- Preamble item 3 revised: asymmetric-admission-cost OPEN dissolved; replaced with reframing note.
- §1 verdict updated: M2 → M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED).
- §3.4 + §3.5 revised: single-template admission framework + first-arrival selection replaces "two admitted classes + asymmetric cost between them."
- §4 audit table: P-BinaryAdmission row reclassified from P (postulate) to D-via-I (substrate-graph composition of Q-C3-2 + coherence functional + no-slack + IC supply per this memo); asymmetric-admission-cost row removed; IC-INHERITED first-arrival row added.
- §6 closing position statement updated with M3 verdict-tier sync.

**Under Outcome B (would-have-falsified R4, ruled out by §3 analysis):** Baryogenesis would remain M2; R4 would be added to `Memo_ED_BinaryChirality` as a fourth failed reduction path. *Not applicable* under this memo's findings.

**Under stricter Outcome C reading (if the conditional M3 upgrade is judged insufficient for full M3 status):** Baryogenesis remains M2 but with the §3.5 OPEN sharply dissolved into a verification question: "does the corpus accept first-arrival IC supply via `Memo_ED_CCC_Realizability_SubConstruct` as equivalent to Q-C3-3 IC supply for Cos_01's M3 verdict?" If yes (current corpus state suggests yes), full M3 upgrade follows. If no (would require a separate position decision), Baryogenesis stays M2 with the cleaner reframed OPEN.

---

## §6 Recommended next steps

**Recommend a two-step plan:**

**Step 1 — Verify the M3 conditional-upgrade pathway is corpus-consistent.** Specifically: confirm that the first-arrival IC supply mechanism under R4 + `Memo_ED_CCC_Realizability_SubConstruct` is at the same logical status as Cos_01's Q-C3-3 IC supply. If both are framework-neutral IC supply (cyclic-CCC vs R3 single-aeon, choice outside scope), the structural analog holds and R4-conditional-M3 ≡ Cos_01-conditional-M3 ≡ M3 unconditional in the current corpus state. This step is short (one-page audit memo): `Memo_ED_R4_IC_Supply_Audit`.

**Step 2 — Draft the Baryogenesis M2 → M3 upgrade memo.** If Step 1 confirms corpus-consistency, draft `Update_Paper_ED_Baryogenesis_M3_via_R4` applying the upgrade per §5 sketch above. This is a paper-level revision memo with the specific edits enumerated. After review, the upgrade lands on the Baryogenesis paper itself.

**Do not proceed directly to paper-level upgrade without Step 1.** The conditional M3 closure depends on accepting the structural analog between R4 IC supply and Q-C3-3 IC supply. This is a defensible analog but not automatic — Step 1 makes it explicit and avoids the upgrade being challenged on framework-consistency grounds later.

**Alternative path: refine the coherence functional reconstruction.** If a fully-canonical coherence functional specification can be located in the corpus (perhaps in a memo file not directly accessible to me), redo §3 of this memo with the canonical functional. Possible outcomes: (i) confirms Outcome C; (ii) tightens to Outcome A if the canonical functional has additional structure that breaks the P09 phase symmetry pre-admission (would make R4 close unconditionally); (iii) shifts to Outcome B if the canonical functional doesn't have the V5 phase-coherence + no-slack capacity-penalty structure assumed in §3.

**Defer further work on the V5-cross-boundary candidate mechanism (Memo_ED_V5PhaseContent).** Under Outcome C with R4 closure, the V5-cross-boundary candidate becomes one possible *realization* of the first-arrival IC supply (the cyclic-CCC framing), not a separate competing mechanism. No further independent work needed on V5-cross-boundary unless the conditional M3 upgrade is rejected and the failed-reduction-path catalog needs expansion.

---

**End Memo_ED_CoherenceFunctional_SingleTemplate_Construct.**
