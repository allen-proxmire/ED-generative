# Diffusion — Layer-2 Recovery

**Result.** ED's layer-1 transport (ballistic worldlines), coarse-grained a second time through the substrate's *intrinsic* scattering off ρ-disorder, produces **genuine diffusion** — confirmed not by its shape but by a passing **coefficient** test: the diffusion coefficient measured from the velocity autocorrelation (Green–Kubo) agrees with the one measured from the spreading (MSD) to ~9%, with nothing tuned. This is the two-layer program's first demonstrated layer-2 recovery.

## The test

Many certified single-chain worldlines propagate in a uniform ρ-disorder medium. The "collision" is **intrinsic** — the worldlines scatter off the substrate's own density fluctuations; no decorrelation knob is added. Diffusion is then checked by coefficients:

- **Green–Kubo:** D_GK = (1/2d)·[C(0) + 2Σ_{τ≥1}C(τ)] from the velocity autocorrelation C(τ).
- **MSD:** D_MSD = MSD / (2d·t) at long time.
- If the process is truly diffusive, these two independent estimates must coincide.

## Numbers

| Quantity | Value | Reading |
|---|---|---|
| MSD exponent α, early (t 4–20) | 1.55 | ballistic onset (expected) |
| MSD exponent α, late | 1.17 → **≈1.0** asymptotically | latest stretch (t 100→150) gives α≈1.0; VACF decays to ~0 by τ=2 (finite integral ⇒ normal diffusion) |
| **D_MSD** (spread) | **1.056** | |
| **D_GK** (Green–Kubo) | **1.158** | |
| **D_MSD / D_GK** | **0.91** | the two coefficients agree to 9% — the could-say-no, passed |
| displacement profile (late t) | skew 0.26, **excess-kurtosis 0.00** | near-Gaussian (kurtosis spot-on; mild residual skew) |

Sim: `event-density/evaluation/CoarseGrain_Arc/diffusion_layer2_test.py` (S=251, T=150, 60 worldlines).

## Honest caveats

- The window-fit α is **1.17, not a clean 1** — contaminated by the ballistic onset. The fast VACF decay *guarantees* α→1 (a finite Green–Kubo integral is, by definition, normal diffusion), and the latest points sit at ≈1.0; a longer run (T≈300) would nail the asymptote.
- The displacement has a **mild residual skew** (0.26) though the kurtosis is exact (0.00). More tracers would tighten both.
- Neither caveat touches the coefficient match, which is the load-bearing result.

## Why it matters

1. **First layer-2 win.** ED-transport (layer 1) plus the substrate's *own* intrinsic scattering — a justified, intrinsic ingredient, not a tuned knob — coarse-grains to real diffusion, coefficients and all. Diffusion *is* a layer up, and ED reaches it.
2. **Reconciles the arc.** ED's direct CG of the *deposited field* is transport (layer 1; what the earlier work found). ED's *walker-position density* plus scattering is diffusion (layer 2). Both true — different objects, different layers. "ED can't make diffusion" was a layer-1 statement.
3. **Reframes Gaussianity (#1).** The diffusing walker-cloud came out **near-Gaussian** (kurtosis 0). So the *layer-2 walker density* is Gaussian while the *layer-1 deposit field* is not (100% non-Gaussian in the phases). Gaussianity is **observable-and-layer-dependent** — the earlier non-Gaussian result and the door-#1 hope are not in conflict, they are two layers. The next test (correlation-length / Gaussianity) now knows to watch the layer-2 walker density, not the layer-1 field.

## Status

Layer-2 diffusion: **recovered** (coefficient-validated; α and profile to be tightened with a longer/larger run). The held substrate-evaluation papers that framed diffusion as a "wall / different object" are superseded by this — diffusion is layer 2, and it is reached. Next in the layers program: the Gaussianity correlation-length test (#1), then the Navier–Stokes / Yang–Mills big swing.
