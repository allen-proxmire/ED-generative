# The Knee in the Data: An Experiment-Ready Test of the Event Density Offset–Velocity Law in Merging Clusters

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — gravity arc (dark-matter phenomenology, observational)
**Status:** Publication draft (short). Observational protocol sharpening the Bullet_Arc prediction into an executable test. Companion to `Bullet_TopologicalDefect` (the mechanism and numerical closure), `Paper_029_a0` and `Paper_ED_DF2_DF4_GroupSuppression` (the rest of the ED dark-matter account). Standalone; cold-reader accessible.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This paper reports no measurement.** It is a protocol: it states an existing ED prediction in executable form, names the dataset, and specifies the statistic. It does not claim the test has been run, nor that the data currently favor any framework.
3. **It does not derive the knee's location.** The companion mechanism paper leaves two substrate ingredients open, which float the transition velocity across roughly $15$–$1500$ km/s. This paper deliberately tests the *shape* (the existence and sharpness of a knee), which is robust to that, not the numerical value, which is not.
4. **It does not refute particle dark matter or MOND.** It specifies the population-level measurement that would *distinguish* the three accounts, and states honestly what each outcome would mean, including outcomes that disfavor ED.
5. **The mechanism it tests is an account with two open ingredients** (`Bullet_TopologicalDefect` §7.1), not a closed derivation. The observational test does not depend on those being closed; that is the point of targeting the shape.

---

## Abstract

The Bullet Cluster has stood for two decades as the clearest evidence for particle dark matter: its weak-lensing mass peak is offset from its X-ray gas. But a single system cannot discriminate mechanisms that all reproduce it, and dark matter, MOND, and the Event Density topological-defect account all reproduce the Bullet. Event Density reads the offset as a monopole–antimonopole pair frozen into the substrate's organizational field by the merger's Kibble–Zurek quench ($\pi_2(S^2)=\mathbb{Z}$; `Bullet_TopologicalDefect`), and this account makes a population-level prediction the rivals do not: across many merging clusters, the mass–gas offset $\Delta r$ as a function of merger velocity $v_{\rm rel}$ traces a **flat–knee–line–ceiling** shape, with a **sharp knee** at the turn-on. Particle dark matter predicts velocity-independent scatter; MOND-EFE predicts a smooth roll-off with no knee. This paper turns that prediction into an executable test. It fixes the observable (the weak-lensing-mass minus X-ray-gas offset, explicitly distinct from the dark-matter–galaxy offset the self-interaction literature reports from the same maps), the velocity proxy (shock/radio-relic Mach numbers and hydrodynamic reconstructions), and the statistic (segmented-regression model comparison: an ED broken line versus a $\Lambda$CDM constant versus a MOND smooth curve). Its central design consequence, following from the mechanism paper's two open ingredients: the test must target the knee's *existence and sharpness*, which are ingredient-robust, not its location, which is not. Its central feasibility finding: dissociative mergers are **velocity-selected** into the ceiling regime, so the diagnostic knee lives in the under-measured population of low-offset, marginal mergers that current archives discard, making the sharpest test a survey-era (Rubin, Euclid, eROSITA) measurement, while the ceiling and multiplicity predictions are checkable now. The result is a falsifiable, ED-distinctive test with the data named and each outcome's meaning stated.

---

## 1. Introduction

The argument from the Bullet Cluster is clean and it convinced most of the field: the gravity is offset from the gas, so the gravity must be sourced by something invisible that traveled through the merger with the collisionless galaxies, and that something is a dark-matter particle. The weakness is that it rests on one system, and one system cannot choose among mechanisms that all reproduce it. Particle dark matter separates mass from gas because the dark matter is collisionless; MOND with its external-field effect shifts the effective-gravity peak as the matter reconfigures; and Event Density freezes a topological defect into the substrate that rides with the galaxies. The Bullet is consistent with all three. It is evidence that the gravity separates from the gas; it is not evidence for any particular reason it does.

The three accounts diverge only across a *population* of mergers, and there they predict different shapes for one measurable relation: how the mass–gas offset depends on merger velocity. This paper takes the Event Density prediction for that relation (derived in the companion `Bullet_TopologicalDefect`) and makes it executable, because a prediction that names no dataset and no statistic is not yet a test. What follows is the observable, the discriminator, the real data, the statistic, and, most importantly, an honest account of where the test is easy and where it is hard.

## 2. Primitive Inputs and Method

**The mechanism, in one paragraph (companion paper).** In Event Density the substrate's organizational state at cluster scales is a field of channel orientations, a unit vector on $S^2$. Because $\pi_2(S^2)=\mathbb{Z}$, that field can wrap $S^2$ an integer number of times around a point, a topologically protected "monopole." A fast merger quenches the field faster than it can relax (a Kibble–Zurek quench), trapping windings; conservation of total winding forces them in canceling pairs, whose two members are the two offset lensing peaks. Each rides with its subcluster's collisionless galaxies rather than the ram-stripped gas, placing the gravity with the galaxies. Numerical closure gives a defect-formation threshold $v_{\rm crit}$, a freeze-out separation $\xi_{KZ}$, and the offset–velocity law tested here.

**The prediction under test.** Across the merging-cluster population,
$$\Delta r(v_{\rm rel}) \approx \begin{cases} 0, & v_{\rm rel} < v_{\rm crit} \\ v_{\rm rel}\, t_{\rm post}, & v_{\rm crit} < v_{\rm rel} \lesssim v_{\rm sat} \\ \xi_{KZ}, & v_{\rm rel} \gtrsim v_{\rm sat} \end{cases}$$
a flat stretch, a sharp knee at $v_{\rm crit}$, a near-linear rise, and a ceiling at $\xi_{KZ}$.

**Method of this paper.** Fix the observable so the test cannot be run against the wrong quantity (§3); state the three hypotheses as data signatures (§4); specify the statistic (§5); name the real dataset and what to extract per system (§6); and confront the feasibility and confounds honestly (§7–8). No primitive forcing is invoked; no new physics is added; the physics is the companion paper's, made testable.

**Regime of validity.** The test is population-level; no single system decides it. It targets the *shape* of $\Delta r(v_{\rm rel})$, not the value of $v_{\rm crit}$, and its conclusions are conditional on assembling a uniform mass–gas offset and velocity sample (§6), which does not yet exist in one place.

## 2.5 Load-Bearing Step Audit

| Step | Status | Source |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Topological-defect mechanism (the $\Delta r(v_{\rm rel})$ law) | account, two open ingredients | `Bullet_TopologicalDefect` §7.1 |
| Knee *location* ($v_{\rm crit}$) | **not pinned** ($\sim 15$–$1500$ km/s) | companion §7.1 |
| Knee *existence + sharpness* (F1, F2) | **ingredient-robust** prediction | this paper §1, companion §7.1 |
| Correct observable = mass–gas offset (not DM–galaxy) | **specified here** | §3 |
| Discriminating statistic (segmented regression) | **specified here** | §5 |
| Real dataset named and pairing corrected | **assembled here (protocol)** | §6 |
| Velocity-selection puts the sample in the ceiling regime | **feasibility finding** | §7 |
| The measurement itself | **not performed** | — |

## 3. The Observable, Fixed So It Cannot Be Run Wrong

**Use the mass–gas offset, not the dark-matter–galaxy offset.** Event Density's $\Delta r$ is the projected separation between the total-mass peak (weak-lensing convergence) and the hot-gas peak (X-ray surface brightness). This must not be confused with the dark-matter–galaxy offset that the self-interaction literature (Harvey et al. 2015; Wittman et al. 2018) measures from the same maps to constrain a self-interaction cross-section. That is a different quantity built from the same data, and an observer who ran it would be testing self-interacting dark matter, not this. The mass–gas offset is the quantity that *defines* a dissociative merger and is recoverable from the same lensing plus X-ray maps.

**Two offsets, track the gas-lag as primary.** Report both the peak-to-peak separation of the two defects (the Bullet's $\approx 700$ kpc) and the per-subcluster gas-lag (mass peak minus its own gas, the Bullet's $\approx 110$ kpc). Both come from one advection scale (companion §5.5); the per-subcluster gas-lag is the cleaner primary $\Delta r$ because it is defined per subcluster and less sensitive to peak multiplicity.

**Velocity and clock.** $v_{\rm rel}$ near pericenter comes, in order of directness, from (i) a shock Mach number (X-ray shock front or radio relic) converted to a shock speed, (ii) a bespoke hydrodynamic reconstruction, or (iii) the two-BCG line-of-sight velocity difference as a projection-limited lower bound. $t_{\rm post}$, the time since pericenter, comes from the same reconstructions. Because the mid-regime prediction is $\Delta r \propto v_{\rm rel}\, t_{\rm post}$, plot against $v_{\rm rel}\, t_{\rm post}$ where $t_{\rm post}$ exists (tests the slope and ceiling) and against $v_{\rm rel}$ alone for the full sample (tests the knee).

## 4. The Three Hypotheses as Data Signatures

| Feature | Event Density | $\Lambda$CDM (particle DM) | MOND-EFE |
|---|---|---|---|
| Low $v_{\rm rel}$ | flat at $\approx 0$ to a threshold | offset set by per-merger geometry (scatter) | offset fades smoothly to 0 |
| Transition | **sharp knee (step)** | none | gradual ramp |
| Mid $v_{\rm rel}$ | near-linear in $v_{\rm rel}\,t_{\rm post}$ | no universal line | smooth monotonic |
| High $v_{\rm rel}$ | ceiling at $\xi_{KZ}$; fastest may show $>2$ peaks | no ceiling | no ceiling |

The decisive row is the transition: a step (ED), nothing (dark matter), or a ramp (MOND). The other rows corroborate.

## 5. The Discriminating Statistic

Fit the population with three competing models and compare by penalized evidence (BIC/AIC or Bayesian evidence with the stated priors):

- **M0 ($\Lambda$CDM null):** $\Delta r =$ constant $+$ intrinsic scatter, uncorrelated with $v_{\rm rel}$ (offset driven by impact parameter, viewing angle, mass ratio).
- **M1 (MOND-EFE):** $\Delta r =$ a smooth monotonic function of $v_{\rm rel}$, no threshold.
- **M2 (ED):** $\Delta r =$ a segmented (broken) line: zero below $v_{\rm crit}$, linear above, plateau above $v_{\rm sat}$, with the $\sim 15$–$1500$ km/s prior on $v_{\rm crit}$.

**F1** asks whether M1 or M2 beats M0 (is the offset velocity-dependent at all). **F2**, the cleanest discriminator, asks whether M2 (sharp break) beats M1 (smooth), and is run by densely sampling near the inferred $v_{\rm crit}$; a formal change-point test (segmented regression with an F-test on the breakpoint, or a Bayesian broken line with a breakpoint posterior) is the natural instrument. **F3** asks whether a plateau exists at high $v_{\rm rel}$ and whether the fastest systems show $>2$ peaks.

## 6. The Real Dataset

**Ensemble offsets.** Harvey et al. (2015, *Science* 347, 1462) assembled $\sim 30$ merging clusters ($72$ substructures) from the HST/Chandra archive; Wittman et al. (2018, *ApJ* 869, 104) reanalyzed the same sample, corrected substantial offset-measurement errors, and is the more reliable offset source. Use a single uniform pipeline, re-pairing to mass–gas.

**Anchor systems** (lensing $+$ X-ray maps, many with shock/relic velocities and hydro reconstructions): the Bullet (1E 0657-558), MACS J0025.4-1222, Abell 520, Abell 2744, Abell 1758N, the Musket Ball (DLSCL J0916.2+2951), El Gordo (ACT-CL J0102-4915), the Sausage (CIZA J2242.8+5301), Abell 2034, Abell 2163, Abell 56. These anchor the high-velocity end.

**The deliverable table**, which does not yet exist in one place for the mass–gas pairing, is one row per system: $\{\Delta r_{\rm mass\text{-}gas}$, projection flag, $v_{\rm rel}$ + source, $t_{\rm post}$ + source, mass ratio, impact-parameter estimate, number of offset peaks$\}$. Assembling it is the bulk of the observational work; the statistics of §5 are cheap once it exists.

## 7. The Feasibility Reality

The binding difficulty is a selection effect, and stating it is the main contribution of this protocol.

**Dissociative mergers are velocity-selected.** A cluster earns a visible mass–gas offset largely by being a *fast* merger; slow mergers do not separate their components enough to be catalogued as dissociative. So the observed sample concentrates at high $v_{\rm rel}$ (roughly $1000$–$4500$ km/s), which is the **ceiling regime**, and is sparse-to-empty near and below the **knee**, which is where F1 and F2 live. The very selection that builds the sample pushes it past the feature that most distinguishes Event Density.

Consequences, stated plainly:

- **F3 (ceiling, multiplicity) is testable now** against the existing fast-merger sample (El Gordo–class systems): does the offset plateau, and do the fastest mergers show more than two peaks?
- **F1/F2 (the knee) need the under-populated low/marginal-velocity regime:** pre-dissociation mergers, minor mergers, low-Mach systems, and near-zero-offset clusters that current archives discard as "relaxed." These are the diagnostic points, and they are unmeasured precisely because a small offset is undramatic.
- **The knee test is a survey-era measurement.** Rubin/LSST weak lensing, Euclid, and eROSITA X-ray will multiply the sample and fill in the low-offset systems the current archive misses. Naming this converts "measure the relation" into "measure the relation *including the boring low-offset systems*, because the knee lives where the drama does not."

## 8. Confounds and Controls

- **Projection.** Measured $\Delta r \leq$ true 3D $\Delta r$. Use plane-of-sky mergers (MACS J0025, the Sausage) as a cleaner sub-sample; carry a per-system projection flag; or de-project with a viewing-angle prior.
- **Impact parameter and mass ratio.** These modulate $\Delta r$ independently of $v_{\rm rel}$ and are the source of the $\Lambda$CDM scatter; record and marginalize. The ED signal is a *threshold in $v_{\rm rel}$* that survives marginalization; $\Lambda$CDM has no such threshold.
- **$t_{\rm post}$ spread.** Systems are caught at different times since pericenter; the linear regime is in $v_{\rm rel}\, t_{\rm post}$. The per-subcluster gas-lag is less $t_{\rm post}$-sensitive than the peak-to-peak separation.
- **Measurement systematics.** The Harvey $\to$ Wittman revision is a live warning that offsets are hard and method-dependent; use one uniform pipeline, not a heterogeneous literature compilation.
- **Selection (the §7 effect).** Explicitly include archival low-offset "relaxed-looking" mergers, or the knee is unobservable by construction.

## 9. Falsification Criteria

- **F1 — no velocity dependence.** If the mass–gas offset is uncorrelated with merger velocity across the population (M0 wins), the offset–velocity law is wrong and the result favors $\Lambda$CDM.
- **F2 — smooth, not sharp.** If the offset depends on velocity but through a smooth roll-off with no threshold (M1 beats M2), the topological (all-or-nothing) mechanism is disfavored and the result favors MOND-EFE. This is the single cleanest discriminator.
- **F3 — no ceiling.** If the offset grows without bound at the highest velocities, with no plateau and no multiplicity, the freeze-out-scale prediction fails.
- **F4 — knee outside the allowed band.** If a sharp knee is found but at a velocity far outside $\sim 15$–$1500$ km/s, the mechanism's numerical closure (not just its shape) is challenged.

## 10. Position Statement

Event Density predicts that the mass–gas offset in merging clusters rises from zero through a **sharp knee** to a **ceiling** as a function of merger velocity, a shape neither particle dark matter (velocity-independent scatter) nor MOND-EFE (smooth roll-off) produces. This paper makes that prediction executable: it fixes the observable (weak-lensing-mass minus X-ray-gas offset, distinct from the self-interaction literature's dark-matter–galaxy offset), the velocity proxy (shock/relic Mach numbers and hydro reconstructions), and the statistic (segmented-regression model comparison), and it names the dataset (the Wittman ensemble plus the well-characterized dissociative mergers). Two honest boundaries define its use: the test targets the knee's existence and sharpness, which are robust to the mechanism's two open ingredients, not its location, which is not; and dissociative mergers are velocity-selected into the ceiling regime, so the diagnostic knee lives in the under-measured low-offset population that current archives discard and that Rubin, Euclid, and eROSITA will supply. The ceiling and multiplicity predictions are testable now; the knee is a survey-era test. No measurement is claimed. What is offered is a falsifiable, Event-Density-distinctive test of the merging-cluster dark-matter question, with the data named and every outcome's meaning stated, including the outcomes that would count against Event Density.
