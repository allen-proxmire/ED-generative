# Which Shadows the Substrate Casts: a Coherent/Disorder Decomposition of Event Density's Continuum Limits

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (the continuum-limit question, decomposition method)
**Status:** Publication draft. Empirical substrate-evaluation with the certified Σ-rule simulator (`Bits/`). Standalone; cold-reader accessible. Companion to *The Continuum Limit of the Certified ED Substrate* (kinetic-lattice-gas) and *From Worldlines to the Canonical PDE* (channel ledger).
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

> **ON HOLD — UNDER REVISION (2026-06-27).** The framing here — treating diffusion, Gaussianity, and the "diffusive pole" as walls or *different objects* ED cannot reach — is **superseded** by the two-layer coarse-graining view: those are *a layer up* (a second coarse-graining of ED's kinetic/transport shadow), not walls, and the gap to them is decorrelation, added at layer 2. Held pending the reframe and the correlation-length / second-CG test; **not to be cited as final.** See `event-density/foundations/TwoLayer_CoarseGraining_Hierarchy.md`.

---

## Preamble: What This Paper Does NOT Claim

1. **It does not prove Event Density.** The result is consilience evidence — one discrete substrate reproducing, or failing to reproduce, several known continuum laws under coarse-graining. Consilience accumulates; it is not a single decisive experiment, and the paper is explicit about what is recovered, what is recovered as a *different* object, and what is not recovered at all.

2. **The Maxwell recovery is partly expected by construction.** Once the substrate is identified as a lattice gauge theory (Paper_MS-I), a Maxwell continuum limit is what such theories generically produce; the result confirms that the substrate has the right structure, not that Maxwell arises from nothing.

3. **The 13 substrate primitives are not derived** (position paper, Paper_087). These are results about the *certified Σ-substrate*, not a derivation of ED.

4. **Single substrate instantiation (the Σ-rule grid), modest sizes, single-configuration sweeps.** Absolute fit values are not the result; the *contrasts* are (a coherent field that tracks Coulomb vs a total that does not; transport beating diffusion; a phase-randomized surrogate that is Gaussian while the field is not).

5. **"Continuum law" means the coarse-grained / projected description, not a claim about fundamental law.** The substrate is the fundamental object here; the continuum equations are its shadows, in the sense made precise below.

---

## Abstract

Coarse-graining a discrete substrate raises a question sharper than "does it give the continuum?": *which* continuum law does it cast, and is that law the textbook object one expected? We coarse-grain the certified Event-Density substrate and read off the answer with a single decomposition — separating the **coherent** part of a field (its ensemble-consistent signal) from the **incoherent** part (the realization-specific disorder) — applied to three continuum questions. The three answers are genuinely different. (i) **Charge → Maxwell, a window:** the coherent part of the coarse gauge field tracks the Coulomb (action-minimizing) field, with the incoherence localized at the source as entropy; the unseparated total does not, because it sums field and entropy. (ii) **Diffusion → transport, a different object:** the ensemble-mean density obeys a clean continuum law, but the eikonal/transport equation (regression R² 0.60), not diffusion (R² 0.26) — Event Density coarse-grains to the *hyperbolic* pole, not the diffusive one. (iii) **Gaussianity → a wall:** a phase-randomized surrogate carrying the substrate's exact power spectrum is essentially perfectly Gaussian (skewness 0.003), while the substrate field is strongly non-Gaussian (skewness 0.96) — so 100% of the non-Gaussianity lives in the Fourier *phases*, which is to say in the substrate's coherent structure; there is no Gaussian signal to recover. The discriminator across the three is one question — *is there a coherent signal under the disorder, and is it the object asked for?* — and it characterizes the substrate in one line: **Event Density is a structure-making, hyperbolic-pole, phase-correlating substrate.** That phrase predicts which continuum laws of the PDE Atlas it casts by building (the hyperbolic and structure-making ones) and which it does not reach by building (the diffusive and structureless ones), giving a falsifiable map rather than a blanket claim.

---

## 1. Introduction

A substrate ontology earns the word "shadow" for the continuum only if it can show, concretely, which continuum laws its own dynamics cast and which they do not. The companion kinetic-lattice-gas paper showed the certified Event-Density substrate's coarse density field is a kinetic (transport) equation, not a diffusion PDE. This paper generalizes the question from one law to many, and sharpens it: rather than asking "does the substrate give the continuum," we ask of each candidate law,

> **which coarse-graining floor casts this shadow, and does the substrate's averaging climb high enough to cast it?**

We answer it with a single tool — a **coherent/incoherent decomposition** — applied to three continuum questions (Maxwell, diffusion, Gaussianity). The three come back different: a window (the textbook object is recovered), a different object (a clean law, but not the one expected), and a wall (no coherent object to recover). The pattern across the three is itself the result: a one-line characterization of the substrate that predicts, for the broader catalogue of continuum equations, which it casts and which live a coarse-graining floor up.

## 2. Background

**The substrate.** The certified Σ-rule (`Bits/`) evolves an active front on a participation graph: it scores admissible neighbors by Σ = coherence − strain − gradient, commits at the winner (the arrow), deposits density, and advances. It is local, generative, and committal.

**The decomposition.** A field measured from the substrate is a sum of an **ensemble-coherent** part — the structure that is consistent across realizations or commit orders — and an **incoherent** part — the realization-specific disorder. Most "does it give the continuum" tests measure a *quadratic* quantity (an energy, a variance, a cumulant) that mixes the two; the decomposition separates them, so that the coherent signal can be compared to the candidate continuum law directly and the disorder can be identified for what it is.

**The pole taxonomy.** The continuum laws fall into structural classes (the PDE Atlas): hyperbolic (transport, Hamilton–Jacobi, Burgers), diffusive (porous-medium, Fokker–Planck, reaction–diffusion), dispersive, geometric, and so on. A law's pole is a property of the *shadow*; the question here is which poles the substrate casts.

## 3. Method

For each continuum question we coarse-grain the substrate, separate the coherent signal from the incoherent disorder, and apply one discriminator:

- **is there a coherent signal under the disorder, and is it the object asked for?**

Three outcomes are possible: (a) the coherent part *is* the textbook object — a **window**; (b) the coherent part is a clean continuum law but a *different* object — a **different object**; (c) there is no coherent object — a **wall**. The three tests:

- **Charge → Maxwell:** ensemble-average the gauge field as the coherent quantity ⟨e^{iφ}⟩ (not the energy), and compare the coherent-field deficit to the action-minimizing (Coulomb) reference; identify the incoherence radially.
- **Diffusion:** ensemble-average the density to extract the coherent (mean) field, and regress its time-derivative on a candidate library (diffusion ∇²ρ, eikonal/transport |∇ρ|).
- **Gaussianity:** build the phase-randomized surrogate — the substrate's *exact* power spectrum with randomized Fourier phases — and compare its real-space cumulants to the field's; this isolates whether the non-Gaussianity lives in the phases.

## 4. Results

### 4.1 Charge → Maxwell: a window

Charge in this substrate is an integer winding of the participation phase (Paper_ChargeAsTopology_B4); the Maxwell action is latent in the coherence term, which penalizes phase gradients as ¼(∇φ)². Measuring the *total* coarse deficit (the energy) yields a profile that grows with radius and does not match Coulomb — because the energy sums the coherent field and the incoherent disorder. Separating them changes the picture. The **coherent-field** deficit·r² (ensemble of 384, L = 121) is

| r | 4 | 8 | 16 | 32 | 48 |
|---|---|---|---|---|---|
| **coherent field** | 0.285 | 0.196 | 0.169 | 0.164 | 0.153 |
| Maxwell (action-minimizing) reference | 0.301 | 0.240 | 0.245 | 0.190 | 0.151 |

The coherent field tracks the Maxwell reference, matching it at the far edge (0.153 vs 0.151), and it cleans up monotonically as the ensemble grows. The **incoherence** 1 − |⟨e^{iφ}⟩| is sharply localized at the source (0.92 at r = 4) and falls toward zero far away (0.14 at r = 48), and the coherence magnitude plateaus near 0.67 across ensemble sizes — a stable disorder fraction, not a finite-sample effect. The coarse-grained substrate casts **Maxwell in the coherent part, with the entropy localized at the charge.** (Note item 2: this confirms the lattice-gauge structure produces its expected continuum limit.)

### 4.2 Diffusion → transport: a different object

Ensemble-averaging the density extracts a smooth coherent field whose evolution is well-described by a single continuum law — but not diffusion. For a step initial condition, regressing the mean field's time-derivative gives

| model | single realization R² | ensemble-mean R² |
|---|---|---|
| diffusion (∇²ρ) | 0.001 | 0.258 |
| **eikonal / transport (\|∇ρ\|)** | 0.094 | **0.597** |

Ensemble-averaging cleans the dynamics dramatically (R² 0.10 → 0.60), confirming a clean continuum law emerges; that law is **eikonal/transport**, which beats diffusion decisively. The mean density spreads ballistically (∝ t), not diffusively (∝ √t), because the substrate's worldlines are straight rather than random-walk. The coarse-grained substrate casts the **hyperbolic-pole** shadow; the diffusive pole lives a coarse-graining floor up, where the mixing the substrate does not perform would be manufactured.

### 4.3 Gaussianity → a wall

A Gaussian random field is defined by independent, random Fourier phases; amplitude-Gaussianity is uninformative, since each Fourier mode is a sum over all of space and is therefore near-Gaussian for almost any field. The discriminating test is the phase-randomized surrogate — the field's exact power spectrum with phases randomized:

| | skewness | excess kurtosis |
|---|---|---|
| **substrate field** | 0.958 | −0.325 |
| phase-randomized surrogate | 0.003 | −0.001 |

The surrogate — same amplitudes, randomized phases — is essentially perfectly Gaussian, so the power spectrum carries none of the non-Gaussianity. The substrate field, with its actual phases, is strongly non-Gaussian. **100% of the non-Gaussianity lives in the phases** (97% at a coarser scale). Correlated phases are precisely what structure is — a filament is a phase-aligned object — so the substrate is non-Gaussian for the same reason it is committal: it builds coherent structure rather than mixing it away. There is no Gaussian signal to recover; this is a wall, not a masked window.

## 5. Synthesis

### 5.1 The discriminator and the three outcomes

| question | coherent part | outcome |
|---|---|---|
| **Charge → Maxwell** | = the textbook object (Coulomb field) | **window** |
| **Diffusion** | a clean continuum law, but a *different* object (transport/eikonal) | **different object** |
| **Gaussianity** | *no* coherent object (the field is intrinsically non-Gaussian) | **wall** |

The decomposition reveals *what continuum law the substrate actually casts*, and it is not always the textbook object one asked for, and sometimes there is no clean object at all. The discriminator — *is there a coherent signal under the disorder, and is it the object asked for?* — is the content, and it is sharper than a blanket "does it give the continuum."

### 5.2 The characterization, and the map it predicts

The three outcomes have one source. The substrate **makes structure** (its non-Gaussianity is entirely phase correlation), it is **hyperbolic** (its coarse density transports rather than diffuses), and it is **phase-correlating** (the coherent part is where its content lives). In one line:

> **Event Density is a structure-making, hyperbolic-pole, phase-correlating substrate.**

That phrase predicts the Atlas. The substrate casts, *by building*, the structure-making and hyperbolic shadows — transport, Hamilton–Jacobi, Burgers, and (through its lattice-gauge structure) Maxwell. It does not reach, *by building*, the structureless and mixing shadows — the diffusive pole and Gaussianity — because building coherent structure is the opposite of the mixing those require; they live a coarse-graining floor up, reached only when a mixing or dissipative ingredient is added (the companion channel-ledger paper identifies those ingredients as real but switched-off ED primitives). The prediction is falsifiable: a structure-making substrate that cast a clean Gaussian field, or whose coarse density diffused on its own, would refute the characterization.

## 6. Discussion

**The form of the evidence.** A claim about a hidden substrate is confirmed the way atomism was — by consilience, one substrate accounting for many independent known laws without retuning between them. The value of the present result is not any single recovery but the *pattern* and its *discriminator*: a substrate that casts the hyperbolic and structure-making shadows, casts no Gaussian one, and tells you in advance which is which. The Maxwell recovery is partly expected once the lattice-gauge structure is granted (item 2); the transport result is the substrate confirming its own ballistic character; the Gaussianity wall is a genuine negative. A negative, located precisely (the non-Gaussianity is the phase structure), is as informative as a positive.

**Relation to the companion papers.** The kinetic-lattice-gas paper established the transport (not diffusion) result for the coarse *field*; this paper recovers it as one of three outcomes and adds the Maxwell window and the Gaussianity wall. The channel-ledger paper explains *why* the diffusive and dissipative shadows are not cast by the bare rule — they require ingredients (mixing, capacity, global feedback) the minimal substrate lacks — which is the mechanism behind this paper's "floor up."

**Limitations.** Single substrate instantiation, modest sizes, single-configuration sweeps; the contrasts, not the absolute fit values, carry the conclusions. The Maxwell coherent-field tracks the action-minimizing reference closely but, on a finite box with a finite source, neither reaches the asymptotic Coulomb constant; the claimed equivalence is coherent-field = action-minimizer, which holds. The transport regression is cleanest for a sharp-front initial condition. The Gaussianity result is decisive but concerns the participation field of this substrate, not a cosmological observable.

## 7. Conclusion

Coarse-graining the Event-Density substrate and separating coherent signal from incoherent disorder gives, across three continuum questions, three different answers: Maxwell is cast (a window), diffusion is cast as transport (a different object), and Gaussianity is not cast at all (a wall). The discriminator behind the three — *is there a coherent signal under the disorder, and is it the object asked for?* — characterizes the substrate as structure-making, hyperbolic, and phase-correlating, and that characterization predicts which continuum laws of the Atlas it casts and which live a floor up. The picture is a map with its first entries filled in, including one that reads "not here."
