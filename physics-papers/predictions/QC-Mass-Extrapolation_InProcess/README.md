# QC-Mass-Extrapolation — Pre-Registered Proposal (In Process)

**Target prediction.** Under Event Density (ED) framework: in matter-wave interferometry, the coherence fraction `V_coh = V_measured / V_env` crosses a quantum-to-classical (Q-C) transition at `V_c_raw ≈ 0.304`. A two-point coherence trajectory anchored at Eibenberger 2013 (~10 kDa, V_coh ≈ 0.82) and Fein 2019 (~25 kDa, V_coh ≈ 0.76) extrapolates the crossing to **molecular mass `m_c ≈ 140,000–250,000 amu`**, 5–10× beyond current Arndt-group experimental reach.

**Origin.** Two-point extrapolation derived in [`retrodictions/fein2019_verdict.md §5.2`](../../retrodictions/fein2019_verdict.md). ED prediction `V_c_raw = 0.304` derived in (legacy) `quantum/effective_theory/visibility_to_bandwidth.md §4.1`; status documented in [project_quantum_program.md](../../../event-density/memory/project_quantum_program.md) (canonical memory pointer).

**Observable.** Coherence fraction `V_coh(m) = V_measured(m) / V_env` as a function of molecular mass `m`, in the range `m ∈ [50,000, 300,000] amu`. Crossing point of `V_coh = 0.304` is the predicted Q-C boundary.

**Prediction (pre-registered).**
1. **Primary.** `V_coh(m)` crosses `0.304 ± 0.05` at `m_c ∈ [140,000, 250,000] amu`. Crossing at `m_c < 100,000` or `m_c > 400,000` would refute the two-point extrapolation under either linear or exponential fit.
2. **Secondary (distinguishing).** In the `D < 0.1` sector approached as `V_coh → V_c`, ED predicts second-harmonic interference content at the 3–6% level (per `Q-C Boundary_Transition` paper §; ED-Phys-16). Standard decoherence theory predicts pure first-harmonic decay. Measurable in the residual of a sinusoidal fit to fringe data near the crossing.

**Platform.** Long-baseline matter-wave interferometry — specifically a LUMI-class or successor instrument capable of `m > 100 kDa`. Candidates:
- **LUMI extension (Arndt group, Vienna)** — the natural home; LUMI was designed extensible. Velocity selection and detection-efficiency limits at high `m` are the documented bottleneck.
- **MAQRO / space-based concepts** — design mass reach `m ~ 10⁶ amu`, but >10-year horizon.
- **Next-generation OTIMA / Talbot-Lau variants** — under discussion in the Arndt-group roadmap.

**Status.** **Stub proposal, 2026-04-28.** Drafted from existing retrodiction analysis as a beamtime/collaboration request. No new derivation, no new data. Three blockers before this becomes a fully-specified protocol:

1. **Promotion of the affine `D_P → D_E` mapping from CANDIDATE to FORCED.** Current V_c = 0.304 prediction depends on three CANDIDATE commitments (three-channel KDTLI scheme, squared-amplitude composition, `b_coh = V²·b_total`). Each affects the predicted crossing value.
2. **Apparatus envelope `V_env(m)` for the target mass range.** Current V_env values (KDTLI ≈ 0.40, LUMI ≈ 0.33) are read from published figures at the operating mass. Envelope for `m > 100 kDa` requires either a Brezger 2003 / Hornberger 2004 reconstruction (factor-12 discrepancy in current first-pass formula) or an empirical extension by the experimental group.
3. **Molecular library at the target mass scale.** A 100–250 kDa Arndt-class molecular library (perfluoroalkylated porphyrin variants extending the Fein 2019 series, or an alternative chemistry) does not yet exist in published form. Synthesis is non-trivial.

**Why a stub now.** This is the highest-leverage matter-wave proposal in the ED program: it specifies a mass range where ED makes a falsifiable prediction *and* standard decoherence theory has no equally sharp commitment. Drafting the proposal now makes the prediction publicly pre-registered before any experiment in the target range is published, which is the relevant epistemic move for an outsider research program. Execution depends on the Arndt group (or successor) reaching the mass range; stub-now-execute-later is the appropriate posture.

**Files.**
- [`proposal.md`](proposal.md) — collaboration / beamtime request draft. Self-contained statement of the prediction, rationale, target measurement, and falsifier conditions.

**Primary collaboration targets.** Markus Arndt (Universität Wien, LUMI/KDTLI); Yaakov Fein (lead author Fein 2019, now at Cambridge); Stefan Gerlich (Vienna, KDTLI); Klaus Hornberger (Duisburg-Essen, decoherence theory). Secondary: MAQRO consortium (Kaltenbaek et al.).

**Cross-references.**
- [`retrodictions/fein2019_verdict.md`](../../retrodictions/fein2019_verdict.md) — source of the two-point extrapolation (§5.2).
- [`retrodictions/arndt_verdict.md`](../../retrodictions/arndt_verdict.md) — Eibenberger 2013 anchor point.
- [`retrodictions/distinguishing_signatures.md`](../../retrodictions/distinguishing_signatures.md) — second-harmonic / N_osc structural observation that the proposal piggybacks on.
- Q-C Boundary paper (in `event-density/papers/root_papers/`) — original ED prediction document.
