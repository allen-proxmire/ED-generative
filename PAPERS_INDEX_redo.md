# Papers Index — Canonical Source of Truth

**Last updated:** 2026-05-13
**Purpose:** Single source of truth for every paper in the ED-Generative repository. Tracks global paper number (historical), title, domain assignment, status, and file location.

**Status enum:**
- **WRITTEN** — paper complete, in repository.
- **DRAFTING** — actively being written.
- **PLANNED** — identified, scheduled, not yet started.
- **CANDIDATE** — on the 101-candidate list but not yet committed to.
- **ARCHIVED** — superseded or retired.
- **SUPERSEDED** — replaced by a later paper or restructured.

---

## Wave-1 Papers (Forcing Papers #1–#19 from `event-density` repo)

These are the first-wave conditional-derivation papers written in the `event-density/papers/Forcing Papers/` folder. Migration to this repository is pending.

| # | Title | Domain | Sub-domain | Status | File path |
|---|---|---|---|---|---|
| 1 | The Participation Measure | qm-kinematics | foundations | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/foundations/01_participation_measure.md` |
| 2 | The Born Rule | qm-kinematics | foundations | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/foundations/02_born_rule.md` |
| 3 | Sesquilinear Inner Product + Tsirelson Bound | qm-kinematics | foundations | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/foundations/03_inner_product_tsirelson.md` |
| 4 | Schrödinger Equation (Stone-theorem route) | qm-kinematics | dynamics | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/dynamics/01_schrodinger_stone.md` |
| 5 | Gauge Fields (Theorem 17) | qft | gauge | WRITTEN (pending migration) | `domain-arcs/qft/gauge/01_gauge_fields_T17.md` |
| 6 | Hamiltonian + Mass Structure | qm-kinematics | observables | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/observables/01_hamiltonian_mass.md` |
| 7 | Dirac Equation + g=2 | qm-kinematics | relativistic | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/relativistic/01_dirac_g2.md` |
| 8 | DCGT Gauge Translation | qft | gauge | WRITTEN (pending migration) | `domain-arcs/qft/gauge/02_DCGT_gauge_translation.md` |
| 9 | Newton's G + a₀ + BTFR + ECR | gravity | foundations | WRITTEN (pending migration) | `domain-arcs/gravity/foundations/01_newton_a0_BTFR.md` |
| 10 | BH Architecture + Hawking Spectrum | black-hole | hawking | WRITTEN (pending migration) | `domain-arcs/black-hole/hawking/01_BH_architecture_hawking.md` |
| 11 | Heisenberg Uncertainty | qm-kinematics | observables | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/observables/02_heisenberg.md` |
| 12 | Momentum Operator | qm-kinematics | dynamics | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/dynamics/02_momentum_operator.md` |
| 13 | Schrödinger thin-participation limit | qm-kinematics | dynamics | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/dynamics/03_schrodinger_thin_limit.md` |
| 14 | Born Rule via Bandwidth Ratio | qm-kinematics | foundations | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/foundations/04_born_via_bandwidth_ratio.md` |
| 15 | Adjacency Kinetic Structure | qm-kinematics | observables | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/observables/03_adjacency_kinetic.md` |
| 16 | Phase-Independence of Bandwidth | qm-kinematics | foundations | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/foundations/05_phase_independence.md` |
| 17 | Four Postulates Unified (synthesis) | qm-kinematics | synthesis | WRITTEN (pending migration) | `domain-arcs/qm-kinematics/synthesis/01_four_postulates_unified.md` |
| 18 | V1 Finite-Width Kernel (Theorem N1) | cross-domain | kernels | WRITTEN (pending migration) | `cross-domain/kernels/V1_finite_width.md` |
| 19 | V1 Retarded Support (Theorem T18) | cross-domain | kernels | WRITTEN (pending migration) | `cross-domain/kernels/V1_retarded_support.md` |

**Wave-1 status:** 19 papers WRITTEN; pending migration into this repository's structure.

---

## Wave-2 Papers (next in queue)

Identified as natural successors to Paper #19. Not yet drafted.

| # | Title | Domain | Sub-domain | Status | Notes |
|---|---|---|---|---|---|
| 20 | V5 Cross-Chain Correlation Kernel | cross-domain | kernels | PLANNED | High priority — cross-scale-unification wedge. Existing material in Arc-D, Arc-E, Arc-Hawking memos. |
| 21 | Memory-Kernel Cascade (N1-E, N2-E, N3-D) | cross-domain | kernels | PLANNED | Inherits retarded support from V1 (Paper #19). |
| 22 | Lindblad Limit | qm-kinematics | measurement | PLANNED | Markovian limit of retarded V1; open-system dynamics. |
| 23 | Kernel Hierarchy Structural Unification | cross-domain | kernels | PLANNED | Synthesis of V1 + V5 + memory-kernel cascade. |

---

## Wave-3+ Candidates (from the 101-candidate list)

The full 101-candidate list identified during the 2026-05-12 corpus mapping spans multiple domains. Candidates here are CANDIDATE-status until promoted to PLANNED / DRAFTING. Realistic completion estimate: ~30–60 papers over the program's lifetime; the 101 is an upper bound, and many candidates will merge, split, or be deprecated on closer inspection.

### qm-kinematics candidates

| Title | Sub-domain | Status |
|---|---|---|
| Berry phase generative derivation | observables | CANDIDATE |
| Aharonov-Bohm phase | observables | CANDIDATE |
| Bloch theorem | dynamics | CANDIDATE |
| Photonic Chern channels + quantized Hall drift | observables | CANDIDATE |
| Rate of Becoming (Hau-Katori-Ye AMO) | dynamics | CANDIDATE |
| Quantum-erasure substrate-level analysis | measurement | CANDIDATE |
| ER=EPR-class entanglement structure | (see entanglement) | CANDIDATE |
| ... (additional Wave-1 candidates not yet allocated) | — | CANDIDATE |

### qft candidates

| Title | Sub-domain | Status |
|---|---|---|
| Renormalization group via DCGT three-regime | renormalization | CANDIDATE |
| ζ-function vacuum-energy derivation | renormalization | CANDIDATE |
| Anomaly content from substrate primitives | anomalies | CANDIDATE |
| LSZ reduction formula from V1 propagator | propagators | CANDIDATE |
| ... | — | CANDIDATE |

### gravity candidates

| Title | Sub-domain | Status |
|---|---|---|
| Curvature emergence (Arc ED-10 closure) | strong-field | CANDIDATE (existing memos in event-density) |
| Galactic rotation curve fits (DR1 sample) | galactic | CANDIDATE |
| Cosmological-arrow synthesis | cosmological | CANDIDATE |
| Weak-lensing activity dependence | galactic | CANDIDATE |
| Merger-lag prediction | galactic | CANDIDATE |
| ... | — | CANDIDATE |

### soft-matter candidates

| Title | Sub-domain | Status |
|---|---|---|
| Maxwell relaxation in polymer melts (Arc D paper) | viscoelasticity | CANDIDATE (existing memos) |
| Universal mobility law publication-grade | mobility | CANDIDATE (FRAP-validated) |
| Navier-Stokes structural smoothness (Intermediate Path C) | fluid-mechanics | CANDIDATE (NS Synthesis Paper exists) |
| MHD kinematic-coupling structural analysis | fluid-mechanics | CANDIDATE |
| Yang-Mills mass-gap structural | (cross-domain?) | CANDIDATE |
| ... | — | CANDIDATE |

### black-hole candidates

| Title | Sub-domain | Status |
|---|---|---|
| BH information paradox resolution (publication-grade) | information | CANDIDATE (paper exists in event-density) |
| Page curve from V5 bandwidth-budget | hawking | CANDIDATE |
| Greybody factors substrate-level | hawking | CANDIDATE |
| Planck-mass remnant cosmological abundance | remnants | CANDIDATE (H-9 memo exists) |
| Trans-Planckian resolution paper | hawking | CANDIDATE |
| ... | — | CANDIDATE |

### q-compute candidates

| Title | Sub-domain | Status |
|---|---|---|
| Class-A multiplicity wall publication-grade | multiplicity | CANDIDATE (Q-COMPUTE foundations exists) |
| Class-B exponential gap-suppression | multiplicity | CANDIDATE |
| Class-C correlation-budget plateau | multiplicity | CANDIDATE |
| Platform-specific bridges (SC qubits, trapped ions, etc.) | platforms | CANDIDATE |
| ... | — | CANDIDATE |

### entanglement candidates

| Title | Sub-domain | Status |
|---|---|---|
| Arc E synthesis paper | — | CANDIDATE (7 memos exist in event-density) |
| Monogamy from cross-chain bandwidth | — | CANDIDATE |
| Bipartite entanglement structural derivation | — | CANDIDATE |
| ... | — | CANDIDATE |

### cross-domain candidates

| Title | Sub-domain | Status |
|---|---|---|
| ED Combination Rule publication-grade | ED_combination_rule | CANDIDATE |
| Cross-scale invariants synthesis | cross_scale_invariants | CANDIDATE |
| Kernel-level arrow of time publication-grade | arrow_of_time | CANDIDATE |
| V5 cross-scale unification publication-grade | kernels | CANDIDATE |
| ED-QFT Overview (unified position paper) | synthesis_papers | CANDIDATE (existing in event-density) |
| ... | — | CANDIDATE |

---

## Total counts (2026-05-13)

- **WRITTEN:** 19 (Wave-1 Forcing Papers; pending migration)
- **PLANNED:** 4 (Wave-2 immediate-queue)
- **CANDIDATE:** ~78 (remaining from 101-list, allocated to domains)
- **ARCHIVED:** 5 (M-series: M-1, M-2, M-3, M-4, M-Omnibus) + Meta-Paper M0 drafts

The 101-candidate list is an upper bound. Realistic program completion: 30–60 papers depending on which candidates merge, prove redundant, or fall out of scope.

---

## Maintenance discipline

- **Each new paper:** add an entry here when promoted from CANDIDATE → PLANNED → DRAFTING → WRITTEN.
- **Cross-references in paper §3.0 sections:** reference papers by domain-local filename, not global #.
- **Global # is historical:** preserved here for paper-trail continuity with the `event-density` Forcing Papers folder. New papers (Wave-2+) get a global # if they're sequenced (Paper #20, #21, etc.); alternatively, new Wave-2+ papers can be referred to by their domain-local filename only and the global # field left blank.
