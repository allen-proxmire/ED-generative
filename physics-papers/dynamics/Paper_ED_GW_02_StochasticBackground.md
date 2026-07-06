# Paper_ED_GW_02 — Stochastic Gravitational-Wave Background as Cosmologically-Integrated NoetherFlux Output of Substrate-Graph Saddle Transitions

**Series:** Wave-3 Generative Papers (Gravitational-Wave Arc — cosmologically-integrated waveform background)
**Status:** Verdict per Paper_095: **M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — net base verdict via component-status composition (§3.2.3)**; inspiral component (dominant in LIGO/Virgo/PTA bands) inherits Dyn_05's M2 (→ Dyn_03 M2); merger+ringdown component M3 via Dyn_04 + GW_01; cosmological+collapse component M3 via Cos_01 + GW_00. Per-component breakdown in §1 table.
**Date:** 2026-05-17
**Anchors:** Paper_087 (13 primitives); Paper_073 (DCGT); Paper_089/090 (V1/V5 kernels); Paper_012 (substrate-c); Paper_027 (Newton's $G$); Paper_028 ($R_H = c/H_0$); Paper_032 (1/r dilution); Paper_ED_SC_4_9 (S1/S2/S3); Paper_ED_Cos_01 (M3); Paper_ED_Cos_05 (M3); Paper_ED_GW_00 (M3); Paper_ED_GW_01 (M3); Paper_ED_Dyn_01 (M3); Paper_ED_Dyn_02 (M2); **Paper_ED_Dyn_03 (M2 — propagates)**; Paper_ED_Dyn_04 (M3); **Paper_ED_Dyn_05 (M2 — load-bearing for net base verdict)**; Paper_095 (verdict grammar — §3.2.1 sub-labels + §3.2.2 mixed-tier + §3.2.3 component-status composition). Substrate-research support memos cross-referenced in §2.

**Label-class note:** Audit-row sub-labels *substrate-parameter-INHERITED* and *IC-INHERITED* per Paper_095 §3.2.1. Component-status composition per Paper_095 §3.2.3.

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim closed-proof derivation of $\Omega_{\mathrm{GW}}(f)$ stochastic-background spectrum from substrate primitives alone. Standard astrophysical population-synthesis machinery (compact-binary merger rates as a function of redshift; collapse-event rate distributions; standard cosmological backgrounds) is **INHERITED**; ED supplies the substrate-graph reading of the *per-event GW emission* (via Dyn_05 + Dyn_04 + GW_01 + GW_00) and the *cosmological-integration framework* (via Cos_01 + Cos_05) without claiming substrate-graph rederivation of the binary-population content.
2. It does **not** sit within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). ED is in the substrate-ontology research program. Methodology per Paper_095 (form-FORCED / value-INHERITED).
3. It does **not** introduce new substrate primitives or paper-specific postulates. The stochastic-background content is composition of GW_00 + GW_01 + Dyn_04 + Dyn_05 + Cos_01 + Cos_05 + Route A4 substrate-parameter-INHERITED scale + standard astrophysical population content.
4. It does **not** claim specific spectral predictions for individual sources beyond standard astrophysics. Compact-binary-inspiral $\Omega_{\mathrm{GW}}(f) \propto f^{2/3}$ scaling inherits standard Peters-formula + binary-population content; collapse-event contributions inherit standard supernova-GW phenomenology; cosmological inflation residual inherits standard inflationary GW spectrum predictions.
5. **Verdict honestly M2**, not M3 (despite GW_00 / GW_01 / Dyn_04 / Cos_01 / Cos_05 all sitting at M3). The reason: the compact-binary-inspiral component of $\Omega_{\mathrm{GW}}(f)$ — dominant in LIGO/Virgo/PTA observational bands — inherits Paper_ED_Dyn_05's M2 status (which itself inherits Paper_ED_Dyn_03 M2). Saturation cases (collapse-dominant frequency bands; ringdown-only contributions; cosmological-inflation residual primordial GW spectrum) inherit M3. The integrated background's M2 verdict is honest given the inspiral-component contribution dominates observable frequency bands.
6. It does **not** address detection / data-analysis methodology for stochastic-background searches (cross-correlation between detectors; Hellings-Downs correlation for PTA arrays; etc.). The data-analysis machinery is standard GW-astronomy inheritance via DCGT continuum bridge.

---

## Abstract

The stochastic GW background $\Omega_{\mathrm{GW}}(f)$ is identified at substrate-graph level as **the cosmologically-integrated NoetherFlux output of all mixed-signature saddle transitions across cosmic history** — compact-binary inspirals + plunge-merger + ringdown + stellar-collapse + cosmological-source contributions. Per-event GW emission inherits Dyn_05 + Dyn_04 + GW_01 + Cos_01; cosmological-history integration via Cos_01 + Cos_05 expansion framework; propagation via GW_00 NoetherFlux at substrate-c. **Three source-class components** (per-component verdicts per Paper_095 §3.2.3): (i) inspiral — M2 via Dyn_05 → Dyn_03; LIGO/Virgo/PTA bands; $\Omega_{\mathrm{GW}} \propto f^{2/3}$; (ii) merger + ringdown — M3 via Dyn_04 + GW_01; (iii) cosmological + collapse — M3 via Cos_01 + GW_00 + standard supernova rates. **Net base verdict per Paper_095: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED)** by component-status composition rule (inspiral component dominates LIGO/Virgo/PTA observable bands); per-component breakdown in §1 table. Subdomain carve-outs: M3 in frequency bands where merger+ringdown or cosmological+collapse components dominate. Substrate-c preserved; substrate-parameter $H_0$ at substrate-parameter-INHERITED level via Route A4. **F1 (sharpest):** $\Omega_{\mathrm{GW}}(f)$ spectrum systematically inconsistent with substrate-graph per-event composition refutes the chain. Currently consistent: LIGO/Virgo upper limits at $\Omega_{\mathrm{GW}} \lesssim 10^{-8}$ in 25–500 Hz; NANOGrav PTA nHz stochastic signal (2023, model-degenerate; SMBH-inspiral interpretation matches Dyn_05 prediction). Addresses **Paper_ED_GW_00 row 13** at corpus level via population integration.

---

## §1 Statement of Result

The stochastic GW background spectrum $\Omega_{\mathrm{GW}}(f)$ is the substrate-graph **cosmologically-integrated NoetherFlux output of mixed-signature saddle transitions across cosmic history**, composed as:

$$
\Omega_{\mathrm{GW}}(f) = \sum_{\mathrm{event\ class}\ E} \int dz\, \frac{n_E(z)}{H(z)(1+z)} \cdot \frac{dE_{\mathrm{GW}}}{df_s}\bigg|_E\bigg(f(1+z)\bigg)
$$

with cosmological-history integration over redshift $z$, event-rate density $n_E(z)$, source-frame frequency $f_s = f(1+z)$, and per-event emission spectrum $dE_{\mathrm{GW}}/df_s|_E$ supplied by the relevant Dynamics-Arc + GW-Arc paper for event class $E$. The Hubble parameter $H(z)$ enters via cosmological-history-integration kernel (inherits Cos_01 + Cos_05 framework + Route A4 substrate-parameter-INHERITED scale).

**Three source-class components** in observable frequency bands:

| Component | Source class | ED substrate-graph mechanism | Frequency band | Verdict tier |
|---|---|---|---|---|
| **Inspiral** | Compact-binary inspiral (BH-BH, NS-NS, BH-NS) across cosmic history | Paper_ED_Dyn_05 two-saddle coupled evolution + Dyn_03 quadrupole radiation | LIGO/Virgo (~Hz–kHz) + PTA (nHz) for SMBH inspirals | **M2** (inherits Dyn_05 → Dyn_03) |
| **Merger + ringdown** | BH-BH plunge/merger + post-merger ringdown across cosmic history | Paper_ED_Dyn_04 saddle-merging collapse + Paper_ED_GW_01 ringdown framework | LIGO/Virgo + Einstein Telescope band | **M3** (inherits Dyn_04 + GW_01) |
| **Cosmological + collapse** | Inflation-residual primordial GW + stellar-collapse + first-order phase transitions | Paper_ED_Cos_01 inflation + Paper_ED_Dyn_04 collapse + standard astrophysics | LISA + PTA + very-low-frequency observatories | **M3** (inherits Cos_01 + Dyn_04 + GW_00) |

**FORM:** $\Omega_{\mathrm{GW}}(f)$ = cosmologically-integrated NoetherFlux composition — **IDENTIFIED** via composition of GW_00 + GW_01 + Dyn_04 + Dyn_05 + Cos_01 + Cos_05 frameworks.

**VALUE:** cosmological-integration kernel $H(z)$ inherits standard cosmology + Route A4 substrate-parameter-INHERITED scale; per-event emissions inherit substrate-graph chains; binary-population content $n_E(z)$ inherits standard astrophysics.

**IC:** binary-merger + collapse-event population history inherited from standard astrophysical population-synthesis at all cosmological epochs.

**Verdict: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — net base verdict by component-status composition (Paper_095 §3.2.3)** within DCGT A→regime per §4 audit table. Net base M2 because the inspiral component (Dyn_05 → Dyn_03 M2 inheritance) dominates LIGO/Virgo/PTA observational bands where the integrated observable carries its load-bearing empirical anchors. **Subdomain carve-outs:** frequency bands where merger+ringdown or cosmological+collapse components dominate close at **M3** via Dyn_04 + GW_01 + Cos_01 + GW_00 inheritance. Upgrade of base verdict to M3 requires Dyn_03 → M3 (Route C4 + C1 closures), propagating through Dyn_05 → M3 then GW_02 → M3.

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02 (participation), P03 (translation invariance — Noether source), P09 (polarity), P10 (multiple rule-types — V1, V5 kernel structure), P11 (commitment / time arrow), P12 (stability landscape), P13 (translation arrow).

**Upstream papers:**
- Paper_012 (P-RB-1 substrate-c bound)
- Paper_027 (Newton's $G$ via dimensional rearrangement)
- Paper_028 (cosmic decoupling surface $R_H = c/H_0$ — supplies cosmological-integration kernel via Hubble parameter)
- Paper_032 (weak-field 1/r dilution — GW amplitude falloff per event)
- Paper_073 (DCGT hydrodynamic-window coarse-graining)
- Paper_089 (V1 retarded kernel + T18)
- Paper_090 (V5 cross-chain finite-memory)
- Paper_ED_SC_4_9 (saddle classification S1/S2/S3)
- Paper_ED_Cos_01 (Inflation; M3 — supplies inflationary-residual primordial GW spectrum framework + cosmological-expansion history)
- Paper_ED_Cos_05 (Dark Energy; M3 — supplies late-universe expansion-history $H(z \to 0)$ framework)
- Paper_ED_GW_00 (GW propagation; M3 + row 12 partial form-closure — supplies substrate-c propagation + NoetherFlux chain for outward GW emission)
- Paper_ED_GW_01 (Ringdown spectroscopy; M3 — supplies post-merger ringdown emission per event)
- Paper_ED_Dyn_01 (Saddle dynamics; M3 — supplies S2 mixed-signature framework for compact objects)
- Paper_ED_Dyn_02 (Horizon-Motion; M2)
- **Paper_ED_Dyn_03 (Radiation Law; M2 — propagates to Dyn_05, then to GW_02)**
- **Paper_ED_Dyn_04 (Gravitational Collapse; M3 — supplies merger-event substrate-graph mechanism + supernova-collapse contribution)**
- **Paper_ED_Dyn_05 (Inspiral Dynamics; M2 — supplies compact-binary-inspiral GW emission via Dyn_03 quadrupole chain; load-bearing for GW_02 M2 verdict)**
- Update_ED_SC_4x_Arc_M3 (six-projection arc-wide M3 upgrade post-Route-A)
- Standard astrophysical population-synthesis machinery (binary-formation channels; cosmological star-formation history; supernova rates; merger-rate distributions) — textbook inheritance via standard astrophysics
- Standard cosmological-background machinery (inflationary GW spectrum predictions; phase-transition GW spectrum; cosmic-string GW signatures if applicable) — textbook inheritance

**Substrate-research support:**
- Memo_ED_RouteA_MultiRouteConvergence_Audit (multi-route convergence option (ii); substrate-parameter-INHERITED level)
- Memo_ED_Q1Q2_JointClosure_Construct + Memo_ED_ChainClass_C3_Construct + Audit (saturation chain; cosmological-history framework inheritance)

**No new substrate primitives. No paper-specific postulates.**

---

## §3 Derivation

### §3.1 NoetherFlux propagation across cosmic history (GW_00 + cosmology composition)

Per Paper_ED_GW_00's row 12 partial form-closure (§3.9 NoetherFlux substrate-graph chain): each saddle-Hessian-signature-reconfiguration event at substrate-graph level produces outward GW emission with $P_{\mathrm{GW}} = (G/5c^5)\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$. For events distributed across cosmic history, each event's emission propagates outward at substrate-c (Paper_012 + Paper_089); cosmological-expansion-history (Cos_01 + Cos_05) redshifts the GW frequencies during transit. The cumulative output observed at present epoch is the integrated NoetherFlux over all events + cosmic history.

### §3.2 Per-event emission inheritance (Dyn_05 + Dyn_04 + GW_01)

Per-event GW emission spectra are supplied by the Dynamics-Arc + GW-Arc papers:

- **Compact-binary inspiral:** $dE_{\mathrm{GW}}/df_s \propto f_s^{-1/3}$ via Peters 1964 chirp scaling, inherited from Paper_ED_Dyn_05 + Dyn_03 substrate-graph quadrupole-formula chain (M2 status).
- **Plunge / merger:** standard NR-derived merger waveform peak, inherited at NR-quantitative level via DCGT continuum bridge (Paper_ED_Dyn_04 §3.5; standard astrophysics quantitative content).
- **Post-merger ringdown:** QNM-spectrum emission with $\omega_n = \omega_R^{(n)} + i\omega_I^{(n)}$, inherited from Paper_ED_GW_01 substrate-graph Hessian-eigenstructure framework (M3 status).
- **Stellar collapse:** time-varying mass-quadrupole during aspherical collapse, inherited from Paper_ED_Dyn_04 + standard supernova-GW phenomenology (M3 status; quantitative content via standard astrophysics).
- **Cosmological-inflation residual:** primordial GW spectrum from Paper_ED_Cos_01 saturation-regime dynamics + standard inflationary-perturbation theory (M3 status with cosmological-perturbation-spectrum content inherited).

### §3.3 Cosmological-history integration kernel

The cosmological-history integration:

$$
\Omega_{\mathrm{GW}}(f) = \frac{1}{\rho_c} \sum_E \int_0^\infty dz \, \frac{n_E(z)}{H(z) (1+z)} \cdot f \cdot \frac{dE_{\mathrm{GW}}}{df_s}\bigg|_E\bigg(f_s = f(1+z)\bigg)
$$

with $\rho_c = 3H_0^2/(8\pi G)$ the critical density (Friedmann inheritance + Paper_027 substrate-parameter content), $H(z)$ the Hubble parameter at redshift $z$ (inherits Cos_05 saturation-regime $H_0$ + Cos_01 inflation-regime + standard cosmology for matter/radiation eras), and event-rate density $n_E(z)$ from standard astrophysical population-synthesis.

Substrate-graph framework supplies the structural form via composition; substrate-parameter content $H_0$ (and hence $\rho_c$ and $H(z)$ asymptotics) inherits Route A4 substrate-parameter-INHERITED level (Paper_027-analog).

### §3.4 Compact-binary-inspiral component (Dyn_05 → Dyn_03 M2 chain)

For compact-binary inspirals across the cosmological binary-merger population (BH-BH, NS-NS, BH-NS), the per-event $dE_{\mathrm{GW}}/df_s \propto f_s^{-1/3}$ scaling (Peters 1964) combined with cosmological-integration produces:

$$
\Omega_{\mathrm{GW}}^{\mathrm{inspiral}}(f) \propto f^{2/3}
$$

at low frequencies (well below the merger frequency of each contributing event). This is the standard astrophysical-foreground prediction for the inspiral component of the stochastic background.

**Load-bearing:** the substrate-graph chain Dyn_05 → Dyn_03 carries M2 status (Route C4 source-class identification + Route C1 substrate-graph parameter constructions). The inspiral component of $\Omega_{\mathrm{GW}}(f)$ therefore inherits M2; the substrate-graph framework supplies the *form* at M2-equivalent level; the standard $f^{2/3}$ scaling is recovered via the substrate-graph chain.

### §3.5 Merger + ringdown component (Dyn_04 + GW_01 M3)

For BH-BH merger events at cosmologically-distributed times and masses, the merger-peak GW emission + post-merger ringdown GW emission inherit Paper_ED_Dyn_04 + Paper_ED_GW_01 frameworks. Merger-peak emission supplies a high-frequency spectral feature per event (around the ISCO scale $f_{\mathrm{ISCO}} \sim c^3/(GM)$); post-merger ringdown supplies the QNM-spectrum decay tail per event.

Cosmologically-integrated, the merger + ringdown contribution to $\Omega_{\mathrm{GW}}(f)$ spans the LIGO/Virgo band for stellar-mass BHs (10 Hz - 1 kHz) and the Einstein Telescope / Cosmic Explorer extended band (sub-Hz - few kHz). **M3 status** via Dyn_04 + GW_01 inheritance.

### §3.6 Cosmological + collapse component (Cos_01 + Dyn_04 + GW_00 M3)

For cosmological sources (inflation-residual primordial GW spectrum from Cos_01; first-order phase-transition GW spectrum from standard cosmology if applicable; cosmic-string GW signatures if such defects exist), the substrate-graph framework supplies:

- **Inflationary residual:** Cos_01 saturation-regime substrate-graph framework supplies the substrate-side mechanism for inflationary tensor-mode generation; quantitative spectrum (typically nearly-scale-invariant, $\Omega_{\mathrm{GW}}^{\mathrm{infl}}(f) \approx \mathrm{const}$ at LISA / PTA scales) inherits standard inflationary-perturbation theory.
- **Stellar collapse contribution:** Paper_ED_Dyn_04 collapse framework + standard supernova-rate distributions across cosmic history supply the stellar-collapse component.

**M3 status** for both via Cos_01 + Dyn_04 + GW_00 inheritance.

### §3.7 Value inheritance from Route A and component-status composition

Per Memo_ED_RouteA_MultiRouteConvergence_Audit option (ii): cosmological-integration kernel $H(z)$ inherits Route A4 substrate-parameter-INHERITED scale at present-epoch $H_0$ + Cos_01 inflation-regime $H_{\mathrm{infl}}$ + standard cosmology for intermediate-redshift Hubble evolution. Substrate-parameter values $\tau_{V_5}/\tau_P \approx 10^{61}$ + $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ at primitive level; tightening via RA-OPEN-4a/4b/4c-explicit substrate-research-frontier, not blocking.

**Component-status composition rule:** the net verdict of the integrated $\Omega_{\mathrm{GW}}(f)$ is bounded above by the verdict of the dominant frequency-band component. In LIGO/Virgo/PTA observational bands, the compact-binary-inspiral component is dominant (M2 via Dyn_05); the merger + ringdown + cosmological components are M3 but subdominant in the inspiral-dominated regime. **Net verdict: M2 with explicit component-status breakdown.** Frequency bands where the inspiral component is subdominant (e.g., very-low-frequency LISA bands where cosmological-source contributions dominate; high-frequency post-merger ringdown bands) close at M3 via dominant-component inheritance.

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P03, P09, P10, P11, P12, P13 | **P** | Paper_087. |
| 2 | Upstream inheritance block | **I** | Paper_012; Paper_027; Paper_028; Paper_032; Paper_073; Paper_089; Paper_090; Paper_ED_SC_4_9; Paper_ED_Cos_01 (M3); Paper_ED_Cos_05 (M3); Paper_ED_GW_00 (M3); Paper_ED_GW_01 (M3); Paper_ED_Dyn_01 (M3); Paper_ED_Dyn_02 (M2); **Paper_ED_Dyn_03 (M2 — propagates)**; Paper_ED_Dyn_04 (M3); **Paper_ED_Dyn_05 (M2 — propagates to GW_02 M2 verdict)**; Update_ED_SC_4x_Arc_M3. |
| 3 | Standard astrophysical population-synthesis machinery (binary formation rates; star-formation history; supernova rate distributions) | **I** | Textbook inheritance via standard astrophysics + DCGT continuum bridge. |
| 4 | Standard cosmological-background machinery (inflationary tensor-mode spectrum; phase-transition GW spectrum; cosmic-string signatures) | **I** | Textbook inheritance. |
| 5 | NoetherFlux propagation per event via GW_00 row 12 chain | **D-via-I** | §3.1. GW_00 §3.9 NoetherFlux chain. |
| 6 | Cosmological-history redshift of per-event GW frequencies | **D-via-I** | §3.1, §3.3. Composition of Cos_01 + Cos_05 expansion history + standard cosmology for intermediate epochs. |
| 7 | Per-event $dE_{\mathrm{GW}}/df_s$ supplied by component-specific Dynamics-Arc + GW-Arc papers | **D-via-I (conditional on Dyn_03 M2 for inspiral component)** | §3.2. Dyn_05 (inspiral, M2); Dyn_04 (collapse + merger, M3); GW_01 (ringdown, M3); Cos_01 (inflation residual, M3). |
| 8 | Cosmological-integration form $\Omega_{\mathrm{GW}}(f) = \rho_c^{-1} \sum_E \int dz \cdot n_E(z)/[H(z)(1+z)] \cdot f \cdot dE_{\mathrm{GW}}/df_s$ | **D-via-I** | §3.3. Standard cosmology integration + Friedmann critical density + Route A4 substrate-parameter-INHERITED scale. |
| 9 | $H(z)$ cosmological-history kernel via Cos_01 + Cos_05 + standard cosmology | **D-via-I** | §3.3, §3.7. Composition of Cos_01 + Cos_05 + Route A4 inheritance. |
| 10 | Compact-binary-inspiral component $\Omega_{\mathrm{GW}}^{\mathrm{inspiral}}(f) \propto f^{2/3}$ | **D-via-I (conditional on Dyn_03 M2)** | §3.4. Inherits Dyn_05 → Dyn_03 chain at M2 status. **Load-bearing for net M2 verdict.** |
| 11 | Merger + ringdown component spectrum (LIGO/Virgo band for stellar-mass BHs + ET / CE extended band) | **D-via-I** | §3.5. Dyn_04 + GW_01 at M3. |
| 12 | Cosmological-inflation residual primordial GW spectrum | **D-via-I** | §3.6. Cos_01 saturation-regime + standard inflationary-perturbation theory inheritance. |
| 13 | Stellar-collapse contribution from cosmological-history supernova rates | **D-via-I** | §3.6. Dyn_04 + standard supernova rates inheritance. |
| 14 | Event-rate density $n_E(z)$ from standard astrophysical population-synthesis | **I** | §3.3. Standard astrophysics; substrate-graph framework does not rederive. |
| 15 | $\rho_c = 3H_0^2/(8\pi G)$ critical-density inheritance | **D-via-I** | §3.3. Friedmann + Paper_027 substrate-parameter content. |
| 16 | $H_0$ at Route A4 substrate-parameter-INHERITED level | **I** | Sub-type per Paper_095 §3.2.1: *substrate-parameter-INHERITED*. §3.7. Memo_RouteA_MultiRouteConvergence_Audit option (ii). |
| 17 | Substrate-c bound preserved throughout (propagation + redshift) | **D-via-I** | §3.1. Paper_012 + Paper_089. |
| 18 | Binary-merger + collapse-event population history (IC) inherited from astrophysical population-synthesis | **I** | Sub-type per Paper_095 §3.2.1: *IC-INHERITED*. §1 + §2.IC. Standard astrophysics. |
| 19 | Component-status composition rule: net verdict bounded above by dominant-frequency-band component | **D-via-I** | §3.7. Inspiral component (M2 via Dyn_05) dominant in LIGO/Virgo/PTA bands → net M2. |
| 20 | Verdict M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — net base via component-status composition; M3 subdomain carve-outs | **A→position** | Per Paper_095 §3.2.1 (three-axis) + §3.2.3 (component-status composition). Five-anchor verdict-sync: status / abstract / §1 / this row / §6 all carry base M2 with per-component breakdown noted. Subdomains where merger+ringdown or cosmological+collapse components dominate close at M3 via Dyn_04 + GW_01 + Cos_01 + GW_00 inheritance. |

**Audit summary:** zero pure-D rows; **eleven substantive D-via-I rows** (5–13, 15, 17, 19); four I rows (2, 3, 4, 14); one substrate-parameter-INHERITED row (16); one IC-INHERITED row (18); one P row (1); one A→position verdict row (20). **Load-bearing remaining OPEN: Paper_ED_Dyn_05 M2 status propagates** (which itself inherits Paper_ED_Dyn_03 M2 — Route C4 source-class identification + Route C1 substrate-graph parameter constructions). Upstream OPENs from other papers (SC-4.9 substrate-FORCED exhaustiveness; Route A tightening RA-OPENs) inherited at upstream status. No new substrate primitives; no paper-specific postulates.

---

## §5 Falsification Criteria

- **F1 (sharpest):** Observation of $\Omega_{\mathrm{GW}}(f)$ spectrum systematically inconsistent with composition of substrate-graph per-event emissions across cosmological binary-merger + collapse-event + cosmological-source populations. Specifically: detected spectral shape deviating significantly from the expected component-composition in observable frequency bands (LIGO/Virgo ~Hz–kHz; NANOGrav PTA nHz; LISA mHz when operational; Einstein Telescope / Cosmic Explorer extended sub-Hz–kHz) beyond standard astrophysical + population-synthesis uncertainty refutes the substrate composition. Currently consistent: LIGO/Virgo upper limits at $\Omega_{\mathrm{GW}} \lesssim 10^{-8}$ in 25-500 Hz; NANOGrav PTA stochastic signal at nHz (Sep 2023) is consistent with SMBH-binary-inspiral interpretation per Dyn_05.

- **F2:** Detection of inspiral-dominant frequency bands with $\Omega_{\mathrm{GW}}(f)$ spectral slope significantly deviating from $\propto f^{2/3}$ scaling (the Peters-formula-derived inspiral prediction) beyond observational uncertainty. Refutes §3.4 + audit row 10. Currently consistent: NANOGrav PTA signal slope is consistent with SMBH-binary-inspiral prediction.

- **F3:** Detection of merger-band or ringdown-band stochastic contributions inconsistent with Dyn_04 + GW_01 per-event emission compositions. Refutes §3.5 + audit row 11.

- **F4:** Detection of cosmological-source contributions (very-low-frequency LISA bands; primordial-inflation residual) significantly inconsistent with Cos_01 + GW_00 composition framework. Refutes §3.6 + audit row 12.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

The stochastic GW background spectrum $\Omega_{\mathrm{GW}}(f)$ is the cosmologically-integrated NoetherFlux output of all mixed-signature saddle transitions across cosmic history. Per-event emission spectra inherit from the Dynamics-Arc + GW-Arc papers (Dyn_05 inspiral, Dyn_04 collapse/merger, GW_01 ringdown, Cos_01 inflation residual); cosmological-history integration inherits Cos_01 + Cos_05 + standard cosmology framework; outward propagation per event via GW_00 NoetherFlux chain at substrate-c. Substrate-parameter content $H_0$ at substrate-parameter-INHERITED level via Route A4 (Paper_027-analog).

**Verdict: M2 (form-IDENTIFIED + value-INHERITED + IC-INHERITED) — net base via component-status composition (Paper_095 §3.2.3)** within DCGT A→regime. Eleven D-via-I rows; four I rows; one substrate-parameter-INHERITED row; one IC-INHERITED row; zero pure-D rows; no paper-specific postulates; no new substrate primitives. **Load-bearing remaining OPEN: Paper_ED_Dyn_05 M2 status propagates** (Dyn_05 inherits Dyn_03 M2 — Route C4 + Route C1 load-bearing for upgrade chain). Net base M2 because the inspiral component dominates LIGO/Virgo/PTA bands; **subdomain carve-outs at M3** in merger+ringdown-dominated and cosmological+collapse-dominated bands via Dyn_04 + GW_01 + Cos_01 + GW_00 inheritance. The cosmological-integration framework itself is M3-supported via GW_00 + Cos_01 + Cos_05; the per-event inspiral-component inheritance pulls the *net base* down to M2 in the load-bearing observable domain. Standard astrophysical population-synthesis content (binary-formation channels; star-formation history; supernova rates) is INHERITED; substrate-graph framework supplies the structural form. Substrate-ontology distinguishing content: $\Omega_{\mathrm{GW}}(f)$ as cosmologically-integrated saddle-Hessian-signature-reconfiguration NoetherFlux output *replaces* metric-perturbation-superposition.

**Cross-arc consequences.** Upstream, GW_02 inherits unchanged from all 8+ listed upstream papers at their stated verdicts; the only propagation is Dyn_03 → Dyn_05 → GW_02 M2 base inheritance. Downstream / cross-arc: **closes Paper_ED_GW_00 row 13** (full inspiral-merger-ringdown waveform; standing OPEN) **at corpus level via population integration** — combined with Dyn_05 + NR + Dyn_04 + GW_01 per-event waveform framework, the full BH-BH merger waveform is now structurally complete at substrate-graph + population level; component-status composition makes the population-level closure mixed-tier (M2 base; M3 subdomain carve-outs). Strengthens the empirical-prediction sector via the substrate-graph reading of LISA / ET / CE / PTA forward-looking observatory targets, and supplies an additional empirical-test channel for the SCBU BH-horizon projection through the collapse + merger + ringdown contribution to $\Omega_{\mathrm{GW}}(f)$. **NANOGrav PTA postdiction:** the 2023 nHz stochastic signal is currently consistent with multiple source models (SMBH-binary inspirals, cosmic strings, first-order phase transitions, primordial inflation) and NANOGrav's own analyses prefer the SMBH-inspiral interpretation with significant model uncertainty. ED's Dyn_05 + GW_02 inspiral component reproduces the SMBH-inspiral $f^{2/3}$ slope prediction at M2 level; future PTA refinement will discriminate among source models, and ED's substrate-graph framework supplies both the SMBH-inspiral reading and the cosmological-source-component readings (Cos_01 inflation residual; Dyn_04 collapse channel) for alternative source classes.

---

**End Paper_ED_GW_02.**
