# The Arrow in the Law: Emergent Gravity from a Discrete, Irreversible Substrate

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — program synthesis (gravity line)
**Status:** Self-contained research paper. Presents the Event-Density gravity program — its primitives, its emergent geometry, its weak-field and khronometric structure, its dynamical rule, its horizon thermodynamics, and its open fronts — in one place, for a reader new to the framework. A conditional, falsifiable, tiered account; not a derivation archive.
**Audience:** philosophers of physics, foundations researchers, and mathematically literate theorists.

---

## Abstract

Standard physics places time-symmetric dynamical laws at the foundation and recovers the arrow of time from boundary conditions. This paper presents a research program — **Event Density (ED)** — that inverts that order: the substrate's fundamental law is an *irreversible* act of commitment, so the arrow of time lives in the dynamics rather than the initial data. The paper asks what theory of gravity such a substrate produces, and answers it. From thirteen postulated relational primitives, a Lorentzian metric emerges as the coarse-grained shadow of a discrete "bandwidth" field; the weak-field limit reproduces the Einstein metric, including the factor-of-two light deflection, with the Einstein-versus-Nordström fork *forced* toward Einstein by the irreversibility of commitment. A uniqueness argument (Lovelock's theorem) together with a degrees-of-freedom count shows the emergent gravity is not pure General Relativity but **khronometric** — Einstein's tensor sector plus a single propagating scalar, the *khronon*, which is the arrow of time made dynamical. The dynamical law that governs the bandwidth field is built and simulated; its steady state is the Newtonian field equation, it forms black-hole-like horizons spontaneously, and those horizons carry area-law (holographic) entropy and a Hawking-like temperature scaling. The scalar mode propagates at the speed of light — a derivation, not an assumption — because the substrate's irreversibility makes the relevant sector dissipative rather than kinetic. A massive-particle deflection calculation confirms that matter follows the timelike geodesics of the emergent metric, with the correct relativistic velocity dependence interpolating Newtonian deflection to the factor of two. A recurring structural fact organizes the whole construction: **the same irreversibility selects the Einstein branch at the metric level, makes the khronon a physical mode, and pins that mode to the light cone** — one primitive, three jobs. Throughout, every claim is tiered as *derived*, *measured*, *structural*, *value-inherited*, or *open*. Two numbers and several program-level debts remain honestly open: the preferred-frame post-Newtonian parameters (the theory's sharpest falsification target, structurally suppressed but not computed), the small-scale origin of the modified-dynamics regime, the magnitude of the cosmological constant, the cluster and cosmic-microwave-background sectors, and quantum-information unitarity. The result is offered as a worked example of a generative substrate ontology yielding the structure of general relativity with a principled, falsifiable departure — conditional on its postulates, and consistent with observation where it has been pushed.

---

## 1. Introduction and Motivation

### 1.1 The arrow at the bottom

Most of fundamental physics is built on time-symmetric laws. Newton's equations, Maxwell's equations, the Schrödinger equation, and the Einstein field equations are all invariant under time reversal (or CPT). The manifest asymmetry of the world — that eggs break but do not unbreak, that we remember the past but not the future — is then explained not by the laws but by *boundary conditions*: a low-entropy early universe, the "past hypothesis." On this orthodox view the arrow of time is emergent, statistical, and contingent; the laws themselves do not know which way time points.

This paper develops the consequences of the opposite choice. Suppose the most fundamental thing about the world is not a symmetric equation of motion but an *act*: a discrete, irreversible **commitment** by which what was indeterminate becomes determinate, never to be undone. On this view becoming is primitive, the arrow of time is written into the law, and time-symmetric dynamics — if they appear at all — are coarse-grained approximations several layers up. The program that takes this seriously is called **Event Density (ED)**. It is a member of the substrate-ontology lineage in foundations of physics — alongside 't Hooft's cellular-automaton interpretation and the causal-set and Wolfram programs — in which a discrete, relational substrate underlies the apparently continuous structures of physics.

The question this paper answers is narrow and sharp: **what theory of gravity does such a substrate produce?** Gravity is the right test, because gravity is geometry, and geometry is exactly the kind of smooth, continuous, time-symmetric structure that a discrete and irreversible substrate has no obvious right to produce. If the substrate cannot make a metric, the program fails at the first hurdle. If it makes a metric but the wrong one — no light bending, say — it is falsified. If it makes the right one, the interesting question becomes *where and why it differs from Einstein*, and whether those differences are a liability or a signature.

### 1.2 What the paper claims, and how it speaks

The answer, developed over the following sections, is that the substrate does make a Lorentzian metric; that the weak-field limit is the Einstein metric with the correct factor-of-two deflection; that the full theory is not pure General Relativity but **khronometric gravity** (the infrared limit of Hořava gravity), differing from Einstein by exactly one propagating scalar field; and that this scalar is the arrow of time itself, now dynamical. A single structural fact runs through the construction: the substrate's irreversibility does three apparently independent jobs — it selects the Einstein branch of the weak-field metric, it promotes the scalar mode from gauge to physical, and it keeps that scalar on the light cone. The factor of two, the extra polarization, and that polarization's speed turn out to be one commitment wearing three hats.

A word on register, because it is methodological rather than rhetorical. This is a *conditional* program: every result is conditional on thirteen postulated primitives and on a small number of constants (Newton's constant, the Planck scale) taken from observation rather than derived. ED's working discipline distinguishes the **form** of a physical law (which the program aims to *force* from the primitives) from its **numerical values** (which it generally *inherits* from measurement, on the view that dimensionful constants are global relational facts rather than free parameters). Accordingly, every claim below is tagged:

- **derived** — forced from the primitives or from already-established results, by argument;
- **measured** — established by simulation of the substrate's dynamics, or of their admissible extension;
- **structural** — following from the architecture (e.g., a symmetry or a uniqueness theorem) without model detail;
- **value-inherited** — a number taken from observation, by the program's stated stance on constants;
- **open** — not established, and flagged as such.

This tiering is not hedging. It is what makes the program auditable: a reader can see exactly which load-bearing steps are arguments, which are simulations, which are inheritances, and which are promissory notes. Where a number cannot be computed honestly (the preferred-frame parameters, the magnitude of the cosmological constant), the paper says so and does not fabricate it. A theory that states precisely what it has and has not shown is harder to dismiss than one that overclaims, and that is the intent.

The paper proceeds from the primitives (§2) to the emergent metric (§3), the weak-field Einstein limit (§4), the khronometric class (§5), the dynamical law and its horizons (§6–§7), three recent closing results (§8), the falsification front (§9), the open problems (§10), and the synthesis (§11).

### 1.3 Relation to neighbouring ideas

ED's emergent-gravity result sits near several established programs, and locating it helps. Like Jacobson's "Einstein equation of state" (1995) and Verlinde's entropic gravity (2011), it treats the field equations as emergent rather than fundamental; unlike those, it produces a *specific discrete substrate* and a *specific dynamical law*, not only a thermodynamic relation. Its gravitational class — khronometric — is exactly the one studied in the Hořava (2009) and Einstein-aether (Jacobson–Mattingly 2001) literatures, which is both a constraint (those theories' viability conditions apply) and a resource (their analytic machinery transfers). Its galactic-dynamics sector reproduces the phenomenology of Milgrom's Modified Newtonian Dynamics (MOND, 1983), with the relativistic completion in the manner of the khronometric-MOND constructions (Blanchet–Marsat 2011). And its inversion of the usual order of time — arrow first, symmetry emergent — resonates with Penrose's conformal cyclic cosmology, in which cosmic symmetry is keyed to the absence of relational structure at the temporal endpoints. The novelty is not any single one of these connections but the claim that *one discrete, irreversible substrate yields all of them at once*, with the departures from Einstein concentrated at a single locus. The technical derivations behind each step below appear in companion papers (cited in the references); this paper presents their results and their connective logic, not their machinery.

---

## 2. The Substrate Primitives

### 2.1 The participation graph

ED's fundamental object is not a spacetime but a **participation graph**: a discrete, relational structure of nodes and edges, with no background metric and no fundamental notion of distance. Relations are prior to relata — an isolated node carries no physics; what exists is the pattern of participation among nodes. The framework is specified by thirteen primitives (labelled P01–P13) and two memory kernels (V1, a finite-width retarded kernel; V5, a finite-memory cross-chain kernel). A foundational position paper in the broader ED program states and motivates these; a companion paper audits which primitives are load-bearing for which results. For the present purpose, a reader needs only the handful that carry the gravitational construction, described here in plain terms.

- **P02 — reciprocal adjacency.** Edges are shared, symmetric records: the connection strength between two nodes is a single quantity belonging to both (`b_{ij} = b_{ji}`). This reciprocity is what later makes the emergent spatial metric symmetric.
- **P04 — four-band bandwidth.** Each locus carries a finite "bandwidth" budget, partitioned into four additive bands — among them an *internal/adjacency* band (which will become the metric field), a *commitment-reserve* band (drawn down when commitments fire), and channel-distributed and concentrated bands. Bandwidth is conserved: it is redistributed among bands, never created or destroyed.
- **P05 — transport.** There is a single transport process by which influence propagates across adjacency, at a single maximal speed. This single process is the seed of a single causal cone — the fact that, later, all signals share one light cone.
- **P11 — commitment irreversibility.** This is the arrow. A *commitment* is the act by which an indeterminate degree of freedom becomes a determinate fact; it is monotone and one-way (no "uncommitting"), and it draws bandwidth from the commitment-reserve band and concentrates it. P11 is the single most load-bearing primitive in this paper.
- **P13 — the tick.** Becoming proceeds at a homogeneous rate; there is a fundamental "tick" of commitment, the substrate's intrinsic clock.

The other primitives govern polarity and phase (P09, a U(1) structure), gradient response (P06), spatial homogeneity (P03), and so on. They appear in other sectors of the broader ED program (quantum kinematics, gauge structure, charge) but are not the protagonists here.

### 2.2 Bandwidth, commitment, and the rate law

Two derived structures recur throughout. First, the **bandwidth field** `b`: a non-negative quantity living on edges (P04, P02), measuring the capacity for connection at each link. It will become the metric. Second, the **commitment rate**: the substrate dynamics give a rate at which commitments fire,

> `Γ_commit ∼ b_int / reserve`,

the internal bandwidth over the commitment-reserve budget — a built-in feedback (more available bandwidth, faster commitment; more depleted reserve, the dynamics below). This rate law, and the irreversibility of the reserve drain, do real work in Sections 4 and 6.

### 2.3 Methodology: form forced, value inherited

The program's epistemic discipline deserves an explicit statement, because it shapes every claim. ED aims to *force the form* of physical laws from the primitives — to show that the structure of, say, the gravitational field equation is the only structure the substrate admits — while *inheriting the numerical values* of dimensionful constants from observation. The justification offered for the latter is that, in a relational substrate, a dimensionful constant such as Newton's `G` is a *global relational fact* about the whole structure, not a knob to be tuned; one reads it off the world rather than deriving it from nothing. Results are graded on a three-tier scale by how much is forced versus inherited. A standing discipline, which the broader ED program calls "crank-safety," requires that derivations run *forward* from the primitives, never *backward* from the desired answer, and that every paper open with an explicit statement of what it does *not* claim. This paper honours that discipline in the tiering described in §1.2.

---

## 3. From Primitives to Geometry

### 3.1 The spatial metric from bandwidth

The first task is geometry. In ED there is no fundamental metric; at the scale of the discrete graph there are only edge weights. A smooth metric appears only in the coarse-grained ("thick-regime," or *diffusion coarse-graining*) continuum limit — the same way temperature appears only as a coarse-grained summary of molecular motion. This is a deliberate ontological commitment: the metric is the forgetful summary, the bandwidth field is the fact-level beneath it.

The identification is direct. The spatial metric is the inverse of the bandwidth field,

> `g_{ij} ∼ b_{ij}^{-1}`   *(structural — the natural metric on a graph whose edge weights are connection capacities; symmetric by P02 reciprocity, local by construction, positive-definite in the bulk where `b > 0`).*

Where bandwidth is high, the metric distance is short (nodes are "close"); where bandwidth falls toward zero, the metric distance diverges. This last fact is not a pathology: it is exactly the behaviour of a metric at a horizon, and §7 shows that the locus `b → 0` is simultaneously a metric horizon, a decoupling surface, and a region of saturated memory — one object under three descriptions.

### 3.2 Lorentzian signature: space, cone, and arrow

A metric built from a non-negative bandwidth is Riemannian (positive-definite). The *Lorentzian* signature (the distinction between time and space, and the light cone) must come from elsewhere, and the broader ED program assembles it from three substrate ingredients:

- **space** is `g_{ij} ∼ b_{ij}^{-1}`;
- **the light cone** is the **single maximal transport speed** (P05): finite-speed propagation is precisely what gives an emergent/analogue metric its causal cone, and because there is *one* transport process there is *one* cone — a fact with large consequences in §5;
- **the time-orientation** — which half of the cone is future — is the **arrow** (P11): the irreversible direction of commitment.

Assembled, the leading-order line element is `ds^2 = -c^2 dt^2 + g_{ij}\,dx^i dx^j` *(structural reconstruction from corpus ingredients; the explicit derivation of the cross-terms requires the directed-flux dynamics of §6).* The philosophical point worth pausing on is that the *causal* structure of the emergent spacetime is inherited from the substrate's transport and arrow, not from any Σ-level selection rule — so the emergent light cone and time direction are robust features of the architecture, not delicate model choices.

---

## 4. Weak-Field Gravity

### 4.1 The temporal lapse, and the factor of two

The metric of §3 has a spatial part fixed by `b` and a temporal part — the **lapse** `N`, with `g_{00} = -N^2` — that must be determined. Here the substrate's rate law earns its keep. Requiring the substrate's fastest signal (the maximal-speed front) to be *null* on the emergent metric, together with the commitment-rate law `Γ_commit ∼ b`, forces the lapse:

> `N^2 ∼ b`   *(derived, from the null condition plus the commitment rate).*

This is the crucial new content. The *same* bandwidth field that sets how space curves (`g_{ij} ∼ b^{-1}`) also sets how fast clocks run (`N^2 ∼ b`). Combining them gives the relation between the metric components,

> `g_{00}\,g_{rr} ∼ (-b)(b^{-1}) = -1`   *(derived)*,

which is the **Schwarzschild relation** — the Einstein branch. Combined with the inherited Newtonian limit (the bandwidth Laplacian sourced by matter, `∇^2 b ∼ ρ`, which the program establishes separately and which fixes the vacuum profile `b = 1 - r_s/r`), this assembles the **weak-field Schwarzschild metric**, and with it the three classical tests of general relativity:

- **light bending by the full Einstein factor of two.** The optical index for null propagation is `n_opt ∼ b^{-1}`, the *square* of the spatial-only index `b^{-1/2}`, so the deflection is exactly twice the Newtonian value: the decisive factor distinguishing Einstein's gravity from scalar theories. A self-contained ray-tracing simulation confirms the ratio, **2.09 against the predicted 2.000** (the ~4% excess is a finite-source weak-field curvature artifact, not a deviation). *(derived + measured.)*
- **gravitational redshift**, a free corollary of `N ∼ b^{1/2}`: clocks run slow where bandwidth is depleted. *(derived.)*
- **perihelion precession** for test particles in the derived metric. *(derived for the metric; the claim that massive matter actually follows these timelike geodesics is closed in §8.)*

The historical weight of the factor of two is hard to overstate: it is the prediction that, in 1919, decided between Newton and Einstein, and it kills every theory in which gravity is a scalar field on flat space (those bend light by half the Einstein amount, or not at all). That ED lands on the Einstein value — and lands there because one field sets both space and time curvature — is the program's first genuinely *relativistic* result.

### 4.2 Why Einstein and not Nordström: the arrow's first job

The lapse derivation depends on one labeled assumption, and closing it is the first appearance of this paper's organizing theme. Writing the commitment rate as `Γ ∼ b^{\alpha}`, the Einstein/Nordström fork is the value of `\alpha`: `\alpha = 1` gives Einstein (the Schwarzschild relation), `\alpha = 0` gives Nordström (a conformally flat metric, no light bending, *experimentally excluded*). The value of `\alpha` is set by whether the commitment-reserve band co-scales with the metric band.

It does not, and the reason is the arrow. The reserve and the metric band are different state variables: the metric band is the *ambient* adjacency capacity (shaped by matter), while the reserve is a *carried, monotone-draining budget* set by commitment history (P11; no replenishment). For the Nordström value, the reserve would have to *co-vary* with the metric band, to be raised where the metric band is high, which is replenishment; and replenishment is forbidden by the very irreversibility that defines commitment. So:

> **The P04 band law forces `\alpha = 1`, and Nordström is positively excluded** — by P11 irreversibility. *(derived, modulo a stated band-accounting premise.)*

Had the substrate defined its reserve differently (as a fixed fraction of the total, say), ED would have been a Nordström theory and experimentally excluded. It does not, and so the irreversibility of becoming selects the Einstein branch of the weak-field metric. This is the arrow's first hat.

---

## 5. The Khronometric Reduction

### 5.1 Lovelock, and the one open condition

Section 4 gives the weak-field *metric*; the next question is the *field equation* and the gravitational *class*. Rather than compute the field equation by brute force, the program uses the uniqueness theorem that makes Einstein's equation inevitable. **Lovelock's theorem** states that, in four dimensions, the only symmetric, divergence-free, second-order tensor built solely from the metric is the Einstein tensor (plus a cosmological term). ED has a genuine four-dimensional metric (§3–§4), a covariantly conserved rank-2 matter source (whose conservation, derived from the bandwidth current, turns out to *be* the geodesic equation), and a second-order field law (the Newtonian limit). Three of Lovelock's four hypotheses are therefore met by results already in hand. By the theorem, the field equation is forced to be Einstein's —

> *unless* the gravitational field carries a propagating degree of freedom beyond the metric. *(structural; the field-equation form is forced conditional on one degrees-of-freedom condition.)*

The entire question of whether ED is pure General Relativity reduces to a single condition: a **mode count**.

### 5.2 The arrow's second job: a physical scalar

It does carry an extra mode, and again the arrow is responsible. Because the substrate's arrow lives in the *law* (P11 irreversibility, P13 tick) rather than in boundary conditions, it singles out a preferred time-foliation at the level of the dynamics. This reduces the gauge symmetry from full diffeomorphism invariance to *foliation-preserving* diffeomorphisms — the gauge group of khronometric gravity — and the propagating-mode count becomes **two tensor polarizations plus one scalar**. The scalar is the **khronon**: the preferred-foliation field, which is to say the arrow of time made dynamical. In pure General Relativity the analogous scalar is pure gauge and does not propagate; in ED the arrow breaks the time-reparametrization symmetry that would otherwise remove it, so it survives as a physical mode.

> **ED's gravity is khronometric** — the infrared limit of Hořava gravity: Einstein's two tensor modes plus one physical scalar, the khronon. *(structural — gauge-group + mode count.)* The single departure from textbook General Relativity is the fingerprint of the primitive arrow. This is the arrow's second hat.

### 5.3 Why the departure is survivable

Preferred-frame theories of gravity are easy to build and usually easy to kill: a preferred frame generically makes gravitational waves travel at a different speed from light (excluded to one part in `10^{15}` by the neutron-star merger GW170817), and makes different matter species see different light cones (excluded to one part in `10^{20}` by laboratory Lorentz tests). ED evades both, structurally, for a single reason: *matter and geometry are the same substrate.* Because there is one transport process (P05), there is one causal cone shared by everything, so

- the tensor gravitational-wave speed equals the light speed as an **identity**, not a fine-tuning (`c_T = c`); *(structural.)*
- Lorentz violation is **universal** (one cone for all species) rather than **differential** (different cones), and universal violation is absorbed by a single global rescaling at leading order, invisible to the matter-sector bounds that execute generic Hořava and Einstein-aether models. *(structural.)*

The residual preferred-frame effects — the post-Newtonian parameters `\alpha_1, \alpha_2` — are the genuine falsification target, and §9 treats them honestly. But the leading-order viability that kills most theories of this class is, for ED, a consequence of the single-substrate architecture rather than a tuned escape.

---

## 6. The Dynamical Rule and Its Consequences

### 6.1 Building the engine

Lovelock fixes the *form* of the field equation; the field equation itself is, in ED, the *steady state of a dynamical law for the bandwidth field*. The program identifies this law as the formalization of the commitment-reserve dynamics that P04 and P11 already declare, an admissible extension of the substrate's base dynamics, introducing no new primitive. Its structure is forced (by covariance of the bandwidth current, by the lapse exponent of §4, and by the geodesic structure of §8); its minimal covariant form is

> `\dot{b} = D\,\nabla^2 b - \kappa\,\rho`   *(the rule, with two terms each tied to a primitive).*

The first term, `D\nabla^2 b`, is **P02 adjacency-sharing**: the reciprocal, shared metric band equilibrates across adjacency by the graph Laplacian — the elliptic geometry sector. (This is distinct from, and does not contradict, a separate ED result that the substrate's *matter* transport is kinetic rather than diffusive; Newtonian gravity is elliptic by nature.) The second term, `-\kappa\rho`, is **P11 commitment-concentration**: persistent matter holds bandwidth in its concentrated channel, depleting the metric band in proportion to its density — so `b` is low near matter, the correct sign of gravity. The two coefficients are fixed up to inherited scales: their physical ratio is `\kappa/D = 8\pi G`, the Einstein coupling, which is Newton's constant and therefore value-inherited, while their individual values reduce to the Planck scale (inherited) times dimensionless band-partition fractions (postulated). *(derived that the ratio is `8\pi G`; the coefficients are inherited-plus-postulated, not new numbers.)*

### 6.2 What the engine produces

Built and simulated, the rule delivers — separating what is built into the forced terms from what emerges:

- **the Newtonian field equation `∇^2 b ∼ ρ`** as its steady state (correlation 0.999 between the bandwidth Laplacian and the matter density). This is the fixed point of the two forced terms; its content is that those terms are primitive-grounded, not that Poisson is a surprise. *(measured; fixed-point.)*
- **the Schwarzschild mass-scaling `r_s ∝ M`** — the deficit amplitude is exactly linear in the source, in both two and three dimensions. *(measured.)*
- **a spontaneously forming horizon** (§7), with nothing about a horizon written into the rule. *(measured, emergent.)*
- **the mode count read directly off the dynamical law**: linearizing the rule and analysing its gauge structure reproduces the two-tensor-plus-one-scalar count of §5 by explicit operator analysis rather than by the gauge-group argument alone. *(derived.)*

### 6.3 The arrow's third job, and the unification

The dynamical rule is where the paper's organizing fact becomes fully visible. The same primitive — P11 irreversibility, the arrow — has now done three structurally independent jobs:

1. **at the lapse** (§4): the reserve cannot replenish to track the metric band, so the Einstein branch is forced and Nordström excluded;
2. **at the mode count** (§5): the arrow breaks the time-reparametrization gauge that would freeze the scalar, making the khronon physical;
3. **at the scalar's speed** (§6.4, below): the reserve sector is dissipative, not kinetic, so the khronon stays on the light cone.

One irreversibility, three structural consequences: the factor of two, the extra polarization, and that polarization's speed. *The same arrow that makes the khronon keeps it on the light cone.* This is not a coincidence engineered after the fact; it is the recurring consequence of a single commitment, and it is the strongest structural through-line in the program.

### 6.4 The khronon at the speed of light — a derivation, not an assumption

Generic khronometric theories allow the scalar mode a speed `c_s` different from the speed of light; whether ED's khronon does was, until recently, an open question in the program. It is now settled, and the answer is the arrow's third job. The only candidate for a term that would give the khronon a second cone is the commitment-reserve sector — and the reserve, being monotone and one-way (P11; no replenishment), is *dissipative*, not kinetic. A dissipative coupling enters the wave equation as damping (an imaginary part of the frequency), not as a change of speed (the real part); a conservative kinetic term would shift the speed. Simulation confirms the distinction is physical: a reserve coupling *damps* and eventually *overdamps* the khronon without moving its cone. Therefore:

> **The khronon propagates at the speed of light, `c_s = c`** — a scalar gravitational-wave polarization at light speed, damped near active matter and clean in vacuum. *(derived.)*

This is sharper than generic khronometric gravity (which leaves `c_s` free), and it is observationally distinctive: a *scalar* gravitational-wave polarization travelling at `c` is, in principle, distinguishable both from pure General Relativity (which has only the two tensor polarizations) and from generic preferred-frame theories (which would put the scalar on a different cone). A sub-leading correction from integrating out the dissipative reserve slows the khronon by a tiny, wavenumber-dependent amount that vanishes in vacuum and never produces a distinct propagation cone (confirmed numerically), so the observable far-field prediction is `c_s = c`. *(derived; sub-leading shift measured.)*

---

## 7. Emergent Horizons and Thermodynamics

### 7.1 A horizon that forms itself

Run the dynamical rule with a strong source and something appears that the rule never mentions. The bandwidth field is driven to zero on a *finite-radius surface*: where the local matter-sink outpaces what adjacency-sharing can refill, `b` hits its floor on a sphere, the emergent radial metric component diverges there (`g_{rr} ∼ 1/b → ∞`), and the commitment reserve in that region is exhausted, so the surface is *dynamically frozen*; it cannot reopen. *(measured, emergent.)*

This realizes, by build-and-run, a unification that the program had previously only argued: the locus `b → 0` is *at once*

- a **metric horizon** (where the emergent geometry degenerates),
- an **emergent decoupling surface** (across which the substrate's determinability is severed, a separately established result), and
- a **memory-saturated surface** (the V5-kernel boundary that companion work on black holes identifies with the Hawking-emitting horizon).

One rule, one locus, three identities. The black hole, in ED, is not imposed; it is what the bandwidth field does to itself under concentrated matter.

### 7.2 Area-law entropy

The emergent horizon carries the entropy a black hole should. Across the frozen surface, the substrate's controllable information capacity is *exactly* zero — a separately established "common-cause, not channel" result — so the degrees of freedom hidden behind the horizon are the severed adjacency channels, which live on the *boundary*. Measuring their count across horizons of different size:

> the severed-channel count scales with the horizon **area**, not with the enclosed **volume**: `S ∝ A`, the holographic area law, on a horizon the dynamical rule formed by itself. *(measured; the surface-versus-volume contrast is clean and was a nontrivial test.)*

The numerical coefficient (the famous one-quarter of `S = A/4`) is value-inherited through Newton's constant; the *scaling* — that entropy is a surface and not a bulk quantity — is what the construction delivers.

### 7.3 Hawking temperature scaling

The horizon also has the right temperature scaling, and the way this result was reached is worth recounting because it illustrates the program's discipline. An earlier analysis reported the surface gravity as *flat* with horizon size — the wrong scaling — and located the failure to an unbuilt "strong-field" rule. Asked to build that rule, the honest first step was to re-examine the premise, and the premise was wrong: the earlier analysis had measured a quantity (`∂_r\sqrt{b}`) that *diverges* at the horizon (since the lapse `\sqrt{b} → 0` there) and is therefore meaningless. The correct surface gravity, given the Schwarzschild relation of §4, is `\kappa = \tfrac{1}{2}\,\partial_r b`, which is finite; on the rule's vacuum solution `b = 1 - r_s/r` this gives

> `\kappa = 1/(2 r_s) ∝ 1/r_h` — the Hawking temperature scaling (smaller horizon, hotter), with `r_s ∝ M` measured. *(derived — from the rule's vacuum solution plus the Schwarzschild relation; a fully-direct simulation of the near-horizon slope remains resolution-limited.)*

No new "strong-field" machinery was needed; the negative result had been a measurement artifact, and it was withdrawn. The episode is reported because methodological discipline matters: the willingness to retract one's own result on inspection is exactly what separates a research program from an apologetic. The temperature *coefficient* (`T = \kappa/2\pi`) is value-inherited; the *scaling* is derived.

---

## 8. The Three Closing Derivations

Three loose ends in the construction have recently been closed or precisely located. They are gathered here because together they show the program at its most characteristic: two clean results delivered, and one residual correctly identified as a deep problem rather than fudged.

### 8.1 Matter follows the metric: the massive eikonal

Section 4 derived the metric and showed that *light* follows its null geodesics (the factor of two). The claim that *massive* matter follows the corresponding *timelike* geodesics was, until recently, assumed. It is now computed. Treating a massive ED front as the eikonal (geometric-optics limit) of the bandwidth field, with an index function derived from the metric, one can trace its trajectory past a mass and measure the deflection as a function of velocity. The result reproduces the standard relativistic deflection law,

> `\alpha(\beta) = (r_s/\xi)\,(1 + 1/\beta^2)`,  `\beta = v/c`,

across the whole velocity range: at `\beta \to 0` it gives the Newtonian `1/\beta^2` law (slow particles deflect more), and at `\beta = 1` it gives `2 r_s/\xi`, the factor of two, landing exactly on the independently-established null result. *(measured; the massless limit recovers the proven light-bending result.)* So matter free-falls on the emergent metric with the correct relativistic velocity dependence; the timelike geodesic identity is confirmed at the eikonal level.

### 8.2 The reserve renormalization is benign

The dissipative reserve that keeps the khronon at light speed (§6.4) also, on closer analysis, slightly renormalizes its speed. The computation gives `c_s/c = \sqrt{1 - (\gamma/2ck)^2}` — a tiny, damping-squared-suppressed, wavenumber-dependent shift *below* the light cone, vanishing in vacuum and overdamping (no propagation) near dense matter. *(derived; confirmed numerically where resolvable.)* The upshot is that the correction reinforces rather than threatens the result: the observable, far-field khronon is at exactly `c`, and the substrate never produces a second characteristic cone.

### 8.3 The cosmological constant integral lands on the hard problem

The program identifies the cosmological constant `\Lambda` with the vacuum energy of one of its memory kernels, integrated over the cosmic boundary. Computing that integral from first principles, one finds it is finite, *positive* (the de Sitter sign, confirmed from the substrate side), and proportional to the inverse fourth power of a cutoff scale. *(derived — sign and structure.)* But the *magnitude* rides entirely on which scale: the naive Planck cutoff gives the Planck density — the famous one-hundred-twenty-orders-of-magnitude discrepancy, the cosmological-constant problem — while the observed value requires a specific substrate-cosmology boundary scale that is itself an open derivation within the program. So the ab-initio integral confirms what it can (sign, structure, scaling) and stops at the magnitude, which *is* the cosmological-constant smallness problem. *(open, and explicitly not faked.)* This is the correct negative result: the construction does not fail, but its one remaining number is the hardest open problem in cosmology, and the program declines to manufacture a value for it.

---

## 9. The Falsification Front: `\alpha_1, \alpha_2`

A theory worth taking seriously must be able to lose, and ED's gravity can — at a single, well-defined place. Because ED has a preferred frame (the cosmic rest frame, the khronon's background), it predicts *preferred-frame effects*: a system moving relative to that frame experiences a slightly anisotropic gravitational environment, parametrized in the standard post-Newtonian formalism by two numbers, `\alpha_1` (effects linear in the system's velocity) and `\alpha_2` (quadratic). These are the most tightly constrained parameters of any preferred-frame gravity, bounded by lunar laser ranging and pulsar timing to roughly one part in `10^4` and `10^7` respectively, and they are what generically execute theories of this class.

ED is driven into the maximally-suppressed corner of this parameter space by *five independent, derived* mechanisms: universal (not differential) Lorentz violation makes the parameters sub-leading; both gravitational cones lie at the light speed (`c_T = c`, `c_s = c`); the matter coupling is purely metric (removing the most direct source of `\alpha_1`); and the khronon is *overdamped near matter* (where the relevant near-field is evaluated), so it cannot build the frame-dependent response the parameters measure. Five independent suppression mechanisms, all pointing the same way. *(structural; strong suppression established.)*

But — and this is the load-bearing honesty of the paper — **the values are not computed.** Producing `\alpha_1, \alpha_2` requires either mapping the rule's pinned coefficients onto the standard khronometric post-Newtonian formulas, or a direct post-Newtonian expansion of the dynamical rule; both demand machinery beyond what is established here, and the paper does not fabricate the numbers. The falsification front therefore remains **formally open as a number**: the structural pressure is strongly toward viability, but the verdict awaits the computation. This is, deliberately, the sharpest place the theory exposes its falsification point.

---

## 10. Open Problems and Program-Level Debts

Honesty about what is *not* done is part of the claim. The open items, tiered by character:

- **The preferred-frame numbers `\alpha_1, \alpha_2`** (§9) — the one genuine falsification number, structurally suppressed but uncomputed; needs the khronometric post-Newtonian machinery. This is the live front.
- **The small-scale origin of the modified-dynamics (MOND) regime.** ED's galactic sector reproduces MOND phenomenology with the transition acceleration coming out as the cosmic horizon scale rather than a tuned input, and (in companion work) the khronon supplies the relativistic completion. But *why* the substrate's response goes to the geometric-mean (deep-MOND) form below the cosmic acceleration scale is left as a deliberately unattempted derivation (guarded), the place where reverse-engineering would most easily masquerade as explanation. **Open, and guarded.**
- **The magnitude of the cosmological constant** (§8.3) — the cosmological-constant smallness problem, reached and correctly identified, not solved. **Open; flagged as value-inherited-in-principle.**
- **Clusters and the cosmic microwave background.** Reproducing galactic dynamics is necessary but not sufficient; MOND-class theories famously under-predict cluster masses and must account for the CMB acoustic peaks. ED's cosmological sector (the khronon's expansion-sector behaviour) is *positioned* to carry a dark-matter-like component, and the relevant dial is constrained, but **the cluster and CMB sectors are not discharged.** This is the largest outstanding cosmological debt, and it was never gravity-proper; it lives in the program's cosmology sector.
- **Quantum-information unitarity.** The program reproduces the *structure* of the black-hole information story (a Page-curve-like behaviour) but not full unitary completeness. **Open.**
- **Strong-field solutions.** The construction gives the weak-field metric, the field-equation *form*, and an emergent horizon; the full nonlinear strong-field solutions are not solved. **Open.**

None of these is hidden, and none is fatal on present evidence; together they mark the honest perimeter of the program.

---

## 11. Conclusion

### 11.1 What was shown

Begin with a discrete relational substrate whose one special feature is that becoming is irreversible — the arrow of time written into the law rather than the boundary conditions — and follow it, without tuning, through gravity. What emerges is a Lorentzian metric (the coarse-grained shadow of a bandwidth field), a weak-field limit that is Einstein's with the factor-of-two light deflection, a gravitational class that is khronometric rather than pure General Relativity, a dynamical law whose steady state is the Newtonian field equation and which forms black-hole-like horizons by itself, horizons that carry area-law entropy and a Hawking temperature scaling, a scalar gravitational-wave mode pinned to the light cone, and matter that free-falls on the emergent metric with the correct relativistic deflection. The departures from Einstein are not scattered; they are concentrated at a single locus, the arrow, which selects the Einstein branch at the metric level, promotes the scalar mode to physical, and keeps it on the light cone. One field, one scale, one irreversibility performing three structural roles.

### 11.2 What it means, philosophically

The orthodox order of explanation runs: symmetric laws at the bottom, the arrow of time emergent from a low-entropy past. ED inverts that order and reports what falls out when the inversion is pushed through gravity without flinching. The result is a worked example, conditional on its postulates but carried all the way to simulation, of a generative substrate ontology producing the structure of general relativity together with a principled, falsifiable departure. Whether or not the universe is built this way, the construction establishes something of independent interest: that "the arrow of time is fundamental" is not an idle metaphysical preference but a *productive* one, with specific, derivable, and in places falsifiable consequences for the form of gravity. The smooth, time-symmetric geometry of general relativity appears, on this account, as the forgetful summary of a fact-level that is discrete, relational, and irreversible — as thermodynamics is the forgetful summary of statistical mechanics, one floor down.

### 11.3 The honest standing

This paper has tiered every claim deliberately, and the tiers are the claim. What is *derived* — the lapse, the Einstein branch, the khronometric class, the khronon's existence and its speed, the field-equation form, the mass-scaling, the area-law scaling, the temperature scaling, the massive deflection — is forced from the primitives or measured in simulation of their admissible dynamics. What is *inherited* — Newton's constant, the entropy and temperature coefficients — is taken from observation, on the program's stated view of constants. What is *open* — the preferred-frame numbers, the deep-MOND origin, the cosmological-constant magnitude, clusters and the CMB, unitarity — is named and not fabricated. The theory can lose, and the place it can lose is marked.

That is the most a foundations program can honestly offer at this stage, and it is offered without apology: a single irreversible act, taken seriously, reproduces the architecture of gravity, locates its own departures at the one place it differs from standard physics by construction, and pays its numbers to observation where it cannot yet derive them. It may be wrong; it specifies exactly where to look to find out. And it hangs together, across the weak field, the gravitational-wave sector, the horizon, the thermodynamics, and the scalar mode, on a single idea. Whatever else is true of it, that coherence is real, and it is the reason the program is worth the reader's attention.

---

## References

### Internal (Event-Density corpus)

- Proxmire, A. *The 13 Primitives — Position Paper* (Paper_087); *Form-FORCED / Value-INHERITED Methodology* (Paper_095). Foundational primitives and methodology.
- Proxmire, A. *The Bandwidth Lapse and the Factor of Two: The Weak-Field Einstein Metric in Event Density* (GR-I).
- Proxmire, A. *The Arrow's Fingerprint: Event-Density Gravity is Khronometric, GW-Clean, and Lorentz-Safe* (GR-II).
- Proxmire, A. *The Arrow's Engine: The Dynamical Rule of ED Gravity, and the Closing of Its Weak-Field Assumptions* (GR-III).
- Proxmire, A. *The Arrow's Deep Field: Dark-Matter Phenomenology from the Khronon* (KM-I); *The Arrow's Horizon: The Khronon's Cosmological Face* (KM-II).
- Proxmire, A. *Newton's G as a Substrate Constant* (Paper_027); *Cosmic Decoupling Surface and the Transition Acceleration* (Papers_028–029); *Scalar-Tensor Acoustic-Metric Covariantization* (Paper_033); *Λ as the V1 Cosmological-Scale Integral* (Paper_038.5).
- Proxmire, A. *Common Cause, Not Channel* (capacity/severance); *The Topological Skeleton of Charge*; *Template, Not Escape* (the finite-memory ceiling); *Form and Flesh: The Two Walls* (substrate-evaluation synthesis).

### External

- Lovelock, D. (1971). The Einstein tensor and its generalizations. *J. Math. Phys.* 12, 498.
- Hořava, P. (2009). Quantum gravity at a Lifshitz point. *Phys. Rev. D* 79, 084008.
- Blas, D., Pujolàs, O., Sibiryakov, S. (2010). Consistent extension of Hořava gravity. *Phys. Rev. Lett.* 104, 181302.
- Jacobson, T., Mattingly, D. (2001). Gravity with a dynamical preferred frame. *Phys. Rev. D* 64, 024028.
- Foster, B. Z., Jacobson, T. (2006). Post-Newtonian parameters and constraints on Einstein-aether theory. *Phys. Rev. D* 73, 064015.
- Abbott, B. P., et al. (LIGO/Virgo) (2017). GW170817 and the speed of gravity. *Astrophys. J. Lett.* 848, L13.
- Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation of state. *Phys. Rev. Lett.* 75, 1260.
- Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *JHEP* 04, 029.
- Milgrom, M. (1983). A modification of the Newtonian dynamics. *Astrophys. J.* 270, 365.
- Bekenstein, J., Milgrom, M. (1984). Does the missing mass problem signal the breakdown of Newtonian gravity? *Astrophys. J.* 286, 7.
- Blanchet, L., Marsat, S. (2011). Modified gravity approach based on a preferred time foliation. *Phys. Rev. D* 84, 044056.
- Zlosnik, T. G., Ferreira, P. G., Starkman, G. D. (2007). Modifying gravity with the aether. *Phys. Rev. D* 75, 044017.
- Chamseddine, A. H., Mukhanov, V. (2013). Mimetic dark matter. *JHEP* 11, 135.
- Penrose, R. (2010). *Cycles of Time: An Extraordinary New View of the Universe.* Bodley Head.
- 't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics.* Springer.
- Bekenstein, J. D. (1973). Black holes and entropy. *Phys. Rev. D* 7, 2333.

---

**End of paper.**

*A program synthesis. Event Density posits a discrete relational substrate whose fundamental law is irreversible commitment — the arrow of time in the dynamics. From this, the gravity line derives an emergent Lorentzian metric, the weak-field Einstein structure with the factor-of-two deflection, a khronometric gravitational class differing from General Relativity by one physical scalar (the khronon), a dynamical field-equation rule that forms area-law, Hawking-scaled horizons by itself, and a scalar mode at the speed of light — with the substrate's irreversibility selecting the Einstein branch, the physical scalar, and its light-cone speed in a single structural stroke. Constants are inherited from observation; the preferred-frame parameters and the cosmological-constant magnitude are named open and not fabricated. Conditional on its postulates, falsifiable at a marked front, and coherent across every sector it touches.*
