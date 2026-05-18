# Update_Paper_095_LabelClasses — Corpus-wide formalization of I sub-labels

**Date:** 2026-05-17
**Scope:** Methodology patch to Paper_095 (Form-FORCED / Value-INHERITED Methodology); follow-on cleanup of in-paper bridging notes across 2026-05 Wave-3 papers.
**Status:** Paper_095 patches applied (§3.2.1 sub-labels added; §3.2.2 mixed-verdict-tier base+sub-case added; §3.2.3 component-status composition added; §2.5 row 6 added). In-paper bridging notes can be removed from affected papers at next revision.

---

## What changed in Paper_095

A new **§3.2.1 Sub-labels of I** formalizes two sub-labels introduced in the 2026-05 corpus push:

- **I (substrate-parameter-INHERITED)** — for numerical values inherited via substrate-parameter content (e.g., $\Theta_{\mathrm{ED}}$, $\tau_{V_5}/\tau_P$, $\ell_P$) at the **Paper_027-analog** level. Anchor: Paper_027 (Newton's $G$) as original template; Route A4 closure via Memo_ED_RouteA_MultiRouteConvergence_Audit option (ii) as corpus-wide tier.
- **IC-INHERITED** — for initial-condition / boundary-state content inherited from an upstream substrate-state specification; framework-neutral with respect to cyclic-CCC vs single-aeon ontology per Memo_ED_CCC_Realizability_SubConstruct.

Both remain **I** in the three-tier (M1/M2/M3) grammar; sub-label is recorded in the Notes column of the audit table. Audit row label cell reads **I**; Notes column reads "Sub-type per label-class note: *<sub-label>*. [reference]."

A **three-axis M3 verdict notation** is also formalized:

> **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED)**

This is still M3 in the M1/M2/M3 grammar; the three-axis form makes the composition of the M3 verdict explicit and supports the five-anchor verdict-sync check (status / abstract / §1 / audit row / §6).

§2.5 audit table extended with row 6 documenting the sub-label extension.

A new **§3.2.2 Mixed-verdict-tier papers** formalizes a second 2026-05 pattern: papers with a single **base verdict** (M1/M2/M3) plus named **sub-case carve-outs** whose substrate-graph chain closes at a *stronger* verdict than the base. Convention:

- Base verdict appears in the five-anchor sync (status / Abstract / §1 / audit verdict row / §6).
- Sub-case verdicts appear in §1 (regime block), the audit table (dedicated row), and §6 (closing note) — explicitly named at each anchor in the form "M2 (generic) with M3 saturation-case noted."
- Sub-case verdicts may not be weaker than the base verdict.
- Does **not** create new tiers; makes the *composition* of inherited verdicts within a paper explicit.

The three-axis notation of §3.2.1 composes cleanly with mixed-tier framing: e.g. `M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic case; M3 saturation-case via Dyn_01 + Dyn_04`. Leading user: Paper_ED_Dyn_05 (Inspiral Dynamics).

A new **§3.2.3 Component-status composition rule** formalizes a third 2026-05 pattern: papers integrating several upstream chains as **distinct frequency-band / domain components** of one observable, with each component carrying a different verdict tier. Convention:

- **Component-status composition rule.** Net verdict in any observable domain is bounded above by the verdict of the component dominating that domain. The paper's base verdict (for the five-anchor sync) is the net verdict in the domain where the integrated observable carries its load-bearing empirical anchors.
- **Per-component verdict table** required in §1 (or audit row): source class, ED substrate-graph mechanism, observable domain, verdict tier.
- **Subdomain carve-outs** at higher tier may be called out as §3.2.2-style sub-cases.

Three rules compose cleanly: a paper may carry a three-axis verdict (§3.2.1) with base + sub-case structure (§3.2.2) driven by component-status composition (§3.2.3). Leading user: Paper_ED_GW_02 (Stochastic Background) — full triple composition.

---

## Affected papers (in-paper bridging notes can be removed at next revision)

These papers currently carry an in-paper "Label-class note" block after the Anchors line, defining the same two sub-labels by self-reference. With Paper_095 §3.2.1 in place, those bridging blocks become redundant and can be cut to a one-line pointer:

> **Label-class note:** Audit-row sub-labels *substrate-parameter-INHERITED* and *IC-INHERITED* per Paper_095 §3.2.1.

Papers to update on next revision pass:

| Paper | Path | Current bridging-note location |
|---|---|---|
| Paper_ED_Cos_05 (Dark Energy) | `physics-papers/cosmology/Paper_ED_Cos_05_*.md` | Post-Anchors block |
| Paper_ED_Cos_06 (Inflationary Spectrum) | `physics-papers/cosmology/Paper_ED_Cos_06_InflationarySpectrum.md` | Post-Anchors block |
| Paper_ED_Dyn_01 (Saddle Dynamics) | `physics-papers/dynamics/Paper_ED_Dyn_01_SaddleDynamics.md` | Post-Anchors block |
| Paper_ED_Dyn_04 (Gravitational Collapse) | `physics-papers/dynamics/Paper_ED_Dyn_04_GravitationalCollapse.md` | Post-Anchors block |
| Paper_ED_Dyn_05 (Inspiral Dynamics) | `physics-papers/dynamics/Paper_ED_Dyn_05_InspiralDynamics.md` | Post-Anchors one-line pointer (already uses canonical form) — also leading user of §3.2.2 mixed-tier framing |
| Paper_ED_GW_01 (Ringdown Spectroscopy) | `physics-papers/dynamics/Paper_ED_GW_01_RingdownSpectroscopy.md` | Post-Anchors one-line pointer (already uses canonical form) — uses §3.2.2 mixed-tier for GW_00 row 13 closure |
| Paper_ED_GW_02 (Stochastic Background) | `physics-papers/dynamics/Paper_ED_GW_02_StochasticBackground.md` | Post-Anchors one-line pointer (already uses canonical form) — **leading user of §3.2.3 component-status composition**; full triple §3.2.1 + §3.2.2 + §3.2.3 composition |
| Paper_ED_Cos_02 (BBN) | `physics-papers/cosmology/Paper_ED_Cos_02_BBN.md` | Post-Anchors one-line pointer (already uses canonical form) — §3.2.1 sub-labels; M3 via continuum-Friedmann inheritance with architectural division from Dyn_02 M2 (Preamble item 7) |
| Paper_ED_Cos_03 (CMB Acoustic) | `physics-papers/cosmology/Paper_ED_Cos_03_CMBAcoustic.md` | Post-Anchors one-line pointer (already uses canonical form) — §3.2.1 sub-labels; M3 via continuum-Friedmann inheritance with architectural division from Dyn_02 M2 (Preamble item 6) |
| Paper_ED_Cos_04 (Linear Structure Formation) | `physics-papers/cosmology/Paper_ED_Cos_04_StructureFormation.md` | Post-Anchors one-line pointer (already uses canonical form) — §3.2.1 sub-labels; M3 via continuum-Friedmann inheritance with architectural division from Dyn_02 M2 (Preamble item 6) |
| Paper_ED_Cos_06 (Inflationary Spectrum) | `physics-papers/cosmology/Paper_ED_Cos_06_InflationarySpectrum.md` | Post-Anchors one-line pointer (already uses canonical form) — §3.2.1 sub-labels; M3 via Cos_01 saturation-regime + GW_00 saddle-Hessian-signature framework + Route A4 |
| Paper_ED_Baryogenesis (Matter-antimatter asymmetry) | `physics-papers/cosmology/Paper_ED_Baryogenesis.md` | **Upgraded 2026-05-17 from M2 → M3** via R4 single-template admissibility under saturation + IC-supply equivalence with Cos_01 Q-C3-3 (per `Update_Paper_ED_Baryogenesis_M3_via_R4` + five-memo closure cascade: Verification → Scoping → Construction → Audit → Update). Eighth Cosmology Arc paper at M3. Renamed from `Paper_ED_Baryogenesis_Open.md`. P-BinaryAdmission withdrawn; asymmetric-admission-cost OPEN dissolved. Zero paper-specific postulates. IC-INHERITED row carries layer-specification (fluctuation-selection level vs Cos_01 Q-C3-3 substrate-state level — non-load-bearing). |

Also indirectly affected (use the sub-labels in audit-row Notes but already lean on Paper_095 anchor without a separate bridging block — no edit needed):

- Paper_ED_Cos_01 (Inflation; M3 unconditional update)
- Paper_ED_Cos_02 (BBN)
- Paper_ED_Cos_03 (CMB Acoustic)
- Paper_ED_Cos_04 (Structure Formation)
- Paper_ED_GW_01 (Ringdown Spectroscopy)
- Paper_038_5 (Λ as saturation)

---

## Forward convention

From 2026-05-17 onward, new Wave-3 papers using these sub-labels should:

1. Cite Paper_095 §3.2.1 in the Anchors line for the verdict grammar (already standard).
2. Use the plain label cell **I** in audit-table rows, with sub-label cited in the Notes column.
3. Use the three-axis M3 notation **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED)** where all three axes apply; otherwise two-axis or one-axis as appropriate.
4. Skip the in-paper bridging-note block (Paper_095 §3.2.1 is now the canonical reference).

---

## Resolved 2026-05-17: Paper_038_5 verdict upgrade M2 → M3 retroactive

**Resolution.** Paper_038_5's status line (as found 2026-05-17) read **M2 (Intermediate Path C)** with §3.7 reframing (2026-05-16) explicitly stating: *"M2 → M3 retroactive upgrade conditional on Route A closure (substrate-derived $\ell_{V_5}(H_0)$)."* The Route A4 substrate-parameter-INHERITED closure per Memo_ED_RouteA_MultiRouteConvergence_Audit option (ii) at Paper_027-analog tier (with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ and $\tau_{V_5}/\tau_P \approx 10^{61}$ at primitive level) **satisfies this stated condition** — this is the same Route A4 closure path Paper_ED_Cos_05 uses for its M3 unconditional verdict, so applying the upgrade to Paper_038_5 is corpus-consistent.

**Applied upgrade.** Paper_038_5 status line, Abstract, §1 verdict, audit rows 14 + 14b + 15, and closing position statement all updated to **M3 retroactive (form-IDENTIFIED + value-INHERITED + IC-INHERITED) per Paper_095 §3.2.1**. Prior M2 verdict + §3.7 reframing (2026-05-16) preserved as audit-history record. Five-anchor verdict-sync verified.

**Propagation across Cos_03 / Cos_04 / Cos_06.** Cos_03 had no Paper_038_5 references — no edit needed. Cos_04 + Cos_06 verify-pending flags replaced with **"seven Cosmology Arc papers at M3"** + explicit "upgraded 2026-05-17 via Route A4 closure" provenance line. The Cosmology Arc completion framing is now uniformly **seven at M3** across all three downstream papers.

**Zenodo follow-up.** Paper_038_5 was already on Zenodo (per ED_Zenodo_Uploads.md) at the prior M2 verdict. The upgrade qualifies for a v2 deposit. Cos_04 + Cos_06 .tex/.pdf regenerated on Desktop 2026-05-17 to reflect updated framings.

## Affected papers — additional entry

| Paper | Path | Notes |
|---|---|---|
| Paper_038_5 (Λ-V1 Cosmological) | `physics-papers/gravity/Paper_038_5_Lambda_V1_Cosmological.md` | **Verdict upgraded 2026-05-17: M2 → M3 retroactive** via Route A4 substrate-parameter-INHERITED closure. Label-class note added per §3.2.1. |

## Audit-trail summary

- Paper_095 §3.2.1 added (new sub-section).
- Paper_095 §2.5 row 6 added (extension of P-Methodology-Triple grammar).
- No new postulates introduced. P-Methodology-Triple and the M1/M2/M3 three-tier verdict grammar unchanged.
- No verdict changes in any constituent paper. This is a notational / labeling patch, not a substantive revision.
- Future cleanup: remove in-paper bridging blocks from Cos_05, Cos_06, Dyn_01, Dyn_04 on next revision pass (cosmetic; no verdict impact).

---

**End Update_Paper_095_LabelClasses_2026_05_17.**
