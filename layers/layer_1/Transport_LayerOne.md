# Transport / Eikonal — Layer-1 (ED's Native Continuum)

**Result.** ED's *direct* coarse-graining — one CG from the substrate — produces a **transport / eikonal** law, not diffusion. The coarse density field's evolution regresses cleanly onto |∇ρ| (a hyperbolic, kinetic equation), not ∇²ρ (parabolic diffusion). This is ED's native continuum: ballistic worldlines (|v|≈1) propagating and depositing density. It is the **layer-1 kinetic shadow** — the thing the substrate casts by building, still carrying the arrow.

## The test

The certified substrate is a chain/worldline propagator: a single active front traces a worldline; an ensemble deposits a density field. Two readings:

- **Single chain — straightness.** A worldline's net displacement over path length is ≈1 in a smooth landscape: ballistic, not a random walk. The substrate makes *trajectories* first.
- **Ensemble field — which PDE class?** Coarse-grain the deposited density and regress ∂_t⟨ρ⟩ on a candidate library (diffusion ∇²ρ vs eikonal/transport |∇ρ|), letting the data pick the class.

## Numbers

For a step initial condition (the cleanest front), regressing the ensemble-mean field:

| model | single realization R² | ensemble-mean R² |
|---|---|---|
| diffusion (∇²ρ) | 0.001 | 0.258 |
| **eikonal / transport (\|∇ρ\|)** | 0.094 | **0.597** |

Ensemble-averaging cleans the dynamics dramatically (R² 0.10 → 0.60), revealing a coherent continuum law — and that law is **eikonal/transport**, beating diffusion decisively. The mean density spreads *ballistically* (∝ t), not diffusively (∝ √t), because the worldlines are straight, not random-walk steps.

Sims: `event-density/evaluation/CoarseGrain_Arc/diffusion_coherent_decomp.py`, `coarsegrain_test.py`.

## The Lagrangian / Eulerian distinction (important)

Two different objects, two different behaviors — and both are real:

- The **deposited density field** (Eulerian) evolves by **transport** — this result, layer 1.
- The **walker positions** (Lagrangian), scattering off ρ-disorder, **diffuse** — the layer-2 result (`../layer_2/Diffusion_LayerTwo_Recovery.md`).

So "ED is transport" and "ED diffuses" are not in tension: the *field* transports at layer 1; the *walkers* diffuse at layer 2. Knowing which observable you are coarse-graining is the whole game.

## Honest caveats

- The regression R² is **modest** (0.60 for the cleanest, step IC; weaker for smooth gaussian/ring ICs that lack a sharp front). The result is the **contrast** — eikonal decisively beats diffusion — not the absolute fit value.
- Single substrate instantiation (the Σ-rule grid), modest sizes. The conclusion is about the *class* (hyperbolic/kinetic), not a polished coefficient.

## Why it matters

1. **This is ED's native continuum.** The substrate's direct shadow is a *kinetic* equation — ballistic transport — confirming the CoarseGrain trilogy's verdict that the certified substrate is a kinetic lattice-gas, not a diffusion PDE.
2. **It carries the arrow.** Transport is directional; the layer-1 shadow inherits the substrate's committal, one-way character. Reversibility lives one layer up.
3. **Diffusion is its layer-2 descendant.** Transport + the substrate's intrinsic scattering coarse-grains (a second time) to genuine diffusion (the layer-2 recovery). Transport is the parent; diffusion is the child. The hierarchy starts here.

## Status

Layer-1 transport: **established** (the contrast is robust; absolute R² limited by the sparse deterministic field). The foundational entry of the layers program — every layer-2 result is a second coarse-graining of this one.
