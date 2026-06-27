# Soliton Test — a Negative Result, and the Thesis Correction It Forces

**Result: ED does not make a soliton. The could-say-no bit.** A localized packet of certified
worldlines **spreads** — diffusively (late width-exponent p ≈ 0.5, the same √t as the diffusion
recovery) — and a **dense** packet spreads *more* than a sparse one (width 29.3 vs 18.9 at t=80),
not less. There is no self-trapping. This falsifies the layer-1 placement of the dispersive pole
(KdV/NLS) as I had stated it, and it removes what I had called the thesis's "decisive proof."

## What was tested

`event-density/evaluation/CoarseGrain_Arc/soliton_layer1_test.py`. A soliton is dispersion
(spreading) **balanced** by a focusing nonlinearity. ED has both ingredients intrinsically: the
finite-kernel-width gives dispersion, and a moving packet deposits its own ρ, so it feels a
self-field (the nonlinearity). The test seeded a localized disk of active worldlines, evolved the
**certified** rule, and tracked the packet's RMS width(t), comparing a sparse packet (weak
self-field) against a dense one (strong self-field). Soliton signature would be: dense packet
width bounded while sparse spreads. **Observed: both spread; dense spreads faster.**

## Why there is no soliton — two independent reasons

1. **The nonlinearity is defocusing.** ED's Σ-rule drives ρ toward ρ\*, so an over-dense core is
   *dispersed*, not focused. A bright soliton needs an *attractive/focusing* nonlinearity (the
   focusing |ψ|²ψ of NLS); ED's is repulsive. Defocusing NLS has **no bright solitons** — packets
   spread. The dense-spreads-faster result is this defocusing, measured directly.
2. **The rule is dissipative.** The certified rule scatters (that is the layer-2 diffusion we
   recovered). A reversible structure cannot survive a dissipative rule by construction. So even
   absent reason 1, the substrate's own scattering spreads the packet.

ED has the *dispersion ingredient* but the *wrong-sign nonlinearity* and *intrinsic dissipation*.
No balance → no soliton.

## The thesis correction

The synthesis (`Synthesis_TheDivideIsTheArrow`) lumped **dispersive solitons** with **hyperbolic
shocks** as one layer-1 category ("structure-preserving / reversible"), and called the dispersive
pole the decisive proof that the divide is the arrow and not the derivative order. **That was an
overreach.** The sim forces a finer split:

- **Committal structure-MAKING — layer-1-native (confirmed).** Shocks (worldlines converging),
  density deposition, the coherent Maxwell/Coulomb field, Keller–Segel-style aggregation. ED
  *concentrates* and *commits*. This is genuinely what the arrow does, and it is ED-native.
- **Dissipative structure-ERASING — layer-2 + an add (confirmed).** Diffusion, viscosity. The arrow
  averaged away.
- **Reversible structure-PRESERVING (solitons) — NOT ED-native.** This is the new finding. A soliton
  is neither committal-making nor dissipative-erasing; it is a *reversible balance*. ED's committal+
  dissipative substrate does not strike it — it disperses. **The dispersive pole is an edge (or an
  open case in a different sector), not a layer-1 confirmation.**

So the arrow makes ED good at **making/committing** structure and at the **dissipative** limit, but
a soliton needs a **reversible preservation** that the committal substrate does not supply. The
clean "structure-preserving = layer-1" slogan does not survive; **"committal structure-making =
layer-1" does.** The hyperbolic→layer-1 and diffusive→layer-2 halves of the thesis stand; the
dispersive→layer-1 claim does not.

## Honest caveats (what this does and does not settle)

- **What it settles:** at the **substrate-rule level** — which is what the thesis is about (what ED
  makes *by building*) — ED disperses a packet and does not self-trap one. The defocusing sign is
  measured, robust, and reason enough on its own.
- **What it does not settle:** whether a *reversible coherent-field sector* of ED (the phase field,
  the Madelung/Schrödinger construct where Maxwell lives) could host a soliton with a *different*
  effective nonlinearity. But the measured defocusing sign argues against bright solitons even there
  — a focusing nonlinearity would have to come from somewhere the ρ-rule does not provide. This is
  the honest place the QM-sector thread would have to start, and it starts from a negative.

## Status

**Negative result, recorded with full weight.** The dispersive/soliton placement was the thesis's
most-likely-to-break case; it broke. ED makes *committal* structure (layer-1) and reaches the
*dissipative* laws with an add (layer-2), but it **does not make reversible self-trapped solitons —
it disperses them.** The thesis is corrected to "committal structure-making = layer-1," and the
dispersive pole moves from "decisive proof" to **open/edge**. The map gained a coastline.
