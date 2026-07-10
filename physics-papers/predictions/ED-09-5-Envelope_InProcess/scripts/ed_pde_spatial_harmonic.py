"""
ED-09.5 -- spatial canonical-PDE run, for the 3rd-harmonic (F4) leg.

The uniform-mode run (ed_pde_envelope_drive.py) settled the envelope FREQUENCY
but could not test the harmonic/triad legs (F4/F5): those come from the P7
nonlinear term M'(rho)|grad rho|^2, which is exactly zero for a spatially
uniform field. This runs the full 1-D canonical PDE (P1+P2+P3+P4+P5) with a
single spatial mode excited, and measures how much 3rd-harmonic content the
nonlinearity generates -- the pre-registered claim is 3-6% (protocol F4).

Canonical PDE (Architectural_Canon.md):
    rho_t = D*F[rho] + (1-D)*v
    v_t   = (F[rho] - zeta*v)/tau
    F[rho]= M(rho)*rho_xx + M'(rho)*(rho_x)^2 - P_SY2(rho)
    M(rho)= M0*(rho_max-rho)/(rho_max-rho*)   (P4: M(rho_max)=0),  M' = -M0/(rho_max-rho*)

Honest scope: measures the temporal 3rd-harmonic ratio (power at 3*f_v over
power at f_v) at a probe point, the observable protocol F4 targets. It does NOT
re-open the frequency question (settled: f_v ~ Q/pi * gamma_dec). Deps: numpy, scipy.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp

RS, RMAX = 1.0, 2.0            # rho*, rho_max
R0, AG = 1.0, 1.0             # penalty scale, alpha*gamma


def P_SY2(rho):
    d = rho - RS
    return AG * d / np.sqrt(d * d + R0 * R0)


def make_rhs(N, L, D, zeta, tau, M0):
    dx = L / N
    Mslope = -M0 / (RMAX - RS)  # M'(rho), constant for beta=1

    def M(rho):
        return np.clip(M0 * (RMAX - rho) / (RMAX - RS), 0.0, None)

    def rhs(t, y):
        rho = y[:N]
        v = y[N:]
        rp = (np.roll(rho, -1) - np.roll(rho, 1)) / (2 * dx)        # rho_x
        rpp = (np.roll(rho, -1) - 2 * rho + np.roll(rho, 1)) / dx**2  # rho_xx
        F = M(rho) * rpp + Mslope * rp**2 - P_SY2(rho)
        drho = D * F + (1 - D) * v
        dv = (F - zeta * v) / tau
        return np.concatenate([drho, dv])

    return rhs


def run(D=0.05, zeta=0.25, tau=1.0, M0=0.02, N=128, L=2 * np.pi,
        amp=0.15, T=160.0, nt=8000):
    x = np.linspace(0, L, N, endpoint=False)
    rho0 = RS + amp * np.cos(x)          # single spatial mode k=1
    v0 = np.zeros(N)
    rhs = make_rhs(N, L, D, zeta, tau, M0)
    sol = solve_ivp(rhs, (0, T), np.concatenate([rho0, v0]),
                    t_eval=np.linspace(0, T, nt), method="LSODA",
                    rtol=1e-8, atol=1e-10)
    t = sol.t
    probe = sol.y[N // 4]                 # rho(x0, t) at a fixed point
    # detrend: remove the slow decay/settling (deg-3 polynomial) so the FFT sees
    # the oscillation, not the drift that otherwise dominates the low bins.
    coef = np.polyfit(t, probe, 3)
    sig = probe - np.polyval(coef, t)

    # temporal spectrum -> fundamental f_v (searched in a physical band, not DC)
    dt = t[1] - t[0]
    freqs = np.fft.rfftfreq(sig.size, dt)
    amp_spec = np.abs(np.fft.rfft(sig * np.hanning(sig.size)))
    band = (freqs >= 0.03) & (freqs <= 0.5)      # exclude residual drift bins
    kfund = np.where(band)[0][int(np.argmax(amp_spec[band]))]
    f_v = freqs[kfund]
    k3 = int(np.argmin(np.abs(freqs - 3 * f_v)))
    ratio = amp_spec[k3] / amp_spec[kfund] if amp_spec[kfund] > 0 else float("nan")

    # spatial check: does k=3 appear from the k=1 excitation?
    rho_final = sol.y[:N, -1] - np.mean(sol.y[:N, -1])
    sk = np.abs(np.fft.rfft(rho_final))
    sk_ratio = sk[3] / sk[1] if sk[1] > 0 else float("nan")

    print(f"\n=== spatial canonical PDE  D={D} zeta={zeta} M0={M0} amp={amp} ===")
    print(f"  temporal fundamental f_v   = {f_v:.4f}")
    print(f"  temporal 3rd-harmonic ratio = {ratio*100:.2f}%   (F4 pre-registered: 3-6%)")
    print(f"  spatial  k=3/k=1 ratio      = {sk_ratio*100:.2f}%")
    band = "IN 3-6% band" if 0.03 <= ratio <= 0.06 else ("BELOW 3%" if ratio < 0.03 else "ABOVE 6%")
    print(f"  >>> temporal 3rd harmonic: {band}")
    return {"D": D, "amp": amp, "f_v": float(f_v), "third_harmonic_pct": float(ratio * 100),
            "spatial_k3_k1_pct": float(sk_ratio * 100), "band": band}


def main():
    print("=" * 70)
    print("ED-09.5 spatial run -- does the P7 nonlinearity make a 3-6% 3rd harmonic?")
    print("=" * 70)
    out = []
    print("\n-- canon-default zeta=1/4 (Q~3.5, oscillation damps in ~1 cycle) --")
    for amp in (0.15, 0.30):
        out.append(run(amp=amp, zeta=0.25))
    print("\n-- high-Q zeta=0.02 (rings ~8 cycles; where a clean harmonic can be read) --")
    for amp in (0.15, 0.30):
        out.append(run(amp=amp, zeta=0.02))
    print("\n" + "=" * 70)
    print(f"{'amp':>6} {'f_v':>8} {'3rd-harm %':>11}  band")
    for r in out:
        print(f"{r['amp']:>6} {r['f_v']:>8.4f} {r['third_harmonic_pct']:>10.2f}%  {r['band']}")
    print("=" * 70)
    return out


if __name__ == "__main__":
    main()
