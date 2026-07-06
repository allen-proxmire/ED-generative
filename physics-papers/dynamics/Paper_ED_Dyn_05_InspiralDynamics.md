# Paper_ED_Dyn_05 — Inspiral Dynamics as Two-Saddle Coupled Evolution with Radiation Reaction

**Series:** Wave-3 Generative Papers (Dynamics Arc — pre-merger component of the full inspiral → plunge → collapse → ringdown chain)
**Status:** Verdict per Paper_095: **M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic inspiral case; M3 saturation-case (asymptotic circular-orbit limit) via Dyn_01 + Dyn_04** within DCGT A→regime. Mixed-verdict-tier framing per Paper_095 §3.2.2 (base verdict + sub-case carve-out). Generic M2 inherits Paper_ED_Dyn_03's M2 status for the radiation-reaction step (Route C4 + Route C1 pending).
**Date:** 2026-05-17
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_089/090/093 (V1/V5/T18 kernels); Paper_012 (substrate-c); Paper_027 (Newton's $G$); Paper_032 (1/r dilution); Paper_ED_SC_4_9 (S1/S2/S3); Paper_ED_GW_00 (M3); Paper_ED_Dyn_01 (M3 — S2 regime); Paper_ED_Dyn_02 (M2); **Paper_ED_Dyn_03 (M2 — load-bearing for generic verdict)**; Paper_ED_Dyn_04 (M3); Paper_ED_GW_01 (M3); Paper_095 (verdict grammar — §3.2.1 sub-labels + §3.2.2 mixed-tier). Substrate-research support memos cross-referenced in §2.

**Label-class note:** Audit-row sub-labels *substrate-parameter-INHERITED* and *IC-INHERITED* per Paper_095 §3.2.1. Mixed-verdict-tier base + sub-case convention per Paper_095 §3.2.2.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim closed-proof derivation of standard general-relativistic Post-Newtonian (PN) inspiral expansion from substrate primitives. Standard PN machinery (Peters 1964 orbital decay; PN-expansion to arbitrary order; effective-one-body formalism; numerical-relativity inspiral simulations) is **INHERITED** via DCGT continuum bridge. ED supplies the substrate-graph reading of *what* evolves (two-saddle mixed-signature configuration) and *what drives the evolution* (radiation reaction via Dyn_03 quadrupole formula) — not a substrate-graph rederivation of standard PN machinery.
2. It does **not** sit within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). ED is in the substrate-ontology research program ('t Hooft cellular-automaton; Wolfram Ruliad; causal-set program, Sorkin et al.). Methodology per Paper_095 (form-FORCED / value-INHERITED).
3. It does **not** introduce new substrate primitives or paper-specific postulates. The inspiral content is composition of Paper_ED_Dyn_01 (S2 mixed-signature saddle regime) + Paper_ED_Dyn_03 (radiation-reaction quadrupole) + Paper_ED_Dyn_04 (collapse endpoint) + Paper_ED_GW_01 (post-merger ringdown) + Route A4 substrate-parameter-INHERITED scale.
4. It does **not** claim numerical-precision derivation of specific PN coefficients (e.g., $v^7$ tail terms; spin-orbit/spin-spin coupling beyond leading order). Specific numerical coefficients are INHERITED from standard PN-expansion machinery; ED supplies substrate-graph identification of *what physical content* the PN machinery encodes (two-saddle Hessian-coupling evolution) without claiming substrate-graph rederivation of all PN coefficients.
5. It does **not** address the plunge regime (the strong-field transition between inspiral and merger) at substrate-graph derivational level. The plunge is standard numerical-relativity territory; ED inherits NR phenomenology for the plunge phase and supplies the substrate-graph framework for what is happening (two saddle loci merging) without quantitative substrate-graph PN-style closure of the plunge dynamics.
6. **Verdict honestly M2**, not M3 (despite Dyn_04 / GW_01 / Dyn_01 all sitting at M3). The reason: Dyn_05 inherits **Paper_ED_Dyn_03's M2 status** for the radiation-reaction step. Dyn_03's load-bearing OPENs are Route C4 (source-class identification: time-varying mass-quadrupole) + Route C1 (substrate-graph parameter constructions). Dyn_05's radiation-reaction step uses Dyn_03's substrate-graph quadrupole-formula chain; the M2 status propagates. The saturation case of Dyn_05 (e.g., asymptotic late-inspiral circular-orbit limit) inherits Dyn_01 + Dyn_04 M3 status; generically the M2 verdict holds.

---

## Abstract

Compact-binary inspiral is identified at substrate-graph level as **the coupled evolution of two mixed-signature (S2-class) saddle loci with orbital separation $r$ shrinking monotonically due to substrate-graph quadrupole-formula radiation reaction** (Paper_ED_Dyn_03 chain). Each compact object is an S2-class saddle locus per Dyn_01 + GW_01; the binary is two such saddles coupled via V1 + V5 + DCGT-mediated gravity. Three temporal regimes: early inspiral (standard PN) → late inspiral (saddle-overlap; PN breakdown approached) → transition to plunge/collapse/ringdown (NR + Dyn_04 + GW_01). **Form-IDENTIFIED** via Dyn_01 + Dyn_03 + Dyn_04 + GW_01. **Value-INHERITED**: orbital evolution $\dot r \sim -GM/c^5 \cdot r^{-3}$ via Dyn_03 quadrupole + Peters 1964; $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4. **IC-INHERITED** from progenitor binary formation channel. Substrate-c bound preserved throughout. **Verdict per Paper_095: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic inspiral case**, inheriting Dyn_03's M2 status (Route C4 + Route C1 load-bearing OPEN); **M3 saturation-case** (asymptotic circular-orbit limit) via Dyn_01 + Dyn_04. **F1 (sharpest):** orbital decay rate deviating from Peters 1964 across the binary-pulsar + LIGO/Virgo catalog refutes the substrate-graph chain. Currently consistent: Hulse-Taylor (PSR B1913+16) at ~0.1% precision since 1974. **Completes the full inspiral → plunge → collapse → ringdown framework** (Dyn_05 + Dyn_04 + NR + GW_01), addressing Paper_ED_GW_00 row 13 at corpus level.

---

## §1 Statement of Result

Compact-binary inspiral is the substrate-graph **coupled evolution of two mixed-signature (S2-class per SC-4.9) saddle loci**, with orbital separation $r$ shrinking monotonically due to energy loss via substrate-graph quadrupole-formula radiation reaction (Paper_ED_Dyn_03 + GW_00 NoetherFlux chain).

**Three temporal regimes** (standard astrophysical inspiral phenomenology, substrate-side reading):

| Regime | Substrate-graph content | Continuum-side phenomenology |
|---|---|---|
| Early inspiral | Two well-separated mixed-signature saddles; slow Hessian-coupling evolution; small dE/dt; substrate-c-bound V1 propagation between saddles | Standard PN expansion at low order; quasi-circular orbit; weak chirp signal |
| Late inspiral | Saddle separation shrinks rapidly; Hessian-eigenvalue cross-saddle overlap grows; strong radiation reaction; PN expansion breakdown approached | Standard high-PN-order regime; ISCO approach; high-amplitude chirp signal |
| Transition (plunge → collapse → ringdown) | Saddle merging → collapse-threshold crossing (Dyn_04) → post-merger mixed-signature saddle relaxation (GW_01) | Standard NR plunge phase + post-merger QNM-spectrum ringdown |

**FORM:** inspiral = two-saddle coupled evolution with substrate-graph quadrupole radiation reaction — **IDENTIFIED** via Dyn_01 + Dyn_03 + Dyn_04 + GW_01 composition. Zero pure-D rows.

**VALUE:** orbital evolution rate $\dot r \sim -GM/c^5 \cdot r^{-3}$ inherits standard astrophysics + Peters 1964 + Paper_ED_Dyn_03 quadrupole formula; substrate-parameter content $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4. $r_{\mathrm{ISCO}} \sim 6GM/c^2$ for Schwarzschild-class BH-BH inheritance.

**IC:** binary system pre-inspiral configuration (separation, masses, spins, orbital eccentricity) inherited from progenitor formation channel (standard astrophysics — binary stellar evolution; dynamical capture; primordial-BH formation).

**Verdict: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic inspiral case; M3 saturation-case (asymptotic circular-orbit limit) via Dyn_01 + Dyn_04** within DCGT A→regime per §4 audit table. Mixed-verdict-tier per Paper_095 §3.2.2. Generic M2 inherits Paper_ED_Dyn_03 M2 status for radiation-reaction step; upgrade to M3 requires Dyn_03 M2 → M3 (Route C4 + C1 closures).

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02 (participation), P03 (translation invariance — Noether source for quadrupole-flux content), P09 (polarity), P10 (multiple rule-types — V1, V5 kernel structure), P11 (commitment / time arrow), P12 (stability landscape), P13 (translation arrow).

**Upstream papers:**
- Paper_012 (P-RB-1 substrate-c bound)
- Paper_027 (Newton's $G$)
- Paper_032 (weak-field 1/r dilution — GW amplitude falloff)
- Paper_073 (DCGT hydrodynamic-window coarse-graining)
- Paper_089 (V1 retarded kernel + T18 — supplies inter-saddle propagation + outward GW radiation)
- Paper_090 (V5 cross-chain finite-memory — supplies cross-saddle correlation content)
- Paper_093 (T18 kernel-arrow direction)
- Paper_ED_SC_4_9 (saddle classification S1/S2/S3; **S2 mixed-signature class** corresponds to each compact object's substrate-graph configuration)
- Paper_ED_GW_00 (GW propagation; row 12 partial form-closure via NoetherFlux chain — outward GW emission during inspiral)
- Paper_ED_Dyn_01 (saddle dynamics — universal generator; supplies S2 mixed-signature regime for each compact object)
- Paper_ED_Dyn_02 (horizon-motion law — supplies mixed-signature substrate dynamics framework)
- **Paper_ED_Dyn_03 (radiation law — supplies substrate-graph quadrupole formula for binary radiation reaction; M2 status propagates to Dyn_05)**
- Paper_ED_Dyn_04 (gravitational collapse — supplies merger endpoint as saddle-merging + collapse-threshold crossing)
- Paper_ED_GW_01 (ringdown spectroscopy — supplies post-merger stabilization framework)
- Update_ED_SC_4x_Arc_M3 (six-projection arc-wide M3 upgrade post-Route-A; BH horizon projection)
- Standard PN-expansion machinery (Peters 1964 orbital decay; PN expansion through arbitrary order; effective-one-body formalism; numerical-relativity inspiral simulations) — textbook inheritance via DCGT continuum bridge

**Substrate-research support:**
- Memo_ED_RouteA_MultiRouteConvergence_Audit (multi-route convergence option (ii); substrate-parameter-INHERITED level)
- Memo_ED_Q1Q2_JointClosure_Construct (Q1A + Q2A construction-uniqueness; saturation context)
- Memo_ED_ChainClass_C3_Construct + Audit (saturation chain-class identification)

**No new substrate primitives. No paper-specific postulates.**

---

## §3 Derivation

### §3.1 Two-saddle mixed-signature structure (Dyn_01 S2 regime)

Per Paper_ED_Dyn_01 §3.6 + Paper_ED_Dyn_02 + Paper_ED_GW_01 §3.1: each compact object (BH or NS) in a binary system is a substrate-graph mixed-signature (S2-class per SC-4.9) saddle locus. For a BH, the saddle locus is at the horizon; for an NS, the saddle locus is at the neutron-star surface (mixed-signature in a different parameter regime than BH but structurally analogous). The binary system at substrate-graph level is **two mixed-signature saddle loci** separated by orbital distance $r$, coupled via V1 retarded propagation + V5 cross-chain content + DCGT-mediated continuum gravity.

For each individual saddle, the Hessian eigenstructure is the BH/NS internal substrate-graph configuration (per Dyn_02 + GW_01 §3.1); for the *coupled* two-saddle system, the Hessian content extends to inter-saddle correlations encoded by V5 cross-chain coupling + V1 retarded propagation between the two loci.

### §3.2 Radiation-reaction from Dyn_03 quadrupole formula

The binary's time-varying mass-quadrupole $Q_{ij}^{\mathrm{sub}}(t)$ from the orbital motion of the two saddle loci generates outward GW emission per Paper_ED_Dyn_03's substrate-graph chain (quadrupole formula at M2; row 12 partial form-closure of GW_00 §3.9):

$$
P_{\mathrm{GW}} = \frac{G}{5c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle
$$

For a quasi-circular binary with masses $m_1, m_2$ and separation $r$, standard Peters 1964 gives $\dddot Q_{ij}^{\mathrm{circular}} \sim (G\mu M/r)^{3/2} \cdot r$ where $\mu = m_1 m_2/(m_1+m_2)$, leading to $P_{\mathrm{GW}} \sim (G^4/c^5) \cdot \mu^2 M^3/r^5$. ED's substrate-graph chain reproduces this Peters-formula scaling at M2 status (inherited from Dyn_03); the substrate-graph mechanism (substrate-side Noether flux for time-varying $\Psi$ + DCGT → linearized Einstein quadrupole) is supplied by Dyn_03's NoetherFlux chain.

The energy loss $dE/dt = -P_{\mathrm{GW}}$ drives the orbital evolution: the saddle separation $r$ shrinks monotonically until reaching the collapse threshold (Dyn_04 territory).

### §3.3 Inspiral timescale $\tau_{\mathrm{insp}} \sim E/(dE/dt)$

For a quasi-circular binary, total orbital energy $E \sim -G\mu M/(2r)$; energy loss rate $dE/dt = -P_{\mathrm{GW}} \sim -(G^4/c^5) \cdot \mu^2 M^3/r^5$. Inspiral timescale:

$$
\tau_{\mathrm{insp}} \sim \frac{|E|}{|dE/dt|} \sim \frac{c^5 r^4}{G^3 \mu M^2}.
$$

This is the standard Peters 1964 inspiral timescale — at early inspiral ($r \gg r_{\mathrm{ISCO}}$), $\tau_{\mathrm{insp}}$ is long (saddle separation shrinks slowly); at late inspiral ($r \to r_{\mathrm{ISCO}}$), $\tau_{\mathrm{insp}}$ is short (rapid shrinking). The substrate-graph framework inherits this scaling via the Dyn_03 quadrupole-formula chain; substrate-parameter content $G$ via Paper_027.

For BH-BH inspiral, $\tau_{\mathrm{insp}} \to 0$ as $r \to r_{\mathrm{ISCO}} \sim 6GM/c^2$ (Schwarzschild ISCO); standard NR inspiral simulations supply specific high-PN-order coefficients beyond the leading Peters-formula content.

### §3.4 Late-inspiral approach to collapse threshold (Dyn_04)

As the binary separation shrinks toward $r_{\mathrm{ISCO}}$, the two mixed-signature saddle loci begin to **overlap** at substrate-graph level — the Hessian eigenvalue spectrum at intermediate substrate-graph loci between the two saddles starts to show coupled-saddle structure. The Hessian-signature pattern between the two saddles begins to evolve from "two well-separated mixed-signature regions with intervening expansion-dominant region" toward "single mixed-signature region with internal substructure."

This is the substrate-graph reading of the late-inspiral PN-expansion breakdown: standard PN expansion treats each compact object as a quasi-point-source in a quasi-flat background; ED's substrate-graph framework treats each compact object as a mixed-signature saddle locus, and the late-inspiral regime is when the saddle loci begin to interact at substrate-graph level (not just gravitationally at continuum level).

When the saddle separation crosses the threshold at which compression-eigenvalue overlap initiates collapse (Dyn_04 §3.2 + §3.3), the inspiral transitions to plunge. The threshold crossing inherits Dyn_04's substrate-graph mechanism.

Note on the saddle-overlap mechanism itself: the substrate-graph identification of "two mixed-signature saddles begin to merge at late inspiral" inherits at the level that Dyn_02 (mixed-signature saddle framework) + Dyn_04 (compression-eigenvalue growth precursor) already establish. The *specific* substrate-graph derivation of the late-inspiral overlap rate (Hessian-eigenvalue cross-saddle correlation growth as a function of $r/r_{\mathrm{ISCO}}$) is not constructed here; the rate is inherited via DCGT continuum bridge from standard PN-breakdown phenomenology. Same Q1-class identification status as the Dyn_02 / Dyn_03 chain-class identifications; consistent with Preamble item 1.

### §3.5 Transition to plunge (NR domain)

The plunge regime — short, strongly-nonlinear transition between inspiral and ringdown — is **standard numerical-relativity territory**. ED's substrate-graph framework supplies the structural identification (two mixed-signature saddles merge to single highly-perturbed mixed-signature saddle; compression-eigenvalues grow per Dyn_04 §3.2; horizon-formation threshold crossing per Dyn_04 §3.3); NR supplies the quantitative waveform shape, peak strain, transition timing via DCGT continuum bridge inheritance.

### §3.6 Post-plunge stabilization → ringdown (GW_01)

Post-plunge merger-formed mixed-signature saddle carries residual Hessian-signature perturbations; these decay via GW_01 ringdown framework (complex eigenfrequencies from substrate-graph Hessian eigenstructure; outward GW radiation per GW_00 NoetherFlux). Full inspiral → plunge → ringdown at substrate-graph level: **Dyn_05 (M2) + NR (INHERITED) + GW_01 (M3) composition** — addresses Paper_ED_GW_00 row 13 at corpus level.

### §3.7 Value inheritance from Route A

Per Memo_ED_RouteA_MultiRouteConvergence_Audit option (ii): substrate-parameter-INHERITED scale via Route A4. Relevant inspiral scales: orbital $r$ (varies during inspiral); $r_{\mathrm{ISCO}} \sim 6GM/c^2$ at plunge; GW wavelength $\lambda_{\mathrm{GW}} \sim r$ during inspiral, $\sim r_{\mathrm{horizon}}$ during ringdown. All inherit standard astrophysics; substrate-parameter content $\tau_{V_5}/\tau_P \approx 10^{61}$ + $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ at Paper_027-analog primitive level. RA-OPEN-4a/4b/4c-explicit substrate-research-frontier; not blocking.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P09, P10, P11, P12, P13 | **P** | Paper_087. P03 + P13 supply Noether translation invariance. |
| 2 | Upstream inheritance block | **I** | Paper_012; Paper_027; Paper_032; Paper_073; Paper_089; Paper_090; Paper_093; Paper_ED_SC_4_9; Paper_ED_GW_00; Paper_ED_Dyn_01; Paper_ED_Dyn_02; **Paper_ED_Dyn_03 (M2; propagates to this paper)**; Paper_ED_Dyn_04; Paper_ED_GW_01; Update_ED_SC_4x_Arc_M3. |
| 3 | Standard PN-expansion machinery (Peters 1964; PN expansion; EOB formalism; NR inspiral simulations) | **I** | Textbook inheritance via DCGT continuum bridge. |
| 4 | Each compact object = mixed-signature (S2-class) saddle locus | **D-via-I** | §3.1. Dyn_01 §3.6 + Dyn_02 + GW_01 §3.1. |
| 5 | Binary system = two mixed-signature saddle loci coupled via V1 + V5 + DCGT-mediated gravity | **D-via-I** | §3.1. Composition of row 4 + Paper_089 + Paper_090 + Paper_073. |
| 6 | Time-varying mass-quadrupole $Q_{ij}^{\mathrm{sub}}(t)$ from orbital motion | **D-via-I (conditional)** | §3.2. Composition of row 5 + Paper_ED_Dyn_03 substrate-graph quadrupole-formula chain. **Conditional on Dyn_03 M2 chain-class identifications**. |
| 7 | $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$ radiation reaction at substrate-graph level | **D-via-I (conditional on Dyn_03 M2)** | §3.2. Inherits Paper_ED_Dyn_03 quadrupole formula + GW_00 §3.9 row 12 partial form-closure. **Load-bearing OPEN: Dyn_03 M2 status propagates — Route C4 source-class identification + Route C1 substrate-graph parameter constructions** pending. |
| 8 | Inspiral timescale $\tau_{\mathrm{insp}} \sim c^5 r^4/(G^3 \mu M^2)$ (Peters 1964 scaling) | **D-via-I (conditional on Dyn_03)** | §3.3. Composition of row 7 + standard astrophysics energy formula. |
| 9 | Saddle-separation shrinking + Hessian-eigenvalue cross-saddle overlap at late inspiral | **D-via-I** | §3.4. Composition of rows 4–6 + Dyn_04 §3.2 compression-eigenvalue growth precursor. |
| 10 | Collapse-threshold crossing at plunge transition | **D-via-I** | §3.4. Inherits Dyn_04 §3.3 horizon-formation threshold framework. |
| 11 | Plunge regime structural identification (saddle merging + compression-eigenvalue growth) | **D-via-I** | §3.5. Inherits Dyn_04 §3.2 + standard NR phenomenology for quantitative content. |
| 12 | Specific NR-derived plunge waveform shape, peak strain, transition timing | **I** | §3.5. Standard NR + DCGT continuum bridge. |
| 13 | Post-plunge ringdown via GW_01 framework | **D-via-I** | §3.6. Inherits GW_01 verbatim. |
| 14 | Full inspiral → plunge → ringdown waveform at substrate-graph level (composition Dyn_05 + NR + GW_01) | **D-via-I (conditional on Dyn_03)** | §3.6. Addresses GW_00 row 13 at corpus level. |
| 15 | Substrate-c bound preserved throughout inspiral (V1 propagation between saddles + outward GW emission) | **D-via-I** | §3.2, §3.3. Paper_012 + Paper_089 + Paper_093. |
| 16 | Characteristic length $\ell_{\mathrm{insp}}$ ranges from orbital $r$ to $r_{\mathrm{ISCO}} \sim 6GM/c^2$ | **I** | §3.7. Standard astrophysics + Paper_027. |
| 17 | $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at Route A4 substrate-parameter-INHERITED level | **I** | Sub-type per Paper_095 §3.2.1: *substrate-parameter-INHERITED*. §3.7. Memo_RouteA_MultiRouteConvergence_Audit option (ii); Paper_027-analog tier. |
| 18 | Pre-inspiral binary configuration (separation, masses, spins, eccentricity) inherited from progenitor formation channel | **I** | Sub-type per Paper_095 §3.2.1: *IC-INHERITED*. §1 + §2.IC. Standard astrophysics for binary stellar evolution + dynamical capture + primordial-BH formation. |
| 19 | Saturation case (asymptotic circular-orbit limit) closes at M3 via Dyn_01 + Dyn_04 chain | **D-via-I** | §1 + §3.4. Specific late-inspiral limit before plunge. |
| 20 | Verdict M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic case; M3 saturation-case via Dyn_01 + Dyn_04 inheritance | **A→position** | Per Paper_095 §3.3 + §3.2.1 (three-axis) + §3.2.2 (mixed-tier). Five-anchor verdict-sync: status / abstract / §1 / this row / §6 all carry base M2 with M3 saturation-case noted at each anchor. |

**Audit summary:** zero pure-D rows; **eleven substantive D-via-I rows** (4–11, 13–15, 19); three I rows (2, 3, 12, 16); one substrate-parameter-INHERITED row (17); one IC-INHERITED row (18); one P row (1); one A→position verdict row (20). **Load-bearing remaining OPEN: Paper_ED_Dyn_03 M2 status propagates** (Route C4 source-class identification + Route C1 substrate-graph parameter constructions). Upstream OPENs from other papers (SC-4.9 substrate-FORCED exhaustiveness; Route A tightening RA-OPENs) inherited at upstream status; not load-bearing for Dyn_05 specifically beyond Dyn_03 inheritance. No new substrate primitives; no paper-specific postulates.

---

## §5 Falsification Criteria

- **F1 (sharpest):** Observation of compact-binary inspiral timescale inconsistent with substrate-graph quadrupole-formula radiation reaction at significant precision. Specifically: orbital decay rate deviating from Peters 1964 $\tau_{\mathrm{insp}} \sim c^5 r^4/(G^3 \mu M^2)$ across the binary-pulsar + LIGO/Virgo BH-BH inspiral catalog beyond observational uncertainty refutes §3.2–§3.3 + audit rows 7–8. Currently consistent: Hulse-Taylor binary pulsar (PSR B1913+16) orbital decay matches GR quadrupole formula at ~0.1% precision since 1974; LIGO/Virgo BH-BH merger waveforms match PN expansion through inspiral phase.

- **F2:** Detection of substrate-graph two-saddle coupled-evolution phenomenology inconsistent with NR simulations — e.g., late-inspiral waveform shape or chirp evolution rate systematically deviating from substrate-graph mixed-signature saddle-merging prediction beyond NR-simulation precision. Refutes §3.4 + audit row 9.

- **F3:** Inconsistent transition to collapse threshold (Dyn_04) — e.g., observed plunge transition occurring at substantially different binary compactness from substrate-graph Hessian-signature crossing prediction. Refutes §3.4 + audit row 10. Currently consistent: observed BH-BH plunge transition matches standard NR-derived ISCO scaling.

- **F4:** Inconsistency with GW_01 ringdown endpoint — e.g., post-merger ringdown signal inconsistent with GW_01 framework when the merger formed from inspiral. Refutes §3.6 + audit row 13. Currently consistent: LIGO/Virgo BH-BH merger ringdown signals match standard QNM-spectrum predictions.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

Compact-binary inspiral in ED is two mixed-signature (S2-class) saddle loci coupled via V1 + V5 + DCGT-mediated gravity, with orbital separation shrinking monotonically due to substrate-graph quadrupole-formula radiation reaction (Paper_ED_Dyn_03 chain). Late inspiral carries the system toward the collapse threshold (Dyn_04); plunge inherits NR; post-merger ringdown per GW_01. Substrate-c bound preserved throughout; substrate-parameter content $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4.

**Verdict: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — generic inspiral case; M3 saturation-case (asymptotic circular-orbit limit) via Dyn_01 + Dyn_04** within DCGT A→regime, per Paper_095 §3.2.1 (three-axis) + §3.2.2 (mixed-tier). Eleven D-via-I rows (three conditional on Dyn_03 M2); zero pure-D rows; no paper-specific postulates; no new substrate primitives. **Load-bearing remaining OPEN: Paper_ED_Dyn_03 M2 status propagates** — Route C4 source-class identification + Route C1 substrate-graph parameter constructions load-bearing for upgrade to M3. **Completes the substrate-graph full-waveform framework** — Dyn_05 + NR + Dyn_04 + GW_01 composition addresses Paper_ED_GW_00 row 13 at corpus level. Substrate-ontology distinguishing content: two-saddle mixed-signature coupled evolution *replaces* two quasi-point-sources on quasi-flat background.

**Cross-arc consequences.** Upstream, Dyn_05 inherits unchanged from Dyn_01 (M3), Dyn_02 (M2), Dyn_03 (M2 — load-bearing), Dyn_04 (M3), GW_00 (M3), GW_01 (M3), Paper_ED_SC_4_1, and the ED-SC 4.x arc-wide M3 picture. Downstream, Dyn_05 *enables* GW_00 row 13 (full inspiral-merger-ringdown waveform; standing OPEN) at base verdict M2 via Dyn_05 + NR + Dyn_04 + GW_01 composition; *strengthens* Paper_ED_GW_02 (Stochastic Background) by supplying the inspiral-emission component (mixed-tier inheritance per Paper_095 §3.2.2: GW_02 inherits M2 via Dyn_05 inspiral content and M3 via GW_01 ringdown component); *strengthens* the Hulse-Taylor postdiction (PSR B1913+16 orbital decay matched at ~0.1% precision since 1974 via Dyn_03 + Dyn_05 chain) and the LIGO/Virgo/KAGRA BH-BH merger waveform-matching across the full inspiral → plunge → ringdown sequence. Verdict-tier of downstream papers depends on each paper's own substrate-graph chain.

---

**End Paper_ED_Dyn_05.**
