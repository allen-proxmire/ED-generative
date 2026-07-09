# Relational Gravity: The Emergent Metric Is Fixed to g~1/b in 3D by the Holographic Count, with a Gauss's-Law Newtonian Limit and a MOND Nonlinearity

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers, gravity arc (curvature emergence)
**Status:** Publication draft (structural consolidation). Consolidates the curvature-emergence program: how a metric emerges from the participation graph, why it is fixed to g~1/b in 3D, its Newtonian field equation, its relational (background-free) character, and its MOND (not Einstein) nonlinearity. Standalone; cold-reader accessible. Companion to Paper_027 (Newton's G).
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This is not General Relativity.** ED gravity reproduces Newton, the weak-field metric, MOND, and the baryonic Tully-Fisher slope, but it does **not** reproduce Einstein's dynamical-metric field equations. The metric is kinematic and the nonlinearity is MOND (interference), not metric self-coupling. The distinctive, falsifiable claim is MOND-covariantization, **not** GR.
2. **The derivations are self-consistency / fixed-point results, not from-nothing.** They inherit the holographic surface-count (the area-law-as-edge-count, an established ED result but an input here), read bandwidth as the independent-channel count, and (in §4) read a mass as a conserved bandwidth-influence `Q`; these two readings are natural but are readings, not canonical statements. They convert "a natural choice" into "fixed by ED's own holographic principle (a self-consistency)," not "derived from a vacuum." Every "forced/derived" below should be read with this caveat attached.
3. **Values are inherited.** Newton's `G`, the substrate scale `ℓ_P`, and the MOND acceleration `a₀` are inherited from measurement (the `G` identification is Paper_027's); this paper derives the *forms*, not the numbers.
4. **The dimension and topology are primitive.** Three-dimensionality is P06 (a primitive/selection; the reduction program found it selected-not-derived). "Background-free" here means *relational* (the geometry lives on the graph's adjacency, no coordinates); it does **not** mean the topology is derived from nothing, which is a wall.
5. **The clean metric and isotropy are layer-2 (coarse-grained) objects.** The raw substrate is ballistic (layer 1); reading a clean single metric exponent or exact isotropy off raw ballistic transport does not work. The clean results live in the counting derivations (the holographic cut) and under coarse-graining.
6. **The nonlinear equation is characterized, not derived as GR.** The MOND-covariantization form and the identification of its interpolation function with the interference cross-term are a characterization; a fully derived covariant field equation is open (and would still be MOND, not Einstein).
7. **No new primitive is introduced.**

---

## Abstract

Does spacetime geometry emerge from ED's participation graph, and if so, which theory of gravity results? This paper consolidates the curvature-emergence program into one tiered answer. **A metric emerges** from bandwidth-connectivity alone: on a graph where bandwidth enters only through reach, hop-distance defines a metric (fit `R²=1.000`), and a bandwidth depletion (a "mass") reads as *far*, the curvature signature. **The metric is fixed to g~1/b, and uniquely in 3D**: the reach exponent in `reach ~ b^p` is not free but fixed by ED's holographic channel-count (independent channels through a ball's surface scale as the boundary cut `~R^{d-1}`), giving `p = 1/(d-1)`, so `g ~ 1/b^{2/(d-1)}`, a conformal spatial factor that matches GR's weak-field *spatial* sector only in `d=3` (the GR identification is inherited, not re-derived here; the Lorentzian `g_tt` match is separate; measured cut exponents 0.984 in 2D, 2.008 in 3D; emergent metric `R²=1.000`). **The Newtonian field equation is a substrate Gauss's law**: bandwidth conservation plus the same holographic cut give a conserved influence spread over `N(R)~R^{d-1}` channels, so force `~1/R^{d-1}` (inverse-square only in 3D) and potential `~1/R^{d-2}` (Newtonian `1/r` only in 3D). This is an *alternative, kernel-free* route to the `1/r` Paper_027 reaches from the V1 kernel; whether the two are the same mechanism is open (§8), and the only independent empirical content is the cut scaling plus a full-lattice `1/r` solve (`R²=0.998`, rejecting `1/R²` at 0.904). **The gravity is relational**: on a coordinate-free irregular graph, the intrinsic dimension (2.98), the holographic cut, and the field equation (`1/k` Newtonian, from the graph Laplacian) all read out of adjacency alone, with a 2D control returning the 2D Green's function, so the geometry lives on the relations, not an embedding. **The nonlinearity resembles MOND, not Einstein**: the metric is a kinematic read-out of the bandwidth field (acoustic-metric class), so the present account provides no route to Einstein's dynamical self-coupling; the nonlinear term is the interference cross-term `2√(b_loc b_hor)cosΔπ`, whose geometric-mean *modulus* resembles MOND's structure (the sign-indefinite phase factor, and the averaging that would give a monotone interpolation, are open). The honest verdict: ED gravity is a relational, holographically-fixed (self-consistency), 3D-unique `g~1/b` metric with a Gauss's-law Newtonian limit and a MOND (not GR) nonlinearity, with `G`, `ℓ_P`, `a₀` inherited and the dimension a P06 wall. Two caveats are load-bearing and stated up front: the clean metric and field-equation results hold in the *counting / coarse-grained (layer-2)* description, and ED's raw ballistic dynamics has not yet been shown to reach them (an open verification, §7); and on radiative gravity the MOND-not-GR stance makes a sharp, distinctive, and currently-disfavoured prediction: ED does radiate (the scalar bandwidth field), structurally evades the *dipole* catastrophe (its universal `Q ∝ M` coupling is the equivalence principle), and, because its kinematic metric has one radiative degree of freedom, predicts **scalar breathing-mode** gravitational waves rather than GR's spin-2 tensor, a live potential-falsification that LIGO-Virgo polarization data currently disfavour, with the quadrupole *rate* a separate open question (§6). Its distinctive prediction is MOND-covariantization rather than GR, and it aims to explain *why* MOND works: the nonlinearity is amplitude interference (a resemblance in the geometric-mean modulus, with the phase-averaging step still open).

---

## 1. Introduction: Does Geometry Emerge, and Which Gravity?

In a substrate ontology, spacetime geometry cannot be assumed; it must either emerge from the primitive relations or be honestly flagged as postulated. ED's substrate is a participation graph (chains participating in channels at loci), with a bandwidth scalar `b` (participation capacity) on it. The question this paper consolidates: does a metric emerge from that graph, is it fixed to a specific form, what field equation does it obey, is it a fact about the relations or about a chosen lattice, and which theory of gravity results?

The answer, assembled from the curvature-emergence arc, is a clean tiered story. A metric *emerges*, is *fixed* to `g~1/b` uniquely in 3D by ED's holographic channel-count, obeys a Newtonian field equation that is the substrate's own *Gauss's law*, is *relational* (lives on adjacency, not coordinates), and has a *MOND*, not Einstein, nonlinearity because the metric is a kinematic shadow of the bandwidth field. Values (`G`, `ℓ_P`, `a₀`) are inherited, the dimension is primitive (P06), and the sharp clean results are layer-2 (coarse-grained) objects.

Section 3 gives the metric emergence and the `g~1/b` fixing; §4 the Gauss's-law field equation; §5 the relational (background-free) character and the topology wall; §6 the MOND-not-Einstein nonlinearity; §7 the layer structure; §8 the relation to Paper_027; §§9-11 limitations, falsifiers, and the position statement.

## 2. Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| Bandwidth graph + holographic surface-count | P / inherited | Paper_087; the area-law-as-edge-count (Paper_025), an established but input result |
| A metric emerges from bandwidth-connectivity | **measured / structural (layer-2)** | §3, foothold: hop-distance metric, fit `R²=1.000`; raw ballistic dynamics not shown to reach it (§7) |
| Reach law `p = 1/(d-1)` (holographic) | **derived (self-consistency, inherits the cut)** | §3, cut `~R^{d-1}` measured (0.984 in 2D, 2.008 in 3D) |
| `g~1/b` (weak-field spatial factor) uniquely in 3D | **derived (self-consistency)** | §3, emergent metric `q=0.500` in 3D, `R²=1.000`; GR identification inherited, not re-derived |
| Newtonian field eq (Gauss's law, `1/r`, inverse-square) | **derived (self-consistency, layer-2 counting)** | §4; independent content = cut `~R^{d-1}` + full-lattice `1/r` solve; force exponent NOT independent (`F≡Q/N`); "mass=`Q`" a reading |
| Gravity is relational (coordinate-free) | **measured / structural** | §5, intrinsic dim 2.98 + graph-Laplacian `1/k` Newtonian on an adjacency-only graph (2D control decisive) |
| Nonlinearity resembles MOND (interference), metric kinematic | **characterized (account)** | §6, geometric-mean modulus resembles MOND; phase-averaging to a monotone `μ` assumed not shown |
| Reproduces GR (Einstein equation) | **NOT CLAIMED** | preamble 1, metric kinematic, nonlinearity MOND |
| Radiative sector: ED radiates; dipole evaded (equivalence principle) | **structural** | §6; scalar bandwidth radiation, `Q∝M` kills the dipole; probe-confirmed |
| GW polarization: scalar breathing, not GR tensor | **prediction (DISFAVOURED)** | §6, §10.4; one radiative DOF; LIGO-Virgo favours tensor, a live potential-falsification |
| Radiative: scalar quadrupole *rate* vs GR tensor | **OPEN** | §6; separate quantitative question |
| `1/r`-mechanism reconciliation with Paper_027 | **OPEN** | §8; `N(R)` cancels there, sources here |
| Dimension / topology derived | **NOT CLAIMED (P06 wall)** | §5, preamble 4; reduction program: 3D selected-not-derived |
| `G`, `ℓ_P`, `a₀` values | **inherited** | preamble 3; `G` identification is Paper_027's |
| Clean metric / exact isotropy at layer 1 | **NOT CLAIMED (layer-2)** | §7, raw substrate is ballistic |

Every step is P, inherited, measured, structural, derived (self-consistency / layer-2 counting), characterized, or explicitly not-claimed. No step claims GR or a derived dimension.

## 3. A Metric Emerges, and Is Fixed to g~1/b Uniquely in 3D by the Holographic Count

**The foothold: a metric emerges.** Take the participation graph with bandwidth entering *only* through reach (no assigned lengths): a locus of bandwidth `b` reaches to `reach ~ b^p` neighbours, and distance is the unweighted hop-count (BFS) on the resulting graph. The hop-distance is a genuine emergent metric: it fits `∫ dx / b^q` with `R²=1.000`, and a bandwidth depletion (a "mass") reads as *far*, longer hop-distance across it, which is the curvature signature (a mass bends the emergent geometry toward it). Nothing metric was assigned; the metric is read off the bandwidth-connectivity.

**The forcing: p is not free.** The foothold left the reach exponent `p` open (`reach ~ b^p` gives `g ~ 1/b^{2p}`, and `p=½` recovers GR's `g~1/b`, but `p` was hand-picked). ED's own holographic channel-count fixes it. Bandwidth is participation capacity, the number of *independent* relational channels a locus sustains. For a locus reaching to radius `R` in a short-range d-dimensional substrate, the independent channels threading its neighbourhood are the boundary **cut**, the edges crossing the ball's surface, and for short-range edges that cut scales as the surface `~R^{d-1}`, not the volume (this is ED's holographic bound, the area-law-as-edge-count). So a fixed channel budget `b` buys reach `R ~ b^{1/(d-1)}`, giving

$$p = \frac{1}{d-1}, \qquad g \sim \frac{1}{b^{2/(d-1)}}.$$

**Only 3D gives the `g~1/b` factor that matches GR's weak-field spatial sector.** Measured on real lattices: the ball-cut exponent is 0.984 in 2D and 2.008 in 3D (surface, not volume), so `p=1` in 2D and `p=½` in 3D; feeding the *derived* `p` into the emergent-metric measurement gives `g~1/b²` in 2D and `g~1/b` in 3D, both at `R²=1.000`. The emergent `g~1/b` is a **conformal / refractive spatial factor** (`ds² ⊃ (1/b)dx²`, the acoustic-metric class), and it matches GR's **spatial** sector in the weak field; the identification with GR is inherited from the earlier "GR-I" result and is *not* re-derived here, and the Lorentzian `g_tt` sector is a separate, un-established match (an analog/acoustic spatial factor is generic and is not by itself the full Lorentzian metric). So the honest claim is: **3D is the unique dimension in which the holographic reach law gives the `g~1/b` factor that matches GR's weak-field spatial metric**, "unique" being relative to that `g~1/b` target. The length scale `R₀` drops out of the metric exponent (flat across `R₀ = 4..128`); no new scale is introduced, the scale is P08's `ℓ_P` grain, inherited.

This converts "`√b` is a natural choice" into "`p=½` is fixed by the holographic channel-count (a self-consistency, inheriting that count), and only in 3D," tying the `g~1/b` factor to the same holographic principle that gives the area law, and to the number 3 (the same 3 the linking argument independently selects).

## 4. The Newtonian Field Equation Is a Substrate Gauss's Law

The emergent metric relates `g` to `b`, but what sets the `b(R)` profile around a mass? The foothold *imposed* the dip by hand; Paper_027 recovers the `1/r` potential but *inherits* the falloff from the V1 kernel (with the holographic count cancelling). Neither derives the field equation. It is the substrate's own Gauss's law.

- **Conservation (P04).** A mass is treated as a single conserved substrate fact, an influence `Q`, not something each channel carries a separate copy of. (This "mass = conserved bandwidth-influence `Q`" is a natural *reading* of P04 joined to "mass = localized bandwidth perturbation," not a canonical primitive statement, see preamble #2.)
- **The holographic cut.** The independent channels connecting the source to a shell at radius `R` number `N(R) ~ R^{d-1}`, the same surface-count the reach law uses.
- **Gauss's law.** A conserved influence `Q` distributed across `N(R)` channels gives a per-channel flux (force) `F(R) = Q/N(R) ~ 1/R^{d-1}`, and the potential is its radial integral `Φ(R) ~ 1/R^{d-2}` (`log R` in 2D).

So **force `~1/R^{d-1}` (inverse-square only in 3D) and potential `~1/R^{d-2}` (Newtonian `1/r` only in 3D)**, a self-consistency of conservation plus the holographic cut (both inherited). The force exponent comes out `-(d-1)` cleanly (2D `-0.985`, 3D `-1.999`, 4D `-2.956`, all `R²=1.000`), but **this is not an independent measurement**: `F` is *defined* as `Q/N(R)`, so the force exponent is the cut exponent with a minus sign, by construction. The genuinely independent empirical content is exactly two things: (i) the cut scaling `N(R) ~ R^{d-1}` (§3), and (ii) a full-lattice solve of the conservative field equation (a point source on a real 3D lattice), which gives potential `1/R` (`R²=0.998`, rejecting `1/R²` at 0.904). That solve gives `1/R` *because* it is Laplace's Green's function in 3 dimensions, guaranteed by the assumed conservation plus the inherited `d=3`; it confirms the counting and the solver, not anything ED-specific beyond them. So "derived" here should be read throughout as "Gauss's law applied to inherited inputs (the surface cut and the P06 dimension)."

Two consequences. This is a kernel-free route to the same `1/r` Paper_027 reaches from the V1 kernel; whether the two are one mechanism or two is left open (§8), and this section does **not** claim to ground Paper_027's inheritance. And the metric and the field equation come from *one* ingredient, the holographic cut: it fixes both the `g~1/b` factor and the inverse-square law (self-consistency, inheriting the cut), both uniquely in 3D.

## 5. The Gravity Is Relational; the Topology Is the P06 Wall

Are these results facts about the substrate's *relations*, or artifacts of the clean lattice used to measure them? The question splits, and the two halves resolve oppositely.

**Relational (the meaningful sense): yes.** On a *coordinate-free* irregular graph (a random geometric graph with the coordinates discarded after construction, all measurements using adjacency and hop-distance only): the intrinsic dimension reads out of hop-ball growth (`|B(k)| ~ k^d` gives `d = 2.98` on the 3D graph, `1.99` on a 2D control), and the field equation on the **graph Laplacian** (a purely relational operator) returns the dimension-appropriate Green's function, `1/k` (Newtonian) on the 3D graph (form-fit `R²=0.987`, beating `log` and `1/k²`) and `log k` on the 2D control. The 2D control is decisive: the same code, on a graph differing only in intrinsic dimension, returns the *2D* Green's function, so it is the graph's own dimension, not any coordinates, producing the result. ED's emergent metric and Newtonian field equation are **relational**: they live on the participation relations, not on an embedding. The clean lattice was a convenient carrier, not a load-bearing assumption.

**Topology from nothing: a wall.** The graph's *being* three-dimensional is input (here from the construction; canonically P06, a primitive/selection). The reduction program found 3D selected-not-derived, with only a conditional linking candidate. So the arena's dimension is primitive; deriving the topology from a deeper rule is not achieved and is not expected. The honest closure is a partial yes plus a named wall: the geometry *reads* its dimension from the graph (2.98), so the `d` the holographic cut, the reach law, and the Gauss field equation all use is an intrinsic graph fact, not a coordinate artifact, but *which* dimension the graph has stays P06.

## 6. The Nonlinearity Is MOND, and the Metric Is Kinematic (Not Einstein)

The results so far are the static / linear regime. The nonlinear behaviour is where ED gravity announces that it is *not* GR, and the reason is structural.

**The metric is kinematic.** `g~1/b` is a read-out of the bandwidth/participation-density field, the acoustic-metric class (like the effective metric sound sees in a moving fluid). A metric that is a passive read-out of another field is not, in this account, a dynamical field carrying its own Einstein equation; the dynamics live in the bandwidth field, and the metric is its shadow. So the present account provides **no route to** `G_μν = 8πG T_μν` as a fundamental equation (a stronger "structurally cannot" would overreach what the characterization licenses).

**The radiative tension, confronted and partially resolved.** An acoustic/kinematic metric does not obviously radiate energy as self-propagating spin-2 waves, and binary-pulsar orbital decay and gravitational-wave inspirals are **weak-field, radiative** confirmations of dynamical-metric behaviour (matched to GR at sub-percent), *not* extreme-density, so they are not covered by the strong-field hedge of §9. A companion analysis (`CurvatureEmergence_RadiativeSector_...`) takes this on and splits it:

- **ED does radiate.** The worry looks at the shadow, not the field: the bandwidth field `b` propagates retarded (the V1 kernel plus the arrow's finite substrate speed), so `□b = source` has radiative solutions, and a time-varying mass radiates bandwidth waves carrying energy (as density waves do in the fluid analogy). The radiation is **scalar** (`b` is a scalar).
- **The dipole catastrophe is structurally evaded.** Scalar gravity generically has *dipole* radiation, the strongest pulsar killer of scalar-tensor theories. But a mass is a *universal* bandwidth-influence `Q ∝ M`, so the scalar dipole moment `D = Σ Q_i x_i` is `(Q/M)` times the mass dipole, whose second derivative is `d(momentum)/dt = 0` for an isolated binary: no dipole radiation, leading radiation at *quadrupole*, like GR (probe-confirmed: dipole/quadrupole power `~10^{-22}` for universal coupling, reappearing for non-universal). And that universality is not an added assumption, it is ED's *equivalence principle* (the metric is one universal read-out of `b`, so all bodies fall alike and `Q/M` is universal). So ED passes the strongest scalar-gravity pulsar test structurally.
- **The polarization is a sharp, distinctive, currently-disfavored prediction.** ED cannot generate GR's spin-2 tensor radiation: two tensor modes require a *dynamical* rank-2 metric, and ED's metric is kinematic (a read-out of the scalar `b`), so it has *one* radiative degree of freedom. The metric perturbation from any source is `h_ij = -(δb/b²)δ_ij ∝ δ_ij`, pure trace / conformal, which is the **breathing** (spin-0) polarization with zero transverse-traceless part (probe: ED 100% breathing, 0% tensor; GR the reverse). So **ED predicts scalar breathing-mode gravitational waves, not GR's tensor**, the cleanest observational face of "the metric is a shadow, not a field," and it is falsifiable: a network of `≥3` differently-oriented detectors separates scalar from tensor (probe: 3-detector independence 0.52; 2 detectors degenerate, which is why LIGO+Virgo's three-detector network was needed). **Current status: LIGO-Virgo polarization tests (GW170814) favour pure tensor over pure scalar, so ED's prediction is *disfavoured*, a live potential-falsification, honestly a tension, not a pass** (`CurvatureEmergence_TensorQuestion_...`). The quadrupole *rate* (does the scalar coefficient match the observed pulsar decay?) is a separate, unsettled quantitative question.

**The nonlinearity is interference.** ED's gravitational bilocal strain is quadratic (amplitude interference): `|P_loc + P_hor|² = b_loc + b_hor + 2√(b_loc b_hor)cosΔπ`. The diagonal (arithmetic) part is Newton; the off-diagonal (interference cross-term) carries the **geometric-mean modulus** `√(b_loc b_hor)`, which is the structure of MOND's low-acceleration regime. So the coarse-grained nonlinear field equation is plausibly the scalar-tensor MOND covariantization `∇_μ[μ(√(∇Φ·∇Φ)/a₀)∇^μΦ] = 4πG T`, with the interpolation carrying that geometric-mean structure, rather than a metric self-coupling. **This is a resemblance in the amplitude structure, not an equality of functions.** The honest gap: MOND's `μ(x)` is smooth, positive, monotone, and bounded in `[0,1]`, whereas the cross-term carries the phase factor `cosΔπ`, which is sign-indefinite (it can be negative, the "partial-negative" envelope). Recovering a monotone positive `μ` therefore requires a coarse-graining / phase-averaging step that is assumed, not shown; until it is derived, the identification is a structural resemblance in the modulus factor, not `μ = ` the cross-term. This is characterized, not derived as GR (and a fully derived covariant equation would still be MOND, not Einstein).

So ED gravity reproduces Newton (diagonal strain) and the weak-field metric (`g~1/b`, the tested regime), and MOND (off-diagonal interference) with the baryonic Tully-Fisher slope-4 (the galactic low-acceleration regime), and it does **not** reproduce GR's dynamical-metric Einstein equations. The distinctive, falsifiable prediction is MOND-covariantization, not GR, and it *explains* why MOND works: the nonlinearity is amplitude interference and the metric is a kinematic shadow.

## 7. The Layer Structure: the Clean Results Are Layer-2

A caution that is itself a result. The raw ED substrate is a *kinetic lattice-gas* (ballistic transport), the "layer 1" of the two-layer coarse-graining picture. On a genuine 3D lattice with a spherical bandwidth dip, three things hold: a metric emerges and curves; isotropy is *not* exact on the raw graph but *emerges* as reach coarsens (axis/diagonal anisotropy falls to zero, the layer-1 to layer-2 transition); and the clean radial `g~1/b` exponent is *not* extractable from the raw ballistic BFS paths (they are ballistic worldlines on a faceted cubic reach-ball, and a clean single metric exponent plus exact isotropy are layer-2, coarse-grained, objects).

This has a blunt consequence the paper states plainly rather than hides: **the clean `g~1/b` and `1/r` results are established by counting (surface cuts, the Laplace Green's function) and coarse-grained conservative solves, not by running ED's actual ballistic (layer-1) dynamics, which does not display them.** So the accurate claim is "a metric emerges, and `g~1/b` and `1/r` hold, *in the counting / coarse-grained (layer-2) description*"; that the raw ballistic dynamics coarse-grains *to* these is **attributed** to a layer transition, not independently shown. Reading a layer-2 continuum quantity off raw layer-1 ballistic paths would be a layer mismatch, consistent with the two-layer picture, but "consistent with" is not "confirmed by," and the honest test is §10.5: coarse-grain the *real* simulator and check it converges. The clean exponents currently live in the cut-count and the coarse-grained proxy; whether ED's own dynamics reaches them is the open verification.

## 8. Relation to Paper_027 (Newton's G): an Alternative Route, with a Reconciliation Left Open

Paper_027 develops Newton's `G` as `G = c³ℓ_P²/ℏ`, combining the holographic participation-count with a cumulative-strain reading of P12, and recovers `Φ ∝ -M/R` with the per-channel `1/R` falloff taken from the **V1 kernel**, the holographic count `N(R)` *cancelling* at the level of the final potential (Paper_027 §4.4).

This paper's §4 reaches the same `1/R` by a **different route**: the per-channel flux is itself `Q/N(R) ~ 1/R^{d-1}` (no kernel invoked), and `N(R)` *sources* the falloff rather than cancelling. These two accountings are not obviously the same mechanism, and honesty requires flagging the tension rather than papering it:

- In Paper_027 the `1/R` is in the kernel and `N` cancels; in §4 here the `1/R` is `Q/N` and `N` is load-bearing. Both reach `Φ ~ 1/R` in 3D, but via opposite roles for `N(R)`.
- Paper_027 §4.6 explicitly *rejected* a naive area-scaling argument (one that gave `Φ ~ R`, gradient `1`, not `1/R²`); the flux argument here (`F = Q/N ~ 1/R²`) is a *different* construction and is not that rejected one, but the two papers owe a shown (not asserted) identity between the kernel-`1/R`-with-`N`-cancelling route and the flux-`Q/N`-with-`N`-sourcing route.

So the honest statement is **not** "this paper grounds Paper_027's inheritance." It is: **§4 is a complementary, kernel-free derivation of the same `1/r`; whether it and Paper_027's kernel route are the same mechanism or two distinct ones is open.** What is uncontested and complementary: Paper_027 fixes the *value* `G = c³ℓ_P²/ℏ` (with `ℓ_ED = ℓ_P`), which this paper leaves inherited; this paper fixes the *geometry* (`g~1/b`, 3D-unique), the relational character, and the theory (MOND, not GR). The `1/r`-mechanism reconciliation is declared open work.

## 9. Limitations (honest)

- **Radiative gravity: dipole evaded, polarization a disfavoured prediction, rate open (§6).** ED radiates (the scalar bandwidth field is retarded), structurally evades the *dipole* catastrophe (its universal `Q ∝ M` coupling is the equivalence principle), and predicts **scalar breathing-mode** radiation (one radiative degree of freedom from the kinematic metric), *not* GR's tensor. That polarization prediction is sharp and falsifiable but **currently disfavoured** by LIGO-Virgo polarization tests, a live potential-falsification and the paper's most exposed claim. The quadrupole *rate* is a separate, unsettled quantitative question. All weak-field, not covered by the strong-field hedge below.
- **Not GR, and the nonlinear equation is characterized.** The MOND-covariantization is characterized (a resemblance in the geometric-mean modulus, with the sign-indefinite phase factor's averaging step assumed not shown), not derived as a full covariant field equation; strong-field GR (black-hole interiors) is separately speculative, since the kinematic-metric picture may break at extreme density.
- **Self-consistency, inheriting the holographic count and two readings.** The reach-law and Gauss derivations inherit the area-law surface-count and the readings "bandwidth = channel count = cut" and "mass = conserved influence `Q`"; they are fixed-point results, not from-nothing. The `1/r`-mechanism reconciliation with Paper_027 (whether `N(R)` cancels or sources) is open (§8).
- **Values inherited.** `G`, `ℓ_P`, `a₀` are not derived here (`G` is Paper_027's identification).
- **The dimension is primitive.** 3D is P06; background-free is relational-only. The topology-from-nothing sense is a wall.
- **Layer-2 clean results, and a tuning tension.** The clean metric exponent and exact isotropy are coarse-grained objects; raw ballistic transport does not display them, and that ED coarse-grains *to* them is attributed, not shown (§7, §10.5). The irregular-graph cut exponent is noisier than the lattice's (2.38 vs 1.999); and on the irregular graph graph-density cannot simultaneously optimize the cut exponent and the field-equation solve, so the reported run was chosen to favour the load-bearing field equation, at the cost of the inflated cut.

## 10. Falsification Criteria

### 10.1 The metric is not g~1/b, or not 3D-unique

**Falsifier sentence:** *A demonstration that the holographic cut does not scale as `R^{d-1}`, or that the emergent metric under the derived reach law is not `g~1/b` in 3D (or is `g~1/b` in some other dimension), would falsify the metric result (§3).*

### 10.2 The field equation is not Gauss's law

**Falsifier sentence:** *A demonstration that a conserved influence over the holographic channels does not give force `~1/R^{d-1}` and potential `~1/R^{d-2}` (inverse-square and `1/r` in 3D) would falsify the Gauss's-law field equation (§4).*

### 10.3 The gravity is not relational

**Falsifier sentence:** *A demonstration that the emergent metric or field equation cannot be computed from graph adjacency alone (that it requires a coordinate embedding, failing on a coordinate-free graph of the right intrinsic dimension) would falsify the relational result (§5).*

### 10.4 ED gravity is GR (dynamical metric), not the kinematic MOND account

**Falsifier sentence:** *Two live instances. (a) Radiative polarization (the sharpest, and already disfavouring): ED's kinematic metric has one radiative degree of freedom, so it predicts scalar breathing-mode gravitational waves, not GR's two tensor modes (§6). A gravitational-wave polarization measurement establishing pure-tensor radiation (as LIGO-Virgo's GW170814 analysis already favours over pure-scalar), with ED unable to acquire a tensor sector without abandoning the kinematic metric, would falsify ED gravity. This is the cleanest ED-vs-GR discriminator and is not deferrable to strong field. (b) Galactic: rotation curves requiring dark matter rather than the MOND interpolation, or the absence of the deep-MOND regime, would falsify the MOND-covariantization prediction.*

### 10.5 Coarse-graining the real dynamics fails to converge to g~1/b / 1/r

**Falsifier sentence:** *If explicit coarse-graining of the actual ED ballistic simulator (not a separate conservative solve, but the real layer-1 dynamics coarsened) fails to converge to `g~1/b` and the `1/r` potential as the coarsening scale grows, the layer-2 attribution is false, and the clean results would stand exposed as artifacts of the counting/conservative proxy rather than properties of ED's dynamics.* (This falsifies the theory's claim, not merely the layer-mismatch explanation.)

## 11. Position Statement

**ED gravity is a relational, holographically-fixed (self-consistency), 3D-unique `g~1/b` metric with a Gauss's-law Newtonian limit and a MOND (not GR) nonlinearity.** A metric emerges from bandwidth-connectivity; its form is fixed to the weak-field spatial factor `g~1/b` by the holographic channel-count, uniquely in 3D; its Newtonian field equation is the substrate's Gauss's law (conservation plus the same holographic cut), giving inverse-square force and the `1/r` potential; the whole structure is relational (computable from graph adjacency alone, no coordinates); and the nonlinearity resembles MOND in its geometric-mean modulus, because the metric is a kinematic shadow of the bandwidth field and the present account provides no route to Einstein's self-coupling.

**What this paper claims.** The metric emergence (measured, in the layer-2 description), the `g~1/b` weak-field-spatial-factor fixing and 3D-uniqueness (self-consistency, inheriting the holographic cut), the Gauss's-law Newtonian field equation (self-consistency / layer-2 counting; independent content = the cut plus the full-lattice `1/r` solve), the relational character (measured, coordinate-free), and the MOND-resembling, not-Einstein nonlinearity (characterized). Together, a distinctive falsifiable direction: MOND-covariantization rather than GR, aiming to explain why MOND works.

**What this paper does not claim.** GR (the Einstein equation is neither derived nor predicted; on radiative gravity the dipole catastrophe is structurally evaded, but ED predicts scalar breathing-mode GW polarization which LIGO-Virgo data currently *disfavour*, a live potential-falsification, and the quadrupole rate is open, §6/§10.4); a from-nothing derivation (the holographic count and two readings are inherited); that §4 grounds Paper_027's `1/R` (an alternative route; the reconciliation is open, §8); derived values (`G`, `ℓ_P`, `a₀` inherited); a derived dimension (P06 wall; background-free is relational-only); a fully derived covariant nonlinear equation (characterized, with the phase-averaging step open); or that ED's raw ballistic dynamics reaches the clean results (they are layer-2 counting / coarse-grained; the convergence is attributed, not shown).

**Series context.** The curvature-emergence consolidation of the ED gravity arc, and the companion to Paper_027 (Newton's G): where Paper_027 fixes the coefficient `G`, this paper fixes the geometry, the field-equation form, the relational character, and the theory. It uses the same holographic principle that gives the area law and the same primitive the reduction program isolates (the arrow underlies the causal structure; the bandwidth field carries the geometry), and it lands on the same number 3 the linking argument independently selects.

---

## Appendix: Glossary and Reader Map

### Glossary

- **Emergent metric.** Distance = bandwidth-weighted hop-distance on the participation graph; the weak-field spatial factor `g~1/b` in 3D (a conformal factor matching GR's spatial sector, not the full Lorentzian metric).
- **Holographic cut.** The independent channels threading a ball's surface, `~R^{d-1}`; the ingredient that fixes both the `g~1/b` factor and the inverse-square law (a self-consistency, inheriting the cut).
- **Substrate Gauss's law.** A conserved influence spread over the holographic cut gives force `~1/R^{d-1}`, potential `~1/R^{d-2}`; Newtonian `1/r` and inverse-square only in 3D.
- **Relational** (achieved). The geometry is computed from graph adjacency alone, no coordinates; confirmed on a coordinate-free irregular graph (the 2D control shows it is the intrinsic dimension, not coordinates, that drives the result).
- **Background-free, strong sense** (a wall). Deriving the graph's dimension/topology itself; not achieved (P06 primitive). The paper claims only the relational sense, not this one.
- **Kinematic metric.** The metric is a read-out of the bandwidth field (acoustic-metric class), not a dynamical field with its own Einstein equation.
- **MOND nonlinearity.** The nonlinear term is the interference cross-term `2√(b_loc b_hor)cosΔπ`, whose geometric-mean *modulus* resembles MOND's structure (a resemblance, not an equality: the sign-indefinite phase factor and the averaging to a monotone interpolation are open), and is not metric self-coupling.
- **Layer 1 / layer 2.** Layer 1 = raw ballistic substrate (kinetic lattice-gas); layer 2 = coarse-grained continuum, where clean metric exponents and exact isotropy live.

### Reader map

*Intuition.* Put a bandwidth field on a graph and let each locus reach as far as its bandwidth allows. Distances bend where bandwidth is low, so a "mass" (a bandwidth dip) makes nearby space effectively larger: gravity. How fast bandwidth buys reach is set by how many independent channels thread a sphere, which is a surface (holographic), and that one fact fixes both the `g~1/b` metric and the inverse-square force, and only in three dimensions. The whole picture is a fact about the graph's connections, not about any coordinates, and its nonlinearity is the interference of participation amplitudes, which is MOND, not Einstein.

*The distinctive claim.* ED gravity is emergent and acoustic: a kinematic metric on a bandwidth field, relational, 3D-unique, Newtonian in the Gauss's-law limit, and MOND in the nonlinear limit. It predicts MOND-covariantization, not GR, and it says *why* MOND holds. That is a genuine, falsifiable ED-vs-GR discriminator.

**Where to look next.**
- *The coefficient G:* Paper_027 (Newton's G).
- *The interference / MOND mechanism:* the P14 / interference-gravity result.
- *The dimension it lands on:* the minimal-ontology paper (3D selected, linking candidate).

**Open work** (declared): the nonlinear covariant field equation as a *derived* (not characterized) object; the strong-field regime (where the kinematic-metric picture may break); and `ℓ_P` / `r_s`-in-grains (needs `G`, inherited). The static, linear, and relational structure is established; the dimension stays the P06 wall.

---

**End of Paper (Relational Gravity).**

*Gravity arc. A metric emerges from bandwidth-connectivity and is fixed to `g~1/b` by the holographic channel-count, uniquely in 3D; the Newtonian field equation is the substrate's Gauss's law (conservation + the same holographic cut), giving inverse-square force and `1/r` potential; the gravity is relational (computable from graph adjacency alone, confirmed coordinate-free); and the nonlinearity is the interference cross-term, MOND, because the metric is a kinematic shadow of the bandwidth field. Values (`G`, `ℓ_P`, `a₀`) inherited, dimension a P06 wall, clean results layer-2. Distinctive falsifiable prediction: MOND-covariantization, not GR, with an explanation of why MOND works. Companion to Paper_027 (Newton's G).*
