# The Relic Lagrangian, First Construction: the Committed Neutral Relic as an Event-Density Matter Field

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — dark-sector program. This is the **first move** on the relic Lagrangian named as the bottleneck in `DarkSector_SuperfluidRelic_Program.md` and the "How far from a Lagrangian and a CMB spectrum" scoping.

**Status: construction skeleton, honestly tiered.** The relic's field content and its pressureless-dust (`a⁻³`) behaviour are assembled from standing corpus results (Baryogenesis, Mass-Without-Mass, MS-II). The mass *value* is inherited exactly as `η_B` is. The superfluid self-interaction `L_self` — the term that was to decide whether dark matter and MOND are one substance — has now been coarse-grained (§3.3, `v5_coarsegrain_Lself_probe.py`) and comes out **canonical**: the relic is (super)fluid CDM, not a MOND source, so **the dark sector is two-component** (a CDM relic plus the separate matter↔horizon interference MOND of `Paper_QuadraticStrain_v1`). No CMB spectrum is computed: this is the action one would *feed* a Boltzmann code, not the spectrum.

**Anchors:** `Paper_ED_Baryogenesis` (M3; committed neutral relic, single-template admission, P11 number-lock); `Paper_MassWithoutMass_BindingInertia` (binding mass, V5-conditional, cold-capable composite); `Paper_MS-II_MatterSectorFromTheArrow` (channels P07 + polarity P09 + transport P05 + arrow P11); `Paper_087` (the 13 primitives); `Paper_KM-I_KhrononMOND` + GR-II (the khronometric preferred frame); `DarkSector_DebtMap.md` (the `a⁻³`-volume-memory no-go for Route A); `DarkSector_SuperfluidRelic_Program.md` (the two-role picture and the open self-term).

---

## Preamble — What This Paper Does NOT Claim

1. **It does not derive the relic mass or abundance.** Both are **value-inherited**, the same tier and for the same reason as `η_B ≈ 6×10⁻¹⁰` (Baryogenesis §4, row 19). The construction fixes the *form* of the action, not its two numbers.
2. **The mass term's origin is binding, not a Higgs Yukawa, and it is V5-conditional.** Per Mass-Without-Mass, a lone ED front is massless; mass is what V5 binding does to a *collection*. The mass term written below is the effective-field-theory mass of that bound composite. Its *form* is standard; its *mechanism* is native but V5-conditional (V5 is a faithful structural addition, not shown primitive-forced); its *value* is inherited.
3. **The superfluid self-interaction has now been coarse-grained, and it is canonical.** The term `L_self` that would give the relic condensate a MOND-producing collective mode was flagged open in the first draft; the V5 coarse-graining (§3.3) has since been run and yields a **canonical** kinetic term (measured exponent `p ≈ 1.99` on the real functional). So the relic is (super)fluid CDM, not a MOND source, and the sector is **two-component**. This paper therefore delivers the CDM-relic (Route B) as an action, with MOND remaining the separate matter↔horizon term (`Paper_QuadraticStrain_v1`), not a feature of this field.
4. **No CMB spectrum, no cluster profile.** The background result (`ρ ∝ a⁻³`, `w ≈ 0`) is derived; folding perturbations through a Boltzmann code is downstream and gated on §5.
5. **No new primitives, no primitive-forcing claim.** Every term is either composed from standing corpus results (tiered) or inherited (flagged). "Form-fixed" here means *conditional on the primitives plus the standard effective-field-theory reading*, never "ED forces this from nothing."

---

## 1. What the relic is, in ED terms

Three standing results fix what object we are writing an action *for*.

- **It is committed matter in a neutral channel (Baryogenesis).** At the saturation exit the substrate admits a single chain-class template; the baryons are that template committed to a *charged* channel (net P09 polarity). The relic is the **neutral-channel sibling**: a committed chain-class carrying no net P09 charge, hence **decoupled from electromagnetism**. Because commitment is irreversible (P11), the *number* of committed relic chains in a comoving volume is fixed once laid down.
- **It is massive by binding, and cold-capable (Mass-Without-Mass).** A lone front is massless and `c`-moving. V5's finite-reach retarded attraction confines a collection of such fronts into a bound composite that is sub-luminal, inertial, and heads to rest as it grows. The relic's mass is this **binding mass** — which is why the relic *can* be cold without a fundamental mass being assumed.
- **Its field content is channel + polarity (MS-II).** Matter is channel structure (P07) dressed with a U(1) polarity phase (P09) and transported by P05, all along the arrow (P11).

Put together: **the relic is a bound composite of committed neutral fronts** — massive (binding), EM-decoupled (neutral), and number-conserved (P11). That last property is the one the cluster/CMB debt turns on, and it is native, not added.

## 2. Field content

Coarse-grain the neutral-channel committed chains into a single coherent participation amplitude. ED's participation measure is `P = √b · e^{iπ}` (`b` = local event-density/bandwidth, `π` = P09 phase). The relic field is that measure for the neutral channel, in condensate (Madelung) normalization:

$$\Phi(x) \;=\; \sqrt{\frac{\rho(x)}{m_R}}\; e^{\,i\theta(x)},$$

- `ρ(x)` — the coarse-grained relic event-density (the neutral-channel `b`). **This is the dust.**
- `θ(x)` — the coarse-grained P09/coherence phase. **This is the candidate MOND khronon** (the phase whose gradient, in the superfluid picture, carries the extra force).
- `m_R` — the binding-mass scale (Mass-Without-Mass; value-inherited).

**Neutral** means the electromagnetic covariant derivative reduces to an ordinary one (charge `q = 0`): the relic does not couple to the photon. The phase `θ` is the *global-coherence/individuation* phase (the χ-sector of Baryogenesis), not the EM-gauged phase. This is the field-theoretic content of "decoupled from light."

## 3. The action, term by term

ED carries a preferred foliation: the arrow gives a unit timelike vector `u^μ` (the khronon direction, GR-II), and the spatial metric is `h^{μν} = g^{μν} + u^μ u^ν`. Matter transport (P05) is *along the arrow*, so the natural matter action is the **khronometric** one, with the time-derivative-along-`u` separated from the spatial gradient. Schematically (a skeleton, not a fully covariantized action):

$$S_R \;=\; \int d^4x\,\sqrt{-g}\;\Big[\; \underbrace{\tfrac{1}{2}\big|u^\mu\partial_\mu\Phi\big|^2 \;-\; \tfrac{1}{2}\,c_\perp^2\, h^{\mu\nu}\partial_\mu\Phi\,\partial_\nu\Phi^*}_{L_{\rm kin}\ \text{(P05 transport, P04 bandwidth)}} \;\underbrace{-\; \tfrac{1}{2} m_R^2\,|\Phi|^2}_{L_{\rm mass}\ \text{(binding, V5)}} \;+\; \underbrace{L_{\rm self}(\Phi,\partial\Phi;u)}_{\text{OPEN — the superfluid term}} \;\Big]$$

Term by term, with its source and tier:

**3.1 `L_kin` — kinetic, khronometric.** From P05 transport plus P04 bandwidth conservation (which made transport norm-preserving/unitary in MS-II §2). The two-speed split — a time part along `u^μ` and a spatial part with coefficient `c_⊥²` — is the ED-native feature: it is khronometric because the arrow is a preferred frame, not because a frame was chosen by hand. For the minimal relativistic relic `c_⊥ = c`; the superfluid term (3.3) is what would drive `c_⊥` down to a slow phonon speed inside galaxies. *Tier: form **structural** (standard kinetic form + the corpus's preferred-frame split).*

**3.2 `L_mass` — mass, from binding.** `m_R²|Φ|²` is the effective-field-theory mass of the bound composite of §1. Its *mechanism* is V5 binding (Mass-Without-Mass), native but V5-conditional; its *value* `m_R` is inherited. A massive `Φ` whose phase advances (`θ̇ ≈ m_R`) oscillates, and a fast-oscillating massive scalar has time-averaged pressure `⟨p⟩ → 0`: **pressureless dust**. *Tier: form **structural**, mechanism **native/V5-conditional**, value **inherited**.*

**3.3 `L_self` — the superfluid self-interaction. RESOLVED (2026-07-19): canonical → two-component.** This is the term that was to decide *one substance vs two components*, and the coarse-graining has now been done (`event-density/evaluation/DarkSector/v5_coarsegrain_Lself_probe.py`). The relic self-interaction is the **relic↔relic** off-diagonal of the quadratic strain, `E = −Σ_{i<j} K(r_ij)√(b_i b_j)cos(θ_i−θ_j)` with the finite V5 reach `K(r) = exp(−r/ℓ)`. Because `cos` is analytic (even powers only, `cos x = 1 − x²/2 + …`), a gradient expansion of this finite-reach kernel yields only analytic powers, `E = const + c_2(∇θ)² + c_4(∇θ)⁴ + …`, whose leading term is the **canonical** superfluid kinetic term `∝ b|∇θ|²`. There is **no route to the non-analytic `(∇θ)^{3/2}` (AQUAL/deep-MOND) term at any order**, and **no acceleration scale `a₀` appears** — the kernel carries only the local reach `ℓ`, no horizon. Measured on the real functional: exponent `p = 1.99` (uniform density), `1.99` (with density response — the concern the retracted khronon-mode probe missed), `1.97` (other reach); energy a pure power of the gradient with no intrinsic scale, so the force `δE/δθ` is **linear in `∇θ`** (Poisson/Newtonian). **So `L_self` is canonical: the relic is (super)fluid CDM, not a MOND source.** The Berezhiani–Khoury one-substance route needs an *engineered* fractional term that an analytic ED kernel provably cannot produce. MOND's non-analyticity and its `a₀` live in the **separate matter↔horizon** cross-term (`Paper_QuadraticStrain_v1`, `a₀ = cH₀/2π` from the horizon), not here. *Tier: **derived** (analytic + confirmed on the real functional), with one open edge: the perturbative kinetic sector only — a non-perturbative/defect (vortex) contribution is not covered by the gradient expansion (flagged, minor).*

**3.4 The conserved number — the headline, and Route A's missing piece.** The action has a global phase symmetry `Φ → e^{iα}Φ` (rotating the P09/coherence phase `θ`), whose Noether current is

$$J^\mu \;=\; \tfrac{i}{2}\big(\Phi^*\partial^\mu\Phi - \Phi\,\partial^\mu\Phi^*\big) \;=\; \frac{\rho}{m_R}\,\partial^\mu\theta,\qquad \nabla_\mu J^\mu = 0.$$

The conservation is not an assumption; it is **P11**, commitment-irreversibility, read at the field level: a committed relic chain cannot un-commit, so its comoving number is fixed. In an FRW background `∇_μJ^μ = 0` gives comoving number `n a³ = {\rm const}`, hence

$$\boxed{\;\rho \;=\; m_R\, n \;\propto\; a^{-3}\;}$$

This is exactly the **volume memory** the DebtMap (§3, Route A) proves a *local function of the expansion rate cannot have*: "a⁻³ requires volume memory a function of `H` lacks." The relic's conserved commitment number *is* that volume memory. The khronon dial (Route A) could supply the dust's *clustering* (`c_s ≈ 0`) but not its *abundance* (`a⁻³`); the relic field supplies the abundance natively, because P11 gives it a conserved number and the khronon has none. *Tier: **derived**, given the field content of §2.*

## 4. What the skeleton already delivers (Route B, the CMB dust)

With `L_self` switched off (dilute regime), the construction is a massive, EM-decoupled, number-conserved matter field, and that is precisely the component the CMB acoustic peaks require:

| CMB/cluster requirement (DebtMap §2) | Delivered by the skeleton |
|---|---|
| decoupled from the photon fluid | **neutral channel** (no P09 charge), §2 |
| dilutes as `a⁻³` at recombination | **P11 number conservation**, §3.4 — the native result |
| clusters like pressureless dust (`w ≈ 0`, `c_s ≈ 0`) | **fast-oscillating massive scalar**, §3.2 |
| cold-capable | **binding mass**, sub-luminal composite (Mass-Without-Mass) |
| abundance ~5× baryons | **value-inherited** (as `η_B` is) — *not* delivered, flagged |

So the dark component that `Paper_ED_Cos_03` currently plugs in as ΛCDM's `Ω_c` now has an **ED field-theoretic home**: it is the dilute phase of the committed neutral relic, and its `a⁻³` is derived rather than inherited. The *amount* (`Ω_c ≈ 0.12`) remains inherited, at the same tier as every other ED-inherited value. This is Route B of the DebtMap, made into an action.

## 5. What is open, in order (the next moves)

1. **`L_self` from V5 — DONE (§3.3): canonical → two-component.** The relic is (super)fluid CDM; MOND is *not* a feature of this field, it is the separate matter↔horizon interference cross-term (`Paper_QuadraticStrain_v1`). One open edge remains: the non-perturbative/defect (vortex) sector, not covered by the gradient expansion. Because the relic is now a plain CDM component (not the MOND khronon), the double-counting between the relic and galactic MOND must be handled the standard two-component way — a free-streaming length large enough that the relic is diffuse at galactic scale (DebtMap §4), which folds into item 2.
2. **The mass value / free-streaming length.** `m_R` is inherited and natural-scale arguments lean cold, the galaxy-unfriendly end. This is now the *dominant* live risk (DebtMap §5): a two-component sector needs the relic diffuse in galaxies (so it does not spoil MOND) yet clustering at cluster/CMB scale — the free-streaming length must land near cluster scale. If forced cold, it clumps in galaxies and the sector fails.
3. **The CMB spectrum.** Feed the background (`ρ ∝ a⁻³`) plus the relic's canonical perturbation equations (`δ`, `θ`, from this action) into a modified Boltzmann code and compare to Planck — the AeST pipeline (Skordis–Złośnik 2021), run on an ED-grounded action. With `L_self` canonical, the relic perturbations are those of a standard (super)fluid CDM, so this is now a well-specified computation gated only on the mass/abundance (item 2), not on an unknown self-term.

## Falsifiers

- **F1 — this is the outcome that occurred (§3.3).** Coarse-graining V5 yields a canonical kinetic term with no `√(a_N a₀)` deep limit and no `a₀`, so `L_self` is not a MOND source: the one-substance route is closed, and the sector is a CDM-relic (Route B) **plus** the separate matter↔horizon interference MOND (two components, mechanism-unified via the shared cross-term structure but not substance-unified). Reopening the one-substance route would require the non-perturbative/vortex sector (F1's residual) to supply what the perturbative kinetic term cannot.
- **F2.** The global U(1) of §3.4 is shown *not* to be ED-native (e.g. the coarse-grained neutral channel carries no conserved number, so P11 does not deliver it) — then the `a⁻³` headline collapses and the relic loses its advantage over Route A.
- **F3.** A binding mass in the inherited window is shown to give a free-streaming length that breaks galactic MOND even in the condensed picture — the double-count the Superfluid-Relic Program flagged (its F4) is not dissolved.
- **F4.** The condensed mode fails to reproduce the khronometric structure (`c_T = c`, `α₂ = 0`) — `θ` is not the khronon, and step 3 fails.

## Tiers

*Derived (given the field content):* the conserved number `∇_μJ^μ = 0` from P11 and the resulting `ρ ∝ a⁻³` (§3.4); the pressureless-dust limit of the oscillating massive scalar (§3.2); **the canonical form of `L_self` from coarse-graining the real V5 functional (§3.3, `p ≈ 1.99`), hence the two-component verdict.** *Structural:* the khronometric kinetic form (§3.1); the field-content identification `Φ = √(ρ/m_R)e^{iθ}` as the coarse-grained neutral-channel participation measure (§2). *Native but V5-conditional:* the binding-mass mechanism (§3.2). *Inherited:* the mass value `m_R` and the abundance `Ω_c` (§4), at the `η_B` tier. *Open:* the relic mass / free-streaming length (§5.2), the CMB spectrum (§5.3), and the non-perturbative/vortex edge of `L_self` (§3.3). *Composed from:* Baryogenesis (neutral committed relic, P11 lock), Mass-Without-Mass (binding mass), MS-II (channel + polarity field content), GR-II/KM-I (khronometric frame), Paper_QuadraticStrain_v1 (MOND = the matter↔horizon term, not this field). *No new primitives.*

## Position

The relic Lagrangian's first construction gives the CDM-relic an ED field-theoretic home: a neutral, binding-massive, P11-number-conserved matter field that is **natively `a⁻³` pressureless dust** — supplying exactly the volume memory the khronon dial (Route A) provably could not. That single result, `ρ ∝ a⁻³` from commitment-irreversibility, is the payoff of writing the action at all: it converts the CMB dark component from an unflagged ΛCDM insert (`Paper_ED_Cos_03`'s inherited `Ω_c`) into a derived consequence of a standing ED matter field, with only its *amount* inherited (as `η_B` is). The self-term that would have made this same substance produce MOND has now been coarse-grained from the real V5 functional (§3.3) and comes out **canonical**: the relic is (super)fluid CDM, not a MOND source. So ED's dark sector is **two-component** — a CDM relic *plus* the separate matter↔horizon interference MOND — mechanism-unified (both are the same bilinear cross-term of `P = √b e^{iθ}`) but not substance-unified, the two roles differing precisely because MOND's pairing includes the horizon (hence `a₀`) and the relic's self-pairing does not. The one-substance (Berezhiani–Khoury) route is closed at the perturbative level, its only residue the non-perturbative/vortex sector. What remains is the mass/free-streaming value (the live risk) and the Boltzmann computation, now well-specified: standard (super)fluid-CDM perturbations on an ED-grounded, `a⁻³`-native action. This is the skeleton one would feed a Boltzmann code, with its central ambiguity resolved.

---

*Dark-sector program, first construction. Composed from `Paper_ED_Baryogenesis`, `Paper_MassWithoutMass_BindingInertia`, `Paper_MS-II_MatterSectorFromTheArrow`, and the khronometric frame (GR-II/KM-I). The `a⁻³`-from-P11 result is derived; the mass value and abundance are inherited; the superfluid self-term is open.*
