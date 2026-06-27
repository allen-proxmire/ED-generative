# The Atlas Through the Layers — and the Rule Refined

The two-layer program predicted: **hyperbolic / structure-making PDEs → layer-1-native; diffusive / constrained PDEs → layer-2 with an added ingredient.** Swept across the AD PDE-Atlas's fourteen systems, the hyperbolic→layer-1 and diffusive→layer-2 halves hold. The *dispersive* pole (KdV/NLS) was first read as a sharpening (parabolic order, layer-1 character) — but the **soliton test refuted that**: ED *disperses* a packet, it does not self-trap one, so the dispersive pole is an **edge/open case, not layer-1**. The corrected divide is **committal structure-MAKING (layer-1) vs dissipative structure-erasing (layer-2)**; reversible structure-*preservation* (solitons) is a third thing ED does not reach. See `layer_1/Soliton_Test_NegativeResult.md`.

## The sweep

| PDE | Atlas pole | Layer | What ED reaches / the added ingredient |
|---|---|---|---|
| **Hamilton–Jacobi** | hyperbolic | **1 native** | *is* the eikonal/transport ED casts directly (the #3 result) |
| **Burgers (inviscid)** | hyperbolic | **1 native** | shocks = ballistic worldlines converging; the viscous term is a layer-2 add (the diffusion/viscosity) |
| **KdV** | integrable / dispersive | **edge / open** | ~~1 native~~ — **soliton test FAILED**: ED disperses a packet (defocusing nonlinearity + dissipation), no self-trapping. Reversible structure-preservation is not ED-native (`layer_1/Soliton_Test_NegativeResult.md`) |
| **NLS** | dispersive | **edge / open** | ~~1 native~~ — same negative; the QM-sector thread would have to start from this negative (defocusing sign argues against bright solitons even in the coherent-field construct) |
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

## The rule, corrected: committal-making vs dissipative-erasing

The original cut ("hyperbolic = layer 1, diffusive = layer 2") was *almost* right, and the soliton test fixed the rest. I first read the **dispersive** pole (KdV, NLS) as the sharpening — parabolic *order* but, I claimed, layer-1 *character* (reversible solitons). **The soliton sim refuted that:** ED disperses a packet, it does not self-trap one (defocusing nonlinearity + intrinsic dissipation). So the dispersive pole is **not** layer-1. The corrected rule:

> **Layer 1 = committal structure-MAKING** — what ED *is*: it concentrates and commits. The hyperbolic laws (shocks = converging worldlines), the coherent fields (Maxwell), aggregation (Keller–Segel). ED makes structure by *building* it.
>
> **Layer 2 = dissipative structure-ERASING** — the parabolic/diffusive laws. These need an **added decorrelation or constraint** the committal substrate does not manufacture (diffusion needs scattering; the UDM needs capacity; Navier–Stokes needs incompressibility; Gaussianity needs independence).
>
> **Reversible structure-PRESERVING (solitons) = neither** — a reversible balance ED does not strike. It is an **edge**: ED disperses what it does not commit. The dispersive pole lives here.

**What separates ED-native (layer 1) from the rest is *commitment* — whether the law is built by concentrating/committing (native) or requires the arrow averaged away (layer-2 add) or a reversible balance ED won't hold (dispersive edge).**

## The two kinds of layer-2 add

The sweep also distinguishes the ingredients ED's bare rule lacks:
- **Decorrelations** — diffusion's scattering, viscosity, Gaussianity's independence. These erase the arrow (the move to smooth/reversible).
- **Constraints** — the UDM capacity (ρ_max), Navier–Stokes incompressibility (∇·u = 0), Cahn–Hilliard conservation. These impose a global or boundary condition the local generative rule does not enforce.

Both are the *same kind of thing* in the program's sense: the structure the committal/generative substrate does not supply by building. Dispersion (KdV/NLS) is in **neither** bucket and is **not** layer-1 either: ED has the dispersion ingredient but a *defocusing* nonlinearity, so it disperses rather than self-traps — solitons are an **edge** (the soliton test, below).

## Honest tiers and the live cases

- **Confirmed, grounded:** Hamilton–Jacobi and the diffusive pole — these rest on the *measured* results (the eikonal/transport #3, the diffusion recovery, the capacity/UDM finding, the RC penalty). Solid.
- **Confirmed structurally:** Burgers (inviscid shocks = converging worldlines) — the structure-making character is ED-native, not yet a dedicated sim.
- **Tested and FAILED — dispersive (KdV, NLS):** the soliton sim shows ED disperses a packet (defocusing nonlinearity + dissipation, dense spreads faster), so the layer-1 placement is **refuted**; the dispersive pole is an **edge/open**. The QM/Madelung thread would have to start from this negative.
- **Straddles — Keller–Segel:** its defining feature (aggregation/blowup) is committal/structure-making (layer-1-native — ED concentrates), with diffusion as the layer-2 counterweight. A genuine mix, not a clean placement.
- **Geometric (Ricci, Mean-Curvature):** parabolic/smoothing → layer-2-*character*, but they live on the **metric**, i.e. ED's gravity sector. Tentatively layer-2 (they smooth curvature as diffusion smooths density), but they connect to the separate gravity arc (b→0, khronometric), not the density layers — flagged, not claimed.

## Status

The Atlas sweep **confirms the pattern and sharpens it**: the layer divide is the **arrow** — structure-preserving (hyperbolic *and* dispersive) is layer-1-native; structure-erasing (dissipative/diffusive) is layer-2 with an added decorrelation or constraint. The fourteen systems sort cleanly except for the two honest mixes (Keller–Segel straddles; the geometric pair sits in the gravity sector). This is the organizing law of the layers program, now tested across the whole Atlas rather than asserted from four cases.
