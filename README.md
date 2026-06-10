# Event Density — A Generative Substrate Ontology for Physics

[![DOI](https://zenodo.org/badge/1237222292.svg)](https://doi.org/10.5281/zenodo.20149496)

**Event Density (ED) is a substrate-based reading of physics.** The universe is not a smooth continuum running its equations on top of itself. It is a process of discrete events — and what standard physics has been describing all along is the coarse-grained pattern those events make, seen from far enough away.

Picture a large LED billboard. A wave moves across it — but nothing actually crosses the screen. There is only a grid of discrete lights switching on and off in coordinated ways; the "motion" is a sequence of state-changes in the grid underneath. The pattern is real. The thing moving is not. ED says the universe is built that way: the smooth spacetime of standard physics is the appearance, and the substrate underneath is a network of discrete events updating one at a time, each constrained by every update before it. What we measure as motion, gravity, charge, probability, and time are patterns in how those events relate.

---

## What ED claims — and what it doesn't

ED's claim is not that any single result is proven. It's that one small substrate — thirteen primitives, two kernels — generates the *form* of physical law across quantum mechanics, gauge theory, gravity, black holes, computation, entanglement, and fluids, internally consistent and honestly tiered, without breaking. The evidence isn't one decisive prediction; it's **breadth without contradiction**. A framework spanning this many independent domains has that many independent chances to fail — and it hasn't. That doesn't make it true. It makes it worth a serious look.

And there is a second claim, on a different axis. Beneath the physics, ED takes a position on what its results *mean*: that constants are **global relational facts**, not micro properties; that determinateness is a substrate event — **commitment** — not a given; that the old choice between "things first" and "relations first" is a **false binary**. That is not a confirmed prediction. It is a *category shift* — a claim about the right **ontology** for physics. ED did not derive the constants; it said what *kind of thing* they are, and why a substrate cannot produce them in isolation.

Two consequences make the ontology concrete:

- **Geometry is relational.** Distances and curvatures are relations, not things — so geometry is the natural large-scale expression of a relational substrate. It appears wherever the substrate's relations carry metric-forming structure. Relationality doesn't *force* geometry — most relational structures aren't geometric — it makes geometry *available*.
- **Constants are global relational invariants.** The geometric ones (G, c, Λ) fix how geometric relations couple — to matter and to one another; the field ones (the fine-structure constant, the mass ratios) play the same global-invariant role for matter and field couplings rather than for geometry.

In short: **the breadth is the evidence that ED *works*; the ontology is the claim about what it *is*.**

---

## The framework

ED is a **13-primitive, two-kernel generative substrate ontology**.

*Generative* means every result is derived from the primitives — nothing is smuggled in mid-derivation that the substrate didn't supply. The thirteen primitives are a small fixed list of structural commitments (discrete events, finite reach, finite memory, irreversible commitment, channel structure, participation, and a handful of others). Two memory kernels — **V1** (finite-width retarded) and **V5** (cross-chain finite-memory) — carry the dynamics. Every theorem and prediction is downstream of those.

The methodology is **theorem-first, not equation-first**, and scrupulously tiered. A claim enters the corpus when a proof closes from the primitives without slack — not when the math happens to work in some other frame and gets imported. Where the substrate supplies the *form* of a law but the universe supplies the *number* (H₀, the Planck mass, observed mixing angles), the split is named explicitly: **form-forced, value-inherited**. Open derivations are flagged, not hidden.

---

## What it derives

A non-exhaustive list of standard-physics postulates this corpus derives rather than assumes — form-forced from the substrate, with numerical values inherited where noted:

| Result | Paper |
|---|---|
| Newton's gravitational constant *G* | `Paper_027_Newtons_G` |
| MOND acceleration scale *a₀* | `Paper_029_a0` |
| Baryonic Tully–Fisher relation | `Paper_031_BTFR` |
| Cosmological constant Λ | `Paper_ED_Cos_05_DarkEnergy` |
| BBN light-element abundances | `Paper_ED_Cos_02_BBN` |
| CMB acoustic structure | `Paper_ED_Cos_03_CMBAcoustic` |
| Inflationary spectrum | `Paper_ED_Cos_06_InflationarySpectrum` |
| Baryogenesis (matter–antimatter asymmetry) | `Paper_ED_Baryogenesis` |
| Hawking radiation spectrum | `Paper_047_HawkingSpectrum` |
| Gravitational-wave ringdown structure | `Paper_ED_GW_01_RingdownSpectroscopy` |
| Horizon universalization | `Paper_GR_HorizonUniversalization` |
| Newton recovery / Planck identification | `Paper_GR_NewtonRecovery_PlanckIdentification` |
| Origin of ℏ from substrate primitives | `Paper_RQM_hbar_Origin` |
| Anyon prohibition (spin–statistics) | `Paper_RQM_T3_AnyonProhibition` |
| Four-postulate unification | `Paper_U_FourPostulatesUnification` |

The corpus's sharpest currently-clean falsifier is the **Baryonic Tully–Fisher relation at slope 4 with zero intrinsic scatter** in the deep-MOND regime — testable against present galaxy-rotation-curve catalogs. For the full paper list and per-result verdict tiers, see `PAPERS_INDEX.md`.

---

## The companion book

The popular-companion volume to this research is **[*The Universe Becoming: The Pattern Beneath Physics*](https://www.amazon.com/dp/B0H34MSH87)** — sixteen chapters tracing the same architecture in plain English, no math required. ISBN 979-8-19858-606-2.

---

## Entry points

- **New to ED (plain English):** `ED_Public_Onboarding_LessTechnical.md`, or the companion book above.
- **New to ED (technical):** the position paper — `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` (the 13 primitives) — then `ED_WHITEPAPER.md` (the unified statement of the framework).
- **The ontology / "Facts" paper:** `position-paper/paper_ED_Contrast_First_Ontology.pdf` — ***When Contrast Becomes Fact*** — what physics looks like when contrast is primitive, commitment is determinateness, and constants are global relational facts. This is the foundational layer beneath the physics.
- **Navigating the corpus:** `PAPERS_INDEX.md` (the canonical paper list with status and tiers).
- **AI / Claude sessions:** `ED_ORIENTATION.md` first.

---

## Repository structure

```
position-paper/        Foundational statements: the 13-primitive position paper;
                       the contrast ontology ("Facts") paper.
primitives/            The 13 primitives + load-bearing audit + concept glossary.
physics-papers/        Per-domain derivation papers — gravity, cosmology, black-hole,
                       qm-kinematics, relativistic-qm, qft, entanglement, q-compute,
                       soft-matter, dynamics, wedges.
scale correspondence/  Cross-scale invariants and the substrate–cosmology synthesis.
theorems/              Standalone theorem statements.
falsifiers/            Falsification criteria for the framework.
predictions/           Active empirical-test program (BTFR scatter, a₀ tightening, …).
archive/               Superseded artifacts.
```

Top-level reference documents: `ED_WHITEPAPER.md` (unified statement), `PAPERS_INDEX.md` (corpus index), and the two `ED_Public_Onboarding_*.md` orientations.

---

## What ED is not

ED is **not** a Theory of Everything, **not** a derivation from nothing, and **not** a forcing-from-zero-assumptions program. It is a postulational generative system whose case rests on cross-domain reach and methodological honesty. The thirteen primitives are *posited*, not derived. The constants' values are *inherited*, not computed — and the ontology explains *why* a substrate cannot produce them in isolation. Key derivations remain open and are named as such: the full Einstein field equations, the numerical values of the constants, and a confirmed parameter-free novel prediction. ED's claim is breadth without contradiction plus a defensible ontology — a program worth serious examination, not a finished or confirmed theory.

For the full position statement, see `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md`.
