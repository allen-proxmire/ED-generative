# Paper GR-Λ-V1 — Cosmological Constant $\Lambda$ as V1 Cosmological-Scale Integral

**Series:** Wave-3 Gravity Arc Extension — Cosmological Sector
**Status:** Wave-3 generative paper; **M2 (Intermediate Path C)** verdict with OPEN flag on substrate derivation of observed $\rho_\Lambda$ scale. Λ smallness derivation **reframed (2026-05-16)** as reducing to Route A + Friedmann inheritance, not direct V1-cutoff or specialized substrate-graph mechanism (see §3.7 + load-bearing program overview).
**Companions:** Paper_028 ($R_H = c/H_0$), Paper_038 (cosmological implications), Paper_089 (V1), Paper_017 (Lorentz covariantization), Paper_ED_SC_4.1 (SCBU BH ↔ cosmic boundary), Paper_027 (Newton's $G$ substrate-side), Paper_ED_Cos_01 (M3-upgraded inflation, vacuum-energy template). **Reframing-support memos:** Memo_ED_LambdaSmallness_Scoping; Memo_ED_DCGT_LambdaSuppression; Memo_ED_LoadBearingProgram_Overview.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the cosmological constant $\Lambda$ from nothing. Result is conditional on the 13 ED primitives (Paper_087) + declared paper-specific postulates.
2. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
3. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is stated in §1.
4. It does **not** claim derivation of the observed value $\rho_\Lambda \sim 10^{-120}\rho_P$ — that derivation is **OPEN, conditional on Route A closure** per §3.7 reframing. The naïve V1-cutoff estimate (§3.4) is off by ~$10^{60}$; preserved as record of failure. The smallness of $\Lambda$ is NOT explained by this paper directly; the substrate-graph closure path reduces to Route A + Friedmann inheritance (§3.7).
5. **INHERITED vs FORCED breakdown:** The V1-reframing of the cosmological-constant problem ($\Lambda$ as V1 cosmological-scale integral with curvature-coupling) is the structural ED contribution; the observed numerical value $\rho_\Lambda$ is INHERITED via empirical matching; substrate derivation of smallness reduces to Route A closure (highest-leverage open derivation per ED_MEMORY anchor 7).

---

## Abstract

This paper supplies the substrate-level structural identification of the cosmological constant $\Lambda$ as a V1 cosmological-scale integral of curvature-induced vacuum backreaction over the substrate-cosmology boundary $R_H = c/H_0$ (Paper_028, Paper_ED_SC_4.1). The structural form is form-IDENTIFIED via V1 finite second moment (Paper_089) + curved acoustic-metric coarse-graining (Paper_014) + cosmological-boundary integration domain. **Smallness derivation reframed (2026-05-16):** substrate-graph closure of $\rho_\Lambda \sim 10^{-120}\rho_P$ reduces to Route A closure (substrate-derived $\ell_{V_5}(H_0)$) + Friedmann inheritance $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$ + Paper_027 substrate-side $G$ via dimensional rearrangement (per Memo_ED_DCGT_LambdaSuppression). The naïve V1-cutoff approach (§3.4) is structurally absent substrate-side because ED's discrete substrate ontology doesn't admit infinite QFT mode-tower zero-point summation (§3.7). Per Paper_095 form-FORCED / value-INHERITED methodology, verdict remains **M2 (Intermediate Path C)** with **OPEN status now conditional on Route A**. Closure of Route A would close $\rho_\Lambda$ smallness simultaneously and upgrade Paper_038_5 verdict M2 → M3 retroactively (parallel to Paper_ED_Cos_01 M3-upgrade pattern). Key falsifier **F1:** Route A closure or independent substrate-derivation of $H_0$ would close OPEN status; Friedmann inheritance then gives $\rho_\Lambda$.

---

## §1 Statement of Result

**Claim.** The cosmological constant $\Lambda$ emerges in ED as the **integrated curvature-induced vacuum backreaction of the V1 kernel over the cosmological-boundary scale $R_H = c/H_0$**:
$$\Lambda \;\propto\; \int_{V \sim R_H^3} \rho_{\mathrm{vac, V1}}(x) \; d^3x ,$$
where $\rho_{\mathrm{vac, V1}}(x)$ is the V1 kernel's curvature-induced vacuum-energy density and the integration is over the substrate-cosmology boundary region.

The **structural form** — $\Lambda$ as cosmological-scale integral of V1 vacuum content — is form-IDENTIFIED (no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3) by:
1. V1 finite second moment (Paper_089) supplying a vacuum-energy density structure.
2. Curved acoustic-metric coarse-graining (Paper_014 N1/GR1) inducing curvature-coupling.
3. Cosmological boundary at $R_H$ supplying the integration domain (Paper_028 / Paper_ED_SC_4.1).

The **numerical value** $\Lambda \approx 1.1 \times 10^{-52}\,\text{m}^{-2}$ is INHERITED via empirical / canon-internal matching. Substrate-level first-principles derivation is OPEN (closes via Paper_ED_SC_4.2 Route A or analogous cosmological-coupling derivation).

Verdict: **M2 (Intermediate Path C)** with OPEN flag.

---

## §2 Primitive Inputs

### 2.1 Primitives invoked

- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — substrate-UV anchor.
- **P10 (Rule-type primitive)** — V1 kernel rule-type.
- **P11 (Commitment-irreversibility)** — V1 retardation.
- **P13 (Time homogeneity)** — $H_0$ as cosmological-rate.

### 2.2 Upstream Dependencies

- **I-028:** $R_H = c/H_0$ cosmic decoupling surface.
- **I-038:** Substrate-gravity cosmological implications.
- **I-089:** V1 finite-width retarded kernel.
- **I-014:** V1 in curved acoustic background (N1/GR1).
- **I-017:** Substrate→continuum Lorentz covariantization.
- **I-ED_SC_4_1:** BH ↔ cosmic boundary projection (SCBU framework).
- **I-RQM-T9:** Primitive-level UV finiteness.
- **I-CC:** Standard cosmological-constant machinery.

---

## §3 Derivation

### 3.1 V1 vacuum-energy density

At substrate level, the V1 kernel modulates participation-amplitude propagation. The substrate vacuum $|0\rangle_{\mathrm{sub}}$ (Paper_RQM_Q7Q8) carries zero-point vacuum fluctuation content from V1 kernel modes:
$$\rho_{\mathrm{vac, V1}}(x) \;=\; \frac{1}{2}\int \frac{d^3k}{(2\pi)^3} \;\omega_k\;|\hat K_{V1}(k)|^2 ,$$
where $\omega_k = c|k|$ for massless rule-types and $\hat K_{V1}(k)$ is the V1 form factor.

By Paper_RQM_T9 (primitive-level UV finiteness), this integral is **finite** at substrate level: the V1 form factor cuts off at $|k| \sim 1/\ell_P$. There is no UV divergence.

The substrate V1 vacuum-energy density is therefore a **finite** quantity at each spacetime point — unlike standard QFT vacuum energy, which is UV-divergent without renormalization.

### 3.2 Curvature-induced vacuum backreaction

**Honest framing:** A constant vacuum-energy contribution gravitates in GR (Weinberg 1989) and cannot be eliminated by gauge redefinition. The V1-kernel content does NOT remove the cosmological-constant problem at the level of substrate-physics; it reframes which scale enters the regulator. The residual hierarchy ($\rho_{\rm vac}^{\rm obs} \ll \rho_{\rm vac}^{\rm naïve QFT}$) is OPEN under the current substrate construction. This paper does not claim to derive the smallness of $\Lambda$.

In flat acoustic-metric regions, $\rho_{\mathrm{vac, V1}}$ is constant by P03 spatial homogeneity. We retain the kinematic discussion of the flat-region density below for completeness, but the constant component is NOT removable and contributes to the unresolved hierarchy.

In **curved** acoustic-metric regions (Paper_014 N1/GR1), the V1 vacuum-energy density is **modulated by curvature**:
$$\rho_{\mathrm{vac, V1}}^{\mathrm{curved}}(x) \;=\; \rho_{\mathrm{vac, V1}}^{\mathrm{flat}} \;+\; \alpha_{\mathrm{curv}} \cdot R(x) \cdot \ell_P^2 \cdot \rho_{\mathrm{vac, V1}}^{\mathrm{flat}} \;+\; O(R^2) ,$$
with $R(x)$ the Ricci scalar of the acoustic metric and $\alpha_{\mathrm{curv}}$ a substrate-derived coupling constant.

The curvature-induced part of the vacuum-energy density is the **vacuum backreaction**: substrate curvature induces non-trivial vacuum-energy content that does NOT cancel by gauge redefinition.

### 3.3 Cosmological-scale integration

At cosmological scales, the substrate is approximately flat on small scales but exhibits non-zero curvature integrated over the cosmological-boundary region $V \sim R_H^3$. The total curvature-induced vacuum backreaction is
$$E_{\mathrm{vac, cosmological}} \;=\; \int_{V \sim R_H^3} \alpha_{\mathrm{curv}} \cdot R(x) \cdot \ell_P^2 \cdot \rho_{\mathrm{vac, V1}}^{\mathrm{flat}} \;d^3x .$$

The cosmological constant $\Lambda$ enters the Einstein equation as
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = (8\pi G/c^4) T_{\mu\nu} ,$$
where $\Lambda$ acts as a "vacuum-energy contribution" with density $\rho_\Lambda = \Lambda c^4 / (8\pi G)$.

By matching $\rho_\Lambda$ to the cosmological-scale integrated V1 vacuum backreaction (§3.2):
$$\Lambda \;\propto\; \int_{V \sim R_H^3} \rho_{\mathrm{vac, V1}}^{\mathrm{curv}}(x) \, d^3x .$$

This is the substrate-level identification of $\Lambda$ as a **V1 cosmological-scale integral**.

### 3.4 Attempted dimensional rearrangement (preserved as a record of the attempt and its failure)

**OPEN:** Derivation of the observed value $\rho_\Lambda \sim 10^{-120} \rho_P$ from V1-substrate parameters is OPEN. The naïve V1-cutoff estimate is off by $\sim 10^{60}$ orders of magnitude on the dimensional rearrangement attempted below; the section is preserved as a record of the attempt and its failure.

The standard cosmological-constant problem: vacuum energy from QFT computed without UV regulator gives $\rho_\Lambda \sim \ell_P^{-4}$ (Planck-scale density), which is ~120 orders of magnitude larger than the empirical $\rho_\Lambda \sim H_0^4/G$ (Hubble-scale density).

A dimensional rearrangement using V1-cutoff content yields:
- V1 UV cutoff at $\ell_P$ supplies a Planck-scale density $\sim 1/\ell_P^4$ for the flat-region vacuum-energy density.
- The **curvature-induced** part (§3.2) is suppressed by $\ell_P^2 \cdot R(x)$, with $R(x) \sim 1/R_H^2$ at cosmological scales.
- Resulting: $\rho_\Lambda \sim \ell_P^2 / R_H^4 \cdot \rho_{\mathrm{Planck}} \sim 1/(R_H^2 \ell_P^2) = H_0^2/c^2 \cdot 1/\ell_P^2$.

This estimate fails to recover the observed scale: the discrepancy with empirical $\rho_\Lambda$ remains $\sim 10^{60}$ orders of magnitude on this rearrangement. The flat-region constant component is NOT removable; the curvature-suppression argument does not close the hierarchy. **No claim of substrate-level explanation of smallness is made.**

### 3.5 What is OPEN

- Substrate-level derivation of $\alpha_{\mathrm{curv}}$ from kernel data — OPEN (Paper_ED_SC_4.2 Route A analog).
- Resolution of the residual hierarchy (substrate-prediction $\sim H_0^2/(c^2\ell_P^2)$ vs empirical $\sim H_0^2/(c^2 \ell_P^2 \cdot N_{\mathrm{factor}})$ for some $N_{\mathrm{factor}}$) — OPEN.
- Substrate audit of dark-energy time-evolution (if $\Lambda$ is truly constant or slowly evolving) — OPEN.

### 3.6 Numerical content

- $\Lambda$ numerical value: INHERITED via empirical matching $\Lambda \approx 1.1 \times 10^{-52}\,\text{m}^{-2}$.
- $\alpha_{\mathrm{curv}}$: INHERITED.
- Structural form $\Lambda \propto$ V1 cosmological-scale integral: form-IDENTIFIED.

### 3.7 Reframing: Λ smallness reduces to Route A + Friedmann inheritance (Added 2026-05-16)

The naïve V1-cutoff approach of §3.4 fails by ~$10^{60}$. Per Memo_ED_DCGT_LambdaSuppression, the substrate-graph closure of $\Lambda$ smallness reduces to **Route A + Friedmann inheritance**, not specialized substrate-graph mechanism.

**Why naïve QFT estimates do NOT apply substrate-side.** Standard QFT's $\rho_{\mathrm{vac}}^{\mathrm{naive}} \sim M_P^4 \sim 10^{76}$ GeV⁴ comes from summing zero-point energies of an infinite tower of QFT modes between $k = 0$ and $k = M_P$:
$$
\rho_{\mathrm{vac}}^{\mathrm{naive}} = \frac{1}{2}\int_0^{M_P} \frac{d^3 k}{(2\pi)^3} \, \omega_k \sim M_P^4 .
$$
**ED's substrate is fundamentally discrete at $\ell_{\mathrm{ED}}$ per Paper_087 + Paper_089.** There is no infinite tower of modes between substrate-scale and observation-scale. The naïve QFT estimate is **structurally absent from the substrate ontology**. The "120-OOM problem" is partially dissolved at substrate-side by the discrete substrate ontology before any DCGT scale-separation enters.

**The actual substrate-graph closure path** (per Memo_ED_DCGT_LambdaSuppression):

Standard Friedmann equations for Λ-dominated late universe ($w = -1$):
$$
\rho_\Lambda = \frac{3 H_0^2}{8\pi G} = \frac{3}{8\pi} H_0^2 M_P^2 .
$$

The 120-OOM "smallness" IS the dimensionless ratio $(H_0/M_P)^2 \sim 10^{-122}$. **Not a separate fine-tuning question — a direct consequence of two substrate-side scales.**

Substrate-side derivations needed:
- **$M_P$ / $G$** via Paper_027 (Newton's $G$ derivation): substrate-side identified via dimensional rearrangement of $G, \hbar, c$ ↔ $\ell_P$. **INHERITED at I-level** per ED_MEMORY.
- **$H_0$** via Route A: substrate-derived $\ell_{V_5}(H_0)$ per Paper_ED_SC_4.2. **OPEN per ED_MEMORY anchor 7 — highest-leverage open derivation in the program.**

**If Route A closes**, $H_0$ is substrate-derivable from $\ell_{V_5}$ + substrate-side constants. Combined with Paper_027's substrate-side $M_P$ + Friedmann inheritance, $\rho_\Lambda$ closes at D-via-I as:
$$
\rho_\Lambda^{\mathrm{substrate}} = \frac{3}{8\pi} H_0^2(\text{Route A}) \cdot M_P^2(\text{Paper\_027}) .
$$

**Load-bearing #5 (Λ smallness) ≡ Route A closure + standard Friedmann inheritance.**

**The §3.4 naïve V1-cutoff approach is structurally on the wrong track.** It attempts substrate-graph closure via direct cutoff estimation, which inherits the naïve-QFT-mode-summation pattern. The substrate-side closure path is via macroscopic scales ($H_0$, $G$) — not via direct vacuum-energy summation. The §3.4 attempt is preserved as record of an early substrate-research-frontier exploration; the §3.7 reframing supplies the correct closure path.

**Cross-arc consequence of Route A closure:**
- ED-SC 4.x arc-wide M3 → M2 upgrade (pre-existing per ED_MEMORY anchor 7)
- **Paper_038_5 (this paper) retroactive upgrade M2 → M3** (closure of $\rho_\Lambda$ smallness)
- Paper_ED_Cos_05 (Dark Energy paper) draftable at M3 (conditional on Route A)
- Quantitative cosmological scales ($H_0$, $\rho_\Lambda$, cosmic age) substrate-side derivable

**Route A is the SINGLE substrate-research-frontier item with most consequential cross-arc impact in the corpus.**

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P08, P10, P11, P13 primitives | P | Primitives. |
| 2 | V1 finite-width retarded kernel | I | Paper_089. |
| 3 | V1 in curved acoustic background | I | Paper_014. |
| 4 | Primitive-level UV finiteness | I | Paper_RQM_T9. |
| 5 | V1 flat-region vacuum-energy density | D-via-I | Standard QFT vacuum-energy + UV cutoff. |
| 6 | Curvature-induced V1 vacuum backreaction | D-via-I | Standard QFT in curved spacetime + V1. |
| 7 | $R_H = c/H_0$ cosmological boundary | I | Paper_028. |
| 8 | Cosmological-scale integration domain | D-via-I | Composition with Paper_ED_SC_4.1. |
| 9 | $\Lambda \propto $ V1 cosmological-scale integral | D-via-I | Composition of inherited results is D-via-I, not D (per Paper_095 §2.3). |
| 10 | Hierarchy suppression $(\ell_P/R_H)^2$ structural (naïve V1-cutoff attempt) | OPEN — failed approach | §3.4 preserved as record of failure. **Reframed §3.7: substrate-graph closure path is via Route A + Friedmann inheritance, not direct V1-cutoff.** |
| 11 | $\alpha_{\mathrm{curv}}$ coupling constant | I | Substrate parameter; OPEN derivation. |
| 12 | Empirical $\Lambda$ value | I | Empirical. |
| 13 | Substrate-level derivation of $\alpha_{\mathrm{curv}}$ | OPEN | Future work; reduces under §3.7 framework to subset of Route A. |
| 14 | Substrate derivation of observed $\rho_\Lambda$ scale via Route A + Friedmann inheritance | **OPEN (conditional on Route A)** | §3.7. Closure path identified: $\rho_\Lambda = (3/8\pi) H_0^2(\text{Route A}) M_P^2(\text{Paper\_027})$. If Route A closes, $\rho_\Lambda$ closes at D-via-I. Naïve V1-cutoff (§3.4) is structurally on the wrong track. |
| 15 | Verdict M2 (Intermediate Path C); upgrades to M3 conditional on Route A closure | A→position | Per Paper_095 §3.3 line 77. **M2 → M3 retroactive upgrade conditional on Route A** per §3.7 reframing. |

---

## §5 Falsification Criteria

- **F1 (reframed 2026-05-16):** Route A closure (substrate-derived $\ell_{V_5}(H_0)$ per Paper_ED_SC_4.2) gives substrate-side $H_0$. Combined with Paper_027 substrate-side $M_P$ + Friedmann inheritance $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$, this closes the OPEN status and upgrades verdict M2 → M3 retroactively (parallel to Paper_ED_Cos_01 M3-upgrade pattern). Direct V1-parameter derivation per §3.4 is structurally on the wrong track (§3.7 reframing).
- **F2:** Substrate evidence that V1 vacuum backreaction does NOT couple to curvature — refutes step 6.
- **F3:** Detection of $\Lambda$ evolution inconsistent with V1 cosmological-scale integral — would require revising step 9.
- **F4:** Resolution of the residual hierarchy from a non-substrate source — would shift the dominant mechanism away from V1 cosmological-scale integration.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

This paper supplies the substrate-level structural identification of the cosmological constant as a V1 cosmological-scale integral, addressing the previously-flagged corpus gap (List 1 item: "Curvature-induced vacuum backreaction → Λ as V1 cosmological-scale integral").

**Relationship to other papers:**
- **Paper_089 V1:** supplies kernel structure.
- **Paper_014 (N1/GR1):** curved-acoustic-metric V1.
- **Paper_028, 038:** cosmological-boundary content.
- **Paper_ED_SC_4.1, 4.6:** SCBU framework places $\Lambda$ in regime-4 cosmological projection.

**Numerical content INHERITED.** $\Lambda$ value, $\alpha_{\mathrm{curv}}$. **Form IDENTIFIED.** $\Lambda$ as V1 cosmological-scale integral.

**Reframing (2026-05-16, §3.7):** Substrate-graph derivation of $\rho_\Lambda$ smallness reduces to **Route A + Friedmann inheritance**, not direct V1-cutoff (§3.4 preserved as record of failure). Naïve QFT vacuum-energy estimates are **structurally absent substrate-side** because ED's discrete substrate doesn't admit infinite QFT mode-tower zero-point summation. The 120-OOM "smallness" IS the dimensionless ratio $(H_0/M_P)^2$ — a direct Friedmann consequence given the two substrate-side scales.

**Closure path:** $\rho_\Lambda^{\mathrm{substrate}} = (3/8\pi) H_0^2(\text{Route A}) \cdot M_P^2(\text{Paper\_027})$. Route A is **the single highest-leverage open derivation in the corpus** per ED_MEMORY anchor 7. Its closure simultaneously:
- Closes Paper_038_5 (this paper) at D-via-I; verdict M2 → M3 retroactive upgrade
- Closes ED-SC 4.x arc-wide M3 → M2 upgrade
- Unlocks Paper_ED_Cos_05 (Dark Energy paper) at M3
- Supplies substrate-side derivation of fundamental cosmological scales

**Future work.** Route A closure (substrate-derived $\ell_{V_5}(H_0)$, per Paper_ED_SC_4.2) is the load-bearing remaining derivation. Substrate audit of dynamical dark energy / quintessence-class alternatives independent of Route A. Substrate audit of the cosmological "coincidence problem" (why universe transitions to Λ-dominated at current cosmic age) — independent of Route A.

Verdict: **M2 (Intermediate Path C)** with OPEN flag; **conditional retroactive upgrade to M3 pending Route A closure**.

---

**End Paper GR-Λ-V1.**
