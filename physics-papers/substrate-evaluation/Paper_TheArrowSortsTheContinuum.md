# The Arrow Sorts the Continuum

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation / continuum-emergence line. Standalone; cold-reader accessible. Supersedes and absorbs three earlier coarse-graining notes written under a flat "walls" framing.

---

## Preamble — What This Paper Does *Not* Claim

1. **It does not derive General Relativity.** ED's gravity sector is **khronometric** and weak-field (GR-I…GR-IV); the geometric results used here are inherited from those papers, not re-derived, and the full nonlinear Einstein equation is not obtained.
2. **It does not solve, or claim progress on, the Clay problems** (the Yang–Mills mass gap, Navier–Stokes global regularity). It supplies *physical mechanism*; the rigorous-mathematics proofs are a different discipline and are explicitly disclaimed (§8).
3. **It does not claim ED reaches every continuum law.** The opposite: the *edges* — the laws ED cannot cast — are part of the result, and one of them is established by a *failed* test (§6).
4. **The sorting principle is a structural thesis.** Its instances are tiered explicitly throughout as **measured** (simulated, coefficient-checked), **derived** (analytic from primitives), or **structural** (a reading of an existing rule). The thesis is not claimed at a tier higher than its weakest load-bearing instance permits, and those instances are named.
5. **It introduces no new substrate primitives.** The 13-primitive system (Paper_087) is taken as given.

---

## Abstract

Event Density is a substrate built on one defining primitive: **commitment**, the irreversible arrow (P11). This paper asks which continuum laws of physics that substrate produces under coarse-graining, and finds that a single principle — commitment — sorts them. Continuum laws are not all the same distance from the substrate; they form a **hierarchy of coarse-grainings** (substrate $\to$ kinetic $\to$ hydrodynamic), and ED's direct coarse-graining lands on the first, *kinetic* layer. What distinguishes the layers is not the order of a derivative or the type of a pole, but whether a law **keeps or forgets the arrow's footprint** — the correlations, direction, and phase that commitment writes into structure. Three classes result. **Committal structure-making** laws (transport/eikonal, shocks, the coherent Maxwell field, aggregation) keep the footprint and are layer-1-native — ED builds them. **Dissipative structure-erasing** laws (diffusion, viscosity, the Gaussian limit) forget the footprint and are reached only at layer 2, by adding a single forced operator — at second order, the unique isotropic-local-conservative gradient-flux Laplacian $\nabla\!\cdot\!(M\nabla\varphi)$, of which Gaussianity is the heat-kernel and capacity the degenerate mobility. **Reversible structure-preserving** laws (solitons) ask for a balance the *bare* substrate does not supply on its own — tested directly, the bare rule disperses the packet; ED hosts a soliton only with an added focusing medium (a higher layer), not at the very bottom. This is *not* a claim that solitons cannot exist — only that ED does not build one from the bottom rule alone. The same primitive reaches into gravity: ED's measured weak-field metric rule (GR-III) *is* the two-layer structure — a layer-2 metric-smoothing (weak-field Ricci flow) competing with a layer-1 commitment-concentration that forms horizons — so the continuum-PDE map and the horizon/information map are two faces of one commitment. The operator-level statement is sharp: the heat operator and the wave operator share the same Laplacian, and the arrow is the order of the time derivative on it. The diffusive results are coefficient-checked (Green–Kubo); the geometric results are inherited as simulated; the soliton edge is a measured negative; the Yang–Mills and Navier–Stokes contributions are *physics*, with the rigorous proofs explicitly disclaimed. The arrow draws the coastline as well as the land.

---

## 1. The Question, and the Ladder

The Event-Density substrate is austere: worldlines that move and *commit*, with the commitment irreversible (P11) — the arrow of time built in at the bottom rather than emerging on top. The continuum world it must answer to is the opposite of austere: heat-spreading, fluid flow, electromagnetism, gauge fields, the Schrödinger equation, the bending of spacetime. The question this paper settles is direct: **which of those laws does ED produce, which does it not, and what decides?**

The decisive move is to stop treating "the continuum limit" as a single step. It is not. No one coarse-grains atoms straight to the equation for how heat spreads; the route is **atoms $\to$ a kinetic picture of particles streaming and colliding $\to$ the smooth hydrodynamic equations** — *two* coarse-grainings, not one. This layering is textbook kinetic theory. "A layer up" means literally one more coarse-graining applied to the layer below.

ED's *direct* coarse-graining lands on the **first, kinetic layer**. Squint at the substrate once and you get **transport** — streaming, concentration, structure being built. You do not get the smooth, spread-out hydrodynamic laws directly; those sit one layer higher and require a second coarse-graining. The content of this paper is what that second step adds, why it adds the same thing every time, and why one primitive decides the whole map.

## 2. The Thesis: the Divide Is the Arrow

What the arrow writes into the world is not motion as such — every step a worldline takes is a commitment — but **memory**: the correlations between commitments, the direction they share, the phase structure they carry, the record of how they link. That memory is the arrow's footprint.

A continuum law is sorted by what it does with that footprint:

- **Layer 1 — keeps the footprint.** Directional, structured, phase-correlated, lumpy. The law still remembers. These are the laws ED *builds*.
- **Layer 2 — forgets the footprint.** Smooth, isotropic, memoryless, Gaussian. Going up a layer does not un-commit anything; it commits *while discarding the record of how the commits were linked*. This is why the ingredient always added at layer 2 is independence — molecular chaos, decorrelation. It is, precisely, *forgetting*.

And the third class, which the first two imply:

- **Edge — needs a footprint ED cannot write.** A law that requires a *reversible* balance — perfect preservation of a delicate structure, run-backward symmetric — asks the substrate to hold without committing. A thing made of commitment cannot. These laws are walls.

The principle is forced, not fitted. ED's single defining primitive is commitment; a substrate whose foundation is the arrow is native to laws that share its character, reached-with-help for laws that forget it, and barred from laws that need its absence. **The map of which continuum laws ED casts is the arrow's footprint spread across the continuum.**

The general cut is **hyperbolic versus parabolic**: hyperbolic laws (real characteristics, finite-speed propagation) keep the memory — first-order transport $\partial_t + v\cdot\nabla$ is the simplest, the wave operator a second-order case — while parabolic laws (Laplacian dissipation) forget it. The sharpest single instance of the cut is worth isolating, because there the difference is *only* the arrow. Compare the heat operator $\partial_t - \nabla^2$ (diffusion, layer-2) with the wave operator $\partial_t^2 - \nabla^2$ (the coherent field, layer-1): **they share the same spatial Laplacian**, and the lone difference is the time derivative — paired with $\partial_t^2$ it propagates reversibly and keeps the memory, paired with $\partial_t$ it smooths irreversibly and forgets. On that one shared operator, commitment is the order of the time derivative. Remember-versus-forget, made as formal as it gets.

## 3. The Atlas Sweep, and the Rail

The thesis is tested by sorting the standard catalogue of continuum PDEs. The table records each law's class and the tier of the evidence.

| Law | Class | Tier |
|---|---|---|
| Hamilton–Jacobi / eikonal | layer-1 (keeps) | **measured** — ED's direct transport shadow |
| Burgers (inviscid) — shocks | layer-1 (keeps) | structural — converging worldlines |
| Coherent Maxwell / Coulomb | layer-1 (keeps) | **measured** — coherent part tracks the Coulomb minimizer |
| Keller–Segel aggregation | layer-1 (keeps) | structural — committal concentration |
| Diffusion / Fokker–Planck | layer-2 (forgets) | **measured** — Green–Kubo-consistent |
| Navier–Stokes viscosity | layer-2 (forgets) | structural — same decorrelation as diffusion |
| Porous-medium / UDM | layer-2 + capacity | structural — degenerate mobility |
| Reaction–diffusion, Allen–Cahn, Cahn–Hilliard, thin-film | layer-2 + add | structural |
| Gaussian field statistics | layer-2 kernel | **measured** — the smoothing operator's fingerprint |
| Ricci flow (gravity) | layer-1 + layer-2 | **measured** (GR-III), weak-field; mean-curvature the structural sibling |
| Navier–Stokes incompressibility | constraint add | structural — the elliptic edge |
| **Solitons (KdV / NLS)** | **edge** | **measured negative** — ED disperses |
| Primality (escape/parity) | proven edge | inherited (finite-memory ceiling) |

The sort is governed by a discipline, stated so the result cannot be self-fulfilling:

1. **The ingredient added at a coarse-graining step is specified in advance and independently justified** — never tuned to land on the target law. Adding whatever is needed to reach the law you wanted is reverse-engineering, and it predicts nothing.
2. **Reached is tested by coefficients, not shape.** Does ED-plus-the-named-ingredient reproduce the law's *constants* (a validated diffusion constant, a Green–Kubo consistency) — not merely its form?
3. **The no's are recorded with equal weight.** They are the coastline. ED already carries a *proven* edge (primality: a finite-memory substrate provably cannot reach the parity/escape layer, graded against Sarnak's barrier), and this paper adds a *measured* one (solitons, §6).

The following sections take the three classes in turn, then the bridge.

## 4. Layer 1 — What ED Builds

ED's direct coarse-graining keeps the arrow's footprint, and the laws it casts are correspondingly directional and structure-making.

- **Transport / eikonal (Hamilton–Jacobi).** The coarse density field of ED's worldlines obeys a transport/eikonal law — Hamilton–Jacobi, the canonical hyperbolic, memory-keeping equation. This is **measured**: the ensemble-mean density regresses to the eikonal form, the substrate's most direct continuum shadow.
- **Shocks (inviscid Burgers).** Worldlines converging concentrate the field into shocks — structure formed by commitment, not smoothed away. The viscous regularization of Burgers is a *layer-2* add (§5); the shock itself is layer-1.
- **The coherent Maxwell field.** ED's coherent (in-phase) sector reproduces the Coulomb field: its coherent part tracks the Coulomb energy minimizer (**measured**). This is the abelian, massless, long-range field — propagation, not dissipation.
- **Aggregation (Keller–Segel).** Self-concentration to the point of blow-up is committal structure-making par excellence; it is layer-1-native in ED even though the equation also carries a layer-2 diffusive counter-term.

All four are hyperbolic in character — they propagate and concentrate, they keep the memory. They are what the arrow does when it builds.

## 5. Layer 2 — One Forced Operator

The laws that forget the footprint are reached by a second coarse-graining, and the ingredient it adds is always the same — provably so.

**Diffusion is the clean case, and it is measured.** ED's worldlines scatter off the substrate's own density-disorder; that intrinsic scattering decorrelates the velocity, and the result is *normal diffusion*. The check is by coefficients, not shape: the Green–Kubo diffusion constant (from the velocity autocorrelation) agrees with the mean-square-displacement constant to within ~9%, with the mean-square displacement growing linearly and the displacement distribution Gaussian. The walker still commits every step; the diffusion *equation* is what remains once the correlations between steps are discarded.

**The operator is unique.** A dissipative term produced by the second coarse-graining must be **isotropic** (decorrelation has no preferred direction — that is what it means), **local** (the window is finite), and **conservation-respecting** (it redistributes the field, a divergence of a flux). The unique **second-order** operator with those three properties is the gradient-flux Laplacian
$$ \nabla\!\cdot\!\big(M\,\nabla\varphi\big). $$
The fourth-order gradient flows (Cahn–Hilliard, thin-film) do not break this — they are the *same* conservation/flux form $\nabla\!\cdot J$ with the flux driven by a structured potential that carries surface tension; the second-order Laplacian is the minimal, pure-decorrelation case, the higher-order ones are it plus that potential. So the layer-2 decorrelation is not a family of look-alikes; it is **one operator** (the divergence-of-a-flux, minimally the Laplacian), differing only in the field it acts on and the mobility $M$:

- **diffusion** — $M$ constant, $\varphi=\rho$ (measured);
- **viscosity** (Navier–Stokes) — $M=\nu$, $\varphi=u$ (the same velocity decorrelation as diffusion, so the kinematic viscosity shares the diffusion constant's substrate origin rather than being merely fitted — the *mechanism* is measured via diffusion; the viscosity coefficient itself is structural, not separately simulated);
- **Ricci / metric-smoothing** (gravity) — $M$ constant, $\varphi=$ the metric field (measured; §7);
- **capacity** (porous-medium / UDM) — the *same* operator with a field-dependent mobility $M(\rho)=M_0(\rho_{\max}-\rho)^\beta$ going degenerate at the bound $\rho_{\max}$.

**Gaussianity is the operator's kernel.** The heat kernel of $\nabla^2$ is a Gaussian, so a field driven by this operator becomes Gaussian; this is the layer-2 walker density, **measured** to Gaussianize. The layer-1 deposit field, which does *not* undergo the smoothing, stays **non-Gaussian** (its structure sits entirely in the Fourier phases, persisting even far past its correlation length — also measured). "Gaussian versus not" maps exactly onto "smoothed versus not": the operator and its absence, measured on both sides.

**The honest split.** Not every layer-2 add is this operator. Incompressibility ($\nabla\!\cdot u = 0$, an elliptic constraint enforced by a nonlocal pressure response) and the conservation laws of the higher-order gradient flows are **global/kinematic constraints**, not gradient-flux smoothings. So the layer-2 add comes in exactly two kinds: **one operator, or one constraint.** The committal, local, hyperbolic substrate supplies neither by building — it builds; the operator forgets and the constraint binds, and both are added at the second step.

## 6. The Edge — What ED Cannot Do, Predicted and Tested

The thesis makes a testable prediction about ED's *bare* rule: a law requiring a *reversible* balance asks the bare substrate to preserve without committing. The sharpest such law is the **soliton** — a localized structure that neither spreads nor decays, dispersion held in perfect balance by a focusing nonlinearity. The prediction is that ED's bare substrate does not build one on its own (a soliton needs a focusing medium it does not supply at the bottom). We tested it.

A localized packet of certified worldlines was evolved under the substrate rule and its width tracked, comparing a sparse packet (weak self-field) against a dense one (strong self-field). A soliton would show the dense packet self-trapping. **The result was the opposite.** Both packets spread diffusively, and the *dense* packet spread *faster* — its own field driving the density back toward the substrate's preferred value, dispersing the core rather than focusing it. Two independent reasons, both measured: the substrate's density-nonlinearity is **defocusing** (the wrong sign for a bright soliton), and the rule is **dissipative**. No balance, no soliton.

This is a **negative result, and it is load-bearing.** A theory that only confirms itself predicts nothing; a theory that names where its bare rule will come up short, and is then confirmed to come up short exactly there, is one that could have been wrong and was not. The soliton is the measured edge of the bare rule, as the proven primality result is the analytic one. It also forces a precise statement of the thesis: the native class is *committal structure-making*, not "structure-preserving in general" — reversible preservation is a third thing, neither made nor smoothed by the bare rule, and it is exactly what the committal substrate does not supply on its own. A soliton is not denied; it needs an added focusing ingredient — a higher layer ED does not provide at the bottom, just as diffusion needs an added decorrelation.

## 7. The Bridge — the Geometric Corner Is Gravity, Measured

The geometric flows (Ricci, mean-curvature) are not a separate conjecture. ED's gravity sector (GR-III) reduces to a **measured** weak-field metric rule, and that rule already *is* the two-layer structure. The dynamical bandwidth rule, simulated in 2D and 3D, is
$$ \dot b \;=\; \underbrace{D\,\nabla^2 b}_{\text{layer-2: smoothing}} \;-\; \underbrace{\kappa\,\rho}_{\text{layer-1: commitment-concentration}}, $$
where $b$ is the bandwidth field that fixes the metric. The first term is the gradient-flux Laplacian of §5 acting on the metric field — in weak field, the linearized form of **Ricci flow** (Ricci flow being a heat equation for the metric). The second is the commitment-concentration sink: matter holds bandwidth and depletes the metric band, and where it wins it drives $b\to 0$ — a **horizon**.

So the geometric corner has the *same competition as Navier–Stokes*: layer-1 concentration against layer-2 smoothing. In vacuum the smoothing wins and the profile is the smooth Schwarzschild form $b = 1 - r_s/r$; at a strong source the concentration wins and a finite-radius $b\to0$ horizon forms. GR-III confirms the Newtonian field equation as the fixed point (correlation 0.999), the linear mass-scaling $r_s\propto M$, the emergent horizon, and its area-law entropy.

The bridge is the payoff. The *same measured rule* produces both the continuum geometric corner **and** the horizon — and the $b\to0$ horizon is, in ED, identically the frozen decoupling cut and the determinability boundary of the information sector. The continuum-PDE map and the horizon/information map are therefore not two results that resemble each other; they are **two faces of one commitment primitive.** Moreover the *mechanism* is shared: the commitment sink drives $b\to0$ in the same way the substrate rule drives the density toward its preferred value $\rho^*$ — a committal drive toward a capacity. The restoring force that dispersed the soliton packet (§6) and the depletion that closes a horizon are the same kind of move, on the capacity axis the gravity sector already isolated ("One Capacity, Two Scales"); the identification is structural, not a claim that the two scales share a numerical value. The honest bound is the gravity sector's own: this is weak-field and khronometric; the full nonlinear Ricci/Einstein flow is the strong-field completion ED supplies only at the khronometric level, not as full General Relativity.

## 8. The Trophy Problems, Honestly

Two of the laws on the map carry Clay Millennium Prizes, and the boundary between what ED contributes and what it does not must be stated plainly.

**Yang–Mills.** ED's gauge sector is a non-abelian lattice gauge theory, and the Yang–Mills action is **derived** (not postulated) from the substrate's coherence-deficit on the plaquette holonomy: the deficit *is* the Wilson action, whose continuum limit is $-\tfrac14\mathrm{Tr}\,F^2$, with the trace form forced by channel indistinguishability. The mass **gap mechanism** then follows in ED's own language: the gap is the signature of *non-commuting channels* — the same coherence-deficit that yields $F^2$ carries the self-interaction for the non-abelian group that the abelian (Maxwell) case lacks, so Maxwell is layer-1 massless and Yang–Mills is gapped.

**Navier–Stokes.** Compressible Navier–Stokes is reached (inertia at layer 1, viscosity at layer 2); incompressibility is the added elliptic constraint, located precisely (§5). The Clay *regularity* question — whether the layer-2 viscous smoothing always defeats the layer-1 inertial concentration — is exactly the layers competition, which gives a *picture* of the problem.

What ED supplies in both cases is **physics**: where the action comes from, why the gap exists, what the regularity question is about. What ED does **not** supply, and this paper does not claim, is the **rigorous-mathematics proof** — the constructive 4D quantum field theory and nonperturbative gap for Yang–Mills, the global-regularity theorem for Navier–Stokes. Those live in disciplines (constructive QFT, PDE analysis) that have resisted the field's best for a generation; the physical mechanisms reproduced here have been known to physicists for decades, and reproducing them is a consilience result *for ED*, not a step toward the prizes. The distinction is not modesty; it is the line whose erasure turns a research program into a crank one.

## 9. Discussion — the Inverted Stack

ED's oldest claim is an inversion of the usual order. In standard physics the reversible micro-laws are fundamental and the arrow is emergent — the second law is nowhere in Newton's equations and must be added by statistics. In ED the **arrow is primitive** and reversibility is the approximation. The map assembled here is that inversion made continuum-wide:

- the laws standard physics calls fundamental-because-reversible — the smooth field, the diffusion limit — are in ED the **arrow-forgotten shadows**, reached only by the second coarse-graining that discards the memory;
- the laws that *keep* the arrow — transport, shocks, the coherent field — are the substrate's **native** output;
- and the laws that need the arrow *absent* — solitons — the **bare substrate does not build on its own** (they need an added focusing ingredient, a higher layer).

One primitive does all of it: it builds (layer 1), it tolerates being forgotten (layer 2, one operator or one constraint), and it leaves some laws to a higher layer it does not supply at the bottom (the edge). The same primitive, in the geometric corner, makes horizons and bounds information. The value of the map is not that ED reaches the continuum — a framework that could reach anything would predict nothing — but that its *bare rule* reaches *this* and not yet *that*, with the boundary drawn by commitment and two points on it established rather than assumed: primality (proven unreachable for finite memory) and the soliton (where the bare rule is measured to disperse).

## 10. Conclusion

The continuum laws of physics sort into three classes by a single primitive. Commitment — the arrow, P11 — is native to the laws that keep its footprint (layer-1 structure-making: transport, shocks, the coherent field), reached-with-one-operator for the laws that forget it (layer-2 dissipation: diffusion, viscosity, Ricci-smoothing, with Gaussianity its kernel and capacity its mobility), not yet building, on its own, the laws that need a reversible balance (the soliton edge — measured: the bare rule disperses, and a soliton needs an added focusing medium), and — in the geometric corner of the same measured rule — the maker of horizons. The diffusive results are coefficient-checked; the geometric results are inherited as simulated; the soliton edge is a measured negative; the trophy-problem contributions are physics, with the proofs disclaimed. The arrow sorts the continuum, and it draws the coastline as well as the land.

---

## Falsifiers

- **A reversible structure ED demonstrably makes by building** — a soliton it self-traps, a delicate balance it holds — would refute "committal structure-making = native."
- **A dissipative law ED produces without the gradient-flux operator or a constraint** would refute the layer-2 account.
- **A layer-2 decorrelation term that is *not* the unique isotropic-local-conservative operator** (an anisotropic or non-flux dissipation generated by the second coarse-graining) would break the "one operator" result.
- **A measured failure of the bandwidth rule's two-term structure** (e.g. horizons forming without the commitment-concentration sink, or smoothing without the Laplacian term) would break the gravity bridge.

## Inheritances and Tiers

Measured (simulated, coefficient-checked): the transport/eikonal shadow; the coherent Coulomb field; the diffusion recovery (Green–Kubo); the Gaussianity door results; the soliton negative; the GR-III bandwidth rule and its consequences. Derived (analytic from primitives): the Yang–Mills action and the gap mechanism. Structural (a reading of an existing or standard rule): the layer placements of Burgers, the higher-order gradient flows, and Navier–Stokes viscosity; the uniqueness of the gradient-flux operator; the weak-field identification of the metric-smoothing term with Ricci flow. Inherited (other ED papers / standard mathematics): the gravity sector (GR-I…GR-IV), the primality edge (finite-memory ceiling), kinetic theory's coarse-graining hierarchy, and the lattice-gauge continuum limit.
