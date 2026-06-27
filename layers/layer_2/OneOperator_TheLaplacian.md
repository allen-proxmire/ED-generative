# Layer-2's Decorrelation Is One Operator — the Gradient-Flux Laplacian

**Result.** Every layer-2 *decorrelation* term across the map is the **same operator**: the gradient-flux
Laplacian $\nabla\!\cdot\!(M\nabla\varphi)$. Diffusion, Navier–Stokes viscosity, and the Ricci/gravity
metric-smoothing are three instances of it; Gaussianity is its heat-**kernel** (the distribution the operator
drives any field toward). And the operator is not a coincidence — it is **forced**: the second coarse-graining
imposes isotropy + locality + conservation, and $\nabla\!\cdot\!(M\nabla\varphi)$ is the *unique* operator with
those properties. One mechanism, forced, wearing the whole dissipative column. **But this is the
*decorrelation* sub-type only** — the *constraint* sub-type (incompressibility, conservation laws) is a
genuinely separate kind of add, not this operator.

## The instances (all grounded in measured rules)

| layer-2 term | form | grounding |
|---|---|---|
| **Diffusion** | $\partial_t\rho = D\nabla^2\rho = \nabla\!\cdot\!(D\nabla\rho)$ | measured (Green–Kubo recovery) |
| **NS viscosity** | $\nu\nabla^2 u = \nabla\!\cdot\!(\nu\nabla u)$ | mechanism = the same velocity decorrelation as diffusion |
| **Ricci / gravity smoothing** | $D\nabla^2 b = \nabla\!\cdot\!(D\nabla b)$ | measured (GR-III bandwidth rule, 2D/3D) |
| **Gaussianity** | the heat **kernel** $e^{t\nabla^2}$ is Gaussian | measured (door-#1 walker density is Gaussian = Laplacian-smoothed) |

The first three are the *operator*; the fourth is its *fingerprint*. The layer-1 deposit field stays
**non-Gaussian** (door #2) precisely because it does **not** undergo this Laplacian smoothing — it keeps the
committal phase structure. So "Gaussian vs not" maps exactly onto "Laplacian-smoothed vs not." That is the
operator and its absence, measured on both sides.

## Why it is forced (not a coincidence)

A dissipative term produced by the second coarse-graining must be **isotropic** (the decorrelation has no
preferred direction — that is what decorrelation *means*), **local** (the CG window is finite), and
**conservation-respecting** (it moves the field around, it does not create it — a divergence of a flux). The
*unique* second-order operator that is isotropic, local, and in divergence-of-a-flux form is
$\nabla\!\cdot\!(M\nabla\varphi)$. So diffusion, viscosity, and Ricci-smoothing are "the same" not by analogy
but by **uniqueness**: they are all *the* isotropic-local-conservative dissipative operator, differing only in
what field $\varphi$ it acts on (density, momentum, metric) and in the mobility $M$. The second CG manufactures
the isotropy and locality; those force the Laplacian. This is the precise content of "the second CG manufactures
the symmetry."

## The mobility carries the capacity (porous-medium / UDM)

The degenerate cases are the **same operator with a field-dependent mobility**. Porous-medium / the UDM is
$\partial_t\rho=\nabla\!\cdot\!\big(M(\rho)\nabla\rho\big)$ with $M(\rho)=M_0(\rho_{\max}-\rho)^\beta$ — the
gradient-flux Laplacian, with the **capacity** living in $M$. So capacity is not a separate operator; it is the
mobility of the one operator going degenerate at the bound $\rho_{\max}$. (And $\rho_{\max}=$ the capacity $=$
the b→0 horizon floor — the same capacity the gravity bridge and the soliton no both ran into.)

## The honest boundary — constraints are NOT this operator

The synthesis named two kinds of layer-2 add. This result sharpens the distinction into something precise:

- **Decorrelations = the operator** $\nabla\!\cdot\!(M\nabla\varphi)$ — one forced thing (diffusion, viscosity,
  Ricci; Gaussianity its kernel; capacity its mobility).
- **Constraints = NOT the operator** — incompressibility ($\nabla\!\cdot u=0$, an elliptic/kinematic condition
  enforced by the pressure Poisson) and conservation laws (Cahn–Hilliard) are **global/kinematic conditions**,
  not gradient-flux smoothings. They are the genuinely *second* kind of add, and they do not reduce to the
  Laplacian.

So "one operator" is true and forced for the **dissipative column**, and the rail keeps it from overreaching:
the constraint column is a different beast. The layer-2 add is *either* the unique decorrelation operator *or* a
global constraint — exactly two kinds, now each pinned to a precise object.

## Status

The layer-2 **decorrelation** is one operator, the gradient-flux Laplacian $\nabla\!\cdot\!(M\nabla\varphi)$,
**forced** by the second CG's isotropy + locality + conservation; diffusion / viscosity / Ricci are its
instances (all measured), Gaussianity is its kernel (measured), capacity is its degenerate mobility. The
**constraint** adds (incompressibility, conservation) are a separate kind and are *not* this operator. This
collapses the dissipative half of the layer-2 column to a single forced object and makes the synthesis's
"two kinds of add" exact: **one operator, or one constraint.**
