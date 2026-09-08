#!/usr/bin/env python3
"""
HRV 5-Limit Resonance Analysis
==============================
Testet ob die Spektral-Peaks der Herzratenvariabilität (HRV)
in 5-Limit-Verhältnissen (Primzahlen 2, 3, 5) stehen — im Sinne
des Eulerschen Tonnetzes (1739).

Verwendung:
  python3 hrv_5limit_analysis.py --physionet bidmc/1.0.0 bidmc01 bidmc02 ...
  python3 hrv_5limit_analysis.py --rr rr_intervals.csv
  python3 hrv_5limit_analysis.py --demo

PhysioNet: pip install wfdb   (Datenzugang ggf. mit physionet-Account)
RR-CSV: eine Spalte, RR-Intervalle in Millisekunden

Ausgabe: Peaks, Verhältnisse, Euler-Gradus, 5-Limit-Test,
         Nullmodell (zufällige Peaks) als Vergleich.
"""
import argparse, sys
from math import gcd
from fractions import Fraction
import numpy as np
from scipy import signal
from scipy.signal import find_peaks
from scipy.interpolate import interp1d

# ---------------------------------------------------------------- Euler
def prime_factors(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def euler_gradus(p, q):
    """Euler: Gradus suavitatis = 1 + sum (prime-1)*multiplicity über p*q."""
    g = gcd(p, q)
    fac = prime_factors((p // g) * (q // g))
    return 1 + sum((pr - 1) * m for pr, m in fac.items())

def is_5limit(p, q):
    g = gcd(p, q)
    fac = prime_factors((p // g) * (q // g))
    return set(fac) <= {2, 3, 5}

def rationalize(ratio, max_den=12):
    fr = Fraction(ratio).limit_denominator(max_den)
    err_cents = 1200 * np.log2(ratio / float(fr)) if fr > 0 else np.nan
    return fr, err_cents

# ---------------------------------------------------------------- HRV
def rr_to_tachogram(rr_ms, fs=4.0):
    """RR-Intervalle (ms) -> gleichmäßig abgetastete HRV-Zeitreihe."""
    rr = np.asarray(rr_ms, dtype=float)
    # Artefakte grob filtern
    rr = rr[(rr > 300) & (rr < 2000)]
    t = np.cumsum(rr) / 1000.0
    t -= t[0]
    ti = np.arange(0, t[-1], 1 / fs)
    f = interp1d(t, rr, kind="cubic", fill_value="extrapolate")
    x = f(ti)
    x = signal.detrend(x)
    return ti, x, fs

def spectrum(x, fs, nperseg=512):
    freqs, psd = signal.welch(x, fs=fs, nperseg=min(nperseg, len(x)))
    m = (freqs >= 0.003) & (freqs <= 0.5)
    return freqs[m], psd[m]

def find_band_peaks(freqs, psd):
    bands = {"VLF": (0.003, 0.04), "LF": (0.04, 0.15), "HF": (0.15, 0.40)}
    peaks = {}
    for name, (lo, hi) in bands.items():
        m = (freqs >= lo) & (freqs < hi)
        if m.sum() == 0:
            continue
        i = np.argmax(psd[m])
        peaks[name] = (freqs[m][i], psd[m][i])
    return peaks

# ---------------------------------------------------------------- Analyse
def analyse_peaks(peaks, label=""):
    names = list(peaks)
    rows = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            f1, f2 = peaks[names[i]][0], peaks[names[j]][0]
            ratio = f2 / f1
            fr, cents = rationalize(ratio)
            rows.append(dict(
                pair=f"{names[j]}/{names[i]}", ratio=ratio, frac=str(fr),
                cents=cents, gradus=euler_gradus(fr.numerator, fr.denominator),
                five=is_5limit(fr.numerator, fr.denominator)))
    if label:
        print(f"\n--- {label} ---")
        for n, (f, p) in peaks.items():
            print(f"  {n}: {f:.4f} Hz")
        print(f"  {'Paar':<10}{'Ratio':>8}{'Bruch':>8}{'Cent':>8}{'Grad':>6}  5-Limit")
        for r in rows:
            print(f"  {r['pair']:<10}{r['ratio']:>8.3f}{r['frac']:>8}{r['cents']:>8.1f}"
                  f"{r['gradus']:>6}  {'✓' if r['five'] else '✗'}")
    return rows

def null_model(n_trials=2000, seed=0):
    """Zufällige Peak-Positionen innerhalb der Bänder: wie oft 5-limit?"""
    rng = np.random.default_rng(seed)
    hits, grads = 0, []
    for _ in range(n_trials):
        pk = {"VLF": (rng.uniform(0.003, 0.04), 1),
              "LF": (rng.uniform(0.04, 0.15), 1),
              "HF": (rng.uniform(0.15, 0.40), 1)}
        rows = analyse_peaks(pk)
        if all(r["five"] for r in rows):
            hits += 1
        grads.append(np.mean([r["gradus"] for r in rows]))
    return hits / n_trials, np.mean(grads)

# ---------------------------------------------------------------- Eingabe
def load_physionet(db, rec):
    import wfdb
    r = wfdb.rdrecord(rec, pn_dir=db)
    # ECG-Kanal suchen
    idx = next((i for i, n in enumerate(r.sig_name) if "II" in n or "ECG" in n.upper()), 0)
    ecg = r.p_signal[:, idx]
    fs = r.fs
    # Einfache R-Peak-Detektion
    b, a = signal.butter(3, [5 / (fs / 2), 20 / (fs / 2)], "band")
    y = signal.filtfilt(b, a, ecg)
    pk, _ = find_peaks(y, distance=int(0.4 * fs), height=np.percentile(y, 95) * 0.5)
    rr = np.diff(pk) / fs * 1000
    return rr

def demo_rr(seed=1):
    rng = np.random.default_rng(seed)
    fs, T = 4.0, 600
    t = np.arange(0, T, 1 / fs)
    x = (30 * np.sin(2 * np.pi * 0.02 * t) + 20 * np.sin(2 * np.pi * 0.10 * t)
         + 15 * np.sin(2 * np.pi * 0.25 * t) + 8 * rng.standard_normal(len(t)))
    rr = 850 + x
    return rr

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--physionet", nargs="+", metavar=("DB", "REC"))
    ap.add_argument("--rr", help="CSV mit RR-Intervallen (ms)")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()

    datasets = []
    if a.physionet:
        db, recs = a.physionet[0], a.physionet[1:]
        for r in recs:
            try:
                datasets.append((r, load_physionet(db, r)))
            except Exception as e:
                print(f"  {r}: Fehler {e}", file=sys.stderr)
    if a.rr:
        datasets.append((a.rr, np.loadtxt(a.rr, delimiter=",")))
    if a.demo or not datasets:
        datasets.append(("DEMO (synthetisch)", demo_rr()))

    all_rows = []
    for name, rr in datasets:
        ti, x, fs = rr_to_tachogram(rr)
        fr, psd = spectrum(x, fs)
        pk = find_band_peaks(fr, psd)
        all_rows += analyse_peaks(pk, label=name)

    print("\n=== ZUSAMMENFASSUNG ===")
    n = len(all_rows)
    five = sum(r["five"] for r in all_rows)
    print(f"Verhältnisse gesamt: {n}, davon 5-limit: {five} ({100*five/n:.0f}%)")
    print(f"Mittlerer Euler-Gradus: {np.mean([r['gradus'] for r in all_rows]):.2f}")

    p_null, g_null = null_model()
    print(f"\nNullmodell (zufällige Peaks in den Bändern, 2000 Läufe):")
    print(f"  Anteil komplett 5-limit: {100*p_null:.1f}%")
    print(f"  Mittlerer Euler-Gradus:  {g_null:.2f}")

if __name__ == "__main__":
    main()
