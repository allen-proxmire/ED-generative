# P04 — Bandwidth (non-negative additive scalar, four-band partition)

**Canonical primitive of the ED Generative System.**
**Position paper reference:** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1.3.

---

## Canonical statement

Each channel $K$ at each locus $u$ carries a real-valued non-negative quantity $b_K(u) \geq 0$, additive under channel decomposition. Bandwidth further decomposes into four mutually orthogonal substrate-level bands:

- **Internal** band: carries the channel's own coherent participation content.
- **Adjacency** band: carries content shared with neighboring loci via P05 polarity-transport.
- **Environmental** band: carries content coupled to the substrate environment (decohering channels).
- **Commitment-reserve** band: carries the budget consumed by P11 commitment events.

The four-band partition (P04 §1.5) supplies the sesquilinear inner-product structure on the participation manifold (Paper 003).

## Audit verdict

LOAD-BEARING. Bandwidth supplies the magnitude side of the complex polar participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (Paper 001), the Born-rule probability weights $\text{Prob}(K \mid u) = b_K/\sum b_{K'}$ (Paper 002), and the Tsirelson-bound saturation via orthogonal-band algebra (Paper 003).

## Underlying concept treatments

- `concepts/participation_bandwidth.md` — the graded scalar measure of participation; turns the relational fact (P02) into something with quantity.
