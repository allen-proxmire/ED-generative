# The Atlas Through the Layers — and the Rule Refined

The two-layer program predicted: **hyperbolic / structure-making PDEs → layer-1-native; diffusive / constrained PDEs → layer-2 with an added ingredient.** Swept across the AD PDE-Atlas's fourteen systems, the prediction holds — but the *dispersive* pole forced a sharper statement of the rule. The real divide is not hyperbolic-vs-parabolic. **It is the arrow.**

## The sweep

| PDE | Atlas pole | Layer | What ED reaches / the added ingredient |
|---|---|---|---|
| **Hamilton–Jacobi** | hyperbolic | **1 native** | *is* the eikonal/transport ED casts directly (the #3 result) |
| **Burgers (inviscid)** | hyperbolic | **1 native** | shocks = ballistic worldlines converging; the viscous term is a layer-2 add (the diffusion/viscosity) |
| **KdV** | integrable / dispersive | **1 native** | solitons = structure-making **and reversible**; dispersion is a *coherent* finite-kernel-width effect, **not** a decorrelation |
| **NLS** | dispersive | **1 native** | solitons; the dispersion is Schrödinger (ED's QM sector); reversible, structure-preserving |
| **Fokker–Planck** | diffusive | **2** | the walker-density diffusion (+ drift) — *is* the diffusion recovery |
| **Porous-Medium** | diffusive | **2 + capacity** | linear diffusion + degenerate mobility (ρ_max) = the UDM |
| **Reaction–Diffusion** | diffusive | **2 + reaction** | diffusion + a penalty/reaction term (Turing needs both) |
| **Allen–Cahn** | diffusive | **2 + bistable** | diffusion + a double-well penalty (vs the substrate's monostable ρ\*) |
| **Cahn–Hilliard** | diffusive | **2 + conservation + bistable + 4th-order** | conserved higher-order diffusion |
| **Thin-Film** | diffusive | **2 + capacity + surface-tension** | degenerate fourth-order diffusion |
| **Navier–Stokes** | fluid | **1 + 2; edge = incompressibility** | inertia (1) + viscosity (2); incompressibility = the added elliptic constraint |
| **Keller–Segel** | aggregation | **straddles** | the aggregation/blowup is committal/structure-making (**layer-1-native**); the diffusion is layer 2 |
| **Ricci Flow** | geometric | **2-character, gravity sector** | metric-smoothing (parabolic) = layer-2-like; geometric → connects to ED's gravity arc, not the density layers |
| **Mean-Curvature Flow** | geometric | **2-character, gravity sector** | curvature-smoothing = layer-2-like; geometric |

## The rule, refined: the divide is the arrow

The original cut ("hyperbolic = layer 1, diffusive = layer 2") was *almost* right. The **dispersive** pole (KdV, NLS) is the case that sharpens it. KdV and NLS are **second/third-order** (parabolic *order*, like diffusion) — yet they land on **layer 1**, because their solitons are **structure-preserving and reversible**: they conserve, they do not decorrelate, they do not erase the arrow. So the divide is not the derivative order. It is:

> **Layer 1 = structure-preserving / reversible / committal** — what ED *is*. This includes the hyperbolic laws (shocks) **and** the dispersive laws (solitons): both build and keep structure, both carry no dissipation.
>
> **Layer 2 = structure-erasing / dissipative / smoothing** — the parabolic/diffusive laws. These need an **added decorrelation or constraint** the committal substrate does not manufacture (diffusion needs scattering; the UDM needs capacity; Navier–Stokes needs incompressibility; Gaussianity needs independence).

The dispersive pole is the proof: it has the *order* of a layer-2 law but the *character* of a layer-1 law, and it lands on layer 1. **What separates the layers is whether the law keeps the arrow (native) or averages it away (added).**

## The two kinds of layer-2 add

The sweep also distinguishes the ingredients ED's bare rule lacks:
- **Decorrelations** — diffusion's scattering, viscosity, Gaussianity's independence. These erase the arrow (the move to smooth/reversible).
- **Constraints** — the UDM capacity (ρ_max), Navier–Stokes incompressibility (∇·u = 0), Cahn–Hilliard conservation. These impose a global or boundary condition the local generative rule does not enforce.

Both are the *same kind of thing* in the program's sense: the structure the committal/generative substrate does not supply by building. Dispersion (KdV/NLS) is **not** in either bucket — it is a *coherent, reversible* effect (finite-kernel-width), which is exactly why those laws are layer-1, not layer-2.

## Honest tiers and the live cases

- **Confirmed, grounded:** Hamilton–Jacobi and the diffusive pole — these rest on the *measured* results (the eikonal/transport #3, the diffusion recovery, the capacity/UDM finding, the RC penalty). Solid.
- **Confirmed structurally:** Burgers (inviscid shocks = converging worldlines) — the structure-making character is ED-native, not yet a dedicated sim.
- **The live test that refined the rule — dispersive (KdV, NLS):** placed on layer 1 by character (reversible solitons); a structural reading (we have not sim-tested ED producing a soliton). NLS connects to ED's QM/Madelung sector — a thread, not a closed result.
- **Straddles — Keller–Segel:** its defining feature (aggregation/blowup) is committal/structure-making (layer-1-native — ED concentrates), with diffusion as the layer-2 counterweight. A genuine mix, not a clean placement.
- **Geometric (Ricci, Mean-Curvature):** parabolic/smoothing → layer-2-*character*, but they live on the **metric**, i.e. ED's gravity sector. Tentatively layer-2 (they smooth curvature as diffusion smooths density), but they connect to the separate gravity arc (b→0, khronometric), not the density layers — flagged, not claimed.

## Status

The Atlas sweep **confirms the pattern and sharpens it**: the layer divide is the **arrow** — structure-preserving (hyperbolic *and* dispersive) is layer-1-native; structure-erasing (dissipative/diffusive) is layer-2 with an added decorrelation or constraint. The fourteen systems sort cleanly except for the two honest mixes (Keller–Segel straddles; the geometric pair sits in the gravity sector). This is the organizing law of the layers program, now tested across the whole Atlas rather than asserted from four cases.
