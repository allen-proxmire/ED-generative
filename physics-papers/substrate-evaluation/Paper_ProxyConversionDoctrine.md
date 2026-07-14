# The Proxy Conversion Doctrine: One Rule Set for Reading Substrate Predictions Through Lab Variables

**Series:** Event Density (ED) Generative Papers — methodological consolidation (cross-arc)
**Author:** Allen Proxmire
**Status:** Publication draft (doctrine/consolidation; no new physics claims). Consolidates the corpus's scattered proxy-to-content conversion factors into one stated doctrine, and pre-registers the live-width content rule that empirical floor/ceiling claims must use.
**Companions:** `Paper_058_ClassC_Plateau` (α), `Paper_056_ClassA_Wall` (αβ), `predictions/ED-09-5-Envelope_InProcess/protocol.md` + `ED_Master_Predictions_List` §4.6 (Q), `Paper_050_PageCurve` / `Paper_V5UnifiedBudget` (f_ent·g_∂, ρ_loc, w_pair), `Paper_QuantumDarwinism_RecordBandwidth` (w_min, w̄, the width content rule).

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **No conversion value is derived here.** Every factor cataloged in §1 keeps its existing tier (mostly inherited / empirically anchored). This paper states the rules governing their *use*, not their values.
2. **No conversion is claimed universal.** The doctrine's central content is the opposite: conversions are architecture- and encoding-specific.
3. **No existing tier changes.** Where the doctrine exposes a gap (notably the encoding-dependence of 058's α, §3.4), the gap is flagged as open, not resolved.
4. **This is methodology with teeth, not physics.** Its falsifiable content (§6) is about the *structure* of conversions (per-architecture constancy), not about any single prediction.

---

## Abstract

ED's caps, walls, and thresholds live in **substrate content variables** (multiplicity, live V5 correlation weight, commitment content). Every experiment measures a **proxy** (mass, code distance, qubit count, frequency, fidelity). The corpus has, case by case, invented a local conversion factor each time the two had to meet: α (redundancy → correlation content, Paper_058), αβ (mass → effective multiplicity, Paper_056), Q (envelope shape → envelope-modulation frequency, ED-09.5 arc / Predictions §4.6), f_ent·g_∂ (budget → boundary entanglement, Paper_050/V5UnifiedBudget), and now w_min/w̄ and a certified-width content rule (Paper_QuantumDarwinism_RecordBandwidth). Three local patches in one week is a pattern, not a coincidence. This paper states the **general doctrine** those patches were each rediscovering: (D1) predictions are sharp in content, banded in any proxy; (D2) conversions are structural per-architecture constants, never universal, never silently transported; (D3) where budgets bind, content means *per-locus live V5 weight*, with the committed/live split applied first; (D4) any empirical floor or ceiling claim must **pre-register its content rule** before citing data — counting qubits is not a content rule. §3 supplies the pre-registered live-width content rule and works it on the three state families now used as budget floors (GHZ, graph states, topological codes), which resolves an active dispute: naive width-counting made certified GHZ records appear to push the Class-C plateau beyond near-term reach; under the content rule, the floor and the plateau live in different α-regimes and the arithmetic must be done per-encoding.

---

## 1. The pattern: five local patches for one missing rule

| Factor | Paper | Converts | Status there |
|---|---|---|---|
| `α` | 058 (Class-C) | code redundancy `R_C` → per-locus correlation content, `B_cross ≈ α·R_C` | 058's own words: "substrate-level mapping coefficient inherited from V5 envelope structure"; the *architecture-specific* reading is `Paper_V5UnifiedBudget` §4's re-characterization, which D2 adopts — a revision of 058, flagged as such (same open item as §3.4, seen from the other end) |
| `α·β` | 056 (Class-A) | molecular mass → effective multiplicity, `M_eff ≈ αβ(m/m_u)` | order-unity, empirically anchored, re-anchorable |
| `Q` | ED-09.5 envelope arc (`protocol.md`; Predictions List §4.6) | oscillator envelope shape → envelope-modulation frequency, `f_v = (Q/π)·γ_dec ≈ 1.1·γ_dec` | canonical-PDE quality factor `Q ≈ 3.5`, assumed-universal, flagged |
| `f_ent·g_∂` | 050 / V5UnifiedBudget | budget `W_max` → boundary entanglement `B_ent,max` | measured 0.88 (straddling-edge tiling) |
| `ρ_loc` | V5UnifiedBudget | per-chain → per-locus budget | resolved: identity (= 1) |
| `w_pair` | 058 / V5UnifiedBudget §4 | per-locus content → correlation count, `N_V5 = B_cross,max/w_pair` | inherited; presumably the same object as w̄/w_min below — identification open |
| `w̄`, `w_min`, content rule | QD/RecordBandwidth | live states → budget floors; widths → content | declared; content rule was *missing* — the tell |

Each was invented locally, correctly, and blind to the others. The doctrine below is what they share.

## 2. The doctrine

**D1 — Sharp in content, banded in proxy.** Substrate predictions are point-thresholds in the content variable. A proxy inherits a *band* whose width is the spread of the conversion factor across the sampled architectures. (This generalizes V5UnifiedBudget's R1 and the Class-A mass band: the 140–250 kDa band *is* the spread of αβ; the code-distance band *is* the spread of α.) Corollary: a band in the proxy is not imprecision in ED; a *point* claimed in a proxy would be the error.

**D2 — Conversions are structural constants of the architecture, not of the substrate.** α, β, Q, w̄ are fixed by *what the platform is* (molecular structure, encoding scheme, envelope geometry), so they are constant within an architecture and freely different across architectures. Two disciplines follow: (i) a conversion measured on one platform is never silently transported to another; (ii) claiming a conversion is universal (as 085 currently does for Q) is a flagged additional assumption, not a default.

**D3 — Where budgets bind, content = per-locus live V5 weight.** The unified budget caps `∫K_V5` at a locus. So the content variable for any budget claim is: *the live (uncommitted) pairwise V5 correlation weight summed over partners at the loaded locus*, after applying the committed/live split (committed records are free — Paper_QuantumDarwinism_RecordBandwidth §2). Content is a property of the sustained state's correlation *pattern*, not of the device's size.

**D4 — Pre-registration.** Any claim that empirical data floors or ceilings a substrate quantity must state, *before* citing the data: (i) the content rule used, (ii) the locus it loads, (iii) the certification discount. Counting qubits is not a content rule. A floor computed without a pre-registered rule is quietly convertible into any conclusion by choosing the conversion afterward — the exact failure D4 exists to block.

## 3. The pre-registered live-width content rule

### 3.1 The rule

For a sustained (uncommitted) state and a locus `u`:

$$
C_{\rm live}(u) \;=\; \sum_{\text{partners } v} \big[\text{certified live pairwise correlation content between } u \text{ and } v\big],
$$

where "certified" means: only the correlation content guaranteed by the state certification actually performed (a fidelity-F GHZ certification guarantees pairwise pointer correlation only to the degree F exceeds the certification threshold; the floor uses the guaranteed lower bound, not the ideal-state value). A budget floor is then `W_max/w_min ≥ max_u C_live(u)` over the certified state.

### 3.2 Worked on the three floor families

- **GHZ-type (broadcast) states, N qubits:** ideal per-locus content ~ `N−1` bits (every pair carries unit pointer MI). Certified content: discounted to the *guaranteed* bound, per D4. Worked for `N=120`, `F=0.56` (barely above the 0.5 GME threshold): aligned-population `p₀₀+p₁₁ ≥ 0.56` with ≤ 0.44 of the state unconstrained junk. Adversarial junk (maximally anti-correlated) → ~0.010 bits/pair → **guaranteed floor ≈ 1 bit per locus (order 10⁰)**. Under an uncorrelated-junk *assumption* (not licensed by the certification) → ~0.24 bits/pair → ≈ 28 bits/locus (order 10¹). The ideal 119 is reachable only as `F → 1`. So the honest certified floor is **order 10⁰–10¹ per locus**, and quoting anything higher requires an undeclared junk model — exactly the failure D4 blocks.
- **Graph states / local certifications (e.g. 414-qubit entanglement characterizations):** per-locus content ~ vertex degree = O(1), regardless of total qubit count. **These floor almost nothing.** A 414-qubit local-entanglement certification is not a 414-wide budget floor; treating it as one is precisely the qubit-counting fallacy D4 blocks.
- **Topological codes (surface code, distance d):** the logical information is *by design* hidden from local probes; pairwise correlation with any single physical qubit is ~0, and per-locus live load is set by local stabilizer participation = O(1) in d. So a deeper code does **not** proportionally load any locus.

### 3.3 What this resolves: the "self-tightening lock" dispute

The dispute (raised adversarially, correctly, against Paper_QuantumDarwinism_RecordBandwidth §6): *if certified GHZ widths floor `W_max`, and the Class-C plateau is commensurate, doesn't every bigger cat state push the predicted plateau beyond the code distances industry will scan this decade — quietly demoting weapon #4 from near-term?*

Under the content rule the arithmetic changes shape: the GHZ floor and the code-distance plateau sit at the ends of **different conversions** — and for topological encodings the difference is *in kind*, not in coefficient (§3.4). The GHZ floor bounds `W_max/w_min` in *content* units; the plateau's *code-distance* onset is `R_C^sat = W_max/α_encoding`. With the honest certified floor at order 10⁰–10¹ per locus (§3.2), the certified frontier (~120 qubits now, ~10³ planned within 2–5 years) probes the broadcast-side wall *directly*. Consequences, stated honestly in both directions:

1. **Repetition/cat-type redundancy hits the wall first, and that wall is the near-term face.** The nearest-term claim of weapon #4 is a ceiling on *broadcast-type* certifiable live width (biggest certifiable cat state), not on surface-code distance. GHZ-fidelity decay vs N is currently fully explained by engineering noise; ED adds a floor-tracked fundamental component to look for.
2. **The topological code-distance leg may not exist at all.** If topological per-locus load is O(1) in `d` (§3.2), then `B_cross(u)` never approaches `B_cross,max` as `d` grows: the linear `α·R_C` form fails for topological encodings and **the plateau in code distance does not occur via this mechanism for topological codes** — not a demotion from near-term, a transfer of the entire code-distance leg to broadcast-type redundancy. Note also `Paper_058` §4.3 itself classifies surface codes as **hybrid Class-B + Class-C**, not pure Class-C, so the flagship topological platform was never a clean carrier of the pure-class plateau. And under the QD paper's own committed/live split, syndrome measurements are P11 commitments whose records are budget-free — further reducing topological live load and strengthening this branch.
3. **The rescue branch, stated:** if 058's per-locus accounting turns out to load content proportional to `R_C` even for topological codes (α_topological non-small, contradicting §3.2's O(1) reading), the code-distance leg survives — and then the lock does tighten and its consequences for weapon #4's near-term status must be recomputed in the addenda. Either way the doctrine makes it a computable question instead of a mood. The deciding item is §3.4.

### 3.4 Open item created (deliberately)

D3 + §3.2 expose that `Paper_058`'s `B_cross(R_C) ≈ α·R_C` needs its encoding-dependence made explicit: the linear form with one α cannot cover both broadcast and topological encodings if their per-locus loadings differ in kind. This is the single highest-value review question for the Class-C arc.

## 4. Retroactive grounding

- **R1** (V5UnifiedBudget §4) = D1 applied to the plateau.
- **The Class-A 140–250 kDa band** (056) = D1 + D2: the band is αβ-spread, the wall is sharp in `M_eff`.
- **The envelope-modulation frequency** (ED-09.5 arc, Predictions §4.6): D2 demands `Q`'s assumed universality be either derived per-architecture or carried as a flagged assumption — it is currently flagged; the doctrine keeps it that way.
- **The 0.88** (A2/UnifiedBudget §6): a conversion that got *measured* — the model for what closing a conversion looks like.
- **The QD floors** (RecordBandwidth §6): now read through §3.1's rule, with the certification discount applied.

## 5. Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| The catalog (§1) | **descriptive** | direct quotation of each paper's own declared factor |
| D1 sharp-in-content/banded-in-proxy | **D (structural)** | single budget + architecture-varying conversion; generalizes R1/056 |
| D2 per-architecture constancy | **P (doctrine)** | declared discipline; falsifiable (§6) |
| D3 per-locus live content | **D (structural)** | 065 partition + QD accounting theorem |
| D4 pre-registration | **methodological rule** | not a physics claim |
| §3.1 content rule | **pre-registered definition** | the deliverable |
| §3.2 per-family loadings | **D (form)** | correlation structure of each family; standard |
| §3.3 lock resolution | **D conditional** | on α_encoding fork; item 3 states the failure branch |
| α_topological value | **OPEN** | gated on 058 accounting (§3.4) |

## 6. Falsification Criteria

- **F-D2:** a conversion factor demonstrated to vary *within* one fixed architecture (same platform, same encoding, different α) — breaks per-architecture constancy, and with it the band-structure account (D1).
- **F-D3:** a budget phenomenon (plateau/ceiling) whose onset tracks device *size* rather than per-locus live content across state families with different correlation patterns — content isn't the binding variable.
- **F-band:** a substrate threshold observed as a sharp *point* across architectures in a proxy variable (sharper than the conversion spread allows) — the band prediction inverts.

## 7. Position Statement

One doctrine replaces five local patches: ED predicts in content, experiments measure proxies, conversions are per-architecture structural constants that must be declared before data is cited, and where budgets bind, content means per-locus live V5 weight with the committed/live split applied first. The pre-registered width rule (§3.1) makes budget floors computable and blocks qubit-counting; its first application (§3.3) converts an adversarial "self-tightening lock" objection into a per-encoding calculation, with the honest branch stated on which weapon #4's code-distance leg demotes. The doctrine adds no physics and derives no values; it makes the corpus's empirical interface uniform, and it creates exactly one new open item — the encoding-dependence of 058's α — on purpose.

---

**Series context.** Methodological consolidation prompted by three same-shaped patches landing in one week (α resurfacing in the plateau work, w_record in the QD scoping, the width content rule in the floors dispute). Companion working notes: `event-density/theory/V5_Characterization/`.
