# Substrate-Evaluation — Folder Guide *(cold-reader consolidation papers)*

**What this folder is.** Standalone, **cold-reader-accessible** papers that each package one ED result for an outside reader — the consolidation layer of the corpus. They span the minimal ontology and the layers program, the coarse-graining "which continuum shadow does the substrate cast" results (Maxwell, transport-not-diffusion, non-Gaussianity), the determinability boundaries (A1/A2), charge topology (B4), the gauge structure, the parity verdict, the quantum-logic keystone, phase coherence, and the finite-memory (primes) ceiling.

**State** *(authoritative source: `event-density/docs/ED_Research_Targets.md`; tiers cross-checked against the map, not each paper's own summary)*:
- **Most are consolidations of CLOSED results** — A1 (channel-capacity zero), A2 (emergent boundary), B4 (charge topological skeleton), Primes (finite-memory ceiling), the CoarseGrain trilogy (Maxwell/transport/non-Gaussianity), the layers capstone.
- **Two honest edges to read carefully** (the map overrides the paper's framing):
  - **The Quantum-Logic Keystone (Gleason)** — the ℂ-field selection and Born non-contextuality are grounded, but the **inner-product / channel-orthogonality step is NOT closed** (#8b: three derivation routes fail). Read it as *partial*, not a completed reconstruction.
  - **The Parity Wall** — this is the *honest verdict*: ED gives the matter/antimatter reference (C) natively but **does not derive the weak force's chirality** (P). That is consistent with the open matter frontier (#2b); it is a "what ED does not have" result, correctly stated. **Its verdict is now superseded (in tier, not direction) by *The Clean Substrate Is Vector*.**
  - **The Clean Substrate Is Vector** (successor to *The Parity Wall*) — hardens the conditional "vector by default" into a **theorem**: the parity-clean commitment map has an even determinant, so its point-gap winding is zero for **every** channel-count, hence the clean transport is vector and any parity violation is **necessarily spontaneous**. Grounds the chirality operator (`γ⁵ = arrow × spontaneous orientation`) and names the casting (which force is chiral) as inherited representation-theory (`SU(2)` pseudoreal). Same direction as the Wall (P inherited), one tier firmer.
- **The Gauge Structure** paper carries the #2b open frontier (SU(N) form + non-abelian + F² + mass-gap grounded; the `{1,2,3}` multiplicities and anomalies open).

**Tier key:** `Derived` · `Grounded` (conditional/structural) · `Measured` (simulation-backed) · `Wall` (a proven / honest limit — the order ED does not reach) · `Synthesis` · `Partial / Open` (grounded but with a named unclosed step).

---

## The spine — read in this order

1. **[Commitment and Participation — The Minimal Ontology](Paper_CommitmentAndParticipation_MinimalOntology.md)** — what ED *is*, minimally.
2. **[The Arrow Sorts the Continuum](Paper_TheArrowSortsTheContinuum.md)** — the layers capstone: one primitive (the arrow) sorts every continuum law into three classes.
3. **[Knots, Not Crystals](Paper_BlindnessInvariant_KnotsNotCrystals.md)** — the order ED does not have, and the order that matters.

---

## Papers by theme

### Ontology & the layers program
| Paper | Result | Tier |
|---|---|---|
| [Commitment and Participation (Minimal Ontology)](Paper_CommitmentAndParticipation_MinimalOntology.md) | the minimal ontology — the substrate in two words | Synthesis / Grounded |
| [The Arrow Sorts the Continuum](Paper_TheArrowSortsTheContinuum.md) | one primitive sorts continuum laws into structure-making / erasing / preserving | Synthesis (breaker-passed) |
| [Knots, Not Crystals](Paper_BlindnessInvariant_KnotsNotCrystals.md) | ED lacks crystalline order but has topological (knot/link) order — the order that matters | Grounded |

### Coarse-graining → continuum (which shadow?)
| Paper | Result | Tier |
|---|---|---|
| [From Worldlines to the Canonical PDE](Paper_CanonicalPDEChannels_BottomUp.md) | the three channels: coherent (Maxwell), transport, disorder — a bottom-up ledger | Grounded |
| [The Continuum Limit: a Kinetic Lattice-Gas](Paper_Continuum_KineticLatticeGas.md) | ED's certified continuum is a kinetic lattice-gas (ballistic transport), **not** a diffusion PDE | Grounded / Measured |

### Determinability boundaries & charge
| Paper | Result | Tier |
|---|---|---|
| [Common Cause, Not Channel (A1)](Paper_CommonCauseNotChannel_A1.md) | the determinability boundary: controlled channel capacity is exactly zero (ED locality) | Derived |
| [Grown, Not Installed (A2)](Paper_GrownNotInstalled_A2.md) | an emergent decoupling boundary reproduces exact channel-zero | Grounded / Measured |
| [The Topological Skeleton of Charge (B4)](Paper_ChargeAsTopology_B4.md) | quantized winding `w∈ℤ` + integral Gauss law on the graph (skeleton closed; local Coulomb open) | Grounded (Coulomb Open) |

### Gauge, matter, parity (the #2b frontier)
| Paper | Result | Tier |
|---|---|---|
| [The Gauge Structure of ED](Paper_GaugeStructure_FromChannelTransport.md) | SU(N) form, non-abelian gauging, the F² action, the mass-gap mechanism from channel transport | Grounded (`{1,2,3}` / anomalies Open, #2b) |
| [The Parity Wall](Paper_ParityWall_ChiralityVerdict.md) | ED gives matter/antimatter (C) natively but **not** the weak force's chirality (P) — the honest verdict | **Wall** (chirality not derived, #2b); *verdict superseded by the Clean-Substrate paper below* |
| [The Clean Substrate Is Vector](Paper_CleanSubstrateVector_ParitySpontaneous.md) | grounds `γ⁵ = arrow × spontaneous orientation`; **theorem:** the parity-clean transport is vector for every channel-count, so parity violation is necessarily spontaneous; casting inherited (rep-theory) | **Wall + theorem** (supersedes The Parity Wall's verdict tier, #2b) |

### QM keystone & coherence
| Paper | Result | Tier |
|---|---|---|
| [The Quantum-Logic Keystone (Gleason)](Paper_QuantumLogicKeystone_GleasonReconstruction.md) | reconstructs the ℂ-field + Born non-contextuality; **the inner-product/orthogonality step is not closed** | **Partial / Open** (#8b) |
| [Phase Coherence in ED](Paper_PhaseCoherence_P12Coh.md) | attractive sign, finite reach, and substrate disorder in the P12 coherence term | Grounded |
| [The Sign of the Binder (V5 Attraction)](Paper_V5AttractiveSign_P12Coh.md) | V5's attractive sign derived from substrate coherence | Grounded |
| [The Relational Tick](Paper_RelationalTick_v1.md) | local clocks without a universal one | Grounded |

### Limits & holography
| Paper | Result | Tier |
|---|---|---|
| [Template, Not Escape (Primes)](Paper_FiniteMemoryCeiling_Primes.md) | finite-memory ED saturates the prime-counting template but provably not the parity layer (Sarnak barrier) | **Wall** (a proven limit) |
| [The Area Law Is the Edge Count](Paper_AreaLawIsTheEdgeCount.md) | holographic entropy = the count of straddling cross-chain (V5) edges | Grounded |

*(One plain-language companion `thearrowsortsthecontinuum_plain_language.txt` accompanies the layers capstone. The two honest edges — the Gleason inner-product (#8b) and the parity/chirality wall (#2b) — are tiered against the research map, not the papers' own framing.)*
