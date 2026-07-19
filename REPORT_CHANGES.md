# Report — Pending Changes (post-v2.0.2)

> Changes to fold into the next report version. **Do not edit `ED_UnifiedFramework_Report.md` in place mid-cycle**; accumulate here, then apply as a batch. Current released version: **v2.0.2** (commit `4c07299`).

Each entry: what changes, where, current text, proposed replacement, why, and status.

---

## C1 — §5 "The debts": sharpen *why* the CMB/cluster debt is hard  **[HOLD — do not apply until verified]**

**Status: PENDING VERIFICATION. Do not apply yet.** This rests on a **first-pass, unverified** derivation chain from the 2026-07-17 session (logged in memory `project_cmb_dust_mimetic_debt` + `ED_Research_Targets` §5b). The report's current §5 language is *already correctly honest* ("live falsification risk, not a bookkeeping debt"), so there is **no error to fix and no urgency** — this only *sharpens* the account, and only if the chain survives an adversarial check. If the chain fails, discard this entry.

**Where:** §5, "The debts," the CMB/clusters bullet (currently ~line 300).

**Current text (correct as-is):**
> Clusters and the CMB are a live falsification risk, not a bookkeeping debt. This is where khronometric/MOND theories characteristically die, and KM-II is explicit that it does *not* discharge them: no regulator member is chosen, no CMB spectrum is computed, no cluster profile is fit… If that dial cannot thread the CMB acoustic peaks and the clusters, the sector fails.

**Proposed sharpening (only if the chain verifies):** add one sentence locating the debt more precisely —
> *The debt is now more sharply located than "the dial is unset": a khronon cosmological sector local in the expansion rate supplies the CMB's clustering condition (`c_s ≈ 0`) but not its dust **abundance** (`∝ a⁻³` at recombination), which is structurally a separate, volume-memory quantity; ED's conserved bandwidth current is natively that dust, but whether a **photon-decoupled** component (the cold dark matter the CMB peaks require, ~5× baryons) exists distinct from baryons — and whether it avoids double-counting against galactic MOND — are the two open knots. The Orthogonality Theorem sequesters the dial, not the dust abundance.*

**Why:** turns the debt from "MOND theories die here / dial unset" into two specific, testable knots. But it imports internal first-pass reasoning into the flagship, so it must clear verification first — otherwise it's exactly the skim-vs-detail / over-banking drift the report has been cleaned of.

**Verification gate (must pass before applying C1):**
1. Confirm the local-`𝒲(0,Θ)` no-go (the `ρ∝H²` vs `H^{3/2}` era argument) with the full KM-II §5–6 equations, not the grep excerpts.
2. Resolve open knot 1 — does ED have a photon-decoupled ~5×-baryon dark component, or is the native dust just baryons? (If just baryons, the whole sharpening collapses and the honest report change is the *opposite*: flag that ED may lack a CMB dark component entirely.)
3. Resolve/scope open knot 2 — the galactic double-counting.

---

## Provenance (2026-07-17)

Source: the CMB/cluster-debt work session (task 1 = the local-dial dust no-go; task 2 = GR-II native-dust; the OneField capstone reconciliation; the adversarial downgrade). Full detail: memory `project_cmb_dust_mimetic_debt`; map entry: `event-density/docs/ED_Research_Targets.md` §5b. **Nothing here is applied to the report; C1 is a candidate gated on verification.**
