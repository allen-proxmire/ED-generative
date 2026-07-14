# Track B Literature Dig — Finding (2026-07-14)

**Task.** Find public high-framerate FRAP data on *concentrated* samples suitable for the ED-09.5 participation-envelope test at the corrected band `f_v ≈ 1.1·γ_dec ≈ 11–110 Hz` (needs sampling ≥ ~250 Hz, ideally ≥ 500 Hz; concentrated/crowded regime so `γ_dec` is high enough to put `f_v` in-band).

**Bottom line.** One instrument class cleanly meets both hard requirements — **Line-FRAP** (Dey, Marciano & Schreiber, *J. Mol. Biol.* 2021; biorxiv 2020.07.01.181750). No ready-to-download raw-trace dataset was located. The realistic path is a **data request to the Schreiber lab** (real, reachable, Weizmann), gated by one physics check that must be done first (record-length / cycle-count, below). This supersedes the protocol §7 candidate list (Mueller 2008 ~100 Hz, Kang 2012, Wachsmuth 2003 — all borderline on framerate and not deposited).

## Why Line-FRAP is the right instrument class

| Requirement | Line-FRAP | Verdict |
|:---|:---|:---|
| Sampling ≥ ~250 Hz | **800 Hz line rate** (vs 20–50 Hz classical); linescan modes at 1000/500/125 Hz reported | ✓ covers full 11–110 Hz band (Nyquist 400 Hz) |
| Concentrated / crowded regime (high `γ_dec`) | in vitro, HeLa (~2.5× slower), *E. coli* (~15× slower), **osmotic stress increased until proteins stop moving** | ✓ spans dilute → near-arrest; the high end is exactly the high-`γ_dec` target |
| Standard, reproducible instrument | standard confocal, line mode; method paper with full protocol | ✓ |
| Fast diffusers (short `τ`) | designed specifically for fast-diffusing molecules | ✓ but see record-length risk |

The osmotic-stress series is the most valuable feature: it is a **`γ_dec` sweep in one system** — precisely the axis the ED prediction lives on (`f_v ∝ γ_dec` across 10+ orders of magnitude). If any Line-FRAP data can test ED-09.5, it is the crowded / osmotically-arrested end.

## The two blockers (honest)

1. **No public raw traces found.** JMB 2021 predates routine raw-data deposition; no Zenodo/figshare/GitHub deposit surfaced. The paper's observable is bleach-depth-per-line; whether the **un-smoothed per-line intensity time series** (which carries any 11–110 Hz residual) is retained is unknown. → Action: request raw `I(t)` per-line traces + metadata from the Schreiber lab. This is the same class of ask as the Track A Aspelmeyer request, but to a group with no competitive overlap and a method-sharing paper — lower friction.

2. **Band placement — RESOLVED by the viability calc ([`ViabilityCalc_LineFRAP_2026-07-14.md`](ViabilityCalc_LineFRAP_2026-07-14.md)).** Using `γ_dec ≈` FRAP recovery rate `k = D/w²`: the **crowded cellular** conditions (HeLa, E. coli, mild osmotic stress) land `f_v` inside 11–110 Hz for plausible spot sizes; dilute buffer overshoots (too fast), heavy arrest undershoots (too slow, `f_v → 0`). **The sweet spot is intermediate crowding, NOT the arrested end** (this corrects an earlier guess in this note). Cycle count is non-binding at 800 Hz (≥3 cycles need only 27–200 ms of record; the line rate oversamples). So the arithmetic **passes** for the crowded-cell conditions; the data request is worth drafting. The remaining risks are residual **SNR** (few-% modulation on noisy post-bleach traces — mitigate by coherent averaging over bleach-triggered replicates) and the **theory mapping** (γ_dec identification / oscillatory-vs-parabolic side), not the frequency placement.

## Recommendation (fork)

- **Path 1 — pursue Line-FRAP:** compute `γ_dec`/`f_v` for the paper's most-crowded conditions from its `D` table; if in the viable window, draft a data request to Schreiber (raw per-line `I(t)`, longest records, most-crowded/arrested samples). Zero cost; success gated on their willingness + record length.
- **Path 2 — the certain, no-data alternative:** run the **spatial-PDE harmonic legs (F4/F5)** — the third-harmonic ratio and triad coupling — by driving the canonical ED PDE with the P7 gradient term (the uniform-mode run already done in `ED_PDE_Drive_Finding_2026-07-10.md` cannot test these). No data, no funding, no permission; sharpens the prediction (locks the F4/F5 numbers) so that *any* future dataset — Line-FRAP or the in-house high-framerate FRAP add-on — has the full pre-registered target. This is the higher-certainty use of effort.

**Suggested order:** do the Path-1 `γ_dec` viability calc first (it is ~30 minutes and decides whether the data request is even worth sending), then default to Path 2 regardless, since it is the guaranteed-progress leg and makes every downstream dataset more decisive.

## Log

- Instrument-class match found: Line-FRAP (800 Hz, crowded/arrested regime). Promoted to top Track B candidate.
- No public raw-trace repository located (searched: FRAP + high-framerate + concentrated + deposited/Zenodo/figshare; condensate-FRAP; line-scan FRAP; point/photometric FRAP).
- Superseded protocol §7 candidates (Mueller/Kang/Wachsmuth): all sub-viable on framerate and/or not deposited.
- Corrected band used throughout: `f_v ≈ 1.1·γ_dec`, 11–110 Hz (per `ED_PDE_Drive_Finding_2026-07-10.md`), not the retired 80–800 Hz.

**References.** Dey D., Marciano S., Schreiber G. *Line-FRAP…* J. Mol. Biol. 433, 166898 (2021); biorxiv 10.1101/2020.07.01.181750. Related: Rapaport/line-FRAP membrane variant (Membranes 10, 434, 2020).
