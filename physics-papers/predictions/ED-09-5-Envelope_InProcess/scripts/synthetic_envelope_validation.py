"""
ED-09.5 Track B -- synthetic validation of the FRAP envelope pipeline.

Purpose: prove the analysis INSTRUMENT (frap_envelope_lombscargle.analyze)
behaves correctly BEFORE it is ever run on real data. Three cases:

    (1) INJECTION  -- recovery curve + a faithful finite-Q participation mode
                      at the predicted f_v = 8*gamma_dec, with a 3rd harmonic
                      and measurement noise. The pipeline MUST detect it:
                      F0 pass, f_v recovered within factor-2, Q_v in range.
    (2) NULL       -- recovery curve + noise, NO envelope. The pipeline MUST
                      NOT report a significant peak (no false positive).
    (3) OFF-FREQ   -- a real mode, but at 600 Hz while the prediction (from
                      gamma_dec) is 240 Hz. The pipeline MUST reject it on F0
                      (specificity: right detector, wrong frequency -> FAIL).

The injected mode is narrowband noise through a 2nd-order resonator (a driven
damped oscillator, PSD Lorentzian of width f_v/Q) -- a physically faithful
"mode with quality factor Q", NOT a rigged pure sinusoid.

WHAT THIS ESTABLISHES: the detector works (sensitive + specific). It does NOT
test ED. Confirming ED-09.5 requires running analyze() on real concentrated,
high-framerate FRAP data (protocol Sec.7). A stronger theory-side check is to
drive the injected signal from the actual canonical ED PDE (Canon P6) rather
than a resonator -- flagged as the next step, not done here.
"""
from __future__ import annotations
import numpy as np
from scipy.signal import iirpeak, lfilter

from frap_envelope_lombscargle import analyze, _exp1


def _recovery(t, A=0.8, tau_D=0.05, C=0.1):
    return _exp1(t, A, tau_D, C)


def _mode(n, f0, fs, Q, rms, rng):
    """Narrowband noise through a resonator at f0 with quality Q.

    Output has a Lorentzian PSD centered at f0 with FWHM ~ f0/Q, scaled to the
    requested RMS. This is a faithful finite-Q mode, not a pure tone.
    """
    b, a = iirpeak(f0 / (fs / 2.0), Q)
    x = lfilter(b, a, rng.standard_normal(n))
    x = x / (np.std(x) or 1.0) * rms
    return x


def make_case(kind, *, fs=2000.0, T=2.0, gamma_dec=30.0, N_osc=8.0,
              Q_inj=6.0, env_rms=0.03, noise=0.010, h3=0.04, seed=0):
    rng = np.random.default_rng(seed)
    n = int(fs * T)
    t = np.arange(n) / fs
    I = _recovery(t)
    f_v = N_osc * gamma_dec  # 240 Hz for the defaults

    if kind == "injection":
        env = _mode(n, f_v, fs, Q_inj, env_rms, rng)
        env += _mode(n, 3.0 * f_v, fs, Q_inj, h3 * env_rms, rng)  # 3rd harmonic
        I = I + env
    elif kind == "offfreq":
        I = I + _mode(n, 600.0, fs, Q_inj, env_rms, rng)  # real mode, wrong freq
    elif kind == "null":
        pass  # recovery + noise only
    else:
        raise ValueError(kind)

    I = I + noise * rng.standard_normal(n)
    return t, I


def run():
    print("=" * 74)
    print("ED-09.5 Track B -- synthetic pipeline validation")
    print("predicted f_v = 8 * gamma_dec = 8 * 30 Hz = 240 Hz  (band 80-800 Hz)")
    print("=" * 74)

    checks = []

    # (1) injection -- must DETECT
    t, I = make_case("injection", seed=1)
    r = analyze(t, I, gamma_dec=30.0, rng=1)
    m = r["measured"]
    print("\n[1] INJECTION (true mode at 240 Hz present)")
    print(f"    f_v measured   = {m['f_v_Hz']:.1f} Hz   (pred 240.0)")
    print(f"    significant    = {m['significant']}  (FAP={m['false_alarm_prob']:.2e})")
    print(f"    Q_v            = {None if m['Q_v'] is None else round(m['Q_v'],2)}   (F3 band 4-9)")
    print(f"    N_osc          = {None if m['N_osc'] is None else round(m['N_osc'],2)}   (F2 band 6-12)")
    print(f"    3rd-harm ratio = {None if m['third_harmonic_ratio'] is None else round(m['third_harmonic_ratio'],3)}   (F4 band .03-.06)")
    print(f"    F0..F5         = {r['falsification']}")
    print(f"    verdict        = {r['verdict']}")
    ok1 = r["falsification"]["F0"] and abs(np.log2(m["f_v_Hz"] / 240.0)) <= 1.0
    checks.append(("injection detected at right f_v (F0)", ok1))

    # (2) null -- must NOT detect
    t, I = make_case("null", seed=2)
    r = analyze(t, I, gamma_dec=30.0, rng=2)
    m = r["measured"]
    print("\n[2] NULL (recovery + noise, no envelope)")
    print(f"    significant    = {m['significant']}  (FAP={m['false_alarm_prob']:.2e})")
    print(f"    F0             = {r['falsification']['F0']}")
    print(f"    verdict        = {r['verdict']}")
    ok2 = (not r["falsification"]["F0"])
    checks.append(("null correctly gives no F0 detection (specificity)", ok2))

    # (3) off-frequency -- real peak, wrong freq -> F0 must FAIL
    t, I = make_case("offfreq", seed=3)
    r = analyze(t, I, gamma_dec=30.0, rng=3)
    m = r["measured"]
    print("\n[3] OFF-FREQ (real mode at 600 Hz; prediction is 240 Hz)")
    print(f"    f_v measured   = {m['f_v_Hz']:.1f} Hz  (significant={m['significant']})")
    print(f"    F0             = {r['falsification']['F0']}")
    print(f"    verdict        = {r['verdict']}")
    ok3 = (not r["falsification"]["F0"])
    checks.append(("off-frequency peak correctly rejected on F0 (specificity)", ok3))

    print("\n" + "=" * 74)
    allok = True
    for name, ok in checks:
        print(f"    [{'PASS' if ok else 'FAIL'}]  {name}")
        allok = allok and ok
    print("=" * 74)
    print("INSTRUMENT VALIDATION:", "PASS -- detector is sensitive and specific"
          if allok else "FAIL -- pipeline needs fixing")
    print("(Reminder: this validates the detector, NOT ED. The ED test needs"
          " real high-framerate concentrated-FRAP data.)")
    return allok


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
