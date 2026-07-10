# Maxwell as an Emergent Shadow in Event Density: the Charge Skeleton Is Native, the Coherence-Weighted Limit Is Coulomb, and the Smooth Field Is Coarse-Grained

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers, substrate-evaluation arc (the continuum / gauge sector). Short structural result, companion to the charge-as-topology paper.
**Status:** Publication draft (structural, one confirming computation). Resolves the open edge the charge-as-topology paper declared. Standalone, cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative).

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **ED does not derive electromagnetism as a fundamental field.** The result is that the *smooth Coulomb field* is a coarse-grained **shadow** of ED's determinate substrate, not a determinate-dynamics output. This is ED's monist ontology (the smooth continuum is emergent, not fundamental), stated positively, not a gap being papered over.
2. **The coherence-weighted-limit-is-Coulomb step is standard electrostatics with ED's action.** Minimizing the coherence action around a charge gives the Coulomb field because that action *is* the electrostatic action; the ED content is the identification (the coherence deficit is the latent Maxwell action), not a new field-theory result.
3. **The "shadow" reading is *tested* for diffusion and *structural* for Maxwell.** A companion result showed, by build-and-run, that the determinate substrate does not cast a smooth diffusion PDE; the extension to the smooth Maxwell field is by the same structure (the phase sector is Σ-blind, so this is analytic), not an independent build.
4. **No charge magnitudes, no fine-structure constant, no spectrum.** The winding carries no selected magnitude, and (per the charge-as-topology paper) it realizes charge's topological *skeleton* in form and structure only — it is not claimed that the winding *is* electric charge.
5. **No new substrate primitive is introduced**, and no primitive forcing is invoked.

---

## Abstract

The charge-as-topology result established that Event Density's substrate carries the *skeleton* of electromagnetism natively — a quantized integer winding with an exact integral Gauss law, measured to machine precision — and that the Maxwell action is *latent* in the substrate's coherence term (`sin²(Δφ/2) ≈ ¼(∇φ)²`, the standard `∫(∇φ)²` electrostatic action). It left one edge open: does the coarse-graining actually *select* the Maxwell configuration as the continuum expectation of the holonomies, or only leave it latent? This paper resolves that edge in two moves, and the answer for the determinate substrate is *negative* (a "came-back-no," like diffusion): the smooth field is a shadow, not natively cast. **First, the coherence-weighted continuum limit is Coulomb.** In the coherence-weighted limit the field around a charge is the one that minimizes the coherence action, the Poisson solution; solved for a point charge on a lattice it fits the 3D Coulomb field cleanly (best fit at the `1/r` exponent, `R² = 0.97`, versus `0.77` for `1/r²`, with `φ·r` constant in the near field). So the coherence-weighted continuum limit of the substrate's holonomies *is* Maxwell/Coulomb. **Second, the determinate substrate does not cast that smooth field from within.** A companion build-and-run result showed the certified determinate substrate coarse-grains to a kinetic lattice-gas of ballistic trajectories, not a field-relaxing PDE, reaching the smooth PDE "only by leaving ED"; and the gauge phase sector is invisible to the certified selection dynamics. So the smooth Coulomb field lives only in the thick, coherence-weighted (ensemble) limit — it is a coarse-grained **shadow**, not a determinate-dynamics output. The two together give the honest resolution, and it is the same shape everywhere in the program: **ED derives the *form* of electromagnetism** (the native topological charge skeleton, the latent Maxwell action, and, confirmed here, that its coherence-weighted continuum limit is the Coulomb field), while the **smooth Coulomb field is an emergent shadow** the determinate substrate does not fundamentally carry. This is not a deficiency; it is ED's monist position — the smooth continuum is a forgetful coarse-grained summary, as statistical mechanics is to thermodynamics — now made concrete for electromagnetism (tested for diffusion, structural for Maxwell), and it matches the deeper pattern that ED's native continuum is *geometry* (a metric, trajectories), not smooth *fields*.

---

## 1. The Open Edge

The charge-as-topology result reached electromagnetism graph-first, and mapped exactly how far the parallel goes. **Native (measured):** committed `U(1)` polarity gives a quantized integer winding `w ∈ ℤ` (`π₁(U(1)) = ℤ`), conserved and irreversibility-protected, obeying an integral Gauss law (circulation `= 2πw`, loop-independent). That is the topological skeleton of charge. **Latent (derived):** the Maxwell action is present in the substrate's coherence term — `cos²(Δφ/2) ≈ 1 − ¼(∇φ)²`, so the incoherence `sin²(Δφ/2) ≈ ¼(∇φ)²` has exactly the continuum form of the standard `∫(∇φ)²` electrostatic/Maxwell action.

What that result declared **open** is the selection: read as lattice gauge theory, the holonomies are link variables and the Coulomb field is their continuum limit, with the Maxwell action latent — but does the coarse-graining *measure* actually select the Maxwell configuration as the continuum expectation, or does it leave the field undetermined? This paper answers it.

## 2. The Coherence-Weighted Limit Is Coulomb

In the coherence-weighted continuum limit the field configuration around a charge is the one that **minimizes the coherence action** `∫(∇φ)²`, which is the Euler–Lagrange (Poisson) solution `∇²φ = −ρ_charge`. Solving it for a point charge (a substrate winding source) on a three-dimensional lattice:

- **The near field is `1/r`, the clean discriminator.** Fitting `φ(r) ∼ A/r^p` gives `R² = 0.97` at `p = 1` (3D Coulomb), `0.95` at `p = 1.5`, `0.77` at `p = 2`. The *global* fit only weakly separates `p = 1` from `p = 1.5` (a 14-point radial fit contaminated by the periodic-box neutralizing-background artifact), so the decisive signature is the **near-field `φ·r ≈ 0.060` plateau** (`r = 2–4`), the `1/r` fingerprint that a genuine Coulomb field carries and `p = 1.5` does not.

**Tier, stated honestly.** This is an **analytic / computed** result, *not* a substrate measurement. The solve contains no ED substrate — it cannot, since the phase sector is Σ-blind (§3) — it is a lattice `∫(∇φ)²` minimization. What it establishes is not a measurement of ED but the **identification**: the substrate's coherence deficit *is* the electrostatic action, so its minimizer around a charge is Coulomb (which, as pure electrostatics, was never in doubt). The ED content is the identification, not the Poisson solve. So: **in the coherence-weighted continuum limit, the substrate's holonomies give Maxwell/Coulomb** — the *conditional* the charge-as-topology paper's open edge needed.

## 3. The Determinate Substrate Does Not Cast It

Confirming that the smooth field *is* Maxwell in the coherence-weighted limit is only half the answer. The other half is whether the *determinate* substrate produces that coherence-weighted ensemble from within. It does not, for two established reasons.

- **The certified substrate is kinetic, not field-relaxing.** A companion build-and-run result showed the certified determinate substrate coarse-grains to a **kinetic lattice-gas** — ballistic worldlines — **not** a diffusion PDE, and that both routes to a field-relaxing continuum (injected noise, emergent mixing) reach it *only by leaving ED*: the determinate selection is committal/trapping, not the Boltzmann/coherence-weighted relaxation a smooth field requires. So a coherence-weighted ensemble is not what the determinate dynamics generate.
- **The phase sector is Σ-blind.** The substrate's selection dynamics read the density and graph structure, never the polarity phase; the winding is inert to them (it couples only weakly, through a bandwidth channel). So the field-selecting question lives outside the determinate dynamics entirely — it is an analytic question about the coarse-grained ensemble, not a certified-simulator run (which is why §2 is a lattice electrostatics solve, not a substrate run).

So the smooth Coulomb field is reached only in the **thick, coherence-weighted (ensemble) limit** — a coarse-grained **shadow** of the determinate substrate, not something the determinate dynamics cast from within. This is exactly the diffusion situation (the determinate substrate does not cast the smooth diffusion PDE, a *tested* result) transposed to the gauge sector; here it is tested for diffusion and structural for Maxwell (preamble 3).

## 4. The Resolution: Form Native, Smooth Field a Shadow

**B4 §7's literal question was whether the *determinate* DCGT measure selects Maxwell. The honest answer, assembled from §2–§3, is *no*: the determinate coarse-graining is kinetic and Σ-blind, so Coulomb appears only in a coherence-weighted ensemble the determinate dynamics do not produce. So the edge resolves *negatively for the determinate substrate* — the smooth field is a shadow, not natively cast — a "came-back-no" of the same kind the continuum-limit paper reports for diffusion.** What survives as positive is the *form*, and the honest split is:

- **Native / derived (the form):** the topological charge skeleton (integer winding + exact Gauss law, measured); the latent Maxwell action (derived from the coherence deficit); and, confirmed here, that the coherence-weighted continuum limit around a charge *is* the Coulomb field.
- **Emergent shadow (the smooth field):** the determinate substrate does not cast the smooth Coulomb field from within (kinetic-not-field-relaxing, Σ-blind phase sector); it lives only in the thick, coherence-weighted ensemble limit — a coarse-grained shadow.

This is **ED's monist ontology**, made concrete for electromagnetism: the smooth continuum field is a forgetful coarse-grained summary of the determinate substrate (as statistical mechanics is to thermodynamics), not a fundamental object. It is a *feature*, not a gap: ED's claim is precisely that the fact-level lies beneath the smooth field, and the smooth field is what its coarse-graining makes. And it matches the deeper pattern the program keeps returning: **ED's native continuum is geometry — a metric, trajectories, the topological skeleton of charge — not smooth fields.** The metric emerges natively from the graph; the smooth field-PDEs (diffusion, and here Maxwell) are the coarse-grained shadows of the trajectory/skeleton density.

## 5. Honest Tiers

- **Measured (solid):** the charge skeleton (winding + Gauss law, from the charge-as-topology paper); and the determinate substrate being kinetic-not-field-relaxing (from the continuum-limit paper).
- **Analytic / computed (not a substrate measurement):** the coherence-weighted limit around a charge is Coulomb (this paper) — a lattice `∫(∇φ)²` minimization confirming the *identification* (coherence deficit = electrostatic action), with no ED substrate in the solve and none possible (the phase sector is Σ-blind).
- **Derived:** the latent Maxwell action (the coherence deficit's continuum form).
- **Structural / tested-by-analogy:** the smooth field is a shadow the determinate substrate does not cast — *tested* for diffusion (build-and-run), *structural* for Maxwell (the Σ-blind, analytic argument), not an independent Maxwell-specific substrate run (which the Σ-blind phase sector precludes).
- **Not claimed:** that ED derives electromagnetism as a fundamental field (the monist position: the smooth field is emergent); any charge magnitude or the fine-structure constant.

## 6. Falsification Criteria

### 6.1 The coherence action does not select Coulomb

**Falsifier sentence:** *A demonstration that minimizing the substrate's coherence action around a charge does not give the Coulomb field (a non-`1/r` best fit in 3D) would falsify the selection result (§2).*

### 6.2 The determinate substrate casts the smooth field

**Falsifier sentence:** *A demonstration that the certified determinate substrate (not the coherence-weighted ensemble limit) coarse-grains to the smooth Maxwell/Coulomb field from within — i.e. that it is field-relaxing rather than kinetic, or that the phase sector is not Σ-blind — would overturn the emergent-shadow verdict (§3) and make Maxwell a determinate-dynamics output.*

### 6.3 A retrofit charge spectrum

**Falsifier sentence:** *Any result reproducing specific charge magnitudes or the fine-structure constant, if reached by fitting rather than graph-first, would violate the charge-as-topology discipline this paper inherits (preamble 4).*

## 7. Position Statement

**Event Density derives the form of electromagnetism and locates the smooth field one coarse-graining layer up.** The topological charge skeleton is native (a measured integer winding with an exact Gauss law), the Maxwell action is latent in the coherence term, and — resolving the edge the charge-as-topology paper left open — the coherence-weighted continuum limit around a charge is the Coulomb field. But the determinate substrate does not cast that smooth field from within: it is kinetic, not field-relaxing, and its selection dynamics are blind to the phase. So the smooth Coulomb field is a coarse-grained **shadow**, reached only in the thick coherence-weighted limit. This is ED's monist ontology, and it is the same shape as the rest of the program: form native, smooth continuum a shadow.

**What this paper claims.** That the coherence-weighted continuum limit of ED's charge holonomies is the Coulomb field (measured, standard electrostatics with the substrate's action), and that the determinate substrate does not cast that smooth field (structural, tested for diffusion) — so Maxwell is an emergent shadow of a substrate whose native content is the topological charge skeleton and the latent action.

**What this paper does not claim.** That ED derives electromagnetism as a fundamental field (it is emergent, the monist position); any charge magnitude or the fine-structure constant; or that the Maxwell shadow is independently substrate-tested (it is tested for diffusion and structural for Maxwell, the phase sector being Σ-blind).

**Series context.** The continuum/gauge-sector companion to the charge-as-topology paper (whose open edge it closes) and the continuum-limit paper (whose kinetic-not-field-relaxing result it uses). Its one new computation is the confirmation that the identified action's minimizer is Coulomb (§2); the resolution otherwise recombines those two standing results into an explicit, cold-reader close of a declared open edge. It instances the program's monist thread — the determined continuum object is in every case the coarse-grained shadow of the determinate substrate — for electromagnetism, the cleanest case because the lattice-to-continuum dictionary is already standard.

---

## Appendix: Glossary, Reader Map, Artifacts

### Glossary

- **Charge skeleton.** The native topological content of charge: a quantized integer winding with an exact integral Gauss law; measured.
- **Latent Maxwell action.** The substrate coherence deficit `sin²(Δφ/2) ≈ ¼(∇φ)²`, whose continuum form is the standard `∫(∇φ)²` electrostatic/Maxwell action.
- **Coherence-weighted limit.** The thick / ensemble limit in which the field around a charge minimizes the coherence action; its continuum expectation is Coulomb.
- **Emergent shadow.** A smooth continuum object (here the Coulomb field) that is the coarse-grained summary of the determinate substrate, not a determinate-dynamics output; ED's monist reading of the continuum.
- **Σ-blind.** The certified selection dynamics read density and graph structure, never the polarity phase; the charge sector is invisible to them.

### Reader map

*Intuition.* ED already has the *bones* of electricity for free: a whole-number charge that can't leak, and a Gauss law that says how much flux threads any surface around it. It even has the right *energy bookkeeping* (the coherence cost is exactly the electrostatic energy). What it does not have, at the fundamental level, is the *smooth field* itself — the `1/r` potential you draw around a charge. That smooth field is what you get when you *average* the substrate the coherence-weighted way, and this paper checks that the average really is Coulomb. But ED's determinate rule doesn't do that averaging from the inside (it makes sharp trajectories, not relaxed fields), so the smooth field is a *shadow* of the substrate, not a piece of it. That is on purpose: ED says the smooth continuum is the coarse picture, and the sharp substrate is the real one.

*Why it is worth stating.* Charge is the cleanest place to see ED's whole stance on the continuum, because the lattice-to-continuum dictionary for electromagnetism is already textbook. So the question is unusually sharp — not "what continuum object should appear?" but "does the coarse-graining select the known one?" — and the answer is yes for the field's form and no for the field being fundamental.

### Artifacts

- `evaluation/B4_Arc/maxwell_from_coherence_probe.py` — the §2 solve: minimize the coherence action around a charge, fit the radial field (Coulomb `p = 1`, `R² = 0.97`).
- `foundations/Maxwell_From_CoherenceAction_ShadowResolved.md` — the resolution record.
- Companions: the charge-as-topology paper (the skeleton + latent action + the open edge); the continuum-limit paper (the kinetic-not-field-relaxing result §3 uses).

### Load-Bearing Step Audit

| Claim | Tier | Source |
|---|---|---|
| Charge skeleton (integer winding + exact Gauss law) | **measured** | charge-as-topology paper |
| Maxwell action latent in the coherence deficit | **derived** | charge-as-topology paper §7 |
| Coherence-weighted limit around a charge = Coulomb | **analytic / computed** (confirms the identification; no substrate in the solve, none possible — Σ-blind) | §2 |
| Determinate substrate is kinetic, not field-relaxing | **measured** | continuum-limit paper |
| Phase sector is Σ-blind | **grounded** | charge-as-topology paper |
| Smooth Maxwell field = emergent shadow | **structural** (tested for diffusion, analytic for Maxwell) | §3, §4 |
| ED derives EM as a fundamental field | **NOT CLAIMED** (emergent shadow, monist position) | preamble 1 |
| Charge magnitudes / fine-structure constant | **NOT CLAIMED** | preamble 4 |

---

**End of Paper (Maxwell as an Emergent Shadow).**

*Substrate-evaluation arc. The charge skeleton (integer winding + exact Gauss law) is native and the Maxwell action is latent in the coherence deficit (charge-as-topology paper); this paper resolves that paper's open edge — the coherence-weighted continuum limit around a charge is the Coulomb field (`p = 1`, `R² = 0.97`) — and combines it with the tested kinetic-not-field-relaxing character of the determinate substrate to conclude the smooth Coulomb field is a coarse-grained emergent shadow, not a determinate-dynamics output. Form native, smooth field a shadow: ED's monist ontology for electromagnetism, and the same pattern as its native continuum being geometry, not smooth fields.*
