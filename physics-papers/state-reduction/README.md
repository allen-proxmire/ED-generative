# ED State Reduction — the measurement/gravity seam

**What this folder is.** The **standalone state-reduction papers** — Event Density's peer-facing statement on gravitational collapse of the wavefunction, positioned against its three nearest published neighbors (Diósi, Penrose, Hossenfelder). This is the *measurement-side* companion to the dark-sector folder: Penrose and Hossenfelder are ED's measurement-side interlocutors as Berezhiani and Khoury are its dark-matter-side ones. The *working record* behind these (the outline and the referee history) lives in the `event-density` working repo under `theory/State_Reduction/`.

## The position in one paragraph

The three neighbors all say **gravity causes collapse** and put the scale in an energy (`E_G`, the gravitational self-energy of the difference of the mass distributions). ED says something adjacent but deeper: the **definiteness of measurement outcomes and the flow of gravitational time are one primitive** — the arrow of commitment (P11), which *is* the khronon — so the collapse variable is **time, not energy**, and the "cause" is not a cause but an identity. Read against Penrose specifically, ED **supplies the well-defined preferred time whose absence drives his argument**; read against Hossenfelder, ED shares her matter-equals-geometry ontology (`g ~ 1/b`) and buys locality with a forward arrow instead of her superdeterminism. The honest ledger, after adversarial review: a deep reframe, a **scaling argument that reproduces `τ ∝ ℏ/E_G`** (coefficient and exact energy functional open), one externally confirmed falsifiable fork (**difference-not-sum**, against Hossenfelder), and a **retired experimental risk** (the 2020 Gran Sasso spontaneous-radiation bound does not exclude ED's discrete which-channel commitment — but that is immunity shared with standard QM, not a distinctive win) with three named open pieces.

## The papers (this folder)

- **[Paper_ED_StateReduction_vs_CollapseModels.md](Paper_ED_StateReduction_vs_CollapseModels.md)** — **START HERE.** The peer-facing positioning note: the shared conviction (geometry not an independent quantized field; collapse physical and gravity-rooted), ED's cited account (§4 arrow = einselection = pointer basis; §6 arrow = khronon), the three neighbors gift-then-diverge, the unifying difference (time not energy), the honest gap, position, falsifiers, and tiers.
- **[StateReduction_CollapseRate_ED_Derivation.md](StateReduction_CollapseRate_ED_Derivation.md)** — the companion **derivation**: the `τ ∝ ℏ/E_G` scaling argument from the khronon-clock difference + einselection, its three forks from the rivals, and the emission-signature analysis (why the 2020 bound does not exclude ED, honestly scoped). Detailed working behind §5 of the positioning note.

## Status (after adversarial referee, 2026-07-21)

Refereed against the corpus and the four external sources; verdict **major revisions, all applied**. What stands: the Hossenfelder sum-vs-difference fork (verified, externally sourced), the Diósi/Penrose characterizations, corpus discipline, the §6 guardrail carried honestly. What was corrected: the collapse rate is a **scaling argument**, not a structural derivation (`E_G` identified with Penrose's answer, not computed); the 2020 immunity is **shared with standard QM**, not a distinctive prediction.

**Residual (ii) now resolved (2026-07-21).** The referee's sharpest objection — that "no momentum diffusion of a localized charge" was in tension with P11's dissipative (line-gap) face — is answered from the corpus. The Lindblad derivation (`event-density` `arcs/arc-Q/lindblad_extension.md`) fixes, FORCED from P11, that ED's jump operators are **channel projectors** `Ĵ_α = g_α Π̂_α`, not position operators; so a committed charge `ρ = Π̂_α` is an **exact fixed point** of the dissipative face (`D[Π̂_α] = 0`), with no continuous momentum diffusion — unlike CSL/DP, whose position-coupled noise has no fixed point and pumps `d⟨p²⟩/dt = const` forever. The line-gap face is not suppressed; it simply has the committed states as dark states. The same argument covers the spontaneous-heating bound. Tier: **structural result** (FORCED identification + exact algebra). **Two open pieces before this is a finished result:** (i) compute the energy functional / coefficient from the participation fields; (i-quant) pin the channel granularity that sets the one-time decoherence-burst magnitude (in a channel-continuum limit ED would recover CSL/DP diffusion, so this is the one quantitative sensitivity).

## Source papers (this folder synthesizes, it does not supersede)

- **Measurement / arrow = einselection:** `../../ED_UnifiedFramework_Report.md` §4; `qm-kinematics/Paper_001_PreIndividuation.md`, `Paper_003_BornRule.md`, `Paper_005_ProjectiveMeasurement.md`; the Gleason keystone.
- **Arrow = khronon / gravity's time:** Report §5–§6; `gravity/Paper_GR-I_WeakFieldEinsteinMetric.md`, `Paper_GR-II_KhronometricClass.md`; `gravity/Paper_QuadraticStrain_v1.md` (gravity = interference cross-term, not Einstein–Hilbert — bears on the exact energy functional).
- **Locality without superdeterminism:** the A1 channel-capacity-zero result (`event-density` `Bits/docs/A1_ChannelCapacity_Results.md`).
- **P11's two non-Hermitian faces:** `event-density` `theory/Anomaly_Cancellation/` (point-gap worldline vs line-gap Lindblad).

## The neighbors (external)

Diósi 1987 (Phys. Lett. A 120, 377); Penrose 1996 (GRG 28, 581); Hossenfelder 2025 (arXiv 2510.11037); the 2020 spontaneous-radiation exclusion (Donadi et al., *Nat. Phys.* 17, 74 (2021); arXiv 2111.13490) and the follow-up effectiveness-of-collapse literature.
