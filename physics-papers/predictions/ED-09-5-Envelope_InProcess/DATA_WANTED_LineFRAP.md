# Open data request — high-frame-rate FRAP recovery traces on crowded protein samples

**What this is.** An open call for a specific kind of existing data that would let us run a clean, pre-registered test of one Event Density prediction. If you have data like this (or know who does), we would be grateful to hear from you. Contact: **allen.proxmire@gmail.com** — or open an issue on this repo.

## The one-paragraph ask

We are looking for **raw, un-averaged fluorescence-recovery-after-photobleaching (FRAP) traces** taken at **≥ 250 Hz** (line-scan or point mode) on **crowded / concentrated protein samples** — cytoplasm, osmotically compressed cells, dense in-vitro solutions, condensates. We need the **individual replicate `I(t)` time series** (not the averaged or fit-reduced curve), with the acquisition rate, the bleach geometry (spot/line width), and an estimate of the diffusion coefficient for each condition. Line-scan confocal FRAP (e.g. the 800 Hz "Line-FRAP" method) is exactly the right instrument class.

## Why these exact specs

The prediction is a **slow envelope modulation** riding on the recovery curve, at frequency `f_v ≈ 1.1 · γ_dec`. For crowded samples the recovery rate `γ_dec` is of order 10–100 s⁻¹, which puts the modulation in the **~11–110 Hz** band — so the sampling has to clear ~250 Hz, and the sample has to be crowded enough to raise `γ_dec` into the band (dilute buffer is too fast, fully arrested is too slow; the sweet spot is cytoplasm-like crowding). A viability calc for these conditions is in [`ViabilityCalc_LineFRAP_2026-07-14.md`](ViabilityCalc_LineFRAP_2026-07-14.md).

The signal is small (a few-percent modulation), so we specifically need the **individual replicate traces**: the modulation is triggered by the bleach, so it is phase-locked across replicates and can be pulled out by coherent averaging, while incoherent noise averages away. An averaged or model-fit-reduced curve destroys exactly the information we need.

## What we would do with it, and what we would return

A pre-registered re-analysis: subtract the standard recovery model, take the Lomb–Scargle periodogram of the residual, and test for a peak in 11–110 Hz (analysis pipeline and pass/fail criteria are in [`protocol.md`](protocol.md), Track B). We would share all code and results, credit the data source explicitly, and offer co-authorship on any resulting write-up. A **null result is equally publishable and equally welcome** — it narrows or retires the prediction, which is the point.

## Honest caveats (so any collaboration starts clear-eyed)

- This tests **our model** of the participation channel via a candidate identification (recovery rate ↔ decoherence rate) that is itself a modeling assumption, not an established fact. We say so up front.
- The discriminating quantities are the **envelope's existence at `f_v`, its quality factor `Q ≈ 3.5`, and its cycle count** — *not* a harmonic or triad fingerprint (we checked the canonical model; it does not produce a detectable single-mode 3rd harmonic — see [`PDE_Harmonic_Triad_Finding_2026-07-14.md`](PDE_Harmonic_Triad_Finding_2026-07-14.md)).
- We are an independent research program, not a funded lab; this is a zero-cost re-analysis of data you already have.

## If you are the Line-FRAP group (or similar)

The osmotic-stress `γ_dec` sweep in the Line-FRAP work (Dey, Marciano & Schreiber, *J. Mol. Biol.* 2021) is close to ideal — it walks the recovery rate across the band in one system. Raw per-line `I(t)` traces (all replicates) for the crowded / stressed conditions, with bleach geometry and per-condition `D`, would let us run the test immediately. We would be glad to collaborate.

---

*Part of the ED-09.5 participation-envelope test. See [`README.md`](README.md) and [`protocol.md`](protocol.md) for the full context. This note is an open invitation, not a claim about anyone's data.*
