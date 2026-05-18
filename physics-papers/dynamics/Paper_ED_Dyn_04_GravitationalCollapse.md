# Paper_ED_Dyn_04 — Gravitational Collapse as Compression-Dominated Saddle-Signature Evolution

**Series:** Wave-3 Generative Papers (Dynamics Arc — direct M3 extension of Dyn_01 + Dyn_02 + GW_01)
**Status:** Verdict per Paper_095: **M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED)** within DCGT A→regime. Direct composition of Dyn_01 (S1 all-compression regime) + Dyn_02 (horizon-motion) + GW_00 (NoetherFlux chain) + GW_01 (ringdown) + Route A4 substrate-parameter inheritance; no new primitives or paper-specific postulates.
**Date:** 2026-05-17
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_089/090/093 (V1/V5/T18 kernels); Paper_012 (substrate-c); Paper_027 (Newton's $G$); Paper_ED_SC_4_9 (S1/S2/S3); Paper_ED_GW_00 (M3); Paper_ED_Dyn_01 (M3 — saddle dynamics, S1 regime); Paper_ED_Dyn_02 (M2 — horizon motion); Paper_ED_Dyn_03 (M2 — radiation law); Paper_ED_GW_01 (M3 — ringdown); Paper_ED_SC_4_1 (BH ↔ cosmic decoupling); Paper_095 (verdict grammar). Substrate-research support memos cross-referenced in §2.

**Label-class note (per Paper_095 §2.2, pending formal addition):** This paper uses two sub-labels of **I** introduced across the 2026-05 corpus push (Cos_05, Cos_06, Dyn_01, Dyn_04): **I (substrate-parameter-INHERITED)** = inheritance of a numerical value through substrate-parameter content (e.g., $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}}$, $\tau_{V_5}/\tau_P$) at the Paper_027-analog level; **IC-INHERITED** = inheritance of initial-condition / boundary-state content from an upstream substrate-state specification (framework-neutral per Memo_ED_CCC_Realizability_SubConstruct). A formal Paper_095 §2.2 update is the preferred corpus-wide grounding; the present in-paper note is the bridging definition.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a closed-proof derivation of standard general-relativistic collapse phenomenology from substrate primitives. Standard collapse machinery (Oppenheimer-Snyder dust collapse; Choptuik critical collapse; trapped-surface formation theorems; numerical-relativity collapse simulations) is **INHERITED** via DCGT continuum bridge. ED supplies the substrate-graph reading of *what* evolves and *what threshold* triggers horizon formation — not a substrate-graph rederivation of standard NR collapse machinery.
2. It does **not** sit within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). ED is in the substrate-ontology research program ('t Hooft cellular-automaton; Wolfram Ruliad; causal-set program, Sorkin et al.). Methodology per Paper_095 (form-FORCED / value-INHERITED).
3. It does **not** introduce new substrate primitives or paper-specific postulates. The collapse content is composition of Paper_ED_Dyn_01 (saddle dynamics; S1 all-compression regime) + Paper_ED_Dyn_02 (horizon-motion) + Paper_ED_GW_00 (NoetherFlux radiation chain) + Paper_ED_GW_01 (post-collapse ringdown) + Route A4 substrate-parameter-INHERITED scale.
4. It does **not** claim numerical-precision derivation of specific collapse-rate timescales, critical-collapse exponents (e.g., Choptuik's $\gamma \approx 0.374$ for scalar-field collapse), or post-collapse BH mass distribution. Specific numerical values are INHERITED from standard astrophysics + NR simulations; ED supplies the substrate-graph *mechanism* (compression-eigenvalue growth + horizon-signature crossing) without claiming substrate-graph rederivation of all numerical coefficients.
5. It does **not** address singularity resolution within the collapsed BH interior. ED's discrete substrate (Paper_087 + Paper_089) suggests substrate-scale physics modifies the singularity regime, but substrate-graph derivation of singularity-resolution mechanism is substrate-research-frontier (related to but distinct from Dyn_04 scope; see Paper_039 + Paper_047 for substrate-graph BH-interior context).
6. It does **not** address pre-collapse stellar-evolution physics (nuclear-burning timescales; stellar structure; explosion-vs-implosion thresholds). Pre-collapse substrate state is supplied as initial condition; substrate-graph framework supplies the collapse-phase dynamics only.
7. **Inheritance from Dyn_02 M2 status:** Dyn_04 supplies the *form* of collapse (monotonic compression-eigenvalue growth + horizon-signature-class-boundary crossing) independently of the underlying chain-class identifications driving each regime. Dyn_02's OPEN-HM-Q1 + OPEN-HM-Q2 (chain-class criterion + substrate-graph stress-energy form per regime) remain OPEN at Dyn_02's level; Dyn_04 does not load-bear on these closures because the saddle-dynamical *framework* is identified independently of which chain-class content drives each regime. This is the same architectural-division logic Dyn_01 uses (foundational framework vs application).

---

## Abstract

Gravitational collapse is identified at substrate-graph level as **the monotonic evolution of a substrate region's Hessian-signature toward all-compression (S1-class), crossing the horizon-formation threshold along a closed substrate-graph surface, and terminating in mixed-signature equilibrium via ringdown stabilization**. Three temporal regimes: pre-collapse (mixed or expansion-dominant Hessian) → collapse (monotonic compression-eigenvalue growth; horizon-formation threshold crossing) → post-collapse ringdown (GW_01). **Form-IDENTIFIED** via Dyn_01 (S1 all-compression regime) + Dyn_02 (horizon-motion) + GW_00 (NoetherFlux chain) + GW_01 (ringdown). **Value-INHERITED**: $\ell_{\mathrm{coll}} \sim r_{\mathrm{horizon}} = 2GM/c^2$ with $G$ via Paper_027; $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4 (Paper_027-analog). **IC-INHERITED** from progenitor substrate state (standard astrophysics + Dyn_02). Substrate-c bound preserved throughout (apparent infinite-redshift at horizon is signature-class boundary effect, not substrate-c violation). **Verdict per Paper_095: M3.** **F1 (sharpest):** horizon-formation timing inconsistent with substrate-graph all-compression-eigenvalue-crossing threshold beyond NR uncertainty refutes the composition. Enables Paper_ED_Dyn_05 (inspiral) and strengthens Paper_ED_GW_02 (stochastic background) + SCBU BH-horizon projection.

---

## §1 Statement of Result

Gravitational collapse is the substrate-graph **monotonic Hessian-signature evolution toward all-compression**: the substrate-action Hessian eigenvalues at a substrate region evolve from mixed-signature (or expansion-dominant) at pre-collapse to all-compression (S1-class per SC-4.9) within the BH interior, with horizon formation occurring at the closed substrate-graph surface where the Hessian signature crosses from mixed to all-compression.

**Three temporal regimes** (standard astrophysical collapse phenomenology, substrate-side reading):

| Regime | Substrate-graph content | Continuum-side phenomenology |
|---|---|---|
| Pre-collapse | Mixed-signature or expansion-dominant Hessian; non-saturation substrate state with standard matter content | Standard astrophysics: progenitor stellar / cluster matter configuration |
| Collapse | Monotonic growth of compression-dominant Hessian eigenvalues along radial axes; signature-class evolution toward S1; horizon-formation threshold crossing along closed substrate-graph surface | Standard NR collapse: increasing curvature; trapped-surface formation; horizon formation |
| Post-collapse ringdown | Newly-formed mixed-signature saddle at horizon equilibrates; perturbed Hessian-signature pattern relaxes per GW_01 framework | Standard post-collapse GW emission: QNM-spectrum ringdown signal |

**FORM:** collapse = monotonic compression-eigenvalue growth crossing horizon-formation threshold — **IDENTIFIED** via Dyn_01 + Dyn_02 + GW_01 composition. Zero pure-D rows.

**VALUE:** characteristic length $\ell_{\mathrm{coll}} \sim r_{\mathrm{horizon}} = 2GM/c^2$ inherits standard astrophysics with $G$ via Paper_027; substrate-parameter content $\tau_{V_5}$ and $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4 (Paper_027-analog).

**IC:** pre-collapse Hessian-signature configuration + $\Psi$-gradient structure inherited from progenitor substrate state (standard astrophysics + Dyn_02 horizon-motion framework supplies pre-collapse substrate content).

**Verdict: M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) within DCGT A→regime per §4 audit table.**

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02 (participation), P03 (translation invariance — Noether source), P09 (polarity), P10 (multiple rule-types — V1, V5 kernel structure), P11 (commitment / time arrow), P12 (ED-threshold + stability landscape — Hessian-signature relevance), P13 (translation arrow).

**Upstream papers:**
- Paper_012 (P-RB-1 substrate-c bound)
- Paper_027 (Newton's $G$ — substrate-parameter inheritance for $GM$ content)
- Paper_073 (DCGT hydrodynamic-window coarse-graining)
- Paper_089 (V1 retarded kernel + T18 forward-causal — supplies outward GW propagation during collapse)
- Paper_090 (V5 cross-chain finite-memory — sets damping rate during post-collapse stabilization)
- Paper_093 (T18 kernel-arrow direction)
- Paper_ED_SC_4_9 (saddle-geometry classification S1/S2/S3; **S1 all-compression class** corresponds to collapsing region; collapse = signature-class evolution toward S1)
- Paper_ED_GW_00 (GW propagation; row 12 partial form-closure via NoetherFlux chain — outward GW emission during collapse)
- Paper_ED_Dyn_01 (saddle dynamics — universal generator; supplies S1 all-compression regime as collapse-dynamical regime, §3.3 + §3.6)
- Paper_ED_Dyn_02 (horizon-motion law — supplies mixed-signature ↔ all-compression boundary as horizon framework)
- Paper_ED_Dyn_03 (radiation law — supplies quadrupole formula for collapse-phase GW emission)
- Paper_ED_GW_01 (ringdown spectroscopy — supplies post-collapse stabilization framework)
- Paper_ED_SC_4_1 (BH horizon ↔ cosmic decoupling — cross-arc identification at substrate-parameter level)
- Update_ED_SC_4x_Arc_M3 (six-projection arc-wide M3 upgrade post-Route-A; BH horizon projection)
- Standard NR collapse machinery (Oppenheimer-Snyder; Choptuik critical collapse; trapped-surface theorems; numerical-relativity simulations) — textbook inheritance via DCGT continuum bridge

**Substrate-research support:**
- Memo_ED_RouteA_MultiRouteConvergence_Audit (multi-route convergence option (ii) at substrate-parameter-INHERITED level)
- Memo_ED_Q1Q2_JointClosure_Construct (Q1A + Q2A construction-uniqueness; saturation context)
- Memo_ED_ChainClass_C3_Construct + Audit (saturation chain-class identification; non-saturation context inherits Dyn_02 M2 status)

**No new substrate primitives. No paper-specific postulates.**

---

## §3 Derivation

### §3.1 All-compression saddle signature (Dyn_01 S1 regime)

Per Paper_ED_Dyn_01 §3.3 + §1 table: a substrate locus with **all-eigenvalues-negative** Hessian signature ($\lambda_i < 0$ for all $i$) is in the S1-class all-compression regime — substrate-action concavity along all directions; local dynamics favor *collapse* along all axes. Per Paper_ED_Dyn_02 + Paper_ED_SC_4_9 saddle classification: this is the substrate-graph configuration of the *interior* of a BH, in contrast to the *exterior* mixed-signature configuration.

The transition from mixed-signature (exterior) to all-compression (interior) along a closed substrate-graph surface defines the BH **horizon** as the substrate-graph Hessian-signature boundary (Paper_ED_GW_00 §3.1: "the horizons are the dynamics"; Paper_ED_Dyn_02 §3.6).

### §3.2 Growth of compression eigenvalues during collapse

Gravitational collapse is the **monotonic evolution** of the substrate-action Hessian eigenvalues at a substrate region from initial mixed-signature or expansion-dominant configuration toward all-compression. As progenitor matter content concentrates into a smaller substrate-graph region (standard astrophysical contraction), the local substrate-action density rises; via Paper_ED_SC_4_9 + Paper_087 P12 (stability landscape), the Hessian eigenvalue spectrum evolves: expansion-dominant axes turn into mixed-signature, then mixed-signature axes turn into compression-dominant, monotonically.

The substrate-graph mechanism for this monotonic evolution: V1 retarded propagation (Paper_089) of substrate content inward + V5 cross-chain cumulative-strain accumulation (Paper_090) at the contracting region. Both kernels drive substrate-action density upward; per the substrate-action functional structure (Paper_ED_SC_4_9), this pushes Hessian eigenvalues toward more-negative values along radial axes.

This is the substrate-graph analog of standard GR's "increasing curvature" during collapse — same monotonic-evolution structure, different ontological reading (Hessian-eigenvalue evolution vs spacetime-curvature increase). Note on the monotonicity claim itself: at the level invoked here, monotonicity inherits from standard NR collapse phenomenology via the DCGT continuum bridge; a substrate-graph monotonicity proof (deriving monotonic Hessian-eigenvalue evolution directly from V1-inward + V5-cumulative-strain kernel structure without inheritance from NR phenomenology) is not constructed in this paper. Consistent with Preamble item 1.

### §3.3 Horizon-formation threshold (Dyn_02)

The horizon-formation threshold is the substrate-graph **signature-class boundary crossing**: at the moment a closed substrate-graph surface encloses an all-compression interior region, a horizon exists at that surface. The substrate-graph criterion for horizon formation:

$$
\exists \text{ closed substrate-graph surface } \Sigma : \forall \ell \in \mathrm{Int}(\Sigma), \quad \mathrm{sign}(\lambda_1, \ldots, \lambda_d) = (-, -, \ldots, -)
$$

with mixed signature on $\Sigma$ itself (the horizon surface) and exterior (outside $\Sigma$). Per Paper_ED_Dyn_02 §3.6: this signature-class boundary is the substrate-graph analog of the standard GR trapped-surface formation criterion; the standard astrophysical compactness condition $r \sim 2GM/c^2$ inherits.

The horizon-formation timing for given progenitor mass/configuration inherits from standard NR collapse simulations + Paper_027 substrate-parameter content for $G$.

### §3.4 Collapse kinematics from Hessian evolution

The dynamical evolution of the substrate-graph configuration during collapse — the substrate-graph analog of "free-fall time", "Hubble-time", and similar standard GR collapse timescales — is set by the rate at which compression eigenvalues grow. Per Paper_ED_Dyn_01 §3.4: characteristic timescale $\tau_{\mathrm{coll}} \sim 1/\sqrt{|\lambda_{\mathrm{compression}}|}$, where $\lambda_{\mathrm{compression}}$ is the magnitude of the dominant compression-eigenvalue.

At horizon formation, $\lambda_{\mathrm{compression}}$ has reached the substrate-graph scale corresponding to $r_{\mathrm{horizon}} = 2GM/c^2$. Substrate-c bound (Paper_012 P-RB-1 + Paper_089) is preserved throughout: V1 retarded propagation operates within substrate-c during all collapse phases; the apparent "infinite-redshift" at horizon formation is the substrate-graph signature-class boundary effect, not a substrate-c violation.

DCGT (Paper_073) translates the substrate-graph dynamical evolution to continuum-side metric-collapse phenomenology at leading order in $\varepsilon = \ell_{\mathrm{ED}}/R_{\mathrm{cg}}$; at near-horizon scales the standard astrophysical collapse phenomenology inherits cleanly.

### §3.5 Energy flux and NoetherFlux inheritance (GW_00)

During collapse, time-varying substrate configuration generates outward GW emission per Paper_ED_GW_00's NoetherFlux substrate-graph chain (row 12 partial form-closure; §3.9): substrate-side Noether flux $T^{0i}_{\mathrm{sub}}$ from time-varying $\Psi$ → DCGT translation → continuum GW radiation with $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$. For collapse specifically, the time-varying mass-quadrupole $Q_{ij}^{\mathrm{sub}}(\ell, t)$ during the contraction phase produces GW emission characteristic of stellar / core-collapse supernova GW signals.

For aspherical collapse (which is the generic case in astrophysical core-collapse), substantial GW emission is predicted; for perfectly spherically-symmetric collapse, no GW emission (consistent with standard Birkhoff theorem). Substrate-graph framework reproduces this standard astrophysical structure via composition of GW_00 + Dyn_03 quadrupole-formula + standard astrophysics inheritance.

### §3.6 Post-collapse stabilization via ringdown (GW_01)

Upon horizon formation, the newly-formed mixed-signature saddle at the horizon is **not** at equilibrium — the just-formed BH carries residual Hessian-signature perturbations from the collapse-phase time-varying configuration. These residual perturbations decay to equilibrium via the GW_01 ringdown framework: complex eigenfrequencies $\omega_n = \omega_R^{(n)} + i\omega_I^{(n)}$ corresponding to substrate-graph Hessian eigenmodes near the horizon; outward GW radiation carrying the decaying signature reconfiguration via GW_00's NoetherFlux chain.

The post-collapse ringdown is structurally identical to BH-BH merger ringdown — same GW_01 framework; same QNM-spectrum phenomenology; same substrate-graph mechanism. The distinguishing feature for collapse-formed BHs (vs merger-formed BHs) is the *spectrum of initial perturbations*: collapse-formed BHs typically have lower-amplitude perturbations + different mode-content distribution than merger-formed BHs (standard astrophysics inheritance for the initial-perturbation amplitudes).

### §3.7 Value inheritance from Route A

Per Paper_ED_Dyn_01 §3.4 + Memo_ED_RouteA_MultiRouteConvergence_Audit option (ii): substrate-parameter-INHERITED scale is $\ell_{\mathrm{saddle}} \sim \ell_P (\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}})^{-1/2}$ at saturation; in kernel-dominated IR regime reduces to $\ell_{V_5} = c\tau_{V_5}$. For collapse specifically, the relevant scale is $r_{\mathrm{horizon}} = 2GM/c^2$, composed with substrate-parameter content $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at near-horizon Hessian-eigenvalue scale (Paper_027-analog).

The substrate-parameter content sets the rate at which compression-eigenvalue growth proceeds (via V5 cross-chain coupling strength + V1 propagation timescale), but the *form* of the collapse-kinematics is inherited from the saddle-dynamical framework (Dyn_01). Substrate-parameter values $\tau_{V_5}/\tau_P \approx 10^{61}$ + $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ inherited at primitive level; tightening via RA-OPEN-4a/4b/4c-explicit is substrate-research-frontier, not blocking.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P09, P10, P11, P12, P13 | **P** | Paper_087. P03 + P13 supply Noether translation invariance; P12 supplies Hessian-signature relevance. |
| 2 | Upstream inheritance block | **I** | Paper_012; Paper_027; Paper_073; Paper_089; Paper_090; Paper_093; Paper_ED_SC_4_9; Paper_ED_GW_00; Paper_ED_Dyn_01; Paper_ED_Dyn_02; Paper_ED_Dyn_03; Paper_ED_GW_01; Paper_ED_SC_4_1; Update_ED_SC_4x_Arc_M3. |
| 3 | Standard NR collapse machinery (Oppenheimer-Snyder; Choptuik; trapped-surface theorems) | **I** | Textbook inheritance via DCGT continuum bridge; no substrate-graph rederivation. |
| 4 | All-compression (S1-class) saddle signature = BH-interior substrate-graph configuration | **D-via-I** | §3.1. Composition of Dyn_01 §3.3 + SC-4.9 S1 + Dyn_02 mixed↔all-compression boundary. |
| 5 | Mixed-signature ↔ all-compression boundary along closed substrate-graph surface = horizon | **D-via-I** | §3.1, §3.3. Inherits Dyn_02 §3.6 + GW_00 §3.1 "horizons are the dynamics." |
| 6 | Monotonic compression-eigenvalue growth during collapse via V1 inward propagation + V5 cumulative strain | **D-via-I** | §3.2. Composition of Paper_089 + Paper_090 + SC-4.9 substrate-action functional structure. |
| 7 | Horizon-formation threshold = closed-surface signature-class boundary crossing | **D-via-I** | §3.3. Row 5 + standard NR trapped-surface inheritance via DCGT. |
| 8 | Collapse-timescale $\tau_{\mathrm{coll}} \sim 1/\sqrt{|\lambda_{\mathrm{compression}}|}$ | **D-via-I** | §3.4. Inherits Dyn_01 §3.4 characteristic-timescale identification. |
| 9 | Substrate-c bound preserved throughout collapse (infinite-redshift at horizon is signature-class boundary effect, not substrate-c violation) | **D-via-I** | §3.4. Paper_012 + Paper_089 + Paper_093. |
| 10 | DCGT translation to continuum metric-collapse phenomenology at near-horizon scales | **D-via-I** | §3.4. Paper_073 hydrodynamic-window. |
| 11 | Outward GW emission from time-varying $Q_{ij}^{\mathrm{sub}}$ during aspherical collapse | **D-via-I** | §3.5. Composition of GW_00 §3.9 NoetherFlux chain + Dyn_03 quadrupole. |
| 12 | Spherically-symmetric collapse → no GW emission (Birkhoff-analog) | **I** | §3.5. Standard astrophysics + Dyn_03 multipole-selection inheritance. |
| 13 | Post-collapse residual Hessian-signature perturbations decay via GW_01 ringdown | **D-via-I** | §3.6. Inherits GW_01 framework verbatim. |
| 14 | Post-collapse ringdown = GW_01 structurally; distinguishing feature = initial-perturbation spectrum from collapse vs merger | **D-via-I** | §3.6. GW_01 + standard astrophysics for initial-perturbation distribution. |
| 15 | Characteristic length $\ell_{\mathrm{coll}} \sim r_{\mathrm{horizon}} = 2GM/c^2$ | **I** | §3.7. Standard astrophysics + Paper_027. |
| 16 | $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at Route A4 substrate-parameter-INHERITED level | **I** | Sub-type per label-class note: *substrate-parameter-INHERITED*. §3.7. Memo_RouteA_MultiRouteConvergence_Audit option (ii); Paper_027-analog tier. |
| 17 | Pre-collapse Hessian-signature configuration (IC) inherited from progenitor substrate state + standard astrophysics + Dyn_02 horizon-motion framework | **I** | Sub-type per label-class note: *IC-INHERITED*. §1 table + §2.IC. Standard astrophysics supplies progenitor matter; substrate-graph framework supplies pre-collapse Hessian content. |
| 18 | Verdict M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) within DCGT A→regime | **A→position** | Per Paper_095 §3.3 line 77. Five-anchor verdict-sync: status / abstract / §1 / this row / §6 all M3. |

**Audit summary:** zero pure-D rows; **nine substantive D-via-I rows** (4–11, 13, 14); four I rows (2, 3, 12, 15); one substrate-parameter-INHERITED row (16); one IC-INHERITED row (17); one P row (1); one A→position verdict row (18). **No load-bearing OPEN items.** All upstream OPEN content inherited at upstream status; Dyn_04 does not aggravate or depend on those OPENs for its M3 verdict.

---

## §5 Falsification Criteria

- **F1 (sharpest):** Observation of gravitational-collapse phenomenology with horizon-formation timing inconsistent with substrate-graph all-compression-eigenvalue-crossing threshold. Specifically: detection of horizon formation at substantially different compactness from substrate-graph prediction (which inherits $r_{\mathrm{horizon}} = 2GM/c^2$) beyond numerical-relativity uncertainty refutes §3.3 + audit row 7. Currently consistent: observed compact-object formation phenomenology matches standard NR-derived horizon-formation timing.

- **F2:** Detection of GW signals from gravitational-collapse events inconsistent with substrate-graph $P_{\mathrm{GW}} \propto |\dddot Q_{ij}|^2$ scaling — e.g., GW signal from aspherical collapse violating quadrupole-formula prediction beyond observational uncertainty. Refutes §3.5 + audit row 11.

- **F3:** Detection of post-collapse ringdown signal inconsistent with GW_01 framework — e.g., ringdown-mode structure for collapse-formed BHs differing systematically from GW_01-derived QNM spectrum beyond standard astrophysics + initial-perturbation uncertainty. Refutes §3.6 + audit rows 13–14.

- **F4 (empirical form):** Detection of stable astrophysical configurations exceeding the substrate-graph compression-eigenvalue-crossing threshold without horizon formation — i.e., observation of compact objects denser than $r = 2GM/c^2$ that do *not* form BH horizons. Refutes §3.2 + §3.3 + audit rows 6–7. Currently consistent: observed compact-object population obeys the standard BH compactness threshold; no super-compact non-BH detections.
- **F4 (structural form):** Substrate-graph proof that compression-eigenvalue monotonic growth is structurally impossible from any pre-collapse substrate state consistent with Paper_087 + SC-4.9 + standard matter content. Substrate-research-frontier; empirical refutation not currently available. Refutes §3.2 + audit row 6.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

Gravitational collapse in ED is the monotonic evolution of a substrate region's Hessian-signature toward all-compression (S1-class per Dyn_01), crossing the horizon-formation threshold along a closed substrate-graph signature-class boundary surface (per Dyn_02), with outward GW emission during the collapse phase via GW_00's NoetherFlux chain and post-collapse stabilization via GW_01 ringdown. Characteristic length $\ell_{\mathrm{coll}} \sim r_{\mathrm{horizon}} = 2GM/c^2$ inherits standard astrophysics; substrate-parameter content $\tau_{V_5}$ + $\Theta_{\mathrm{ED}}$ at substrate-parameter-INHERITED level via Route A4 (Paper_027-analog). Substrate-c bound preserved throughout; the apparent infinite-redshift at horizon formation is the substrate-graph signature-class boundary effect, not a substrate-c violation. Substrate-ontology distinguishing content vs standard GR: Hessian-eigenvalue monotonic evolution *replaces* spacetime-curvature increase as the collapse mechanism; signature-class boundary *replaces* trapped-surface as the horizon-formation criterion. No graviton, no metric perturbation, no spacetime-singularity assertion (substrate-graph singularity-resolution remains substrate-research-frontier per Paper_039 + Paper_047 context).

**Verdict: M3 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) within DCGT A→regime hydrodynamic-window** per Paper_095. Nine D-via-I rows; four I rows; one substrate-parameter-INHERITED row (Route A4); one IC-INHERITED row (progenitor substrate state); zero pure-D rows; no paper-specific postulates; no new substrate primitives; **no load-bearing OPEN items**. All upstream OPENs (including Dyn_02 OPEN-HM-Q1/Q2; see Preamble item 7) inherited at upstream status. Standard astrophysical collapse phenomenology (empirically supported by observed compact-object formation rates + GW170817-class NS-NS merger events) is structurally inherited; the substrate-ontology distinguishing framing is the genuine ED contribution.

**Cross-arc consequences.** Upstream, Dyn_04 inherits unchanged from Dyn_01 (M3), Dyn_02 (M2), Dyn_03 (M2), GW_00 (M3), GW_01 (M3), Paper_ED_SC_4_1 (strengthens via collapse mechanism), and the ED-SC 4.x arc-wide M3 picture. Downstream, Dyn_04 *enables* Paper_ED_Dyn_05 (Inspiral Dynamics) via composition with Dyn_03 + GW_01 (inspiral-to-merger-to-ringdown waveform framework); *strengthens* Paper_ED_GW_02 (Stochastic Background) by supplying the core-collapse-supernova emission component; *strengthens* GW_00 row 13 (full inspiral-merger-ringdown waveform OPEN) by supplying the post-inspiral content; and *strengthens* the SCBU BH-horizon projection by supplying the dynamical mechanism by which BH horizons form (not just exist at equilibrium). Whether each enabled/strengthened paper closes at M3 or M2 depends on its own substrate-graph chain and is not forecast here; Dyn_05 inherits Dyn_03's M2 status at minimum.

---

**End Paper_ED_Dyn_04.**
