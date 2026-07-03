# Pre-Registered Proposal: Q-C Boundary Test at 140–250 kDa via LUMI-Class Interferometry

**Author.** Allen Proxmire (independent researcher, Event Density framework). Contact via Zenodo / GitHub `allen-proxmire`.
**Date drafted.** 2026-04-28.
**Status.** Pre-registered prediction; collaboration request. Not yet endorsed by an experimental group.
**Primary recipients.** Markus Arndt (Universität Wien); Yaakov Fein (Cambridge); successor groups operating long-baseline matter-wave interferometers.

---

## 1. Executive summary

The Event Density (ED) framework predicts a quantum-to-classical (Q-C) transition at a coherence fraction `V_coh = 0.304 ± 0.05` (where `V_coh = V_measured / V_env`). A two-point extrapolation anchored on Eibenberger 2013 (~10 kDa, KDTLI) and Fein 2019 (~25 kDa, LUMI) places the crossing at **molecular mass `m_c ∈ [140,000, 250,000] amu`**, depending on whether the coherence trajectory is linear or exponential in mass.

This is 5–10× beyond the current Arndt-group experimental record. We propose a mass-sweep measurement of `V_coh(m)` on a LUMI-class instrument across `m ∈ [50, 300] kDa`, with the explicit objective of locating (or refuting) the predicted crossing. The prediction is sharp, falsifiable, and made *before* the relevant experiment exists.

The ED-distinguishing secondary observable — second-harmonic content at 3–6% of the fundamental in the `D < 0.1` sector — is extractable from the same fringe data as a residual of the sinusoidal fit, with no additional data acquisition.

---

## 2. The prediction

### 2.1 ED Q-C boundary value

ED's structural commitment dynamics yield a Q-C boundary at coherence fraction:

```
V_c_raw = 0.304    (under three CANDIDATE commitments;
                    see project_quantum_program.md §"Guardrails" item 5)
```

Apparatus-envelope-corrected:

```
V_c_measurable = V_env × V_c_raw
              ≈ 0.122  (KDTLI, V_env ≈ 0.40)
              ≈ 0.100  (LUMI,  V_env ≈ 0.33)
```

### 2.2 Two-point coherence trajectory

Under the envelope-corrected framework:

| Anchor | Mass (amu) | V_measured (peak) | V_env | V_coh = V_measured / V_env |
|---|---|---|---|---|
| Eibenberger 2013 (L12, KDTLI) | ~10,000 | 0.33 | ≈ 0.40 | ≈ 0.82 |
| Fein 2019 (25 kDa library, LUMI) | ~25,000 | 0.25 | ≈ 0.33 | ≈ 0.76 |

A linear extrapolation in mass crosses `V_coh = 0.30` at:
```
m_c (linear) ≈ 140,000 amu
```

An exponential decay `V_coh = V_0 · exp(−m / m_0)` fits with `m_0 ≈ 200,000 amu` and crosses at:
```
m_c (exponential) ≈ 240,000 amu
```

### 2.3 Pre-registered falsifiable predictions

**Primary.** A measurement of `V_coh(m)` over `m ∈ [50, 300] kDa` shall observe a crossing of `V_coh = 0.304 ± 0.05` at some `m_c ∈ [100, 350] kDa` (admitting two-point-extrapolation uncertainty).

- **Confirmation:** crossing observed in `[100, 350] kDa`.
- **Refutation:** monotone `V_coh > 0.40` throughout `m ∈ [50, 300] kDa` (no approach to crossing) **OR** rapid crossing at `m_c < 100 kDa` (trajectory steeper than the two-point fit predicts).

**Secondary (distinguishing).** As `V_coh` approaches `V_c` from above, ED predicts second-harmonic interference content at 3–6% of the first-harmonic amplitude. Standard decoherence theory predicts no such structure (pure first-harmonic exponential decay). Measurable in the residual of a sinusoidal fit to fringe data at any mass within `m ∈ [80, 200] kDa`.

- **Confirmation:** residual second-harmonic in the 2–8% band at the predicted masses.
- **Refutation:** residual consistent with zero (< 1%) at all measured masses.

---

## 3. Why this matters

### 3.1 Sharpness of the prediction

Standard decoherence theory (Joos-Zeh, Hornberger, etc.) predicts that visibility decays with mass; it does not commit to a specific crossing value of `V_coh` and does not predict a sharp transition. The 0.304 value is ED-specific. A measurement of `V_coh(m)` with sufficient mass span will either find a crossing where ED predicts (and standard theory is silent) or fail to find one (refuting ED).

### 3.2 Distinguishing test, not threshold-only

The second-harmonic prediction is independent of the crossing-mass prediction and exposes ED to refutation even if the experimental mass range falls short of `m_c`. The residual of any high-quality fringe fit at `m ≥ 80 kDa` is sufficient.

### 3.3 Pre-registration epistemic value

The two-point extrapolation is published openly (this document; [`fein2019_verdict.md`](../../retrodictions/fein2019_verdict.md)) before any experimental dataset in the target mass range exists. This is the epistemic move available to an independent research program: write the falsifier down first, then wait for the data.

---

## 4. Proposed measurement

### 4.1 Target instrument

**LUMI extension or successor.** Required instrument capability:

- Mass range: at least `m ∈ [50, 200] kDa`, ideally `[50, 300] kDa`.
- Visibility resolution: `σ_V ≤ 0.02` at `V ≈ 0.05–0.30`.
- Fringe-fit harmonic content extraction: capability to fit `V_1 sin(φ + φ_0) + V_2 sin(2φ + φ_0') + noise` with `σ_{V_2} ≤ 0.01`.
- Velocity selection and chopping: as in Fein 2019, scaled to lower velocities for higher-mass molecules.

### 4.2 Target molecular library

A perfluoroalkylated porphyrin or equivalent extended-chain library spanning `m ∈ [50, 300] kDa`. The Fein 2019 chemistry (tetraphenylmethane core + 4 zinc-coordinated porphyrin branches + fluoroalkylsulfanyl chains) is extensible in principle by adding more or longer fluoroalkyl branches. Synthesis route is the responsibility of the experimental collaboration; this proposal does not specify it.

Minimum coverage: 5 mass points distributed log-uniformly across the target range (e.g., 50, 80, 130, 200, 300 kDa). Three points minimum to constrain a trajectory shape; five gives crossing localization.

### 4.3 Apparatus-envelope characterization

**Required accompanying measurement.** `V_env(m)` for the LUMI-class instrument across the target mass range. Current `V_env_LUMI ≈ 0.33` is at `m ≈ 25 kDa`. At higher mass:

- Velocities are lower → Talbot times longer → potentially higher V_env contribution from spread-related dephasing reduction.
- Vertical-fall over `2 × 0.98 m` baseline becomes relevant at slow velocities → potential gravity-correction needed.
- Detection efficiency at higher mass may reduce signal but not envelope.

The envelope-correction formula (Brezger 2003; Hornberger 2004) is the principled route; a first-pass reconstruction of that formula by the present author yielded a factor ~12 discrepancy with empirical readings, and is explicitly flagged as not authoritative. Empirical V_env extension from quantum-prediction-curve peaks at each measured mass is the direct route.

### 4.4 Data products requested

For each mass point `m_i`:

1. Raw fringe data `count(transverse displacement)` at the optimal laser power (the quantum-prediction peak).
2. Sinusoidal fit visibility `V_measured(m_i)` with error bar.
3. Quantum-prediction-curve maximum across laser power: `V_env(m_i)`.
4. Coherence fraction `V_coh(m_i) = V_measured(m_i) / V_env(m_i)`.
5. Sinusoidal-fit residual harmonic decomposition: `V_2(m_i) / V_1(m_i)` — second-harmonic ratio.
6. Apparatus parameters at this run: velocity distribution `(v, Δv)`, gas pressure, photon-emission environment estimate.

---

## 5. What this proposal does NOT do

To pre-empt likely concerns from collaboration partners:

- **Does not derive ED.** The framework lives in the linked repositories (`event-density`, `ED-primitives`, `ed-lab`). This proposal cites the prediction; it does not re-argue it.
- **Does not promote the CANDIDATE commitments.** The 0.304 value depends on three CANDIDATE commitments (three-channel KDTLI scheme, squared-amplitude composition, `b_coh = V²·b_total`). The crossing-mass uncertainty `[140, 250] kDa` already absorbs this; further sharpening is a theory task, not an experimental one.
- **Does not propose synthesis.** The 100–300 kDa molecular library is the limiting resource; the proposal commits no synthesis route.
- **Does not propose CSL parameter-space competition.** Fein 2019's primary distinguishing test (CSL bounds) is orthogonal to ED's primitive-level structure. The CSL-to-ED parameter bridge is open theory work; it is not assumed here.

---

## 6. Failure modes and what they teach

| Outcome | Implication for ED | Implication for the field |
|---|---|---|
| Crossing at `m_c ∈ [100, 350] kDa` | Two-point trajectory and V_c = 0.304 both confirmed | First experimental observation of a sharp Q-C transition; would also constrain CSL parameter space at higher mass |
| No crossing at `m ≤ 300 kDa` (V_coh > 0.40 throughout) | Refutes the linear/exponential extrapolations and possibly V_c = 0.304 (depending on the V_coh values observed) | Pushes Q-C transition (whatever its origin) to even higher mass — a result of interest independent of ED |
| Crossing at `m_c < 100 kDa` | Refutes ED's prediction; trajectory steeper than two-point | Important constraint for any framework that predicts a Q-C transition |
| Second-harmonic residual at 3–6% in `m ≥ 80 kDa` regime, no crossing observed | Distinguishing-signature confirmation; supports ED structural prediction without requiring crossing | Novel structural feature in matter-wave fringes, of theoretical interest regardless of source |
| Residual consistent with zero across all measured masses | Refutes the second-harmonic prediction; weakens but does not eliminate ED | Reaffirms standard decoherence pure-first-harmonic prediction |

All five outcomes are publishable. The prediction is genuinely two-sided.

---

## 7. Status of the proposing program

This is being submitted by an independent researcher with no academic affiliation, no advisor, no group, and no arXiv endorsement. The framework (Event Density) has DOIs through Zenodo and a public GitHub trail covering primitives, derivations, retrodictions, and pre-registered predictions. The relevant pre-registration trail for this specific prediction:

- ED Q-C boundary derivation: `quantum/effective_theory/visibility_to_bandwidth.md` (legacy location; archived as of 2026-04-27 reorganization, see [project_qm_emergence_arc.md](../../../event-density/memory/project_qm_emergence_arc.md))
- Eibenberger 2013 anchor: [`retrodictions/arndt_verdict.md`](../../retrodictions/arndt_verdict.md), 2026-04-24
- Fein 2019 anchor and two-point extrapolation: [`retrodictions/fein2019_verdict.md`](../../retrodictions/fein2019_verdict.md) §5, 2026-04-24
- This proposal: [`predictions/QC-Mass-Extrapolation_InProcess/proposal.md`](proposal.md), 2026-04-28

The intent of the proposal is to make the prediction *pre-registered, public, and citable* before any experimental dataset in the target mass range exists. Whether ED ultimately survives the test is a question the data will answer; whether the prediction was made in advance is a question this document settles.

---

## 8. Request

We invite the Arndt group and successor collaborations operating long-baseline matter-wave interferometers to:

1. Acknowledge or critique the pre-registered prediction in §2.3.
2. Indicate whether the target measurement (§4) is feasible on existing or planned hardware, and on what timescale.
3. Identify the dominant blocker — instrument mass reach, molecular library synthesis, beamtime availability — and whether a smaller-scope variant (e.g., a 3-mass-point sweep extending only to `m ≈ 80 kDa` to anchor a third trajectory point) would be a useful intermediate.
4. Engage on the distinguishing-signature secondary observable (§2.3 secondary) which can be tested at lower mass without extending instrument reach.

A dataset accommodating one or more of these requests would, regardless of outcome, generate a citable verdict on a pre-registered prediction made by an external program. The author commits to publishing the verdict — confirmation, refutation, or null — within 60 days of receiving the data.

---

## 9. Cross-references

- Two-point extrapolation source: [`retrodictions/fein2019_verdict.md`](../../retrodictions/fein2019_verdict.md) §5.
- Eibenberger anchor: [`retrodictions/arndt_verdict.md`](../../retrodictions/arndt_verdict.md).
- Distinguishing-signature memo: [`retrodictions/distinguishing_signatures.md`](../../retrodictions/distinguishing_signatures.md).
- Program memory pointer: [project_quantum_program.md](../../../event-density/memory/project_quantum_program.md).
- Q-C Boundary theory paper: `event-density/papers/root_papers/Q-C Boundary_Transition. Theory, Prediction, Path.pdf`.
