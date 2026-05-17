# Paper 005.5 — Double-Slit Experiment

**Series:** Wave-3 Generative Papers (QM-Kinematics Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (Paper_087) + one paper-specific naming convention. Verdict per Paper_095: **M3 (form-IDENTIFIED + value-INHERITED).**
**Date:** 2026-05-15
**Anchors:** Paper_005 (P11 commitment / projector form), Paper_063 (bipartite non-factorizability via V5), Paper_089 (V1 kernel), Paper_090 (V5 kernel), Paper_003 (Born frequency limit), Paper_072 (individuation regime).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of $\lambda = h/p$, the fringe-spacing geometry $d\sin\theta = m\lambda$, or the visibility-vs-coupling decoherence curve. All three are INHERITED from standard QM + standard wave optics + standard decoherence theory.
2. It does **not** claim a substrate first-principles derivation of the apparatus-specific value of $\Theta_{\mathrm{ED}}$ (P12 ED-threshold). Substrate derivation in $\ell_{ED}$ + V1/V5 kernel parameters is OPEN; apparatus-specific value INHERITED via empirical matching to coherence-loss boundary.
3. It does **not** claim closed-proof reconstruction in the Hardy 2001 / CDP 2011 / Coecke-Kissinger operational-reconstruction sense. ED sits in the substrate-ontology lineage ('t Hooft cellular-automaton, Wolfram Ruliad, causal-set program), not the operational-reconstruction lineage.
4. It does **not** override Paper_095's three-tier verdict grammar. Verdict for this paper is **M3 (form-IDENTIFIED + value-INHERITED)** as stated in §1; the audit table contains zero pure-D rows. The structural substrate composition is identified, not forced; the language "form-IDENTIFIED" rather than "form-FORCED" is the §1 / §4 / §6 default.
5. It does **not** introduce new substrate primitives. P-EDThreshold-Collapse is a naming convenience (P12 + P11 + Paper_005 conjunction), not a new postulate. The earlier-draft P-MultiChannel-Capacity and P-WhichPath-as-EDInjection are absorbed into upstream content (Paper_072 individuation; V5 + P12 conjunction respectively).

---

## Abstract

The double-slit experiment is the structural composition of four substrate-level mechanisms acting on a single chain $C$: (i) **multi-channel participation** below the P12 ED-threshold, with one chain distributing bandwidth across slit-A, slit-B, and downstream channels per P02+P04+P07+Paper_072 — no splitting, no duplication; (ii) **coherent V1 propagation** (Paper_089) preserving the substrate phase difference $\Delta\pi(x)$ across channels; (iii) the **detection-plane participation distribution** $\rho^C(x) = |\sum_K P_K(x)|^2$, whose constructive/destructive structure (substrate phase, Paper_008) gives the fringe pattern as the per-trial commitment-probability density (Paper_003 Born frequency limit + Paper_005 projector); (iv) **threshold-driven collapse** with which-path-as-V5-injection: V5 cross-channel coupling (Paper_063, Paper_090) to a path-distinguishing environment transfers substrate event-density into $C$, raising local ED above $\Theta_{\mathrm{ED}}$ and triggering single-channel commitment before the participation field reaches the detector.

Delayed-choice carries no retrocausality: threshold-crossing is local in time and follows V5 coupling at the moment any path-distinguishing apparatus engages the chain. Verdict per Paper_095: **M3 (form-IDENTIFIED + value-INHERITED)**. Form IDENTIFIED: existence of the interference pattern as participation distribution; binary structural collapse at $\Theta_{\mathrm{ED}}$; visibility loss under V5 coupling; locality-in-time of delayed-choice. Value INHERITED: fringe spacing, $\lambda = h/p$, $\Theta_{\mathrm{ED}}$ apparatus-value, visibility-vs-coupling curve. Sharpest falsifier (F1): a quantum carrier whose local ED exceeds $\Theta_{\mathrm{ED}}$ yet sustains multi-channel interference at the detector — refutes the P12 + P11 + Paper_005 commitment composition.

---

## §1 Statement of Result

The double-slit experiment composes four substrate mechanisms on a single chain $C$:

1. **Multi-channel participation** below $\Theta_{\mathrm{ED}}$: $\Psi^C = \sum_K P_K |K\rangle$ with $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (Paper_001 / Paper_003_5). One chain, multiple channels per P02+P04+P07; chain-identity preserved per Paper_072.
2. **Coherent V1 propagation** (Paper_089) advances the multi-channel amplitudes jointly, preserving $\Delta\pi(x) = \pi_{K_A}(x) - \pi_{K_B}(x)$.
3. **Detection-plane participation distribution** $\rho^C(x) = |\sum_K P_K(x)|^2$ via Born frequency limit (Paper_003) on V1-propagated amplitude. Per-trial: P11 commits to one $K^*$ via Paper_005's projector form. Many-trial: empirical density converges to $\rho^C(x)$.
4. **Threshold collapse and V5 which-path injection.** Crossing $\Theta_{\mathrm{ED}}$ (P12) triggers irreversible single-channel commitment (P11). Path-distinguishing apparatus couples $C$ to environment $E$ via V5 cross-chain (Paper_063, Paper_090); the V5 coupling injects substrate event-density into $C$, raising local ED above $\Theta_{\mathrm{ED}}$ and forcing collapse before V1 propagation reaches the detector. Visibility loss is structural (V5-driven cross-chain ED injection), not epistemic.

Delayed-choice carries no retrocausality: threshold-crossing is local in time and follows V5 coupling at the moment of apparatus engagement.

**Form IDENTIFIED:** existence of the interference pattern as participation distribution; binary structural collapse at $\Theta_{\mathrm{ED}}$; visibility loss under V5 coupling; locality-in-time of delayed-choice. **Value INHERITED:** fringe spacing $\Delta x = \lambda L/d$ (Born–Wolf path-difference applied to $\pi_K$); $\lambda = h/p$ (Paper_012, Paper_012_5; $h$ INHERITED); apparatus-specific value of $\Theta_{\mathrm{ED}}$; visibility-vs-coupling curve.

---

## §2 Primitive Inputs + Upstream Dependencies

**Primitives (Paper_087):** P02 (participation), P04 (bandwidth), P07 (channel structure), P09 (U(1)-valued polarity), P11 (commitment-irreversibility), P12 (ED-threshold / stability landscape).

**Upstream:**
- I-001 / I-003_5: $P_K = \sqrt{b_K}\,e^{i\pi_K}$ amplitude convention.
- I-003: Born frequency limit $f_K = b_K / \sum b_{K'}$.
- I-005: Projector form $\Pi_{K^*}$ from P11 commitment-event identification.
- I-008: $\pi_K \in S^1$.
- I-063: Bipartite non-factorizability under V5 cross-channel correlation.
- I-072: Individuation regime — chain-identity preservation across multi-channel participation.
- I-089: V1 finite-width retarded kernel (coherent propagation).
- I-090: V5 cross-chain finite-memory kernel.
- I-WaveOptics: Path-difference geometry (Born–Wolf).
- I-deBroglie: $\lambda = h/p$ ($h$ INHERITED).

**Paper-specific naming convention (no new postulate):**

- **P-EDThreshold-Collapse:** Naming convenience for the joint action of P12 (threshold exists) + P11 (commitment is irreversible) + Paper_005 (commitment ↔ projector). Definitional per Paper_095 §2.3 (composition of upstream content under a single name). No new substrate content.

The earlier-draft P-MultiChannel-Capacity and P-WhichPath-as-EDInjection are absorbed into upstream content (Paper_072 individuation regime preserves chain-identity across distributed bandwidth; V5 cross-chain coupling + P12 threshold conjunction supplies the which-path-as-injection identification). Recording the absorption as honest historical accounting; neither remains load-bearing as a paper-specific postulate.

---

## §3 Derivation

### 3.1 Multi-channel participation below threshold

Below $\Theta_{\mathrm{ED}}$ (P12), a chain $C$ traversing the two-slit aperture has bandwidth distributed across the substrate channels coupled by the aperture geometry:

$$
\Psi^C(\text{aperture}) = P_{K_A}|K_A\rangle + P_{K_B}|K_B\rangle, \qquad P_{K_\alpha} = \sqrt{b_{K_\alpha}}\,e^{i\pi_{K_\alpha}}.
$$

Per Paper_072, $C$ retains a single substrate identity across this distribution; the multi-channel form is one chain participating in multiple channels, not multiple copies. For symmetric slits, $b_{K_A} = b_{K_B}$.

### 3.2 Coherent V1 propagation

The V1 kernel (Paper_089) acts on each channel amplitude:

$$
P_{K_\alpha}(x) = \int K_{V_1}(x - x'_\alpha)\,P_{K_\alpha}(x'_\alpha)\,d^3 x'_\alpha.
$$

Linearity of convolution + V1's finite-width retarded support preserves the relative phase $\Delta\pi(x) = \pi_{K_A}(x) - \pi_{K_B}(x)$ in the regime $\ell_{V_1} \ll d$ (slit separation). To leading order in standard far-field geometry:

$$
\Delta\pi(x) = \frac{2\pi}{\lambda}\,\frac{d\,x}{L}, \qquad \lambda = h/p \;\text{(INHERITED)}.
$$

### 3.3 Detection-plane participation distribution

Per Paper_003 (substrate-frequency Born identification) the participation density at the detector is the Born rule applied to the V1-propagated multi-channel amplitude:

$$
\rho^C(x) \;=\; |P_{K_A}(x) + P_{K_B}(x)|^2 \;=\; b_{K_A}(x) + b_{K_B}(x) + 2\sqrt{b_{K_A}\,b_{K_B}}\,\cos\Delta\pi(x).
$$

For symmetric slits with $b_{K_A}(x) \approx b_{K_B}(x) \equiv b_0(x)$:

$$
\rho^C(x) \;=\; 4 b_0(x)\,\cos^2\!\bigl(\tfrac{1}{2}\Delta\pi(x)\bigr).
$$

Per-trial: P11 commits to one $K^*$ with probability $\propto \rho^C$ (Paper_005). Many-trial: empirical distribution converges to $\rho^C(x)$ (Paper_003 frequency limit). Bright fringes correspond to $\Delta\pi = 2\pi m$; dark fringes to $\Delta\pi = (2m+1)\pi$; fringe spacing $\Delta x = \lambda L/d$ from standard wave-optics path-difference geometry applied to the substrate phase $\pi_K$.

### 3.4 Threshold collapse

When local event-density crosses $\Theta_{\mathrm{ED}}$ (P12), P11 fires once; Paper_005's projector form selects $K^*$ with probability $b_{K^*}/\sum b_{K'}$. Pre-threshold: multi-channel. Post-threshold: $\Psi^C = |K^*\rangle$. The transition is binary, structural, physical — not epistemic. This is the substrate quantum-classical boundary at the per-event level; P-EDThreshold-Collapse is the naming convenience for the P12 + P11 + Paper_005 conjunction.

### 3.5 Which-path = V5 ED-injection

Path-distinguishing apparatus $D$ at slit $\alpha$ couples to $C$ via V5 cross-chain (Paper_090). The substrate joint state is non-factorizable (Paper_063):

$$
\Psi^{C \cup D} \;=\; P_{K_A}\,|K_A\rangle_C \otimes |D_A\rangle_D \;+\; P_{K_B}\,|K_B\rangle_C \otimes |D_B\rangle_D.
$$

Two substrate consequences:

(i) **Strong coupling:** the V5 cross-chain transfers substrate event-density into $C$'s local ED budget. The substrate-graph derivation of the V5-coupling-to-ED-injection rate from V5 kernel parameters is OPEN; the **identification** that V5 coupling carries substrate ED transfer is what is established here. For sufficient coupling, $C$'s local ED exceeds $\Theta_{\mathrm{ED}}$ at the slit; threshold collapse fires immediately and $C$ commits to a single channel before V1 propagation reaches the detector. The interference cross-term is absent; the screen records the single-slit envelope $|P_{K_A}|^2 + |P_{K_B}|^2$.

(ii) **Weak coupling:** the chain's reduced state — obtained by tracing out $D$ — is diagonalized in $\{|K_A\rangle, |K_B\rangle\}$ at the rate set by $\langle D_A | D_B\rangle$. Visibility decreases monotonically with V5 coupling strength; the standard decoherence visibility-vs-coupling curve is INHERITED.

Which-path is V5 cross-channel coupling; it is not knowledge.

### 3.6 Delayed-choice without retrocausality

Threshold-crossing is local in time: it occurs when cumulative V5 ED transfer into $C$ exceeds $\Theta_{\mathrm{ED}}$. If $D$ is inserted before the chain's V1-propagated participation field reaches it, V5 coupling at $D$'s spatial position injects ED at the time of insertion → threshold-crossing → single-channel collapse → no interference. If $D$ is removed (or absent), no V5 coupling, no ED injection, multi-channel participation persists to the detector → interference. The "choice" is the timing of V5 coupling; the substrate response is local, no retrocausality required.

### 3.7 Channels vs pattern

Channels (P07) exist before the pattern: slit A, slit B, micro-geometric sub-paths, downstream propagation channels $K(x)$. Pattern is the participation distribution $\rho^C(x)$ accumulated over many P11 commitments. Bright fringe = high-strength channel (constructive substrate phase reinforcement); dark fringe = channel where substrate phase cancels.

Mapping: **Channels → coherent V1 propagation of $P_K$ → participation distribution $\rho^C(x)$ → per-trial P11 commitment → many-trial pattern.**

---

## §4 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P02, P04, P07, P09, P11, P12 | P | Paper_087. |
| 2 | $P_K = \sqrt{b_K}\,e^{i\pi_K}$ | I | Paper_001 / Paper_003_5. |
| 3 | Born frequency $f_K = b_K/\sum b_{K'}$ | I | Paper_003. |
| 4 | P11 commitment ↔ projector $\Pi_{K^*}$ | I | Paper_005. |
| 5 | Chain-identity preserved across multi-channel participation | I | Paper_072. |
| 6 | V1 coherent kernel propagation | I | Paper_089. |
| 7 | V5 cross-chain coupling, non-factorizable joint state | I | Paper_063, Paper_090. |
| 8 | Multi-channel participation below $\Theta_{\mathrm{ED}}$ | **D-via-I** | Composition of P02+P04+P07+P12+I-072 under the substrate identification of "one chain across multiple channels." Per Paper_095 §2.3. |
| 9 | Phase-preserving V1 propagation in $\ell_{V_1} \ll d$ regime | **I** | Linearity of convolution; substrate-specific content (V1's finite-width retarded support) is identified but not load-bearing — any single linear kernel preserves relative phase under far-field separation. |
| 10 | Detection-plane participation density $\rho^C(x) = |\sum_K P_K(x)|^2$ | **D-via-I** | Born rule (I, Paper_003) applied to V1-propagated multi-channel amplitude (I, Paper_089). Composition of inheritances per Paper_095 §2.3. |
| 11 | Constructive/destructive fringe structure from $\Delta\pi$ | **I** | Standard wave-optics path-difference (Born–Wolf) applied to substrate phase carrier $\pi_K$. Carrier identification only; geometry is standard. |
| 12 | Fringe spacing $\Delta x = \lambda L/d$ | I | Born–Wolf, $\lambda = h/p$ INHERITED. |
| 13 | Threshold collapse: P12 crossing → P11 commitment (P-EDThreshold-Collapse) | **P** | Definitional naming convention per Paper_095 §2.3; no new substrate content beyond P12 + P11 + Paper_005 conjunction. |
| 14a | V5 coupling → cross-chain ED injection → threshold collapse | **D-via-I** | Composition of V5 (Paper_090) + P12 + P11 under the identification that V5 coupling carries substrate ED transfer. Per Paper_095 §2.3. |
| 14b | Substrate-graph derivation of V5-coupling-to-ED-injection rate | **OPEN** | The identification at row 14a is established; the substrate-graph computation linking V5 kernel parameters to the ED-injection rate is not constructed. |
| 15 | Reduced-state visibility under weak V5 coupling | I | Standard decoherence theory. |
| 16 | Delayed-choice locality-in-time | **D-via-I** | V5 coupling event is local in time; threshold-crossing fires at coupling time. Composition of V5 locality + P-EDThreshold-Collapse. |
| 17 | Apparatus-specific value of $\Theta_{\mathrm{ED}}$ | **OPEN** | Substrate derivation in $\ell_{ED}$ + V1/V5 parameters not constructed. INHERITED via empirical matching. |
| 18 | Visibility-vs-coupling curve from V5 first principles | **OPEN** | Standard decoherence phenomenology INHERITED; substrate first-principles derivation not constructed. |
| 19 | Verdict M3 (form-IDENTIFIED + value-INHERITED) | **A→position** | Per Paper_095 §3.3 line 77 (framing-claim verdict row). |

Zero pure-D rows. Audit content matches M3 form-IDENTIFIED + value-INHERITED (composition + identification + standard inheritance, no genuine new substrate-graph derivation). No A rows beyond the verdict-framing row 19.

---

## §5 Falsification Criteria

- **F1 (sharpest):** A quantum carrier whose local ED demonstrably exceeds $\Theta_{\mathrm{ED}}$ (per Paper_012 RB1 substrate-rate identification, with $\Theta_{\mathrm{ED}}$ pinned by the visibility-loss boundary in the same apparatus class) yet sustains multi-channel interference at the detector — refutes the P12 + P11 + Paper_005 commitment composition.

- **F2:** A path-distinguishing apparatus that produces interference erasure with V5 coupling strength below the threshold required for $\Theta_{\mathrm{ED}}$-crossing AND below the visibility-decay coupling implied by the standard decoherence curve — refutes the V5-driven which-path identification. Operational: visibility decay that exceeds the V5-coupling-implied bound at the same apparatus geometry.

- **F3:** Visibility loss not monotonically increasing in V5 coupling strength — refutes the V5 + P12 + decoherence composition.

- **F4:** A delayed-choice variant in which the future configuration of $D$ affects past commitment statistics in a way not reducible to local-in-time V5-coupling-at-engagement — refutes the locality-in-time of P-EDThreshold-Collapse.

---

## §6 Position Statement

This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton; Wolfram Ruliad; causal-set program), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

The ED account replaces wave-particle duality with single-chain multi-channel participation, epistemic collapse with V5-driven substrate ED injection above $\Theta_{\mathrm{ED}}$, many-worlds branching with single-chain commitment selection, and retrocausal pilot-wave with local-in-time threshold-crossing. The Channels-vs-Pattern distinction (channels are P07 path geometry existing before the trial; pattern is the participation distribution accumulated over many P11 commitments) is the substrate-side reading of the apparent paradox: there is no "wave" propagating in physical space — there is a single chain whose multi-channel participation amplitude is structured by V1 across the apparatus, with the per-trial commitment-density $\rho^C(x)$ giving the screen pattern in the many-trial limit.

The genuine substrate content is the composition (rows 8, 10, 14a, 16): the participation-distribution-as-pattern identification, the Born-rule application to V1-propagated multi-channel amplitude, the V5-as-which-path-injection identification, and the locality-in-time of delayed-choice. Numerical content (fringe geometry, $\lambda$, $\Theta_{\mathrm{ED}}$, visibility curve) is INHERITED. Three named OPEN items remain (rows 14b, 17, 18); closing row 14b would consolidate the substrate-graph derivation of which-path mechanism; closing row 17 would consolidate $\Theta_{\mathrm{ED}}$ as a derived substrate scale.

Verdict: **M3 (form-IDENTIFIED + value-INHERITED)** per Paper_095. Audit table contains zero pure-D rows; the four substantive substrate-side rows (8, 10, 14a, 16) are composition/identification of upstream content, not new substrate-graph derivation. The "form-IDENTIFIED" framing rather than "form-FORCED" is the honest reading: the structural account is identified across the substrate composition, not forced from substrate primitives alone.

---

**End Paper 005.5.**
