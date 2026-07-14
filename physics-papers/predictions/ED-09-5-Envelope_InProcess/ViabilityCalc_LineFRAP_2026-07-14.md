# Line-FRAP Viability Calc — Does f_v Land In-Band? (2026-07-14)

**Question.** For Line-FRAP's measured conditions, does the corrected envelope prediction `f_v ≈ 1.1·γ_dec` land in the 11–110 Hz band, and do ≥3 envelope cycles fit a usable record at the 800 Hz line rate? This decides whether a data request to the Schreiber lab is worth drafting.

**Identification used.** `γ_dec ≈` the FRAP recovery rate `k = D/w²` (D = measured diffusion coefficient, w = confocal bleach half-width). This is the self-consistent reading of the §6 mapping: the recovery rate is the slow observable rate that plays the role of the participation-channel decoherence `γ_dec`; the fast "system frequency" `ω_m` is a microscopic (collision/vibration) scale, so `D_disc = γ_dec/ω_m ≪ 1` (deep oscillatory side) is preserved. *(The protocol §6 table line "ω_m ↔ 1/τ_D" conflates the recovery rate with the fast scale; that line is the confusing one and is not used here — see caveat 2.)*

**Inputs.** D from Line-FRAP: buffer ≈ 50 µm²/s for their small labelled proteins; abstract fold-slowdowns HeLa ÷2.5, E. coli ÷15, osmotic stress further (→ arrest). Spot size w swept 0.3–0.8 µm (confocal line width, order diffraction limit). *D values are order-of-magnitude estimates pending the paper's exact D table + w.*

## Result — band placement

`f_v = 1.1 · D/w²` (Hz, D in µm²/s, w in µm):

| Condition | D (µm²/s) | f_v @ w=0.3 | f_v @ w=0.5 | f_v @ w=0.8 |
|:---|---:|---:|---:|---:|
| buffer (dilute) | 50 | 611 (hi) | 220 (hi) | **86 (IN)** |
| HeLa cytoplasm | 20 | 244 (hi) | **88 (IN)** | **34 (IN)** |
| E. coli cytoplasm | 3.3 | **40 (IN)** | **15 (IN)** | 5.7 (lo) |
| E. coli + osmotic | 1.2 | **15 (IN)** | 5.3 (lo) | 2.1 (lo) |
| near-arrest | 0.3 | 4.0 (lo) | 1.5 (lo) | 0.6 (lo) |

**Verdict: viable in the intermediate-crowding regime.** The **crowded cellular** conditions (HeLa, E. coli, mild osmotic stress) put `f_v` inside 11–110 Hz for plausible spot sizes. Dilute buffer **overshoots** (too fast → f_v above band); heavy arrest **undershoots** (too slow → below band). At any single w, *some* crowded condition is in-band; the exact one shifts with w (a ~4× lever across w = 0.3–0.8 µm), so the target condition must be picked using the paper's real D + w.

**This corrects the dig note's earlier guess** that the most-arrested end is best: under `γ_dec ≈ recovery rate`, arrest drives `γ_dec → 0` and `f_v` *below* the band. The sweet spot is **cytoplasmic / mildly-stressed crowding**, not near-arrest, and not dilute buffer.

## Result — cycle count (at 800 Hz)

| f_v | envelope period T_v | record for ≥3 cycles | samples/cycle |
|---:|---:|---:|---:|
| 15 Hz | 67 ms | 200 ms | 53 |
| 40 Hz | 25 ms | 75 ms | 20 |
| 90 Hz | 11 ms | 33 ms | 9 |
| 110 Hz | 9 ms | 27 ms | 7 |

**Cycle count is not the blocker.** 800 Hz oversamples the whole band (≥7 samples/cycle at 110 Hz), and ≥3 cycles need only 27–200 ms of usable post-bleach record — comfortably within a typical Line-FRAP acquisition (recovery + baseline, ~1 s). At the in-band conditions (15–90 Hz) this is easy.

## The two real risks (neither is the arithmetic)

1. **SNR of the residual.** The predicted envelope + third-harmonic is a *few-percent* modulation, sitting on a noisy post-bleach trace (low photon count after the bleach). This, not framerate or cycle count, is the dominant detection risk. **Mitigation:** the envelope is *bleach-triggered*, so it is phase-locked across replicates → **coherent averaging over the replicate acquisitions** pulls out a phase-locked residual that incoherent noise averages away. Any data request must ask for the individual replicate traces, not the averaged curve.
2. **Theory mapping (unchanged by this calc).** The `γ_dec ≈ recovery-rate` identification and the oscillatory-vs-parabolic-side question (does classical protein diffusion sit on the ED PDE's oscillatory side at all?) remain the standing soft spot — the §22 candidate identification. This calc shows the numbers *work if the mapping holds*; it does not validate the mapping.

## Decision

**The data request is worth drafting** — but targeted, not generic:
- Ask the Schreiber lab for **raw per-line `I(t)` traces (all replicates, un-averaged)** for the **crowded** conditions (HeLa and E. coli, incl. the osmotic-stress series), plus w (bleach geometry) and per-condition D.
- State the analysis up front (coherent-averaged Lomb–Scargle residual in 11–110 Hz) so they know it is a re-analysis, not a critique.
- Pre-condition to send: none blocking — the arithmetic passes. The honest framing of the theory caveat (2) should be in the ask so the collaboration is entered clear-eyed.

**But the guaranteed-progress leg is still Path 2** (the spatial-PDE F4/F5 harmonic legs), because it needs no one's data and it fixes the third-harmonic/triad numbers this calc assumed — making any dataset that does arrive fully decisive. Recommended order unchanged: request drafted now (arithmetic passes), Path 2 run regardless.

## Log
- `f_v = 1.1·D/w²`; crowded cellular conditions land in 11–110 Hz for w = 0.3–0.8 µm; buffer overshoots, arrest undershoots.
- Cycle count non-binding at 800 Hz.
- Corrected the dig note's "arrested end is best" → intermediate crowding is the sweet spot.
- Dominant risk = residual SNR; mitigation = coherent averaging over bleach-triggered replicates.
- Calc: `scratchpad` one-off (reproduced in this note's tables); D values are estimates pending the paper's exact table.
