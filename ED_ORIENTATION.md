# ED Orientation — ED-Generative repository

**Last update:** 2026-05-16 (post-Load-Bearing-Program substrate-research cascade; corpus paper structure updated with cross-arc closures).

This file is the **orientation primer** for the ED-Generative repository. Read this first when arriving at the repo for the first time, returning after a gap, or onboarding an external reader.

---

## What ED is, in one paragraph

**Event Density (ED) is a 13-Primitive Generative Substrate Ontology** — a substrate-ontology research program that posits 13 primitives (P01–P13) and exhibits cross-domain reach across quantum mechanics, gauge theory, gravity, black holes, soft matter, quantum computing limits, entanglement, and foundational kernel theory. The primitives are **posited**, not derived. The empirical case is downstream cross-domain reach.

---

## Intellectual neighborhood

ED's closest neighbors are substrate-ontology research programs:

- **'t Hooft's cellular-automaton interpretation of QM** (discrete substrate posited; quantum mechanics emerges as coarse-grained description)
- **Wolfram's Ruliad / hypergraph-rewriting program** (computational substrate posited; physics emerges as substrate-level exhibits)
- **Causal-set program (Sorkin et al.)** (discrete causal-set substrate posited; continuum spacetime emerges via coarse-graining)

ED is **NOT in the operational-reconstruction lineage** (Hardy 2001, CDP 2011, Masanes-Müller 2011, Coecke-Kissinger 2017). Those programs derive finite-dimensional QM from operational axioms with closed proofs; ED postulates a substrate and exhibits cross-domain reach without a closed substrate→continuum reconstruction theorem.

The methodological precedent for *positing axioms and arguing from downstream reach* runs through Newton, Einstein, Schrödinger, Dirac — but ED's epistemic standing is honestly closer to Wolfram's Ruliad than to closed-proof reconstructions.

---

## Methodology — the program's discipline backbone

ED uses a **form-FORCED / value-INHERITED methodology** with a three-tier verdict grammar (formalized in Paper_095):

| Verdict tier | Meaning |
|---|---|
| **M1 (FORCED-unconditional)** | Result follows from the 13 primitives + standard math alone, no additional paper-specific postulates required. No corpus result currently sits at M1. |
| **M2 (Intermediate Path C)** | Structural mechanism identified with declared paper-specific postulates; closed-proof reduction OPEN. Phase-1 QM-emergence, Yang-Mills mass-gap, NS-Smoothness, NS-MHD closure, Arc ED-10 curvature emergence all sit at M2. |
| **M3 (form-FORCED + value-INHERITED)** | Structural form follows under primitives + postulates; numerical values inherited via empirical matching. DCGT (within A→regime), SCBU + ED-SC 4.x, Newton's G, $a_0$, BTFR slope-4, Hawking spectrum, Class-A wall, NS-Q canonical Q ≈ 3.5 all sit at M3. |

**Each paper carries a §2.5 Load-Bearing Step Audit Table** with explicit P/D/A/I labels for every load-bearing step. No "asserted-without-label" rows. This is the discipline that distinguishes ED from speculative-only substrate-ontology proposals.

---

## Quick read on the load-bearing claims

1. **The substrate exists as a primitive structural layer** (P01: Event-density layer existence). Chains, channels, polarity, bandwidth all live within this layer.

2. **The dynamical content is two memory kernels:** V1 (finite-width retarded, Paper_089) and V5 (cross-chain finite-memory, Paper_090). V1 supplies the kinetic-window content; V5 supplies cross-domain correlations across ~40 orders of magnitude of parameter scales.

3. **The substrate→continuum bridge is DCGT** (Paper_073) at verdict tier **M3 within an A→regime hydrodynamic-window scale-separation assumption**. Every continuum-level corpus result inherits this M3-with-regime-caveat status.

4. **The corpus's most ambitious synthesis is SCBU** (Substrate-Cosmology Boundary Unification): the substrate-cosmology boundary at $R_H = c/H_0$ is offered as the framework's **organizing structural claim**. Six projections of this boundary are proposed in the ED-SC 4.x extension arc (BH horizon, cosmic decoupling, $\xi_{canonical}$, $a_0$, $\mathcal{M}_{crit}$, $Q$ ≈ 3.5). **Route A (substrate-derived $\ell_{V5}(H_0)$) is currently OPEN**; closing it would upgrade the entire arc M3 → M2 simultaneously. Post-2026-05-16: Route A additionally controls Paper_038_5 retroactive M2 → M3 (load-bearing #5 reframing) and Paper_ED_Cos_05 draftability — the single highest-leverage open derivation, with extended cross-arc reach.

5. **The sharpest currently-clean empirical falsifier is BTFR slope-4 with zero intrinsic scatter** in the deep-MOND asymptotic (Paper_031). Testable against galaxy-rotation-curve catalogs at present precision.

---

## Repository layout

| Directory / file | Role |
|---|---|
| `ED_WHITEPAPER.md` | Public-facing front door. Non-technical orientation for new readers. Read first if external. |
| `position-paper/` | Canonical foundational statement of the 13-Primitive Generative System. |
| `physics-papers/` | All Wave-2 papers organized by arc (qm-kinematics, qft, gravity, black-hole, q-compute, entanglement, soft-matter, wedges). |
| `primitives/` | Two-tier structure: canonical P01–P13 reference cards at top level + `concepts/` subdirectory with pre-consolidation ontological-concept treatments. See `primitives/README.md`. |
| `theorems/` | T-numbered theorem stubs (T19, T20, T21 currently). T17, T18, T21, GR1, N1, UR-1 also exist as full papers elsewhere. |
| `scale correspondence/` | ED-SC arc papers (SCBU + ED-SC 4.x). |
| `falsifiers/` | Falsification register (Paper_101). |
| `predictions/` | Active empirical-test program packets (FRAP, QC mass extrapolation, AFM dewetting, acoustic analog tests, etc.). |
| `to_publish_01/` | First Zenodo posting batch (10 PDFs as of 2026-05-14). |
| `archive/` | Superseded artifacts (M-series, older Phase-2 overviews). |

---

## Entry points (in reading order for a cold reader)

1. **`ED_WHITEPAPER.md`** — front door, non-technical, ~50 pages. Names the program, methodology, intellectual neighborhood, falsification program, 100+ paper navigation.

2. **`physics-papers/wedges/Paper_087_13Primitives.md`** — the 13 primitives stated as axioms with operational content per primitive. The methodological discipline at its sharpest.

3. **`physics-papers/wedges/Paper_095_FormForced_ValueInherited.md`** — the form-FORCED / value-INHERITED methodology formalized. This is the program's defense against the "speculative substrate ontology with no constraint discipline" critique.

4. **`physics-papers/wedges/Paper_090_V5Kernel.md`** — the most cross-domain substrate object. V5's job across six domains is the program's signature pattern.

5. **One or two standalone results** depending on interest:
   - Gravity: `physics-papers/gravity/Paper_027_Newtons_G.md` (Newton's $G$ from substrate constants), `Paper_029_a0.md` ($a_0 = cH_0/(2\pi)$), `Paper_031_BTFR.md` (slope-4 BTFR).
   - Black holes: `physics-papers/black-hole/Paper_047_HawkingSpectrum.md`.
   - Q-Compute: `physics-papers/q-compute/Paper_060_Mcrit_Unification.md` (matter-wave/qubit unification).

6. **Synthesis (read after foundations + a result):**
   - `scale correspondence/Paper_SCBU_SubstrateCosmologyBoundary.md` (cross-arc synthesis with Route A OPEN honesty).
   - `scale correspondence/Paper_ED_SC_4_6_UnifiedCrossScale.md` (ED-SC 4.x capstone, four-regime model).
   - `falsifiers/Paper_101_FalsificationRegister.md` (corpus-level empirical-test program).

---

## Terminology discipline

### Use (✓)

- "13 primitives," "Generative Primitives System," "13-Primitive Generative Substrate Ontology"
- "Posited substrate axioms," "conditional derivation from the primitives," "cross-domain reach"
- "Substrate-ontology research program" (Wolfram / 't Hooft / causal-set lineage)
- "Form-FORCED / value-INHERITED" with verdict tiers M1 / M2 / M3
- "Methodological precedent" (Newton, Einstein, Schrödinger, Dirac) — for positing-and-arguing-from-downstream-reach
- "Substrate-cosmology boundary," "Route A," "organizing structural hypothesis" (SCBU framing)
- "M2 (Intermediate Path C)" for Phase-1 QM-emergence and other declared-postulate derivations
- "BTFR slope-4 with zero intrinsic scatter" — the sharpest currently-clean falsifier

### Avoid (✗)

- "Forcing the primitives," "deriving the primitives from a deeper layer," "primitive forcing"
- "ToE," "Theory of Everything," "derivation from nothing"
- "Closed-proof reconstruction" applied to ED at the QM-emergence level (it isn't pure Hardy-class; declares paper-specific postulates)
- "FORCED-unconditional (M1)" for Phase-1 — it's M2 with declared per-paper postulates
- "Operational-postulational tradition" alongside Hardy/CDP/Coecke-Kissinger as ED's lineage — ED is in the substrate-ontology lineage, methodologically precedented by Newton/Einstein/Schrödinger/Dirac
- "One substrate, six projections" as a derived result — Route A is OPEN; it's an organizing schema
- "Substrate gravity explains galactic dynamics without dark matter" unqualified — qualify to deep-MOND asymptotic
- "~40 orders of magnitude" without the Route-A-open caveat for cross-scale parameter relations
- "Eight closed research arcs" — say "structurally complete with declared open derivations"
- "Structural-positive on Clay-relevance" for YM — say "M2 (Intermediate Path C); closed-proof reduction not claimed"

---

## Honest framing of the program's current status

ED has crossed three external-review thresholds (Round 1 / Round 2 / Round 3 audit-then-correct cycles in May 2026). After Round 3:

- The methodology discipline (Paper_095) holds up under hostile review.
- The verdict-tier labeling is honest at executive-summary level for every load-bearing structural commitment.
- The intellectual-neighborhood placement (substrate-ontology, not closed-proof reconstruction) is consistently applied across the canonical front-door documents.
- Specific empirical predictions (BTFR slope-4; Class-A wall 140–250 kDa; Hawking $(\omega/\omega_c)^2$ correction; $a_0 \approx 1.08 \times 10^{-10}$ m/s²) are named and falsifiable.
- OPEN derivations (Route A, Phase-3 GR, YM mass-gap mechanism, NS-Smoothness, $\xi_{canonical}(H_0)$) are named rather than hidden.

The corpus is **structurally complete with declared open derivations** — not a finished theory, not a derivation-from-nothing claim, not equivalent to closed-proof reconstructions. The honest framing is "substrate-ontology research program with methodological hygiene that exceeds the field's norm; load-bearing OPEN derivations explicitly named; cross-domain reach the empirical wedge."

---

## What this repository is NOT

- **Not a Theory of Everything.** The 13 primitives are postulated; not derived from a deeper layer.
- **Not a closed-proof reconstruction.** Phase-1 QM-emergence declares paper-specific postulates; the operational-reconstruction tradition (Hardy, CDP, etc.) is a different research genre.
- **Not a primitive-forcing program.** The M-series pre-pivot attempt at forcing the primitives from upstream M-postulates was identified as circular and archived.
- **Not a derivation of standard physics from nothing.** Standard physics's predictions are excellent within their regimes; ED supplements them with a substrate-level account of *why* the standard results take the forms they do.
- **Not finished.** Route A is open; Phase-3 GR emergence is open; explicit per-galaxy SPARC transition-regime fits are pending. The OPEN flags are honestly named throughout.

---

## Where to find more

- **Memory anchor:** `ED_MEMORY.md` (same directory) — durable program-state facts, verdict-tier inventory, Round 4 cleanup queue, Load-Bearing Program tally (2026-05-16).
- **Load-Bearing Program memo cascade:** `event-density/papers/Load_Bearing_Program_2026_05/` — Wave-3 substrate-research memos for the five load-bearing OPEN derivations (3 closed + 1 negative + 1 reframed to Route A).
- **Reading list:** `ED_WHITEPAPER.md` §10 has the canonical core-reading sequence.
- **Falsification register:** `falsifiers/Paper_101_FalsificationRegister.md`.
- **PAPERS_INDEX:** `PAPERS_INDEX_redo.md` for the canonical paper inventory with status flags.

---

*If you are arriving at this repository for the first time, read `ED_WHITEPAPER.md` next. If you are returning after a gap, read `ED_MEMORY.md` for the durable state + Round 4 cleanup queue. If you are auditing, read `physics-papers/wedges/Paper_095_FormForced_ValueInherited.md` for the methodology discipline and then sample any paper's §2.5 Load-Bearing Step Audit Table to see the discipline in practice.*
