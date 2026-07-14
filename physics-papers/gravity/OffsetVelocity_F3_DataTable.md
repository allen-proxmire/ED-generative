# F3 Anchor Table: Compiled Mass–Gas Offsets and Merger Velocities for the Offset–Velocity Test

**Companion data table to `Paper_OffsetVelocityLaw_MergingClusterTest`** (the ceiling + multiplicity leg, F3). Assembled 2026-07-14 from the primary literature. **Provenance: this is a v1 literature compilation, not a uniform-pipeline measurement.** Every number is tied to a citation; values flagged contested/model-dependent are marked. It is exactly the table the paper (§6) says "does not yet exist in one place" — a starting point, not a result.

## What F3 predicts (from `Paper_117_Bullet_TopologicalDefect` §5)

- Ceiling: the mass–gas offset saturates at **ξ_KZ ≈ 860 kpc** (never exceeds it — beyond that the defects are no longer a correlated pair).
- Saturation velocity **v_sat ≈ 5600 km/s**; below it, advection-limited (offset ∝ v_rel·t_post); above it, ceiling.
- Multiplicity: the **fastest** mergers may show **>2** offset peaks.

## The table

Δr conventions: **gas-lag** = per-subcluster (weak-lensing mass peak − its own X-ray gas peak); **peak-sep** = separation between the two subcluster mass peaks. The paper's *primary* Δr is the gas-lag. Velocity = **collision/subcluster** velocity (distinct from shock-front speed, which is faster); the method is noted.

| System | z | gas-lag (kpc) | peak-sep (kpc) | v_coll (km/s) | method | t_post (Gyr) | mass ratio | # peaks | geometry |
|---|---|---|---|---|---|---|---|---|---|
| **Bullet** 1E 0657-56 | 0.30 | ~110 (main), ~270 (bullet) | ~700–720 | **~2700** | hydro sim (shock 4740) | ~0.15 | ~7–10:1 | 2 | plane-of-sky |
| **El Gordo** J0102-4915 | 0.87 | ~62 (2σ) | ~700 | ~2250 infall; **≳4700** at peri | hydro sim | ~0.48 | ~1.9:1 | 2 | inclined |
| **Sausage** J2242+5301 | 0.19 | not clean¹ | (elongated) | ~2000–2500 | dyn/hydro (relic ℳ4.6) | ~0.6–0.8 | ~1.3–2.5:1 | 2 | plane-of-sky (edge-on) |
| **A520** Train Wreck | 0.20 | **~0** (coincident)² | — | ~1000 (shock 2300) | X-ray shock ℳ2.2 | ~1 | ~1:1 | 5–6² | ~60° |
| **A2744** Pandora | 0.31 | ~77 (core), ~136 (N/W)³ | — | ~2900 (LOS split) | optical LOS | ~0.12–0.15 | ~2.6–3:1 | **4–8+** | ~27° |
| **MACS J0025** Baby Bullet | 0.59 | ~192 (NW), ~316 (SE) | — | ~2000 (crude⁴) | dispersion-scaled | ~0.3–1 | ~1:1 | 2 | plane-of-sky (LOS 100) |
| **Musket Ball** J0916 | 0.53 | ~530 | ~1000 (3D ~1600) | **2300** at peri; 670 now | MC dynamics | **1.1** (0.7–2.4) | ~1.8:1 (WL) | 2 | ~48° |
| **A1758N** | 0.28 | ~408 (NE); NW coincident | — | ~423 (LOS only) | spectroscopic | ~0.27 | ~1.44:1 | 2 | ~21° |
| **A2034** | 0.11 | ~350 (S) | — | ~1767 (shock 2057, ℳ1.59) | MC + shock | ~0.56 | ~2.18:1 | 2 (of 8) | ~27° |
| **A2163** | 0.20 | ~240 | — | **not found** | — | <1 (qual.) | ~3:1 | 2–3 | plane-of-sky |
| **A56** J1508+5755 | 0.30 | ~103–118 | ~438 | ~184 (LOS) | hydro sim | ~0.52 (or 0.12) | ~1.6:1 | 2 | ~58° |

¹ Sausage gas is N–S elongated with no bullet-like peaks; a clean lensing-vs-gas offset isn't defined (a catalog quotes 0.45–0.89 Mpc, flagged contested). ² A520's mass "dark core" sits *on* the gas (offset ≈ 0) — the anti-Bullet; the core is **contested** (Mahdavi 2007 / Jee 2012 claim it, Clowe 2012 refutes). ³ A2744's NW "ghost" clump has gas *leading* mass (>150 kpc, reversed) — an interloper. ⁴ Bradač 2008 explicitly labels the ~2000 km/s a "crude" dispersion-scaling estimate, not a measurement.

## Preliminary F3 read (honest — this is weak, and here is exactly why)

**Ceiling (F3a): consistent but unstressed.** Every per-subcluster gas-lag falls in 0–530 kpc — **none exceeds ξ_KZ ≈ 860 kpc**. Peak-separations reach ~700 kpc (Bullet, El Gordo) and ~1000 kpc (Musket Ball, an old merger whose subclusters have flown apart). So the data violate no ceiling — but this is weak: nothing pushes *against* 860 kpc, and every collision velocity is **below v_sat ≈ 5600 km/s** (the fastest, El Gordo, is ≳4700 at pericenter). The sample never enters the saturated regime, so it cannot actually test the cap; it only fails to contradict it.

**Multiplicity (F3b): confounded, leans against the naive reading.** The systems with the most peaks — A2744 (4–8+) and A520 (5–6) — are **not** the fastest; they are complex multi-way mergers at moderate velocity. The genuinely fast binaries (Bullet ~2700, El Gordo ≳4700) show exactly **2**. So "fastest ⇒ >2 peaks" is not supported here: multiplicity tracks merger *complexity/mass*, not velocity. A real test must separate primordial multi-way-infall substructure from Kibble–Zurek defect-network multiplicity — this compilation cannot.

**The advection slope (F3, mid-regime): no law survives the heterogeneous data.** Predicted gas-lag `v_coll·t_post` vs observed: Bullet 414 vs ~110–270 (2×), El Gordo **2307 vs ~62 (37×)**, Musket Ball 2587 vs ~530 (5×), A2034 1012 vs ~350 (3×), A1758N 117 vs ~408 (0.3×), A56 98 vs ~103 (≈1×). The naive `Δr = v·t` scatters by more than an order of magnitude in *both* directions. This is dominated by projection (62 kpc for inclined El Gordo vs 700 kpc peak-sep), method heterogeneity (gas-lag vs gas-BCG vs peak-sep mixed across papers), and order-of-magnitude t_post. **It confirms the paper's own §7 caveat with numbers: a literature compilation cannot do this test; a uniform re-measurement pipeline is required.**

## What a real F3 test needs (beyond this table)

1. **A uniform-pipeline mass–gas offset** for all systems from one method (re-reduce the lensing + X-ray maps identically) — not the mixed literature quantities above. This is the bulk of the work the paper names.
2. **The actual advection+ceiling offset model** (from the hydro closure), not `v·t`, to predict Δr(v_coll, t_post, projection) per system with de-projection.
3. **Systems near/above v_sat ≈ 5600 km/s** to stress the ceiling — none exist in the current dissociative sample (the velocity-selection effect of §7).
4. **A multiplicity metric** separating KZ-network >2-peaks from multi-way infall.

## Honest bottom line

The table is real and cited, and it is a usable starting scaffold that did not exist in one place. But run against it, **F3 today gives only "not contradicted, weakly"**: the ceiling is unviolated but unstressed (no system reaches v_sat), the multiplicity signal is confounded by merger complexity, and the mid-regime slope is buried in projection/method scatter. This is consistent with the parent paper's position — F3 is "checkable now" only in the limited sense that no gross violation appears; a decisive test still needs the uniform pipeline and the survey-era low-velocity systems (F1/F2). No claim of confirmation is made.

## Sources (per system)

Bullet: Clowe et al. 2006 ApJ 648 L109; Markevitch 2006 (shock); Springel & Farrar 2007 MNRAS 380 911; Paraficz et al. 2016 A&A 594 A121. — El Gordo: Jee et al. 2014 ApJ 785 20; Molnar & Broadhurst 2015 ApJ 800 37. — Sausage: van Weeren et al. 2010 Science 330 347; Dawson et al. 2015 ApJ 805 143; Jee et al. 2015 ApJ 802 46; Finner et al. 2024 (offset catalog, flagged). — A520: Mahdavi et al. 2007 ApJ 668 806; Jee et al. 2012 ApJ 747 96; **Clowe et al. 2012 ApJ 758 128 (refutes dark core)**; Wang et al. 2018. — A2744: Merten et al. 2011 MNRAS 417 333; Owers et al. 2011 ApJ 728 27; Jauzac et al. 2016 MNRAS 463 3876. — MACS J0025: Bradač et al. 2008 ApJ 687 959; Riseley et al. 2017 A&A 597 A96. — Musket Ball: Dawson et al. 2012 ApJL 747 L42; Dawson 2013 ApJ 772 131 (arXiv:1210.0014). — A1758N: Monteiro-Oliveira et al. 2017 MNRAS 466 2614. — A2034: Monteiro-Oliveira et al. 2018 MNRAS 481 1097; Owers et al. 2014 (shock). — A2163: Soucail 2012 A&A 540 A61. — A56: Albuquerque, Machado & Monteiro-Oliveira 2024 MNRAS 530 2146; Wittman et al. 2023. — Ensemble offset reference (DM–galaxy, for re-pairing): Wittman et al. 2018 ApJ 869 104; Harvey et al. 2015 Science 347 1462.
