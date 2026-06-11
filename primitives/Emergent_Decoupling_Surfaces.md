# Emergent Decoupling Surfaces — Foundations Note

**Documentation/foundations note. Not a corpus edit, not a new primitive, not a simulator proposal.**
Companion to `P11_commitment.md` (content decomposition) and `Contrast_Minimality.md`.
**Question:** can ED's decoupling surfaces (determinability boundaries) arise *endogenously* from the substrate dynamics, or must they be *installed* (as by `boundary.py`'s decoupled-edge flag)?
**Source basis:** P02, P04, P05, P11, P13; the determinability-boundary results (`evaluation/Bits`, `evaluation/Bits/docs/A1_ChannelCapacity_Results.md`); the B4 arc (`evaluation/B4_Arc`); the certified simulator (`evaluation/Bits/simulator/{graph,update,sigma,strata,boundary}.py`); the Facts paper's horizon/determinability discussion.

---

## 1. What a decoupling surface is

A **decoupling surface (B6)** is an edge across which reciprocal participation fails. Strata are the connected components of the *reciprocal* subgraph; the surfaces are the edges separating them; Δ (within − across mutual information) is measured across such a surface. Operationally, in the certified simulator a surface is the `decoupled = True` flag on an edge: `admissible_neighbors` excludes decoupled edges, so a front cannot cross, and the two sides become separate strata. A genuine surface is therefore (i) a **structural**, edge-level property, (ii) **reciprocal** (non-reachable in both directions = "true boundary"), and (iii) **persistent**.

## 2. The two mechanisms

- **(A) Installed.** The `decoupled` flag is set at build time (e.g. the decoupled A[-1]→B[0] bridge in `size_sweep.build_substrate`). The surface is an **input** fixed before any dynamics run.
- **(B) Emergent.** The flag — or, equivalently, the loss of reciprocal reachability — would arise *from the dynamics themselves*, with no build-time installation.

## 3. The decisive structural fact

The certified update loop evolves **node state** (ρ, orientation, active) on a **fixed graph**. It never modifies edge structure: `apply_update`/`step` write only `NodeState`; `graph.set_decoupled` is *defined but never called* by any dynamics; bandwidth is *read* (the tie-break key `graph.bw`) but never *written*; no edge is added or removed. The graph — its adjacency (P02), its bandwidths (P04), its decoupling flags — is therefore a **build-time constant**, not an output of the dynamics. A decoupling surface is an edge-level property of that constant; nothing in the certified rule set can create or destroy one. The "emergent mode" referenced in `strata.assign_stratum_ids` ("re-call after any decoupling-flag change, emergent mode, Build Step 6+") is precisely a *re-stratification hook* anticipating such a change — but **no certified rule ever drives the change**. This is the same lesson B4 reached for orientation: irreversibility (P11) freezes committed *state*, it does not author *structure*.

## 4. The four candidate emergent routes

| Route | Mechanism | Under certified rules? | Why |
|---|---|---|---|
| **Bandwidth collapse** | P04 `b_uv → 0` ⇒ no channel (`P_K = √b·e^{iπ} → 0`) ⇒ effective cut | **No** | bandwidth is static — read for tie-break, never evolved; needs a P04-*dynamics* rule |
| **Participation starvation** | front extinction (Σ ≤ threshold) leaves a region with no active front | **No (wrong object)** | yields *quiescence*, not a *cut*: edges stay intact and admissible, a later front can re-cross. Absence-of-activity ≠ non-reciprocity |
| **Irreversible commitment cascade** | high-ρ wall repels fronts (Σ strain term penalizes dense targets), frozen by P11 | **No (only a soft barrier)** | a *state-level potential barrier*, not a structural edge cut; and the Σ-rule *resists* runaway ρ (coherence pulls toward ρ\*; strain penalizes excess), so a self-reinforcing wall is not an attractor; gives high resistance, not the exactly-zero reciprocal capacity A1 measured |
| **Orientation-induced anisotropy** | B4's weak channel: winding-suppressed coherence-bandwidth `cos²(πw/N) → 0` ⇒ edge cut | **No** | needs *both* bandwidth↔orientation coupling (Σ is orientation-blind — not certified) *and* bandwidth dynamics; strictly more than route 1 |

Only routes that touch **edge structure** (bandwidth collapse, orientation-driven b→0) can produce a true B6 cut, and both require a rule that feeds node state back into the graph — absent from the certified update. The routes that *are* available under certified rules (extinction, ρ-walls) produce quiescence or a *soft* state-level barrier, not a structural, reciprocal, persistent surface; the ρ-wall is moreover actively resisted by the Σ design.

## 5. Installed vs emergent — summary

| | Installed (certified) | Emergent (sought) |
|---|---|---|
| Locus of change | edge `decoupled` flag, at build | edge reciprocity, from dynamics |
| Writer | `set_decoupled` at setup | would need a state→edge-structure rule |
| In the update loop? | n/a (input) | **never** — loop writes node state only |
| Result | structural cut → excluded from admissibility → **capacity = 0** (A1) | not realized |
| Closest certified analogue | — | soft ρ-wall (state barrier), or quiescence — neither a B6 surface |

## 6. Verdict

**Emergent only under extended rules.** Under the certified dynamics, emergent decoupling is **impossible**, for a structural reason: the dynamics act on node state over a static graph, and a decoupling surface is an edge-level property of that graph. The only routes that yield a genuine structural cut (bandwidth collapse; orientation-driven b→0) require a rule coupling node state back to edge structure — minimally, a **dynamical-bandwidth rule with a collapse channel** (P04 evolving, `b_uv → 0` pruning the edge from admissibility). That is a *rule extension*, **not a new primitive**: P04 (bandwidth) already exists; what is missing is a bandwidth-*dynamics* law. The `set_decoupled` hook and the `strata` "emergent mode" comment anticipate exactly this insertion point, but no certified rule occupies it.

## 7. Implications for ED-10 horizons

Physical horizons (cosmic, black-hole) are by nature **emergent** determinability surfaces — they form from matter/dynamics, not from a hand-set flag. The verdict therefore locates precisely what ED-as-certified lacks for horizons: not a new primitive, but a **state→edge-structure coupling** — a bandwidth-collapse / participation-pruning *dynamics* on the existing P04. This is consistent with the Bits-program reading that the installed boundary is a *toy* surface and that an emergent boundary is "the only path toward anything physical." Two honest caveats, named not resolved: (a) whether such a bandwidth-collapse law is ED-admissible — consistent with the other primitives and crank-safe — is itself open; (b) an emergent ρ-wall is *soft* (resistance, not exact-zero capacity), so it would **not** reproduce A1's exactly-zero severance — that signature is specific to a *structural* cut, which still requires the extended rule. Naming the missing law is the contribution here; endorsing or constructing it is not.

---

*Foundations note only. Verdict: decoupling surfaces are emergent only under an extended state→edge-structure rule (minimally, dynamical bandwidth collapse on P04); under the certified dynamics they must be installed. No corpus or ontology changes; no new primitives.*
