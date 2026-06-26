# From Worldlines to the Canonical PDE: a Bottom-Up Ledger of Event Density's Three Channels

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (the continuum-limit question, channel-resolved)
**Status:** Publication draft. Empirical substrate-evaluation with the certified Σ-rule simulator (`Bits/`). Standalone; cold-reader accessible. Direct companion to *The Continuum Limit of the Certified ED Substrate* (kinetic-lattice-gas paper) and to the top-down Universal-Mobility / canonical-PDE work (Paper_085; ED Foundational Paper; ED-Math-01).
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **It does not re-derive or re-validate the canonical ED PDE / Universal Mobility Law (UDM).** The UDM is an independently, empirically validated top-down law (eleven soft-matter systems, R² > 0.986; Paper_085 / ED Foundational Paper §5.8). Nothing here adds to or subtracts from that validation. This paper is the *discrete-origin* question, run separately.

2. **"Channel" here means the three *constitutive* terms of the canonical PDE** — mobility, penalty, participation — in the sense of the UDM/foundational PDE papers. **This is a different use of the word from the participation-graph "channels" of the matter-sector / gauge work** (Paper_MS-I, *Gauge from Channels*), where a "channel" is a directional substrate structure (P07) whose multiplicity gives gauge groups. The two senses are unrelated; we keep the established PDE-channel terminology and flag the collision here so no reader conflates the constitutive PDE channels with the gauge-theoretic graph channels.

3. **The 13 substrate primitives are not derived** (position paper, Paper_087). This is a result about the *certified Σ-substrate*, not a derivation of ED.

4. **The substrate's missing ingredients are switched on by hand, one at a time, as admissible ED extensions — not co-derived from one master rule.** Extinction, capacity (b→0), and global participation are real ED primitives present in the framework but turned *off* in the minimal certified rule used for substrate evaluations. We demonstrate each singly; we do **not** claim a single unified rule that turns them on together and reproduces the full PDE in one shot.

5. **The diffusion result is Lagrangian (walker dispersion), and it refines — does not contradict — the Eulerian kinetic-lattice-gas finding.** The companion kinetic-lattice-gas paper showed the *deposited density field* evolves by transport, not diffusion (d_tρ regression: diffusion R² ≈ 0). Here we show the *walkers* (worldlines) disperse diffusively. Both hold: the field transports (Eulerian), the walkers diffuse (Lagrangian). We are explicit about which observable each statement concerns.

6. **One substrate instantiation (the Σ-rule grid), modest sizes, single-configuration sweeps.** The absolute fit values are not the result; the **contrasts** are (diffusive vs ballistic exponents; flat vs degenerate mobility; monotone vs ringing; up-relaxation vs down-decay).

---

## Abstract

The canonical Event-Density PDE — derived top-down from seven axioms and validated as a degenerate-mobility law across eleven soft-matter systems — decomposes into three constitutive channels: **mobility** (porous-medium / Universal Mobility diffusion), **penalty** (RC/Debye relaxation), and **participation** (RLC/telegraph oscillation). We ask the converse, bottom-up question: does the *discrete generative substrate* of Event Density — worldlines committing on a participation graph under the certified Σ-rule — reproduce these channels under coarse-graining, and what does each require? We find a sharp channel-by-channel ledger. The bare local rule **natively** supplies the *generative* content: a worldline diffuses in a disordered medium (mean-squared displacement $\propto t^{1.18}$, velocity autocorrelation decaying in ~2 steps), and a front packet spreads Fickian (radius $\propto t^{0.51}$). The remaining content is **dissipative or non-local** and each piece requires a specific Event-Density primitive switched off in the minimal rule: downward relaxation needs **extinction** (the substrate relaxes *up* toward the target density ρ* but cannot decay *down* — it only deposits density); the participation channel's oscillation needs the **global feedback** variable (the bare local rule is monotone, but rings once feedback is added); and the UDM's signature **degenerate mobility** needs a **capacity** bound (the bare rule has none — density grows unbounded, mobility never dies). Each missing ingredient is a known Event-Density primitive — extinction, the b→0 bandwidth-capacity that also governs gravitational horizons, and the participation coupling — none foreign to the framework. The substrate is thus the *generative core* of the canonical PDE; the full equation is that core plus Event Density's own dissipative and non-local primitives. The result is a ledger, not a blanket reconstruction, and it is complementary to the UDM's independent empirical validation.

---

## 1. Introduction

Event Density presents two faces. The **top-down** face is a continuous law: the canonical ED PDE, the unique second-order dissipative scalar equation satisfying seven structural axioms (ED-Math-01), whose mobility channel is the Universal Mobility Law (UDM) validated across eleven chemically distinct soft-matter systems (Paper_085). The **bottom-up** face is a discrete generative substrate: micro-events that participate in one another's becoming, forming worldlines that commit and advance on a participation graph under the certified Σ-rule (`Bits/`).

The two faces have not been reconciled. The companion kinetic-lattice-gas paper established that the certified substrate's *deposited density field* coarse-grains to a kinetic (ballistic/transport) equation, not a diffusion PDE, and that the bare Σ-dynamics do not *generate* the UDM mobility — leaving open whether, and in what sense, the substrate underlies the canonical PDE at all.

This paper closes that gap as a **ledger**. We coarse-grain the substrate and ask, channel by channel, what it reproduces and what each channel requires. The answer is clean: the substrate is the **generative core** — it supplies diffusion and the up-half of relaxation natively — while every dissipative or non-local feature of the PDE (downward decay, capacity, oscillation) is a distinct Event-Density primitive that is *admissible but switched off* in the minimal rule, and which restores its channel the moment it is turned on. We do not re-claim the UDM's validation; we locate the discrete origin of each of its channels.

## 2. Background

### 2.1 The canonical PDE and its three channels

The canonical ED system (ED Foundational Paper; ED-Math-01) is

$$\partial_t\rho = D\big[\nabla\!\cdot(M(\rho)\nabla\rho) - P(\rho)\big] + Hv,\qquad \dot v = \tfrac{1}{\tau}(\bar F - \zeta v),$$

with degenerate mobility $M(\rho)=M_0(\rho_{\max}-\rho)^\beta$ and linear penalty $P(\rho)=P_0(\rho-\rho^*)$. Its three **constitutive channels** and the textbook laws they reproduce top-down are:

| Channel | Operator | Reproduces (top-down match) |
|---|---|---|
| **Mobility** | $\nabla\!\cdot(M(\rho)\nabla\rho)$ | porous-medium / UDM diffusion (1.1%) |
| **Penalty** | $-P(\rho)$ | RC / Debye relaxation (0.00%) |
| **Participation** | $+Hv$ | RLC / telegraph oscillation (0.00%) |

(*Terminology note, cf. Preamble item 2: "channel" throughout this paper is a constitutive PDE term, **not** a participation-graph channel in the gauge sense of Paper_MS-I.*) The UDM mobility's defining feature is **degeneracy** — $M\to 0$ as $\rho\to\rho_{\max}$ — which encodes capacity / maximum packing and is the physical reason the law fits jammed soft matter.

### 2.2 The certified worldline substrate

The certified substrate evolves an active front on a participation graph by the orientation-blind functional $\Sigma = k_c\,\mathrm{Coh} - k_s\,\mathrm{Str} - k_g\,\mathrm{Grad}$, with coherence $\mathrm{Coh}=-(\rho_v-\rho^*)^2$ (favoring targets near $\rho^*$), strain $\mathrm{Str}=\rho_v$ (penalizing dense targets), and gradient-strain $\mathrm{Grad}=|\rho_v-\rho_u|$. A front scores admissible neighbors, **commits** at the winner (the irreversibility chokepoint — the arrow), deposits a density increment, and **advances**. The rule is **local** and **generative**: it adds density, never removes it; it has no capacity bound; and it carries no global mode. Three real ED ingredients — **extinction** (a front dies where Σ falls below a threshold), **capacity** (the b→0 bandwidth bound that elsewhere produces gravitational horizons), and **global participation** (the non-local coupling) — exist in the framework but are *off* in this minimal rule.

## 3. Method

We coarse-grain the substrate and test each PDE channel against a falsification criterion (the feature must be present when the channel's ingredient is active, absent when it is off, and controlled by its parameter). The five observables:

- **Diffusion (mobility):** the mean-squared displacement $\langle|x(t)-x(0)|^2\rangle$ and velocity autocorrelation of a worldline tracer in a disordered medium; the spread exponent of a front packet.
- **Mobility degeneracy:** the effective diffusivity $D_{\mathrm{eff}}$ as a function of local density, fit to $(\rho_{\max}-\rho)^\beta$.
- **Penalty (RC):** $\langle\rho\rangle(t)$ relaxation toward $\rho^*$ from initial conditions both above and below $\rho^*$, with and without extinction.
- **Participation (RLC):** $\langle\rho\rangle(t)$ ringing — sign-crossings of $\langle\rho\rangle-\rho^*$ — as a function of global-feedback strength $H$.

A crucial distinction (Preamble item 5): the **walkers** (worldline positions) are a Lagrangian observable; the **deposited field** is Eulerian. Diffusion below concerns the walkers.

## 4. Results

### 4.1 Mobility → diffusion: native

A single worldline in a disordered (uniform-random) medium **diffuses**: its mean-squared displacement grows as $t^{1.18}$, and its velocity autocorrelation collapses within ~2 steps (1.00, 0.18, 0.05, 0.03, …; tail ≈ 0.02). The direction forgets itself — the operational signature of a random walk. A localized **front packet** spreads with radius $R\propto t^{0.51}$ — Fickian diffusion ($\mathrm{MSD}=R^2\propto t$) — robustly and amplitude-independently (Table 1).

This **refines, not contradicts**, the kinetic-lattice-gas result (Preamble item 5): the *deposited field* evolves by transport (Eulerian; that paper's d_tρ regression), while the *walkers* disperse diffusively (Lagrangian; here). The reconciliation is the standard one — eikonal/ballistic motion in a smooth medium, diffusive scattering in a disordered one.

> **[FIGURE 1 — diffusion]** Tracer MSD on log-log axes (slope 1.18) with the velocity autocorrelation inset decaying to zero; packet radius $R(t)$ (slope 0.51).

### 4.2 Penalty → RC: one-sided

Initialized away from $\rho^*=0.5$, the substrate relaxes **asymmetrically**:

| extinction | $\rho_0$ | $\langle\rho\rangle$: start → end | toward $\rho^*$? | rate $k$ |
|---|---|---|---|---|
| off | 0.20 / 0.65 | → 6.9 / 9.1 | no (unbounded growth) | — |
| **on** | 0.20 | 0.20 → 0.42 | **yes (up)** | 1.32 (exp.) |
| **on** | 0.35 | 0.35 → 0.57 | yes (up) | — |
| **on** | 0.65 | 0.65 → 0.87 | **no (grows away)** | — |
| **on** | 0.80 | 0.80 → 1.02 | no (grows away) | — |

From **below** $\rho^*$, the field relaxes up toward $\rho^*$ exponentially (rate 1.32), and only with **extinction** — without it, density grows without bound to ~7 (pure generative deposition, no relaxation). From **above** $\rho^*$, the field **cannot** decay: it grows away. The substrate reproduces the *up-half* of RC but not the symmetric downward decay, because it deposits density and has no removal mechanism.

> **[FIGURE 2 — RC]** $\langle\rho\rangle(t)$ from above and below $\rho^*$ with extinction on; log-linear decay from below, monotone divergence from above.

### 4.3 Participation → RLC: emergent with global feedback

The bare local rule is **monotone**: $\langle\rho\rangle$ climbs to a plateau (0.35 → 0.57, flat) with a single sign-crossing — no oscillation, because there is no global mode to ring against. Adding the global participation feedback ($\dot v = (-\kappa(\langle\rho\rangle-\rho^*) - \zeta v)/\tau$, uniform feedback $\rho \mathrel{+}= Hv$) makes $\langle\rho\rangle$ **ring** — a damped telegraph oscillation around $\rho^*$:

| $H$ | sign-crossings | verdict |
|---|---|---|
| 0.00 | 1 | monotone |
| 0.05 | 6 | rings |
| 0.10 | 8 | rings (damps to 0.50) |
| 0.20 | 11 | rings |

The oscillation appears the instant feedback is added and its strength scales with $H$. Oscillation is **not native** to the local rule; it is the signature of the non-local participation ingredient.

> **[FIGURE 3 — RLC]** $\langle\rho\rangle(t)$: flat plateau at $H=0$; damped harmonic ring settling to $\rho^*$ at $H=0.10$.

### 4.4 The degenerate mobility (capacity): absent

The UDM's signature — mobility dying at capacity — is **not** present. $D_{\mathrm{eff}}$ is flat across density (≈ 0.94–1.13 over $\rho_0=0.1\text{–}0.8$; power-law fit $\beta\approx-0.1$, $R^2=0.38$, i.e. no degeneracy), and the packet spread exponent stays at 0.5 even as the core density climbs past the nominal capacity to ~3.0. The bare rule has **no $\rho_{\max}$**: density grows unbounded, fronts are never trapped, mobility never degenerates. The capacity is the one feature wholly absent from the minimal generative rule.

## 5. Synthesis — the generative-core ledger

### 5.1 The ledger

| UDM channel | bare local substrate | missing piece | the ED primitive |
|---|---|---|---|
| **Mobility → diffusion** | **native** (worldlines diffuse; Fickian packet) | — | the generative core |
| **Penalty → RC** | **half** — relaxes *up* (with extinction), not *down* | density removal | extinction |
| **Participation → RLC** | **no** — monotone; **rings** with feedback | global feedback | participation coupling |
| *(degenerate mobility)* | **no** — linear only (no capacity) | a $\rho_{\max}$ bound | b→0 bandwidth-capacity |

### 5.2 The pattern

The certified substrate is the **generative, local floor**. It supplies, natively, the *generative* content of the canonical PDE: diffusion (mobility) and the up/saturating half of relaxation. Everything else is either **dissipative** — downward decay (RC's other half) and the capacity (degenerate mobility), needing a density-removal / $\rho_{\max}$ mechanism the additive deposit-rule lacks — or **non-local** — the oscillation (RLC), needing the global feedback a purely local rule cannot have. Crucially, **every missing piece is a real Event-Density primitive**, not a foreign patch: extinction supplies the decay, the b→0 bandwidth-capacity supplies the capacity, the participation coupling supplies the oscillation. Each is *off by default* in the minimal certified rule and *restores its channel* when switched on.

### 5.3 Capacity across scales

The capacity that is missing here is not idle elsewhere. The UDM's degeneracy ($M\to 0$ at maximum packing) is, in substrate terms, the **same bandwidth-collapse $b\to 0$** that the gravity arc identifies with the formation of horizons (the metric degenerates as participation bandwidth runs out). One capacity primitive, two domains: *the capacity that makes a crowded gel stop flowing is the capacity that makes a black hole.* The degenerate-mobility soft-matter law and the gravitational horizon are the same primitive read at two scales — a concrete, falsifiable cross-scale identification offered for scrutiny, not asserted as established.

## 6. Discussion

**What "the UDM is ED coarse-grained" precisely means.** Two senses, both honest. *Axiomatically*, yes: the canonical PDE's seven axioms are Event-Density principles, and the UDM is their unique dissipative realization (ED-Math-01), validated by data. *Bottom-up*, the substrate supplies the **generative core** (diffusion, up-relaxation), and Event Density's other primitives (extinction, capacity, participation) supply the dissipative and non-local channels. The original derivation path was top-down (ED principles → axioms → UDM → physics, validated); this is the same physics reached from the discrete side, with a channel-by-channel ledger of which content is generative-native and which primitive supplies the rest.

**Relation to the validated UDM paper.** Complementary, not duplicative. The empirical validation (eleven materials) lives in Paper_085 and the Foundational Paper and is untouched here; this paper is the discrete-origin story. A negative on any single channel's *bare-rule* reproduction (e.g. the missing capacity) is a statement about the minimal substrate, never about the UDM, which stands on its measurements.

**Honest limits.** The ingredients are switched on by hand, one at a time (Preamble item 4) — we do not exhibit a single master rule that turns them on together and yields the full coupled PDE in one shot; that unification is the natural next target. The participation feedback is implemented as the minimal coupling, not shown to self-organize from the bare dynamics. Results are single-instantiation and modest in size; the contrasts (diffusive vs ballistic exponents, flat vs degenerate mobility, monotone vs ringing, up vs down relaxation) carry the conclusions, not the absolute values. The diffusion result is Lagrangian and is reconciled with — not a reversal of — the Eulerian kinetic-lattice-gas finding.

## 7. Conclusion

The three constitutive channels of the canonical Event-Density PDE have a discrete origin: a generative worldline substrate, plus Event Density's own dissipative and non-local primitives. The substrate is the engine — it diffuses and relaxes-upward on its own — and the full PDE is what that engine, with its switched-on ingredients (extinction, capacity, participation), coarse-grains to. The picture is a ledger, not a blanket reconstruction, and it is complementary to the UDM's independent empirical validation: where the UDM paper shows the law is *true*, this paper shows *which part of it the substrate already is*. The companion shadow-machine paper asks the broader version of the same question — which continuum laws the same substrate casts — and the capacity-across-scales identification (gel jamming = gravitational b→0) is offered as the sharpest cross-scale consequence.

---

*Substrate-evaluation, channel-resolved. The certified ED worldline substrate is the generative core of the canonical PDE: diffusion (mobility) is native (walkers diffuse, MSD $\propto t^{1.18}$; Fickian packet, $R \propto t^{0.51}$ — Lagrangian, refining the Eulerian kinetic-lattice-gas transport result); the dissipative channels (RC down-decay, degenerate-mobility capacity) and the non-local channel (RLC oscillation) each need a real ED primitive switched off in the minimal rule (extinction; b→0 capacity; participation feedback), and each restores its channel when turned on (RC up-relaxation via extinction, k=1.32; RLC ring via feedback; capacity absent → linear diffusion). Ledger, not blanket reconstruction; complementary to the UDM's independent eleven-material validation, not a re-claim of it. "Channel" = constitutive PDE term, NOT the gauge-graph channels of Paper_MS-I. Capacity across scales: gel jamming = gravitational b→0, one primitive. Notebook/draft.*
