# The Event Density Dark Sector: MOND as Horizon Interference, a Warm Relic for the Cosmic Web, and a Falsifiable Bet Against Cold Dark Matter

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — dark-sector flagship. Self-contained and cold-reader accessible; it consolidates the ED dark-sector program into one peer-facing statement (companion construction: `Paper_ED_RelicLagrangian_v1`).

**Status: research paper, honestly tiered.** One standing result (MOND as a horizon-interference cross-term), two derived results (the relic's `a⁻³` dust from commitment-irreversibility; the relic self-interaction is canonical, so the sector is two-component), one consistency bound (the relic is warm, `~keV`), and one named limit (the `keV` scale is inherited, and no ED spectrum is computed). The headline is a falsifiable prediction: **ED's dark matter is warm, not a cold WIMP.**

---

## Preamble — What This Paper Does NOT Claim

1. **It does not claim to compute the CMB power spectrum or fit cluster profiles from ED.** It writes down the sector's action and its qualitative content; the Boltzmann computation is downstream and named as such (§8).
2. **It does not derive the relic's mass or abundance.** Both are value-inherited, at the same tier as the baryon-to-photon ratio `η_B` (Paper_ED_Baryogenesis). The mass is *bounded* by consistency (§5), not pinned.
3. **It does not derive the `keV` scale.** No ED mechanism supplies it; this is the framework's general mass-value limit, not a dark-sector-specific gap (§6).
4. **It does not claim primitive-forcing.** "Form-fixed" means conditional on the ED primitives plus the standard effective-field-theory reading. Where a result is a coarse-graining of ED's own coherence kernel it is marked *derived*; where it composes standing corpus papers it is marked *structural*; where it rests on inherited cosmology it is marked *inherited*.
5. **It introduces no new primitives.** Every mechanism is either a standing ED result (cited) or an inherited piece of standard physics (flagged).

---

## Abstract

Event Density explains galactic dynamics — flat rotation curves, the baryonic Tully–Fisher relation, the acceleration scale `a₀` — with no dark-matter particle, through its khronon (the arrow of time made dynamical), i.e. MOND. This paper first sharpens that account: reading gravitational strain as quadratic in the participation amplitude, `Str = |Σ_a P^(a)|²` with $P = \sqrt{b}\,e^{i\pi}$, splits it into a **diagonal term that is Newton** and an **off-diagonal term that is MOND** — the interference cross-term between a local mass and the cosmic horizon, whose modulus is exactly $\sqrt{a_N\cdot a_0}$ with `a₀ = cH₀/(2π)` supplied by the horizon. MOND is not an added force; it is what the interference of matter *with the horizon* looks like. But galaxies are not the whole sky: the CMB acoustic peaks and galaxy clusters demand a component that gravitates without oscillating in the photon–baryon fluid, decoupled and diluting as `a⁻³` at roughly five times the baryon density, and MOND-class theories characteristically die here. ED's candidate is a **committed neutral relic** produced at the inflation/saturation exit by the same admission mechanism that makes the baryons, decoupled because it is uncharged and massive by binding. We write its Lagrangian and find its central feature is **derived, not assumed**: the relic carries a conserved commitment number (P11 read at the field level), so `ρ ∝ a⁻³` follows — exactly the volume memory a MONDian modification of gravity structurally cannot supply. We then ask whether this same relic *is* MOND (superfluid dark matter, one substance) by coarse-graining its self-interaction from ED's real coherence kernel. It comes out **canonical**: because that kernel is built from a cosine (analytic), no non-analytic deep-MOND kinetic term can arise at any order, and the relic's local self-interaction carries no horizon and hence no `a₀`. So the relic is ordinary (super)fluid cold dark matter, and **the sector is two-component**: a CDM relic plus the separate horizon-interference MOND, mechanism-unified (both are the same bilinear cross-term) but not substance-unified. Two-component consistency then **bounds the relic mass**: warm enough to be diffuse in galaxies (or it clumps as a halo and double-counts against MOND), cold enough to cluster at cluster scale and be pressureless by recombination — a **warm ~0.2–0.7 keV** window, the keV sterile-neutrino range. This is a falsifiable directional prediction: **ED requires warm dark matter, not a cold WIMP.** The `keV` scale itself is inherited, blocked by the same wall that stops ED deriving the electron mass, and it sits below ED's natural mass scales, which is the sector's live risk. No spectrum is computed; the action is written, and the computation is specified.

---

## 1. The problem: galaxies without dark matter, and the rest of the sky

Event Density's gravity is khronometric: the arrow of time, made dynamical, is the khronon, a preferred-foliation field that reproduces the weak-field Einstein metric and the classical tests (Papers GR-I..IV) and, in its deep-field limit, gives the MOND phenomenology that fits galaxies with no dark-matter particle (Papers KM-I, 027–034). This is a genuine strength, and it is also a bill. Every MOND-class theory that fits galaxies without dark matter faces the same two facts it cannot fit (KM-I §8):

- **Clusters.** MOND under-predicts cluster masses by a factor of roughly two.
- **The CMB acoustic peaks.** Their pattern requires a component that gravitates but does *not* oscillate with the photon–baryon fluid: a decoupled, pre-formed set of potential wells diluting as `a⁻³`, at roughly five times the baryon abundance by recombination. A boost to baryonic gravity, which is what MOND is, deepens the sloshing; it cannot hold a well still while the fluid rings. This is precisely why MOND-class theories die at the CMB.

ED does not refute dark matter as particle content (Papers 029, 031): the galactic success shows a particle is not *needed for galaxies*, not that none exists. So the honest structure of the sector is: a standing galactic account (MOND), plus a separate, mapped debt at cluster and CMB scale. The rest of this paper sharpens the galactic account into a mechanism, supplies a native candidate for the debt with a written action, determines whether the two are one thing or two, bounds the candidate's one free property, and states the resulting prediction and its risk.

## 2. MOND is a horizon-interference cross-term, not an added force

ED's participation amplitude is $P = \sqrt{b}\,e^{i\pi}$, where `b` is the local event-density (bandwidth) and `π` the U(1) polarity phase (P09). Reading gravitational strain as **quadratic** in this amplitude,

$$\mathrm{Str} = \Big|\sum_a P^{(a)}\Big|^2 = \sum_a |P^{(a)}|^2 \;+\; \sum_{a\neq b} \sqrt{b_a b_b}\,\cos(\pi_a - \pi_b),$$

splits gravity into two pieces (Paper_QuadraticStrain, sharpening Paper_030 §8.4):

- **The diagonal $\sum_a |P^{(a)}|^2$ is Newton** — each source's self-potential.
- **The off-diagonal $\sum_{a\neq b}\sqrt{b_a b_b}\cos(\Delta\pi)$ is MOND** — the interference cross-term. For a local mass interfering with the cosmic horizon, its modulus is the geometric mean $\sqrt{a_N\cdot a_0}$, with $a_0 = cH_0/(2\pi)$ supplied by the horizon (Paper_029).

This is the same interference structure as a double-slit: the cross-term of two amplitudes is their product with a cosine, and here $\sqrt{b_{\rm local}\,b_{\rm horizon}}$ is exactly the geometric-mean modulus. Two consequences follow. First, ED does not *add* a MOND force; MOND is what the strain's off-diagonal, the interference of matter **with the horizon**, looks like, and Newton is the same strain's diagonal. Second, the square-root form that MONDian phenomenology previously carried as a postulate (a bilocal geometric-mean coupling) is now *forced* by $P = \sqrt{b}$, not chosen. One residual is open and named: the constructive sign of the interference, which is the same open question as the attractive sign of ED's cross-chain coherence kernel V5 (Paper_090), discharged with it by the coherence work (Paper_V5AttractiveSign_P12Coh).

The scale `a₀` is a **horizon** property. This will matter in §4: MOND lives in a term one of whose two partners is the horizon, and nothing local can reproduce it.

## 3. The relic, and the one thing its action derives

The CMB's decoupled `a⁻³` component is a *matter* requirement, not a modification of gravity, and ED has a native candidate. At the inflation/saturation exit, ED's baryogenesis mechanism commits matter by single-template admission (Paper_ED_Baryogenesis): the baryons are that template committed to a *charged* channel. The **committed neutral relic** is the neutral-channel sibling — a committed chain-class carrying no net polarity charge, hence decoupled from electromagnetism. It is massive by binding (a lone ED front is massless and moves at `c`; V5 binding confines a collection into a sub-luminal, cold-capable composite — Paper_MassWithoutMass), and it survives reheating because commitment is irreversible (P11).

Coarse-grain the neutral-channel committed chains into one coherent amplitude, $\Phi = \sqrt{\rho/m_R}\,e^{i\theta}$, where `ρ` is the relic density (the dust) and `θ` its coherence phase. In ED's preferred foliation (arrow direction `u^μ`), the matter action is khronometric,

$$S_R = \int d^4x\,\sqrt{-g}\;\Big[\tfrac{1}{2}\big|u^\mu\partial_\mu\Phi\big|^2 - \tfrac{1}{2}c_\perp^2\,h^{\mu\nu}\partial_\mu\Phi\,\partial_\nu\Phi^* - \tfrac{1}{2}m_R^2|\Phi|^2 + L_{\rm self}\Big],$$

with kinetic term from transport (P05) and bandwidth (P04), and mass term the binding mass (value-inherited). The action's one **derived** feature is the one the sector turns on. Its global phase symmetry `Φ → e^{iα}Φ` gives a conserved Noether current, and that conservation *is* P11 at the field level — a committed chain cannot un-commit, so the comoving relic number is fixed:

$$\nabla_\mu J^\mu = 0 \quad\Longrightarrow\quad \rho \propto a^{-3}.$$

This is exactly the **volume memory** a MONDian modification lacks. A dark fluid that is a local function of the expansion rate `H` cannot dilute as `a⁻³` across the radiation-to-matter transition (its density would track `H²` or `H^{3/2}`, era-dependent), because `a⁻³` requires an integration constant, a memory of the volume, that a function of instantaneous `H` does not have (DebtMap §3; the khronon-dial no-go). The relic's conserved commitment number *is* that integration constant. So where a modified-gravity route (Route A) supplies the dust's clustering but not its abundance, the relic field supplies the abundance natively. The amount (`Ω_c ≈ 0.12`, ~5× baryons) remains inherited, at the `η_B` tier; the `a⁻³` is derived.

## 4. One mechanism, two roles: the sector is two-component

Is this relic *also* MOND? That is the superfluid-dark-matter hypothesis (Berezhiani–Khoury 2015): one substance that is cold dark matter when dispersed and, when condensed inside galaxies, has a collective mode that produces the MOND force — dissolving the double-counting between MOND and the relic at a stroke. In ED this cannot be assumed; it must come out of the relic's self-interaction `L_self`, which is the **relic↔relic** off-diagonal of the same quadratic strain, carrying only the finite reach `ℓ` of the V5 kernel:

$$L_{\rm self} \sim -\sum_{i<j} e^{-r_{ij}/\ell}\,\sqrt{b_i b_j}\,\cos(\theta_i - \theta_j).$$

Coarse-graining this on ED's real coherence functional (`v5_coarsegrain_Lself_probe.py`) gives a clean answer, for two independent and structural reasons:

- **The cosine is analytic.** Its gradient expansion is `const + c_2(∇θ)^2 + c_4(∇θ)^4 + …`, even powers only. The deep-MOND kinetic term is `(∇θ)^{3/2}`, non-analytic; it cannot appear at any order. (Berezhiani–Khoury obtain it by *engineering* a fractional-power term; an analytic ED kernel cannot.)
- **There is no horizon in `L_self`.** MOND is defined by `a₀`, a horizon scale (§2). The relic's self-interaction carries only the local reach `ℓ`, so no `a₀` appears, and no MOND force can live in it.

Measured on the real functional, the phase-stiffness exponent is `p = 1.99` (uniform density), `1.99` with the density responding (the variable an earlier probe had wrongly held fixed), and `1.97` at a different reach; the energy is a pure power of the gradient with no intrinsic scale, so the force is linear in `∇θ` (Newtonian). **`L_self` is canonical: the relic is ordinary (super)fluid cold dark matter, not a MOND source.**

So the dark sector is **two-component**: a CDM relic (for clusters and the CMB) plus the separate horizon-interference MOND (for galaxies). The two are *mechanism-unified* — both are the same bilinear cross-term of $P = \sqrt{b}\,e^{i\theta}$ — but not *substance-unified*: the roles differ precisely by whether one partner is the horizon (matter↔horizon gives MOND, with `a₀`; relic↔relic gives CDM stiffness, without). The one-substance route is closed at the perturbative level; its only residue is the non-perturbative/defect (vortex) sector, which the gradient expansion does not cover, and which we flag rather than claim.

This costs the elegant escape: condensation-as-MOND was to have dissolved the galactic double-counting. It does not, so the relic must be kept out of galaxies the ordinary way, by free-streaming, which sets up the mass bound.

## 5. The mass bound: the relic is warm (~keV)

The relic's mass sets its free-streaming length, and two-component consistency squeezes that length from both sides (`relic_mass_bound.py`):

- **Upper mass bound (warmer side).** The relic must be diffuse in galaxies. A cold relic clusters like CDM and would form a halo of order five times the baryonic mass; with MOND already fitting rotation curves from the baryons alone, that halo over-predicts. So the relic must free-stream out of galaxy-scale structure. Heavier means colder means shorter free-streaming, so this is an upper bound on the mass.
- **Lower mass bound (colder side).** The relic must cluster at cluster scale (the missing cluster mass) and be non-relativistic, pressureless dust by recombination (the CMB peaks). Lighter means warmer means it free-streams past clusters and stays relativistic too long. This is a lower bound.

Mapping free-streaming to a thermal-equivalent mass with standard warm-dark-matter cosmology (the half-mode relation) puts the relic at

$$m_R \sim 0.2\text{–}0.7 \ \mathrm{keV},$$

the **warm dark matter** window, coinciding with the much-studied keV sterile neutrino (neutral and warm, exactly the relic's character). What is truly bounded is the relic's *warmth* (free-streaming ~0.1–1 Mpc); the `keV` is the thermal-equivalent, and because ED's relic is produced non-thermally at the saturation exit, its mass at a given warmth depends on the inherited production velocity.

This is the paper's falsifiable headline: **ED's dark sector must be warm (~keV), not cold WIMP-like CDM.** If dark matter is shown to be a heavy cold WIMP, or perfectly cold with no warm free-streaming signature, ED's picture fails. That is a real bet against the cold default.

One standard objection is softer than it looks. The Lyman-α forest normally excludes thermal warm dark matter below ~3–5 keV, which would exclude a sub-keV relic — but that bound assumes the relic makes the observed small-scale structure. In ED it does not: MOND makes the small-scale structure. So the standard Lyman-α wall does not directly apply, and the relic is allowed warmer and lighter than it otherwise could be. The price of this exemption is that the relic's viability is now tied to MOND reproducing the small-scale (Lyman-α) power, which is its own open test.

## 6. The `keV` scale is inherited: the general mass-value wall

Can ED *derive* the `keV` scale, and so turn the warm-dark-matter prediction into a first-principles result? No, and the reason locates the limit rather than excusing it. Every candidate handle is blocked by ED's *general* mass-value wall, not a dark-sector-specific gap:

- A `keV` **mass value** is refused for the same reason as the electron mass: ED derives no mass values, and the mass hierarchy and ratios were attempted six independent ways and all refuted (Paper_113, the "Arc-M six ratio-mechanism refutation").
- There is no ED **neutrino-mass, sterile-neutrino, or see-saw** mechanism; the neutrino-mass case is inherited/empirical and the massless-slot occupancy is open (Paper_116).
- The **inflation-exit / reheating** epoch that would set a production warmth is itself open and inherited (Paper_ED_Cos_01, Route C1), and an early-produced relic redshifts *cold* in any case.

A tempting shortcut — "the relic is neutral, so it binds weakly, so it is naturally light and warm" — is invalid, and is stated here so it is not mistaken for a result: neutrality does not set the binding scale (the neutron is neutral and near 1 GeV). So the relic's mass is **not a separable problem**. It is ED's standing mass-sector frontier (Paper_113's H1→H2 upgrade) wearing a dark-sector hat; the relic mass and the electron mass would be pinned by the same breakthrough or by neither. What survives the survey is exactly the pre-survey position: the *direction* (warm, not cold) is a real falsifiable prediction, the inherited *value* (~keV, neutral) is a respected candidate rather than an ad-hoc number, and the *scale* is inherited, sitting below ED's two natural reference scales (the Planck grain and the ~GeV baryon-sibling), hence unmotivated though not forbidden.

## 7. The prediction, and the live risk

The sector's content, stated as a bet and its downside:

- **The prediction (falsifiable):** ED's dark matter is **warm (~keV), two-component with MOND, and neutral** — not cold WIMP-like CDM, and not a modification of gravity doing everything. It is the keV sterile-neutrino region of parameter space, reached from a substrate ontology rather than a particle model. Cold heavy dark matter, or a detection of a WIMP, refutes it.
- **The live risk (honest):** ED's mass mechanism cannot derive the required warm scale (§6) and its natural scales lean cold and heavy. If the relic is forced cold, it clumps in galaxies and double-counts against ED's own galactic MOND, and the sector fails. The risk is genuine and it is the mass-sector frontier showing up here, not a new defect.

Neither the prediction nor the risk is softened for the reader. The sector is a native, form-complete account with one derived result (the `a⁻³` dust), one settled structural question (two components, not one), one falsifiable prediction (warm), and one inherited number whose value is uncomfortable.

## 8. What is not done, and the path

No CMB spectrum is computed from ED, and no cluster profile is fit. That is the standing debt, and it is now *well-specified* rather than open-ended. With `L_self` canonical (§4), the relic's perturbations are those of a standard warm (super)fluid CDM, and the background is the derived `ρ ∝ a⁻³`. So the computation is: feed this action's background and perturbation equations into a modified Boltzmann code and compare to Planck — the pipeline Skordis–Złośnik ran for the Aether-Scalar-Tensor theory (AeST, 2021), which is the sister-theory existence proof that a relativistic-MOND-class model *can* fit the acoustic peaks. The one free input is the relic mass, inherited and bounded to the warm window of §5. This is a computation with an inherited input, not a from-scratch derivation, and it is the natural first joint deliverable for a collaboration with the superfluid-dark-matter or relativistic-MOND community.

## Falsifiers

- **F1 (the headline).** Dark matter is shown to be cold and heavy (a WIMP detection, or a demonstration that it is perfectly cold with no warm free-streaming). ED's warm relic is refuted.
- **F2.** The off-diagonal interference reading of MOND is shown to be inconsistent with lensing or the classical tests, i.e. the strain quadratic-in-amplitude structure fails where GR-I..IV succeed. The $\sqrt{a_N a_0}$ derivation collapses.
- **F3.** The relic's conserved commitment number is shown *not* to be an ED-native symmetry (the coarse-grained neutral channel carries no conserved number), so P11 does not deliver `ρ ∝ a⁻³`. The relic loses its one derived advantage over a modified-gravity route.
- **F4.** A relic mass in the inherited window is shown to give a free-streaming length that breaks galactic MOND even in the two-component picture — the double-count is not avoided.
- **F5.** MOND is shown *not* to reproduce the small-scale (Lyman-α) structure, so the relic can no longer be exempt from the standard warm-dark-matter Lyman-α bound, closing the warm window from below.
- **F6.** A computed CMB spectrum from the relic action misses the Planck peaks for every mass in the warm window.

## Tiers

| Claim | Tier |
|---|---|
| Galactic dynamics from MOND/khronon, no particle needed | **standing result** (KM-I / 027–034) |
| MOND is the off-diagonal horizon-interference cross-term; $\sqrt{a_N a_0}$ forced | **standing / structural** (Paper_QuadraticStrain, sharpening Paper_030) |
| Committed neutral relic as the CMB/cluster candidate | **form-complete / native** (Baryogenesis + MS-II + binding mass) |
| Relic `ρ ∝ a⁻³` from the P11-conserved commitment number | **derived** (relic action; the volume memory a modified-gravity route lacks) |
| `L_self` is canonical → the sector is two-component | **derived** (coarse-graining the real V5 functional; `p ≈ 1.99`) |
| Relic bounded to the warm ~0.2–0.7 keV (WDM) window | **derived bound** (two-component consistency + WDM cosmology); mass value inherited |
| ED's dark matter is warm (~keV), not cold WIMP CDM | **falsifiable directional prediction** |
| The `keV` scale is derivable from ED | **no** — the general mass-value wall (Paper_113; Paper_116) |
| CMB spectrum computed from ED | **not done** (well-specified; AeST pipeline) |

## Position

ED's dark sector is not "no dark matter," and it is not one substance doing everything. It is **two components joined by one mechanism**: gravity's own strain, read as interference of the participation amplitude, is Newton on its diagonal and MOND on its off-diagonal with the horizon; and a committed neutral relic, the neutral-channel sibling of the baryons, supplies the decoupled `a⁻³` dust the CMB demands, with that `a⁻³` derived from the irreversibility of commitment rather than assumed. The relic is not MOND — its self-interaction coarse-grains to a canonical kinetic term, because a cosine kernel cannot make a non-analytic MOND force and a local interaction carries no horizon — so the two roles are the same interference structure with different partners. Consistency then forces the relic to be warm, in the keV sterile-neutrino window, which is a genuine falsifiable prediction against cold dark matter; the scale is inherited, at the same tier and blocked by the same wall as every other ED mass, and it leans uncomfortably cold, which is the sector's live risk. The account is complete in form and honest in its one number. What remains is a computation, not a mystery: the acoustic peaks from a warm relic on an `a⁻³`-native action, along the path a sister theory has already walked.

---

*Dark-sector flagship; a self-contained consolidation of the ED dark-sector program (companion construction: `Paper_ED_RelicLagrangian_v1`). Standing: MOND as horizon interference (Paper_QuadraticStrain). Derived: the relic's `a⁻³` from P11; `L_self` canonical (two-component). Bounded: the relic is warm, ~keV. Inherited: the mass value and the abundance. Not done: the CMB spectrum. The prediction is warm dark matter; the risk is that ED's natural relic is cold.*
