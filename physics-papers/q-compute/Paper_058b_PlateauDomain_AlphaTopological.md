# Where the Plateau Binds: Settling the Encoding-Dependence of the Class-C Mechanism

**Series:** Event Density (ED) Generative Papers — Q-COMPUTE arc (058 domain-sharpening; "Paper_058b")
**Author:** Allen Proxmire
**Status:** Publication draft (settlement of the open item created by `Paper_ProxyConversionDoctrine` §3.4: the encoding-dependence of Paper_058's α). Domain-sharpening of `Paper_058_ClassC_Plateau`, not a correction: 058's own hedges (Preamble 8, §4.3, falsifier 6.4) anticipated exactly this resolution.
**Companions:** `Paper_058_ClassC_Plateau`, `Paper_090_V5Kernel`, `Paper_V5UnifiedBudget`, `Paper_QuantumDarwinism_RecordBandwidth`, `Paper_ProxyConversionDoctrine`.

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **Paper_058 is not falsified or corrected.** P-Redundancy-Mapping was declared there as a *regime assumption* (058 §2, audit row "A→regime"); this paper locates the regime boundary. 058 §4.3 already classified surface codes as hybrid, and falsifier 6.4 already contemplated a non-linear mapping.
2. **No claim that topological codes evade every substrate limit** — only that they evade the *per-locus V5 correlation-budget saturation* mechanism (UR-1.3 / lever C). The Class-B rigidity analysis (057) and the other M_cap constituents (053: N_bw, N_commit) are untouched.
3. **The Google repetition-code floor is NOT claimed as a confirmation.** It is a watch item with a live mundane attribution (correlated burst events ~1/hr; cosmic rays / TLS). The discriminator is stated (§5), not prejudged.
4. **No absolute scales derived** (B_cross,max, R_C^sat, Γ_plateau remain inherited, as in 058).
5. The settlement is conditional on: 090's pairwise-kernel form for V5, 058's own per-locus P-Corr-Budget, and the standard stabilizer-state correlation structure of topological codes (an inherited quantum-information fact, not an ED result).

---

## Abstract

`Paper_ProxyConversionDoctrine` §3.4 opened one question as the highest-value review item of the Class-C arc: does 058's redundancy-to-coverage coefficient α load a substrate locus linearly in code distance for *topological* codes, or is topological per-locus load O(1)? We settle it from the corpus's own commitments. 058's P-Corr-Budget is explicitly **per-locus**; 090's V5 is a **pairwise** kernel with finite reach, so all multi-chain live correlation is a web of pairwise links; and a topological code's web is **local by construction** — each physical channel holds live pairwise correlation with O(z) neighbors regardless of distance d, while pairwise correlation between distant code qubits is ~0 (that is what topological encoding *is*), and syndrome extraction produces P11-committed records, which are budget-free. Therefore per-locus B_cross stays bounded at ~z·w_pair, never approaches B_cross,max as d grows, and **the §3.3 saturation of 058 never triggers for topological codes: α_topological = 0 in the per-locus sense.** P-Redundancy-Mapping's linear regime is the **broadcast/hub regime** — repetition-type codes, GHZ-type encodings, any scheme whose redundant channels hold direct live correlation with a common locus. Consequences: the Class-C plateau prediction (report weapon #4, Predictions List 4.10) re-scopes from "high code distance" to **broadcast-type redundancy**; the topological branch predicts *no* substrate plateau via this mechanism — which converts the brewing tension with clean surface-code suppression (Willow, Λ≈2, no plateau through d=7) into a *match*; and the near-term weapon becomes a **broadcast pair**: persistence of the repetition-code error floor (Google observed an apparent 10⁻¹⁰ floor above d≈15 — in exactly the encoding type this mechanism binds) and the cat-state width ceiling (`Paper_QuantumDarwinism_RecordBandwidth`), tied to each other and to the monogamy/Page budgets through the fixed ratios of `Paper_V5UnifiedBudget`.

---

## 1. The question, precisely

058's plateau mechanism: redundant channels carrying the protected state must be **coherently correlated** ("at saturation, additional redundant substrate-channels carry the protected state nominally but cannot be coherently correlated with the existing substrate-channel set," 058 §3.3), and the budget that saturates is **per-locus** ("V5 cross-chain correlation content at a substrate-graph locus," P-Corr-Budget; glossary: "carried at chain locus"). The unsaturated-regime form `B_cross(R_C) ≈ α·R_C` (058 §3.2) then requires that growing the redundancy parameter grows the correlation content *at some locus*. The question: for which encodings is that true?

## 2. The pairwise-web lemma

By 090 §3.2, V5 "acts on pairs of chains" with finite reach ℓ_V5 and finite memory τ_V5. So any live multi-chain correlation structure is carried as a **web of pairwise V5 links**, and the per-locus budget of P-Corr-Budget counts the pairwise weight incident at each locus (exactly 065's partition, `W = Σ_i W_{A,B_i}`; `Paper_V5UnifiedBudget` §5). A locus's load is set by the **degree and weight of its incident live links**, not by the size of the web it belongs to.

## 3. The two regimes

**Broadcast/hub regime (α non-zero).** Repetition-type codes and GHZ-type encodings correlate every redundant channel *directly* with a common locus (hub) or with all others (all-to-all pointer correlation, ~1 bit per pair). Incident live load at the loaded locus grows ~R_C·w_pair. P-Redundancy-Mapping's linear form holds; B_cross → B_cross,max at `R_C^sat = B_cross,max/α`; the 058 plateau follows. *(Under P-QD-LiveWeight this is also the GHZ-width ceiling — the same budget, `Paper_QuantumDarwinism_RecordBandwidth` §5.)*

**Topological/local regime (α_topological = 0).** In a surface/color code at distance d: (i) each physical channel is gate- and stabilizer-coupled to O(z) nearest neighbors — its incident live web has bounded degree, independent of d; (ii) pairwise correlation between *distant* code qubits is ~0 by construction — hiding the logical information from local (including pairwise) probes is the defining property of topological encoding, so there is no long-range pairwise live load for the budget to count; (iii) syndrome measurements are P11 commitments, and committed records are budget-free (`Paper_QuantumDarwinism_RecordBandwidth` §2), so repeated stabilizer extraction does not accumulate live load. Hence per-locus `B_cross(u) ~ z·w_pair`, **constant in d**. Since working codes exist, `z·w_pair < B_cross,max`, and growing d adds channels without moving any locus toward saturation:

$$
\boxed{\;\alpha_{\rm topological} = 0 \text{ (per-locus): the §3.3 saturation of Paper\_058 never triggers for topological codes.}\;}
$$

**Settlement of P-Redundancy-Mapping's domain:** the linear regime assumption holds for encodings whose redundancy adds *incident* live correlation at a common locus (broadcast/hub); it fails — not approximately, but structurally — for encodings whose redundancy adds *area* to a bounded-degree local web (topological). This is 058's falsifier 6.4 resolved from inside the corpus rather than by experiment, and 058 §4.3's hybrid classification made precise.

## 4. Consequences

1. **Prediction 4.10 re-scopes.** The Class-C plateau is a prediction about **broadcast-type redundancy**, not about surface-code distance. The topological branch now *predicts the absence* of a substrate plateau via this mechanism.
2. **The tension with clean surface-code suppression dissolves into a match.** Willow's surface codes suppress exponentially (Λ ≈ 2) through d = 7 with no plateau — under the old uniform reading this was accumulating pressure on 058; under the settlement it is the expected behavior of the out-of-domain encoding.
3. **The near-term weapon is a broadcast pair, active today:**
   - **Repetition-code floor persistence.** Google's d ≤ 29 repetition codes deviated from exponential suppression above d ≈ 15, with an apparent logical error floor ~10⁻¹⁰/cycle from rare correlated bursts (~1/hour) — *the plateau shape, in exactly the encoding type this mechanism binds.*
   - **Cat-state width ceiling** (`Paper_QuantumDarwinism_RecordBandwidth` §5–6): same budget, same regime, floored today at 10⁰–10¹ bits/locus by the 120-qubit GHZ under the pre-registered content rule.
   By `Paper_V5UnifiedBudget`'s fixed ratios, these two must sit at **commensurate converted content** with each other and with the monogamy/Page budgets — one number family, several public data streams.
4. **R1 finalizes.** The `Paper_V5UnifiedBudget` §4 caveat resolves: topological architectures drop out of the R1 band (they never saturate via this mechanism); R1's cross-platform consistency claim (058 §5.2) ranges over broadcast-type platforms.
5. **058's falsifier 6.1 re-scopes** to broadcast-type platforms: continued suppression at arbitrarily high *topological* distance no longer bears on P-Corr-Budget.

## 5. The discriminator (stated, not prejudged)

The repetition-code floor has a live mundane attribution: correlated burst events (cosmic rays, TLS transients), which Google expects to mitigate by shielding and burst-detection. The two hypotheses separate cleanly:

- **Mundane:** the floor is engineered away (shielding, gap protection, burst post-selection); different platforms' floors sit at *uncorrelated* heights set by their local burst environments.
- **ED substrate floor:** a residual floor survives mitigation, and its converted content (per the `Paper_ProxyConversionDoctrine` §3.1 rule) is **consistent across broadcast-type platforms** (058 §5.2) and **commensurate with the certified cat-width ceiling** (one budget).

Either outcome is informative; only the second is ED's. No confirmation is claimed from the 2024 data — the burst attribution is plausible and the mitigation campaign is the experiment.

## 6. Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| P-Corr-Budget is per-locus | **I (corpus, verbatim)** | 058 §2 + glossary |
| V5 pairwise, finite reach → correlation = pairwise web | **I (corpus)** | 090 §3.2; 065 partition; V5UnifiedBudget §5 |
| Topological codes: bounded incident degree, ~0 distant pairwise correlation | **I (standard QI)** | defining property of topological encoding; not an ED result |
| Syndrome records budget-free | **D (from QD accounting theorem)** | Paper_QuantumDarwinism_RecordBandwidth §2 |
| α_topological = 0 (per-locus); saturation never triggers | **D-structural** | §3; conditional on the three rows above |
| P-Redundancy-Mapping domain = broadcast/hub | **D-structural (regime settlement)** | §3; resolves 058's declared regime assumption from inside |
| 4.10 re-scope + falsifier re-scope | **bookkeeping (forced)** | §4 |
| Repetition-code floor as ED plateau | **NOT claimed** — watch item | §5; mundane attribution live |
| Absolute scales | **I** | as in 058 |

## 7. Falsification Criteria

- **F-058b-1:** a *pure broadcast-type* platform (repetition-code-like, no topological admixture) showing continued exponential suppression to arbitrarily high R_C after burst mitigation — falsifies the re-scoped plateau (this inherits 058's 6.1, now correctly targeted).
- **F-058b-2:** a topological platform exhibiting a code-distance plateau whose converted content matches B_cross,max — would show per-locus loading this paper says cannot occur, falsifying §3's web analysis (and rescuing the original code-distance leg).
- **F-058b-3:** post-mitigation broadcast floors at *inconsistent* converted content across platforms — falsifies the cross-platform leg (058 §5.2) in the settled domain.

## 8. Position Statement

Read against its own definitions, the corpus settles its newest open item: 058's budget is per-locus, V5's correlation is a pairwise web, and topological encoding is the art of keeping that web local — so the Class-C saturation mechanism cannot bind in code distance, and **α_topological = 0**. The plateau prediction does not weaken; it *relocates* to where the mechanism actually binds: broadcast-type redundancy, where public data already shows the predicted shape (a repetition-code floor) and a second, independent observable (the certified cat-width ceiling) draws on the same budget at a fixed ratio. One family of near-term numbers — repetition floors, cat widths, monogamy, Page — one inherited scale, and a stated discriminator against the mundane explanation. The topological branch becomes a prediction of absence, already consistent with the cleanest QEC data in existence.

**What this paper claims:** the domain settlement (α_topological = 0, broadcast = the linear regime); the 4.10 re-scope; the discriminator. **What it does not:** any confirmation from the 2024 repetition-code floor; any absolute scale; any limit on topological codes from other M_cap constituents.

---

**Series context.** Q-COMPUTE arc, domain-sharpening of 058; closes `Paper_ProxyConversionDoctrine` §3.4 (deliberate open item, same-week closure). Third product of the V5 unified-budget arc (`Paper_V5UnifiedBudget` → `Paper_QuantumDarwinism_RecordBandwidth` → this).
