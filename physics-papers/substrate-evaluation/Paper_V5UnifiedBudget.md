# The V5 Correlation Budget is One Envelope: Unifying the Monogamy, Page-Curve, and Class-C Plateau Bounds

**Series:** Event Density (ED) Generative Papers — cross-arc consolidation (V5 kernel; entanglement / black-hole / q-compute)
**Author:** Allen Proxmire
**Status:** Publication draft (conditional structural derivation within the 13-Primitive Generative System). Consolidation of three separately-postulated V5 budgets into projections of one bounded envelope; two forced scale-independent relations; one O(1) factor pinned to the area law.
**Companions:** `Paper_090_V5Kernel` (the kernel), `Paper_065_Monogamy` (E-4), `Paper_050_PageCurve`, `Paper_058_ClassC_Plateau`, `Paper_053_Mcap`, `Paper_HorizonTilingThreeCounts` (the straddling-edge count).

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 primitives are not derived** (Paper_087); V5 exists as a P10 kernel-rule-type posit (Paper_090), not forced.
2. **The absolute V5 budget scale `W_max` (equivalently `Γ_plateau`, `t_Page`, the CKW coefficient) is not derived.** It rides on the V5 envelope scale (`τ_V5`, `ℓ_V5`), a substrate constant inherited like `ℓ_P`. This paper pins *relations among* the budgets, not the scale.
3. **No new falsifiable numerical prediction of `Γ_plateau` itself.** The forced content is (i) the plateau onset is universal in the substrate complexity variable, and (ii) the three arena budgets stand in fixed ratios.
4. **The O(1) projection factors depend on the (inherited) envelope shape**, except the entanglement/boundary factor, which is pinned to the area-law tiling (§6). The two others reduce to a structural identity (`ρ_loc = 1`, §5).
5. **No claim that the three arenas share a single *numerical* budget across regimes** without the (inherited, common) DCGT renormalization of `ℓ_V5`; the claim is that the *ratios* are fixed because the renormalization is common and cancels.

---

## Abstract

Three ED results each postulate a *finite V5 cross-chain budget* as an independent commitment: monogamy of entanglement caps a chain's total cross-chain correlation weight `W_V5` (Paper_065, P-V5-Budget); the black-hole Page curve caps the cross-boundary entanglement-amplitude `B_ent,max` (Paper_050, P-V5-EntBudget); and the Class-C quantum-error-correction plateau caps a locus's cross-chain correlation content `B_cross,max` (Paper_058, P-Corr-Budget). We show these are **not three commitments but one**: each is a projection of the single bounded V5 envelope `W_max = ∫F_V5`, whose finiteness is form-forced by Paper_090's boundedness + P04 additivity. Two relations follow that are **independent of the inherited scale**, hence forced: **(R1)** the Class-C plateau (and the Class-A wall) is a *point* in the substrate complexity variable and a *band* in any lab proxy (mass, code distance), because the proxy-to-content conversion varies; **(R2)** the three budgets stand in fixed ratios `W_V5 : B_cross,max : B_ent,max = 1 : 1 : 0.88`, the first equality a structural identity (`ρ_loc = 1`, one budget spent two ways) and the `0.88` the entanglement/boundary projection measured as the horizon straddling-edge count (`Paper_HorizonTilingThreeCounts`), i.e. the Bekenstein–Hawking tiling. The consequence for the Class-C plateau (a report §14 weapon) is that its height is no longer a free inherited number: it *equals* the monogamy bound and is `1/0.88×` the Page-curve budget. The absolute scale remains inherited; the relations are the failable content.

---

## 1. Three budgets, one kernel

`Paper_090` fixes the V5 kernel as `K_V5(A,B) = θ(t_A−t_B)·F_V5(σ/ℓ_V5², Δt/τ_V5)`, with `F_V5` **bounded and finite-width** (§4.1: no δ-function limit, no infinite-width limit) and V5 producing **bounded cross-chain correlations** (§4.2). Boundedness + finite width means the total integrated envelope weight is finite:

$$
W_{\max} \;\equiv\; \int F_{V5}\,\mathrm{d}\mu \;<\;\infty
\qquad(\text{form-forced: Paper\_090 §4.1–4.2} + \text{P04 additivity}).
$$

`W_max` is the total V5 cross-chain correlation weight the substrate can carry, per chain-locus. Its existence and finiteness are forced; its value rides on the inherited envelope scale (`τ_V5`, `ℓ_V5`).

Three downstream papers each posit a finite V5 budget:

| Arena | Postulated budget | Definition |
|---|---|---|
| Monogamy (065) | `W_V5 ≤ W_max` | `∫K_V5(r,r') dr'` summed over a chain's partner-chains |
| Class-C plateau (058) | `B_cross(u) ≤ B_cross,max` | V5 cross-chain correlation content at a locus `u` |
| Page curve (050) | `B_ent(t) ≤ B_ent,max` | V5 entanglement-amplitude content across a boundary |

Paper_050 states its budget is *"structurally related to but distinct from"* Paper_058's. We make that precise: same parent `W_max`, different projection.

## 2. The projections

$$
W_{V5}=W_{\max},\qquad
B_{\mathrm{cross,max}}=\rho_{\rm loc}\,W_{\max},\qquad
B_{\mathrm{ent,max}}=f_{\rm ent}\,g_\partial\,W_{\max},
$$

where `ρ_loc` is the per-locus vs per-chain factor (§5), `f_ent ∈ (0,1]` the fraction of the envelope weight carrying *entanglement* amplitude vs general correlation, and `g_∂` the boundary geometry. §§5–6 evaluate the two non-trivial factors.

## 3. Consolidation

The three commitments — **P-V5-Budget** (065), **P-Corr-Budget** (058), **P-V5-EntBudget** (050) — collapse to **one** substrate commitment (a finite V5 envelope, §1) plus geometric/content projections. This is the "one Λ, two descriptions" move (KM-II §7) applied to the V5 budget: three inherited postulates → one inherited scale + O(1) projections. It removes two independent inherited numbers from the corpus by fixing their ratios (§§5–6).

## 4. Relation R1 — the plateau is universal in complexity (a band in the proxy)

Class-C is `N_V5`-limited: `M_cap = min{N_bw, N_V5, N_commit}` (Paper_053), and Class-C is the branch where the V5-correlation count `N_V5 = B_cross,max/w_pair` saturates first. So **the plateau onset is at fixed correlation-content `B_cross,max` for every architecture** — Paper_058 §5.2's cross-platform-consistency claim, now a consequence of the single envelope.

In any lab proxy the onset is a **band**: for redundancy/code distance `R_C`, Paper_058 has `B_cross(R_C) ≈ α R_C` with `α` the architecture-specific redundancy→coverage coefficient, so `R_C^sat = B_cross,max/α` spreads with `α`. This is **the same figure as the Class-A wall**: sharp in `M_eff` (multiplicity = internal complexity), a band in mass because complexity-per-kDa varies (`m_wall = M_cap·m_u/(αβ)`, Paper_056). In both, the sharp variable is *internal complexity*; mass and code-distance are proxies; **the band is the proxy-shadow of a sharp complexity threshold**. Forced, given the single envelope + architecture-varying proxy conversion. *(Caveat, added on review: R1's band presumes every architecture has a finite, nonzero effective `α` — i.e. eventually saturates. Encodings whose per-locus load stays O(1) in the redundancy parameter (topological codes, plausibly) drop out of the band rather than sitting in it; see `Paper_ProxyConversionDoctrine` §3.2–3.4.)*

## 5. Relation R2, part 1 — `ρ_loc = 1` (monogamy budget = plateau budget)

`W_V5` (065) is `∫K_V5` over a chain's partner-chains; `B_cross,max` (058) is the cross-chain correlation content *at a locus*. Both are **the total V5 cross-chain correlation weight a chain-locus can carry to other chains** = `∫K_V5 = W_max`. At the substrate grain (one chain-locus per Planck cell, P08) they are the *same integral*. The arenas differ only in what the budget is *spent on* — entanglement partners (monogamy) vs redundant-encoding channels (Class-C) — not in its size. Hence

$$
\boxed{\;\rho_{\rm loc}=1,\qquad W_{V5}=B_{\mathrm{cross,max}}=W_{\max}.\;}
$$

This is a structural identity, not a fit: **the monogamy bound and the Class-C plateau budget are the same `W_max`.** (Across arenas at different coarse-grained scales the literal equality carries the DCGT renormalization of `ℓ_V5`; being common to all V5 observables, it cancels in the ratio.)

## 6. Relation R2, part 2 — the entanglement factor is the area-law tiling (`f_ent·g_∂ ≈ 0.88`)

`B_ent,max` is the V5 entanglement-amplitude carried across a boundary — the straddling cross-chain edges of `Paper_039` §3.5. `Paper_HorizonTilingThreeCounts` measures exactly this: the count of entanglement-carrying V5 edges crossing a boundary at `ℓ_V5 ~ ℓ_P` is **≈ 0.88 per Planck cell** (`evaluation/AreaLaw_Arc/edge_density_coefficient.py`), converging with the frozen-state (0.78) and holographic (1) counts on ~1 bit per Planck cell. That number *is* the entanglement/boundary projection factor:

$$
f_{\rm ent}\,g_\partial \;\approx\; 0.88 \quad(\text{substrate units, }\ell_{V5}\sim\ell_P),
$$

so `B_ent,max` is anchored to the Bekenstein–Hawking tiling. (This is a substrate-scale value; the plateau's coarse-grained `ℓ_V5` renormalization is the common, inherited factor that cancels in ratios.)

**R2, closed:**
$$
\boxed{\;W_{V5} : B_{\mathrm{cross,max}} : B_{\mathrm{ent,max}} \;=\; 1 : 1 : 0.88.\;}
$$

## 7. Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| Finite `W_max = ∫F_V5` exists | **form-forced** | Paper_090 §4.1–4.2 + P04 |
| Three arena budgets = projections of `W_max` | **structural** | §2; Paper_050 "related but distinct" |
| `ρ_loc = 1` (monogamy = plateau budget) | **D-structural (identity)** | §5; same `∫K_V5`, one budget spent two ways, at P08 grain |
| `f_ent·g_∂ ≈ 0.88` (entanglement = area-law tiling) | **measured** | §6; `edge_density_coefficient.py`, Paper_HorizonTilingThreeCounts |
| R1 plateau universal in complexity (band in proxy) | **D conditional** | §4; single envelope + varying proxy conversion; = Paper_058 §5.2 re-grounded |
| R2 ratios `1:1:0.88` | **D conditional** (identity + measured) | §§5–6 |
| Absolute `W_max`, `Γ_plateau`, `t_Page` | **I** | inherited V5 substrate constant (envelope scale) |
| Cross-arena DCGT renormalization of `ℓ_V5` | **I, common** | cancels in ratios |

## 8. Falsification Criteria

- **F-R2 (strong):** infer the V5 budget in two of {monogamy, Page curve, Class-C plateau} and find the ratio inconsistent with `1:1:0.88` (after the common `ℓ_V5` renormalization) — falsifies the single-envelope consolidation (§3), i.e. that one V5 kernel underlies all three.
- **F-R1:** two pure-Class-C architectures plateau at substantially different correlation-content after their redundancy→coverage conversion (also Paper_058 §6.3).
- **F-form:** error suppression continues to zero at arbitrarily high redundancy, no plateau (Paper_058 §6.1) — no finite envelope.
- **F-ρ:** a demonstration that the monogamy budget and the Class-C correlation budget are genuinely distinct quantities (not one `∫K_V5`) — falsifies `ρ_loc = 1` (§5).

## 9. Position Statement

The finite V5 budgets of monogamy (065), the Page curve (050), and the Class-C plateau (058) are **one bounded V5 envelope seen three ways.** Two forced, scale-independent relations follow: the plateau/wall onset is a point in internal complexity and a band in the lab proxy (R1); and the three budgets stand in the fixed ratios `1 : 1 : 0.88`, the first a structural identity (`ρ_loc = 1`) and the second the area-law straddling-edge tiling (R2). For the Class-C plateau this means its height is not a free inherited number: it **equals the monogamy bound** and is `1/0.88×` the Page-curve budget. The absolute scale stays inherited (a V5 substrate constant); the relations are the falsifiable content, and they interlock three sectors — entanglement, black-hole thermodynamics, and quantum error correction — through one kernel.

**What this paper claims:** one envelope, three projections; R1; R2 with `ρ_loc = 1` and `f_ent·g_∂ ≈ 0.88`. **What it does not:** the absolute budget scale, or the plateau height as a standalone number.

---

**Series context.** Cross-arc consolidation. Sharpens `Paper_058` (Class-C plateau, report §14 weapon #4) by tying it to `Paper_065` (monogamy) and `Paper_050` (Page curve) through `Paper_090`'s single bounded envelope. Working derivation: `event-density/theory/V5_Characterization/V5_UnifiedBudget_Consolidation.md`.
