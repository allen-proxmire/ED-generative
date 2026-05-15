# ED Memory — ED-Generative repository

**Last update:** 2026-05-14 (post-Tier-A/B/C reviewer-feedback round; pre-Zenodo posting).

This file is the **durable program-state anchor** for the ED-Generative repository. It tracks structural decisions, conventions, status anchors, and cleanup queues that should travel with the repository across sessions.

---

## Durable facts (canonical as of 2026-05-14)

1. **ED is a 13-Primitive Generative Substrate Ontology.** The 13 primitives (P01–P13) are **posited**, not derived. Canonical enumeration lives in `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1 and is mirrored in `physics-papers/wedges/Paper_087_13Primitives.md` §4 (the publication-grade Paper 087) and per-primitive reference cards in `primitives/P01_*.md` through `P13_*.md`.

2. **The canonical enumeration is P01 = Event-density layer existence (NOT "Chains").** Chains are derived composite structures introduced in P02 (participation), not a canonical primitive. This was the single load-bearing fix from the reviewer's first round.

3. **Intellectual neighborhood: substrate-ontology research program** ('t Hooft's cellular-automaton interpretation, Wolfram's Ruliad / hypergraph rewriting, causal-set program). **ED is NOT in the operational-reconstruction lineage** (Hardy 2001, CDP 2011, Masanes-Müller 2011, Coecke-Kissinger 2017), which derives finite-dimensional QM from operational axioms with closed proofs. Methodological precedent (positing axioms and arguing from downstream reach) runs through Newton, Einstein, Schrödinger, Dirac — but ED's epistemic standing is honestly closer to Wolfram-Ruliad than to closed-proof reconstructions.

4. **Methodology is form-FORCED / value-INHERITED** with a three-tier verdict grammar (Paper_095):
   - **M1 (FORCED-unconditional):** result follows from primitives + standard math, no additional postulates.
   - **M2 (Intermediate Path C):** structural mechanism identified with declared paper-specific postulates; constructive proof OPEN.
   - **M3 (form-FORCED + value-INHERITED):** structural form follows under primitives + postulates; numerical values inherited via empirical matching.

5. **Each paper carries a §2.5 Load-Bearing Step Audit Table** with P/D/A/I labels for every load-bearing step. This is the program's discipline backbone.

6. **The substrate→continuum bridge is DCGT (Paper_073)**, at verdict tier **M3 within an A→regime hydrodynamic-window scale-separation assumption** ($\ell_{ED} \ll R_{cg} \ll L_{flow}$). Because DCGT is upstream of every continuum-level result, its M3-with-regime-caveat status is inherited by every downstream continuum prediction.

7. **SCBU (Substrate-Cosmology Boundary Unification) is offered as the framework's organizing structural hypothesis**, not a closed cross-arc derivation. Paper ED-SC 4.2 explicitly acknowledges that the load-bearing derivation closing the synthesis — **Route A: a substrate-derived $\ell_{V5}(H_0)$** — does not currently close. With Route A open, the six-projection picture is the framework's hypothesis about how cross-domain structure is organized, not a derived result. **Closing Route A is the highest-leverage open derivation in the program.**

8. **The sharpest currently-clean empirical falsifier is BTFR slope-4 with zero intrinsic scatter in deep-MOND** (Paper_031), testable against galaxy-rotation-curve catalogs at present precision (McGaugh-Lelli-Schombert 2016 SPARC: slope 3.95 ± 0.08, scatter ~0.1 dex consistent with observational).

9. **The "no dark matter" claim is qualified to the deep-MOND asymptotic.** Transition-regime per-galaxy SPARC fits are *predicted* by the ECR (Paper_030) but not yet performed in the corpus.

10. **The M-series is archived** and no longer active. See `archive/`.

11. **The academic case is downstream cross-domain reach**, not primitive derivation.

---

## Verdict tier inventory (current state)

| Verdict | Domain |
|---|---|
| M1 (FORCED-unconditional) | None currently. Closing Route A + Routes B + C without additional postulates would upgrade ED-SC 4.x arc-wide to M1 — first cross-arc M1 in the corpus. |
| M2 (Intermediate Path C) | Phase-1 QM-emergence (per per-paper audit tables; corrected Paper_098 2026-05-14); YM mass-gap mechanism; NS-Smoothness; NS-MHD H1/H2/H3 closure; Arc ED-10 curvature emergence. |
| M3 (form-FORCED + value-INHERITED) | DCGT (with A→regime); SCBU + all six ED-SC 4.x projections; Newton's $G$ (T19); $a_0$ (T20); BTFR slope-4 (T21); Area-law form; Hawking spectrum; Class-A wall 140–250 kDa; NS-Q canonical Q ≈ 3.5. |
| A→regime | DCGT scale separation; Acoustic guardrails (Paper_035). |
| A→position | Various composite verdicts (paradox-not-generated, cross-domain echoes, methodological framing claims). |

---

## Round 4 cleanup queue (post-Zenodo, low priority)

These items don't block tonight's Zenodo posting but are worth queueing for future hygiene rounds.

### Cleanup 1: Two parallel position-paper sources

The repo has TWO files functioning as "the 13-primitive position paper":

1. `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md`
2. `physics-papers/wedges/Paper_087_13Primitives.md`

Both are currently synced (post-2026-05-14 sync session) on the canonical enumeration + tradition placement + minimality caveats. But two parallel sources is a divergence risk for any future edit. **Action:** Decide which is canonical; delete or alias the other. The `physics-papers/wedges/Paper_087_13Primitives.md` is the version referenced as "Paper 087" in the Whitepaper §10 reading list and downstream papers' I-rows; that's probably the survivor.

### Cleanup 2: Full audit of remaining PDFs for untracked drift

Spot-checked four PDFs (Whitepaper, Paper_087, Paper_027, Paper_029) for consistency with the corrected framing. **Not spot-checked:** Paper_031, Paper_047, Paper_062, Paper_090, Paper_095, Paper_SCBU. None of their .mds were edited in the 2026-05-14 session, so they're presumed clean — but a full Round 4 audit could verify no untracked drift exists in tradition placement or verdict labels.

### Cleanup 3: Route A closure (substantive research, not writing)

The highest-leverage research closure in the corpus. Closing Route A (substrate-derived $\ell_{V5}(H_0)$) would propagate to:
- Six-way simultaneous M3 → M2 upgrade across the entire ED-SC 4.x arc.
- Tightens SCBU's covariation prediction from "family of falsifiers with un-derived per-projection exponents" to specific scaling laws.
- Closes the load-bearing OPEN flag throughout the Whitepaper + SCBU + ED-SC 4.x arc.

If Routes A + B + C all close without introducing additional postulates, the upgrade reaches M1 arc-wide — the first cross-arc M1 result in the corpus.

### Cleanup 4: Transition-regime SPARC fits

The §5 Gravity arc claim "explains galactic dynamics without dark matter" is currently qualified to the deep-MOND asymptotic. Transition-regime per-galaxy SPARC fits across the catalog are predicted by ECR (Paper_030) but not yet performed in the corpus. **Action item for the empirical-test program:** explicit per-galaxy residual fits across the transition radius. This is a Paper_101-register item, not a writing fix.

### Cleanup 5: T-stub PDFs (T19, T20, T21)

The three theorem stubs are in `theorems/` but have no corresponding PDFs in `to_publish_01/`. If you want them published as standalone Zenodo entries (they're brief and could carry their own DOIs), generate PDFs and add to a follow-up Zenodo batch.

---

## Session accomplishments (2026-05-14)

This session addressed three rounds of reviewer feedback and stabilized the corpus to a publication-ready state:

### Tier A — Mechanical writing fixes (5 items)
1. V5 "same kernel vs same rule-type" honest framing propagated to Whitepaper §3 + position paper §6.1 + Paper_087.
2. "~40 orders of magnitude" rhetoric tightened with Route A caveat across abstracts.
3. "Eight closed research arcs" → "structurally complete research arcs with declared open derivations" across Whitepaper §1, §5, §12.
4. YM "structural-positive on Clay-relevance" → "M2 (Intermediate Path C); mass-gap mechanism identified, closed-proof reduction not claimed."
5. $a_0$ "parameter-free match within ~10%" internal inconsistency in position paper §4.2 resolved.

### Tier B — Verdict label (1 item)
6. DCGT verdict label added to Whitepaper Executive Summary: "M3 within an A→regime hydrodynamic-window scale-separation assumption." Mirror in §5 Soft-Matter arc.

### Tier C — Substantive clarifications (3 items)
7. Position paper §3.10 four-QM-postulates clarified as M2 (not M1) with explicit list of paper-specific postulates declared per Phase-1 paper.
8. T19 audit table expanded to distinguish genuine substrate-counting forcing (inverse-square law, which constants enter $G$) from dimensional-analysis-forcing (exponents in $G$'s decomposition) from value-inheritance (coefficient = 1 via Newton-recovery).
9. §5 galactic-dynamics claim qualified: "deep-MOND asymptotic without dark matter; transition-regime SPARC fits part of ongoing empirical-test program."

### Source-divergence fixes
10. `physics-papers/wedges/Paper_087_13Primitives.md` synced to canonical enumeration (P01 = Event-density layer existence) + tradition placement (substrate-ontology lineage, NOT operational-reconstruction) + minimality caveats (P03 bundling + P11/P13/V1 arrow redundancy).
11. Paper_098 M1→M2 sync (4 locations: abstract, audit table row 2, §3.1 Sector A, appendix arc-inventory table). Previous "FORCED-unconditional (4 postulates)" framing corrected throughout.

### Primitives directory restructure
- Created two-tier structure: canonical `P01_*.md` through `P13_*.md` reference cards at top level + `concepts/` subdirectory preserving the pre-consolidation ontological-concept treatments.
- Added `primitives/README.md` explaining the two-tier structure and citation convention.

### Other artifacts
- `theorems/T19.md` audit table expanded (Item 8).
- `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` extensively edited (Tier A items 2, 5, 7 + Tier C item 6).
- `README.md` (top-level) tradition placement + 40-orders caveat.

---

## Zenodo posting state (2026-05-14, scheduled tonight)

Curated 10-paper set in `to_publish_01/`:

1. ED_WHITEPAPER (front door)
2. Paper_087 (13 primitives position paper)
3. Paper_095 (form-FORCED / value-INHERITED methodology)
4. Paper_090 (V5 cross-chain kernel)
5. Paper_027 (Newton's G)
6. Paper_029 (a₀ = cH₀/2π)
7. Paper_031 (BTFR slope-4 — banner empirical falsifier)
8. Paper_047 (Hawking spectrum)
9. Paper_062 (Cross-domain echo BH ↔ Q-Compute)
10. Paper_SCBU (Substrate-Cosmology Boundary Unification synthesis)

Recommended upload order: same as list above (Whitepaper first as anchor DOI).

Zenodo community: create before uploading; tag all 10 to it. One consolidated announcement after all 10 are posted.

Cross-DOI references between papers can be added in v2 uploads later; not required for v1.

---

## Structural conventions

- **Paper numbering:** Wave-1 papers preserve their original global numbers (#1–#19) for historical continuity. New papers use within-arc filename numbering (Paper_NNN_*.md). T-stubs use T-numbered naming (T19.md, T20.md, T21.md).
- **Cross-references between papers:** use Paper_NNN convention; I-rows in §2.2 of each paper list upstream paper dependencies with load-bearing flags.
- **Primitive references:** use canonical P-codes (P01–P13) as enumerated in the position paper and Paper_087. The two parallel position-paper sources currently agree post-sync; long-term canonical source = TBD per Round 4 Cleanup 1.
- **Status transitions:** CANDIDATE → PLANNED → DRAFTING → WRITTEN, tracked in `PAPERS_INDEX_redo.md`.
- **Verdict labels:** every load-bearing claim gets an M1/M2/M3 or A→regime/A→position label per Paper_095 methodology.

---

## Where the active program state lives

- **Repository (canonical home):** `C:\Users\allen\GitHub\ED Generative\`.
- **Whitepaper (public-facing front door):** `ED_WHITEPAPER.md` at top level.
- **Position paper (canonical foundational statement):** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` AND `physics-papers/wedges/Paper_087_13Primitives.md` (currently both canonical, post-sync; pick one per Round 4 Cleanup 1).
- **Methodology:** `physics-papers/wedges/Paper_095_FormForced_ValueInherited.md`.
- **Falsification register:** `falsifiers/Paper_101_FalsificationRegister.md`.
- **Primitives:** `primitives/` with two-tier structure (P01–P13 canonical + concepts/).
- **T-stubs:** `theorems/T19.md`, `T20.md`, `T21.md`.
- **Scale-correspondence arc:** `scale correspondence/` directory.
- **Predictions / falsifiers:** `predictions/` and `falsifiers/` directories.
- **PDFs for Zenodo:** `to_publish_01/`.

---

## Discipline reminders for future sessions

- **Never let a load-bearing claim go unlabeled.** Every paper's §2.5 audit table should label every load-bearing step P / D / A→regime / A→position / I / D-via-I / OPEN. No "asserted-without-label" rows.
- **Never call ED a closed-proof reconstruction.** ED is in the substrate-ontology research-program lineage (Wolfram / 't Hooft / causal-set). The Hardy/CDP/Masanes-Müller/Coecke-Kissinger tradition is methodological precedent, NOT ED's epistemic-standing equivalent.
- **Never claim "FORCED-unconditional" (M1) for Phase-1 QM-emergence** without rechecking the per-paper audit tables. They explicitly declare paper-specific postulates (P-Motif-Algebra, P-Channel-Orthogonality, etc.). Phase-1 is M2.
- **Never call a substrate result "form-FORCED" without checking whether dimensional analysis is doing the load-bearing work.** Genuine form-forcing requires substrate-counting; if dimensional analysis given the substrate constants is sufficient, label as "D-via-dimensional-analysis" (weaker).
- **Never lead SCBU framing with "one substrate, six projections" as a closed claim.** Route A is OPEN. The six-projection picture is an organizing hypothesis, not a derived result. Reframe as "organizing structural claim" until Route A closes.
- **Never claim "explains galactic dynamics without dark matter" without qualification.** Deep-MOND asymptotic only; transition-regime SPARC fits are pending empirical work.
- **The "necessary-for-current-derivations" minimality claim** is the honest one. P03 bundles three commitments. The arrow of time is supplied jointly by P11 + P13 + V1 retardation (T18); the redundancy question is open.

---

*This file becomes the canonical memory anchor for the ED-Generative repository. Future sessions should read this first to establish context.*
