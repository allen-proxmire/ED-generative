# The Gauge Structure of Event Density: SU(N) Form, Non-Abelian Gauging, the F² Action, and the Mass-Gap Mechanism from Channel Transport

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (gauge-structure derivation)
**Status:** Publication draft (structural). Consolidates the gauge program: the gauge-group form, its non-abelian gauging, its action, and the mass-gap mechanism, with an explicit line between derived structure and inherited/walled content. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative) — substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This does NOT solve Yang–Mills (the Clay problem).** The mass gap is presented as a *mechanism / origin* — the non-abelian self-interaction in the substrate coherence-deficit — verified at the structural level. It is **not** a constructive proof, and the gap's **continuum survival** (the non-perturbative core of the Clay problem) is explicitly left open.
2. **The multiplicities {1, 2, 3} are NOT derived.** Why the stable channel-families are singlets, doublets, triplets, and no higher, is a **wall**: ED's own stability route to {1,2,3} was tested and *refuted* (a symmetric multiplet is stable for all N), and the question is unsolved in standard physics too. The framework gives SU(N) for *any* N.
3. **Couplings, scales, and charge values are inherited.** The coupling `g`, the effective graph scale `a`, and the hypercharge assignments are inherited from measurement, not derived.
4. **Electroweak breaking is Higgs-gated.** The unbroken group structure is derived; the electroweak mixing/breaking (Weinberg angle, W/Z masses, `SU(2)×U(1)_Y → U(1)_EM`) sits on the substrate-Higgs, which is a wall in ED, and is **not** derived here.
5. **The gauge channels are not in the certified simulator.** The *abelian* (Maxwell) case is grounded on the certified Σ-substrate via the Maxwell coherent recovery; the *non-abelian* lift is analytic, at the gauge-program tier, not a certified-simulator measurement.
6. **Spin-SU(2) is a separate frame bundle, not treated here.** This paper is about the *internal* channel gauge structure only; the spacetime frame/spin bundle is a different object and is deferred.
7. **No new primitive is introduced.** The construction uses the canonical primitives (Paper_087); it adds none.

---

## Abstract

The Standard Model's gauge group `SU(3) × SU(2) × U(1)` is an *input* in conventional physics. This paper reports how much of its *structure* (not its values, uniqueness, or breaking) follows from ED's channel substrate. Assembling the substrate objects into a bundle — base = emergent loci, fiber = a rule-type family's channels (P07), connection = polarity-transport (P05) — the gauge group is the fiber's structure group, and for a family of **N dynamically-indistinguishable channels** (P07 gives distinct tokens but no accessible intra-family label) it is `U(N) = SU(N) × U(1)/ℤ_N`, *given* the complex-amplitude structure (from the quantum-logic keystone) and taking total bandwidth (preserved by P05 transport as an isometry) as the sole accessible invariant. So **non-abelian SU(N) is derived-conditional from channel multiplicity** — conditional because indistinguishability alone gives only the permutation group `S_N`; the continuous `U(N)` needs the ℂ-amplitude and the sole-invariant assumption. The gauging is **genuinely non-abelian generically** — position-dependent transport gives non-commuting holonomies in 2000/2000 trials, with the abelian case measure-zero — and this is reconciled with the einselection result (intra-multiplet mixing is free because the N channels are individually unresolved; einselection acts on SU(N)-invariant observables). The **action is F²**: the substrate's coherence-deficit on the plaquette holonomy is the Wilson action, with the trace form the matter-averaged per-chain deficit over dynamically-indistinguishable channels (by Schur's lemma, given the effective-action prescription), coarse-graining to `−¼∫Tr(F²)`. The **mass gap has a clean ED origin**: the same coherence-deficit carries a self-interaction `[A,A]` for non-commuting channels and none for commuting ones, so *in pure Yang–Mills* the classical massless flat direction is lifted iff the channels are non-abelian — verified structurally (a constant potential costs zero for U(1), nonzero for U(N≥2)). That tree-level lift is necessary, not sufficient, for the quantum gap; the continuum survival is the Clay-hard part and is not claimed, and the biconditional is not universal (matter content can remove the gap; Higgsing can add one). The **single hypercharge U(1)** is grounded in P09 being one primitive with one arrow-reference (an identification, not a forced collapse; the charge normalization is not derived). The honest net: the gauge *structure* (SU(N) form derived-conditional, non-abelian gauging, F² action given inputs, gap mechanism, single U(1)) is accounted for; the specific group {1,2,3} is a wall, and the couplings, charge values, and electroweak breaking are inherited or Higgs-gated. ED explains the *shape* of the SM gauge sector while inheriting its *values* — the program's consistent pattern.

---

## 1. Introduction: What a Substrate Can Say About Gauge Structure

The Standard Model gauge group and its representation content are postulated in conventional physics. A substrate ontology can ask a sharper question: which parts of that structure are *forced* by the substrate, and which are inherited? This paper draws that line for ED's gauge sector, consolidating the gauge program into one cold-reader statement.

The result is a clean split. The *structural form* of the gauge sector — that it is a non-abelian `SU(N)` theory, that the gauging is genuine, that the action is `F²`, that a mass gap appears exactly when the channels stop commuting, and that there is a single shared hypercharge `U(1)` — follows from the primitives. The *specific content* — why the multiplicities are {1,2,3}, the coupling values, the hypercharge assignments, and the electroweak breaking — is a wall or is inherited. ED explains the shape and inherits the numbers.

Section 2 builds the group form; §3 shows the gauging is genuinely non-abelian and reconciles it with einselection; §4 derives the `F²` action; §5 gives the mass-gap mechanism; §6 the single hypercharge; §7 states the walls and inheritances honestly; §§8–9 limitations and falsifiers.

### 1.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated; ℂ-amplitude on channels | P / inherited | Paper_087; the ℂ-field from the quantum-logic keystone |
| "Dynamical indistinguishability" reading of P07 | **structural (a reading of P07)** | §2 — P07 gives distinct tokens but no *accessible* intra-family label; not P07's ontological statement |
| Bandwidth preserved under transport | **grounded (P05 isometry)** | §2 — *not* P04 (P04 = additivity + non-negativity only) |
| Group form `U(N)=SU(N)×U(1)/ℤ_N` | **derived-conditional** | §2 — given ℂ-amplitude + total bandwidth as sole invariant; indistinguishability alone gives only `S_N` |
| Genuine non-abelian gauging | **account (+ trivial numerics)** | §3 — random non-commutation is a triviality; einselection-compatibility (account) is the real content |
| `F²` action form | **derived-given-inputs** | §4 — given the per-chain cost form + the matter-averaging prescription; Wilson trace by Schur's lemma |
| Mass gap | **mechanism / account** | §5 — `[A,A]` lifts the *classical* flat direction (verified); the quantum gap's continuum survival is OPEN (Clay) |
| Single hypercharge `U(1)_Y` | **grounded / account (identification)** | §6 — P09 is one primitive; the charge normalization (ℤ_N, anomaly) is not derived |
| Multiplicities {1,2,3} | **WALL** | §7 — unsolved in standard physics; ED's stability route *refuted* |
| Couplings `g`, scale `a`, charge values | **inherited** | §7 |
| Electroweak breaking | **gated (Higgs)** | §7 — substrate-Higgs wall |
| Non-abelian sector on the certified simulator | **NOT (abelian only)** | preamble 5 — abelian grounded, non-abelian analytic |

The honest reading: the group *form* is derived-conditional (on the ℂ-amplitude), the action is derived-given-inputs, the gap is a mechanism, and the single hypercharge is an identification; the multiplicities are a wall and the couplings/charges/breaking are inherited or gated. No item is a clean from-primitives derivation; the derived content is *structural shape given ED's amplitude structure*.

---

## 2. The Gauge-Group Form: SU(N) from Channel Multiplicity

Assemble the substrate into a bundle: the **base** is the emergent spacetime (coarse-grained loci of the participation graph); the **fiber** at a locus is the channel space of a rule-type family (P07), each channel carrying a U(1) polarity phase (P09); the **connection** is polarity-transport (P05). The gauge group is then the fiber's **structure group** — the fiber transformations transport can induce while preserving substrate structure. The question "which gauge group?" becomes "what is the symmetry of the channel fiber?"

For a family of **multiplicity N** (N channels of the same rule-type at a locus — the channel structure is P07), a chain distributes its participation amplitude across them, `ψ = (ψ_1, …, ψ_N) ∈ ℂ^N`, where the complex-amplitude structure is the one grounded by the quantum-logic keystone (the ℂ-field selection).

**A reconciliation with canonical P07 first.** Paper_087 §P07 says channels are *distinguishable* carriers with intrinsic identities — so in what sense are they treated as indistinguishable here? The distinction is **dynamical, not ontological**: P07 grants each channel a distinct *token* identity, but within one same-rule-type family no substrate *observable* resolves that identity (only bandwidth and the rule-type label are dynamically accessible). "Indistinguishable" here means there is no accessible handle to tell the N apart, so mixing among them is a symmetry *of the accessible dynamics* — not a claim that the tokens are identical. This is the load-bearing premise, and it is a reading of P07 (dynamical indistinguishability), not P07's ontological statement.

Two facts then constrain the fiber symmetry:
1. **No accessible intra-family label** (P07, as above): the accessible symmetry includes mixing the N components.
2. **Transport preserves total bandwidth**: P05 transport is an *isometry* (invertible between commitments, preserving `Σ_i|ψ_i|²`). Additivity and non-negativity of bandwidth are P04; *conservation under transport* is the P05-isometry property, not P04 itself.

Given the complex-linear amplitude, the transformations of `ℂ^N` that mix the components while preserving `Σ|ψ_i|²` are the **unitary group** `U(N) = SU(N) × U(1) / ℤ_N`. The `U(1)` factor is the common P09 phase (rotate all channels together); the `SU(N)` factor is the traceless mixing of the N channels.

**One honest gap, stated up front.** Indistinguishability of N tokens, *by itself*, is only a permutation symmetry `S_N`. The step to the *continuous* `U(N)` uses two further inputs: the complex-linear amplitude (transport acts linearly on `ψ ∈ ℂ^N`, so the realizable maps form a continuous group — imported from the quantum-logic keystone), and the assumption that total bandwidth is the *sole accessible invariant*. So the result is **derived-conditional**:

> **Given the ℂ-amplitude structure and taking total bandwidth as the sole accessible invariant, the structure group of N dynamically-indistinguishable channels is `U(N) = SU(N)×U(1)`.** It is not forced by indistinguishability alone (that gives only `S_N`).

The SM correspondence is then a statement about which families are stable: `U(1) × SU(2) × SU(3)` corresponds to channel-family multiplicities {1, 2, 3} — singlets (charge), doublets (weak), triplets (color), which is the SM's representation content. **Why {1,2,3} and no higher is deferred to §7 as a wall.**

---

## 3. The Gauging Is Genuinely Non-Abelian, and Consistent with Einselection

Having the group *form* is not yet having a *gauge theory* — that requires the connection to realize genuine non-commuting parallel transport. Polarity-transport of the N channels is a `U(N)` lattice link variable (re-routing mixes channels, bandwidth-conservation makes it an isometry, invertibility between commitments makes it unitary). The open question was whether the holonomies genuinely fail to commute (`SU(N)`, `F ≠ 0`) or could secretly share an eigenbasis (`U(1)^N`, abelian).

**Non-abelian is generic.** For position-dependent transport, the plaquette holonomies have a non-trivial `SU(N)` part in 2000/2000 trials and commute in 0/2000, while the abelian case requires every link diagonal in one fixed channel basis. Stated honestly: *that generic U(N) links don't commute is a measure-theoretic triviality* — commuting pairs are measure-zero for any random draw, so the simulation confirms only that abelianness would require fine-tuning. The substantive claim — that ED's *actual* transport is not fine-tuned to a common eigenbasis — rests on the einselection-compatibility argument below (an account-tier argument, not the simulation). Given that, **ED's channel-lattice is generically a genuine non-abelian gauge theory** rather than a disguised `U(1)^N`.

**Reconciliation with einselection (the crank-critical point).** A companion result establishes that channels are the primitive pointer basis (einselection). Taken naively, a fixed basis preserved by every transport would force diagonal links and kill the non-abelian structure. The resolution: einselection acts on *observable commitment* at the inter-family level, **not within an SU(N) multiplet**. The N channels of one family are *dynamically indistinguishable* (no accessible intra-family label, §2) — there is no fixed labeling to preserve within the multiplet, and no commitment resolves *which* of the N. So transport is free to `SU(N)`-mix them, while einselection pins the basis for the SU(N)-*invariant* observables across families. No contradiction. (Suggestively — flagged, not claimed — "SU(N)-charged individual channels are never individually committed" is structurally the confinement pattern.)

**One correction, stated for the record.** An earlier gauge-program note read "V5 (the cross-chain kernel) is the SU(N) mixer." That conflated cross-*chain* with cross-*channel*. The SU(N) connection is **P05 re-routing** — a matrix on the N-channel fiber. V5 is a scalar cross-*chain* coherence, a different object (correlation/dynamics, not the intra-fiber connection). The gauge connection is P05; the "V1/V5 ↔ U(1)/SU(N)" mapping is a loose analogy, not the mechanism.

---

## 4. The Action Is F², from the Substrate Coherence-Deficit

Why is the gauge action `∝ F²`? Because the substrate's own coherence-deficit on the plaquette holonomy *is* the Wilson action.

**Abelian, grounded.** In the U(1) reading (the charge arc and the Maxwell coherent recovery on the certified substrate), the per-edge coherence is `cos²(Δφ/2) ≈ 1 − ¼(∇φ)²`, so a phase deficit costs `¼(∇φ)²`. Around a plaquette the holonomy is `e^{iΦ}` with `Φ = a²F`, and the loop deficit is `1 − cosΦ ≈ ½a⁴F²` — the abelian Wilson action, summing to the Maxwell action. This is *why* the coherent field tracked Coulomb; it is simulator-grounded.

**Non-abelian lift, and the trace form.** With multiplicity N the holonomy is `U_□ ∈ U(N)`, and the plaquette cost is the deficit `1 − (1/N)Re Tr U_□`. This trace form is not chosen by hand; it follows from two things. A single chain carrying `ψ ∈ ℂ^N` around the loop retains coherence `Re⟨ψ|U_□|ψ⟩`, so the per-chain cost is `1 − Re⟨ψ|U_□|ψ⟩`. Then, identifying the coarse-grained gauge action with the *average of this per-chain cost over the matter distribution* (a matter-induced effective action — this identification is itself a prescription, disclosed as an input), and using that the accessible amplitude distribution is U(N)-invariant (dynamical indistinguishability), the average is
$$\big\langle 1 - \mathrm{Re}\langle\psi|U_\square|\psi\rangle\big\rangle_\psi = 1 - \tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_\square,$$
because a U(N)-invariant distribution has `∫|ψ⟩⟨ψ|dψ ∝ 𝟙` by **Schur's lemma** (not because the distribution must be uniform — any invariant distribution suffices), fixing the constant to `𝟙/N` by trace. **So the Wilson trace is the matter-averaged per-chain deficit over dynamically-indistinguishable channels (P07), given the effective-action prescription — not a separate postulate.** (Verified numerically: fiber-average 1.1112 vs `1 − (1/N)Re Tr U` 1.1115 at N=3.)

**Coarse-graining to F².** Writing `U_□ = exp(i a² F)` with `F = dA + i[A,A]` and expanding the trace,
$$1 - \tfrac1N\mathrm{Re}\,\mathrm{Tr}\,U_\square \approx \tfrac{a^4}{2N}\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}),$$
so summing over plaquettes gives `S → −¼∫ F^a_{μν}F^{a μν} d⁴x`, the **Yang–Mills action**. The non-abelian quartic (from the `[A,A]` commutator) is built in; Lorentz covariance is inherited from the substrate acoustic metric. (Verified: `deficit/a⁴ → Tr(F²)/2N` as `a → 0`.) So the action is derived *given two disclosed inputs*: (i) the per-chain cost form `1 − Re⟨ψ|U_□|ψ⟩` (the substrate's coherence-overlap, abelian-grounded on the certified substrate, non-abelian at the gauge-program tier, preamble 5), and (ii) the identification of the coarse-grained gauge action with the matter-averaged per-chain cost. Given both, the `F²` form is forced; it is a **derived-given-inputs** result, not a from-nothing derivation.

---

## 5. The Mass-Gap Mechanism: Gap ⟺ Non-Commuting Channels (Pure Yang–Mills)

Maxwell is massless and long-range; Yang–Mills has a mass gap. The gap is not a generic feature of "a gauge field" — it is precisely what changes when the channel structure stops commuting, and ED locates it exactly.

From the same coherence-deficit `S = Σ_□ (1 − (1/N)Re Tr U_□)` with `F = dA + [A,A]`:

- **Abelian (Maxwell).** U(1) holonomies commute, so `[A,A] = 0`, `F = dA`, and the deficit is purely quadratic — a free field, no self-interaction, no gap. That is the massless long-range Coulomb field.
- **Non-abelian (Yang–Mills).** U(N) holonomies do not commute, so `F` carries `[A,A]`, and the deficit contains cubic and quartic self-interaction `~Tr[A,A]²`. The gauge field sources itself, and non-perturbatively that self-interaction gaps the spectrum.

> **In pure Yang–Mills, the mass gap is the signature of non-abelian channel structure in the coherence-deficit. Maxwell is massless because its channels commute; pure Yang–Mills gaps because they do not.** (Not a universal biconditional: with enough matter a non-abelian theory can flow to a conformal, gapless fixed point, and an abelian theory can be gapped by Higgsing. The statement is about the *pure* gauge sector, and even there the gap's continuum survival is the Clay-hard conjecture, below.)

**Verified structurally (the classical flat-direction lift).** For a spatially-constant potential (`dA = 0`) the cost is `‖[A,A]‖²`: exactly 0.0000 for U(1) (the massless flat direction — the photon), and lifted for U(2), U(3), U(4) (1.33, 0.75, 0.53). The classical massless flat direction is lifted **iff** the channel group is non-abelian — the same `[A,A]` that gives `−¼Tr(F²)`. This *tree-level* lift is necessary, not sufficient, for a *non-perturbative quantum* mass gap; the verified object is the flat-direction lift, not the gap itself.

**What is NOT claimed (preamble 1).** The strong-coupling area law confines *both* abelian and non-abelian theories, so it explains why ED confines at all, not why only the non-abelian gap survives. The thing that keeps the non-abelian theory gapped into the continuum while U(1) deconfines to massless Coulomb is asymptotic freedom — the non-perturbative RG core of the Clay problem. **ED locates the gap's origin; it does not prove continuum survival.** Mechanism: verified. Clay proof: not attempted, and a different (rigorous) discipline.

---

## 6. The Single Hypercharge U(1) Is Grounded in the One Arrow

The `U(N) = SU(N) × U(1)` decomposition gives a `U(1)` per family, but the SM has *one* hypercharge `U(1)`. The grounding is P09's single-primitive status: P09 polarity is *one* primitive with one reference — the phase of the whole rule against the one external flow, the commitment/arrow flow (P11). Because there is one P09 phase measured against the same arrow-reference, the per-family common phases are *identified* with the one global P09-vs-arrow phase, and a global phase rotation is **one** `U(1)`, under which each channel advances by its own charge. That single `U(1)` is hypercharge:
$$\text{gauge group} = \prod_i SU(N_i) \times U(1)_{\text{P09}} = SU(3)_c \times SU(2)_L \times U(1)_Y.$$
The `SU(N)_i` stay per-family (internal mixings, no shared reference); the per-family `U(1)`s are identified with one (shared arrow-reference). **There is a single hypercharge because P09 is a single primitive with a single arrow to phase against** — a convergence with the arrow-keystone picture (hypercharge is the arrow wearing a phase).

**Tier, honestly (grounded/account, not derived).** This is an *identification* grounded in P09's single-primitive status, not a forced consequence: nothing in the `U(N)` decomposition alone *forbids* independent per-family internal phases that merely share a reference; collapsing them to one rests on P09 being ontologically one primitive. And the `ℤ_N` quotient structure and the anomaly constraints that fix the surviving `U(1)`'s normalization are not treated here. So §6 grounds *that there is one hypercharge* (one P09, one arrow); it does not derive the charge normalization. The hypercharge *values* (per-particle Y) are the per-channel P09 advance rates — inherited. The electroweak mixing/breaking is **Higgs-gated** (§7).

---

## 7. The Walls and the Inheritances (honest)

The consistent ED pattern: structure derived, values and uniqueness and breaking walled or inherited.

- **The multiplicity wall {1,2,3}.** The framework gives `SU(N)` for any N; it does not say why nature stops at 3. This is unsolved in standard physics, and ED's candidate route was *tested and refuted*: a symmetric channel-multiplet is stable for all N (the binding energy grows with N; the Hessian eigenvalue stays positive), so channel-family stability does **not** select {1,2,3}. This is a genuine wall, reported as one, not a gap awaiting an easy fix.
- **Couplings and scales inherited.** The coupling `g` and the effective scale `a` set the overall normalization; they are inherited, not derived.
- **Hypercharge values inherited.** The single `U(1)_Y` is grounded (§6); the per-particle charges are inherited P09 advance rates.
- **Electroweak breaking Higgs-gated.** The unbroken `SU(3)×SU(2)×U(1)_Y` is derived; the breaking to `U(1)_EM` (Weinberg angle, W/Z masses) rides on the substrate-Higgs, itself a wall. The group is derived; the breaking is not.
- **The abelian/non-abelian simulator boundary.** The Maxwell (abelian) case is grounded on the certified Σ-substrate; the non-abelian lift is analytic (gauge-program tier), because the gauge channels are not in the certified simulator.

So the derived content is the *shape*: `SU(N)` form, genuine non-abelian gauging, the `F²` action, the gap mechanism, and the single hypercharge. The walled/inherited content is the *specifics*: which multiplicities, the couplings, the charges, and the breaking.

---

## 8. Limitations (honest)

- **Not a Yang–Mills proof.** The gap is a mechanism with a verified structural core (`[A,A]` lifts the flat direction); continuum survival (asymptotic freedom, the Clay core) is open.
- **{1,2,3} unsolved and ED's route refuted.** No multiplicity selection is offered; the natural stability route fails.
- **Non-abelian action is gauge-program tier.** The `F²` derivation's abelian base is simulator-grounded; the non-abelian lift is analytic, not a certified-simulator measurement.
- **Values and breaking inherited/gated.** Couplings, charges, and electroweak breaking are not derived.
- **Internal gauge only.** Spin-SU(2) (the frame bundle) and the full matter representation content are separate and not treated here.

---

## 9. Falsification Criteria

### 9.1 The channel fiber is not U(N)-symmetric

**Falsifier sentence:** *A demonstration that transport among the N channels does not preserve `Σ|ψ_i|²`, or that an *observable* distinguishes channels within a family (a dynamically-accessible intra-family label, which would break the dynamical-indistinguishability premise), would break the derived-conditional `U(N)` result (§2).*

### 9.2 The gauging is secretly abelian

**Falsifier sentence:** *A demonstration that ED's plaquette holonomies generically commute (share an eigenbasis) would falsify the genuine non-abelian gauging (§3) and collapse the theory to `U(1)^N`.*

### 9.3 The action is not the holonomy deficit

**Falsifier sentence:** *A demonstration that the substrate's N-channel coherence functional is not the trace-of-holonomy deficit `1 − (1/N)Re Tr U_□` (e.g. channel-diagonal) would falsify the `F²` action (§4).*

### 9.4 The gap does not track non-commutativity

**Falsifier sentence:** *A demonstration that the abelian theory carries a substrate-generated gap, or that the non-abelian `[A,A]` does not lift the massless flat direction, would falsify the gap mechanism (§5).*

### 9.5 Multiple hypercharge U(1)s

**Falsifier sentence:** *A demonstration that ED requires an independent `U(1)` per family (multiple arrow-references) rather than one global P09 phase would falsify the single-hypercharge result (§6).*

---

## 10. Position Statement

**The structural form of ED's gauge sector follows from the channel substrate, conditional on ED's amplitude structure.** The gauge group is the structure group of the channel fiber, `U(N) = SU(N)×U(1)/ℤ_N` for N dynamically-indistinguishable channels — derived-conditional on the ℂ-amplitude (indistinguishability alone gives only `S_N`) and on total bandwidth (a P05-isometry property) being the sole invariant; the gauging is genuinely non-abelian, consistent with einselection (an account-tier reconciliation; intra-multiplet mixing is free); the action is `F²`, with the Wilson trace the matter-averaged per-chain deficit (by Schur's lemma) coarse-graining to `−¼∫Tr(F²)`, given the per-chain cost and the effective-action prescription; the mass gap is the non-abelian `[A,A]` in the same coherence-deficit (in *pure* Yang–Mills the classical flat direction is lifted iff non-abelian, verified; the quantum gap's continuum survival is open); and the single hypercharge `U(1)` is grounded in P09 being one primitive with one arrow-reference.

**What this paper claims.** The `SU(N)` group *form* (derived-conditional on the ℂ-amplitude); genuine non-abelian gauging (account-tier reconciliation with einselection); the `F²` action (derived given the per-chain cost + matter-averaging); the mass-gap *mechanism* (the `[A,A]` flat-direction lift, verified at tree level); and a single hypercharge (grounded in P09's single-primitive status, an identification). `SU(3)×SU(2)×U(1)_Y` is the *shape* of stable channel-families {3,2} plus the global phase.

**What this paper does not claim.** No from-primitives derivation of `U(N)` (it needs the ℂ-amplitude and the sole-invariant assumption; indistinguishability alone gives `S_N`); no Yang–Mills existence/gap *proof* (continuum survival open; the gap⟺non-abelian biconditional holds only for pure YM); no derivation of {1,2,3} (a wall, ED's stability route refuted); no derivation of couplings, scales, charge values, or the hypercharge normalization (inherited); no electroweak breaking (Higgs-gated); and the non-abelian action/gap are gauge-program tier, not certified-simulator measurements.

**Series context.** The gauge-sector consolidation of the ED program. It uses the same primitives the reduction program isolates — the channel structure (P07), the amplitude they carry, and P05 transport shape the group and the action (conditional on the ℂ-amplitude); the arrow (P11) supplies the single hypercharge reference and the einselection that the non-abelian gauging is reconciled against. It pairs with the quantum-logic keystone (which grounds the ℂ-amplitude the channels carry) and exhibits the program's signature pattern: the *shape* of the physics is derived, the *numbers* are inherited.

---

## Appendix — Glossary and Reader Map

### Glossary

- **Channel fiber.** The channels of one rule-type family at a locus; the amplitude `ψ ∈ ℂ^N` lives here.
- **Structure group.** The symmetry of the fiber that transport must preserve; the gauge group. For N dynamically-indistinguishable channels, *given the ℂ-amplitude*, `U(N)` (indistinguishability alone gives only the permutation group `S_N`).
- **Wilson deficit.** `1 − (1/N)Re Tr U_□`, the substrate coherence cost on the plaquette holonomy; the gauge action.
- **`[A,A]` (the commutator).** The non-abelian self-interaction; zero for U(1), nonzero for U(N≥2); the origin of the mass gap in pure Yang–Mills.
- **Gap origin (pure YM).** The ED-native statement of the mass gap: in pure Yang–Mills the *classical* massless flat direction is lifted iff the channels do not commute (a tree-level lift, necessary not sufficient for the quantum gap; not a universal biconditional).
- **Multiplicity wall.** The unsolved question of why stable families are {1,2,3}; ED's stability route to it was refuted.

### Reader map

*Intuition.* Give a locus N channels with no accessible way to tell them apart, insist the total participation is conserved, and grant them a complex amplitude — then the freedom is a unitary rotation among them, `SU(N)×U(1)`, the gauge group. (Without the complex amplitude, indistinguishability alone would give only permutations.) Ask what a loop costs, and the substrate's coherence bookkeeping hands back the Wilson `F²` action. Ask when the force gets a mass, and the answer is exactly when the rotations stop commuting. The whole *shape* of a gauge theory falls out of "N interchangeable channels, participation conserved." What does not fall out is the count (why 3), the strengths (the couplings), or the breaking (the Higgs).

*The pattern.* This is the ED signature: the substrate fixes the form of the physics (given its amplitude structure) and inherits its numbers. The gauge sector is a clean instance — group form (derived-conditional), gauging, action (given inputs), gap-mechanism, and single hypercharge (grounded identification) all accounted for; multiplicities, couplings, charges, and breaking all walled or inherited.

**Where to look next.**
- *The ℂ-amplitude the channels carry:* the quantum-logic keystone.
- *The multiplicity uniqueness wall:* the channel-stability refutation note.
- *The electroweak-breaking gate:* the substrate-Higgs arc.

**Open work** (declared): the {1,2,3} multiplicity selection (a wall — new route needed, not stability); the continuum survival of the gap (asymptotic freedom, the Clay core); the electroweak breaking (substrate-Higgs); and a certified-simulator realization of the non-abelian channel coherence-deficit (currently only the abelian case is simulator-grounded).

---

**End of Paper (The Gauge Structure of Event Density).**

*Substrate-evaluation arc. The gauge-group form `U(N)=SU(N)×U(1)/ℤ_N` is derived-conditional on the ℂ-amplitude for N dynamically-indistinguishable channels (indistinguishability alone gives only `S_N`; bandwidth is preserved by P05 as an isometry, not by P04); the gauging is genuinely non-abelian (einselection-reconciled, account-tier); the `F²` action is the matter-averaged coherence-deficit on the plaquette holonomy (Wilson trace by Schur, given the effective-action prescription); the mass gap is the non-abelian `[A,A]` self-interaction lifting the classical flat direction (in pure YM; verified at tree level; continuum survival open); and the single hypercharge `U(1)` is grounded in P09's single-primitive status. Accounted for: the structural shape, conditional on ED's amplitude structure. Walled/inherited: the multiplicities {1,2,3} (ED's stability route refuted), the couplings and charges, and the electroweak breaking (Higgs-gated). No Yang–Mills continuum proof is claimed. ED fixes the shape of the SM gauge sector and inherits its numbers.*
