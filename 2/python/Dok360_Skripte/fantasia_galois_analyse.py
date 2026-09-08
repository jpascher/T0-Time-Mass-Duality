#!/usr/bin/env python3
"""
fantasia_galois_analyse.py — Galois-HRV-Analyse an PhysioNet Fantasia-Daten
Dok. 360 Nachtrag, Johann Pascher, 8. September 2026

Datensatz: PhysioNet Fantasia Database v1.0.0 (Gold et al. 2002)
  20 Gesunde jung (21-34 J.) + 20 alt (68-85 J.), je 120 min Ruhe, 250 Hz EKG
  Hier: 5 jung (f1y01-05) + 5 alt (f2o01-05), .ecg-Annotationsdateien

Ergebnis: NEGATIV-VALIDIERUNG
  LF-Peak-Stabilität CV: 11-33% >> 1.33% (FFGFT-Auflösungsgrenze)
  5-Limit LF/HF: 4/10 (40%) — nicht signifikant über Nullmodell
  Gruppenunterschied jung/alt: n.s. (n=5 zu klein)

Interpretation:
  Bei spontaner Atmung ist kein Galois-Signal im LF/HF-Verhältnis
  nachweisbar. HF = Atmungsfrequenz (spontan variabel), nicht Resonanz.
  Galois-Test erfordert kontrollierte Atmung (6/min, Resonanzfrequenz-
  Protokoll nach Lehrer & Gevirtz 2014).

Aufruf:
  python3 fantasia_galois_analyse.py --data_dir ./fantasia
"""

import argparse, sys, os
import numpy as np
from scipy import signal, stats
from scipy.interpolate import interp1d
from fractions import Fraction
from collections import Counter
import wfdb

sys.path.insert(0, os.path.dirname(__file__))
from galois_hrv_preprocess import (
    galois_project, galois_depth, arnold_tongue_width,
    HRV_BANDS, RES_LIMIT, _prime_factors
)

def rr_from_ann(rec_path):
    ann = wfdb.rdann(rec_path, 'ecg')
    hdr = wfdb.rdheader(rec_path)
    fs = hdr.fs
    rpeaks = ann.sample[np.array([s in {'N','L','R'} for s in ann.symbol])]
    rr_ms = np.diff(rpeaks) / fs * 1000
    return rr_ms[(rr_ms > 300) & (rr_ms < 1500)]

def welch_hrv(rr_ms, fs=4.0, win_min=10):
    t = np.cumsum(rr_ms) / 1000.0
    t_g = np.arange(t[0], t[-1], 1/fs)
    rr_g = interp1d(t, rr_ms, kind='cubic',
                    bounds_error=False, fill_value='extrapolate')(t_g)
    nperseg = min(int(win_min*60*fs), len(rr_g))
    f, p = signal.welch(rr_g, fs=fs, nperseg=nperseg, nfft=nperseg*4)
    return f, p

def peak_freq_pow(f, p, flo, fhi):
    m = (f >= flo) & (f < fhi)
    if not m.any(): return None, 0.0
    i = np.argmax(p[m]); fm = f[m]; pm = p[m]
    if 0 < i < len(fm)-1:
        a,b,c = pm[i-1],pm[i],pm[i+1]
        delta = 0.5*(a-c)/(a-2*b+c) if (a-2*b+c) != 0 else 0
        return float(fm[i] + delta*(fm[1]-fm[0])), float(np.trapezoid(pm, fm))
    return float(fm[i]), float(np.trapezoid(pm, fm))

def lf_stability(rr_ms, n_seg=6, seg_min=5):
    seg_len = int(seg_min*60*1000 / np.mean(rr_ms))
    peaks = []
    for i in range(min(len(rr_ms)//seg_len, n_seg)):
        seg = rr_ms[i*seg_len:(i+1)*seg_len]
        if len(seg) < 50: continue
        f, p = welch_hrv(seg, win_min=4)
        lf_p, _ = peak_freq_pow(f, p, *HRV_BANDS['LF'])
        if lf_p: peaks.append(lf_p)
    if len(peaks) < 3: return None, None, None
    m = np.mean(peaks); cv = np.std(peaks)/m
    return m, cv, cv < RES_LIMIT

def run(data_dir, records=None):
    if records is None:
        records = {}
        for f in sorted(os.listdir(data_dir)):
            if f.endswith('.hea'):
                rec = f[:-4]
                gruppe = 'jung' if rec.startswith('f1y') else 'alt'
                records[rec] = gruppe

    print("Fantasia-Galois-Analyse (Dok. 360 Nachtrag, FFGFT)")
    print("="*72)
    print(f"{'Rec':<8} {'Gr':<5} {'n_RR':>5} {'LF Hz':>7} {'CV%':>6} "
          f"{'Stab':>5} {'LF/HF':>7} {'p/q':>7} {'k':>3} {'5lim':>5} {'Arnold':>7}")
    print("-"*72)

    results = {'jung': [], 'alt': []}

    for rec_id, gruppe in records.items():
        try:
            rr = rr_from_ann(os.path.join(data_dir, rec_id))
            f_all, p_all = welch_hrv(rr, win_min=10)
            lf_p, lf_pow = peak_freq_pow(f_all, p_all, *HRV_BANDS['LF'])
            hf_p, hf_pow = peak_freq_pow(f_all, p_all, *HRV_BANDS['HF'])
            lf_mean, cv, stable = lf_stability(rr)
            lf_hf = lf_pow/hf_pow if hf_pow > 0 else None

            gr = None
            if lf_hf:
                _, frac, dist, in_grid = galois_project(lf_hf)
                k = galois_depth(frac)
                stab_w = arnold_tongue_width(frac)
                pf = _prime_factors(frac.numerator)|_prime_factors(frac.denominator)
                in_5lim = pf <= {2,3,5}
                gr = dict(frac=frac, k=k, stab=stab_w,
                          in_5lim=in_5lim, lf_hf=lf_hf)

            print(f"{rec_id:<8} {gruppe:<5} {len(rr):>5} "
                  f"{lf_mean:.4f} {cv*100:>6.2f} "
                  f"{'JA' if stable else 'NEIN':>5} "
                  f"{lf_hf:>7.3f} {str(gr['frac']):>7} "
                  f"{gr['k']:>3} {'JA' if gr['in_5lim'] else 'NEIN':>5} "
                  f"{gr['stab']:>7.3f}" if gr else
                  f"{rec_id:<8} {gruppe:<5} {len(rr):>5} — — — — — — — —")

            if gr:
                results[gruppe].append({
                    'lf_cv': cv, 'stable': stable, 'lf_hf': lf_hf,
                    'k': gr['k'], 'stab': gr['stab'],
                    'in_5lim': gr['in_5lim'],
                })
        except Exception as e:
            print(f"{rec_id:<8} FEHLER: {e}")

    print("-"*72)

    # Statistik
    print("\nGruppenvergleich jung vs. alt (Mann-Whitney U):")
    for key, label in [('lf_cv','LF-CV%'), ('stab','Galois-Stabilität'),
                        ('lf_hf','LF/HF'), ('k','Orbit-k')]:
        y = [r[key] for r in results['jung'] if r.get(key) is not None]
        o = [r[key] for r in results['alt']  if r.get(key) is not None]
        if len(y) >= 3 and len(o) >= 3:
            u, p = stats.mannwhitneyu(y, o, alternative='two-sided')
            sig = "***" if p<0.001 else ("**" if p<0.01
                   else ("*" if p<0.05 else "n.s."))
            print(f"  {label:<22}: jung={np.mean(y):.4f}  "
                  f"alt={np.mean(o):.4f}  p={p:.4f} {sig}")

    all_r = results['jung'] + results['alt']
    n5 = sum(1 for r in all_r if r['in_5lim'])
    ns = sum(1 for r in all_r if r.get('stable'))
    print(f"\n5-Limit LF/HF:  {n5}/{len(all_r)} ({100*n5/len(all_r):.0f}%)")
    print(f"LF stabil:      {ns}/{len(all_r)} ({100*ns/len(all_r):.0f}%)")
    print(f"\nBefund: NEGATIV — spontane Atmung macht LF/HF-Galois-Test")
    print(f"        nicht prüfbar. Nächster Schritt: 6/min-Atemprotokoll.")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="./fantasia")
    args = parser.parse_args()
    run(args.data_dir)
