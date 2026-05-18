# Paper_ED_Dyn_03 — Substrate-Graph Radiation Law: EM Larmor and GW Quadrupole via Noether Flux + DCGT

**Series:** Wave-3 Generative Papers (Dynamics Arc — anchor for ED Radiation Law)
**Status:** Conditional structural derivation given the 13 ED primitives (Paper_087) + DCGT (Paper_073) A→regime hydrodynamic-window scale-separation. Substrate-side mechanism for time-varying $\Psi$ source states proposed; the qualitative-mechanism load-bearing closures (substrate-graph source-class criterion and substrate-graph stress-energy flux form per source class) are OPEN. Verdict per Paper_095: **M2 (Intermediate Path C).** Companion to Paper_ED_Cos_01 (Inflation, M2) and Paper_ED_Dyn_02 (Horizon-Motion, M2) under the same substrate-side Noether template applied to time-varying rather than uniform-saturation or non-uniform-stationary states.
**Date:** 2026-05-16
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$); Paper_089 (V1 retarded kernel + T18); Paper_093 (T18 kernel-arrow); Paper_012 (P-RB-1 substrate-c); Paper_015 / T17 (gauge fields — EM analog); Paper_027 (Newton's $G$); Paper_032 (1/r dilution); Paper_109 (Lorentz reps); Paper_116 (massless-slot two-mode); Paper_ED_Cos_01 (saturation-case Noether template, M2); Paper_ED_Dyn_02 (non-saturation extension, M2); Paper_ED_GW_00 (GW saddle-Hessian framework; row 12 partial form-closure target); Paper_095 (verdict grammar). **Substrate-research support:** Memo_ED_DCGT_VacuumEnergyMapping §3 (substrate-side Noether template); Memo_ED_RadiationLaw_NoetherFlux + Audit (this paper's substrate-graph extension proposal + adversarial audit identifying Q1 + Q2 inheritance gaps).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim closed-proof derivation of Maxwell or linearized Einstein retarded-Green's-function machinery from substrate primitives. Maxwell and linearized Einstein retarded structure is **INHERITED** from standard physics via DCGT continuum bridge.
2. It does **not** sit within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). ED is in the substrate-ontology research program ('t Hooft cellular-automaton; Wolfram Ruliad; causal-set program, Sorkin et al.). Methodology per Paper_095 (form-FORCED / value-INHERITED).
3. It does **not** introduce new substrate primitives or paper-specific postulates.
4. It does **not** derive numerical radiation coefficients ($1/(6\pi\epsilon_0 c^3)$ for Larmor; $1/(5c^5)$ for quadrupole) from substrate parameters alone. Coefficients are INHERITED at standard-physics-analog level via Paper_015 T17 (EM gauge content) and Paper_027 (Newton's $G$); substrate-graph derivation of the coefficients is OPEN substrate-research-frontier work.
5. **Two qualitative-mechanism OPEN items are load-bearing for the verdict** and explicitly named (§3.5 + audit rows 6, 7):
   - **OPEN-RL-Q1 (substrate-graph source-class criterion):** explicit substrate-graph derivation identifying "accelerated chain" (EM-class source) and "time-varying mass-quadrupole" (GW-class source). Currently INHERITED by standard-EM/GR analog applied to Paper_015 T17 + Paper_089 chain-arrow direction + Paper_ED_SC_4_9 saddle-Hessian content; substrate-graph mapping not constructed.
   - **OPEN-RL-Q2 (substrate-graph stress-energy flux form derivation):** explicit substrate-graph derivation that V1 + V5 kernel structure gives Poynting-class flux ($\sim \vec E \times \vec B$ analog) for accelerated gauge-coupled chains and quadrupole-flux ($\sim |\dddot Q|^2$ scaling) for time-varying mass-quadrupole sources. Currently INHERITED by standard-QFT-analog choices applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$; substrate-graph construction OPEN.
6. It does **not** claim M3 on Cos_01's or Dyn_02's basis. Both companion papers sit at M2 under the same Q1/Q2 inheritance pattern. Closure of Q1 + Q2 substrate-graph would jointly upgrade Cos_01, Dyn_02, and this paper M2 → M3.
7. **GW_00 audit row 12 (substrate-graph derivation of source-amplitude formula) is partially closed here at form-only / M2-equivalent level.** §3.4 identifies the substrate-graph quadrupole *form* via the inherited M3-template-analog chain; the *numerical coefficient* $1/(5c^5)$ remains OPEN (this paper's audit row 14). The corpus-side GW_00 row 12 framing should be updated to reflect this scoped form-IDENTIFIED-at-M2 closure, not a full form+coefficient closure.

---

## Abstract

Electromagnetic and gravitational radiation in ED are proposed at substrate-graph level by applying the substrate-side Noether template (Memo_ED_DCGT_VacuumEnergyMapping §3) to **time-varying** $\Psi$ source states. Two source classes are candidate-identified: accelerated gauge-coupled chains (Paper_015 T17 + V1 chain-arrow direction change between commitments) for the EM Larmor analog, and time-varying mass-quadrupole $\Psi$-distributions (Paper_ED_SC_4_9 saddle-Hessian framework) for the GW quadrupole analog. Substrate-side Noether on $\mathcal{L}_{\mathrm{sub}}$ for time-varying $\Psi$ produces non-trivial flux $T^{0i}_{\mathrm{sub}}$; DCGT (Paper_073), in its natural hydrodynamic-flux regime, translates to continuum stress-energy flux; standard Maxwell and linearized Einstein retarded-Green's-function machinery inherit; $P_{\mathrm{EM}} = q^2 a^2/(6\pi\epsilon_0 c^3)$ and $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ recover at standard physical frequencies. Substrate-c bound preserved throughout. **Verdict per Paper_095: M2 (Intermediate Path C)**, matching Cos_01 + Dyn_02. Two load-bearing OPEN substrate-graph gaps drive the verdict: substrate-graph source-class criterion (Q1) and substrate-graph stress-energy flux form per source class (Q2); both are INHERITED by standard-EM/GR analog. Numerical radiation coefficients are also INHERITED. **F1 (sharpest):** detection of monopole or dipole gravitational radiation, or scalar/longitudinal EM radiation modes — refutes the substrate-side polarization-mode admittance inherited from Paper_015 T17 + Paper_ED_GW_00 + Paper_109 + Paper_116.

---

## §1 Statement of Result

The substrate-graph radiation law applies the substrate-side Noether template (Memo_ED_DCGT_VacuumEnergyMapping §3) to time-varying $\Psi$ source states. Two candidate source-class identifications (§3.1 + §3.2; load-bearing OPEN-RL-Q1) yield the substrate-side EM and GW analogs. Substrate-side Noether (§3.3; load-bearing OPEN-RL-Q2 for the specific flux form per source class) gives non-trivial flux components $T^{0i}_{\mathrm{sub}}$. DCGT translation (§3.4) — radiation being its natural regime — recovers Maxwell and linearized Einstein retarded structure at standard physical frequencies. Result:

$$
P_{\mathrm{EM}} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3}, \qquad
P_{\mathrm{GW}} = \frac{G}{5 c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle.
$$

$1/r$ amplitude falloff inherits from Paper_032 + V1 spherical dilution; polarization content (two transverse EM modes; two transverse GW modes $h_+, h_\times$; no scalar/monopole/dipole gravitational radiation) inherits from Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7.

**FORM:** substrate-side Noether for time-varying $\Psi$ + DCGT translation + standard-physics retarded-Green's-function inheritance — **proposed via the Memo_ED_DCGT_VacuumEnergyMapping §3 template extended to non-stationary sources** with Q1 + Q2 OPEN. Form-IDENTIFIED via substrate-graph composition would require closing Q1 + Q2; current state is **form-INHERITED via standard-EM/GR analog**.

**VALUE:** numerical coefficients ($1/(6\pi\epsilon_0 c^3)$; $1/(5c^5)$) INHERITED at standard-physics-analog level via Paper_015 T17 + Paper_027 + standard radiation theory; substrate-graph derivation OPEN.

**Verdict: M2 (Intermediate Path C) per §4 audit table.** Matches Cos_01 + Dyn_02 verdicts on the same template. Closure of Q1 + Q2 substrate-graph would upgrade the verdict M2 → M3 and would simultaneously upgrade Cos_01 + Dyn_02 (shared Q1/Q2 pattern).

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02, P03 (Noether translation invariance), P04, P09, P10 (multiple rule-types; supports candidate Q1 closure), P11, P12, P13.

**Upstream papers:**
- Paper_012 (substrate-c bound, P-RB-1) — supplies $c$
- Paper_015 / T17 (gauge fields) — supplies substrate-side gauge-bundle charge $q$
- Paper_027 (Newton's $G$ via dimensional rearrangement) — supplies $G$
- Paper_032 (1/r dilution) — supplies amplitude falloff
- Paper_073 (DCGT)
- Paper_089 (V1 retarded kernel + T18) — substrate-side retarded Green's function analog
- Paper_093 (T18 kernel-arrow) — chain-arrow direction
- Paper_109 (Lorentz reps); Paper_116 (massless-slot two-mode) — polarization content
- Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ + saddle Hessian)
- Paper_ED_Cos_01 (saturation-case Noether template, M2)
- Paper_ED_Dyn_02 (non-saturation extension, M2 — same Q1/Q2 pattern)
- Paper_ED_GW_00 (GW saddle-Hessian framework; row 12 partial form-closure target)
- Standard Maxwell + linearized Einstein retarded-Green's-function machinery (textbook inheritance, INHERITED)

**Substrate-research support (template + audit context):**
- Memo_ED_DCGT_VacuumEnergyMapping §3 (substrate-side Noether template; audit ACCEPTED at approximately-vacuum-energy level for the saturation case — that audit acceptance does not propagate to the time-varying case, which is where Q1 + Q2 enter)
- Memo_ED_RadiationLaw_NoetherFlux + Audit (this paper's time-varying extension proposal + adversarial audit identifying Q1 + Q2 as load-bearing OPEN substrate-graph gaps; Q3 as regime restriction, not load-bearing)

**No paper-specific postulates; no new substrate primitives.**

---

## §3 Derivation

### 3.1 Candidate source-class identification: accelerated chain (EM analog) — OPEN-RL-Q1

Per Paper_089 + Paper_093 T18, each chain $C$ has a V1-mediated chain-arrow direction $\sigma_C(e_n)$ at each commitment event. Per Paper_012 P-RB-1, propagation is bounded by substrate-c.

**Candidate substrate-side acceleration:** when the chain-arrow direction changes between consecutive commitments ($\sigma_C(e_n) \neq \sigma_C(e_{n+1})$), the chain candidate-undergoes substrate-graph acceleration — the candidate-analog of a charged particle's worldline curving. Per Paper_015 T17, chains with rule-type gauge-bundle coupling carry the substrate-side analog of EM charge. An accelerating gauge-coupled chain has time-varying gauge-bundle content → candidate substrate-side EM radiation source.

**OPEN-RL-Q1 (EM):** the specific mapping *"V1-chain-arrow-direction change = EM-class acceleration analogous to standard accelerated charge"* is **not constructed** substrate-graph. The corpus supplies the supporting content (chain-arrow direction via T18; gauge bundles via T17); the specific analog mapping that elevates chain-arrow change to "EM-class acceleration" is INHERITED by standard EM analog. **Load-bearing for the verdict.**

### 3.2 Candidate source-class identification: time-varying mass-quadrupole (GW analog) — OPEN-RL-Q1

Per Paper_ED_GW_00 §3.1 + Paper_ED_SC_4_9, time-varying saddle-Hessian content is the substrate-side mechanism for GW emission. A spatial $\Psi$-distribution with time-varying spatial second-moment

$$
Q_{ij}^{\mathrm{sub}}(\ell, t) = \int (\Psi\text{ density})(x_i x_j - \tfrac{1}{3}\delta_{ij}|x|^2) \, d^3x
$$

has time-varying saddle-Hessian content at the source locus; non-trivial $\dddot Q_{ij}$ → candidate substrate-side GW radiation.

**OPEN-RL-Q1 (GW):** the specific mapping *"time-varying $\Psi$ spatial second-moment = mass-quadrupole analogous to standard GR"* is INHERITED by standard GR analog applied to Paper_ED_SC_4_9 saddle content. Substrate-graph construction OPEN. **Load-bearing for the verdict** (shared Q1 row with §3.1).

### 3.3 Substrate-side Noether flux for time-varying $\Psi$ — OPEN-RL-Q2

Applying the substrate-side Noether template (Memo_ED_DCGT_VacuumEnergyMapping §3) to time-varying $\Psi$:

$$
T^{\mu\nu}_{\mathrm{sub}} = \sum_{K \in \{V_1, V_5\}} \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}.
$$

For time-varying $\Psi$ the flux components

$$
T^{0i}_{\mathrm{sub}} = \sum_K \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K^0 \Psi)} \nabla_K^i \Psi
$$

are non-trivial — substrate-side energy transport in the $i$-direction.

**Candidate specific flux forms** (per source class, inherited by standard analog):

- **Accelerated gauge-coupled chain:** $T^{0i}_{\mathrm{sub}}|_{\mathrm{EM}} \sim$ (substrate analog of $\vec E \times \vec B$)$^i$ — Poynting-vector-class structure.
- **Time-varying mass-quadrupole:** $T^{0i}_{\mathrm{sub}}|_{\mathrm{GW}}$ scales with $|\dddot Q_{ij}|^2$ at appropriate retardation.

**OPEN-RL-Q2:** the specific flux forms (Poynting-class for EM; quadrupole-flux for GW) are INHERITED by standard-QFT-analog choice applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$. Lorentz-covariance of V1 (Paper_089 §3) is necessary but not sufficient — standard QFT distinguishes EM-class (gauge-invariant, conformally coupled, traceless) from scalar-class (non-traceless) flux structures; whether V1 + V5 kernel structure delivers EM-class for accelerated gauge-coupled chains and quadrupole-flux for time-varying mass distributions is not derived substrate-graph. **Load-bearing for the verdict.** Closure (jointly with Q1) would upgrade verdict M2 → M3.

### 3.4 DCGT translation + Maxwell / linearized Einstein retarded-Green's-function inheritance

Per Paper_073, DCGT coarse-grains within $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. **Radiation is the hydrodynamic-flux phenomenon DCGT was specifically built to handle** — BBGKY + Chapman-Enskog preserve energy-momentum conservation and continuum flux structure under coarse-graining. DCGT translation is structurally cleaner than for the saturation regime (Cos_01) or for non-saturation chain-class identification (Dyn_02). Substrate-side flux candidate-forms (per Q1 + Q2) translate to continuum stress-energy flux preserving the form choice.

**V1 / continuum retarded Green's function consistency:** V1's finite-width retarded support reduces to standard continuum $G^{\mathrm{ret}} = \delta(t - t' - |x-x'|/c)/(4\pi|x-x'|)$ at coarse-graining scales $R_{\mathrm{cg}} \gg \ell_{V_1}$. For standard radiation frequencies ($\omega \ll c/\ell_{V_1}$), V1 is effectively delta-function-supported at the coarse-graining scale. **Regime restriction Q3:** near-Planck-scale frequencies ($\omega \to c/\ell_{V_1}$) are at edge of DCGT validity; not load-bearing for standard radiation phenomenology.

Maxwell retarded potentials + standard multipole expansion give the EM Larmor formula; linearized Einstein retarded-Green's-function + transverse-traceless multipole expansion give the GW quadrupole formula. These are textbook standard radiation theory inheritance; the substrate-side stress-energy flux (conditional on Q1 + Q2 closures) supplies the source. Resulting power expressions:

$$
P_{\mathrm{EM}} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3}, \qquad
P_{\mathrm{GW}} = \frac{G}{5 c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle.
$$

$1/r$ amplitude falloff from Paper_032 + V1 spherical dilution. Polarization content from Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7.

**GW_00 row 12 scoped partial closure:** the *quadrupole form* identification — substrate-side Noether flux + DCGT + linearized Einstein machinery → $\dddot Q$-scaling — is form-IDENTIFIED at M2-equivalent level via this paper's chain (conditional on Q1 + Q2). The *numerical coefficient* $1/(5c^5)$ remains OPEN at substrate-graph level (this paper's audit row 14). GW_00 row 12 is therefore partially closed (form aspect at M2; coefficient still OPEN), not fully closed. Corpus-side GW_00 row 12 framing should be updated to reflect this scope.

### 3.5 Closure qualifications + cross-arc placement

Per Memo_ED_RadiationLaw_NoetherFlux_Audit, three qualifications:

- **Q1 (load-bearing OPEN):** substrate-graph source-class criterion — both §3.1 (EM-class) and §3.2 (GW-class). Inherited by standard-EM/GR analog. Audit rows 6.
- **Q2 (load-bearing OPEN):** substrate-graph stress-energy flux form per source class — §3.3 specific flux structures. Inherited by standard-QFT analog. Audit row 7.
- **Q3 (regime restriction, not load-bearing):** DCGT applies cleanly for standard radiation frequencies; near-Planck-scale at edge of validity. §3.4 + audit row 8.

The Q1 + Q2 OPEN status drives the M2 verdict. Closure of Q1 + Q2 substrate-graph would simultaneously upgrade Cos_01, Dyn_02, and this paper M2 → M3 (the three papers share the same Q1/Q2 pattern).

**Cross-arc placement (M2-honest framing):**
- **Paper_ED_GW_00** sits at M3 on the strength of substrate-graph-derived saddle-Hessian propagation + two-polarization derivation via Paper_116 + Paper_109 + T1 + V1 composition — load-bearing content not subject to Q1/Q2 inheritance. This paper does not group with GW_00 at the same verdict tier.
- **Paper_ED_Cos_01, Paper_ED_Dyn_02, this paper** sit at M2 on the same substrate-side Noether template applied to saturation / non-saturation-stationary / time-varying $\Psi$ states respectively, all subject to Q1/Q2 substrate-graph closure for upgrade.
- **Paper_ED_Dyn_05 (Inspiral; pending draft)** would inherit this paper's GW radiation content as energy-loss source term — at M2 if this paper is M2.
- **Paper_ED_GW_01 (BH ringdown; pending draft)** would gain substrate-side radiation-amplitude content at M2 level.
- **Paper_ED_Cos_05 (Dark Energy; pending draft)** inherits the saturation case at M2 via Cos_01.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P04, P09, P10, P11, P12, P13 | **P** | Paper_087. P03 + P13 supply Noether translation invariance; P04 + P10 candidate-underwrite Q1 closure. |
| 2 | Upstream inheritance block | **I** | Paper_012; Paper_015/T17; Paper_027; Paper_032; Paper_073; Paper_089; Paper_093; Paper_109; Paper_116; Paper_ED_SC_4_9; Paper_ED_Cos_01 (M2); Paper_ED_Dyn_02 (M2); Paper_ED_GW_00. |
| 3 | Standard Maxwell + linearized Einstein retarded-Green's machinery | **I** | Textbook inheritance; no substrate-graph derivation claimed. |
| 4 | Saturation-case template (Memo_ED_DCGT_VacuumEnergyMapping §3 Noether) extended here to time-varying $\Psi$ | **D-via-I (conditional)** | §3.3. Template inherited from Cos_01 saturation chain; extension to time-varying $\Psi$ is the substrate-side mechanism proposed here. Conditional on Q1 + Q2 closures. |
| 5 | DCGT translation in radiation regime + V1 / continuum $G^{\mathrm{ret}}$ consistency | **D-via-I** | §3.4. Radiation is DCGT's natural regime; consistency holds for $R_{\mathrm{cg}} \gg \ell_{V_1}$. **Regime restriction Q3:** near-Planck-scale frequencies at edge of validity; not load-bearing. |
| 6 | **OPEN-RL-Q1: substrate-graph source-class criterion** for accelerated chain (EM-class) and time-varying mass-quadrupole (GW-class) | **OPEN** | §3.1, §3.2. Specific analog mappings INHERITED by standard EM/GR analog applied to Paper_015 T17 + Paper_089 chain-arrow direction + Paper_ED_SC_4_9 saddle-Hessian content; substrate-graph mapping not constructed. **Load-bearing for verdict tier.** Shared Q1 with Cos_01 + Dyn_02 (analogous gap; joint closure would upgrade all three). |
| 7 | **OPEN-RL-Q2: substrate-graph stress-energy flux form derivation** (V1 + V5 kernel structure → Poynting-class for EM-class source; quadrupole-flux for GW-class source) | **OPEN** | §3.3. Form choice INHERITED by standard-QFT-analog (EM-class gauge-invariant vs scalar-class). Lorentz-covariance of V1 necessary, not sufficient. **Load-bearing for verdict tier.** Closure (with Q1) would upgrade verdict M2 → M3. |
| 8 | EM Larmor form $P_{\mathrm{EM}} \propto q^2 a^2$ | **D-via-I (conditional)** | §3.4. Composition: substrate-side flux (rows 4, 6, 7) + DCGT (row 5) + Maxwell retarded machinery (row 3). Conditional on Q1 + Q2 closures. $q$ via Paper_015 T17; $c$ via Paper_012; $\epsilon_0$ INHERITED. |
| 9 | GW quadrupole form $P_{\mathrm{GW}} \propto G\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ | **D-via-I (conditional)** | §3.4. Composition: substrate-side flux (rows 4, 6, 7) + DCGT (row 5) + linearized Einstein retarded machinery (row 3). Conditional on Q1 + Q2 closures. $G$ via Paper_027; $c$ via Paper_012. **Partially closes GW_00 audit row 12 at form-only / M2-equivalent level; coefficient (row 14 below) remains OPEN.** |
| 10 | $1/r$ amplitude falloff at large distance | **I** | §3.4. Paper_032 + V1 spherical dilution. |
| 11 | Polarization content: two transverse EM modes; two transverse GW modes ($h_+, h_\times$); no scalar/longitudinal EM; no monopole/dipole gravitational radiation | **I** | §3.4. Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7; standard radiation selection rules via charge / mass-momentum conservation. **F1 sharpness rests on this row.** |
| 12 | Mixed-source-class superposition | **D-via-I (conditional)** | §3.3. Additive Noether stress-energy with per-source-class forms. Conditional on Q1 + Q2 supplying per-class structure. |
| 13 | Saddle-Hessian-dynamics alternative route to substrate-graph radiation (cf. Memo_ED_HorizonMotion_Scoping Route 2 analog) | **OPEN** | Substrate-research-frontier alternative; substantively distinct content potentially valuable for BH-arc / dynamics-arc cross-applications. Not load-bearing for the M2 framing here. |
| 14 | Substrate-graph derivation of numerical coefficients ($1/(6\pi\epsilon_0)$ for Larmor; $1/5$ for quadrupole) from substrate parameters alone | **OPEN** | Substrate-research-frontier; coefficients currently INHERITED at standard-physics-analog level. **Independent of Q1 + Q2** (substrate-graph form closure would not automatically give coefficients). Not load-bearing for the M2 form-claim, but load-bearing for any future full-value M3 upgrade. |
| 15 | Radiation at near-Planck-scale frequencies ($\omega \to c/\ell_{V_1}$); higher-multipole and radiation-reaction extensions | **OPEN** | Beyond DCGT hydrodynamic-window or standard physical-frequency regime; substrate-research-frontier. Not load-bearing for standard radiation phenomenology. |
| 16 | Verdict M2 (Intermediate Path C) | **A→position** | Per Paper_095 §3.3 line 77. Five-anchor verdict-sync: status line / abstract / §1 / this row / §6 Position Statement all M2. Upgrade M2 → M3 requires closing Q1 + Q2 substrate-graph (shared with Cos_01 + Dyn_02). |

**Audit summary:** zero pure-D rows; four conditional D-via-I rows (4, 8, 9, 12 — conditional on Q1 + Q2); one unconditional D-via-I row (5); four I rows (2, 3, 10, 11); **two load-bearing OPEN substrate-graph rows** (6, 7 — Q1 + Q2); three non-load-bearing OPEN rows (13, 14, 15); one A→position verdict row. No paper-specific postulates; no new substrate primitives.

---

## §5 Falsification Criteria

- **F1 (sharpest):** Detection of monopole gravitational radiation, dipole gravitational radiation, or scalar/longitudinal EM radiation modes — substrate-side admitted modes are restricted by Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7 via standard charge / mass-momentum conservation. Refutes §3.4 polarization inheritance (audit row 11). (Currently consistent: LIGO/Virgo polarization-content analyses constrain non-tensor modes; no observed scalar/longitudinal EM modes.)

- **F2:** Observation of radiation power scaling violating Larmor ($P \propto q^2 a^2$) or quadrupole ($P \propto G \dddot Q^2$) forms at standard physical frequencies beyond standard observational uncertainty. Refutes §3.4 form closure. (Currently consistent: Hulse-Taylor and other pulsar-binary inspirals match GW quadrupole within $\sim 0.1\%$ power-loss accuracy; accelerated-charge radiation matches Larmor across all examined regimes.)

- **F3:** Refutation of DCGT hydrodynamic-window applicability at standard radiation frequencies — discovery of substrate-scale physics that interferes with coarse-graining at observable radiation frequencies. Refutes §3.4 / Q3.

- **F4:** Substrate-graph proof that V1 + V5 kernel structure cannot host both Poynting-class (EM-analog) flux and quadrupole-flux (GW-analog) flux forms simultaneously — e.g., a substrate-graph no-go theorem showing the kernel-structure admits only one flux class. Refutes the candidate Q2 form choices (§3.3) and forces a different substrate-graph mechanism.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

The ED radiation law is proposed at substrate-graph level by applying the substrate-side Noether template (Memo_ED_DCGT_VacuumEnergyMapping §3) to time-varying $\Psi$ source states. Accelerated gauge-coupled chains supply the candidate substrate-side EM-analog source; time-varying $\Psi$ second-moment distributions supply the candidate substrate-side GW-analog source. DCGT — in its natural radiation regime — translates substrate stress-energy flux to continuum stress-energy flux; Maxwell and linearized Einstein retarded-Green's-function machinery inherit; standard Larmor and quadrupole formulas recover at standard physical frequencies. Two load-bearing OPEN qualitative-mechanism gaps — substrate-graph source-class criterion (Q1) and substrate-graph stress-energy flux form per class (Q2) — drive the M2 verdict; both are currently INHERITED by standard-EM/GR analog rather than substrate-graph-derived.

**Verdict: M2 (Intermediate Path C) per Paper_095.** Matches Paper_ED_Cos_01 + Paper_ED_Dyn_02 on the same template (saturation / non-saturation-stationary / time-varying applications of the substrate-side Noether template). Joint closure of Q1 + Q2 substrate-graph would simultaneously upgrade all three companion papers M2 → M3 and would fully close Paper_ED_GW_00 audit row 12 (currently partially closed here at form-only / M2-equivalent level via §3.4; corpus-side GW_00 row 12 framing should be updated to reflect this scope rather than a full form+coefficient closure). Paper_ED_Dyn_05 (Inspiral; pending) and Paper_ED_GW_01 (BH ringdown; pending) inherit this paper's radiation content at M2. **Paper_ED_GW_00 itself sits at M3 on independent substrate-graph content** (saddle-Hessian propagation + two-polarization derivation via Paper_116 + Paper_109 + T1 + V1 composition) and does not group with this paper's M2 verdict tier.

---

**End Paper_ED_Dyn_03.**
