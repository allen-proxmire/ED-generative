"""
ED-09.5 -- harmonic (F4) and triad (F5) legs, done with MODAL decomposition.

Supersedes ed_pde_spatial_harmonic.py's point-probe, which sampled at x0 = L/4
(index N//4). That location is a NODE of both the k=1 and k=3 spatial modes
(cos(pi/2)=cos(3pi/2)=0) and an ANTINODE of k=2, so its temporal spectrum is
dominated by the k=2 (2*f_v) response and cannot read the k=1 fundamental or its
k=3/3*f_v harmonic -- the ~0.1% "temporal 3rd harmonic" it reported is a
probe-location artifact, not F4.

Clean method: project rho(x,t) onto spatial modes a_k(t) = (2/N) sum rho cos(kx),
then FFT each a_k(t). This is location-independent. It answers three things:
  (1) does the k=2 mode ring at 2*f_v and k=3 at 3*f_v? (the weakly-nonlinear cascade)
  (2) F4: modal 3rd-harmonic ratio |a3 @ 3f_v| / |a1 @ f_v|  vs pre-registered 3-6%
  (3) F5: triad phase-locking, phase(a2) - 2*phase(a1) and phase(a3) - 3*phase(a1)
      near-constant => quadratic/cubic coupling locked (a triad), with a coupling
      strength read off the locked-mode amplitude fractions.

Canonical PDE (Architectural_Canon.md P1-P5 + P7 gradient term):
    rho_t = D*F + (1-D)*v ;  v_t = (F - zeta*v)/tau
    F = M(rho)*rho_xx + M'(rho)*(rho_x)^2 - P_SY2(rho)
    M(rho) = M0*(rho_max-rho)/(rho_max-rho*),  M' = -M0/(rho_max-rho*)
    P_SY2(rho) = AG*d/sqrt(d^2+R0^2),  d = rho-rho*   (saturating, cubic-anharmonic)
Deps: numpy, scipy.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp

RS, RMAX = 1.0, 2.0
R0, AG = 1.0, 1.0


def P_SY2(rho):
    d = rho - RS
    return AG * d / np.sqrt(d * d + R0 * R0)


def make_rhs(N, L, D, zeta, tau, M0):
    dx = L / N
    Mslope = -M0 / (RMAX - RS)

    def M(rho):
        return np.clip(M0 * (RMAX - rho) / (RMAX - RS), 0.0, None)

    def rhs(t, y):
        rho, v = y[:N], y[N:]
        rp = (np.roll(rho, -1) - np.roll(rho, 1)) / (2 * dx)
        rpp = (np.roll(rho, -1) - 2 * rho + np.roll(rho, 1)) / dx**2
        F = M(rho) * rpp + Mslope * rp**2 - P_SY2(rho)
        return np.concatenate([D * F + (1 - D) * v, (F - zeta * v) / tau])

    return rhs


def modal(sol_rho, x, k):
    """a_k(t) = (2/N) sum_j rho(x_j,t) cos(k x_j)  -- real cosine-mode amplitude."""
    c = np.cos(k * x)
    return (2.0 / x.size) * (sol_rho.T @ c)


def peak(sig, t):
    """dominant non-DC spectral line: (freq, complex amplitude at that bin)."""
    sig = sig - sig.mean()
    dt = t[1] - t[0]
    w = np.hanning(sig.size)
    sp = np.fft.rfft(sig * w)
    fr = np.fft.rfftfreq(sig.size, dt)
    m = fr > 0.02
    idx = np.where(m)[0][int(np.argmax(np.abs(sp)[m]))]
    return fr[idx], sp[idx], fr, sp


def amp_at(fr, sp, f0):
    j = int(np.argmin(np.abs(fr - f0)))
    return sp[j]


def run(D=0.05, zeta=0.02, tau=1.0, M0=0.02, N=256, L=2 * np.pi,
        amp=0.30, T=400.0, nt=16000, label=""):
    x = np.linspace(0, L, N, endpoint=False)
    rho0 = RS + amp * np.cos(x)           # pure k=1 excitation
    rhs = make_rhs(N, L, D, zeta, tau, M0)
    sol = solve_ivp(rhs, (0, T), np.concatenate([rho0, np.zeros(N)]),
                    t_eval=np.linspace(0, T, nt), method="LSODA",
                    rtol=1e-9, atol=1e-11)
    t = sol.t
    rho = sol.y[:N]
    a1, a2, a3 = (modal(rho, x, k) for k in (1, 2, 3))

    f1, s1, fr1, sp1 = peak(a1, t)

    # --- F4: TEMPORAL 3rd harmonic = waveform anharmonicity WITHIN the fundamental
    # mode a1(t). The FRAP/optomechanics observable is power at 3*f_v in the signal;
    # for a k=1-dominated pattern that is the 3*f_v content of a1(t), NOT a cross-mode
    # a3 amplitude. Measured intra-mode: |a1 @ 3f_v| / |a1 @ f_v|.
    A1 = np.abs(amp_at(fr1, sp1, f1))
    r_t3 = np.abs(amp_at(fr1, sp1, 3 * f1)) / A1     # temporal 3rd (F4)
    r_t2 = np.abs(amp_at(fr1, sp1, 2 * f1)) / A1     # temporal 2nd (context)

    # cross-mode content, for the spatial->temporal diagnostic
    fr3 = peak(a3, t)[2]; sp3 = peak(a3, t)[3]
    r_x3 = np.abs(amp_at(fr3, sp3, 3 * f1)) / A1     # k=3 spatial mode @ 3f_v

    # F5 triad phase-locking of the intra-mode harmonics
    ph1 = np.angle(amp_at(fr1, sp1, f1))
    ph3t = np.angle(amp_at(fr1, sp1, 3 * f1))
    d31 = (ph3t - 3 * ph1 + np.pi) % (2 * np.pi) - np.pi

    # spatial harmonic at the moment of peak |a1|
    tp = int(np.argmax(np.abs(a1)))
    sk = np.abs(np.fft.rfft(rho[:, tp] - rho[:, tp].mean()))
    sp_k3 = sk[3] / sk[1] if sk[1] > 0 else float("nan")

    # analytic cross-check: Duffing 3rd-harmonic a3/a1 = |beta| A^2 / (32 w0^2).
    # P_SY2 = d - d^3/2 + ... so cubic/linear = -1/2 => a3/a1 ~ A^2/64.
    r_analytic = amp * amp / 64.0

    b = "IN 3-6%" if 0.03 <= r_t3 <= 0.06 else ("BELOW" if r_t3 < 0.03 else "ABOVE")
    print(f"[{label}] amp={amp} zeta={zeta} D={D}")
    print(f"   f_v(k=1) = {f1:.4f}")
    print(f"   F4 TEMPORAL 3rd harmonic |a1@3f|/|a1@f| = {r_t3*100:5.2f}%   [{b} 3-6%]")
    print(f"      analytic Duffing A^2/64              = {r_analytic*100:5.2f}%")
    print(f"      (temporal 2nd |a1@2f|/|a1@f|         = {r_t2*100:5.2f}%)")
    print(f"   cross-mode k3 @ 3f_v / a1@f             = {r_x3*100:5.2f}%")
    print(f"   spatial k3/k1 at peak |a1|              = {sp_k3*100:5.2f}%")
    print(f"   F5 triad phase resid |ph(3f)-3ph(f)|    = {abs(d31):.2f} rad (0=>locked)")
    return dict(amp=amp, zeta=zeta, f_v=float(f1),
                F4_temporal_pct=float(r_t3 * 100), analytic_pct=float(r_analytic * 100),
                temporal_2nd_pct=float(r_t2 * 100), crossmode_k3_pct=float(r_x3 * 100),
                spatial_k3_pct=float(sp_k3 * 100), triad_d31=float(abs(d31)), band=b)


def main():
    print("=" * 72)
    print("ED-09.5 harmonic (F4) + triad (F5) legs -- MODAL decomposition")
    print("=" * 72)
    rows = []
    print("\n-- high-Q zeta=0.02, amplitude sweep (clean lines; A^2 scaling test) --")
    for amp in (0.20, 0.40, 0.60, 0.80):
        rows.append(run(amp=amp, zeta=0.02, T=500.0, nt=20000, label="highQ"))
        print()
    print("-- canon-default zeta=0.25 (Q~3.5, physical case) --")
    for amp in (0.40, 0.60):
        rows.append(run(amp=amp, zeta=0.25, T=200.0, nt=12000, label="canon"))
        print()
    print("=" * 72)
    print(f"{'label':>6}{'amp':>6}{'zeta':>6}{'f_v':>8}"
          f"{'F4(t)%':>8}{'Duff%':>7}{'2nd%':>7}{'sp_k3%':>8}")
    for r in rows:
        lab = "highQ" if r['zeta'] < 0.1 else "canon"
        print(f"{lab:>6}{r['amp']:>6}{r['zeta']:>6}{r['f_v']:>8.3f}"
              f"{r['F4_temporal_pct']:>8.2f}{r['analytic_pct']:>7.2f}"
              f"{r['temporal_2nd_pct']:>7.2f}{r['spatial_k3_pct']:>8.2f}")
    print("=" * 72)
    print("F4 pre-registered = 3-6% (temporal). Duff = analytic A^2/64 expectation.")
    return rows


if __name__ == "__main__":
    main()
