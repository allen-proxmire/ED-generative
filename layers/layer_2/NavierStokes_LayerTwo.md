# Navier–Stokes — Layer-2, and Where the Edge Is

**Result.** ED's substrate coarse-grains (kinetic → hydrodynamic) to **compressible** Navier–Stokes: the inertial/convective transport is layer 1 (ballistic worldlines carrying momentum), the **viscous stress is layer 2** — the *same* velocity decorrelation that gave the diffusion recovery, now carrying momentum (viscosity ν is the momentum analog of the diffusion coefficient, from the same mechanism). The one piece ED's substrate does **not** supply on its own is **incompressibility** (∇·u = 0) — a kinematic constraint enforced by an instantaneous, nonlocal pressure Poisson solve, which converts the system from hyperbolic to parabolic-elliptic. ED is hyperbolic and generative (it deposits density, it does not hold ∇·u = 0), so incompressibility is the **added ingredient / the honest edge** — exactly the piece NS-2 (Paper_076) already had to postulate (`P-Incompressibility`). This upgrades NS-2: the viscosity is grounded in the same substrate decorrelation as diffusion rather than purely inherited, and the edge is located precisely.

## NS through the layers (using the AD Atlas axioms)

The AD PDE-Atlas evaluation lists Navier–Stokes's eight implicit axioms. Mapped to the ED layers:

| NS axiom (Atlas) | ED layer | status |
|---|---|---|
| **NS-5 momentum conservation + convective (u·∇)u** | 1 (kinetic/hyperbolic) | ✓ native — ballistic worldlines carry momentum; the convective term is second-order transport (Chapman–Enskog, NS-2 step 7) |
| **NS-3 Newtonian stress ν∇²u** | 2 (hydrodynamic) | ✓ same velocity decorrelation as the diffusion recovery → **momentum** diffusion = viscosity ν ~ v²τ; *measurable from the substrate*, not merely inherited |
| **NS-1 continuum hypothesis (Kn ≪ 1)** | the CG window | ✓ = the hydrodynamic window ℓ_V1 ≪ R_cg ≪ L_flow (DCGT) — the regime where layer 2 lives |
| **NS-2 locality, NS-4 isotropy, NS-8 Euclidean** | inherited | properties of the coarse-grained substrate (local transport, isotropic scattering, emergent metric) |
| **NS-6 incompressibility ∇·u = 0** | **constraint / edge** | ✗ **not native** — an instantaneous, nonlocal elliptic constraint (pressure Poisson). ED is hyperbolic/generative/compressible; this is the added ingredient |
| **NS-7 smooth forcing** | external | input channel, not substrate-generated |

## Why incompressibility is the edge (and why that's the *same* edge as before)

Incompressibility is not a dynamical equation — it has no time derivative. It is a **kinematic constraint** satisfied *instantaneously everywhere*, enforced by the pressure solving a global Poisson equation. That is a nonlocal, elliptic, "infinitely fast" response. ED's substrate is the opposite: **local, hyperbolic, one-way, generative** — it deposits density (ρ grows; we watched it run unbounded), it does not hold a divergence-free constraint, and it has no instantaneous global pressure channel. So ED reaches **compressible** NS (hyperbolic transport + viscosity) by building, and the **incompressible** version requires the elliptic pressure constraint added on top.

This is the **same pattern** the layers program keeps finding: ED supplies the generative, hyperbolic, dynamical content; the *constraints and decorrelations* are the added layer-2 ingredients. Incompressibility joins capacity (the UDM degenerate mobility) and independence (Gaussianity) as a feature the committal/generative substrate does not manufacture by itself.

## What this upgrades in NS-2

NS-2 (Paper_076) had NS form-forced but with three postulates: `P-Hydro-Window`, `P-Incompressibility`, `P-Newtonian-Stress`, and **ν inherited by empirical matching**. Under the layers view:

- **ν is no longer purely inherited.** It is the momentum analog of the diffusion coefficient, from the *same* velocity-decorrelation mechanism the diffusion test measured (Green–Kubo, ν ~ v²τ from the measured decorrelation time). Same substrate origin as diffusion. (The exact value still needs its own momentum/shear measurement — see caveats.)
- **The hyperbolic core is ED-native** (layer 1), so `P-Newtonian-Stress` and the convective term follow from the standard kinetic (Chapman–Enskog) expansion of ED's transport — the same V1 second-moment finiteness NS-2 invokes.
- **`P-Incompressibility` is located, not dissolved.** The layers view does not derive incompressibility — it identifies it precisely as the *one* genuinely-added ingredient, the elliptic constraint the hyperbolic substrate lacks. Honest, and sharper than a flat postulate.

## Honest tier and caveats

- **The viscosity *mechanism* is simulator-grounded** via the diffusion recovery (the velocity decorrelation, Green–Kubo). The *full velocity-field* NS is **structural/analytic** — the certified Σ-rule is orientation-blind and evolves ρ, not a momentum field, so the Eulerian velocity u(x,t) is a coarse-graining construct (NS-2's participation-transport), not a certified-simulator object. Same tier as NS-2 and the gauge work.
- **A direct ν measurement** (a shear-decay or stress-autocorrelation run) would need a momentum-carrying rule (the orientation-blind rule does not transport an imposed flow). The diffusion D ≈ 1.1 is the kinetic estimate (Schmidt number ~1); the dedicated viscosity run is the runnable follow-up.
- **Incompressibility is an edge, not a wall** — adding the elliptic constraint (a fast pressure channel) is an admissible extension, the same way decorrelation/capacity are; it is simply not in the bare generative rule.

## Status

Navier–Stokes: **compressible NS reached** (inertia layer 1 + viscosity layer 2, same decorrelation as diffusion); **incompressibility located as the added elliptic constraint** (the edge). Upgrades NS-2 by grounding ν in the substrate decorrelation and locating the postulate precisely. Next in the NS thread: the dedicated viscosity measurement (momentum-carrying run) to pin ν against the kinetic prediction; and whether the smoothness/turbulence arc (NS-3, NS-Turb) reads differently under the layers view.
