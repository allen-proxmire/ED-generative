# Event Density - the Generative Substrate Ontology

[![DOI](https://zenodo.org/badge/1237222292.svg)](https://doi.org/10.5281/zenodo.20149496)

# Event Density

**Event Density (ED) is a substrate-based reading of physics.** The universe is not a smooth continuum running its equations on top of itself. It is a process of discrete events — and what standard physics has been describing all along is the coarse-grained pattern those events make when viewed from far enough away.

## The Picture

Picture a large LED billboard. A pattern moves across it — a wave, a face, a word. But there is no actual thing crossing the screen. There is only a grid of discrete lights, switching on and off in coordinated ways. What looks like motion is a sequence of state changes in the grid underneath. The pattern is real. The thing moving is not.

Event Density says the universe is built that way. The smooth spacetime of standard physics — the continuous canvas across which particles move and fields evolve — is the appearance. The substrate underneath is a network of discrete events updating one at a time, with each update constrained by every update before it. What we measure as motion, gravity, charge, probability, time — all of it is patterns in how those events relate.

The major postulates of standard physics — Newton's *G*, the cosmological constant Λ, the Born rule, Heisenberg's uncertainty, Bekenstein-Hawking entropy, the MOND acceleration scale, the arrow of time — are **derived** from the substrate in this work, not assumed. The data physics measures stays where it is. What changes is the floor underneath it.

The popular-companion volume to this research is **[*The Universe Becoming: The Pattern Beneath Physics*](https://www.amazon.com/dp/B0H34MSH87)** — sixteen chapters tracing the same architecture in plain English, no math required. ISBN 979-8-19858-606-2.

---

## The Framework

Event Density is a **13-primitive generative substrate ontology**.

*Generative* means every result in the corpus has to be derived from the primitives — nothing is smuggled in mid-derivation that the substrate didn't already supply. *13 primitives* means the entire architecture rests on a small fixed list of structural commitments: discrete events, finite reach, finite memory, irreversible commitment, channel structure, participation pattern, and a handful of others. Every theorem and prediction is downstream of those.

The methodology is **theorem-first, not equation-first**. A claim enters the corpus when a proof closes from the primitives without slack — not when the math happens to work in some other frame and gets imported. Where the substrate supplies the structural form but the universe supplies the specific numerical value (H₀, the Planck mass, observed mixing angles), the distinction is named explicitly: `form-forced, value-inherited`. Nothing is papered over.

---

### Closed derivations

A non-exhaustive list of postulates of standard physics that this corpus derives rather than assumes:

| Result | Paper |

| Newton's gravitational constant *G* | `Paper_027_Newtons_G.pdf` |
| MOND acceleration scale *a₀* | `Paper_029_a0.pdf` |
| Baryonic Tully-Fisher relation | `Paper_031_BTFR.pdf` |
| Cosmological constant Λ | `Paper_ED_Cos_05_DarkEnergy.pdf` |
| BBN light-element abundances | `Paper_ED_Cos_02_BBN.pdf` |
| CMB acoustic structure | `Paper_ED_Cos_03_CMBAcoustic.pdf` |
| Inflationary spectrum | `Paper_ED_Cos_06_InflationarySpectrum.pdf` |
| Baryogenesis (matter–antimatter asymmetry) | `Paper_ED_Baryogenesis.pdf` |
| Hawking radiation spectrum | `Paper_047_HawkingSpectrum.pdf` |
| Gravitational-wave ringdown structure | `Paper_ED_GW_01_RingdownSpectroscopy.pdf` |
| Horizon universalization | `Paper_GR_HorizonUniversalization.pdf` |
| Newton recovery / Planck identification | `Paper_GR_NewtonRecovery_PlanckIdentification.pdf` |
| Origin of ℏ from substrate primitives | `Paper_RQM_hbar_Origin.pdf` |
| Anyon prohibition (spin-statistics) | `Paper_RQM_T3_AnyonProhibition.pdf` |
| Four-postulate unification | `Paper_U_FourPostulatesUnification.pdf` |

---

### Foundational documents

- **`ED_WHITEPAPER.pdf`** — unified statement of the framework.
- **`Paper_087_13Primitives.pdf`** — the 13 primitives specified.
- **`Paper_090_V5Kernel.pdf`** — the current kernel formulation.
- **`Paper_073_DCGT.pdf`** — methodological posture (*Don't Change the physics; Generate it from the substrate*).
- **`Paper_095_FormForced_ValueInherited.pdf`** — the inheritance taxonomy: which numerical values come from where.
- **`Paper_ED_Postdictions_PassedTests.pdf`** — what the framework has already explained.
- **`Paper_ED_Predictions_Bundle.pdf`** — what it predicts, and what would refute it.

---

## Repository structure

```
position-paper/   The canonical foundational statement of ED.
primitives/      The 13 primitives + load-bearing audit + glossary.
domain-arcs/      Per-domain conditional-derivation papers (the ED Wedge sectors).
cross-domain/   Kernels (V1, V5), arrow of time, ED Combination Rule, cross-scale invariants, multi-domain syntheses.
falsifiers/    Falsification criteria for the framework.
predictions/   Active empirical-test program: Class-A wall, BTFR scatter, a₀ tightening, etc.
archive/       Superseded artifacts: M-series (frozen 2026-05-13), older Phase-2 overviews.
```

## Entry points

- **For new readers / reviewers:** start with `position-paper/ED_Framework_13_Primitive_Generative_System.md`.
- **For new Claude / AI sessions:** read `ED_ORIENTATION.md` first.
- **For navigating the paper corpus:** see `PAPERS_INDEX.md` (canonical 101-candidate list with status).
- **For understanding paper-to-paper dependencies:** see `DEPENDENCY_GRAPH.md`.
- **For program-state context:** see `ED_MEMORY.md` and `ED_ACCOMPLISHMENTS.md`.

## What this repo replaces

`ED-generative` is the post-pivot successor to the `event-density` repository. The `event-density` repo will eventually be marked deprecated. The `ED-primitives` repo (constitutional core, 13 primitives + amendments) remains the slow-changing reference everything else cites.

## Status

- **2026-05-13:** Repository scaffold created. Pivot to Generative Primitives System completed in `event-density`. Migration of 19 Wave-1 Forcing Papers + position paper + M-series archive pending.
- **Next:** populate `position-paper/`, `primitives/`, and Wave-1 papers across `domain-arcs/`. Then resume Wave-2 paper writing directly in this structure.

## Genre

ED is **not** a Theory of Everything, **not** a derivation from nothing, and **not** a forcing-from-zero-assumptions program. It is a postulational generative system whose case rests on cross-domain reach. The repository's organization reflects this: 13 primitives → per-domain conditional derivations → cross-domain invariants → empirical predictions → falsifiers.

For the full position statement, see `position-paper/ED_Framework_13_Primitive_Generative_System.md`.
