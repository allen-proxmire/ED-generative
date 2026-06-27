# Gaussianity — Two Layers, Two Answers

**Result, in one line.** ED is not simply "Gaussian" or "non-Gaussian." The **raw substrate field** stays non-Gaussian no matter how far you coarse-grain (a *spider web* — the strands never blur into a smooth bell). The **diffused walker density** *is* Gaussian (an *ink drop* — it spreads into a smooth bell). Gaussianity is **observable-and-layer-dependent**: it lives at layer 2, on the diffused/decorrelated quantity, not on the committal layer-1 field. The earlier "ED is non-Gaussian" finding and the expectation that nature is Gaussian were never in conflict — they are two different things to look at.

## The question

A Gaussian field is a bell curve — the most common distribution in nature, and the form the CMB takes to ~0.1%. ED's layer-1 deposit field came out **non-Gaussian** (earlier work: 100% of the non-Gaussianity sits in the Fourier phases — i.e. in the structure). The open question: does ED reach Gaussianity at all, and if so, where? Two doors:

- **Door #1** — the field Gaussianizes once you coarse-grain past its correlation length (the Central Limit Theorem fires when you average independent patches).
- **Door #2** — the field is genuinely non-Gaussian at every scale, and the Gaussian world is paid by a *different* quantity / layer.

## What we found — two parts

**Part A — the layer-1 deposit field: door #2.** We measured the field's correlation length directly (ξ ≈ 2 cells — short and finite), then coarse-grained well past it and watched the cumulants:

| coarse-grain scale R_cg | R_cg / ξ | skewness | excess kurtosis |
|---|---|---|---|
| 1 | 0.5 | 0.83 | −0.51 |
| 2 | 1.0 | 0.89 | 0.13 |
| 4 | 2.0 | 0.79 | 0.27 |
| 8 | 4.0 | 0.64 | 0.27 |
| 16 | 8.0 | 0.46 | 0.30 |

Even at **8× the correlation length**, the field stays non-Gaussian — the skewness barely falls and the kurtosis moves the *wrong* way (from −0.5 up to +0.3 and plateaus). For a field with a short correlation length, the naive CLT predicts the opposite: ~64 independent patches per block should crush the skew ~8× and the kurtosis ~64×. It doesn't. *(Sim: `event-density/evaluation/CoarseGrain_Arc/gaussianity_correlation_length_test.py`.)*

**Part B — the layer-2 walker density: door #1.** The diffusing cloud of worldlines came out **near-Gaussian** (excess kurtosis 0.00, mild residual skew) — see `Diffusion_LayerTwo_Recovery.md`. The diffused, decorrelated quantity Gaussianizes, as the CLT says it should.

## The mechanism (why the short-ξ field stays non-Gaussian)

The catch is *which* length matters. The **two-point** correlation length (the power spectrum) is short, ξ≈2. But the non-Gaussianity lives in the **phases** — the filaments — and the phase structure has a much **longer** range (filaments span the box). Coarse-graining kills the two-point correlation fast but leaves the phase structure intact, so the field stays non-Gaussian. The relevant length for Gaussianizing is the *phase*-correlation length, not the two-point one — and that is long. (This is the earlier phase finding, seen from the correlation-length angle.)

## Why it matters

1. **It resolves a real tension.** "ED is non-Gaussian" (layer-1 field) and "nature is Gaussian" (CMB) are not in conflict — they are two layers. The committal field is a web that never blurs; the diffused walker density is an ink drop that does.
2. **It tells us where the CMB-Gaussian debt is paid.** Not by coarse-graining the committal substrate field (that stays non-Gaussian forever), but by a **layer-2, diffused quantity** — the kind of thing that has already decorrelated. The Gaussian world is the ink-drop kind.
3. **It completes the two-layer Gaussianity picture** and confirms the prior expectation that the raw field is genuinely non-Gaussian (door #2 for layer 1), while showing Gaussianity is genuinely present one layer up (door #1 for layer 2).

## Honest caveats

- The grid caps the coarse-graining at ~8ξ. A larger lattice would let us push to 20ξ+ to be airtight on the *slowly-shrinking skew*. But the **kurtosis growing** (−0.5 → +0.3, the wrong direction) is the decisive tell — for a finite-ξ field it should shrink toward 0; it climbs and plateaus. That is structure that will not wash out, not a finite-size artifact.
- Part B (walker density Gaussian) rests on the diffusion test's displacement profile (kurtosis exact, mild skew); more tracers would tighten it.

## Status

Gaussianity: **resolved into the two layers.** Layer-1 deposit field — non-Gaussian, door #2 (does not Gaussianize past ξ; the structure is in the phases). Layer-2 walker density — Gaussian, door #1. The map's "Gaussianity" row is no longer open; it splits by observable.
