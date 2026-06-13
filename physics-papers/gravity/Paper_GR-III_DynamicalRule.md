# The Arrow's Engine: The Dynamical Rule of Event-Density Gravity, and the Closing of Its Weak-Field Assumptions

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — post-pivot Arc ED-10 (curvature emergence), Paper GR-III
**Status:** Publication draft. Conditional structural derivation + simulation within the 13-Primitive Generative System. Standalone; cold-reader accessible. Companion to GR-I, GR-II, KM-I, KM-II; closes the weak-field assumptions those papers declared, builds the dynamical rule they reduced to, and flags two numbers that remain open.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **The full Einstein field equation is not derived.** This paper builds the *dynamical bandwidth rule* whose steady state GR-II's Lovelock argument identified as the field equation, and closes two weak-field *assumptions* — it does not derive the nonlinear EFE. The gravitational class remains **khronometric** (GR-II), not pure GR.
3. **The dynamical rule `F` is the minimal admissible forced form**, not a uniquely pinned object. Its *structure* is forced (R2 admissibility + the band↔edge map + the `α=1` lapse + the geodesic structure); its *coefficients* (`κ, D`) are **not pinned** — they are minimal-model constants, and the phenomenology that depends on them is flagged.
4. **The Newtonian field-equation result is the fixed point of the forced terms**, not an independent emergence. The forced terms (P02 adjacency-sharing + P11 commitment-concentration sink) *have* `∇²b ∼ ρ` as their steady state by construction; the content is that those two terms are primitive-grounded. The genuinely emergent results are the horizon, the mass-scaling, and the area law.
5. **`α = 1` (P-Commitment-Linear) is forced *modulo a stated band-accounting premise*** (that the metric band and the commitment-rate-numerator band are the same internal band). Nordström is positively excluded; the premise is named, not proven.
6. **The timelike geodesic identity is reduced, not proven.** It is *limit-forced* (the massive Jacobi functional reduces to the proven null Fermat result and to Newtonian orbits) with the explicit Σ-rule massive-front computation as a named residual.
7. **`ε = 0` (the khronon at light speed) is derived at leading order.** Integrating out the dissipative reserve could renormalize the scalar speed by a small amount; it cannot restore a second cone. "No `λθ²` term" is a minimality statement about the forced rule.
8. **`α₁, α₂` are NOT computed.** This paper establishes that ED is driven into the maximally-suppressed corner of the preferred-frame front, but does **not** compute the values — that needs the pinned couplings plus the khronometric PPN machinery, and is deliberately not faked. The falsification front remains formally open as a number.
9. **The Hawking temperature scaling `T ∝ 1/r_h` is NOT reproduced.** The emergent horizon carries area-law entropy `S ∝ A` (measured), but the surface-gravity scaling is flat in the minimal elliptic/relaxational rule — located to the (unbuilt) hyperbolic strong-field rule. Thermodynamic *coefficients* (`1/4`, the exact `T`) are value-inherited.
10. **GR-I, GR-II, KM-I, KM-II are inherited**, not re-derived; this paper closes assumptions they carried and is cited by their (forthcoming) revisions, but it does not restate their results.

---

## Abstract

GR-I derived Event Density's weak-field Einstein metric under two labeled assumptions — the commitment-rate linearity `α = 1` (selecting the Einstein over the Nordström branch) and the timelike geodesic identity (that massive matter free-falls on the bandwidth metric). GR-II established that ED's gravity is khronometric and reduced the field equation, by Lovelock's theorem, to *the steady state of an admissible dynamical-bandwidth rule* `ḃ = F`, leaving `F` unbuilt and the khronon's scalar-mode speed open (KM-II §6). This paper builds `F`, closes both assumptions, and fixes the khronon speed — with one spine running through all of it: **the arrow (P11 irreversibility) selects the Einstein/khronometric structure three independent times.** (i) **`α = 1` is forced** from the P04 band law: the commitment-reserve is a distinct, *monotone-draining* band, and the Nordström branch would require it to replenish in step with the metric band — which P11 forbids; Nordström is positively excluded (modulo a named band-accounting premise). (ii) **The timelike geodesic identity is reduced** to the massive eikonal of GR-I's proven null result — the massive Jacobi functional is limit-forced to recover both the null (Fermat) and Newtonian (Maupertuis) limits, with the explicit Σ-rule computation the residual. (iii) **The khronon propagates at the speed of light** (`c_s = c`): the only candidate for a foliation-specific kinetic term that would give it a second cone is the reserve sector, and P11 makes that sector dissipative — it *damps* the khronon (confirmed in simulation: it damps and overdamps without shifting the cone), it does not supply the conservative `λθ²` term a second cone needs; this resolves KM-II §6 toward maximal predictivity. The rule is then **built and run**: in its forced form (`ḃ = D∇²b − κρ`, P02 adjacency-sharing minus P11 matter-concentration sink) its steady state is the Newtonian field equation `∇²b ∼ ρ` (the fixed point of the two forced terms); the deficit amplitude is exactly linear in source (Schwarzschild `r_s ∝ M`, confirmed in 2D and 3D); strong coupling forms a **finite-radius `b → 0` horizon** that is a **frozen A2 decoupling cut** — realizing dynamically the identity that the A2 cut, the metric horizon, and the `b → 0` locus are one object; the emergent horizon carries **area-law (holographic) entropy `S ∝ A`**; and the hyperbolic rule carries **2 tensor + 1 scalar** modes (the mode count read off `F` rather than the gauge group). Two numbers remain honestly open and are flagged in-paper: the preferred-frame parameters `α₁, α₂` (ED is driven into the maximally-suppressed corner by five independent mechanisms, but the *values* are not computed and not faked), and the Hawking temperature scaling `T ∝ 1/r_h` (not reproduced by the minimal *elliptic* rule — located, after a 3D test ruled out the dimensional explanation, to the unbuilt hyperbolic strong-field rule). The result: **the rule ED's gravity reduces to is built, its weak-field assumptions are closed, and its scalar mode is pinned to the light cone — with the same irreversibility doing all three jobs.** Einstein is not derived; two falsification numbers remain open; the engine exists and runs.

---

## 1. Introduction

### 1.1 What this paper does

GR-I and GR-II took ED's gravity to the khronometric class with the weak-field Einstein tests — but on two labeled assumptions and with the central object, the dynamical rule, unbuilt. This paper closes that. It (a) **forces `α = 1`** from the P04 band law (§4), (b) **reduces the timelike geodesic identity** to a proven limit (§5), (c) **derives the khronon speed `c_s = c`** (§6, resolving KM-II §6), and (d) **builds and runs the dynamical rule `F`** (§7), confirming the Newtonian field equation, the Schwarzschild mass-scaling, an emergent frozen horizon, the area law, and the mode count. It then states honestly the **two numbers that remain open** (§8): the preferred-frame `α₁, α₂` and the Hawking temperature scaling.

### 1.2 Why this matters, and the register

The register of this paper is *closing the gaps*, not breakthrough. Its value is that the quartet's two standing weak-field assumptions become derived (or reduced), the object the whole construction reduces to is shown to exist and run, and a published open question (KM-II §6) is answered. The conceptual spine is worth stating plainly: **one primitive — the arrow, P11 irreversibility — selects the Einstein/khronometric structure three separate times** (the lapse, the mode count, the scalar speed). That the factor of two, the extra scalar, and that scalar's speed all trace to one commitment is the paper's organizing fact.

### 1.3 How this fits the arc

- **GR-I:** the weak-field metric and classical tests, on the `α=1` and geodesic assumptions. *(this paper closes both)*
- **GR-II:** the khronometric class; the field equation reduced to the steady state of `F` (unbuilt); the scalar speed open. *(this paper builds `F`; fixes the speed)*
- **KM-I/KM-II:** the deep-field (MOND) and cosmological sectors, inheriting the weak-field metric. *(KM-II §6 resolved here)*
- **GR-III (this paper):** the engine — the dynamical rule built, the weak-field assumptions closed, the khronon speed pinned, two numbers left open.

### 1.4 Conventions and regime of validity

Signature `(−,+,+,+)`; `c = 1` where convenient. The derivations are **weak-field / DCGT-limit**; the simulations are minimal-model (modest grids; coefficients `κ, D` unpinned). Where a result is *measured* it is labeled so; where *forced/derived/reduced* it is tiered; where *open* it is flagged. No strong-field claim is made beyond the emergent-horizon structure; the `α₁, α₂` values and the Hawking scaling are explicitly deferred.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087), load-bearing:** P11 (commitment irreversibility — the arrow; load-bearing three times), P13 (the tick), P04 (the four-band bandwidth, including the commitment-reserve band), P02 (reciprocal adjacency — the shared metric band), P05 (transport — the single causal cone).

**Inherited results:** GR-I (`g ∼ b⁻¹`, `N² ∼ b`, the weak-field metric; the `α=1` and geodesic assumptions this paper closes); GR-II (the khronometric class; the field equation = steady state of `F`; the mode-count gauge argument); Paper_027 (`G`, value-inherited); R2 (the dynamical rule's admissibility); R4–R9 (the structural arc: genuine metric, conserved source, Lovelock).

**External dictionary (inherited, labeled I):** Lovelock's theorem (GR-II); the khronometric/Einstein-aether mode and PPN structure; the 3D-vs-2D CFL stability bound for explicit diffusion.

**No new primitive is introduced; no primitive forcing is invoked.** The dynamical rule is the formalization of the commitment-reserve dynamics P04 + P11 already declare (R2).

---

## 2.5 Load-Bearing Step Audit

*Status legend:* **I** = inherited; **D** = derived here; **D-cond** = derived modulo a named premise/limit; **measured** = simulation result; **structural** = from structure alone; **fixed-point** = the steady state of the forced terms (built-in via the terms being primitive-grounded); **open** = declared open, not computed.

| Step | Status | Source |
|---|---|---|
| field equation = steady state of `ḃ = F` | **I** | GR-II R9 |
| `α = 1` forced (Nordström excluded) | **D-cond** (band-accounting premise) | §4 |
| Nordström needs reserve replenishment → inadmissible (P11) | **structural** | §4 |
| timelike geodesic identity = massive eikonal of the null result | **D-cond** (limit-forced; Σ-computation residual) | §5 |
| `c_s = c` (`ε = 0`, khronon at light speed) | **D** (leading order) | §6 |
| reserve dissipative → damps, not a `λθ²` second cone | **structural + measured** | §6 |
| the arrow (P11) selects the structure three times | **structural unification** | §4–§6 |
| `F` built; steady state = `∇²b ∼ ρ` | **fixed-point** (corr 0.999) | §7 |
| `r_s ∝ M` (Schwarzschild mass-scaling), 2D + 3D | **measured** | §7 |
| finite-radius `b→0` horizon = frozen A2 cut | **measured (emergent)** | §7 |
| `S ∝ A` (area-law / holographic) on the emergent horizon | **measured** | §7 |
| 2 tensor + 1 scalar, from `F` | **D** | §7 |
| `α₁, α₂` values | **open** — structural suppression only, not computed | §8 |
| Hawking `T ∝ 1/r_h` | **open** — flat in minimal elliptic rule; located to hyperbolic strong-field | §8 |
| full EFE / strong field / pure GR | **NOT CLAIMED** | preamble 2 |

---

## 3. The Rule the Field Equation Reduces To

GR-II's Lovelock argument (R9) established that ED's field equation is **the steady state of an admissible dynamical-bandwidth rule** `ḃ = F(ρ, ∇ρ, b)` — the per-edge bandwidth evolution. R2 showed this rule is admissible: it is the formalization of the commitment-reserve dynamics P04 + P11 already declare, violating no certified invariant, in its commitment-driven, monotone-conservative, orientation-blind form. The structural arc then *forced its form*: the band↔edge map (R5, by flux↔Levi-Civita covariance), the lapse exponent (`α=1`, §4 below), and the geodesic structure (§5). What remained was to **build it, run it, and read off its modes** — and to fix the one open coefficient of its propagating sector, the khronon speed.

This paper does those four things. The rule's minimal forced form is

> `ḃ = D ∇²b − κ ρ`,  `b ≥ 0`,  `b → 1` at the frame,

with `D ∇²b` the **P02 adjacency-sharing** (the reciprocal metric band equilibrates by the graph Laplacian — the elliptic geometry sector) and `−κρ` the **P11 commitment-concentration sink** (persistent matter holds bandwidth in its concentrated channel, depleting the metric band ∝ its density). The hyperbolic (propagating) sector replaces the relaxational `D∇²b` with the retarded single-P05-transport wave operator (§6–§7).

---

## 4. Closing the Lapse Assumption: `α = 1` Forced

GR-I's lapse `N² ∼ b` (hence the Schwarzschild relation `g₀₀g_rr = −1`, the Einstein branch) rested on `α = 1` in `Γ_commit ∼ b_int/reserve`. With `Γ ∼ b^α`, the null condition gives `g₀₀g_rr ∼ −b^{2(α−1)}`: `α = 1` is Einstein, `α = 0` is Nordström (conformal, no light bending, experimentally dead). Writing `reserve ∼ b_int^β`, `α = 1 − β`: the whole fork is whether the commitment-reserve band co-scales with the internal (metric) band.

It does not, and P11 is why. The reserve and `b_int` are **different state variables**: `b_int` is the *ambient* adjacency capacity (shaped by `ρ`, `∇²b ∼ ρ`); the reserve is a *carried, monotone-draining budget* set by commitment **history** (P11; no replenishment, R2 §5). Generically, then, `β = 0`, `α = 1`. The Nordström value `β = 1` requires the reserve to *track* `b_int` — to be **raised** where `b_int` is high — which is **replenishment**, forbidden by the same P11 irreversibility that defines commitment.

> **The P04 band law forces `α = 1` and positively excludes Nordström.** The Einstein branch at the lapse is selected by the arrow (P11): the reserve cannot replenish to track the metric band, so it does not co-scale, so `α = 1`. *(Modulo one band-accounting premise: that the metric band and the rate-numerator band are the same `b_int`; named, not proven.)* Had P04 defined the reserve as a fixed fraction of the total or supplied a replenishment band, ED would have been Nordström — dead. It does neither. **This is the arrow's first hat.**

GR-I's labeled postulate P-Commitment-Linear is thereby a derived result.

---

## 5. Closing the Geodesic Assumption: the Timelike Identity Reduced

`∇·T = 0` for ED's matter reduces (R6) to `ρ a^ν` — so conservation holds iff the bandwidth worldlines are geodesics of `g ∼ b⁻¹`. GR-I proved this for **null** fronts (Fermat, optical index `n_opt ∼ b⁻¹` — the source of the factor of two); the **timelike/massive** case was assumed.

The timelike-geodesic functional for `g ∼ b⁻¹` is the **Jacobi/Maupertuis** function `J(b) = b⁻¹√(E² − m²b)`, and it is *limit-forced*: as `m → 0` it reduces to `E/b = E·n_opt` — **the proven null Fermat functional** (so the timelike result *contains* the null one) — and in the weak field it reduces to `√(2m(E_kin − V))`, the **Maupertuis momentum**, recovering Newtonian orbits. ED's subluminal max-Σ front is then identified as the **massive eikonal** of the same propagation GR-I treated masslessly (its Hamilton–Jacobi ray being the timelike geodesic; the worldline's intrinsic clock from P11 + P13).

> **The timelike geodesic identity is advanced from assumed to limit-forced reduction** — forced to recover both the proven null limit and the Newtonian limit, the two checks any correct functional must pass (and it could have failed the `m → 0` check; it did not). The residual is the explicit Σ-rule massive-front computation; the bald "assumed" is replaced by a located, limit-checked reduction.

---

## 6. The Khronon Speed: `c_s = c`, Derived (KM-II §6 Resolved)

GR-II's mode count (2 tensor + 1 scalar = khronometric) left the **scalar (khronon) speed** open (KM-II §6: "may propagate at a different speed in principle"). The hyperbolic rule reduces this to one coefficient: writing the propagating perturbation as `ḧ_ij = c²∇²h_ij + ε·(trace)`, the khronon speed is `c_s/c = √(1+ε)`, with `ε` a foliation-specific `λθ²` kinetic term. `ε = 0` → khronon at light speed; `ε ≠ 0` → a second cone.

`ε` is derived to be zero. The only candidate source of a `λθ²` term is the commitment-reserve sector — and P11 makes that sector **one-way / dissipative** (monotone drain, no replenishment). A dissipative coupling enters the dispersion as the **imaginary** part of `ω` (damping), never the **real** part (speed); a conservative `λθ²` term shifts the real part. So P11 irreversibility makes the reserve **incapable** of being the kinetic term `ε ≠ 0` requires. Simulation confirms the distinction is physical: a dissipative reserve term **damps and overdamps** the khronon without moving its cone (the speed is unshifted, the amplitude decays), in sharp contrast to the `ε`-knob, which cleanly shifts `c_s/c = √(1+ε)`. The forced rule (P05 transport + P11 drain) supplies no `λθ²` term, and minimality forbids positing one.

> **`ε = 0`, `c_s = c` — derived: ED's scalar gravitational-wave polarization is at the speed of light**, damped near active matter (overdamped where commitment fires) and clean in vacuum (observationally consistent — the far-field khronon is at `c`, undamped). This resolves KM-II §6 *as a derivation*, toward maximal predictivity — sharper than generic khronometric gravity, which allows `c_s ≠ c`. **This is the arrow's third hat** (the second being the mode count: the arrow breaks the time-gauge that would freeze the scalar, GR-II/R10).

**The three hats.** One primitive, P11, selects the Einstein/khronometric structure three independent times: **`α = 1`** at the lapse (the reserve cannot replenish — §4), the **khronon physical** at the mode count (the arrow breaks the time-gauge — GR-II), and the **khronon at light speed** (the reserve is dissipative, not kinetic — this section). The factor of two, the extra scalar, and that scalar's speed are one irreversibility wearing three hats. *The same arrow that makes the khronon keeps it on the light cone.*

---

## 7. The Engine, Built and Run

The rule is built and run (`evaluation/DynamicalBandwidth/`); results separated into *built-in* (the fixed point of the forced terms) and *emergent* (not built in).

**The Newtonian field equation (fixed point).** The steady state satisfies `∇²b ∼ ρ` (`corr(∇²b, ρ) = 0.999`, the bandwidth-Laplacian concentrated 52× on the source, harmonic vacuum). This confirms the two forced terms (P02 sharing + P11 sink) are Newtonian-consistent — the content being that they are primitive-grounded, not that Poisson is a surprise.

**Schwarzschild mass-scaling `r_s ∝ M` (emergent).** The deficit amplitude is **exactly linear** in the integrated source, in **both 2D and 3D** (3D: `r_s = 0.158, 0.316, 0.633` for `M = 504, 1008, 2016`). `r_s ∝ M` — the Schwarzschild relation. *(The raw 3D `1/r` slope is finite-box/convergence-limited; the mass-scaling is the clean statement.)*

**The emergent horizon = a frozen A2 cut (emergent — the payoff).** At strong coupling, `b → 0` on a **finite-radius surface** (`g_rr ∼ 1/b → ∞`) — a metric horizon — where the reserve is exhausted, so the cut is **frozen** (P11). Nothing in the rule mentions a horizon; one forms. This realizes dynamically the identity that the `b → 0` locus is *at once* an **A2 decoupling cut**, a **metric horizon**, and a **V5 surface** — one rule, one locus, three identities. **A2-dynamical is hereby realized by build-and-run, not argued.**

**Area-law entropy `S ∝ A` (emergent, holographic).** The severed-information count across the frozen cut (A1: capacity-zero across the cut → the hidden DOF are the boundary adjacency channels) scales as the horizon **perimeter** (`r_h^{0.96}`), **not** the enclosed bulk (`r_h^{2.01}`). The entropy is a **surface** quantity — holographic — on a horizon the rule formed dynamically. *(Half-structural: A1 severance is a surface cut. Half-measured: the emergent horizon is a clean compact surface — the part that could have failed and did not. The `1/4` coefficient is value-inherited.)*

**The mode count, from `F` (derived).** The hyperbolic rule's gauge structure gives **2 tensor + 1 scalar** — the scalar physical because the arrow breaks the time-gauge — reproducing GR-II's khronometric count by direct operator analysis rather than the gauge-group argument. Tensor modes at `c` (single P05 cone); scalar at `c` (§6).

---

## 8. The Open Edge — Two Numbers, Flagged

Two quantities remain open, and the paper states them as open rather than leaning on the structural pressure.

**`α₁, α₂` (the preferred-frame front) — structurally suppressed, not computed.** ED is driven into the maximally-suppressed corner of the preferred-frame parameter space by **five independent derived mechanisms**: universal (not differential) Lorentz violation makes `α₁, α₂` sub-leading (GR-II); `c_T = c` and `c_s = c` put both gravitational cones at light speed (the most-suppressed khronometric regime); the metric-only matter coupling removes the direct khronon–matter `α₁` source (KM-I); and — ED-specific — the **dissipative near-field** (the overdamped khronon around matter, §6) cannot build the frame-dependent near-field response `α₁, α₂` measure (P11, again). Five arrows, one direction: strong pressure toward PPN-safety. **But the *values* are not computed here, and not faked** — they require the pinned couplings (`κ, D`) plus the khronometric PPN formulas, or a direct PPN expansion of `F`. The falsification front stays **formally open as a number**; what has changed is that the computation is now definite and foliation-knob-free.

**The Hawking temperature scaling `T ∝ 1/r_h` — not reproduced (located).** The emergent horizon carries the area law (`S ∝ A`, §7), but its surface gravity is **flat** (`κ ∼ r_h^{0.09}`) in the minimal *elliptic* rule, not the Schwarzschild `1/r_h`. A 3D test ruled out the dimensional explanation (`κ` is flat in 2D *and* 3D), isolating the cause to the elliptic relaxation's fixed sharing length `D` (an `r_h`-independent transition width). The Hawking scaling is **located to the unbuilt hyperbolic strong-field rule**, not delivered — and not retrofitted (tuning `D` to force it is forbidden).

---

## 9. Position Relative to the Quartet

- **GR-I's two assumptions are closed.** `α = 1` is forced (§4); the timelike geodesic identity is limit-forced (§5). GR-I's preamble items 6 and 9 are downgraded from postulate/assumption to derived/reduced, citing this paper.
- **GR-II's reduced object is built.** The field equation = steady state of `F` (R9) is now an `F` that exists and runs (§7); the mode count is reconfirmed from `F` (§7); the field-equation form's Newtonian limit is measured.
- **KM-II §6 is resolved.** The scalar-mode speed, left open, is `c_s = c` (§6, derived). KM-II's §6 caveat becomes "the khronon is at light speed, derived."
- **A2-dynamical (the working-program target #8) is realized.** The same rule that builds the EFE horizon forms A2's frozen cut — by build-and-run (§7).

What this paper does **not** change: the gravitational class (khronometric, GR-II); the MOND/cosmology sectors (KM-I/II); the value-inherited constants; and the two open numbers (§8).

---

## 10. The Wedge — Empirical Content

1. **The khronon at light speed** — a falsifiable, sharp prediction: ED's scalar GW polarization propagates at `c` (not a fast/slow second cone), damped near matter, clean in vacuum. A scalar polarization at `c` is distinguishable in principle from pure-GR (two tensor modes only) and from generic khronometric gravity (`c_s ≠ c`).
2. **The emergent horizon's area law** — `S ∝ A` on a dynamically-formed horizon; the holographic scaling is a structural prediction, the `1/4` value-inherited.
3. **The preferred-frame numbers** — `α₁, α₂`, once computed (the definite, knob-free calculation §8 sets up), are the GR-II falsification front; this paper sharpens the lean and defines the computation, it does not pre-empt the verdict.
4. **Not claimed as wedges:** the `α₁, α₂` values; the Hawking `T`; the strong-field metric; the full EFE.

---

## 11. Falsification Criteria

### 11.1 The lapse fork

**Falsifier sentence:** *A demonstration that the P04 commitment-reserve band co-scales with the internal band (`β ≠ 0`) — e.g. a replenishment channel slaving the reserve to `b_int` — would reopen `α ≠ 1` and the Einstein/Nordström fork, falsifying §4.*

### 11.2 The geodesic reduction

**Falsifier sentence:** *An explicit Σ-rule computation showing the massive-front coherence functional is **not** the Jacobi `J(b)` (i.e. the massive worldlines are not timelike geodesics of `g ∼ b⁻¹`) would falsify §5 — the limit checks (Fermat, Maupertuis) being necessary but not sufficient.*

### 11.3 The khronon speed

**Falsifier sentence:** *A demonstration that ED's foliation/reserve sector supplies a conservative `λθ²` term (`ε ≠ 0`) — i.e. that the reserve coupling is kinetic, not dissipative — would falsify `c_s = c` (§6) and give the khronon a second cone.*

### 11.4 The field equation / horizon

**Falsifier sentence:** *A demonstration that the forced rule's steady state is **not** `∇²b ∼ ρ`, or that strong coupling does **not** form a finite-radius `b → 0` horizon / the severed entropy scales as the bulk (`r_h²`) not the surface (`r_h`), would falsify §7.*

### 11.5 The preferred-frame front (when computed)

**Falsifier sentence:** *Computed `α₁` or `α₂` outside the lunar-laser-ranging / pulsar bounds (`~10⁻⁴`, `~10⁻⁷`), once `κ, D` are pinned and the PPN expansion performed, would falsify ED-gravity-as-viable — the front this paper leaves open.*

---

## 12. Position Statement

**The dynamical rule Event-Density gravity reduces to is built and runs; its two weak-field assumptions are closed; its scalar mode is pinned to the light cone — and one irreversibility does all three structural jobs.** `α = 1` is forced from the P04 band law (the reserve cannot replenish to track the metric band — Nordström excluded); the timelike geodesic identity is reduced to the massive eikonal of GR-I's proven null result; and the khronon propagates at `c` because the reserve sector is dissipative, not kinetic (KM-II §6 resolved). The rule, built, has the Newtonian field equation as its fixed point, the Schwarzschild relation `r_s ∝ M` (2D and 3D), an emergent finite-radius horizon that is a frozen A2 cut carrying area-law entropy, and the khronometric mode count read off `F`. The same primitive — the arrow, P11 — selects the Einstein branch at the lapse, makes the khronon physical at the mode count, and keeps it on the light cone.

**What this paper claims.** The dynamical rule is built and Newtonian-consistent; `α = 1` is forced (Nordström excluded); the timelike geodesic identity is limit-forced; `c_s = c` is derived; the emergent horizon, frozen A2 cut, and area law are measured; the mode count is from `F`; and the arrow's three structural selections are one unification.

**What this paper does not claim.** The full EFE is not derived; the class is khronometric, not pure GR; `α = 1` rests on a band-accounting premise; the geodesic identity is reduced, not proven; `c_s = c` is leading-order; the rule's coefficients are unpinned; **`α₁, α₂` are not computed (and not faked); the Hawking `T ∝ 1/r_h` is not reproduced (located, not delivered)**; thermodynamic coefficients are value-inherited; and Einstein is not derived.

**Series context.** Paper GR-III of the post-pivot curvature-emergence line — the engine of the quartet (GR-I, GR-II, KM-I, KM-II): the rule they reduce to, built; the assumptions they carried, closed; the scalar speed they left open, derived. Two falsification numbers remain open, stated as such.

---

## Appendix: Cross-References, Glossary, Reader Map

### Cross-references

- **Paper_087:** position paper. — **Paper_027:** Newton's `G` (value-inherited).
- **GR-I:** weak-field metric (assumptions closed here). — **GR-II:** khronometric class; `F`-reduction (built here).
- **KM-I/KM-II:** deep-field + cosmology (KM-II §6 resolved here).
- **Working record:** `event-density/foundations/` (the Phase-3 GR rounds and the dynamical-rule builds) and `evaluation/DynamicalBandwidth/`.

### Glossary

- **The dynamical rule `F`.** `ḃ = F(ρ,∇ρ,b)` — the bandwidth evolution whose steady state is the field equation (GR-II/R9); minimal forced form `ḃ = D∇²b − κρ`.
- **The three hats (of the arrow).** P11 selecting the Einstein/khronometric structure three times: `α=1` (lapse), khronon physical (mode count), khronon at `c` (scalar speed).
- **`α = 1` / P-Commitment-Linear.** The lapse exponent, forced by the reserve's inability to replenish (P11); Nordström excluded.
- **Jacobi functional.** `J(b) = b⁻¹√(E²−m²b)` — the timelike-geodesic functional; limit-forced to Fermat (`m→0`) and Maupertuis (weak field).
- **`ε` / `c_s = c`.** The foliation-kinetic knob (`c_s/c = √(1+ε)`); derived zero (dissipative reserve), so the khronon is at light speed.
- **Frozen A2 cut.** The emergent `b→0` horizon: a metric horizon, an A2 decoupling cut, and a V5 surface — one locus.
- **Area law `S ∝ A`.** The severed-channel count (A1) scaling as the horizon perimeter, not the bulk — holographic; coefficient value-inherited.

### Reader map and open work

**Where to look next.**
- *The weak-field metric and tests:* GR-I. — *The class and GW/Lorentz:* GR-II. — *MOND/cosmology:* KM-I/KM-II.
- *The build details:* `event-density/foundations/Phase3_GR_*` and `evaluation/DynamicalBandwidth/`.

**Open work** (declared): **compute `α₁, α₂`** (pin `κ,D` → khronometric PPN, or direct PPN expansion of `F`); **the Hawking scaling** (the hyperbolic strong-field rule — does `κ ∝ 1/r_h` emerge?); the explicit Σ-rule massive-front computation (closes §5); the sub-leading reserve speed-renormalization; pinning `κ, D`.

---

**End of Paper GR-III.**

*Post-pivot curvature-emergence line, the engine of the quartet. The dynamical rule ED's gravity reduces to is built and runs (Newtonian field equation as its fixed point; Schwarzschild `r_s∝M` in 2D and 3D; an emergent finite-radius horizon that is a frozen A2 cut with area-law entropy `S∝A`; the khronometric mode count read off `F`). Its two weak-field assumptions are closed: `α=1` forced from the P04 band law (Nordström excluded), the timelike geodesic identity limit-forced to GR-I's proven null result. Its scalar mode is pinned to the light cone (`c_s=c`, derived — the reserve is dissipative, not kinetic; KM-II §6 resolved). One irreversibility (P11) does all three structural jobs — the lapse, the mode count, the scalar speed. Two numbers stay open and are flagged: `α₁,α₂` (structurally suppressed, not computed, not faked) and the Hawking `T∝1/r_h` (located to the unbuilt hyperbolic strong-field rule). No new primitives; Einstein not derived; the engine exists.*
