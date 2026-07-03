# Grown, Not Installed: An Emergent Decoupling Boundary Reproduces Exact Channel-Zero

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (determinability-boundary robustness)
**Status:** Publication draft (short). Empirical coding experiment bridging two certified substrate simulators. Companion to "Common Cause, Not Channel" (the A1 capacity result). Standalone; cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative) — substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **No new primitive or postulate is introduced.** This paper wires together two already-existing, already-tested pieces of the corpus: the bandwidth primitive (P04) and a dynamical rule for it that a separate gravity-sector arc already built and validated. Nothing new is added to the substrate's rulebook.
3. **This is a single construction, not a sweep.** One grid size, one coupling strength, one way of combining two neighboring bandwidth values into an edge strength, and a small number of trials. The qualitative result is not a close call, but it has not been stress-tested across parameter regimes.
4. **The admissibility of the underlying dynamical rule is not re-derived here.** Whether a bandwidth-collapse dynamics is fully consistent with the rest of ED's primitives was audited in the gravity-sector arc that built it; this paper inherits that audit rather than repeating it.
5. **No claim about black holes, cosmology, or any physical horizon specifically.** This is a test of the substrate's own internal consistency: can a cutoff that is normally installed by hand instead be grown by the substrate's own dynamics, and does it behave the same way once grown? It does not derive any astrophysical prediction.

---

## Abstract

Event Density's certified information-flow substrate can express a perfect information cutoff between two regions, but until now that cutoff has always been an installed input: a flag set by hand before a run starts, never a consequence of the substrate's own dynamics. This leaves a real question open, because physical horizons (a black hole's, say) are not installed, they form. This paper tests whether the substrate can grow a genuine cutoff on its own. We take a bandwidth-collapse rule from a separate, already-validated part of the program (a rule that correctly reproduces Newtonian gravity, black-hole horizons, and Hawking-type scaling elsewhere in the corpus) and use its output, a region where a local capacity value drains to zero, to automatically decide which connections in the information-flow substrate should be severed, rather than deciding by hand. We then run the same coding-and-decoding test used to certify the installed cutoff: plant a message on one side, and try to recover it on the other. A first construction attempt (combining each connection's two endpoint capacities by averaging them) leaves every boundary connection technically intact and produces a large, spurious information leak (0.8-1.1 bits); this is diagnosed directly (all 40 boundary connections are found still "open") and traced to the averaging choice itself. Combining endpoint capacities by their **minimum** instead (a connection is only as good as its weaker end) seals every boundary connection, and the leak disappears entirely: information recovered across the grown boundary matches the same near-zero, noise-only signature as the installed one, while independently confirming that real, live activity is still happening on both sides. **A cutoff the substrate grows on its own behaves exactly like one installed by hand.** This is a genuine result, not a foregone one: the note that first posed this question predicted the opposite outcome, that a grown cutoff would likely be "soft," leaking some information rather than none.

---

## 1. Introduction

The certified ED information-flow substrate (used throughout the substrate-evaluation arc, see the companion paper "Common Cause, Not Channel") can hold two regions in a state of total mutual isolation: nothing that happens in one region can be detected in the other, at any level of encoding sophistication. Until now, that isolation has always been an **installed** fact, a connection flagged "cut" before the simulation starts, never touched again. That is a reasonable way to build a controlled test, but it leaves open whether the substrate's own rules can ever *produce* such a cutoff on their own, the way a real black-hole horizon forms out of collapsing matter rather than being drawn onto spacetime by hand.

A prior foundations note examined this question directly and found a structural reason to expect difficulty: the substrate's ordinary update rule changes only the *state* of a point, never the *connections* between points, so nothing in the ordinary rule set can ever create or remove a cutoff. The one route that note identified as potentially capable of a genuine cutoff is a **capacity-collapse** mechanism: if the bandwidth of a connection, a primitive quantity every connection already carries, were allowed to drain toward zero, that connection could be treated as effectively severed once it got there. But building bandwidth-*dynamics* (a rule for how bandwidth changes over time) was outside that note's scope, and it explicitly flagged the likely outcome as a "soft wall," a connection that gets weak but probably not exactly, perfectly zero.

This paper builds and tests that missing piece, by borrowing it. A separate line of this research program, aimed at reproducing gravity, already built and validated exactly this kind of bandwidth-collapse rule: bandwidth diffuses between neighbors and drains wherever matter accumulates, and the resulting drained-to-zero regions have already been shown, elsewhere in the corpus, to correctly reproduce the Newtonian gravitational field equation, a finite-size horizon, and the right scaling behavior for horizon area and temperature. That rule is reused here unmodified, its own validation is not repeated. What is new here is connecting its output to the information-flow substrate's test of isolation.

---

## 2. Method

**Step one: grow a cutoff region.** The bandwidth-collapse rule is run on a grid to a steady state, under strong enough matter-like coupling that a finite region's bandwidth drains all the way to zero, a self-contained "horizon" surrounded by ordinary, nonzero bandwidth everywhere else.

**Step two: build the information-flow substrate on top of it.** The grid is treated as a network of directly-neighboring points, each pair of neighbors forming one connection. Each connection is assigned a strength equal to **the smaller of its two endpoints' bandwidth values** (a connection can only be as strong as its weakest participant, the same logic as a chain being only as strong as its weakest link). Any connection whose strength falls to (essentially) zero is marked cut. Because the grown horizon's bandwidth is already at zero, every connection that touches it inherits that zero and is marked cut automatically, with no separate, by-hand decision involved.

**Step three: run the same isolation test used elsewhere in the corpus.** A message (one of several possible values) is planted inside the grown cutoff region. The substrate is evolved forward under its ordinary rules. Two readout regions are checked for any trace of the planted message: one just outside the cutoff boundary, one far away as a control. If the message can be recovered from either readout, the cutoff leaks; if not, it holds.

**Regime tested.** One grid size (36-by-36), one coupling strength (chosen to produce a clean, medium-sized cutoff region of about 80 points), a small number of trials per message-alphabet size (60 trials, alphabets of size 2 and 4). This is a first-pass scope, stated honestly, not a high-precision or exhaustive sweep; see §5.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated; certified substrate | P / I | Paper_087; certified information-flow substrate (companion paper) |
| Bandwidth-collapse rule and its horizon-forming behavior | I | A separate, already-validated gravity-sector construction; reused unmodified |
| Connection strength = minimum of the two endpoints' bandwidth | **D (this paper's construction choice)** | §3 — a first attempt using the average instead was shown to be wrong (§3.1) |
| Grown cutoff produces two independently-active, mutually-undetectable regions | **measured** | §3.2 — confirmed by direct check, not inferred |
| Grown cutoff reproduces the installed cutoff's isolation signature | **measured** | §3.2 |
| A dynamically-grown cutoff is possible in principle (not just installed) | **D** | §4 |

All steps P, I, D, or measured. No asserted rows.

---

## 3. Results

### 3.1 A construction mistake, caught before trusting any result

The first attempt combined each connection's two endpoint bandwidth values by **averaging** them. This turned out to be the wrong choice: a point right at the edge of the grown cutoff (bandwidth at zero) sitting next to an ordinary neighboring point (bandwidth well above zero) produces a moderate *average*, not a value anywhere near zero, so none of the connections crossing the cutoff's boundary were actually marked cut. A direct check confirmed this exactly: all 40 connections bridging the cutoff region to its surroundings were still open. Running the isolation test on this flawed construction produced a large, clearly wrong result, a strong, repeatable "leak" of 0.8 to 1.1 bits, far above the noise floor.

This was diagnosed, not brushed past: because a connection should only be as strong as its weaker end, the fix was to combine the two endpoint bandwidths by taking their **minimum** rather than their average. Rechecking the same 40 boundary connections after this fix found all of them correctly sealed.

### 3.2 The corrected result: exact isolation

With the corrected construction, the same message-recovery test was rerun. The recovered signal from just outside the cutoff, and from the far-away control region, both came back at the noise floor, the same near-zero, no-real-signal reading as when a cutoff is installed by hand rather than grown.

This was checked directly rather than simply reported as a number. Two things were confirmed: first, that the region inside the cutoff and the region just outside it are genuinely in separate, mutually-unreachable groups once the cutoff forms, not merely weakly connected; second, that real activity, dozens of state changes, was still happening independently on both sides during the test, so the "no signal recovered" result reflects true isolation, not simply nothing happening anywhere. Changing which message was planted inside the cutoff, across independent trials, produced **no detectable difference at all** in what could be read from outside, at any level of precision checked.

---

## 4. What It Means

**The substrate can grow a real cutoff, not just have one installed.** The one route to a genuine, structural cutoff that the original foundations note identified, a connection's bandwidth draining to zero rather than a person flipping a flag, works, once the natural "weakest link" rule is used to translate a continuous, gradually-draining quantity into a clean, complete cut. This is not a trivial or guaranteed outcome: the note that first posed the question predicted the opposite, that a grown cutoff would probably be "soft," letting a little information through rather than none. It does not. There is no contradiction with that note's caution, only a sharpening of it: the softness that note anticipated belongs to a *different*, weaker candidate mechanism (a resistance-like barrier built from ordinary state values, which the note had already correctly identified as insufficient on its own), not to the genuine bandwidth-collapse mechanism tested here.

**Why this matters for the larger program.** A theory whose only cutoffs are ones a person draws in by hand is a weaker candidate for explaining real, physically-forming boundaries like black-hole horizons than a theory whose cutoffs can grow from its own rules. This result moves ED from the first kind of theory toward the second, at least for the specific mechanism tested.

---

## 5. Limitations (honest)

- **One construction, not a sweep.** A single grid size, coupling strength, and cutoff threshold; the qualitative result (clean isolation versus a large leak) is not a close call, but no systematic search across parameter regimes has been run.
- **One way of combining endpoint bandwidths.** The minimum was chosen because the average was shown to fail, and the minimum matches the underlying rule's own logic (a connection's strength is written in terms that vanish if either participant's contribution vanishes). Other reasonable combining rules have not been tried.
- **The underlying dynamical rule's own validity is inherited, not re-examined.** This paper does not re-derive or re-audit whether the bandwidth-collapse rule itself is a legitimate extension of the substrate's primitives; that question belongs to the gravity-sector arc that built it.
- **Small trial counts.** Sixty trials per message-alphabet size, two alphabet sizes. Enough to distinguish a large leak from a clean zero, not enough for a precision estimate of any residual small leak.

---

## 6. Falsification Criteria

### 6.1 A leak survives the corrected construction

**Falsifier sentence:** *A demonstration that the corrected (minimum-based) construction still allows a detectable, repeatable information leak across the grown cutoff, at a level clearly above the noise floor, would falsify the exact-isolation result of this paper.*

### 6.2 The isolation is an artifact of no activity

**Falsifier sentence:** *A demonstration that the regions on either side of the grown cutoff are not, in fact, independently active during the test (i.e., that the "no leak" reading is simply "nothing is happening" rather than "two active regions with no shared information") would undercut the interpretation in §3.2, though not necessarily the raw isolation number itself.*

### 6.3 The result does not survive a parameter sweep

**Falsifier sentence:** *A systematic sweep across grid sizes, coupling strengths, or cutoff thresholds that finds the clean-isolation result to be a special case rather than the general behavior would narrow this paper's claim to the single configuration tested.*

---

## 7. Position Statement

**A decoupling boundary grown by the substrate's own bandwidth-collapse dynamics, once properly constructed (connection strength set by the weaker of its two endpoints, not their average), reproduces the same exact information-isolation signature as a boundary installed by hand.** This closes, for the mechanism identified as the one viable candidate, a previously open question about whether ED's substrate can produce a genuine cutoff on its own rather than only ever accepting one as an input. The result required catching and correcting a real construction mistake (averaging instead of taking the minimum), which is reported here alongside the corrected finding rather than silently fixed.

**What this paper claims.** A dynamically-grown cutoff, correctly constructed, reproduces exact information isolation, matching the installed-cutoff baseline; the construction mistake that initially masked this (averaging endpoint bandwidths) is identified and corrected; independent, live activity on both sides of the grown cutoff is confirmed directly.

**What this paper does not claim.** No new substrate primitive or rule; no claim about real physical horizons specifically; no sweep across constructions or parameter regimes; no re-derivation of the underlying dynamical rule's own admissibility.

**Series context.** Companion to "Common Cause, Not Channel" (the installed-boundary capacity result); resolves the emergent-versus-installed question that paper's own substrate left open.

---

## Appendix — Artifacts and Glossary

### Artifacts

- The bandwidth-collapse rule (gravity-sector arc; reused unmodified).
- The certified information-flow substrate and its message-encoding/decoding test (substrate-evaluation arc; reused unmodified).
- The bridge construction connecting the two (this paper): grid-to-network mapping, minimum-based connection strength, cutoff threshold.

### Glossary

- **Installed cutoff.** A connection flagged "severed" by hand before a run begins; never changes during the run.
- **Grown (emergent) cutoff.** A connection that becomes severed as a consequence of the substrate's own dynamics, with no by-hand flag involved.
- **Bandwidth-collapse rule.** A dynamical rule (borrowed from the gravity-sector arc) under which a shared capacity quantity diffuses between neighbors and drains wherever matter-like density accumulates, capable of driving a region's capacity all the way to zero.
- **Weakest-link construction.** Setting a connection's strength to the smaller, not the average, of its two endpoints' capacity values; the choice that correctly seals a grown cutoff, where averaging does not.
- **Isolation / channel-zero.** No message planted on one side of a boundary can be recovered on the other, at any level of encoding sophistication; the same standard used to certify the installed cutoff.

### Reader map

*Intuition.* Think of two rooms separated by a wall. Earlier work always started with the wall already built. This paper asks: if you instead let the wall grow on its own, brick by brick, out of the room's own physics, does it end up just as soundproof? The answer here is yes, once you build it the physically sensible way (a shared wall segment is only as solid as its weaker side, not the average of both sides).

**Where to look next.** A systematic sweep across grid sizes and coupling strengths; other reasonable ways of combining endpoint bandwidths into a connection strength; whether the same construction, applied in three dimensions, still seals cleanly.

---

**End of Paper (Grown, Not Installed).**

*Substrate-evaluation arc. A decoupling boundary grown by the substrate's own bandwidth-collapse dynamics reproduces exact information isolation, matching the installed-boundary baseline, once connection strength is set by the weaker (not the averaged) of its two endpoints. A construction mistake using the average instead was caught and corrected before the result was trusted.*
