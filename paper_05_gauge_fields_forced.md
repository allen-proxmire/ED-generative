# Gauge Fields are FORCED (Theorem 17)

**Paper #5 of the Event Density Forcing Series**

**Author:** Allen Proxmire
**Status:** Publication draft
**Date:** 2026-05-12
**Series:** Event Density (ED) First-Wave Forcing Papers — Paper #5 of 10
**Genre:** Forcing paper. Standalone. Cold-reader accessible.

---

## Abstract

The gauge structure of standard physics — local symmetry, gauge potentials $A_\mu$, covariant derivatives $D_\mu = \partial_\mu + igA_\mu$, field strengths $F_{\mu\nu}$, minimal coupling between matter and gauge fields — is normally a list of postulates: Maxwell's equations for electromagnetism, the Yang-Mills construction for non-Abelian theories, the fiber-bundle formalism that abstracts them. This paper shows that, given a small set of substrate conditions and the participation-measure, Born-rule, inner-product, and Schrödinger results of Papers #1-#4, the entire gauge structure is forced: the gauge potential is the participation measure of a substrate-level rule-type $\tau_g$; minimal coupling is vertex-anchored commitment; field strength is the commutator of transported phases; local symmetry is the residual gauge-quotient invariance that the rule-type carries. The specific gauge group (U(1), SU(2), SU(3), or otherwise) and the coupling magnitudes remain inherited from the value layer, but the structural existence of the gauge-field architecture is forced. Postulated-gauge, global-only-symmetry, non-connection-based, and quaternionic alternatives are each excluded by substrate-condition violation.

---

## 1. Framing

### 1.1 What standard physics postulates about gauge fields

Every undergraduate textbook on quantum field theory presents the gauge structure as a list of axioms. To couple a matter field to electromagnetism, one introduces a U(1) gauge potential $A_\mu(x)$, replaces every ordinary derivative $\partial_\mu$ with a covariant derivative $D_\mu = \partial_\mu + ieA_\mu$, builds the field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, and forms the Lagrangian $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi$. For non-Abelian theories, the same construction repeats with a non-commutative gauge potential $A_\mu^a T^a$, a non-Abelian field strength $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - gf^{abc}A_\mu^b A_\nu^c$, and the Yang-Mills Lagrangian.

Five structural facts are bundled into this construction:

1. **Existence of a gauge potential $A_\mu$.** The potential is a primary field, distinct from the matter field and from the observable field strength.
2. **Local symmetry.** The Lagrangian is invariant under $\psi \to U(x)\psi$, $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$, with $U(x)$ varying from point to point — *local*, not global.
3. **Field strength as curvature.** $F_{\mu\nu} \propto [D_\mu, D_\nu]$ — the commutator of covariant derivatives produces the gauge-invariant observable.
4. **Minimal coupling.** Matter couples to the gauge field exactly through the replacement $\partial \to D$ — no Pauli term, no anomalous magnetic moment by hand, no extra interaction structure.
5. **Specific gauge group.** Nature uses U(1) for electromagnetism, SU(2)×U(1) in the electroweak sector, SU(3) for QCD. Each is a compact simple (or product of compact simple) Lie group with Killing-form / Jacobi closure.

These five facts arrived historically as inferences from experiment and were later organized into the modern formalism. Where they come from — why local rather than global symmetry, why minimal coupling rather than non-minimal, why compact Lie groups rather than discrete groups or non-compact ones — is not derived in standard quantum field theory. They are part of the package.

### 1.2 The puzzle

Several programs have attempted to motivate parts of the gauge structure from deeper principles:

- **Weyl's gauge-principle argument** (1929): if the matter-field phase is locally redefinable, the covariant derivative + gauge potential structure follows by demanding that the dynamics remain invariant. The local-phase-redefinability is the input; gauge structure is the consequence.
- **Fiber-bundle reconstruction**: gauge theories are reformulated as connections on principal bundles. The Lie group, the bundle, and the connection form are mathematical inputs.
- **Emergent-gauge programs** in condensed matter (spin liquids, lattice gauge models): gauge-field-like structures emerge as effective descriptions of highly entangled states. The microscopic Hamiltonian and the emergence mechanism are inputs.

None of these programs derives the gauge structure from a *substrate of pre-quantum, pre-field-theoretic primitive structure*. The deeper question — why the world has rule-types whose participation measures behave like connections on bundles, with curvatures and minimal couplings — remains unaddressed.

A program that wants to settle the question structurally needs:

1. A pre-quantum substrate that contains structural rule-types as primitives, but no gauge group, no covariant derivative, no field strength.
2. An argument that polarity transport on the participation manifold, plus bandwidth conservation, forces the connection structure.
3. An explicit exclusion of alternatives — no-gauge-fields, global-only-symmetry, non-minimal-coupling, real-valued, quaternionic — by substrate-condition violation.

### 1.3 What this paper does

The Event Density (ED) framework supplies the first ingredient. Papers #1-#4 establish the participation measure, the Born rule, the sesquilinear inner product on the participation manifold, and the Schrödinger evolution equation — all forced from substrate primitives. The present paper takes this machinery as input and forces:

1. The **existence of a gauge potential** $A_\mu$ as the participation measure of a substrate-level **rule-type** $\tau_g$.
2. The **gauge-quotient structure** (local symmetry) as the rule-type's interface property — the absence of distinction between structurally-identical configurations.
3. The **field strength** $F_{\mu\nu}$ as the commutator of transported phases along the participation manifold.
4. **Minimal coupling** as the vertex-anchored commitment structure of $\tau_g$.
5. **Non-Abelian-capable group structure** with Killing-form / Jacobi closure, allowing U(1), SU(2), SU(3) and other compact-simple-Lie groups as admissible specific cases. The choice of specific group is inherited from the value layer.

Alternative structures — no-gauge-fields, global-only-symmetry, non-connection-based transport, non-curvature field strength, non-minimal coupling, real-valued or quaternionic gauge structure — are excluded by explicit substrate-condition violation.

**Series context.** Paper #1 forced the amplitude carrier. Paper #2 forced the probability rule. Paper #3 forced the inner product and the Tsirelson ceiling. Paper #4 forced the Schrödinger dynamics. The present paper forces the first interaction structure: gauge fields appear as forced rule-types coupling to the matter participation measure via vertex-anchored commitment. Together, Papers #1-#5 cover the complete kinematic + dynamical + interaction backbone of non-relativistic gauge-coupled quantum mechanics.

---

## 2. Claim

> **Forcing Theorem (Gauge-Field-as-Rule-Type, T17).** Let any substrate satisfy the conditions $\{C\}$ stated in §5. Then there exists a structural rule-type $\tau_g$ whose participation measure $A_\mu$ is FORCED to satisfy:
> - **(F1)** Non-Abelian-capable gauge-group structure with Killing-form / Jacobi closure.
> - **(F2)** Vertex-anchored minimal-coupling vertex; gauge-invariant under the rule-type's local symmetry.
> - **(F3)** Field strength $F_{\mu\nu} \propto [D_\mu, D_\nu]$ as the commutator of transported phases.
> - **(F4)** Local gauge-quotient invariance: structurally-identical configurations are not distinguished by the substrate.
>
> The form of the gauge structure is forced; the specific gauge group (U(1), SU(2), SU(3), or other admissible compact-simple-Lie group) and coupling magnitudes are inherited from the value layer.

---

## 3. Scope

### 3.1 What is FORCED

- The **existence of a gauge potential** $A_\mu$ as the participation measure of a substrate-level rule-type $\tau_g$.
- **Local symmetry**: the gauge-quotient invariance of the rule-type, not a global symmetry only.
- **Field strength as commutator**: $F_{\mu\nu}$ is the curvature 2-form associated with parallel transport on the participation manifold.
- **Minimal coupling**: matter-gauge interactions enter through the substrate-level vertex-anchored commitment vertex, with no extra non-minimal terms.
- **Non-Abelian-capable group structure** with Killing-form / Jacobi closure. The substrate admits compact simple Lie groups as the candidate class.

### 3.2 What is INHERITED

- **Specific gauge group.** U(1) for electromagnetism, SU(2)×U(1) for electroweak, SU(3) for QCD. The choice of specific group is empirical (or inherited from value-layer commitments such as the matter-rule-type content of the Standard Model). T17 commits only to the *non-Abelian-capable group structure* admissible class, not to any specific member of it.
- **Coupling constants** $e$, $g$, $g'$, $g_s$, the gauge couplings of the Standard Model. Inherited from the value layer.
- **V1 kernel parameters** for the gauge-field vacuum sector. Inherited from the substrate vacuum-kernel structure of the ED program's Arc N.
- **Specific labeling of generators.** The basis of generators $T^a$ in the Lie algebra is a labeling choice; the structural content is the algebra itself.

### 3.3 What is OUT OF SCOPE

- This paper does **not** derive the full Standard Model. Specific gauge group (SU(3)×SU(2)×U(1)), matter content (quarks, leptons, three generations), and coupling values are inherited from the value layer. T17 commits only to the structural existence of gauge-field-class rule-types and their interface property.
- This paper does **not** derive the Higgs mechanism. Symmetry breaking and the Higgs sector require additional substrate content (the matter-rule-type sector and its vacuum-condensate structure) not addressed here.
- This paper does **not** derive gravity. Gravitational coupling lives in a separate ED-program sector (substrate-gravity arc) treating curvature emergence as a different forcing chain.
- This paper does **not** derive specific propagator forms or scattering amplitudes. The Feynman-diagram machinery operates downstream of the structural commitments forced here.
- This paper does **not** address full QFT vacuum content (Higgs VEV, QCD condensates, instantons, $\theta$-vacua). The substrate vacuum-kernel structure forces a gauge-invariant V1-form fluctuation envelope; the specific vacuum content of the Standard Model is value-layer empirical.

---

## 4. Key Vocabulary

For the reader new to Event Density:

- **Substrate.** Pre-quantum layer of primitive structure on which the ED framework is built. Not a Hilbert space, manifold, or field theory.
- **Rule-type.** A substrate primitive (P02) class of structural pathway — a kind of channel admitting its own participation measure. Matter fields and gauge fields are participation measures of distinct rule-types.
- **Participation measure.** The complex-valued amplitude carrier on each channel of the participation graph; for the matter sector, $P_K(u) = \sqrt{b_K(u)}\,e^{i\pi_K(u)}$ (Paper #1); for the gauge sector, the gauge potential $A_\mu$.
- **Polarity.** A primitive $U(1)$-valued angular variable on each channel at each locus.
- **Polarity transport.** The structural action by which a polarity value is carried along a path on the participation manifold from one locus to another.
- **Connection.** A geometric object encoding the path-dependence of polarity transport: parallel transport over a path produces a phase factor determined by the connection.
- **Curvature.** The 2-form $F = dA + A \wedge A$ measuring the path-dependence of transport around an infinitesimal loop. Equivalently, the commutator $F_{\mu\nu} \propto [D_\mu, D_\nu]$ of covariant derivatives.
- **Holonomy.** The phase factor accumulated by polarity transport around a closed loop. Equal to $\exp(\oint A_\mu dx^\mu)$ in the U(1) case.
- **Minimal coupling.** The substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu T^a$ in the matter dynamics. In ED language: matter-gauge interactions enter through the substrate-level vertex-anchored commitment vertex, with no separate non-minimal interaction terms.
- **Gauge potential.** The connection 1-form $A_\mu$; the gauge field as opposed to the gauge field strength.
- **Gauge-quotient.** The equivalence relation identifying structurally-identical gauge configurations $A_\mu \sim A_\mu - g^{-1}(\partial_\mu U)U^{-1}$ for $U(x)$ in the gauge group. Local symmetry is the substrate-level fact that this quotient is respected.

---

## 5. Substrate Class $\{C\}$

The forcing theorem applies to any substrate satisfying:

### C1. Participation graph + channel structure (Primitives P03 + P07)

The substrate supplies a participation graph $G = (V, E)$ with discrete channels at each locus, ontologically primitive.

### C2. Bandwidth with additivity (Primitive P04)

The substrate supplies non-negative bandwidth $b_K(u) \in \mathbb{R}_{\geq 0}$ on each channel, additive across disjoint channel decompositions.

### C3. Polarity (Primitive P09)

The substrate supplies a $U(1)$-valued angular variable $\pi_K(u) \in U(1)$ on each channel — the unique angular primitive in the substrate.

### C4. Time homogeneity (Primitive P13)

The substrate supplies a continuous time axis with homogeneous structure, supplying the dynamics of Paper #4.

### C5. Commitment events (Primitive P11)

The substrate supports discrete commitment events. **Commitments are vertex-anchored**: each commitment event occurs at a specific locus (a "vertex" in the participation-graph sense), and the rule-type's contribution to the commitment-rate enters through that vertex.

### C6. Rule-type primitive (Primitive P02)

The substrate supplies a structural primitive class of **rule-types** $\{\tau\}$ — kinds of channel structure admitting their own participation measures. The matter rule-type $\tau_m$ and the gauge rule-type $\tau_g$ are distinct elements of this class. Rule-types have **interface properties**: structural facts about a rule-type that govern its interaction with other rule-types via shared substrate content (vertices, vacuum kernels, gauge-quotient identifications).

### C7. Inherited results from Papers #1-#4

- **Paper #1**: complex-valued participation measure on each channel.
- **Paper #2**: Born rule for commitment outcomes.
- **Paper #3**: sesquilinear inner product on the participation manifold.
- **Paper #4**: linear unitary first-order Schrödinger dynamics with self-adjoint generator.

A reader who has not read Papers #1-#4 may take C7 as a definitional premise: the matter sector of the substrate carries a complex Hilbert-space arena with unitary time evolution.

### C8. No gauge structure as input

The forcing argument invokes only C1-C7. No gauge group, no covariant derivative, no field strength, no gauge invariance, no Yang-Mills Lagrangian, no fiber-bundle structure is assumed. These are produced by the forcing chain.

The argument additionally uses standard mathematical infrastructure: Lie-algebra theory (Frobenius classification of real division algebras was used in Paper #1; for non-Abelian gauge structure we additionally invoke the classification of compact simple Lie groups by Cartan); the Killing-form non-degeneracy criterion; the Jacobi identity for Lie brackets; and the standard differential-geometric machinery of connections and curvatures on principal bundles.

---

## 6. Alternative Encodings

### 6.1 Structural alternatives

**A1. No gauge fields.** No rule-type $\tau_g$ distinct from the matter rule-type $\tau_m$. Matter fields exist; gauge potentials do not. Interactions, if any, are non-gauge — direct contact terms or non-derivative couplings.

**A2. Global-only symmetry.** A rule-type $\tau_g$ exists, but its symmetry group acts globally only: $\psi \to U\psi$ with $U$ independent of position. Local gauge transformations $\psi \to U(x)\psi$ are not respected.

**A3. Non-connection-based transport.** Polarity transport along the participation manifold is path-independent (a global phase, not a connection), or path-dependent but in a way that fails the composition law for parallel transport.

**A4. Non-curvature-based field strength.** The observable field strength is defined other than as the commutator $[D_\mu, D_\nu]$ — for instance, as $\partial_\mu A_\nu$ alone (failing antisymmetry) or as $A_\mu A^\mu$ (failing gauge invariance).

**A5. Non-minimal coupling.** Matter-gauge interactions include extra non-minimal terms beyond $\partial \to D$ — Pauli moments inserted by hand, additional $F_{\mu\nu}F^{\mu\nu}\bar{\psi}\psi$ terms, contact interactions not derivable from a covariant derivative.

**A6. Real or quaternionic gauge structure.** Gauge potentials are real-valued (no phase content) or quaternion-valued ($SU(2)$-or-larger angular structure at the carrier level).

**A7. Non-U(1)/non-SU(n) phase transport.** Gauge groups outside the compact-simple-Lie class — discrete groups (e.g., $\mathbb{Z}_n$ at the gauge level), non-compact groups (e.g., $SL(n, \mathbb{R})$ as a gauge group), or non-Lie group structures.

### 6.2 Mainstream alternatives

**B1. Classical electromagnetism as postulate.** Maxwell's equations adopted as fundamental. Gauge potential and field strength are inputs; their existence and structure are not derived.

**B2. Yang-Mills as postulate.** The Yang-Mills Lagrangian and the gauge group adopted as fundamental. Non-Abelian structure is postulated by analogy with electromagnetism.

**B3. Fiber-bundle gauge theory as assumption.** Gauge fields are connections on a principal $G$-bundle. The bundle, the group $G$, and the connection are mathematical inputs.

**B4. Emergent gauge fields from condensed matter.** Gauge-field-like structures emerge as effective descriptions of microscopically non-gauge systems (e.g., $\mathbb{Z}_2$ gauge theory in spin liquids, emergent photons in dimer models). The microscopic substrate is non-gauge; gauge structure is emergent in a long-wavelength limit.

**B5. Hidden-variable gauge-like models.** Hidden-variable formulations reproducing gauge predictions via non-local hidden variables, without committing to a substrate-level gauge structure.

**B6. Nonlocal gauge potentials.** Action-at-a-distance reformulations (e.g., Aharonov-Bohm-class theories) that retain observable predictions but reject the local-potential ontology.

---

## 7. Constructive Necessity

The argument establishes the gauge-field-as-rule-type structure in six steps. Each step traces to a substrate condition; no input from gauge field theory or fiber-bundle geometry is assumed.

### 7.1 Rule-types and their participation measures

The substrate primitive class of rule-types (C6) supplies a discrete index $\tau \in \{\tau_m, \tau_g, \ldots\}$. Each rule-type $\tau$ has its own channel-and-locus structure $\mathcal{K}_\tau(u)$ and its own participation measure $P_K^{(\tau)}(u)$ on that structure. Paper #1's result applies separately to each rule-type: the unique amplitude carrier is the complex-valued participation measure $\sqrt{b_K^{(\tau)}}\,e^{i\pi_K^{(\tau)}}$.

The matter rule-type $\tau_m$ carries the matter wavefunction $\psi(u) := \sum_K P_K^{(\tau_m)}(u)$. The gauge rule-type $\tau_g$ carries a participation measure on its own channel structure; we denote it $A_\mu^{(\tau_g)}$ — the **gauge potential**.

That a gauge rule-type *exists* (rather than being merely admissible) follows from the substrate-level existence of multiple rule-types as a primitive structural fact (C6). Whether *which* specific gauge group it admits — U(1), SU(2), SU(3), or other — is inherited from value-layer commitments; the forcing theorem applies to whichever specific choice the substrate realizes.

### 7.2 Polarity transport along the participation manifold

Polarity (C3) is a $U(1)$-valued angular variable on each channel at each locus. To compare polarity at distinct loci $u$ and $u'$, the substrate must provide a **transport rule** along paths $\gamma$ on the participation manifold connecting $u$ to $u'$.

Two structural facts constrain the transport rule:

- **Continuity (from C4).** Time homogeneity supplies a continuous parameter along time-like paths; spatial homogeneity (the participation-graph translation invariance underwriting Paper #4's continuum regime) supplies the same along spatial paths. Polarity transport must therefore be continuous along smooth paths.
- **Bandwidth preservation (from C2).** Transport must preserve the substrate-level bandwidth content of each channel; bandwidth is a non-negative invariant of each channel-locus pair, and parallel transport cannot create or destroy bandwidth in the absence of commitment events (C5).

Under these constraints, parallel transport of the matter participation measure $\psi$ along a path $\gamma$ from $u$ to $u'$ is uniquely (up to gauge fixing) a path-dependent unitary action on $\psi$:
$$
\psi(u') = U_\gamma\,\psi(u), \qquad U_\gamma \in U(1) \text{ or non-Abelian generalization}.
$$
The unitarity follows from bandwidth preservation; the path-dependence is the structural source of the connection.

### 7.3 Connection from path-dependence of transport

The transport rule along an infinitesimal path $u \to u + dx^\mu$ is parameterized by a Lie-algebra-valued one-form $A_\mu(u)$:
$$
U_{u \to u+dx} = \mathbb{1} + ig A_\mu(u) dx^\mu + O(dx^2),
$$
where $g$ is a coupling constant (inherited). The object $A_\mu$ is the **gauge potential** — the participation measure of $\tau_g$.

That $A_\mu$ takes values in the Lie algebra of a compact simple Lie group follows from three substrate-level facts:

- **U(1) phase content of polarity (C3).** Polarity is $U(1)$-valued; the transport must respect this at the matter-sector level. For Abelian gauge structure, $A_\mu$ is real-valued and the gauge group is U(1).
- **Multi-channel rule-type composition (C6).** When matter has multiple channels indexed by an internal label (e.g., color, flavor), the transport rule must act on all channels coherently. This forces the gauge group to admit non-Abelian structure: the composition rule for multi-channel transport requires a Lie bracket, which is non-trivial in the non-Abelian case.
- **Jacobi identity (mathematical necessity).** Any associative composition of infinitesimal transports satisfies the Jacobi identity for the underlying Lie bracket. Combined with the Killing-form non-degeneracy required for the gauge-quotient invariance below, this restricts the admissible gauge groups to compact simple Lie groups (and direct products thereof).

The connection $A_\mu$ is therefore Lie-algebra-valued, with the algebra forced to be a compact simple Lie algebra. The specific group (which compact simple Lie group) is inherited from value-layer commitments.

### 7.4 Curvature from the commutator of transports

Consider transport around an infinitesimal closed loop in the participation manifold, spanned by $dx^\mu$ and $dy^\nu$. The two paths $u \to u + dx \to u + dx + dy$ and $u \to u + dy \to u + dx + dy$ differ by a phase factor $\Omega$ whose first non-trivial order is
$$
\Omega = \mathbb{1} + ig\,(\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu])\,dx^\mu dy^\nu + O(dx^3).
$$
The bracketed quantity is the **field strength**
$$
F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu] = -\frac{i}{g}[D_\mu, D_\nu],
$$
with $D_\mu := \partial_\mu + igA_\mu$ the covariant derivative.

The field strength is therefore the commutator of covariant derivatives — equivalently, the curvature 2-form of the connection. Its form is forced by the substrate-level structure of polarity transport plus the Lie-algebra composition rule (§7.3); no separate axiom is required.

Gauge invariance of $F_{\mu\nu}$: under a local gauge transformation $A_\mu \to UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$, the curvature transforms covariantly: $F_{\mu\nu} \to U F_{\mu\nu} U^{-1}$. The trace $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ is therefore gauge-invariant — the substrate-level observable.

### 7.5 Minimal coupling from vertex-anchored commitment

The substrate-level commitment primitive (C5) is **vertex-anchored**: each commitment event occurs at a specific locus. The rule-type's contribution to the commitment-rate enters through that vertex.

For the matter-gauge interaction, the vertex is the locus at which matter participation interacts with gauge participation. The structural content of the vertex is forced to be a single bilinear coupling between matter and gauge participation measures, of the form $\bar{\psi}\,\gamma^\mu\,T^a\,\psi\,A_\mu^a$ (in the relativistic case) or its non-relativistic analog. The factor $T^a$ is the Lie-algebra generator selected by the matter rule-type's internal-symmetry content.

This is **minimal coupling**: matter couples to gauge via the single substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu^a T^a$. No separate Pauli term, no $F_{\mu\nu}F^{\mu\nu}\bar{\psi}\psi$ contact term, no non-derivative coupling. The substrate-level vertex is unique: the commitment primitive supplies one vertex per matter-gauge pair, and the vertex's bilinear structure is fixed by the rule-type composition rule.

Non-minimal-coupling alternatives would require multiple vertices, or non-bilinear vertex structures, neither of which is supplied by C5. Non-minimal couplings appear in *effective* field theories as integrated-out contributions from heavier sectors, but at the substrate level the rule-type interaction is minimal-coupling-only.

### 7.6 Local gauge-quotient invariance

The gauge-quotient invariance — local symmetry — is the **interface property** of the rule-type $\tau_g$: the substrate does not distinguish between structurally-identical gauge configurations.

Two configurations $A_\mu(u)$ and $A_\mu'(u) = UA_\mu U^{-1} - (i/g)(\partial_\mu U)U^{-1}$ with $U(u)$ a local gauge transformation give the same observable predictions: the same field strength (up to the covariant transformation), the same gauge-invariant action, the same Born-rule commitment probabilities. The substrate-level rule-type $\tau_g$ is therefore identified with its gauge-equivalence class, not with any single representative configuration.

That this quotient is *local* (with $U(u)$ varying from point to point) and not global (with $U$ position-independent) follows from the substrate-level locality of the participation graph (C1): channels at different loci are structurally independent, so polarity-redefinitions at different loci are also independent. A global-only symmetry would require the substrate to distinguish loci by their absolute polarity values, which violates the substrate-level translation invariance underwriting C3.

The composite result: a gauge-field-class rule-type with non-Abelian-capable group, vertex-anchored minimal-coupling vertex, commutator-defined field strength, and local gauge-quotient invariance is forced.

---

## 8. Exclusion Arguments

### 8.1 A1 — No gauge fields

A substrate satisfying C6 (rule-type primitive supplying multiple rule-types $\{\tau_m, \tau_g, \ldots\}$) but lacking $\tau_g$ contradicts C6: the rule-type primitive supplies the gauge rule-type as one element of its class. Equivalently, polarity transport on the participation manifold (§7.2-§7.3) cannot be defined without a connection, and the connection *is* the gauge potential — its existence is structurally tied to transport consistency.

### 8.2 A2 — Global-only symmetry

A global-only symmetry would require all polarity-redefinitions across the participation manifold to be tied together by a single $U \in U(1)$ (or non-Abelian analog). This contradicts C1's structural independence of channels at distinct loci: there is no substrate-level mechanism for enforcing a global tying of polarity values across the manifold. The locality of polarity is forced by the locality of the participation graph.

### 8.3 A3 — Non-connection-based transport

If polarity transport were path-independent (a global phase) or path-dependent but not satisfying the composition law $U_{\gamma_1 \circ \gamma_2} = U_{\gamma_1} U_{\gamma_2}$, then transport around closed loops would fail to compose consistently. Bandwidth-preserving (C2), continuous (C4), unitary transport on a complex carrier (C7/Paper #1) forces the composition law; the transport rule is a connection in the standard differential-geometric sense.

### 8.4 A4 — Non-curvature-based field strength

If the observable field strength were defined other than as the commutator $[D_\mu, D_\nu]$, gauge-invariance would fail: the bare derivative $\partial_\mu A_\nu$ is not gauge-invariant; the bilinear $A_\mu A^\mu$ transforms inhomogeneously. The unique gauge-invariant (up to covariant transformation) object built from $A_\mu$ at first order in derivatives is the commutator. The substrate-level requirement that observables respect the gauge-quotient invariance (§7.6) forces the field strength to be the curvature.

### 8.5 A5 — Non-minimal coupling

The vertex-anchored commitment primitive (C5) supplies a single vertex per matter-gauge rule-type pair. Non-minimal couplings would require either additional substrate-level vertices (violating C5's structural single-vertex content per rule-type pair) or non-bilinear vertex structure (violating the rule-type composition rule of C6, which produces bilinear matter-gauge couplings).

Non-minimal couplings observed in effective field theories (e.g., Pauli moments at low energies in heavy-quark physics) arise from integrated-out heavy sectors and are not substrate-level commitments. At the substrate level, the coupling is minimal.

### 8.6 A6 — Real or quaternionic gauge structure

Real-valued gauge potentials lack the phase content required by polarity transport (C3); the substrate's $U(1)$ polarity primitive cannot be carried by real-valued transport. Paper #1's exclusion of real-valued amplitude carriers applies directly: real-valued $A_\mu$ fails to faithfully represent the polarity-transport content.

Quaternionic gauge potentials would carry $SU(2)$-or-larger angular structure at the carrier level, exceeding what polarity supplies. Paper #1's exclusion of quaternionic carriers (no primitive-level basis for the $U(1) \subset SU(2)$ embedding choice; surplus angular content unsupported by the substrate) applies. Non-Abelian gauge structure at the *group* level is permitted; non-quaternionic *carriers* are required.

### 8.7 A7 — Non-U(1)/non-SU(n) phase transport

Discrete gauge groups ($\mathbb{Z}_n$ at the gauge level) fail the continuity requirement of C4: polarity transport along a continuous path must produce a continuous family of unitary transformations, which discrete groups cannot supply.

Non-compact gauge groups (e.g., $SL(n, \mathbb{R})$) fail the Killing-form non-degeneracy required for the bilinear gauge-invariant action $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ to be positive-definite. Non-positive-definite actions violate the bandwidth-non-negativity (C2) that propagates to the gauge sector's vacuum-kernel structure.

Non-Lie group structures (e.g., quasigroups, loops) fail the associativity required for transport-rule composition; the connection construction of §7.3 requires Lie-algebra structure.

The admissible class is therefore compact simple Lie groups (and their direct products), which is exactly the class of standard gauge theories.

### 8.8 B1, B2 — Classical electromagnetism / Yang-Mills as postulate

Maxwell's equations and the Yang-Mills construction are taken as fundamental in the postulate-based formulations. Under the substrate-conditions test, these are *downstream* of the forcing chain: the gauge-field rule-type $\tau_g$ with its structural content (§7) produces Maxwell or Yang-Mills as the dynamical content. They are not alternative substrate-level commitments; they are consequences of the substrate-level rule-type structure.

If the substrate forces the gauge-field rule-type, then Maxwell's equations and the Yang-Mills equations become structural consequences. If the substrate did not force the rule-type, those equations would not be derivable. Either way, they are not in the alternative-encodings space; they live downstream.

### 8.9 B3 — Fiber-bundle gauge theory as assumption

The fiber-bundle formalism is a *reformulation* of standard gauge theory in differential-geometric language. The principal $G$-bundle, the group $G$, and the connection form are mathematical objects that ED's forcing chain *produces*: the participation manifold acquires a connection structure under polarity transport (§7.3); the group $G$ is the rule-type's gauge group (inherited from value-layer); the bundle structure is the geometric expression of the rule-type's interface property.

Fiber-bundle theory is therefore the appropriate mathematical *language* for the forced result, not an alternative to it.

### 8.10 B4 — Emergent gauge fields from condensed matter

Spin-liquid and dimer-model gauge fields are emergent at long wavelengths from non-gauge microscopic Hamiltonians. Under the substrate-conditions test, these systems are *higher-level* effective descriptions: the microscopic Hamiltonian itself is a participation-graph realization at the substrate level, and the emergent gauge field is a coarse-grained signature of a substrate-level rule-type that becomes visible only at long wavelengths.

Emergent gauge theory and substrate-level gauge theory are therefore consistent rather than competing: the substrate forces the rule-type structure; condensed-matter realizations exhibit different specific gauge groups (e.g., $\mathbb{Z}_2$ in some spin liquids) than the Standard Model. The non-Abelian-capable group structure admits both.

### 8.11 B5 — Hidden-variable gauge-like models

Hidden-variable formulations reproducing gauge predictions via non-local hidden variables do not derive the gauge structure from a substrate; they postulate it alongside hidden-variable supplementation. Under the substrate-conditions test, these are downstream interpretations of the forced gauge-field structure (analogously to Bohmian mechanics being downstream of the forced Schrödinger equation in Paper #4). Not in the alternative-encodings space.

### 8.12 B6 — Nonlocal gauge potentials

Action-at-a-distance reformulations (Wheeler-Feynman-style absorber theories, certain Aharonov-Bohm interpretations) retain observable predictions but reject the local-potential ontology. Under the substrate-conditions test, these are reformulations within the same equivalence class of theories that ED forces: the gauge potential is a substrate-level participation measure with local structure; observable predictions match because both formulations sit in the same gauge-quotient class. Nonlocal reformulations are not substrate-level alternatives; they are equivalent descriptions of the forced structure.

### 8.13 Summary of exclusions

| Alternative | Violates | Reason |
|---|---|---|
| A1 no gauge fields | C6 | Rule-type primitive supplies $\tau_g$ as element of the rule-type class. |
| A2 global-only symmetry | C1 | Channel locality forces local polarity-redefinition independence. |
| A3 non-connection transport | C2, C4 | Bandwidth-preserving continuous unitary transport satisfies the composition law. |
| A4 non-curvature field strength | §7.6 gauge-quotient | Only the commutator is gauge-invariant at first derivative order. |
| A5 non-minimal coupling | C5 | Vertex-anchored commitment supplies a single bilinear vertex per matter-gauge pair. |
| A6 real/quaternionic carrier | C3 (Paper #1) | Excluded at carrier level: real fails phase content, quaternionic has surplus $SU(2)$ structure. |
| A7 non-U(1)/non-SU(n) groups | C2, C4, §7.3 Jacobi | Discrete fails continuity, non-compact fails Killing positivity, non-Lie fails associativity. |
| B1 classical EM postulate | not in space | Downstream of forced rule-type structure; consequence rather than alternative. |
| B2 Yang-Mills postulate | not in space | Same as B1 with non-Abelian group; downstream consequence. |
| B3 fiber-bundle gauge theory | reformulation | Mathematical language for the forced result, not an alternative substrate. |
| B4 emergent gauge fields | not in space | Higher-level coarse-grained signature of substrate-level rule-type. |
| B5 hidden-variable models | not in space | Downstream interpretation of forced gauge structure. |
| B6 nonlocal gauge potentials | reformulation | Equivalent description in the same gauge-quotient class. |

**The gauge-field-as-rule-type structure (T17) is the unique survivor.**

---

## 9. Falsifiers and Empirical Exposure

### 9.1 Empirical falsifier

The empirical falsifier is identical to the empirical falsifier of standard gauge field theory: any observed violation of minimal coupling, local gauge invariance, or the commutator-defined field strength.

Specific constraints:

- **Anomalous magnetic moments**: precision measurements of the electron $g - 2$ and muon $g - 2$ agree with QED to ~$10^{-12}$ relative precision (electron) and ~$10^{-9}$ (muon), with all observed contributions accounted for by minimal-coupling QED + higher-order radiative corrections.
- **Tests of local U(1) gauge invariance**: experimental bounds on photon mass ($< 10^{-18}$ eV) and on possible Lorentz-violating photon couplings constrain gauge-invariance violations to extraordinary precision.
- **Aharonov-Bohm experiments**: the holonomy structure of gauge transport (§7.4) is directly measured in AB-type interference experiments; observed phase shifts agree with $\exp(i\oint A_\mu dx^\mu)$.
- **Non-Abelian gauge tests**: precision tests of the electroweak sector (W and Z masses, $\sin^2\theta_W$ measurements, $W$ helicity in pion decay) constrain non-Abelian gauge structure to high precision.

If any of these were experimentally violated — if non-minimal coupling, broken local invariance, or non-commutator field strengths were observed — the substrate-level forcing would be refuted along with standard gauge theory.

### 9.2 Structural falsifier

Construct a substrate satisfying C1-C8 (channel-primitive participation graph, bandwidth additivity, $U(1)$ polarity, time homogeneity, vertex-anchored commitment, rule-type primitive, Papers #1-#4 inherited results) but supporting no gauge-field rule-type, or supporting one with non-curvature field strength, or non-minimal coupling, or non-local symmetry, that survives the exclusion arguments of §8.

The author's claim is that no such substrate exists; each alternative is dispatched by a specific substrate-condition violation. A reader who exhibits a counterexample refutes the present paper.

### 9.3 Downstream exposure

Three immediate exposures of the present forcing:

**Electromagnetism.** The Maxwell equations $\partial_\mu F^{\mu\nu} = J^\nu$ and $\partial_{[\rho} F_{\mu\nu]} = 0$ follow from the variational principle applied to the gauge-invariant action $\mathcal{L} = -\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu} + J^\mu A_\mu$ on the substrate-derived gauge potential. Every electromagnetic experiment — from Coulomb's law to laser interferometry to synchrotron radiation — tests the resulting dynamics.

**Yang-Mills.** The non-Abelian gauge sector of the Standard Model — SU(3) QCD for strong interactions, SU(2)×U(1) for electroweak — is realized as the substrate-level rule-type structure with the value-layer-inherited specific gauge group. Every hadron-collider experiment, every test of QCD running coupling, every electroweak precision measurement, tests this realization.

**Berry phase.** Holonomy around closed loops in parameter space — the geometric Berry phase — is the substrate-level signature of the gauge connection in adiabatic quantum mechanics. AB experiments, molecular Berry-phase measurements, and topological-phase experiments in condensed matter test the substrate-derived connection structure.

The empirical exposure of this paper is therefore the entirety of gauge-coupled phenomenology in physics — electromagnetism, the Standard Model, geometric-phase experiments.

---

## Appendix A — Derivation Chain and Glossary

### A.1 Connection from polarity transport

Polarity (C3) is a $U(1)$-valued angular variable on each channel at each locus. Define the parallel-transport operator $U_\gamma: \mathcal{H}_u \to \mathcal{H}_{u'}$ along a smooth path $\gamma$ from $u$ to $u'$ on the participation manifold. Three substrate-level constraints:

1. **Unitarity** (from C2 bandwidth preservation + Paper #3 inner product): $U_\gamma^\dagger U_\gamma = \mathbb{1}$.
2. **Continuity** (from C4 time homogeneity + spatial homogeneity): $\gamma \mapsto U_\gamma$ continuous in path topology.
3. **Composition** (from path concatenation $\gamma_1 \circ \gamma_2$): $U_{\gamma_1 \circ \gamma_2} = U_{\gamma_1} U_{\gamma_2}$.

These constraints define a connection on the participation manifold. For an infinitesimal path $u \to u + dx^\mu$:
$$
U_{u \to u + dx} = \mathbb{1} + ig A_\mu(u) dx^\mu + O(dx^2),
$$
with $A_\mu(u)$ a Lie-algebra-valued one-form — the **gauge potential**. Unitarity at infinitesimal order requires $A_\mu^\dagger = A_\mu$ (Hermitian connection). Path-dependence at second order produces the curvature derived in A.2.

### A.2 Curvature from commutator of transports

Compare two paths from $u$ to $u + dx + dy$: (i) $u \to u + dx \to u + dx + dy$, (ii) $u \to u + dy \to u + dx + dy$. The transports are:

(i) $U_2^{(2)} U_1^{(1)} = [\mathbb{1} + igA_\mu(u + dx)dy^\mu] [\mathbb{1} + igA_\nu(u)dx^\nu]$
(ii) $U_2^{(1)} U_1^{(2)} = [\mathbb{1} + igA_\nu(u + dy)dx^\nu] [\mathbb{1} + igA_\mu(u)dy^\mu]$

Subtracting at second order:
$$
U_2^{(2)} U_1^{(1)} - U_2^{(1)} U_1^{(2)} = ig\,[\partial_\mu A_\nu - \partial_\nu A_\mu + ig(A_\mu A_\nu - A_\nu A_\mu)]\,dx^\nu dy^\mu = ig F_{\mu\nu} dx^\nu dy^\mu,
$$
with
$$
F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu].
$$
Equivalently, $F_{\mu\nu} = (1/ig)[D_\mu, D_\nu]$ with $D_\mu = \partial_\mu + igA_\mu$. The field strength is the curvature of the connection — the obstruction to commuting infinitesimal transports.

### A.3 Minimal coupling from vertex-anchored commitment

The substrate-level commitment primitive (C5) is vertex-anchored: each commitment event occurs at a specific locus. The matter-gauge interaction enters through the substrate-level vertex, which is structurally a single bilinear coupling between matter and gauge participation measures.

In the relativistic case, the matter rule-type $\tau_m$ has Dirac-spinor structure (forced by the ED program's Arc R), and the matter-gauge vertex is $\bar{\psi}\gamma^\mu T^a \psi A_\mu^a$. Substituting into the matter Schrödinger / Dirac equation gives the minimal-coupling substitution $\partial_\mu \to D_\mu = \partial_\mu + igA_\mu^a T^a$.

In the non-relativistic case (Paper #4 scope), the matter-gauge vertex enters the Hamiltonian as $\hat{H} \to \hat{H} + g\hat{A}_\mu \hat{j}^\mu$ with $\hat{j}^\mu$ the matter current. The vertex is unique: C5 supplies a single vertex per matter-gauge rule-type pair, and the bilinear structure is fixed by rule-type composition.

### A.4 Glossary

- **A_\mu (gauge potential).** The participation measure of the gauge rule-type $\tau_g$; a Lie-algebra-valued one-form on the participation manifold.
- **Bandwidth $b_K(u)$.** Primitive non-negative real-valued substrate quantity on each channel.
- **Commutator.** $[A, B] = AB - BA$, the antisymmetric product of operators.
- **Compact simple Lie group.** A Lie group that is compact, connected, and has no non-trivial closed normal subgroups. U(1) (Abelian), SU(2), SU(3), and the exceptional groups are examples.
- **Connection.** A rule for parallel transport along paths on the participation manifold; equivalently, the gauge potential $A_\mu$.
- **Covariant derivative.** $D_\mu = \partial_\mu + igA_\mu^a T^a$; the gauge-invariant derivative replacing $\partial_\mu$.
- **Curvature.** The 2-form $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]$; the commutator of covariant derivatives.
- **FORCED.** Derived from substrate primitives + standard mathematics with no additional structural commitments.
- **Gauge group $G$.** The compact simple Lie group acting on the matter rule-type's internal indices. U(1), SU(2), SU(3) in the Standard Model.
- **Gauge potential $A_\mu$.** See "A_\mu".
- **Gauge-quotient.** Equivalence class of gauge configurations $A_\mu \sim A_\mu - g^{-1}(\partial_\mu U)U^{-1}$; the substrate identifies all members of the same class.
- **Holonomy.** Phase factor accumulated by transport around a closed loop: $\exp(i\oint A_\mu dx^\mu)$ for Abelian, path-ordered exponential for non-Abelian.
- **INHERITED.** Quantitative content (specific gauge group, coupling values, kernel parameters) not derived in this paper.
- **Killing form.** A bilinear form on a Lie algebra, $K(X, Y) = \text{tr}(\text{ad}_X \text{ad}_Y)$; non-degenerate on semisimple Lie algebras.
- **Minimal coupling.** Matter-gauge interaction via $\partial_\mu \to D_\mu$; structural single-vertex coupling.
- **Participation measure.** Complex-valued amplitude carrier on each channel (Paper #1).
- **Polarity $\pi_K(u)$.** $U(1)$-valued angular primitive on each channel at each locus.
- **Rule-type.** Substrate primitive class of channel structure; matter and gauge are distinct rule-types.
- **Vertex.** A locus on the participation graph at which a commitment event occurs; the substrate-level "interaction point."
- **Vertex-anchored.** Property of commitment events: each occurs at a specific locus, with the rule-type's contribution entering through that vertex.

### A.5 Source-repository citations (for ED-internal readers)

- `papers/Gauge_Fields_Theorem_17/paper_gauge_fields_theorem_17.md` — publication-grade T17 paper (predecessor genre).
- `arcs/arc-Q/19_synthesis_memo_02_theorem_17.md` — Arc Q synthesis memo establishing T17 as FORCED-unconditional.
- `arcs/arc-Q/17_synthesis_memo_00_scoping.md` and `18_synthesis_memo_01_global_integration.md` — synthesis prerequisites.
- `arcs/arc-Q/arc_q_synthesis.md` — Arc Q overview.
- `walkthroughs/from_primitives_to_gauge_fields.md` — public-facing walkthrough.
- `theorems/T17.md` — theorem-level index entry; status FORCED-unconditional, ratified 2026-04-27.

These are *not* required reading for the present paper.

---

*End of Paper #5.*
