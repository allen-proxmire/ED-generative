# The Parity Wall: Why Event Density Gives a Matter/Antimatter Reference Natively but Not the Weak Force's Chirality

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (matter-sector chirality verdict)
**Status:** Publication draft (structural, a wall result). The honest verdict of the emergent-spinor chirality attack: parity violation is found absent at every level checked (default vector for the minimal construction), while a matter/antimatter reference is natively selected. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative) — substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This is a negative result on parity violation, reported as such.** ED's emergent fermion is **vector by default** (for the minimal construction); the weak force's chirality is **inherited, not derived**. That is the finding — a wall — not a failure to be papered over. The one *positive* is a matter/antimatter *reference* (C), whose selection is ED-native.
2. **It does not prove ED is vector forever.** The handed channel-topology that could earn chirality is *undefined-and-unbuilt* at the canonical primitive level, not forbidden. Building the full channel-topology→gauge program could in principle come out handed; the verdict is default-vector conditional on the minimal primitives and the current unbuilt state.
3. **The native positive is the *selection*, not the identification or the value.** The first-arrival mechanism natively selects a matter/antimatter *reference* (C); that this reference *is* charge conjugation / the baryon asymmetry is an account-tier identification, and the baryogenesis *magnitude* is inherited.
4. **The homochirality null is a specific probe, not a universal impossibility.** The `κ_h ≈ 0` result is a measured null on the V5 all-pairs coupling; it refutes that route, it does not prove parity-breaking is impossible by every conceivable mechanism.
5. **This is analytic / probe-level.** The gauge-chiral sector is not in the certified Σ-simulator (it is Σ-blind, the same obstruction as the substrate-Higgs and the anomaly); the discriminator is an analytic construction on the directed participation graph, with probe checks.
6. **It corrects an earlier over-read.** A prior "first-arrival imprints both C and P" claim over-read its P-half; this paper retains the C-half and retires the P-half, with the reason.
7. **No new primitive is introduced.**

---

## Abstract

Does ED's emergent fermion natively produce the weak force's parity violation? The chirality attack reduces the question to a single computed quantity and answers it: **no** — for the minimal construction the fermion is vector by default, and parity violation is inherited. Building the minimal emergent Weyl mode with a helicity along the arrow and transporting it one commitment-step, the chiral discriminator `advance(L) − advance(R)` evaluates in closed form to `−2 atan2(sin(θ/2) n_z, cos(θ/2))`, which is **nonzero iff `n_z ≠ 0`** — the component of the frame-rotation *about the arrow*, i.e. a screw pitch. A vector fermion requires no screw; a chiral one requires the transport to screw the spin-frame about the arrow it advances along. The canonical primitives supply no such screw. This is **one structural absence — ED has no handed spatial structure — checked at the three levels where built-in handedness could enter, plus one distinct probe of the spontaneous route** (these are not four independent proofs; the first three share the one root cause): **(1) wiring** — canonical P07 channels are distinguishable labels with no geometry or topology, so there is no helix to be handed; **(2) transport** — the arrow is a *time* direction and selects no spatial rotation axis, so no screw is forced in 3+1D (consistently, 1+1D is dimension-special, where the arrow *is* the spatial direction); **(3) selection** — the first commitment carries the arrow (a time axis) and the P09 phase (an internal `U(1)`, `S¹`), both parity-*inert* (spatial parity does not act on an internal phase), so it has no pseudoscalar order parameter to break spatial parity; **(4) spontaneous (a distinct probe)** — the diastereomeric coupling `κ_h` measured on the real V5 all-pairs coherence is `≈ 0` (an earlier positive was a docking-registration artifact; this refutes the V5 coupling, not every spontaneous mechanism). So the arrow breaks *time* symmetry (giving the arrow itself, and via the P09 phase a matter/antimatter reference) but cannot break *spatial parity*. The one positive: the first-arrival P09-phase selection on `S¹` natively fixes a matter/antimatter **reference** (C) — the *selection* is native, its identification as the baryogenesis C-reference is account-tier, and the asymmetry's magnitude is inherited. Net verdict: a **vector-default fermion (for the minimal construction) with a C reference native and P inherited** — a clean, falsifiable matter-sector tiering, and a correction (not a fabrication) of the earlier C/P unification's P-half.

---

## 1. Introduction: The Question, and Why the Answer Is a Wall

The Standard Model's weak force is chiral — it couples differently to left- and right-handed fermions, violating parity maximally. A substrate ontology that aims to explain matter should ask whether this chirality is *forced* by the substrate or *inherited*. This paper reports the honest answer of ED's emergent-spinor attack: **inherited.** The emergent fermion is vector by default, and no canonical primitive hands it the weak force's parity violation.

A wall is a legitimate, and in this case valuable, result. It is stated cleanly, it is falsifiable (§7), and it comes with a single unifying reason (ED has no handed spatial structure) and one genuine *positive* alongside it (matter/antimatter asymmetry is native). The paper's discipline is to distinguish sharply between the two things a "chirality" claim can mean — C (matter/antimatter, charge conjugation) and P (parity, handedness) — because ED delivers the first and walls the second, and conflating them is exactly the over-read this paper corrects.

Section 2 reduces the chirality question to the screw pitch. Sections 3–5 check the three levels where built-in handedness could enter; §6 probes the distinct spontaneous route. Section 7 states the native positive and the wall together; §§8–9 give limitations and falsifiers.

### 1.5 Load-Bearing Step Audit

| Claim | Tier | Source / justification |
|---|---|---|
| Chirality discriminator = screw pitch `n_z` | **derived (for the minimal construction)** | §2 — closed-form SU(2) identity; a fuller construction is unbuilt/open |
| Emergent fermion is vector | **derived-conditional (minimal construction)** | §2, §§3–5 — no screw forced; not proven for every construction |
| Wiring: P07 has no channel-topology | **grounded (canonical P07)** | §3 — P07 is combinatorial distinguishability, no geometry |
| Transport: no 3+1D screw | **grounded** | §4 — arrow is a time axis, selects no spatial rotation axis |
| Selection: `S¹` is parity-inert | **grounded, with an open anomaly caveat** | §5 — spatial parity doesn't act on an internal phase; *unless* a chiral anomaly makes P09 P-odd (open) |
| Spontaneous: `κ_h ≈ 0` | **measured null (one coupling, V5)** | §6 — not the whole mechanism class |
| C (matter/antimatter) reference: the *selection* | **native (Selected, from P11+P09)** | §7 |
| C: identification as the baryon C-reference | **account** | §7 |
| C: asymmetry magnitude | **inherited** | §7 |
| P (weak chirality) | **inherited / WALL** | §7 — found absent where checked, not proven impossible |
| "ED is vector forever" | **NOT CLAIMED** | preamble 2 — a handed channel-topology is undefined-and-unbuilt, not forbidden |

The one *positive* (C) is a native selection plus an account-tier identification plus an inherited magnitude; the wall (P) is "found absent at every level checked," with one open anomaly caveat, not a proof of impossibility.

---

## 2. The Discriminator Reduces to One Number: The Screw Pitch

Build the **minimal** emergent Weyl 2-spinor with helicity eigenstates along the arrow (`|L⟩` = spin aligned with the arrow, `|R⟩` = anti-aligned). Transport is a `U(2)` link `U = e^{iφ} V`, where `φ` is the P09 `U(1)` phase advance and `V ∈ SU(2)` is the spin-frame re-routing by angle `θ` about axis `n̂`. Nothing chiral is put in by hand; the frame-rotation axis is scanned. The chiral discriminator is the difference in P09 phase-advance between the two helicities, `advance(h) = arg⟨h|U|h⟩`. In closed form (an exact SU(2) trig identity, confirmed algebraically):
$$\text{advance}(L) - \text{advance}(R) = -2\,\mathrm{atan2}\!\big(\sin(\theta/2)\,n_z,\ \cos(\theta/2)\big),$$
which is **nonzero iff `n_z ≠ 0`** — the component of the frame-rotation about the arrow. The cases:

- **Pure translation** (`θ = 0`) or **transverse rotation** (`n_z = 0`): discriminator `= 0` → **vector**. (Transverse rotation also flips helicity, `[U, σ_z] ≠ 0` — not a clean chiral split.)
- **Rotation about the arrow** (`n_z ≠ 0`, a **screw**): discriminator `≠ 0` → **chiral**, with helicity conserved (`[U, σ_z] = 0`); `|L⟩` and `|R⟩` are transport eigenstates with different geometric phases. **So `n_z` sources the `γ⁵` coupling** (an account-tier identification: `n_z` plays the role of `γ⁵`, it is not literally the Dirac matrix).

> **The entire "phase-screw → `γ⁵`" question reduces to one geometric fact: does transport screw the spin-frame about the arrow it advances along?**

**Scope of this reduction (honest).** The discriminator is computed for this *minimal* construction, and the product form `U = e^{iφ}·V` builds in a *reducible* (phase ⊥ spin) transport — so the scalar P09 phase `e^{iφ}` cancels from the discriminator, and the surviving handedness is `V`'s geometric phase. A different, unbuilt emergent-spinor construction — one with a genuinely *irreducible* P05 generator, where the phase-advance depends on the spin-frame *ab initio* — is not shown to reduce to the same `n_z` discriminator. So "default vector" is a verdict *for the minimal construction*; whether a fuller construction changes it is open (§8). With that scope fixed: chirality is *possible* (`n_z ≠ 0` is not forbidden) but earned only if the substrate forces a screw. The rest of the paper asks, at the levels where a screw could enter, whether it does. It does not.

---

## 3. Route 1 — Wiring: The Channels Have No Topology to Be Handed

Canonical Paper_087 §P07: *"Channels are structurally distinguishable carriers with intrinsic identities in the participation graph… substrate-level distinct objects, even if their bandwidth and polarity content happen to coincide."* This is a **combinatorial distinguishability** statement — channels are distinct labeled objects. It has no geometry, no arrangement, no topology. A set of distinguishable labels has no handedness.

So the helical screw the discriminator needs is not merely un-forced by P07 — it is **undefined** at the canonical level. The "channel topology" invoked elsewhere to carry spin and chirality is an *elaboration* (a Phase-2/3 target), and it has never been built: there is no constructed channel-topology whose handedness could even be checked. Tellingly, even within that elaboration, chirality is routed through a *selection* (baryogenesis filtering channels by polarity), not an intrinsic helix. **Route 1 fails: no topology, no handedness.**

---

## 4. Route 2 — Transport: A Time Arrow Selects No Spatial Screw

Polarity-transport, as derived, is a `U(N)` isometry forced by bandwidth conservation, channel re-routing, and invertibility between commitments. **None of these references spin or helicity** — the transport is spin-blind, so the default is vector. More sharply: a screw requires a rotation about the arrow (`n_z ≠ 0`), but the arrow is a *time* direction, and a time direction picks out no *spatial* rotation axis. There is no forced rotation-about-the-momentum in 3+1D, so `n_z` is a free (unfixed) degree of freedom the minimal primitives leave open.

This coheres with a known dimension-dependence: in 1+1D the single spatial direction *is* the arrow direction, collapsing the screw distinction, so the arrow gives chirality there (the 1+1D winding = anomaly result). In 3+1D the screw distinction reappears and the arrow alone does not supply it. **Route 2 fails: the arrow breaks time, not spatial handedness.**

---

## 5. Route 3 — Selection: No Pseudoscalar for the First Commitment to Imprint

If the wiring and transport do not force chirality, perhaps the first commitment *selects* it (the way it selects matter/antimatter). Breaking parity by selection requires a parity-**odd** (pseudoscalar) order parameter — three spatial axes with a fixed handedness. What does the first commitment actually carry? The arrow (a *time* axis) and the P09 phase (an internal `U(1)`, the circle `S¹`). Spatial parity acts trivially on both — the arrow is a time axis, and spatial parity does not act on an *internal* phase at all: the P09 circle is parity-**inert**. So selecting a point on `S¹` gives a charge-type (C) reference, not a handedness; there is no handed spatial 3-frame, and hence no pseudoscalar, for the first commitment to imprint. (A substrate orientation director is headless — a director plus the arrow is two axes, insufficient for a pseudoscalar.) **Route 3 fails: selecting on a parity-inert circle gives C, not P.**

**One honest caveat (flagged, not resolved).** "Parity-inert" is not automatically "parity-safe": in field theory an *internal* U(1) phase can be promoted to a genuine *pseudoscalar* by a chiral anomaly (the η′, axion, θ-vacuum are exactly parity-odd phase-on-a-circle objects, made P-odd by anomalous coupling to spacetime). The clean chain "internal U(1) ⟹ inert ⟹ C not P" therefore assumes the P09 U(1) is **not anomalously P-odd in 3+1D** — an open check (and the corpus's own 1+1D winding=anomaly result, §4, is exactly where such a coupling would live). If P09's phase were anomalously parity-odd, the selection route could give P after all, and the earlier "imprints both C and P" account would be partly rehabilitated. This is a real residual on Route 3, recorded here.

This is the route where the earlier over-read lived. A prior account claimed the first commitment imprints *both* a C reference (matter/antimatter) and a P reference (handedness). Its C-half is correct and stands (§7); its P-half assumed exactly the channel-topology screw that Routes 1 and 2 remove. This paper retires the P-half and keeps the C-half, with the reason.

---

## 6. Route 4 — Spontaneous (the V5 all-pairs probe): No Handedness Bias in the One Coupling Tested

The last route is a *distinct* one — spontaneous parity breaking of the molecular-homochirality kind, which needs no built-in handedness: a diastereomeric coupling `κ_h` that energetically favors one handedness, amplifying a fluctuation into a global bias (the Frank mechanism). A first probe with a docking/vertex-matching model gave `κ_h > 0` — apparent parity breaking. But that model imposed a lock-and-key registration by hand. Measured instead on the **V5 all-pairs cross-chain coherence**, `κ_h ≈ 0` (a null within the probe's resolution, no bias detected): the docking positive did not survive on the V5 coupling, and with no diastereomeric energy difference there is nothing to amplify.

**Scope, honestly.** This tests *one* coupling (V5 all-pairs), not the spontaneous mechanism class. Two limits are worth stating: (i) it is a **measured null on this coupling**, not a universal impossibility (preamble 4) — other spontaneous couplings are untested; and (ii) rejecting the docking model as an "artifact" and keeping the V5 model rests on the judgment that V5 all-pairs is the physical substrate coupling — a defensible call (the docking model imposes registration by hand), but *which model is physical* is itself not fully settled. So the honest statement is not "the spontaneous route fails" but **the one tested coupling shows no handedness bias; other spontaneous couplings are untested.**

---

## 7. The Verdict: a C Reference Native, P Walled, One Root Cause

The three built-in-handedness routes (wiring, transport, selection) fail for *one* reason — they are not independent proofs but three views of one absence — and the fourth (spontaneous) is a distinct probe that also comes up empty on the one coupling tested:

> **ED has no handed spatial structure.** The arrow breaks *time* symmetry — giving the arrow itself, and (through the P09 phase circle) a matter/antimatter *reference* — but it cannot break *spatial parity*, because nothing in the primitives supplies a pseudoscalar or a spatial screw. Time-asymmetry is native; spatial-handedness is not.

The matter-sector chirality tiering, stated with its tiers:

- **Matter/antimatter reference (C): the selection is ED-native, the identification is account-tier, the magnitude is inherited.** The first-arrival commitment selects a point on the P09 phase circle `S¹` — a genuine parity-inert `U(1)` order-parameter *selection* (this is the native part, from P11+P09). That this selection *is* charge conjugation / the baryon C-reference is an **identification** (account-tier), and the asymmetry's magnitude (the baryon-to-photon ratio) is **inherited**. So "native" applies to the mechanism of selecting a reference, not to the full C-asymmetry-with-a-number.
- **Parity violation / weak chirality (P): a wall.** No native mechanism was found at any level checked — wiring (no topology), transport (no 3+1D screw for the minimal construction), selection (no pseudoscalar, modulo the open anomaly caveat of §5), and the one spontaneous coupling tested (`κ_h ≈ 0` on V5). Weak chirality is **inherited, not derived**. ("Found absent where checked," not "proven impossible" — see the limitations.)

This is the honest culmination of the chirality attack: ED reproduces the matter/antimatter asymmetry but does not natively produce the weak force's parity violation, and the two must not be conflated. The result is a *derived-conditional vector fermion* with C native and P inherited — and a correction (not a fabrication) of the earlier C/P unification's P-half.

---

## 8. Limitations (honest)

- **Vector is default, not proven-forever.** The handed channel-topology that could earn chirality is undefined-and-unbuilt (not forbidden); building the full channel-topology→gauge program could in principle come out handed. The verdict is conditional on the minimal primitives and the current unbuilt state.
- **The homochirality null is one coupling.** `κ_h ≈ 0` refutes the V5-coupling route; it is not a proof that no mechanism could break parity.
- **Probe-level, not certified-simulator.** The chiral sector is Σ-blind; the discriminator is analytic with probe checks, not a certified-Σ measurement.
- **The native positive is a mechanism, not a number.** The matter/antimatter *asymmetry* is native; its magnitude (the baryon-to-photon ratio) is inherited.

---

## 9. Falsification Criteria

### 9.1 A forced screw

**Falsifier sentence:** *A demonstration that the primitives force `n_z ≠ 0` — a spatial rotation of the spin-frame about the arrow under transport — would earn chirality (`γ⁵` = the screw pitch) and overturn the vector-default verdict (§2).*

### 9.2 A handed channel-topology

**Falsifier sentence:** *A construction of the channel-topology→gauge program from the participation graph that comes out intrinsically handed would supply the pseudoscalar structure Routes 1 and 3 find absent, and overturn the wall (§§3, 5).*

### 9.3 A pseudoscalar order parameter

**Falsifier sentence:** *Identification of a parity-odd order parameter carried by the first commitment (a handed spatial 3-frame, or a chiral anomaly making the P09 phase pseudoscalar rather than parity-inert) would let selection break parity (P), not just C (§5).*

### 9.4 A nonzero diastereomeric coupling

**Falsifier sentence:** *A measurement showing `κ_h ≠ 0` on the real substrate coupling (not a docking model) would reopen the spontaneous route (§6).*

---

## 10. Position Statement

**ED's emergent fermion is vector by default (for the minimal construction), and the weak force's parity violation is inherited, not derived.** The chiral discriminator reduces to a single screw-pitch quantity that the primitives do not force, found absent at every level checked — wiring (P07 has no topology), transport (the arrow is a time axis, no spatial screw), selection (no pseudoscalar; the P09 phase is parity-inert, modulo an open anomaly caveat) — plus one distinct spontaneous probe (`κ_h ≈ 0` on the V5 coupling). These are not four independent proofs: the first three are one absence — ED has no handed spatial structure — seen from three sides. The one positive: the first-arrival P09-phase selection on `S¹` natively fixes a matter/antimatter **reference** (C) — a native *selection*, with the identification as the baryon C-reference account-tier and the magnitude inherited.

**What this paper claims.** A derived-conditional (minimal-construction) vector fermion; parity violation found absent at every level checked (three views of one absence, plus one spontaneous probe), so inherited; a natively-selected matter/antimatter *reference* (with account-tier identification and inherited magnitude); and a correction of the earlier "first-arrival imprints both C and P" over-read (C stands, P retired).

**What this paper does not claim.** That ED is provably vector forever (a handed channel-topology is undefined-and-unbuilt, not forbidden); that the routes are independent (they share one root cause); that parity-breaking is impossible by every mechanism (`κ_h ≈ 0` is one coupling; the §5 anomaly caveat is open); or that the C-asymmetry's magnitude is derived (inherited).

**Series context.** The matter-sector chirality verdict of the ED program. It turns on the same primitive the reduction program isolates — the arrow (P11), which breaks time (giving the arrow and matter/antimatter) but not spatial parity — and it pairs with the gauge-structure paper (the weak `SU(2)` whose chirality is here shown inherited) and the quantum-logic keystone (the einselection that makes the arrow the sole asymmetry). It is the program's cleanest wall: a sharp negative on parity, a sharp positive on matter/antimatter, and an explicit line between them.

---

## Appendix — Glossary and Reader Map

### Glossary

- **C (charge conjugation).** A matter/antimatter *reference*; a parity-*inert* internal-phase selection. The *selection* is ED-native (first-arrival P09-phase); the identification as C and the magnitude are account/inherited.
- **P (parity).** Spatial handedness / left-right asymmetry; needs a parity-*odd* (pseudoscalar) order parameter. Walled in ED.
- **Screw pitch (`n_z`).** The rotation of the spin-frame about the arrow under transport; equals `γ⁵`. Zero by default → vector.
- **Diastereomeric coupling (`κ_h`).** An energy difference favoring one handedness (the homochirality route); measured `≈ 0` on the real V5 coupling.
- **Vector-default.** The emergent fermion couples identically to both helicities unless a screw is forced; the derived-conditional verdict.

### Reader map

*Intuition.* To make a left-right asymmetry you need a built-in sense of handedness — a screw, a pseudoscalar, a three-fingered rule. ED's arrow is a *time* direction: it tells past from future, and through the phase it tells matter from antimatter, but it says nothing about left versus right. So ED gets the matter/antimatter imbalance for free and has to be *told* the weak force's handedness. Four different ways of trying to squeeze handedness out of the substrate all come up empty for the same reason: there is no handedness in there to begin with.

*Why the wall is worth publishing.* A theory that quietly manufactured parity violation would be over-claiming; ED's honest verdict is that it cannot, and it says so, while cleanly keeping the one chirality-adjacent thing it *does* deliver (matter/antimatter). The sharp separation of C (native) from P (inherited) is the result.

**Where to look next.**
- *The weak `SU(2)` whose chirality is here inherited:* the gauge-structure paper.
- *The arrow that breaks time but not parity:* the minimal-ontology and quantum-logic papers.
- *The baryogenesis C-selection that stands:* the first-arrival / R4 arc.

**Open work** (declared): whether a built channel-topology→gauge program comes out handed (Routes 1/2); whether any parity-odd order parameter exists in ED (Route 3); the baryon-asymmetry magnitude (native mechanism, inherited value).

---

**End of Paper (The Parity Wall).**

*Substrate-evaluation arc. The chirality discriminator (for the minimal construction) reduces to a screw pitch `n_z` the primitives do not force; parity violation is found absent at the three levels where built-in handedness could enter (no channel-topology, no 3+1D screw, parity-inert phase modulo an open anomaly caveat) — one absence seen three ways — plus a distinct spontaneous probe (`κ_h ≈ 0` on V5). Root reason: ED has no handed spatial structure. The arrow breaks time (→ the arrow, → a matter/antimatter reference via the P09 phase) but not spatial parity. Verdict: a vector-default fermion with a C reference natively selected (identification account-tier, magnitude inherited) and P (weak chirality) inherited; and a correction of the earlier first-arrival C/P over-read (C stands, P retired). A clean, falsifiable matter-sector wall — found absent where checked, not proven impossible.*
