"""
ED-09.5 -- drive the envelope test from the ACTUAL canonical ED PDE.

Instead of injecting a resonator (synthetic_envelope_validation.py, which tests
only the detector), this integrates the real canonical ED participation dynamics
(Architectural_Canon.md, principles P1/P2/P3/P5/P6) in the oscillatory regime,
extracts the participation field v(t), and measures -- directly, not by ansatz:

    f_v      the participation-mode frequency
    gamma_dec the envelope decay rate
    Q        = omega_0 / (2 gamma_dec)   (the Canon's own invariant, ~3.5)
    r        = f_v / gamma_dec           (cycles per 1/e envelope time)
    N_osc    via the ED-Phys-17 turning-point/2 algorithm, at several thresholds

The flagship prediction is  f_v = N_osc * gamma_dec  with N_osc = 8 (protocol Sec.2,
Observable-Sharpening Sec.15). But Sec.15 also anchors the envelope decoherence
time to tau_v = 1/gamma_dec (the 1/e time). Cycles-per-1/e-time is r = Q/pi ~ 1.1,
NOT 8. The corpus (Observable-Sharpening v0.4) flagged this Q-vs-N_osc
inconsistency; N_osc=8 is the count down to ~1e-3 amplitude, a THRESHOLD count,
not r. This script settles which the physical envelope frequency follows by
running the real PDE -- including its nonlinearity, in case that sustains a
higher-Q mode (the v0.4 escape hatch).

Uniform-mode reduction: this is exactly the object Observable-Sharpening Sec.22
used to select the v<->X_cav identification -- the canonical PDE with no spatial
variation, so F[rho] = -P(rho) (the P1 diffusion/gradient terms vanish for a
uniform field; the P7 triad also needs gradients, so harmonics are a separate,
spatial question). rho and v evolve by P2 + P5 with the P3 saturating penalty.

Deps: numpy, scipy.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit


# --- P3 canonical saturating penalty  P_SY2(rho) = a*g*(rho-rs)/sqrt((rho-rs)^2+r0^2)
def P_SY2(rho, rs=1.0, r0=1.0, ag=1.0):
    d = rho - rs
    return ag * d / np.sqrt(d * d + r0 * r0)
# near equilibrium P'(rs) = ag/r0  (the effective stiffness); ag=r0=1 -> P0=1.


def canonical_uniform(t, y, D, zeta, tau):
    """P2 + P5 with F[rho] = -P_SY2(rho) (uniform mode)."""
    rho, v = y
    F = -P_SY2(rho)
    H = 1.0 - D
    drho = D * F + H * v
    dv = (F - zeta * v) / tau
    return [drho, dv]


def _damped(t, A, gamma, omega, phi, C):
    return C + A * np.exp(-gamma * t) * np.cos(omega * t + phi)


def n_osc_turning_points(amp, floor):
    """ED-Phys-17 algorithm (ed_phys_oscosmo.py lines 408-415): count local
    extrema in the series (max OR min), //2. Applied to the oscillation-amplitude
    envelope series truncated where amp < floor*amp[0] (the detection threshold)."""
    a = np.asarray(amp, float)
    a0 = a[0] if a.size else 1.0
    a = a[a >= floor * a0]
    ext = 0
    for i in range(1, a.size - 1):
        if (a[i] > a[i - 1] and a[i] > a[i + 1]) or (a[i] < a[i - 1] and a[i] < a[i + 1]):
            ext += 1
    return ext // 2


def run(D=0.05, zeta=0.25, tau=1.0, amp0=0.5, T=120.0, n=24000, label=""):
    # --- linear-theory expectation (units P0=tau=1) ---
    disc = (D - zeta) ** 2 - 4 * (1 - D)  # <0 => underdamped (P6)
    lin_ok = disc < 0
    om_lin = 0.5 * np.sqrt(-disc) if lin_ok else float("nan")   # omega_0
    g_lin = 0.5 * (D + zeta)                                    # gamma_dec
    Q_lin = om_lin / (2 * g_lin) if lin_ok else float("nan")

    # --- integrate the real (nonlinear) PDE ---
    sol = solve_ivp(canonical_uniform, (0, T), [1.0 + amp0, 0.0],
                    args=(D, zeta, tau), t_eval=np.linspace(0, T, n),
                    rtol=1e-10, atol=1e-12, method="DOP853")
    t = sol.t
    v = sol.y[1]
    vac = v - np.mean(v[-n // 5:])  # subtract settled offset

    # --- ringdown fit of v(t): f_v, gamma_dec, Q (measured, not linearized) ---
    A0 = np.max(np.abs(vac[: n // 20])) or 1.0
    p0 = [A0, g_lin, om_lin if lin_ok else 1.0, 0.0, 0.0]
    fit_ok = True
    try:
        p, _ = curve_fit(_damped, t, vac, p0=p0, maxfev=60000)
        A, gamma, omega, phi, C = p
        gamma, omega = abs(gamma), abs(omega)
    except Exception:
        fit_ok = False
        A, gamma, omega = A0, g_lin, om_lin
    f_v = omega / (2 * np.pi)
    Q = omega / (2 * gamma) if gamma > 0 else float("nan")
    r = f_v / gamma if gamma > 0 else float("nan")   # cycles per 1/e time

    # --- N_osc via the ED-Phys-17 turning-point/2 count, per detection threshold ---
    # amplitude envelope from |Hilbert|-free peak series: successive |vac| local maxima
    from scipy.signal import find_peaks
    pk, _ = find_peaks(np.abs(vac))
    env = np.abs(vac)[pk] if pk.size else np.abs(vac)
    n_by_thresh = {f"{th:g}": n_osc_turning_points(env, th)
                   for th in (np.exp(-1), 1e-2, 1e-3, 1e-6)}

    print(f"\n=== canonical ED PDE, oscillatory regime  D={D}, zeta={zeta}{(' '+label) if label else ''} ===")
    print(f"  P6 discriminant (D-zeta)^2-4(1-D) = {disc:+.3f}  -> {'UNDERDAMPED' if lin_ok else 'overdamped'}")
    print(f"  linear theory:   f_v/2pi={om_lin/(2*np.pi):.4f}  gamma={g_lin:.4f}  Q={Q_lin:.3f}  (Q/pi={Q_lin/np.pi:.2f})")
    print(f"  MEASURED (nonlinear PDE, amp0={amp0}):")
    print(f"     f_v      = {f_v:.4f}   gamma_dec = {gamma:.4f}")
    print(f"     Q        = {Q:.3f}      (Canon invariant ~3.5)")
    print(f"     r=f_v/gamma_dec = {r:.3f}   <-- the physical cycles-per-1/e-time")
    print(f"  N_osc via ED-Phys-17 turning-point/2, by detection threshold:")
    for k, val in n_by_thresh.items():
        print(f"     down to amp={k:>7}: N_osc = {val}")
    print(f"  PREDICTION uses N_osc=8 -> f_v = 8*gamma_dec.  MEASURED r = {r:.2f}.")
    verdict = ("PREDICTION HOLDS (r ~ 8)" if 4 <= r <= 16 else
               f"PREDICTION OFF by ~{8/r:.1f}x  (physical f_v ~ {r:.1f}*gamma_dec, not 8)")
    print(f"  >>> {verdict}")
    return {"D": D, "zeta": zeta, "f_v": f_v, "gamma_dec": gamma, "Q": Q, "r": r,
            "Q_lin": Q_lin, "N_osc_by_threshold": n_by_thresh, "fit_ok": fit_ok,
            "verdict": verdict}


def main():
    print("=" * 74)
    print("ED-09.5 -- driving the envelope prediction from the REAL canonical PDE")
    print("Question: is the participation envelope at f_v = 8*gamma_dec, or ~Q/pi*gamma_dec?")
    print("=" * 74)
    results = []
    # canon-default zeta=1/4, several oscillatory D; small + large perturbation
    for D in (0.02, 0.05, 0.09):
        results.append(run(D=D, zeta=0.25, amp0=0.05, label="(near-linear)"))
        results.append(run(D=D, zeta=0.25, amp0=0.8, label="(large-amp, probes nonlinearity)"))
    # deep-oscillatory small-zeta (where N_osc=8 might live)
    results.append(run(D=0.01, zeta=0.02, amp0=0.5, label="(small zeta, high-Q)"))

    print("\n" + "=" * 74)
    print("SUMMARY  (r = f_v/gamma_dec = physical cycles per 1/e envelope time)")
    print(f"{'D':>6} {'zeta':>6} {'Q':>7} {'r':>7}   verdict")
    for x in results:
        print(f"{x['D']:>6} {x['zeta']:>6} {x['Q']:>7.2f} {x['r']:>7.2f}   {x['verdict']}")
    print("=" * 74)
    return results


if __name__ == "__main__":
    main()
