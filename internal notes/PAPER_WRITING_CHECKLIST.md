# ED Paper-Writing Checklist

**Purpose:** Pre-draft and pre-submission checklist for ED corpus papers. Apply BEFORE finalizing the audit table and BEFORE handing to a reviewer. The discipline here is the upstream intervention that prevents the chronic Paper_095 §2.3 conflations caught downstream across all four review rounds (see ED_MEMORY.md).

**Last update:** 2026-05-16 (post-Paper_ED_GW_00 Tier-A correction; word-count discipline elevated to §0).

---

## §0 STYLE + LENGTH DISCIPLINE (BLOCKING — RUN BEFORE DRAFTING)

ED papers come in two structural densities. **Pick one before drafting, name the word-count target in the header note, and re-check at every major section.**

### Wave-3 generative papers (default)
- **Target: 1,500–3,500 words.**
- **Hard cap: 5,000 words.** Going over means the paper is not Wave-3 — either compress or relabel as Wave-2.
- Tight architectural style. No tutorial recaps, no extended disclaimers, no re-derivation of upstream results.
- Examples: T1–T10, U-series, EDSC arc, Pred_ papers, Paper_005.5 (Double-Slit, 2.5k words), Paper_ED_CCC (revised, 2.3k), Paper_ED_GW_00 (revised, 2.5k).

### Wave-2 generative papers (exceptional)
- **Target: 3,000–8,000 words.**
- Full-length derivation with extended preamble, multi-section §3, narrative phenomenology recap.
- Use only when derivation genuinely requires extended treatment: anchor papers opening a new arc; foundational position papers.
- Examples: Paper_005, Paper_010, Paper_063.

### Anti-pattern to guard against
Across the last three Wave-3 drafts (Paper_ED_CCC, Paper_ED_Baryogenesis, Paper_ED_GW_00), the first-draft word count consistently landed at **~4,500–5,000 words** despite Wave-3 framing — each requiring mechanical Tier-A compression. The recurring drift sources:

1. **Abstract bloat** — listing every structural element with multi-sentence sub-items. Target: ~150–200 words; one-sentence framing + inline list + form/value split + verdict + F1.
2. **§3 sub-section over-explanation** — paragraphs explaining well-known GR / QM machinery before stating the substrate-side reading. Wave-3 cites upstream / external sources rather than re-explaining.
3. **§6 Position Statement repetition** — re-stating Preamble + Abstract content. Two paragraphs max.
4. **Audit table inheritance bloat** — listing every upstream paper as a separate row. Fold inheritance into a single block-row with notes-column breakdown (CCC pattern, rows 1–2).
5. **Falsifier list inflation** — 5–7 falsifiers where 3–4 suffice. Drop weakly-operationalizable falsifiers; fold redundant evidence-channel falsifiers into a single F-line with sub-clauses.

### Pre-draft enforcement

Before opening the file: **write the word-count target in your scratch notes**. Set it at 2,500 words for a typical Wave-3 generative paper unless the structure forces longer. Recheck at each section: Abstract ≤ 200; §1 ≤ 200; §3 total ≤ 1,500; §4 audit table ≤ 20 rows; §5 falsifiers 3–4; §6 Position Statement ≤ 300. If any section exceeds its allocation, compress before continuing.

**This discipline is BLOCKING** — verbose first drafts that require mechanical compression are a recurring tax. Catching at draft time saves the reviewer round.

---

## §1 Required scaffolding (every paper)

Mechanical, but missed in 30+ of 40 corpus papers across the audit gauntlet. Catch upstream:

1. **Header block:** Series · Status · Date · Verdict per Paper_095 · Anchors (upstream papers).
2. **Preamble — "What This Paper Does NOT Claim"** (numbered, 4–6 items). Items 4–5 paper-specific: name what is NOT derived; specify INHERITED vs FORCED breakdown. For EDSC/GRSC papers, add Route A OPEN as item 6. For Pred_ papers, add PROVISIONAL classification flag.
3. **Labeled Abstract** (4–6 sentences). Must state: (a) structural result, (b) postulates / regime, (c) verdict tier per Paper_095, (d) sharpest falsifier F#. NOT optional. §1 "Statement of Result" is not an abstract — both are required.
4. **§1 Statement of Result.** Architectural summary; substrate mechanism; FORM/VALUE breakdown.
5. **§2 Primitive Inputs + Upstream Dependencies.** Compact lists. Only primitives actually used; only upstream papers actually required. Paper-specific postulates declared in §2.3 with substrate-derivation OPEN flag if applicable.
6. **§2.5 Audit Table** (Wave-2) or **§4 Audit Table** (Wave-3). Every load-bearing step labeled per §3 below. No A (asserted) rows. Final row = verdict A→position framing claim.
7. **§3 Derivation** (Wave-3) or **§3 Substrate-Level Construction** (Wave-2). Tight subsections. Minimal math.
8. **§4 / §5 Falsification Criteria.** 3–5 sharp falsifiers; F1 sharpest. Must be ED-specific, not generic-QM falsifiers (refuting Schrödinger or Born globally is not a paper falsifier).
9. **§5 / §6 Position Statement** (NOT "Rewrite Note" — chronic naming violation across the corpus). Two paragraphs max. First: substrate-ontology lineage citation ('t Hooft / Wolfram / causal-set), explicit disavowal of operational-reconstruction lineage (Hardy / CDP / Coecke-Kissinger). Second: verdict tier with audit-table content reconciliation.
10. **End marker:** `**End Paper NNN.**` consistently.

---

## §2 Per-row labeling discipline (Paper_095 §2.3)

The chronic discipline failure across 22 of 40 reviewed papers. Internalize before drafting the audit table.

### Labels:
- **P** — postulate / definition / standard-form construction.
- **A** — analogy / regime / position. Includes `A→position` (Paper_095 §3.3 line 77, for framing-claim verdict rows) and `A→regime` (for hydrodynamic-window / scale-separation regimes).
- **I** — inherited / empirical / standard math / standard textbook result.
- **D** — actual derivation; new substrate-graph content not reducible to upstream papers.
- **D-via-I** — application of standard machinery to substrate-adapted content under declared postulates; composition of upstream inheritances under substrate identification.
- **OPEN** — flagged for future work; not claimed.

### Named-by-§2.3 P examples (always P, never D):
- Writing down the Klein-Gordon equation
- Writing down the Schrödinger equation
- Writing down the Lindblad form
- Writing down the tensor product $\Psi^A \otimes \Psi^B$
- Writing down the momentum operator $\hat p = -i\hbar\nabla$
- Writing down the Heisenberg / Robertson inequality
- Writing down the geodesic equation
- Writing down the Regge-Wheeler potential
- Writing down the Ricci-of-Visser computation
- Writing down minimal coupling
- Definitional naming conventions for upstream conjunctions (e.g., P-EDThreshold-Collapse = P12 + P11 + Paper_005)

### Always-I (standard textbook results, not ED-derived):
- Stone's theorem application
- Polar decomposition
- Tsirelson bound (Cirelson 1980)
- Bekenstein-Hawking $T = \kappa/(2\pi)$
- Bensoussan-Lions-Papanicolaou two-scale homogenization (1978)
- Chern 1946 integer-bundle quantization
- Visser/Unruh analogue gravity geometry
- Robertson inequality (1929)
- Dimensional rearrangement (e.g., $\ell_{ED} = \ell_P$ from $G, \hbar, c$)
- Path-difference geometry (Born–Wolf wave optics)
- Standard decoherence visibility-vs-coupling phenomenology

### Two rules of thumb (Claude B's distillation):

1. **"Do I cite a specific substrate-graph computation or argument that doesn't reduce to upstream papers?"**
   - Yes → **D-via-I** (composition under substrate identification).
   - No → **I** (pure inheritance).

2. **"If I removed the substrate-vocabulary and translated this row to standard physics, would it still hold?"**
   - Yes → **I** (substrate vocabulary is relabeling, not new content).
   - No → **D-via-I** (substrate-adaptation worth flagging).

3. **"Did I introduce genuinely new substrate-graph content here?"**
   - Yes → **D** (rare; most "substantive" rows are actually D-via-I composition).
   - No → **D-via-I** at most.

### Anti-pattern — "substantive substrate-side composition" labeled D:
This is the single most common §2.3 violation. **Composition of two inherited results is D-via-I, not D**, unless the substrate-adaptation itself introduces new substrate-graph content. "Substantive composition" is not enough to elevate to D. Writing $|P_A + P_B|^2$ is standard Born application; identifying $\pi_K$ as the substrate phase carrier is identification, not derivation; relabeling V5 coupling as "ED injection" is identification, not derivation.

---

## §3 Verdict-tier discipline

### M1 (FORCED-unconditional)
Primitives + standard math, no extra postulates. **Audit table contains genuine D row(s) traceable to primitives alone.** Examples: T1 SpinStatistics (D=3+1 forces two statistics classes), T2 Cl(3,1) frame uniqueness, T3 Anyon prohibition.

### M2 (Intermediate Path C)
Substrate mechanism identified; declared paper-specific postulates; constructive derivation OPEN. **Audit table has at least one P-row (paper-specific postulate) marked OPEN or D-via-I composition.** Examples: U_FourPostulatesUnification (compositional synthesis with per-theorem postulates OPEN); GR_Lambda_V1 (V1 reframing; observed value OPEN); RQM_GRH_D1 (P-Gauge declared, substrate-derivation OPEN).

### M3 (form-FORCED + value-INHERITED)
Structural form follows under primitives + postulates with at least one D or D-via-I content row; numerical values inherited. **OR** form-IDENTIFIED + value-INHERITED if zero pure-D rows (the audit table is composition + identification only). Examples: Newton's $G$, $a_0$, BTFR slope-4, Hawking spectrum (genuine D rows present); Paper_005.5 Double-Slit (zero D rows; form-IDENTIFIED).

### Verdict-tier consistency check (5 anchor points):
Verdict tier MUST be identical across:
1. Status line (top of paper)
2. Abstract
3. §1 Statement of Result
4. Audit-table verdict row (final row, A→position framing)
5. §6 Position Statement final line

Verdict-tier drift across these 5 points is the second most common Tier-A bug across the corpus.

---

## §4 FORM-FORCED vs form-IDENTIFIED vs form-COMPOSED vs form-CONSISTENT

Pre-submission check: search the paper for "FORM-FORCED" or "form-FORCED" in §1 and §6.

**Rule:** "FORM-FORCED" requires at least one pure-D row in the audit table. If zero pure-D rows, downgrade:

- **form-IDENTIFIED** — substrate identification of an inherited structure (e.g., identification of BHPT background as V1-acoustic; identification of $U(1)$-bundle as rule-type bundle).
- **form-COMPOSED** — compositional synthesis of inherited results (e.g., U_FourPostulatesUnification synthesizing the four QM postulates from sixteen Phase-1 theorems).
- **form-CONSISTENT** — consistency-with-regime under declared scale-separation or A→regime conditions (e.g., DCGT under hydrodynamic window; thin-participation expansion).

Pick the contextually-appropriate replacement. Add brief audit note: "(no D rows in audit table; downgraded from FORM-FORCED per Paper_095 §2.3)."

---

## §5 Title-vs-body consistency

Pre-submission check: does the title's framing words match what the body delivers?

- "FORM-FORCED Derivation of X" → only if audit has D row backing.
- "Closed-Proof Y" → almost never; ED is not in the closed-proof reconstruction lineage.
- "Compositional / Substrate-Identification / Provisional" → fine and honest if matches body.
- "Structural Identification of X" → safe default for identification papers.

If body content is honestly compositional / identification / M2-level but title claims "FORM-FORCED" or "Derivation," soften the title before submitting.

---

## §6 Anti-overclaims to guard against (corpus-specific)

Lessons from four review rounds:

- **Never** "Phase-1 closes at FORCED-unconditional level" — Hardy-class language; ED disavows.
- **Never** "single substrate, six projections" as derived result — Route A is OPEN; SCBU is organizing hypothesis.
- **Never** "explains galactic dynamics without dark matter" without deep-MOND qualifier — transition-regime SPARC fits OPEN.
- **Never** "closed-proof reconstruction" applied to ED — substrate-ontology lineage, not Hardy / CDP / Coecke-Kissinger.
- **Never** "FORCED-unconditional (M1)" for Phase-1 QM-emergence — declares paper-specific postulates per per-paper audits.
- **Never** "substrate gravity explains Λ smallness" — V1 reframes; smallness OPEN; naïve cutoff fails by ~10⁶⁰.
- **Never** label dimensional rearrangement (e.g., $\ell_{ED} = \ell_P$, $a_0 = cH_0/(2\pi)$) as D — it is I.
- **Never** label a definitional naming convention (e.g., P-EDThreshold-Collapse = P12 + P11 + Paper_005) as D-via-I — it is P.
- **Never** label tautological partitioning (e.g., S1/S2/S3 trichotomy by construction) as D — it is D-via-I with "partition by construction" note.
- **Never** label a textbook result (Bekenstein-Hawking, Tsirelson, Visser, Chern, Robertson) as D-via-I — it is I.

---

## §7 Pred_ paper specific (additional checks)

Pred_ papers are subject to the BTFR-slope-4 standard: must FORCE at least one number, bound, or scaling exponent. If the paper inherits every numerical magnitude AND every functional form coefficient AND has no observable that separates ED from competing explanations (CDM-with-feedback, standard astrophysical), flag **PROVISIONAL Pred_ classification** in:
1. Preamble item 4 or 5
2. Abstract opening
3. §1
4. Audit verdict row
5. Status line

Do not drop Pred_ from the filename (renaming would lose the prediction-program reference); flag PROVISIONAL throughout.

---

## §8 Substrate-ontology lineage citation (every paper)

Required in:
1. Preamble item 2 (one sentence disavowing operational-reconstruction lineage).
2. §6 Position Statement (full citation paragraph).

Standard citation: *"This paper sits within the substrate-ontology research-program lineage ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED)."*

For papers in the QM-emergence arc (U-series, FourPostulatesUnification, etc.) that are at risk of being read as Hardy-class reconstructions: add explicit second-paragraph disavowal in §6.

---

## §9 Pre-submission self-check (5 minutes per paper)

Before sending to reviewer:

1. □ Header has Series, Status, Date, Verdict, Anchors.
2. □ Preamble present, numbered, 4–6 items, items 4–5 paper-specific.
3. □ Abstract present, labeled, cites Paper_095 verdict tier and F#.
4. □ §1 Statement of Result present with FORM/VALUE breakdown.
5. □ §2 lists primitives invoked + upstream dependencies + paper-specific postulates with OPEN flags.
6. □ Audit table: every row labeled; no A rows except verdict-framing A→position; final row = verdict A→position.
7. □ Audit table: no D row that should be D-via-I or I per §2 rules of thumb.
8. □ Audit table: no D-via-I row that should be P (definitional naming convention) or I (textbook result).
9. □ Verdict tier consistent across 5 anchor points.
10. □ "FORM-FORCED" claims backed by ≥1 pure-D row in audit; else downgraded to form-IDENTIFIED / COMPOSED / CONSISTENT.
11. □ Title doesn't claim more than body delivers.
12. □ §6 titled "Position Statement" (NOT "Rewrite Note").
13. □ Substrate-ontology lineage citation present in §6.
14. □ End marker present.
15. □ For Wave-3: under 5000 words.
16. □ For EDSC/GRSC: Route A OPEN flag in Preamble item 6.
17. □ For Pred_: PROVISIONAL flag at all 5 anchor points.
18. □ Falsifiers are ED-specific, not generic-QM / generic-GR / generic-textbook falsifiers.

---

## §10 Why this checklist exists

Across four review rounds covering 40 papers, the same five discipline failures recurred:

1. **Standard-form constructions labeled D** when Paper_095 §2.3 names them as P (Schrödinger, KG, momentum operator, Heisenberg, geodesic, Regge-Wheeler, Ricci-of-Visser).
2. **Composition of inherited results labeled D** when it should be D-via-I (Born rule applied to V1-propagated amplitude; T7+T8 commutator structure; Tsirelson bound from sesquilinear inner product).
3. **"FORM-FORCED" prose claims with zero D rows in the audit** (22 of 40 papers across the corpus before mechanical sweep).
4. **Verdict-tier drift** across status line / abstract / §1 / audit / §6 / final line (4 papers in last sweep alone).
5. **§6 titled "Rewrite Note"** instead of "Position Statement" (40 of 40 papers in the missing-36 batches).

Claude B's verdict at the end of round 3: *"The Paper_095 discipline is written but not internalized at draft time. The intervention point is upstream — a pre-draft Paper_095 checklist that authors run before assembling the audit table — not downstream review."*

This file is that checklist. Run it before you submit.

---

*End PAPER_WRITING_CHECKLIST.*
