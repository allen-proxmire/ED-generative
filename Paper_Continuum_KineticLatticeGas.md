# The Continuum Limit of the Certified ED Substrate: a Kinetic Lattice-Gas, not a Diffusion PDE

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (the continuum-limit question)
**Status:** Publication draft. Empirical substrate-evaluation with the certified Σ-rule simulator (`Bits/`). Standalone; cold-reader accessible. *A tested, came-back-no result.*
**Repository target:** `physics-papers/dynamics/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This is a result about the *certified Σ-substrate*, not about all of ED.** The corpus's Q-C boundary PDE and Universal-(Degenerate-)Mobility law (UDM) are *posited* diffusion-class descriptions (Canon P4); whether a **different** ED instantiation is diffusive by construction is **not tested here** and is left open.
3. **No claim that no coarse-graining whatsoever yields a PDE.** The claim is narrower and tested: the certified substrate's *native* continuum is a kinetic equation, and the *two* routes by which a discrete system could become a diffusion PDE — injected noise and emergent mixing — both fail for it. A different observable, instantiation, or limit is not excluded.
4. **The quantitative hydrodynamic closure is measurement-limited, and we say so.** The continuity equation is not cleanly verified by finite differences on this sparse deterministic field. The *clean* results — diffusion exclusion, the ballistic/scattering worldline, the mode-decay scale-stability, the UDM negative — do not rely on that closure.
5. **The UDM negative refutes UDM-from-these-dynamics, not UDM itself.** The certified Σ-dynamics do not *generate* the UDM mobility law; UDM remains a separate ED posit. No claim that UDM is wrong.
6. **One substrate instantiation (the Σ-rule grid), modest sizes.** The absolute R² values are not the result; the **contrasts** are (diffusion ≈ 0; UDM β ≈ 0 not 2; isotropic equilibrium; scale-unstable vs scale-stable coefficient).
7. **No claim that the substrate is "deficient" for not being a PDE.** A continuum PDE is a lossy, coarse-grained summary; this paper argues the substrate is the fact-level *beneath* that summary, not a failed producer of it. The framing is monism with two description-scales, not a value judgment.

---

## Abstract

We ask, empirically and without prior assumption, what continuum law the **certified ED substrate** — the 13-primitive, two-kernel Σ-rule simulator certified by 20/20 correctness gates for the determinability-boundary measurement — generates under coarse-graining. Running it, coarse-graining the event-density field ρ, and regressing against candidate PDE families, we find that the substrate is a **chain/worldline propagator** whose native continuum is a **kinetic lattice-gas** — ballistic worldlines (`|v| ≈ 1`) scattering off ρ-disorder — **not a diffusion PDE**. Diffusion is decisively excluded (`∇²ρ` carries R² ≈ 0.001–0.004 for `∂_t ρ`); ρ is a *slaved deposition field* (`∂_t ρ ∝ φ`, the front density), not an independent field; the collision relaxes to an isotropic equilibrium with a fast relaxation time τ ≈ 1.5 steps. Two quantitative pushes return negatives: the substrate does **not** generate the corpus's UDM mobility law (front mobility is concentration-independent, β ≈ 0, not β ≈ 2, because the strain rule gives *avoidance, not blocking*); and implementing the P04 bandwidth conservation *exactly* (drift `10⁻¹⁶`) does **not** make the current close (R² ≈ 0.01) — so **conservation is necessary but not sufficient**, and the missing ingredient is **scale separation** (τ ≈ transport time). We then test the two routes by which a discrete system could become a diffusion PDE. **Injecting noise** (forcing the thick regime, interpolating the carrier rule from pure Σ-selection to pure random scatter): a clean diffusion PDE (validated `D ≈ 0.25`) appears at **exactly one point** — full random scatter, where Σ-selection has been *deleted* — and for any admixture of the certified rule, transport is sub-diffusive and traps. **Emergent mixing** (pure ED, no injected noise, 300 self-roughening landscapes): pure ED never decorrelates (persistence `p ≈ 0.45`, not the memoryless 0.25), is sub-diffusive, *worsens* with density (the opposite of mixing), and yields a scale-unstable coefficient (CV ≈ 1.2 versus a flawless CV = 0.00, `D = 0.25` control). ED's determinism is **committal/trapping, not mixing/chaotic** — it locks configurations rather than decorrelating them. Both routes agree: **you reach the PDE only by leaving ED.** The smooth PDE layer is a coarse-grained *shadow* of the determinate substrate, not something the substrate casts from within — monism with two description-scales, now empirical rather than argued. This is the program's clearest *tested* (build-and-run, came-back-no) negative, in the same form-yes / precise-law-no shape the wider program keeps finding.

---

## 1. Introduction

### 1.1 What this paper does

ED's case is **generativity** — one small primitive set generating the *form* of physics across domains. The recurring open question, surfaced across the substrate-evaluation program (charge's field, gravity's field equation, the determinability boundary), is whether ED's coarse-graining actually produces the *continuum*, or only ever yields discrete skeletons. This paper answers the cleanest, most falsifiable instance: *take the certified substrate, coarse-grain it, and see what continuum equation it obeys* — letting the data pick the PDE class, with diffusion and the corpus's Q-C PDE treated as hypotheses, not assumptions. It then asks the sharper constructive question: *if the substrate does not natively make a PDE, what would it take to force one, and what would that cost?*

### 1.2 Why this matters

A substrate ontology earns the right to call the continuum a "shadow" only if it can show, concretely, that its own dynamics produce the fact-level beneath the continuum rather than the continuum itself. A negative here — done honestly, with the mechanism named — is more informative than a hoped-for positive: it locates *exactly* where and why ED and the smooth equations of physics part company, and it converts a philosophical claim ("the PDE is a coarse-grained shadow") into a measured one.

*Why diffusion is the right thing to test.* Diffusion (the heat / Fokker–Planck equation) is the **universal hydrodynamic limit**: almost any conservative, locally-equilibrating discrete system coarse-grains to it — the content of the Boltzmann-equation → Chapman–Enskog → diffusion story, reached even by *deterministic* chaotic systems (the Lorentz gas, hard-sphere molecular dynamics) through mixing. It is therefore the most generic PDE a substrate could produce, and the natural one to test. Its *absence* is correspondingly meaningful: a substrate that does not yield diffusion is not merely missing one equation but sits outside the entire hydrodynamic class.

### 1.3 Arc context

This is the substrate-evaluation program's first **tested** (build-and-run, could-come-back-no) substrate result, distinct from the program's many *located-but-open* results. It pairs with the determinability-boundary measurement (same certified instrument) and connects structurally to the gravity arc (§8): the same thin, ballistic, single-speed character that makes ED gravitationally GW-clean is what makes it non-diffusive here.

### 1.4 Regime of validity

Every result is for the **certified Σ-rule on a fixed participation graph** — deterministic dynamics, no rule modification in the characterization (Rounds 1–6), a single explicitly-labeled regime knob in §7 — at **modest grid sizes** (`S = 64`–`121`), with **no thermodynamic / infinite-size limit** and **no long-time steady state** (committed ρ grows unboundedly; fronts extinguish). The conclusions are about *this* instantiation: **no claim is made about other ED instantiations** (the posited Q-C/UDM diffusion model is untested here, §5, §11), nor about observables beyond those measured. The **contrasts** (diffusion ≈ 0; UDM β ≈ 0; scale-unstable vs scale-stable `D`) are the result, not the absolute R².

---

## 2. Primitive Inputs and Method

**Substrate primitives (postulated, Paper_087):** the full 13-primitive, two-kernel Σ-rule, used **as-is**. Load-bearing for the structural facts: P11 (commitment irreversibility — ρ monotone), P04 (four-band bandwidth — the conserved quantity of §6), the orientation-blind Σ-selection (coherence − strain − gradient).

**Instrument:** the certified `Bits/` Σ-rule simulator (20/20 correctness gates). A front commits (increments ρ by a fixed amount) at its Σ-maximal admissible neighbour and advances; node state is `(ρ, orientation)` on a fixed participation graph.

**Method.** Build an `S×S` grid substrate (`S = 121`); seed ρ-profiles (uniform/random, Gaussian, step, ring, gradient) and an ensemble of fronts; evolve; snapshot fields each step. Coarse-grain by block-averaging at multiple block sizes; estimate `∂_t ρ, ∂_t φ, ∇ρ, ∇²ρ, |∇ρ|, ∇·J` by finite differences; regress (least-squares R²) against candidate term-libraries. Instrument the commit log to recover the front-density `φ(x,t)`, front-current `J(x,t)`, merge sink `M(x,t)`, and directional persistence `p`. **No rule is modified** for the characterization (Rounds 1–6); the constructive tests (§7) introduce a single, explicitly-labeled regime knob and validate the Σ computation bit-for-bit against the certified `compute_sigma`.

**No primitive forcing is invoked.** All constructive deviations (the ε knob, §7) are labeled regime changes, not rule changes.

**Reproducibility.** Grids: `S = 121` (characterization, Rounds 1–6), `S = 96` (inject-noise, §7.1), `S = 64` (emerge-noise, §7.2). Coarse-grain block sizes `B ∈ {2, 4, 8, 16}`; spatial and temporal derivatives by central finite differences (`numpy.gradient` stencil). Ensembles: `N = 120` identical-IC runs (§4.3) and `N = 300` independent landscapes (5 families × 60, §7.2). The inject-noise sweep uses `ε ∈ {0, 0.25, 0.5, 0.75, 1.0}` at carrier densities `0.5` and `2.0` per node. The mode-decay coefficient is fit by linear regression of `ln|a_n(t)|` on `t` over the window where the amplitude is above the noise floor, giving `D_n = γ_n/k_n²` at wavenumbers `k_n = 2πn/S` (`n = 1…4` for the scale-stability test). Random seeds are fixed per run. Scripts are listed in the Appendix; the vectorised Σ used in §7 is validated bit-for-bit against the certified `compute_sigma`.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated; certified Σ-rule instrument | P / I | Paper_087; `Bits/` (20/20 gates) |
| Front does not branch (chain/worldline propagator) | **measured** | §3 — direct observation |
| ρ slaved to fronts (`∂_t ρ ∝ φ`, monotone) | **measured** + P11 | §3, §4.1 |
| Diffusion excluded (`∇²ρ` R² ≈ 0.001–0.004) | **measured** | §4.1 |
| Worldline ballistic (`|v|≈1`) + disorder scattering (`D≈1.26`) | **measured** | §4.2 |
| Isotropic equilibrium, τ ≈ 1.5 steps | **measured** | §4.3 |
| Substrate does **not** generate UDM (β ≈ 0, not 2) | **measured** | §5 — strain gives avoidance, not blocking |
| Saturation supplies blocking but not the UDM form (β ≈ 0) | **measured** | §5 |
| Bandwidth conservation exact (drift `10⁻¹⁶`); current still does not close | **measured** | §6 |
| Missing ingredient = scale separation (not conservation) | **D-structural** | §6 — τ ≈ transport time, no Chapman-Enskog split |
| Inject-noise route: clean PDE only at full scatter (`D=0.25`) | **measured** | §7.1 — ε-sweep + mode-decay (`D` self-validates at ε=1) |
| Emerge-noise route: pure ED never mixes (trapping, scale-unstable) | **measured** | §7.2 — 300 landscapes; CV ≈ 1.2 vs control 0.00 |
| "Reach the PDE only by leaving ED"; two description-scales | **interpretation** | §9 — supported by §7 |
| Single-cone cross-program connection | **observation** | §8 — structural link to the gravity arc, labeled |
| Quantitative continuity closure | **measurement-limited** | §4.3, §6 — not relied on for any clean claim |

All steps are P, I, measured, structural, interpretation, or labeled measurement-limited. *The clean claims are the contrasts (diffusion ≈ 0; UDM β ≈ 0; mixing CV ≈ 1.2 vs 0.00); the one soft spot (continuity closure) is flagged and load-bearing for nothing.*

---

## 3. The Structural Facts That Frame Everything

Two directly-verified facts reshape the question before any regression:

- **The certified front does not branch.** One seed → exactly one active front after many steps, depositing ρ along a **1-D chain (a worldline)**. The Σ-rule is a *chain propagator, not a field-update rule* — so a "ρ-field PDE" is the wrong object for a single front.
- **ρ only changes where a front commits.** ρ is monotone and grows by a fixed increment at each commit (P11), so `∂_t ρ` is the commit-deposition footprint: **ρ is a deposited field slaved to the fronts**, not an independent dynamical field. (To be precise: ρ *does* evolve deterministically — but only *through* front deposition; it has no independent evolution law of its own, which is exactly why no closed equation in ρ alone can exist.)

These two facts already predict that no closed ρ-only PDE can exist; the measurements confirm it.

---

## 4. The Continuum is Kinetic, not Diffusive

### 4.1 Diffusion is excluded; no closed ρ-PDE

Coarse-graining ρ from a front ensemble and regressing `∂_t ρ`:

| IC | diffusion `∇²ρ` | eikonal `|∇ρ|` | diff+eik | PME/UDM |
|---|---|---|---|---|
| uniform | 0.004 | 0.001 | 0.005 | 0.009 |
| gaussian | 0.001 | 0.065 | 0.065 | 0.062 |
| step | 0.001 | 0.094 | 0.095 | 0.095 |
| ring | 0.001 | 0.057 | 0.059 | 0.045 |

**Diffusion is decisively rejected** (R² ≈ 0.001–0.004). No closed ρ-only PDE fits (best ≈ 0.10, a weak transport term) — structural, per §3.

### 4.2 The worldline: ballistic free-flight + disorder scattering

Single-chain statistics on controlled landscapes:

| landscape | metric | value | reading |
|---|---|---|---|
| flat / constant ρ | drift `|v|` | **1.00** | ballistic (max speed) |
| ρ-gradient | drift `|v|` | 0.98 → 0.87 | still ballistic; gradient is a weak modulation |
| random ρ | diffusion `D` (MSD = 4Dt) | **≈ 1.26** | scattering off disorder |
| smooth | persistence `p` | **0.68 / 0.73** | ballistic free-flight |
| random | persistence `p` | **0.36** | collision-dominated |

The front is a **ballistic particle scattering off ρ-disorder** (a Lorentz-gas/kinetic picture): free flight at `v ≈ 1`, randomized by landscape *roughness* (not its gradient). The deposition closure holds (`∂_t ρ ∼ 0.6·φ`, R² 0.23–0.34); the continuity closure is not cleanly verifiable (R² 0.04–0.15), and Round 3 falsified the "merging breaks continuity" hypothesis (merging is ≈1%, negligible), locating the residual as **measurement-limited** (binary-per-node φ, sparse deterministic ensemble, mismatched space-time coarsening; the closure improves then degrades with block size — the fingerprint of an artifact, not a conservation failure).

### 4.3 The kinetic equilibrium is clean

Ensemble averaging (N = 120 identical-IC runs) + matched space-time coarsening + velocity-resolved front populations `f_d`: the collision relaxes to a near-**isotropic equilibrium** (`f_d ≈ [0.25, 0.25, 0.26, 0.23]`, anisotropy 0.044) with **τ ≈ 1.5 steps**. The BGK *structure* is well-defined; the system sits near its over-damped limit — but, crucially, τ is *comparable to* the transport time (§6).

---

## 5. The Substrate Does Not Generate the UDM Law

The Universal-Mobility hypothesis is that the strain rule (fronts avoid high ρ) is the microscopic origin of the mobility-capacity bound `M(ρ) = M₀(ρ_max − ρ)^β`, β ≈ 2. Measuring front mobility against background concentration `c` (built over time, ensemble-averaged over millions of front-steps):

> mobility is **flat at ≈ 0.36, concentration-independent** — UDM fit `(1 − c/c_max)^β` gives **β ≈ −0.08, R² 0.29**, against the canonical β ≈ 2.

**The certified Σ-substrate does not generate UDM.** The reason is clean: the strain term produces **avoidance, not blocking** — a front always commits to *some* neighbour every step, so there is no mobility degeneracy. UDM's "mobility vanishes as `c → c_max`" requires a *blocking* mechanism the substrate (as run) lacks.

**The one blocking mechanism — saturation/extinction — supplies the degeneracy but not the form.** Turning on the certified extinction threshold (fronts die where Σ falls below threshold, i.e. in dense regions): the extinction rate **rises with concentration** (`0.026 → 0.244` as `c` ≈ 0.1 → 1.1) — genuine concentration-dependent blocking, the qualitative UDM ingredient — but the effective mobility is **non-monotonic** and the UDM fit gives **β ≈ 0.05, R² 0.16**, not β ≈ 2. So **saturation supplies the blocking UDM needs, but the resulting transport does not have the UDM functional form** (sharp threshold not smooth reduction; unbounded committed-ρ so no fixed `c_max`). UDM is *qualitatively related* to the saturation regime but *not quantitatively generated* by it; it remains a separate posit.

**This negative applies specifically to the certified Σ-rule.** A *different* ED instantiation — in particular the posited Q-C / UDM diffusion model (Canon P4) — could generate UDM by construction; that is **not tested here** and is explicitly left open (preamble 2, §11). The claim is "the certified Σ-dynamics do not generate UDM," not "ED cannot."

---

## 6. Conservation is Necessary but Not Sufficient

The natural diagnosis is that ρ does not close *because it is not conserved* (a monotone deposit; P11 forbids draining it). ED's actual conserved quantity is **bandwidth** — P04's four-band budget, where commitment draws from the commitment-reserve band and concentrates it, conserving the total. Implementing this faithfully (each front carries a reserve, commits a fixed quantum, exhausts when depleted) and coarse-graining the **conserved** field:

- **Conservation is exact** (drift `1.6 × 10⁻¹⁶`).
- **The current still does not close.** The constitutive test `J = a·m·∇d − D·∇m` gives R² ≈ **0.01** — no Fickian/advective closure.
- **Continuity does not even verify** at the coarse level (R² ≈ 0.04) *despite exact microscopic conservation* — the residual measurement wall.

**To be unambiguous: no claim is made that the substrate violates continuity.** Microscopic conservation is exact (drift `10⁻¹⁶`). The claim is only that the coarse-grained finite-difference estimator cannot *verify* a tight local balance on this sparse, deterministic field — the failure is in the measurement, not the physics (it is load-bearing for nothing; the clean results of §4, §5, §7 do not rely on it).

**Conservation was the wrong suspect.** The conserved quantity is *transported kinetically*, along the same ballistic-plus-scattering worldlines, with no constitutive closure. A discrete system coarse-grains to a PDE when it has five ingredients; measured against the substrate:

| Ingredient (why a PDE needs it) | Certified Σ-substrate |
|---|---|
| **Conservation** (continuity equation) | absent for ρ (P11); **addable for bandwidth** (P04) — done exactly |
| **Local equilibrium** (a state to relax to) | **present** — isotropic `f_d` (§4.3) |
| **Scale separation** (collisions ≪ transport) | **absent** — τ ≈ 1.5 ≈ transport time; no fast/slow split |
| **Isotropy** | absent — square lattice + tie-break |
| **Steady regime** | absent — never steady (ρ → ∞, fronts die) |

**The missing ingredient is not conservation — it is scale separation.** The substrate *has* a local equilibrium, but it relaxes on the timescale it transports, so there is no limit in which the current collapses to `J = −D∇`. A PDE-generating ED substrate would need the **thick, over-damped regime** (τ ≪ transport time) — structurally a **lattice-Boltzmann fluid** (many collisions per transport step, the discrete scheme that *does* yield Navier–Stokes), the *opposite* end from the certified substrate's thin, ballistic, determinate character. **ED makes facts; fluids relax; those are opposite limits of one architecture.**

(On isotropy specifically: the square lattice's anisotropy is **structural** — it cannot be removed without changing the substrate's graph — so it is a genuine limitation of *this* instantiation, not a measurement artifact. It is, however, not the load-bearing obstruction; scale separation is, and it fails even in the measured isotropic equilibrium, §4.3.)

---

## 7. Both Bridge Routes Fail

A discrete system can become a diffusion PDE by exactly two routes: **injected** randomness, or **emergent** mixing (deterministic-but-chaotic, as in molecular dynamics). We test both. Both fail, and they fail in the same direction.

### 7.1 Inject noise — the PDE appears only when the rule is deleted

Force the thick regime (high density, isotropy, periodic steady arena, exact bandwidth conservation) with a single knob **ε** on the carrier-hop rule: ε = 0 is pure certified max-Σ selection; ε = 1 is a uniformly random hop (a conserved random walk — diffusion by construction). The local Fickian regression is shot-noise-limited (≈ 0 even at ε = 1, where the answer is known), so the verdict rests on a **global mode-decay** instrument (seed a cosine density mode, watch `a(t) = a₀ e^{−Dk²t}`), which self-validates: at ε = 1 it returns `D ≈ 0.23` — the analytic 2D random-walk value `1/(2·dim) = 0.25` — with decay-R² ≈ 0.99, α ≈ 1, p → 0.25.

The result is monotone *against* ED: a clean, coefficient-correct diffusion PDE exists at **exactly one point, ε = 1**, where Σ-selection has been wholly replaced by scattering. For any ε < 1 with the certified rule still steering, transport moves *away* from diffusion — the intermediate regime is the worst (non-exponential decay, sub-diffusive α ≈ 0.1–0.33). The mechanism is explicit: Σ always selects the **coherence optimum** — which tends to be a local minimum of disorder (the `ρ ≈ ρ*` basin) — and the monotone P11 footprint then **pins** the carrier there; repeated selection therefore *funnels* carriers into basins rather than *decorrelating* them, the precise opposite of a collision operator's randomizing action. **Σ-selection is a *trapping* operator, not a *collision* operator.** A diffusion PDE needs relaxation; the substrate supplies commitment. The thick regime that *does* give a PDE is reached only by deleting the selection rule. *The price of the PDE is the whole ED character.*

### 7.2 Emerge noise — pure ED never mixes

Injected noise is not the only road: deterministic molecular dynamics coarse-grains to diffusion with *no* injected noise, through **mixing** (chaotic decorrelation). Determinism per se does not block a PDE. So the decisive question is whether **pure ED (ε = 0)** generates its *own* mixing on rough, self-roughening landscapes. The discriminator is **scale-stability of the diffusion coefficient**: diffusion has `γ(k) = D·k²` exactly, so `D = γ(k)/k²` must be flat across wavenumbers. Across 300 independent landscape families:

| signature | pure ED (sparse) | pure ED (dense) | diffusion needs |
|---|---|---|---|
| persistence `p` | 0.40 → 0.47 | 0.49 → 0.49 | → 0.25 |
| MSD exponent α | 0.93 | **0.57** | ≈ 1 |
| `D` scale-stability (CV) | **1.29** | **1.09** | < 0.15 |

(ε = 1 control: `D_n = [0.250, 0.251, 0.251, 0.251]`, CV = 0.00, α = 1.00, p = 0.25 — the instrument detects a true shadow unambiguously when one exists.) **Pure ED shows none of it.** Persistence never decorrelates; transport is sub-diffusive; the coefficient is scale-unstable. The **density trend is the dagger**: higher density makes ED transport *more* trapped (α 0.93 → 0.57) — the exact opposite of mixing, where density *cleans up* diffusion. ED's interactions are not collisions; they are competitions for commitment that **lock** the configuration. ED's determinism is **committal/trapping, not mixing/chaotic.**

Both routes return the same verdict: **inject noise** reaches the PDE only by erasing the rule; **emerge noise** never reaches it at all. *You reach the PDE only by leaving ED.*

---

## 8. Cross-Program Connection: the Same Thinness

The substrate's character here — **thin, ballistic, single-speed** worldlines that do not relax — is the *same* structural fact that governs ED's gravity. In the gravity arc the substrate's single transport (P05) and single maximal speed give it **one causal cone**, which makes its gravitational-wave sector clean (`c_T = c` structurally) and its Lorentz violation universal-not-differential. Here that same single-speed ballistic character is exactly why the substrate *cannot* relax into a diffusion PDE: a fluid needs many speeds thermalized into an over-damped local equilibrium, which is the opposite of one ballistic cone. So the thinness that is a *virtue* in the gravitational sector (a clean single cone) is the *obstruction* in the hydrodynamic sector (no over-damping, no mixing). One architectural property, two faces — stated here as a structural observation across the two arcs, not a derivation.

---

## 9. Interpretation: Two Description-Scales, not Two Realities

The smooth PDE layer is **not a shadow the certified Σ-substrate casts from within** — neither by injected noise nor by emergent mixing. It belongs either to a *different* ED instantiation (the posited Q-C/UDM diffusion model) or to the externally-imposed randomness that *erases* the substrate. This is **monism with two description-scales** — the substrate is the fact-level beneath, the continuum is its forgetful coarse summary (as statistical mechanics is to thermodynamics) — **not two layers of reality.** What is new is that this is now *empirical*: the determinate substrate has been shown, by build-and-run, not to relax into the continuum's smooth law. The native object — *worldlines with a current* — sits on the geodesic/kinetic side, consistent with the wider finding that **geometry** (geodesic motion, the emergent metric) is the natural emergence from this substrate. **The substrate makes trajectories first; fields are what their density makes.**

This is the same shape the wider substrate-evaluation program keeps returning: **form/qualitative-structure yes, precise quantitative law no** — here in the continuum-limit register, and as the program's clearest *tested* negative.

---

## 10. The Method Self-Corrected (and that is the point)

The characterization is a chain of honest corrections: **R1** read the single chain as drift-diffusion driven by ∇ρ; **R2** showed it is ballistic free-flight + disorder scattering (gradient a weak modulation), and that ρ-only does not close; **R3** falsified R2's merging diagnosis and located the residual continuity failure as measurement-limited. Each round overturned the previous round's *interpretation* while preserving its *data*. The robust core that survived all three: chain/worldline propagator → ballistic + scattering → slaved ρ → not diffusion.

---

## 11. Limitations (honest)

- The continuum is characterized *qualitatively* (kinetic, not diffusive); a closed continuum equation was **not** verified *quantitatively* — even ensemble + matched-coarsening left continuity at R² ≈ 0.15, degrading with scale. The substrate may simply not admit a clean local hydrodynamic closure (it never reaches a steady hydrodynamic regime — ρ grows unboundedly).
- The UDM negative was measured for the certified Σ-dynamics; it refutes UDM-from-these-dynamics, not UDM as a posit.
- One substrate instantiation, modest sizes; the **contrasts** are the result, not the absolute R².
- Whether a *different* ED instantiation (the Q-C PDE model itself) is where UDM/diffusion is generated is open and not tested.

---

## 12. Falsification Criteria

### 12.1 A clean diffusion PDE from the certified substrate

**Falsifier sentence:** *A demonstration that the certified Σ-substrate (ε = 0, no injected noise) coarse-grains to a clean diffusion PDE — a scale-stable diffusion coefficient (CV ≲ 0.15) and a diffusive MSD exponent (α ≈ 1) — on any observable, would falsify the §7 verdict that pure ED does not cast its own diffusion shadow.*

### 12.2 Diffusion (or a closed ρ-PDE) recovered

**Falsifier sentence:** *A coarse-graining of the certified ρ field yielding `∂_t ρ ≈ D∇²ρ` (or any closed ρ-only PDE) with substantial R² would falsify §4.1's exclusion of diffusion and the slaved-ρ structural claim.*

### 12.3 UDM generated by the certified dynamics

**Falsifier sentence:** *A measurement showing the certified Σ-dynamics generate the UDM mobility law (`(1 − c/c_max)^β` with β ≈ 2, R² high) — with or without saturation — would falsify §5.*

### 12.4 Mixing without injected noise

**Falsifier sentence:** *A demonstration that pure ED (ε = 0) decorrelates (persistence → 0.25) and produces a scale-stable coefficient as density increases — i.e. mixes like a chaotic deterministic system — would falsify the committal/trapping characterization (§7.2).*

### 12.5 The density trend reverses

**Falsifier sentence:** *Observation that higher carrier density makes pure-ED transport *more* diffusive (α → 1) rather than more trapped (α → 0.57) would falsify the "dagger" result and the trapping mechanism.*

---

## 13. Position Statement

The **certified ED substrate is a kinetic lattice-gas**, not a diffusion PDE. Its native continuum is a Boltzmann-class kinetic equation — ballistic worldlines scattering off ρ-disorder, depositing a slaved event-density field. Diffusion is decisively excluded; the substrate does not generate the UDM mobility law (a separate posit); and the hydrodynamic closure does not exist because the substrate lacks **scale separation**, not conservation.

**What this paper claims.** The certified substrate is **qualitatively generative** (kinetic transport, isotropic fast-relaxing equilibrium, saturation-driven mobility degeneracy) and **quantitatively non-generative** under the methods tried (no clean continuum PDE; no UDM law). The two routes to a diffusion PDE — injected noise and emergent mixing — both fail: the PDE is reachable only by deleting ED's determinate selection. The continuum is the coarse-grained shadow of the determinate substrate; *you reach the PDE only by leaving ED.*

**What this paper does not claim.** The primitives are not derived; this is the certified Σ-substrate, not all of ED; a different instantiation is not excluded; the quantitative continuity closure is measurement-limited; and the substrate is not "deficient" for not being a PDE — it is the fact-level beneath one. Monism with two description-scales, now empirical.

**Series context.** The substrate-evaluation program's clearest tested negative, pairing with the determinability-boundary measurement and connecting structurally (§8) to the gravity arc's single-cone result.

---

## Appendix — Artifacts and Glossary

### Artifacts (certified Σ-simulator scripts; `evaluation/CoarseGrain_Arc/`)

- `coarsegrain_test.py` … `coarsegrain_round5.py` — Rounds 1–5 (PDE-class regression; `(ρ,φ,J)` closure; merge sink + persistence; ensemble + matched coarsening + UDM test; saturation/extinction UDM-form test).
- `bandwidth_conservation_test.py` — Round 6 (exact P04 bandwidth conservation; conserved-field closure).
- `thick_regime_test.py` — inject-noise route (ε-sweep Σ-selection → random scatter; mode-decay instrument).
- `shadow_emergence_test.py` — emerge-noise route (pure ED; multi-mode scale-stability over 300 landscapes; ε = 1 calibration).

### Glossary

- **Certified Σ-substrate.** The 13-primitive, two-kernel simulator (`Bits/`), certified by 20/20 correctness gates.
- **Kinetic lattice-gas.** Ballistic worldlines (`|v| ≈ 1`) scattering off disorder — a Boltzmann-class kinetic picture, not a diffusion PDE.
- **Slaved ρ.** The event-density field is a deposition footprint of the fronts (`∂_t ρ ∝ φ`), not an independent dynamical field.
- **Scale separation.** Collision time ≪ transport time — the Chapman-Enskog small parameter a PDE closure needs; **absent** here (τ ≈ transport time).
- **Trapping vs collision operator.** Σ-selection drives carriers to the coherence optimum and freezes them (trapping), the opposite of the decorrelating collisions a diffusion PDE integrates.
- **Inject-noise / emerge-noise routes.** The two ways a discrete system can become a diffusion PDE — added randomness, or emergent chaotic mixing — both of which fail for the certified substrate.
- **UDM.** The Universal (Degenerate-)Mobility law `M(ρ) = M₀(ρ_max − ρ)^β`, β ≈ 2; a separate ED posit, not generated by the certified Σ-dynamics.

### Reader map and open work

*Intuition — why ED is thin.* ED's determinism and single-speed transport make it **thin**: it produces *trajectories*, not *relaxation*. A fluid needs many speeds thermalized by collisions into a slow hydrodynamic mode; ED has one speed and committal selection. That is the whole reason it makes facts (worldlines) rather than fields (relaxed averages) — and §8's connection to gravity is the same fact wearing the opposite hat.

**Where to look next.**
- *The determinability-boundary measurement (same instrument):* the Bits determinability paper.
- *The gravity connection (the same thinness → single causal cone):* GR-II §6–§8.
- *The UDM / Q-C diffusion model:* Paper_033 and Canon P4.
- *The substrate primitives:* Paper_087.

**Open work** (declared): test other ED instantiations — especially the Q-C/UDM model — for diffusion; larger grids and the thermodynamic limit; alternative observables; multi-front interaction regimes; and whether *any* coarse-graining of this substrate closes into a local hydrodynamic equation.

---

**End of Paper (Continuum Limit).**

*Substrate-evaluation arc. The certified ED substrate coarse-grains to a kinetic lattice-gas, not a diffusion PDE; diffusion excluded, UDM not generated, hydrodynamic closure blocked by missing scale separation. Both routes to a PDE — inject noise, emerge mixing — fail: the PDE is reachable only by deleting ED's determinism. The continuum is the coarse-grained shadow of the determinate substrate. A tested, came-back-no result.*
