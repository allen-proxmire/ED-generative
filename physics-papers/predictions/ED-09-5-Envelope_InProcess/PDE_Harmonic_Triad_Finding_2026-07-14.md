# ED-09.5 harmonic/triad legs (F4/F5): the canonical PDE is quadratic-dominated — the pre-registered "3–6% third harmonic" and "phase-locked triad" are not what it produces

**2026-07-14.** Crank-rail ON: this is a negative about ED's own prediction, held to the positive bar (fresh simulation + analytic cross-check + regime sweep + reconciliation against the corpus source). Path 2 of the envelope program (the no-data leg). Script: [`scripts/ed_pde_harmonic_triad.py`](scripts/ed_pde_harmonic_triad.py). Resolves the "inconclusive" harmonic addendum of [`ED_PDE_Drive_Finding_2026-07-10.md`](ED_PDE_Drive_Finding_2026-07-10.md).

## What was run

The full 1-D canonical PDE (`Architectural_Canon.md` P1–P5 + the P7 gradient term `M'(ρ)|∇ρ|²`, which is nonzero only with spatial structure — the uniform-mode frequency run could not test harmonics). Single k=1 spatial mode excited; **modal decomposition** `a_k(t) = (2/N)Σρcos(kx)` — location-independent, unlike the earlier point-probe (which sampled a node of both k=1 and k=3, an artifact). Measured the temporal 3rd-harmonic ratio `|a₁@3f_v|/|a₁@f_v|` (the FRAP/optomechanics observable F4), the spatial k=3/k=1 ratio, and the triad phase residual (F5), swept over amplitude, damping ζ, and gradient coupling M0.

## Result

| observable | canonical PDE | pre-registered | verdict |
|---|---|---|---|
| **F4 temporal 3rd harmonic** `|a₁@3f|/|a₁@f|` | **0.03–0.06%** (canon ζ, amp 0.4–0.6) | 3–6% | **~50–100× below** |
| analytic Duffing ceiling `A²/64` | 0.06% (A=0.2) → 1.0% (A=0.8) | 3–6% | reaches 3–6% only at **A≳1.4 (unphysical**, ρ<0) |
| spatial k=3/k=1 at peak fundamental | **~0%** for M0 ∈ {0.02, 0.1, 0.3} | 3–6% | not reproduced |
| temporal 2nd harmonic `|a₁@2f|/|a₁@f|` | 0.36–0.38% | (—) | the *leading* harmonic, but modest + amplitude-set |
| F5 triad phase residual `|φ₃−3φ₁|` | 2–3 rad (unlocked) | locked (C≈0.03) | not locked |

Two independent methods agree the third harmonic is tiny: the simulation (~0.06%) and the analytic weakly-nonlinear ceiling (`a₃/a₁ = |β|A²/32ω₀² = A²/64` for the penalty `P_SY2 = d − d³/2 + …`), which caps it at ~1% even at the edge of the physical amplitude range. The apparent "2%" in the 2026-07-10 addendum and the old script were **denominator-vanishing artifacts** (k3/k1 measured after the fundamental had decayed); at peak fundamental the ratio is ~0.

## Reconciliation with the corpus (read-first, per CLAUDE.md) — this is NOT a falsification of ED

The Canon P7 one-liner reads: *"generates higher-harmonic content, especially k=3 from k=1 … harmonic generation is 3–6% … triad coupling ~0.03 … no mode locking."* Its cited source, **ED-Phys-16 (Coupled Oscillators)**, run on the *same* canonical PDE, actually found:

1. **"The nonlinearity is primarily quadratic"** — single-mode excitation generates the **2nd harmonic** (k=2, 2f_v), *not* a strong 3rd. (My run agrees: 2nd ≈ 0.38%, 3rd ≈ 0.06%.)
2. The strong "triad" coupling (combination-mode amplitudes 0.3–0.8, C≈0.03) requires **multiple modes excited simultaneously** (`k₁+k₂=k₃`, e.g. 8+24=32) — it is quadratic sum/difference generation, **not** single-mode k=3-from-k=1.
3. **"No phase locking. Phase differences drift freely (~2 rad decorrelation)."** (My run agrees: 2–3 rad.)

So the Canon's P7 skim compressed ED-Phys-16's detailed result — *quadratic, 2nd-harmonic-dominant, multi-mode combination, no phase locking* — into a tidy "k=3 from k=1, 3–6%, triad" line that the source does not support. This is a **skim-vs-detail drift in the Canon**, and the ED-09.5 protocol inherited the skim as pre-registered F4/F5. The physics (both sources) is consistent; the one-line summary was over-tidy.

## Consequence for the ED-09.5 test (the actionable part)

- **Retire F4 as "3–6% third harmonic (single-mode, temporal)."** The canonical PDE gives ≲0.1% for a single-bleach (single-mode) excitation. A FRAP/optomechanics experiment that excites essentially one participation mode should **not** expect a 3rd harmonic at 3–6%, and — critically — **a null 3rd harmonic must not be scored as falsifying ED** (the PDE predicts ~null). The 2026-07-10 protocol F4 falsifier is corrected here.
- **The leading single-mode harmonic is the 2nd (at 2f_v)**, but it is amplitude-set (~0.4% at these amplitudes), not a clean invariant — a soft secondary check, not a pre-registered number.
- **Retire F5 as a "phase-locked triad."** ED-Phys-16 itself found no phase locking. The C≈0.03 coupling is a *multi-mode* combination coefficient; it would only appear if the experiment deliberately excites two participation modes (`k₁+k₂`), which the standard single-bleach protocol does not.
- **The discriminating power of ED-09.5 rests on F0 + F2 + F3**: the envelope's existence at `f_v ≈ 1.1·γ_dec` (F0) and its `Q ≈ 3.5` / `N_osc` (F2/F3). The frequency correction (2026-07-10) and this harmonic correction together leave a **cleaner, better-scoped test**: one envelope line, its Q, and (soft) a 2nd harmonic — not a 3rd-harmonic/triad fingerprint that the PDE does not generate for a single-mode drive.

## Honest scope / residual

- Unchanged: the `f_v ≈ 1.1·γ_dec` frequency (F0) and `Q≈3.5` (F2/F3) predictions stand; this touches only the harmonic legs.
- The multi-mode combination coupling (ED-Phys-16's real triad result) *is* a genuine ED signature — but it needs a **two-mode excitation** protocol to test, which is a different (harder) experiment than single-bleach FRAP. Flagged as a possible future leg, not a current one.
- Not chased: whether a bespoke two-mode participation excitation is realizable in FRAP or optomechanics. Out of scope for the single-bleach tracks.

**Net:** Path 2 delivered a correction, not a confirmation: the harmonic/triad legs as pre-registered (3–6% single-mode 3rd harmonic, phase-locked triad) are not what the canonical PDE produces; they were a Canon-P7 over-simplification of ED-Phys-16. F4/F5 are corrected/retired, the test is re-scoped onto F0/F2/F3 (which stand), and a null harmonic is no longer a false falsifier. Any future dataset (Line-FRAP or optomechanics) is now scored on the legs that actually discriminate.
