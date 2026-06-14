# Papers Index — Canonical Source of Truth

**Last updated:** 2026-05-14
**Purpose:** Single source of truth for every paper in the ED corpus. Tracks paper number (locked-in numbering), title, domain/arc assignment, status, and file location. Reflects the corpus state after Round 1 (per-paper QC), Round 2 (cross-paper audit + theorem gap-fill), and Round 3 (cross-arc harmonization + SCBU + ED-SC 4.x arc).

**Source corpus:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\`

**Status enum:**
- **WRITTEN** — paper complete in corpus.
- **DRAFTING** — actively being written.
- **PLANNED** — identified, scheduled, not yet started.
- **CANDIDATE** — on the long candidate list but not yet committed to.
- **ARCHIVED** — superseded or retired; preserved for provenance.
- **SUPERSEDED** — replaced by a later paper or restructured.

---

## Arc 1 — Quantum Kinematics (Papers 001–012)

The Phase-1 QM-emergence program. Sixteen theorems closing the four standard quantum-mechanical postulates as substrate-derived results.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 001 | Pre-Individuation Amplitudes | foundations | WRITTEN | `Paper_001_PreIndividuation.md` |
| 002 | Tensor Product / Bipartite Mapping | foundations | WRITTEN | `Paper_002_TensorProduct.md` |
| 003 | Born Rule | foundations | WRITTEN | `Paper_003_BornRule.md` |
| 004 | Gleason-Type Uniqueness | foundations | WRITTEN | `Paper_004_GleasonUniqueness.md` |
| 005 | Projective Measurement | measurement | WRITTEN | `Paper_005_ProjectiveMeasurement.md` |
| 006 | Unitary Evolution | dynamics | WRITTEN | `Paper_006_UnitaryEvolution.md` |
| 007 | Hilbert-Space Emergence | foundations | WRITTEN | `Paper_007_HilbertSpace.md` |
| 008 | Phase Structure / U(1) Cyclic Substructure | foundations | WRITTEN | `Paper_008_PhaseStructure.md` |
| 008 (legacy) | Kernel Arrow (early draft; content moved to Paper_093) | — | ARCHIVED | `Paper_008_KernelArrow.md` |
| 009 | Berry Phase via Adiabatic Coarse-Graining | observables | WRITTEN | `Paper_009_BerryPhase.md` |
| 010 | Aharonov-Bohm Phase | observables | WRITTEN | `Paper_010_AharonovBohm.md` |
| 011 | Bloch Theorem from P10 Translation Symmetry | dynamics | WRITTEN | `Paper_011_BlochTheorem.md` |
| 012 | RB-1: Rate of Becoming (substrate-c invariance) | dynamics | WRITTEN | `Paper_012_RB1_RateOfBecoming.md` |

---

## Arc 2 — Form-Level QFT (Papers 013–024)

Substrate-level QFT scaffolding. V1 spectral structure, T17 gauge fields, Yang–Mills arc, Lindblad open-system limit.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 013 | V1 Vacuum Kernel (Spectral + Form Factor) | kernels | WRITTEN | `Paper_013_V1_VacuumKernel.md` |
| 014 | V1 in Curved Acoustic Background | kernels | WRITTEN | `Paper_014_V1_CurvedBackground.md` |
| 015 | T17 — Gauge Fields as Rule-Type Bundles | gauge | WRITTEN | `Paper_015_T17_GaugeFields.md` |
| 016 | Generalized Minimal Coupling (Non-Abelian) | gauge | WRITTEN | `Paper_016_MinimalCoupling.md` |
| 017 | Free Scalar QFT / Lorentz Covariantization | qft | WRITTEN | `Paper_017_FreeScalarQFT.md` |
| 018 | Yang–Mills YM-1: DCGT-NA Construction | yang-mills | WRITTEN | `Paper_018_YangMills1.md` |
| 019 | YM-2: Substrate→Continuum Action | yang-mills | WRITTEN | `Paper_019_YM2_SubstrateToContinuum.md` |
| 020 | YM-3: Osterwalder–Schrader Positivity | yang-mills | WRITTEN | `Paper_020_YM3_OSPositivity.md` |
| 021 | YM-4: Mass-Gap Mechanism (Coercivity) | yang-mills | WRITTEN | `Paper_021_YM4_MassGap.md` |
| 022 | YM-5: Gauge Orbits / Quotient Hilbert | yang-mills | WRITTEN | `Paper_022_YM5_GaugeQuotient.md` |
| 023 | YM-6: Clay-Relevance Synthesis | yang-mills | WRITTEN | `Paper_023_YM6_ClaySynthesis.md` |
| 024 | Lindblad Master Equation (Open-System Limit) | measurement | WRITTEN | `Paper_024_LindbladLimit.md` |

---

## Arc 3 — Gravity / Substrate Gravity (Papers 025–038)

Substrate-level derivations of Newton's law, a₀, ECR, BTFR slope-4, plus weak-field prerequisites and acoustic-metric covariantization.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 025 | Holographic Participation-Count Bound | holography | WRITTEN | `Paper_025_HolographicBound.md` |
| 026 | Cumulative-Strain Reading of P12 | foundations | WRITTEN | `Paper_026_CumulativeStrain.md` |
| 027 | Newton's $G = c^3\ell_P^2/\hbar$ | foundations | WRITTEN | `Paper_027_Newtons_G.md` |
| 028 | Cosmic Decoupling Surface $R_H = c/H_0$ | cosmology | WRITTEN | `Paper_028_CosmicDecoupling.md` |
| 029 | Transition Acceleration $a_0 = cH_0/(2\pi)$ | mond | WRITTEN | `Paper_029_a0.md` |
| 030 | ED Combination Rule $a = \sqrt{a_N a_0}$ | mond | WRITTEN | `Paper_030_CombinationRule.md` |
| 031 | BTFR Slope-4 $v^4 = GMa_0$ | galactic | WRITTEN | `Paper_031_BTFR.md` |
| 032 | Six Weak-Field Prerequisites | weak-field | WRITTEN | `Paper_032_WeakFieldPrereqs.md` |
| 033 | Scalar-Tensor Acoustic-Metric Covariantization (Arc ED-10) | strong-field | WRITTEN | `Paper_033_AcousticMetric.md` |
| 034 | Deep MOND + Superluminality Cost | mond | WRITTEN | `Paper_034_DeepMOND.md` |
| 035 | Acoustic-Metric Guardrails (C1–C6) | strong-field | WRITTEN | `Paper_035_AcousticGuardrails.md` |
| 036 | Flat-Background MOND Field Equation | mond | WRITTEN | `Paper_036_MOND_FieldEquation.md` |
| 037 | $a_0$ Cosmological-Rate Invariance | mond | WRITTEN | `Paper_037_a0_Invariance.md` |
| 038 | Cosmological Implications (Substrate-Cosmology Decoupling) | cosmology | WRITTEN | `Paper_038_CosmologicalImplications.md` |

---

## Arc 4 — Black Holes / Hawking (Papers 039–052)

Arc BH + Arc Hawking. Horizon as decoupling surface, Hawking spectrum, trans-Planckian resolution, Planck-mass remnant Scenario C, area law, BHPT scattering, helicity, Page curve, info-paradox synthesis.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 039 | Horizon as Decoupling Surface ($\Gamma_{\text{cross}} \to 0$) | foundations | WRITTEN | `Paper_039_HorizonDecoupling.md` |
| 040 | Trans-Planckian Resolution via V5 Cutoff | hawking | WRITTEN | `Paper_040_TransPlanckian.md` |
| 041 | Planck-Mass Remnant Scenario C | remnants | WRITTEN | `Paper_041_RemnantMass.md` |
| 042 | No-Singularity from Substrate Cutoff | interior | WRITTEN | `Paper_042_NoSingularity.md` |
| 043 | Area-Law Form + $\log g$ Coefficient | thermodynamics | WRITTEN | `Paper_043_AreaLaw.md` |
| 044 | BHPT Scattering Structure | scattering | WRITTEN | `Paper_044_BHPT_Scattering.md` |
| 045 | Helicity Behavior at Horizons | scattering | WRITTEN | `Paper_045_Helicity.md` |
| 046 | Kerr Twist / Axisymmetric Substrate Geometry | rotating | WRITTEN | `Paper_046_KerrTwist.md` |
| 047 | Hawking Spectrum via Substrate-Unruh / KMS | hawking | WRITTEN | `Paper_047_HawkingSpectrum.md` |
| 048 | H-8: Higher-Order Resummation Selecting Scenario C | hawking | WRITTEN | `Paper_048_H8_Resummation.md` |
| 049 | H-9: Cosmological PBH Relic Abundance | remnants | WRITTEN | `Paper_049_PBH_RelicAbundance.md` |
| 050 | Page Curve via V5 Entanglement-Bandwidth | information | WRITTEN | `Paper_050_PageCurve.md` |
| 051 | Information Paradox Not Generated (Substrate Audit) | information | WRITTEN | `Paper_051_SubstrateAudit.md` |
| 052 | BH Information-Paradox Synthesis | information | WRITTEN | `Paper_052_BH_ParadoxSynthesis.md` |

---

## Arc 5 — Q-Compute / UR-1 (Papers 053–062)

Substrate origin of quantum-computing limits. $\mathcal{M}_{\text{cap}}$ as one substrate object; Class A/B/C exhaustiveness; UR-1 theorem; cross-platform unification via $\mathcal{M}_{\text{crit}}$; cross-domain echo with BH.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 053 | $\mathcal{M}_{\text{cap}}$ as One Substrate Object | foundations | WRITTEN | `Paper_053_Mcap.md` |
| 054 | UR-1 Theorem (Unresolved-Regime Characterization) | foundations | WRITTEN | `Paper_054_UR1.md` |
| 055 | A/B/C Architectural Exhaustiveness | classification | WRITTEN | `Paper_055_ABC_Exhaustiveness.md` |
| 056 | Class A Wall at 140–250 kDa (Matter-Wave) | predictions | WRITTEN | `Paper_056_ClassA_Wall.md` |
| 057 | Class B Exponential Gap-Suppression | predictions | WRITTEN | `Paper_057_ClassB_GapSuppression.md` |
| 058 | Class C Correlation-Budget Plateau | predictions | WRITTEN | `Paper_058_ClassC_Plateau.md` |
| 059 | Meta-Architectures as Compositions (EC, DD, hybrids) | architectures | WRITTEN | `Paper_059_MetaArchitectures.md` |
| 060 | $\mathcal{M}_{\text{crit}}$ Unification (Matter-Wave / Qubit) | unification | WRITTEN | `Paper_060_Mcrit_Unification.md` |
| 061 | Q-Compute Foundations Consolidated (Capstone) | capstone | WRITTEN | `Paper_061_QCompute_Foundations.md` |
| 062 | Cross-Domain Echo: BH ↔ Q-Compute V5-Saturation | cross-arc | WRITTEN | `Paper_062_CrossDomainEcho.md` |

---

## Arc 6 — Entanglement (Papers 063–072)

Bipartite entanglement architecture substrate-derived. Tensor product, Schmidt, monogamy via V5, no-signaling three-lock, Tsirelson, von Neumann entropy. Interpretive capstone identifying entanglement as the unresolved regime.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 063 | E-1: Tensor Product Structure | foundations | WRITTEN | `Paper_063_TensorProduct.md` |
| 064 | E-3: Schmidt Decomposition | foundations | WRITTEN | `Paper_064_SchmidtDecomposition.md` |
| 065 | E-4: Monogamy via V5 Cross-Chain Bandwidth | foundations | WRITTEN | `Paper_065_Monogamy.md` |
| 066 | E-5: No-Signaling Three-Lock | foundations | WRITTEN | `Paper_066_NoSignaling.md` |
| 067 | von Neumann Entropy (folder slot-shifted; see Paper_068) | foundations | WRITTEN | `Paper_067_VonNeumannEntropy.md` |
| 068 | E-6: von Neumann Entropy (canonical slot per Paper_087) | foundations | WRITTEN | `Paper_068_VonNeumannEntropy.md` |
| 069 | Bell–Tsirelson Polytope Reconstruction | foundations | WRITTEN | `Paper_069_TsirelsonReconstruction.md` |
| 070 | E-7: Bipartite Synthesis (Capstone) | capstone | WRITTEN | `Paper_070_BipartiteSynthesis.md` |
| 071 | ER=EPR-Class Structural Echo (Entanglement ↔ BH) | cross-arc | WRITTEN | `Paper_071_ER_EPR_Echo.md` |
| 072 | Entanglement as Unresolved Regime (Interpretive Capstone) | interpretation | WRITTEN | `Paper_072_IndividuationRegime.md` |

---

## Arc 7 — Soft Matter / Navier–Stokes / MHD (Papers 073–086)

DCGT bridge, V5 viscoelastic, NS-1 dimensional forcing, NS-2 coarse-graining, NS-Smoothness Intermediate Path C, cascade, P4-NN rheology, NS-Q, NS-MHD closure, advection/induction non-ED, vortex-stretching obstruction, Universal Mobility Law.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 073 | DCGT — Diffusion Coarse-Graining Theorem | foundations | WRITTEN | `Paper_073_DCGT.md` |
| 074 | V5 Viscoelastic Maxwell Ansatz | viscoelasticity | WRITTEN | `Paper_074_V5_MaxwellAnsatz.md` |
| 075 | NS-1: Dimensional Forcing to $D = 3+1$ | foundations | WRITTEN | `Paper_075_NS1_DimensionalForcing.md` |
| 076 | NS-2: Substrate→Continuum Coarse-Graining | foundations | WRITTEN | `Paper_076_NS2_CoarseGraining.md` |
| 077 | NS-3: Smoothness via R1 (Intermediate Path C) | regularity | WRITTEN | `Paper_077_NS_Smoothness_R1.md` |
| 078 | NS-Turb: P7 ↔ Cascade | turbulence | WRITTEN | `Paper_078_NS_Turb_P7_Cascade.md` |
| 079 | P4-NN: Krieger–Dougherty + Maxwell Rheology | rheology | WRITTEN | `Paper_079_P4_NN_Rheology.md` |
| 080 | NS-Q Canonical $Q \approx 3.5$ | rheology | WRITTEN | `Paper_080_NS_Q_Factor.md` |
| 081 | NS-MHD H1/H2/H3 Closure | mhd | WRITTEN | `Paper_081_NS_MHD_Closure.md` |
| 082 | Advection / Induction Non-ED Triangulation | mhd | WRITTEN | `Paper_082_Advection_Induction_NonED.md` |
| 083 | Unified Kinematic-Coupling Pattern (NS / MHD) | mhd | WRITTEN | `Paper_083_KinematicCoupling.md` |
| 084 | Vortex-Stretching Obstruction at Substrate Level | regularity | WRITTEN | `Paper_084_VortexStretching.md` |
| 085 | Universal Mobility Law (Empirical Anchor) | mobility | WRITTEN | `Paper_085_UniversalMobilityLaw.md` |
| 086 | Soft-Matter Synthesis (Capstone) | capstone | WRITTEN | `Paper_086_SoftMatter_Synthesis.md` |

---

## Arc 8 — Wedges / Kernel Theory / Foundations (Papers 087–097)

Foundational substrate-level theorems and methodology. 13-primitive position paper, primitive load-bearing audit, V1/V5 canonical references, memory-kernel cascade, kernel hierarchy unification, T18 kernel-level arrow, forward-causal primitive structure, methodology formalization, cross-scale invariance, three-regime RG.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 087 | The 13 Primitives — Position Paper | foundations | WRITTEN | `Paper_087_13Primitives.md` |
| 088 | Primitive Load-Bearing Audit | foundations | WRITTEN | `Paper_088_PrimitiveAudit.md` |
| 089 | V1 Finite-Width Retarded Kernel (Canonical) | kernels | WRITTEN | `Paper_089_V1Kernel.md` |
| 090 | V5 Cross-Chain Correlation Kernel (Canonical) | kernels | WRITTEN | `Paper_090_V5Kernel.md` |
| 091 | Memory-Kernel Cascade Across Scales | kernels | WRITTEN | `Paper_091_KernelCascade.md` |
| 092 | Kernel Hierarchy Unification (Three-Index Classification) | kernels | WRITTEN | `Paper_092_KernelHierarchy.md` |
| 093 | T18 — Kernel-Level Arrow of Time | arrow | WRITTEN | `Paper_093_T18_ArrowOfTime.md` |
| 094 | Forward-Causal Substrate Primitive Structure | arrow | WRITTEN | `Paper_094_ForwardCausality.md` |
| 095 | Form-FORCED / Value-INHERITED Methodology | methodology | WRITTEN | `Paper_095_FormForced_ValueInherited.md` |
| 096 | Cross-Scale Invariance (ED-SC 3.x Canonical) | sc-arc | WRITTEN | `Paper_096_CrossScaleInvariance.md` |
| 097 | Three-Regime RG / 0.6 Problem | sc-arc | WRITTEN | `Paper_097_RG_0p6_Problem.md` |

---

## Program-Level Synthesis Papers (Papers 098–101)

Cross-arc synthesis and corpus-level capstones.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 098 | ED-QFT Unified Overview (Program Synthesis) | synthesis | WRITTEN | `Paper_098_EDQFT_Overview.md` |
| 099 | NS Synthesis Paper | synthesis | WRITTEN | `Paper_099_NS_Synthesis.md` |
| 100 | Five-Sector Program Overview (100-Paper Milestone Capstone) | capstone | WRITTEN | `Paper_100_FiveSector_ProgramOverview.md` |
| 101 | Falsification Register and Prediction Inventory (Corpus Capstone) | capstone | WRITTEN | `Paper_101_FalsificationRegister.md` |

---

## Theorem Stubs (T19, T20, T21)

Recovered theorem-stub papers per Round 2 Phase B.2. Follow Paper_093 (T18 rewrite) template; introduce no new postulates.

| Theorem | Title | Status | File |
|---|---|---|---|
| T19 | Newton's $G$ Structural Role | WRITTEN | `T19.md` |
| T20 | $a_0$ Structural Role | WRITTEN | `T20.md` |
| T21 | BTFR Slope-4 Structural Form | WRITTEN | `T21.md` |

Together with T17 (Paper_015), T18 (Paper_093), GR1 + N1 (Paper_014), UR-1 (Paper_054), the corpus foundational-theorem inventory is complete.

---

## Cross-Arc Synthesis: SCBU

Round 3 Phase B.2 deliverable. Introduces P-Substrate-Cosmology-Unified (corpus's 125th paper-specific postulate).

| Title | Status | File |
|---|---|---|
| Substrate-Cosmology Boundary Unification (SCBU) | WRITTEN | `Paper_SCBU_SubstrateCosmologyBoundary.md` |

---

## ED-SC 4.x Arc (Six-Paper Cross-Scale Extension)

Round 3 cross-scale extension arc. Identifies six SCBU-boundary projections within a unified four-regime RG model (UV / Transition / IR multi-sector / Cosmological).

| Paper | Title | Status | File |
|---|---|---|---|
| ED-SC 4.1 | BH Horizon ↔ Cosmic Decoupling Surface | WRITTEN | `Paper_ED_SC_4_1_BH_CosmicDecoupling.md` |
| ED-SC 4.2 | Substrate-Derivation of $\xi_{\text{canonical}}(H_0)$ | WRITTEN | `Paper_ED_SC_4_2_xi_canonical_H0_derivation.md` |
| ED-SC 4.3 | MOND/Galactic Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_3_MOND_SCBU.md` |
| ED-SC 4.4 | Q-Compute Platform Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_4_QCompute_SCBU.md` |
| ED-SC 4.5 | Soft-Matter NS-Q Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_5_SoftMatter_SCBU.md` |
| ED-SC 4.6 | Unified Cross-Scale Invariance (Capstone) | WRITTEN | `Paper_ED_SC_4_6_UnifiedCrossScale.md` |

All six papers sit at verdict tier M3 (FORM-FORCED + VALUE-INHERITED). Closing Paper_ED_SC_4.2 Route A (substrate-derived $\ell_{V5}(H_0)$) propagates to a **six-way simultaneous M3 → M2 verdict upgrade** across the entire ED-SC 4.x arc. Closing all three Routes A + B + C without additional postulates propagates to **M1** arc-wide — the first cross-arc M1 result in the corpus.

---

## Substrate-Evaluation Wave + Post-Pivot Gravity (June 2026)

Seven standalone papers from the substrate-evaluation program (build-and-run / theorem-anchored tests of the certified Σ-rule substrate) and the post-pivot Arc ED-10 curvature-emergence line. Distinct naming convention; no numbered slots consumed. Each paper carries a does-NOT-claim preamble, a P/D/I load-bearing audit, and falsifier sentences; `.pdf` builds accompany the `.md` sources.

| Paper | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| GR-I | The Bandwidth Lapse and the Factor of Two: The Weak-Field Einstein Metric | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-I_WeakFieldEinsteinMetric.md` |
| GR-II | The Arrow's Fingerprint: ED Gravity is Khronometric, GW-Clean, Lorentz-Safe | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-II_KhronometricClass.md` |
| SE-Continuum | The Continuum Limit of the Certified ED Substrate: a Kinetic Lattice-Gas, not a Diffusion PDE | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_Continuum_KineticLatticeGas.md` |
| SE-Primes | Template, Not Escape: Primes as a Ruler for the Finite-Memory Ceiling | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_FiniteMemoryCeiling_Primes.md` |
| SE-Charge | The Topological Skeleton of Charge: Quantized Winding and an Integral Gauss Law | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_ChargeAsTopology_B4.md` |
| SE-Capacity | Common Cause, Not Channel: The Determinability Boundary as an Observational Structure | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_CommonCauseNotChannel_A1.md` |
| Form-and-Flesh | Form and Flesh: The Two Walls of the Event-Density Substrate (synthesis capstone) | position / synthesis | WRITTEN | `position-paper/Paper_FormAndFlesh_TwoWalls.md` |
| KM-I | The Arrow's Deep Field: Dark-Matter Phenomenology from the Khronon, and the Unification of ED Gravity | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_KM-I_KhrononMOND.md` |
| KM-II | The Arrow's Horizon: The Khronon's Cosmological Face — the Dark Fluid, the Clustering Dial, and One Λ | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_KM-II_KhrononCosmology.md` |
| GR-III | The Arrow's Engine: The Dynamical Rule of ED Gravity, and the Closing of Its Weak-Field Assumptions | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-III_DynamicalRule.md` |
| ED-Gravity (PhilPapers) | The Arrow in the Law: Emergent Gravity from a Discrete, Irreversible Substrate (program synthesis, public-facing) | gravity / synthesis-paper | WRITTEN | `physics-papers/gravity/Paper_ED_Gravity_Program_PhilPapers.md` |
| One-Field | One Field: Gravity, Dark Matter, Dark Energy, and the Arrow of Time in ED (capstone letter) | gravity / synthesis-letter | WRITTEN | `physics-papers/gravity/Paper_OneField_Letter.md` |

Notes: GR-I/GR-II are the post-pivot curvature-emergence results, sharpening (not superseding) the Arc-3 scalar-tensor/MOND papers — see GR-I §7 / GR-II §9 for the explicit reconciliation. Form-and-Flesh is the program reach-statement (the empirical successor to the Contrast-First ontology paper) and lives in `position-paper/` alongside it. Underlying simulation artifacts live in the working repo (`event-density/evaluation/` and `event-density/foundations/`).

---

## Total counts (2026-05-14)

- **Numbered Papers (001–101):** 101 WRITTEN
- **Theorem stubs (T19, T20, T21):** 3 WRITTEN
- **Cross-arc synthesis (SCBU):** 1 WRITTEN
- **ED-SC 4.x arc extensions (4.1–4.6):** 6 WRITTEN
- **Substrate-evaluation wave + post-pivot gravity (June 2026):** 12 WRITTEN — GR-I, GR-II, GR-III, the PhilPapers program synthesis ("The Arrow in the Law"), KM-I, KM-II, the One-Field letter, the four substrate-evaluation papers (Continuum, Primes, Charge/B4, Capacity/A1), and the Form-and-Flesh synthesis. *(see the dedicated section above)*
- **ARCHIVED legacy file:** 1 (`Paper_008_KernelArrow.md` — kernel-arrow content migrated to Paper_093 T18)

**Grand total: 123 distinct corpus entities (122 WRITTEN + 1 ARCHIVED).**

**Registry state (per Round-3 final rebuild, 2026-05-14):**
- Paper-specific postulates: 125 (zero WARN-dup name collisions)
- Foundational theorems: 8 (T17, T18, T19, T20, T21, GR1, N1, UR-1)
- Top-3 most-cited upstream papers: Paper_087 (96), Paper_090 (51), Paper_089 (49)
- Orphan papers: 10 (all by-design — 8 capstones, Paper_011 terminus result, Paper_SCBU pending ED-SC 4.x citers though now resolved post-arc-drafting)

---

## Domain ↔ Arc cross-reference

For migration purposes, the canonical arc structure maps to the domain partition as follows:

| Arc | Paper range | Domain | Sub-domains |
|---|---|---|---|
| 1 QM Kinematics | 001–012 | qm-kinematics | foundations, dynamics, observables, measurement |
| 2 Form-Level QFT | 013–024 | qft | kernels, gauge, yang-mills, measurement |
| 3 Gravity | 025–038 | gravity | foundations, mond, cosmology, strong-field, weak-field, galactic |
| 4 Black Holes / Hawking | 039–052 | black-hole | foundations, hawking, remnants, interior, thermodynamics, scattering, information |
| 5 Q-Compute | 053–062 | q-compute | foundations, classification, predictions, architectures, unification, cross-arc |
| 6 Entanglement | 063–072 | entanglement | foundations, capstone, cross-arc, interpretation |
| 7 Soft Matter / NS | 073–086 | soft-matter | foundations, viscoelasticity, regularity, turbulence, rheology, mhd, mobility |
| 8 Wedges / Foundations | 087–097 | cross-domain | foundations, kernels, arrow, methodology, sc-arc |
| Synthesis (program-level) | 098–101 | cross-domain | synthesis, capstone |
| T-stubs | T19/T20/T21 | gravity / cross-domain | theorem-stubs |
| Cross-arc synthesis | SCBU | cross-domain | substrate-cosmology |
| ED-SC 4.x extensions | 4.1–4.6 | cross-domain | sc-arc |
| Substrate-eval + post-pivot gravity | GR-I/II, SE-x, Form-and-Flesh | gravity / substrate-evaluation / position | curvature-emergence, substrate-evaluation, synthesis |

---

## Maintenance discipline

- **Each new paper:** add an entry here when promoted from CANDIDATE → PLANNED → DRAFTING → WRITTEN.
- **Round-numbered audit suffix `_FIXED`:** several files in the corpus carry a `_FIXED` suffix from Round 1 QC. The file paths in this index use the base name (no `_FIXED` suffix) for stability; treat `Paper_NNN_*.md` and `Paper_NNN_*_FIXED.md` as the same entity when both exist.
- **Cross-references in paper §3 sections:** reference papers by paper number (Paper_NNN) for in-corpus citations; by file path for repository-migration purposes.
- **Locked-in numbering:** the 001–101 numbering is stable as of 2026-05-14. T-stubs and SCBU + ED-SC 4.x papers use distinct naming conventions and do not consume numbered slots.
- **Registry source of truth:** for the live citation graph, postulate inventory, and numerical-value registry, see `event-density/papers/Forcing Papers/_RegistryRound2/`.

---

**End of Papers Index.**
