# Paper_ED_Dyn_03 — Substrate-Graph Radiation Law: EM Larmor and GW Quadrupole via Noether Flux + DCGT

**Series:** Wave-3 Generative Papers (Dynamics Arc — anchor for ED Radiation Law)
**Status:** Conditional structural derivation given the 13 ED primitives (Paper_087) + DCGT (Paper_073) hydrodynamic-window scale-separation + the Paper_ED_Cos_01 M3 substrate-graph-chain template applied to **time-varying** $\Psi$ source states. Verdict per Paper_095: **M3 (form-IDENTIFIED + value-INHERITED).** Load-bearing #4 of the Cosmology/Dynamics load-bearing program (`event-density/papers/Load_Bearing_Program_2026_05/04_RadiationLaw/`); closure D-via-I per Memo_ED_RadiationLaw_NoetherFlux + audit ACCEPTED at "approximately-standard-physics level" with standard-EM/GR-analog inheritance qualifications.
**Date:** 2026-05-16
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$); Paper_089 (V1 retarded kernel + T18); Paper_093 (T18 kernel-arrow); Paper_012 (P-RB-1 substrate-c); Paper_015 (T17 gauge fields — EM analog); Paper_027 (Newton's $G$ — for GW coefficient); Paper_032 (1/r dilution); Paper_109 (Lorentz reps); Paper_116 (massless-slot two-mode); Paper_ED_Cos_01 (M3 saturation-regime template); Paper_ED_Dyn_02 (M3 non-saturation template); Paper_ED_GW_00 (GW saddle-Hessian framework; row 12 closure target); Paper_095 (verdict grammar). **Load-bearing-program support:** Memo_ED_RadiationLaw_Scoping; Memo_ED_RadiationLaw_NoetherFlux; Memo_ED_RadiationLaw_NoetherFlux_Audit; Memo_ED_LoadBearingProgram_Overview (all under `event-density/papers/Load_Bearing_Program_2026_05/`).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim closed-proof derivation of Maxwell or linearized Einstein retarded-Green's-function machinery from substrate primitives. Maxwell and linearized Einstein retarded structure is **INHERITED** from standard physics via DCGT continuum bridge.
2. It does **not** sit within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). ED is in the substrate-ontology research program ('t Hooft cellular-automaton; Wolfram Ruliad; causal-set program, Sorkin et al.).
3. It does **not** quantitatively derive Larmor coefficient $1/(6\pi\epsilon_0 c^3)$ or quadrupole coefficient $1/(5c^5)$ from substrate parameters alone. Numerical coefficients are INHERITED at standard-physics-analog level via Paper_015 T17 (EM gauge content) and Paper_027 (Newton's $G$); substrate-graph derivation of the coefficients themselves is OPEN substrate-research-frontier work.
4. It does **not** introduce new substrate primitives or paper-specific postulates. The radiation law arises by applying the Paper_ED_Cos_01 §3.8 M3-chain template (substrate-side Noether → DCGT → standard-physics inheritance) to **time-varying** $\Psi$ source states, generalizing the Paper_ED_Dyn_02 application (non-uniform stationary states) to non-stationary states.
5. It does **not** claim the audit-acceptance level of the saturation-regime M3 chain itself. Per Memo_ED_RadiationLaw_NoetherFlux_Audit, the closure leans on **standard-EM/GR-analog inheritance** for source-class identification (accelerated chain = standard accelerated charge; time-varying multipole = standard mass-quadrupole) and for the specific stress-energy flux form (Poynting-class for EM; quadrupole-flux for GW). Three explicit qualifications (Q1, Q2, Q3) carried in §3.5 and §4 audit rows.
6. It does **not** address radiation at near-Planck-scale frequencies ($\omega \to c/\ell_{V_1}$). DCGT applies cleanly for radiation at standard physical frequencies (radio through gamma); near-substrate-scale frequencies are at edge of DCGT validity (regime restriction Q3).

---

## Abstract

Electromagnetic and gravitational radiation in ED arise by applying the M3 substrate-graph chain (Paper_ED_Cos_01 §3.8; Paper_ED_Dyn_02 non-stationary extension) to **time-varying** $\Psi$ source states. Two source classes admit substrate-graph identification: **accelerated chains** with gauge-bundle coupling (Paper_015 T17 + V1 propagation-direction change between commitment events), which produce substrate-side EM-analog radiation, and **time-varying mass-quadrupole sources** ($\Psi$-distributions with time-dependent spatial second-moments, per Paper_ED_GW_00 saddle-Hessian framework), which produce substrate-side GW radiation. Substrate-side Noether procedure on $\mathcal{L}_{\mathrm{sub}}$ for time-varying $\Psi$ yields non-trivial flux components $T^{0i}_{\mathrm{sub}}$; DCGT (Paper_073) coarse-grains to continuum stress-energy flux preserving the flux structure within its hydrodynamic-window scale-separation; standard Maxwell and linearized Einstein retarded-Green's-function machinery inherit; **EM Larmor formula** $P_{\mathrm{EM}} = q^2 a^2 / (6\pi\epsilon_0 c^3)$ and **GW quadrupole formula** $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ recover. Substrate-c bound preserved throughout. **Verdict per Paper_095: M3 (form-IDENTIFIED + value-INHERITED).** Closure is **structurally weaker than Cos_01's saturation chain** — source-class identification and stress-energy flux form choice are INHERITED by standard-EM/GR analog rather than substrate-graph-derived; qualifications match the Paper_ED_Dyn_02 non-saturation pattern. **F1 (sharpest):** detection of monopole gravitational radiation or scalar/longitudinal EM radiation modes at substrate-graph level — refutes the substrate composition (which inherits standard polarization-mode selection rules via Paper_015 T17 + Paper_ED_GW_00 + Paper_109 + Paper_116). Inherited consequences: standard EM Larmor + GW quadrupole at observational accuracy across all standard physical frequencies. **Cross-arc closure:** Paper_ED_GW_00 audit row 12 closes retroactively (see §3.4 + §5.4).

---

## §1 Statement of Result

The substrate-graph radiation law is the application of the Paper_ED_Cos_01 §3.8 + Paper_ED_Dyn_02 §3 M3-chain template to **time-varying** $\Psi$ source states. Two source classes:

**EM Larmor analog (accelerated gauge-coupled chain):**

- Substrate-side: chain $C$ with V1-propagation direction that changes between commitment events (the substrate-graph analog of acceleration), carrying gauge-bundle content per Paper_015 T17.
- Substrate-side Noether flux $T^{0i}_{\mathrm{sub}}$ scales as the substrate-side analog of the Poynting vector.
- DCGT translates to continuum EM radiation; Maxwell retarded machinery + standard EM theory inherits.
- $$P_{\mathrm{EM}} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3}$$ with $q$ via Paper_015 T17 (gauge-bundle charge), $a$ as substrate-side chain acceleration, $c$ as substrate-c (Paper_012), and $\epsilon_0$ INHERITED.

**GW quadrupole analog (time-varying mass-quadrupole source):**

- Substrate-side: $\Psi$-distribution with time-varying spatial second-moment $Q_{ij}^{\mathrm{sub}}(\ell, t) = \int (\Psi\text{ density})(x_i x_j - \tfrac{1}{3}\delta_{ij}|x|^2) d^3x$, with non-trivial $\dddot Q_{ij}$.
- Substrate-side Noether flux $T^{0i}_{\mathrm{sub}}$ scales with $|\dddot Q_{ij}|^2$ at appropriate retardation.
- DCGT translates to continuum stress-energy flux; linearized Einstein retarded machinery inherits.
- $$P_{\mathrm{GW}} = \frac{G}{5c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$$ with $G$ via Paper_027 (substrate-side dimensional rearrangement) and $c$ via Paper_012.

**FORM:** substrate-side Noether for time-varying $\Psi$ + DCGT translation + standard-physics retarded-Green's-function inheritance — **IDENTIFIED via the M3-chain template extended to non-stationary sources**. Zero pure-D rows; composition + identification, not new substrate-graph derivation.

**VALUE:** numerical coefficients ($1/(6\pi\epsilon_0 c^3)$ for Larmor; $1/(5c^5)$ for quadrupole) INHERITED at standard-physics-analog level via Paper_015 T17 and Paper_027 + standard radiation theory; substrate-graph derivation of coefficients OPEN substrate-research-frontier.

**Verdict: M3 (form-IDENTIFIED + value-INHERITED) per §4 audit table** — same tier as Paper_ED_Cos_01, Paper_ED_Dyn_02, Paper_ED_GW_00; audit-acceptance qualifications match the Paper_ED_Dyn_02 non-saturation pattern (standard-physics-analog inheritance for source-class identification and flux form choice).

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02 (participation), P03 (translation invariance, source of Noether), P04 (bandwidth), P09 (polarity), P10 (multiple rule-types), P11 (commitment / time arrow), P12 (ED-threshold), P13 (translation arrow).

**Upstream:**
- Paper_012 (substrate-c bound, P-RB-1) — supplies $c$ in radiation formulas
- Paper_015 / T17 (gauge fields) — supplies substrate-side gauge-bundle charge $q$ for EM analog
- Paper_027 (Newton's $G$ via dimensional rearrangement) — supplies $G$ for GW quadrupole
- Paper_032 (weak-field 1/r dilution) — supplies amplitude falloff
- Paper_073 (DCGT hydrodynamic-window coarse-graining)
- Paper_089 (V1 retarded kernel + T18 forward-causal) — substrate-side retarded Green's function analog
- Paper_093 (T18 kernel-arrow) — substrate-graph V1-propagation direction
- Paper_109 (Lorentz reps) — supplies polarization-mode count
- Paper_116 (massless-slot two-mode) — supplies GW polarization count
- Paper_ED_SC_4_9 ($S_{\mathrm{sub}}$ functional + saddle Hessian classification) — substrate-side multipole + saddle content
- Paper_ED_Cos_01 (saturation-regime M3-chain template)
- Paper_ED_Dyn_02 (non-saturation extension of M3-chain template) — this paper's direct precursor
- Paper_ED_GW_00 (GW = propagating saddle-Hessian reconfiguration; row 12 target)
- Standard Maxwell + linearized Einstein retarded-Green's-function machinery (textbook inheritance, INHERITED)

**No paper-specific postulates; no new substrate primitives.** Composition under the M3-chain template applied to time-varying source states.

---

## §3 Derivation

### 3.1 Source-class identification: accelerated chain (EM analog)

Per Paper_089 + Paper_093 T18, each chain $C$ has a V1-mediated propagation direction at each commitment event $e_n$ (the chain-arrow direction). Per Paper_012 P-RB-1, propagation is bounded by substrate-c.

**Substrate-side acceleration:** when the chain-arrow direction changes between consecutive commitments ($\sigma_C(e_n) \neq \sigma_C(e_{n+1})$), the chain undergoes substrate-graph acceleration — the substrate-side analog of a charged particle's worldline curving.

Per Paper_015 T17, chains with rule-type gauge-bundle coupling carry the substrate-side analog of EM charge. An accelerating gauge-coupled chain has time-varying gauge-bundle content → substrate-side EM radiation source.

**Identification status:** the specific mapping *"V1-propagation-direction change = EM-class acceleration"* is INHERITED by standard EM analog applied to the corpus's substrate-graph content (chain-arrow direction + T17 gauge bundles). See §3.5 audit qualification Q1.

### 3.2 Source-class identification: time-varying mass-quadrupole (GW analog)

Per Paper_ED_GW_00 §3.1 + Paper_ED_SC_4_9, time-varying saddle-Hessian content is the substrate-side mechanism for GW emission. A spatial $\Psi$-distribution with time-varying spatial second-moment

$$
Q_{ij}^{\mathrm{sub}}(\ell, t) = \int (\Psi\text{ density})(x_i x_j - \tfrac{1}{3}\delta_{ij}|x|^2) \, d^3x
$$

has time-varying saddle-Hessian content at the source locus. Non-trivial $\dddot Q_{ij}$ → substrate-side GW radiation.

**Identification status:** the specific mapping *"time-varying $\Psi$ second-moment = mass-quadrupole analogous to standard GR"* is INHERITED by standard GR analog applied to Paper_ED_SC_4_9 saddle content. Audit qualification Q1 (shared with §3.1).

### 3.3 Substrate-side Noether flux for time-varying $\Psi$

Applying the M3 chain Step B (per Memo_ED_DCGT_VacuumEnergyMapping §3 template), substrate-side Noether stress-energy from $S_{\mathrm{sub}}[\Psi]$ under P03 + P13 translation invariance:

$$
T^{\mu\nu}_{\mathrm{sub}} = \sum_{K \in \{V_1, V_5\}} \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K \Psi)} \nabla^\nu_K \Psi - g^{\mu\nu} \mathcal{L}_{\mathrm{sub}}.
$$

For time-varying $\Psi$, the **flux components**

$$
T^{0i}_{\mathrm{sub}} = \sum_K \frac{\partial \mathcal{L}_{\mathrm{sub}}}{\partial(\nabla_K^0 \Psi)} \nabla_K^i \Psi
$$

are non-trivial — substrate-side energy transport in the $i$-direction.

**Specific flux structures inherited by standard analog:**
- **EM-coupled accelerated chain:** $T^{0i}_{\mathrm{sub}}|_{\mathrm{EM}} \sim$ (substrate analog of $\vec E \times \vec B$)$^i$ — Poynting-vector-class structure. Standard EM gauge-invariant Lagrangian analog supplies the form.
- **Time-varying mass-quadrupole:** $T^{0i}_{\mathrm{sub}}|_{\mathrm{GW}}$ scales with $|\dddot Q_{ij}|^2$ at appropriate retardation. Standard linearized-GR analog supplies the form.

**Identification status:** the specific flux forms (Poynting-class for EM; quadrupole-flux for GW) are INHERITED by standard-QFT-analog choices applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$. Substrate-side V1 + V5 kernel structure plausibly supports both via Paper_015 T17 + Paper_109 + Paper_116 but explicit substrate-graph construction is OPEN substrate-research-frontier. See §3.5 audit qualification Q2.

### 3.4 DCGT translation + Maxwell / linearized Einstein retarded-Green's-function inheritance

Per Paper_073, DCGT coarse-grains within $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. **Radiation is the hydrodynamic-flux phenomenon DCGT was specifically built to handle** — standard hydrodynamics-from-microscopics (BBGKY, Chapman-Enskog) preserves energy-momentum conservation and continuum flux structure under coarse-graining. DCGT translation is structurally cleaner than for the saturation regime (Cos_01) or chain-class identification (Dyn_02).

**V1 / continuum retarded Green's function consistency:** V1's finite-width retarded support reduces to standard continuum $G^{\mathrm{ret}} = \delta(t - t' - |x-x'|/c)/(4\pi|x-x'|)$ at coarse-graining scales $R_{\mathrm{cg}} \gg \ell_{V_1}$. For standard radiation frequencies ($\omega \ll c/\ell_{V_1}$), V1 is effectively delta-function-supported at the coarse-graining scale.

**Standard machinery inherits:** Maxwell retarded potentials + multipole expansion give the EM Larmor formula; linearized Einstein retarded-Green's-function + transverse-traceless multipole expansion give the GW quadrupole formula. These are textbook standard radiation theory; substrate-side stress-energy flux supplies the source.

**Power radiated:**

$$
P_{\mathrm{EM}} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3}, \qquad
P_{\mathrm{GW}} = \frac{G}{5 c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle.
$$

$1/r$ amplitude falloff inherits from Paper_032 + V1 spherical dilution. Polarization content (two transverse EM modes; two transverse GW modes $h_+, h_\times$) inherits from Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7.

**This chain closes Paper_ED_GW_00 audit row 12** (substrate-graph derivation of source-amplitude formula) retroactively, via the M3-template applied to time-varying mass-quadrupole sources. See Paper_ED_GW_00 §3.9 (added 2026-05-16) and Update_Paper_ED_GW_00_Row12 memo for the corpus-side propagation.

### 3.5 Closure qualifications (per audit ACCEPTED at approximately-standard-physics level)

Per Memo_ED_RadiationLaw_NoetherFlux_Audit (ACCEPTED with three explicit qualifications):

- **Q1 (source-class identification):** the substrate-graph criterion identifying "accelerated chain" (EM-class) and "time-varying multipole" (GW-class) is INHERITED by standard-EM/GR analog. Substrate has supporting content (Paper_015 T17 gauge bundles; Paper_089 chain-arrow direction; Paper_ED_SC_4_9 saddle-Hessian content); explicit substrate-graph mapping not constructed. Same pattern as Paper_ED_Dyn_02 Q1.
- **Q2 (stress-energy flux form choice):** specific flux forms (Poynting-class for EM; quadrupole-flux for GW) inherit standard-QFT-analog choices applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$. Substrate-side V1 + V5 kernel structure plausibly supports both but explicit substrate-graph construction is OPEN. Same pattern as Paper_ED_Dyn_02 Q2.
- **Q3 (DCGT regime restriction):** DCGT applies cleanly for radiation at standard physical frequencies ($\omega \ll c/\ell_{V_1}$); near-Planck-scale frequencies are at edge of DCGT validity. Not load-bearing for standard radiation phenomenology.

The closure is **structurally weaker than Cos_01's saturation chain** — which derived $w = -1$ directly from constant-$\Psi$ Noether without analog choices. Qualifications match the Paper_ED_Dyn_02 audit pattern. Closure remains within Paper_095 §2.3 D-via-I (composition under substrate identification + declared standard-physics inheritance).

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P04, P09, P10, P11, P12, P13 | **P** | Paper_087. P03 + P13 supply Noether translation invariance. |
| 2 | Upstream inheritance block | **I** | Paper_012 ($c$); Paper_015 / T17 (gauge $q$); Paper_027 ($G$); Paper_032 (1/r); Paper_073 (DCGT); Paper_089 (V1 + T18); Paper_093 (T18 kernel-arrow); Paper_109 (Lorentz reps); Paper_116 (massless-slot two-mode); Paper_ED_SC_4_9; Paper_ED_Cos_01 (saturation M3 template); Paper_ED_Dyn_02 (non-saturation template); Paper_ED_GW_00 (saddle-Hessian framework). |
| 3 | Standard Maxwell + linearized Einstein retarded-Green's machinery | **I** | Textbook inheritance; no substrate-graph derivation claimed. |
| 4 | Source-class identification: accelerated chain (EM-class) via V1-propagation-direction change between commitments + Paper_015 T17 gauge bundle | **D-via-I** | §3.1. **Audit qualification Q1:** specific mapping "V1-direction change = EM-class acceleration" is INHERITED by standard EM analog applied to substrate-graph content; explicit substrate-graph mapping not constructed. Same pattern as Paper_ED_Dyn_02 row 4. |
| 5 | Source-class identification: time-varying mass-quadrupole (GW-class) via time-varying $\Psi$ second-moment + Paper_ED_SC_4_9 saddle-Hessian | **D-via-I** | §3.2. **Audit qualification Q1 (shared):** specific mapping inherited by standard GR analog. |
| 6 | Substrate-side Noether flux $T^{0i}_{\mathrm{sub}}$ for time-varying $\Psi$ | **D-via-I** | §3.3. Composition of M3-chain Step B template (Memo_ED_DCGT_VacuumEnergyMapping) extended to time-varying $\Psi$. |
| 7 | Specific flux form: Poynting-class (EM) and quadrupole-flux (GW) | **D-via-I** | §3.3. **Audit qualification Q2:** specific flux forms inherit standard-QFT-analog choices applied to substrate-side $\mathcal{L}_{\mathrm{sub}}$; substrate-graph construction OPEN. Same pattern as Paper_ED_Dyn_02 row 5. |
| 8 | DCGT translation of substrate flux to continuum stress-energy flux | **D-via-I** | §3.4. Radiation is DCGT's natural regime; standard hydrodynamics-from-microscopics applies cleanly. **Audit qualification Q3:** near-Planck-scale frequencies at edge of DCGT validity; not load-bearing for standard radiation phenomenology. |
| 9 | V1 retarded → continuum $G^{\mathrm{ret}}$ at coarse-graining scale $R_{\mathrm{cg}} \gg \ell_{V_1}$ | **D-via-I** | §3.4. Standard radiation frequencies ($\omega \ll c/\ell_{V_1}$); V1 effectively delta-function-supported at coarse-graining scale. |
| 10 | EM Larmor formula $P_{\mathrm{EM}} = q^2 a^2 / (6\pi\epsilon_0 c^3)$ | **D-via-I** | §3.4. Composition: substrate-side flux (rows 6, 7) + DCGT (row 8) + Maxwell retarded machinery (row 3). $\epsilon_0$ INHERITED; $q$ via Paper_015 T17; $c$ via Paper_012. |
| 11 | GW quadrupole formula $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ | **D-via-I** | §3.4. Composition: substrate-side flux (rows 6, 7) + DCGT (row 8) + linearized Einstein retarded machinery (row 3). $G$ via Paper_027; $c$ via Paper_012. **Closes Paper_ED_GW_00 audit row 12 retroactively** (see Paper_ED_GW_00 §3.9 + Update_Paper_ED_GW_00_Row12). |
| 12 | $1/r$ amplitude falloff at large distance | **I** | §3.4. Paper_032 + V1 spherical dilution; standard inheritance. |
| 13 | Polarization content: two transverse EM modes; two transverse GW modes ($h_+, h_\times$); no scalar / vector / monopole / dipole gravitational radiation | **I** | §3.4. Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7; standard radiation selection rules via charge / mass-momentum conservation. |
| 14 | Substrate-graph derivation of numerical coefficients ($1/(6\pi\epsilon_0)$; $1/5$) from substrate parameters alone | **OPEN** | Substrate-research-frontier; not load-bearing for the radiation-law-as-form closure. Coefficients inherited at standard-physics-analog level. |
| 15 | Radiation at near-Planck-scale frequencies ($\omega \to c/\ell_{V_1}$) | **OPEN** | Beyond DCGT hydrodynamic-window; substrate-research-frontier; not load-bearing for standard radiation phenomenology. |
| 16 | Higher-multipole + radiation-reaction effects | **OPEN** | Standard physics inheritance extends via same M3-template; not load-bearing for the form closure. |
| 17 | Verdict M3 (form-IDENTIFIED + value-INHERITED) | **A→position** | Per Paper_095 §3.3 line 77. Five-anchor verdict-sync: status line / abstract / §1 / this row / §6 Position Statement all M3. |

**Audit summary:** zero pure-D rows; **eight substantive D-via-I rows** (4–11); five I rows (inheritance + textbook content); three OPEN rows (14, 15, 16 — none load-bearing for the M3 framing); one A→position verdict row. No paper-specific postulates; no new substrate primitives. **No load-bearing OPEN items.**

---

## §5 Falsification Criteria

- **F1 (sharpest):** Detection of monopole gravitational radiation, dipole gravitational radiation, or scalar/longitudinal EM radiation modes — substrate-side admitted modes are restricted by Paper_015 T17 + Paper_109 + Paper_116 + Paper_ED_GW_00 §3.7 to standard polarization content via standard charge / mass-momentum conservation. Refutes §3.4 polarization inheritance.

- **F2:** Observation of radiation power scaling violating Larmor ($P \propto q^2 a^2$) or quadrupole ($P \propto G \dddot Q^2$) forms at standard physical frequencies beyond standard observational uncertainty. Refutes §3.4 closure. (Currently consistent: pulsar binary inspiral power loss matches GW quadrupole within $\sim 0.1\%$; accelerated-charge radiation matches Larmor across all examined regimes.)

- **F3:** Refutation of DCGT hydrodynamic-window applicability at standard radiation frequencies (e.g., discovery of substrate-scale physics that interferes with coarse-graining below near-Planck-scale). Refutes §3.4 / Q3.

- **F4:** Demonstration that substrate-side V1 + V5 kernel structure cannot supply both Poynting-class (EM-analog) and quadrupole-flux (GW-analog) flux forms — refuting Q2 from below rather than above. Refutes §3.3 + §3.5 Q2.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

The ED radiation law is identified at substrate-graph level by applying the Paper_ED_Cos_01 §3.8 + Paper_ED_Dyn_02 §3 M3-chain template to **time-varying** $\Psi$ source states. Accelerated gauge-coupled chains (Paper_015 T17 + V1 chain-arrow direction change) supply the substrate-side EM-analog source; time-varying $\Psi$ second-moment distributions (Paper_ED_SC_4_9 saddle-Hessian framework) supply the substrate-side GW-analog source. Substrate-side Noether on $\mathcal{L}_{\mathrm{sub}}$ for time-varying $\Psi$ produces non-trivial flux components; DCGT — radiation being its natural regime — translates to continuum stress-energy flux; Maxwell and linearized Einstein retarded-Green's-function machinery inherit; EM Larmor $P = q^2 a^2/(6\pi\epsilon_0 c^3)$ and GW quadrupole $P = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ recover. The closure is **structurally weaker than Cos_01's saturation chain**: source-class identification (Q1) and stress-energy flux form choice (Q2) are INHERITED by standard-EM/GR analog rather than substrate-graph-derived; qualifications match the Paper_ED_Dyn_02 non-saturation pattern. The closure remains D-via-I per Paper_095 §2.3, with inheritance qualifications named explicitly in §3.5 and audit rows 4–8.

**Verdict: M3 (form-IDENTIFIED + value-INHERITED) per Paper_095.** Eight substantive D-via-I rows; zero pure-D rows; no paper-specific postulates; no new substrate primitives; **no load-bearing OPEN items**. Three non-load-bearing OPEN rows (substrate-graph derivation of numerical coefficients; near-Planck-scale-frequency radiation; higher-multipole and radiation-reaction extensions). **Cross-arc consequences:** (i) **Paper_ED_GW_00 audit row 12 closes retroactively** via §3.4 + audit row 11 — the quadrupole source-amplitude formula identification is established by this paper's chain; see Paper_ED_GW_00 §3.9 (added 2026-05-16). (ii) **Paper_ED_Dyn_05 (Inspiral dynamics; pending draft) becomes directly draftable** with this paper's GW radiation content as the energy-loss source term, completing the binary-inspiral substrate-graph chain. (iii) **Paper_ED_GW_01 (BH ringdown spectroscopy; pending draft) gains substantive substrate-side radiation-amplitude content** for quasinormal-mode spectroscopy. Together with Paper_ED_Dyn_02, this paper closes the load-bearing program's Dynamics-Arc derivations (3 closed + 1 negative + 1 conditional on Route A across the full five-item program).

---

**End Paper_ED_Dyn_03.**
