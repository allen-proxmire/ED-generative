# One Bit Per Planck Cell: Three Independent Counts of the Horizon Tiling, and the Place of the 1/4

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — black-hole / horizon arc (entropy structure)
**Status:** Publication draft (short). A convergence result: three independent substrate counts of the horizon tiling, plus the honest placement of the Bekenstein–Hawking coefficient. Companion to `BH_Thermal2Pi_FromNearHorizonRindler` (the derived 1/4), Paper_043 (area-law form), Paper_025 (holographic count), and `Paper_AreaLawIsTheEdgeCount`. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/black-hole/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This paper does not derive the Bekenstein–Hawking coefficient 1/4.** The 1/4 is derived separately and thermodynamically (`BH_Thermal2Pi_FromNearHorizonRindler`: surface gravity κ = 1/(2r_s) plus the 2π from the substrate's own near-horizon Rindler form, the first law then integrating to S = A/4). This paper concerns the *tiling* — the horizon-area-in-Planck-units, A/ℓ_P², that the thermal 1/4 multiplies — not the coefficient itself.
3. **The result is a convergence, and it reproduces a known structure.** Three independent counts agree on ~1 bit per Planck cell. That is the Planck tiling (Paper_025), a known area-law ingredient. This is consilience — three routes landing on the same number — not a novel prediction, and it is not tiered as one.
4. **The tiling value is O(1), not exactly 1, and its scale is inherited.** The counts land near one bit per Planck cell; the exact number is model- and reach-dependent, and the relevant scale (the near-horizon cross-chain reach ℓ_V5 ~ ℓ_P) is inherited (Paper_090), not derived. The convergence, not an exact coefficient, is the content.
5. **Two of the three counts are models on an assumed geometry, not derivations of it.** The straddling-edge count and the participation (holographic) count assume the emergent horizon geometry; deriving that geometry from the raw graph (curvature emergence) is the open bridge underneath, left open here.

---

## Abstract

The Bekenstein–Hawking entropy S = A/4 factors, in Event Density, into a *tiling* (the horizon area measured in Planck cells, A/ℓ_P²) and a *coefficient* (the 1/4). The coefficient is derived thermodynamically elsewhere (`BH_Thermal2Pi`); this paper concerns the tiling, and reports that **three independent substrate-level counts of "what sits on the horizon" all land on the same value: of order one bit per Planck cell.** (i) The *holographic participation count* (Paper_025) tiles the horizon with N = 4πR²/ℓ_ED² cells — exactly one per Planck area, by construction. (ii) A *frozen-state count* on the dynamical-bandwidth horizon (counting the committed states frozen at the b→0 surface, `BH_EntropyCoefficient_FromEventCounting`) gives ≈ 0.78 per Planck area. (iii) A *straddling-edge count* — the number of distinct chains whose cross-chain (entanglement) edges pierce the surface, at substrate density and near-horizon reach (`evaluation/AreaLaw_Arc/edge_density_coefficient.py`) — gives ≈ 0.88 per Planck area. Three different objects — frozen committed states, entanglement wires crossing the surface, and the holographic participation count — converge on ~1 bit per Planck cell. This confirms the horizon tiling from three angles and locates the Bekenstein–Hawking 1/4 cleanly: it is not in the tiling (which counts near 1), it is the thermal factor the derived thermodynamic route (`BH_Thermal2Pi`) supplies on top. The result is consilience: three independent-flavoured counts agreeing on a known area-law ingredient, with the tiling value O(1) and its scale inherited, and the emergent geometry the two model-counts assume left as the open bridge.

---

## 1. Introduction

In Event Density the black-hole entropy S = A/4 has two parts that are worth separating. The **tiling** is the horizon area measured in the substrate's own units, A/ℓ_P² — how many Planck cells the horizon carries. The **coefficient** is the 1/4 that multiplies it. Recent work derived the coefficient: with the surface gravity κ = 1/(2r_s) read off the substrate's bandwidth profile and the 2π forced by that profile's near-horizon Rindler form, the first law integrates to S = A/4 (`BH_Thermal2Pi_FromNearHorizonRindler`). That settles the 1/4 thermodynamically.

This paper concerns the other part — the tiling — and asks how firmly the substrate pins it. The answer is a convergence: three independent ways of counting "what sits on the horizon" all give the same tiling value, of order one bit per Planck cell. Independent agreement of unlike counts is exactly the kind of internal coherence that makes a substrate reading trustworthy, and it locates the 1/4 unambiguously as the thermal factor rather than anything hidden in the count.

## 2. The Three Counts

**(i) The holographic participation count (Paper_025).** The horizon carries a participation-count bound N = 4πR²/ℓ_ED² — the surface area in units of the substrate cell. This is exactly one participation per Planck area, by construction of the bound. It is the reference the other two are measured against.

**(ii) The frozen-state count (`BH_EntropyCoefficient_FromEventCounting`).** On the dynamical-bandwidth horizon (the frozen b→0 decoupling surface, GR-III / Paper_039), count the independent committed states frozen at the surface, divided by the horizon area in Planck-proxy units. Measured: ≈ 0.78 per Planck area — a full-surface tiling at ~1 committed state per cell.

**(iii) The straddling-edge count (`edge_density_coefficient.py`).** Entanglement crossing the horizon is carried by the cross-chain (V5) edges that straddle it (Paper_039 §3.5). At the substrate's own density (one chain-locus per Planck cell, P08) and the near-horizon cross-chain reach (ℓ_V5 ~ ℓ_P, Paper_039), count the distinct chains with a straddling edge, per unit horizon area. Measured: ≈ 0.88 per Planck area.

## 2.5 Load-Bearing Step Audit

| Step | Status | Source |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Holographic count N = 4πR²/ℓ_P² (1 per Planck area) | I — form-forced | Paper_025 |
| Frozen-state count ≈ 0.78 per Planck area | **measured** | `BH_EntropyCoefficient_FromEventCounting` |
| Straddling-edge (chain) count ≈ 0.88 per Planck area | **measured** | `edge_density_coefficient.py` |
| Three counts converge on ~1 bit per Planck cell | **measured (convergence)** | this paper |
| The 1/4 coefficient (multiplies the tiling) | **derived — separately** | `BH_Thermal2Pi` (thermodynamic) |
| Emergent horizon geometry derived from the graph | **OPEN** | curvature emergence, not attempted here |

## 3. Result

The three counts, side by side, per Planck area of horizon:

| Count | What it counts | Value |
|---|---|---|
| Holographic (Paper_025) | participation cells tiling the surface | 1 (by construction) |
| Frozen states | committed states frozen at the b→0 horizon | ≈ 0.78 |
| Straddling edges | distinct chains whose entanglement edges pierce the surface | ≈ 0.88 |

Three unlike objects — participation cells, frozen committed states, and entanglement wires crossing the surface — agree on **~1 bit per Planck cell**. The horizon tiles at one substrate degree of freedom per Planck area, confirmed from three independent directions.

## 4. What This Shows, and Where the 1/4 Sits

**The tiling is robust.** That a holographic count, a dynamical frozen-state count, and an entanglement-edge count all land near one-per-Planck-cell is strong internal coherence: the substrate's several notions of "horizon degree of freedom" agree on the density. This is the A/ℓ_P² of the area law, confirmed three ways.

**The 1/4 is the thermal factor, and it is elsewhere.** Because all three counts land near 1 — not near 1/4 — the Bekenstein–Hawking quarter is *not* hiding in the count. It is supplied by the thermodynamic route (`BH_Thermal2Pi`): the derived κ and 2π, integrated through the first law, give S = A/4 with the tiling as the A. So the full picture is clean and non-redundant: the *tiling* (this paper, three counts) supplies the A/ℓ_P²; the *thermal factor* (`BH_Thermal2Pi`) supplies the 1/4. Neither double-counts the other, and the earlier "coefficient inherited" reading (Paper_043) is superseded — the coefficient is derived, and it lives in the thermal route, not the tiling.

## 5. Honest Scope

The tiling value is O(1), not exactly 1; the exact number is model- and reach-dependent, and the straddling-edge count in particular scales with the cross-chain reach, so its ~0.88 is the value *at* the inherited near-horizon reach ℓ_V5 ~ ℓ_P, not a scale-free constant. Two of the three counts (holographic, straddling-edge) assume the emergent horizon geometry rather than deriving it; that derivation (curvature emergence) is the open bridge under this and every geometric result in the corpus. And the tiling is a known area-law ingredient, so its confirmation is consilience — structural coherence across three independent-flavoured counts — not a novel prediction. The content is the convergence and the clean separation it forces (tiling near 1, coefficient in the thermal factor), not a new number.

## 6. Falsification Criteria

- **F1:** If a substrate count of independent horizon degrees of freedom robustly gave a value far from ~1 per Planck cell (e.g. ~1/4), the three-count convergence would break and the tiling reading would be wrong.
- **F2:** If the thermodynamic 1/4 (`BH_Thermal2Pi`) and the tiling were shown to double-count — i.e. the count already carried a factor the thermal route re-applies — the clean tiling-times-thermal separation would fail.
- **F3:** If, once the emergent geometry is derived (curvature emergence closed), the horizon degree-of-freedom density did not come out ~1 per Planck cell, the tiling would not be the substrate-native count claimed here.

## 7. Position Statement

In Event Density, the horizon tiles at **one substrate degree of freedom per Planck cell**, confirmed by three independent counts — the holographic participation count (1 by construction), a dynamical frozen-state count (≈ 0.78), and an entanglement straddling-edge count (≈ 0.88). This is the A/ℓ_P² of the Bekenstein–Hawking area law, established three ways. It also locates the coefficient cleanly: the 1/4 is not in the tiling (which counts near 1) but is the thermal factor supplied by the derived thermodynamic route (`BH_Thermal2Pi`, κ × 2π × first law). The two combine, without redundancy, to S = A/4. The result is consilience — three unlike counts agreeing on a known tiling — with the value O(1), its scale inherited, and the emergent geometry the model-counts assume left as the open bridge; it is not offered as a novel prediction or as a second derivation of the 1/4.
