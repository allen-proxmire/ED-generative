# Common Cause, Not Channel: The Determinability Boundary as an Observational Structure in Event Density

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (determinability-boundary robustness)
**Status:** Publication draft (short). Empirical coding experiment with the certified substrate; companion to the determinability-boundary measurement. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/dynamics/` (ED-Generative) — substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This is a negative on the "capacity rescue," reported as such.** It does not find a positive intrinsic determinability invariant; it finds zero. The negative is the expected, allowed outcome of the question, and it strengthens — does not overturn — the determinability-boundary measurement it accompanies.
3. **"Exactly zero" is a direct propagation diagnostic, not an estimator artifact.** The headline (`L2 = 0.000000`) is an exact byte-level comparison of final states, not a mutual-information estimate. The estimator pitfall encountered en route (a positively-biased k-NN decoder) is reported honestly (§3); the exact-zero result does not depend on any estimator.
4. **The common-cause reframe is a conceptual clarification, not a new mechanism.** It re-describes what the determinability boundary *is* (an observational correlation structure) without adding any primitive or rule.
5. **ED's locality is confirmed empirically here, not derived.** The "no unmediated nonlocal influence" property is shown as exact channel-zero on the certified substrate; this paper does not derive locality from the contrast-first ontology.
6. **One certified substrate; specific regions and baselines (5/5).** The result is an exact zero on the cases tested, with a passing local-response control; it is not a proof for all possible region geometries.

---

## Abstract

The determinability-boundary measurement found a positive within-stratum mutual information (`Δ > 0`) that is **observable-dependent** — so the scalar `Δ` is not an intrinsic quantity. Channel *capacity* — the supremum of transmitted information over all inputs and readouts — is observable-independent by construction, so it is the natural candidate to rescue a positive intrinsic invariant. We test it with a coding experiment: encode a `K`-ary message into region A's left-half initial condition, evolve the certified substrate, and try to decode it from (i) A's right half (within a stratum) and (ii) region B (across the decoupling boundary). The result is exact and comes from a direct propagation diagnostic: **changing the encoded message leaves the distant region's final state byte-identical — `L2 = 0.000000` — across every baseline (5/5), within a stratum and across the boundary alike**, while the local-response control passes (a region responds to its *own* initial condition, `L2 = 1.8`). The controlled (interventional) channel capacity between distinct regions is therefore **exactly zero everywhere**. Two consequences. **(1)** Capacity yields no positive intrinsic invariant — the only observable-invariant content of the boundary is a zero, confirming and strengthening the prior result. **(2)** The determinability boundary is an **observational (common-cause) structure, not a transmission channel**: the within-stratum correlation `Δ > 0` is shared-origin co-variation (both halves share a run's seed and the front's passage), *not* information flow; the boundary's "severance" is severance of shared origin (independent seeds → independent strata), not of a channel — because there is no channel anywhere. As a corollary, ED's certified **locality** ("no unmediated nonlocal influence") is confirmed empirically as exact channel-zero: a committed fact is strictly local. The boundary's positive content lives entirely at the observational/common-cause level; its interventional content is a universal zero.

---

## 1. Introduction

The determinability-boundary measurement quantified, in bits, how much one region of the certified ED substrate determines about another, and found the within-stratum mutual information `Δ` to be **observable-dependent** — different observables give different `Δ`, so no single `Δ` is intrinsic. Channel capacity is the obvious next move, and it is the *right* candidate for an intrinsic invariant: as the supremum over **all** encodings and readouts it is **observable-independent** by construction, so a positive within-stratum capacity (with a smaller across-boundary value) would be a genuinely intrinsic determinability quantity in a way no single-observable `Δ` can be. Its *failure* is therefore meaningful — it closes the last route to a positive intrinsic scalar. This short paper asks whether capacity delivers, and finds something cleaner and more structural instead. It is a companion to the determinability-boundary measurement, sharpening *what the boundary is*.

---

## 2. Primitive Inputs and Method

**Substrate:** the certified `Bits/` Σ-rule simulator (20/20 correctness gates), used as-is. The load-bearing property is ED's **locality**: a node's committed state is a function of its local neighborhood only.

**The coding experiment.** Encode a `K`-ary message into region A's left-half initial condition; evolve the certified substrate; attempt to decode the message from (i) A's right half (a within-stratum channel) and (ii) region B (across the decoupling boundary). The capacity is the best achievable decoding over inputs and readouts.

**The decisive diagnostic.** Rather than rely on a capacity estimate, we run a direct **propagation diagnostic**: change the encoded message and measure the exact `L2` difference in the distant region's final state. If the message does not propagate, there is nothing to estimate.

**Controls.** A **local-response control** changes a region's *own* initial condition and confirms it responds (the simulator works); an **across-channel-as-null** control guards the estimator.

**No primitive forcing is invoked.**

**Reproducibility.** The certified `Bits/` substrate is run on a grid partitioned into regions **A-left**, **A-right** (the two halves of one stratum) and **B** (across the decoupling boundary). A `K`-ary message is injected by setting region A-left's initial condition to one of `K` distinct values (the diagnostic uses the two extremes, `0.0` and `0.45`); the substrate is evolved to completion and the **final-state arrays** of A-right and B are compared. The propagation metric is the `L2` norm of the difference between the two final-state arrays (`Σ(x^{msg=0}_{final} − x^{msg=0.45}_{final})²`), evaluated over **5 baseline configurations** (5/5). The local-response control applies the same `0.45` change to a region's *own* initial condition. Seeds are fixed per run. Scripts: `capacity_experiment.py` (the diagnostic), `capacity.py` (the bias-corrected k-NN MI estimator, used only for the en-route check).

**Regime of validity.** This result is for the **certified Σ-substrate** and the **specific region geometries and 5 baselines tested**, with specific initial-condition encodings: an exact zero on those cases, with a passing local-response control. It is **not a proof for all possible geometries or ED instantiations** — though ED's locality (§4.3) makes a nonzero result on any *local* partition structurally surprising.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated; certified substrate | P / I | Paper_087; `Bits/` (20/20 gates) |
| Distant-region propagation is exactly zero (`L2 = 0`, 5/5) | **measured (exact)** | §3 — direct byte-level diagnostic |
| Local-response control passes (`L2 = 1.8`) | **measured** | §3 — simulator responds to local input |
| Interventional channel capacity = 0 (within and across) | **D** | §3 — no propagation ⇒ no channel |
| Estimator bias caught and corrected | **measured / honesty note** | §3 — k-NN decoder MI positively biased; control caught it |
| Capacity yields no positive intrinsic invariant | **D** | §4.1 — zero everywhere |
| Boundary is observational (common-cause), not transmission | **interpretation** | §4.2 — within-stratum `Δ` is shared-origin co-variation |
| ED locality confirmed (exact channel-zero) | **D** | §4.3 |
| A positive intrinsic determinability scalar | **NOT FOUND** | §4.1 |

All steps P, I, measured, D, interpretation, or explicitly not-found. *The headline is an exact measured zero, not an estimate; the one estimator hazard is reported and was caught by a control.*

---

## 3. The Result: Exactly Zero

The headline did not come from the estimator; it came from the direct propagation diagnostic, and it is exact:

> **Changing the encoded A-left message (0.0 → 0.45) leaves A-right's final state byte-identical — `L2 = 0.000000` — across every baseline tested (5/5).** The message does not propagate to A-right *at all*. Not weakly. Exactly zero. The same holds for region B across the boundary.

**"Exact zero" here means bit-for-bit identity of the final-state arrays** — `L2 = 0.000000` with no floating-point tolerance and no thresholding; the two runs produce numerically *identical* output, not merely close output.

The **control passes**: A-right *does* respond to its *own* local initial condition (`L2 = 1.8` for the same 0.45 change). So the simulator is working — a region responds to local changes and is *exactly insensitive* to a distant region's input. The logic is then explicit: **if no perturbation to A-left produces any change in A-right or B, the mutual information between input and output is identically zero, so the channel capacity — the supremum of that mutual information over all encodings and readouts — is zero.** The controlled (interventional) channel capacity between distinct regions is therefore **exactly zero — within a stratum and across the boundary alike.** A committed node depends only on its local neighborhood; it carries no information about a distant region's initial condition. There is no controllable channel to have a capacity.

**Estimator honesty note.** The first decoder-MI pass was *wrong*: a naive leave-one-out k-NN decoder MI is positively biased by `~log₂K − log₂k` when `K ≫ k`, and it read `~2.8 bits` even across the *decoupled* boundary. The across-channel-as-null control caught it immediately, and a shuffle-null correction fixed it — but once the diagnostic showed propagation is *exactly* zero, no capacity estimate was needed. **To be unambiguous: the MI estimator was *not* used for the final result; the exact-zero propagation diagnostic supersedes it entirely — the conclusion would be identical with no estimator at all.** This is recorded because the trap is easy and the control is what caught it.

---

## 4. What It Means

### 4.1 Capacity gives no positive intrinsic invariant

At the one genuinely observable-independent level (capacity), the intrinsic quantity is **zero**, and it is zero *everywhere* — within and across. So capacity provides no "within > across" contrast and no canonical positive determinability scalar. The determinability-boundary measurement's conclusion stands and is strengthened: **the only observable-invariant content of the boundary is a zero**, not a scalar.

### 4.2 The boundary is observational (common-cause), not transmission

This is the conceptual payoff. The within-stratum `Δ > 0` measured by the determinability-boundary work is **observational correlation from a common cause**: within one run, both halves of a stratum share the run's seed and the front's passage, so across an ensemble they co-vary. A1 measures **interventional transmission** and finds it zero. The two diverge *exactly because* the within-stratum correlation is **common-cause, not causal-flow**:

- *Within a stratum:* the two halves are correlated because they **share an origin** (the same run), not because information flows between them.
- *Across the boundary:* independent origins (independent seeds) → no shared cause → no correlation.

So the "severance" the determinability work found is severance of **shared origin** (independent seeds make independent strata), **not** severance of a transmission channel — because there is no transmission channel anywhere. **The determinability boundary is a fact about common causes, not about signals.**

Two notes. *The reframe is descriptive, not a new mechanism:* it re-describes what the boundary *is*, leaving ED's primitives unchanged. *And it is the textbook hallmark of common cause:* observational mutual information can be nonzero while interventional mutual information is exactly zero — correlation without transmission — which is precisely the configuration we measure.

### 4.3 ED's locality, confirmed as exact channel-zero

A1 demonstrates ED's "no unmediated nonlocal influence" property directly and at the strongest level: **controlled transmission between distinct regions is exactly zero.** Locality here is precise: a node's committed state is a function only of its local neighborhood — the adjacency/transport primitives **P02–P05** — so **no distant intervention can alter it**, which is exactly what the exact channel-zero measures. A committed fact in ED is strictly local. ED's certified locality is not merely an internal code property; it is observable as exact channel-zero, within and across.

---

## 5. Limitations (honest)

- **One certified substrate; specific regions/baselines (5/5) with a passing control.** An exact zero on the cases tested, not a proof for all region geometries.
- **The result is a clean negative** on the capacity rescue (no positive invariant) and a clean positive on the clarification (common-cause, locality). It is not a new positive determinability quantity.
- **The common-cause split is here demonstrated, not formalized.** A transfer-entropy / common-cause decomposition (the interventional term identically zero, all content in the common-cause term) would formalize it; that is a reformulation, not required for the result.

---

## 6. Falsification Criteria

### 6.1 Nonzero distant-region propagation

**Falsifier sentence:** *A measurement showing the distant region's final state changes (`L2 > 0`) under a change of the encoded message, within a stratum or across the boundary, would falsify the exact channel-zero result and ED's locality.*

### 6.2 A positive intrinsic capacity contrast

**Falsifier sentence:** *A demonstration of a within-stratum channel capacity bounded away from zero (a genuine "within > across" capacity contrast), surviving the local-response and across-null controls, would falsify §4.1 and recover a positive intrinsic determinability invariant.*

### 6.3 Causal flow within a stratum

**Falsifier sentence:** *Evidence that the within-stratum `Δ > 0` reflects information flow between the halves (interventional transmission) rather than shared-origin co-variation would falsify the common-cause reframe (§4.2).*

---

## 7. Position Statement

**The controlled channel capacity between distinct regions of the certified ED substrate is exactly zero — within strata and across the boundary — by ED's locality.** Capacity therefore yields no positive intrinsic determinability invariant; the only observable-invariant content of the boundary is a zero. The conceptual payoff: the determinability boundary is an **observational (common-cause) structure, not a transmission channel** — the within-stratum correlation is shared-origin co-variation, the across-boundary independence is independent origins, and there is no signal channel anywhere. As a corollary, ED's "no unmediated nonlocal influence" is confirmed as exact channel-zero.

**What this paper claims.** Exact zero distant-region propagation (5/5, with a passing local control); no positive intrinsic capacity invariant; the boundary's positive content is observational/common-cause; ED's locality is empirically exact.

**What this paper does not claim.** No positive determinability scalar is found (it is a negative on the rescue); the result is an exact zero on the tested cases, not a geometry-universal proof; the common-cause decomposition is demonstrated, not formalized; locality is confirmed, not derived.

**Series context.** The robustness companion to the determinability-boundary measurement, and the *internal* reading of the same finite-reach ceiling whose *external* reading is the finite-memory (primes) result: ED's hard ceiling on long-range / global information, measured against ED's own observables here and against a math-certified ruler there.

---

## Appendix — Artifacts and Glossary

### Artifacts (`evaluation/Bits/`)

- `analysis/capacity.py` — bias-corrected leave-one-out k-NN decoder MI with shuffle-null (reusable).
- `examples/capacity_experiment.py` — the coding experiment + the exact propagation diagnostic.

### Glossary

- **Stratum.** A determinability-equivalence region of the ED substrate — within one run, a connected set of nodes sharing the run's seed and the front's passage, hence co-varying; distinct strata have independent origins.
- **Channel capacity.** The supremum of transmitted information over all inputs and readouts — observable-independent by construction; here, exactly zero between distinct regions.
- **Interventional vs observational.** *Interventional* = change an input and measure transmission (zero here). *Observational* = correlation across an ensemble (the within-stratum `Δ > 0`).
- **Common cause.** Two regions co-vary because they share an origin (a run's seed + front passage), not because a signal flows between them. The determinability boundary is a common-cause structure.
- **Severance.** Independent seeds make independent strata — severance of shared origin, not of a channel (there is none).
- **Locality (ED).** No unmediated nonlocal influence; confirmed here as exact channel-zero — a committed fact depends only on its local neighborhood.

### Reader map and open work

*Intuition.* Two regions in ED can look correlated because they share a run's seed, but no intervention in one can influence the other — exactly the difference between **correlation** and **causation**. The determinability boundary lives entirely on the correlation side.

*A note of context.* This is the operational content of Pearl's **causal hierarchy**: observational association and interventional effect are distinct rungs, and channel capacity — the interventional measure — is the gold standard for actual causal influence. Here the two rungs come apart maximally: nonzero association (`Δ > 0`), exactly zero intervention.

**Where to look next.**
- *The determinability-boundary measurement this companions:* the Bits determinability paper.
- *The external (math-certified) reading of the same ceiling:* the Finite-Memory (primes) paper.
- *The coarse-graining wall (the continuum / PDE shadow):* the Continuum paper.

**Open work** (declared): test more region geometries and partitions; multi-front interaction regimes; whether stochastic ED variants change the picture; and a formal transfer-entropy / common-cause decomposition (interventional term identically zero, all content in the common-cause term).

---

**End of Paper (Common Cause, Not Channel).**

*Substrate-evaluation arc. Controlled channel capacity between distinct ED regions is exactly zero (`L2 = 0`, 5/5, local control passes) — within strata and across the boundary — by ED's locality. Capacity yields no positive intrinsic determinability invariant; the determinability boundary is an observational (common-cause) structure, not a transmission channel; ED's "no nonlocal influence" is confirmed as exact channel-zero. The boundary's positive content is observational; its interventional content is a universal zero.*
