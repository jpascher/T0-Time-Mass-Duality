#!/usr/bin/env python3
"""
orbit_experiment_synthetic.py — Orbit-Typ-Experiment mit synthetischen HRV-Daten
Dok. 360, Johann Pascher, 8. September 2026

Da PhysioNet eine Registrierung erfordert, werden synthetische RR-Intervall-
Sequenzen generiert, die den publizierten Statistiken entsprechen:

Quellen für LF/HF-Statistiken:
  Task Force ESC/NASPE 1996, Eur. Heart J. 17, 354-381
  Shaffer & Ginsberg 2017, Front. Public Health 5:258
  Billman 2013, Front. Physiol. 4:26 (LBBB/VES)

Rhythmusklassen und typische LF/HF-Bereiche:
  N  (Normal Sinus):     LF/HF ~ Beta(2,2) skaliert auf [0.5, 3.0]
  V  (VES-reich):        LF/HF ~ Beta(2,1) skaliert auf [2.0, 7.0]
  L  (LBBB):             LF/HF ~ Beta(2,2) skaliert auf [0.8, 4.0]
  R  (RBBB):             LF/HF ~ Beta(2,2) skaliert auf [0.6, 3.5]
  A  (Atriale Ektopie):  LF/HF ~ Beta(1.5,2) skaliert auf [0.3, 2.5]
"""

import numpy as np
from scipy import stats, signal
from collections import defaultdict, Counter
from fractions import Fraction
import sys

sys.path.insert(0, '.')
from galois_hrv_preprocess import (
    classify_orbit, galois_project, ORBIT_LABELS,
    HRV_BANDS, RES_LIMIT, hrv_galois_pipeline
)

np.random.seed(42)

# ---------------------------------------------------------------
# Synthetische RR-Sequenzen mit realistischen LF/HF-Verhältnissen
# ---------------------------------------------------------------

def synthetic_rr(n_beats=300, target_lf_hf=2.0, hr_bpm=70,
                  lf_hz=0.10, hf_hz=0.25, noise_frac=0.05):
    """
    Generiert synthetische RR-Sequenz mit vorgegebenem LF/HF-Verhältnis.
    Basiert auf additiver Überlagerung von Sinusschwingungen.
    """
    fs = 4.0
    rr_mean = 60000 / hr_bpm  # ms

    # Amplituden: LF/HF = A_LF^2 / A_HF^2 -> A_LF = sqrt(ratio) * A_HF
    # A_HF normiert auf 5% von rr_mean
    a_hf = rr_mean * 0.04
    a_lf = a_hf * np.sqrt(target_lf_hf)

    t = np.arange(n_beats) * rr_mean / 1000  # s
    lf_comp = a_lf * np.sin(2 * np.pi * lf_hz * t +
                              np.random.uniform(0, 2*np.pi))
    hf_comp = a_hf * np.sin(2 * np.pi * hf_hz * t +
                              np.random.uniform(0, 2*np.pi))
    noise = np.random.normal(0, rr_mean * noise_frac, n_beats)

    rr = rr_mean + lf_comp + hf_comp + noise
    rr = np.clip(rr, 300, 1500)
    return rr

RHYTHM_PARAMS = {
    # (lf_hf_a, lf_hf_b, lf_hf_lo, lf_hf_hi, hr_bpm, noise_frac, n_samples)
    "N": (2.0, 2.0, 0.5, 3.0,  70, 0.05, 80),  # Normal Sinus
    "V": (2.0, 1.0, 2.0, 7.0,  75, 0.10, 60),  # VES-reich (Sympathikus↑)
    "L": (2.0, 2.0, 0.8, 4.0,  68, 0.07, 40),  # LBBB
    "R": (2.0, 2.0, 0.6, 3.5,  72, 0.06, 40),  # RBBB
    "A": (1.5, 2.0, 0.3, 2.5,  80, 0.12, 40),  # Atriale Ektopie
}

def generate_dataset():
    segments = []
    for rhythm, (a, b, lo, hi, hr, noise, n) in RHYTHM_PARAMS.items():
        ratios = stats.beta(a, b).rvs(n) * (hi - lo) + lo
        for r in ratios:
            rr = synthetic_rr(n_beats=300, target_lf_hf=r,
                               hr_bpm=hr + np.random.normal(0, 5),
                               noise_frac=noise)
            segments.append((rr, rhythm, r))
    return segments

# ---------------------------------------------------------------
# Analyse
# ---------------------------------------------------------------

def run_experiment():
    print("="*62)
    print("  Orbit-Typ-Biomarker-Experiment (Dok. 360, FFGFT)")
    print("  Synthetische HRV-Daten nach Task Force 1996 / Shaffer 2017")
    print("="*62)

    segments = generate_dataset()
    print(f"\n{len(segments)} Segmente ({sum(p[6] for p in RHYTHM_PARAMS.values())} geplant)\n")

    orbit_by_rhythm = defaultdict(list)
    stability_by_rhythm = defaultdict(list)
    depth_by_rhythm = defaultdict(list)
    ingrid_by_rhythm = defaultdict(list)
    lf_hf_by_rhythm = defaultdict(list)

    for rr, rhythm, true_ratio in segments:
        try:
            res = hrv_galois_pipeline(rr, verbose=False)
            if res["lf_hf_ratio"] == float('inf') or not res["orbit"]:
                continue
            k = res["orbit"]["orbit_k"]
            orbit_by_rhythm[rhythm].append(k)
            stability_by_rhythm[rhythm].append(res["stability"])
            depth_by_rhythm[rhythm].append(k)
            ingrid_by_rhythm[rhythm].append(int(res["in_grid"]))
            lf_hf_by_rhythm[rhythm].append(res["lf_hf_ratio"])
        except Exception:
            continue

    # Tabelle
    print(f"{'Rhythmus':<8} {'N':>4} {'LF/HF̄':>7} {'k̄':>5} {'σk':>5} "
          f"{'Stab̄':>7} {'Raster%':>8}  Orbit-Verteilung")
    print("-"*70)

    for rhythm in ["N","V","L","R","A"]:
        if rhythm not in orbit_by_rhythm: continue
        ks = orbit_by_rhythm[rhythm]
        stabs = stability_by_rhythm[rhythm]
        lfs = lf_hf_by_rhythm[rhythm]
        ig = ingrid_by_rhythm[rhythm]
        orbit_dist = Counter(ks)
        ostr = " ".join(f"k{k}:{n}" for k,n in sorted(orbit_dist.items()))
        print(f"{rhythm:<8} {len(ks):>4} {np.mean(lfs):>7.3f} "
              f"{np.mean(ks):>5.2f} {np.std(ks):>5.2f} "
              f"{np.mean(stabs):>7.3f} {np.mean(ig)*100:>7.1f}%  {ostr}")

    print("-"*70)

    # Statistische Tests
    print("\nStatistische Tests (Mann-Whitney U, zweiseitig):")
    pairs = [("N","V"), ("N","L"), ("N","A"), ("N","R")]
    for r1, r2 in pairs:
        if r1 not in orbit_by_rhythm or r2 not in orbit_by_rhythm:
            continue
        k1 = orbit_by_rhythm[r1]; k2 = orbit_by_rhythm[r2]
        s1 = stability_by_rhythm[r1]; s2 = stability_by_rhythm[r2]
        _, p_k = stats.mannwhitneyu(k1, k2, alternative='two-sided')
        _, p_s = stats.mannwhitneyu(s1, s2, alternative='two-sided')
        sig_k = "***" if p_k < 0.001 else ("**" if p_k < 0.01
                 else ("*" if p_k < 0.05 else "n.s."))
        sig_s = "***" if p_s < 0.001 else ("**" if p_s < 0.01
                 else ("*" if p_s < 0.05 else "n.s."))
        print(f"  {r1} vs {r2}:  Orbit-k p={p_k:.4f}{sig_k:>4}  "
              f"Stabilität p={p_s:.4f}{sig_s:>4}")

    # Orbit-Typ-Bedeutung
    print("\nOrbit-Typ-Bedeutung (Galois-Tiefe k):")
    for k, label in ORBIT_LABELS.items():
        print(f"  k={k}: {label}")

    # Befund
    print("\nBefund:")
    v_k = np.mean(orbit_by_rhythm.get("V", [0]))
    n_k = np.mean(orbit_by_rhythm.get("N", [0]))
    v_s = np.mean(stability_by_rhythm.get("V", [0]))
    n_s = np.mean(stability_by_rhythm.get("N", [0]))
    print(f"  Normal:    mittlere Orbit-Tiefe k̄={n_k:.2f}, Stabilität={n_s:.3f}")
    print(f"  VES-reich: mittlere Orbit-Tiefe k̄={v_k:.2f}, Stabilität={v_s:.3f}")
    if v_k > n_k:
        print(f"  => VES-reiche Rhythmen zeigen höhere Galois-Tiefe (k̄↑)")
        print(f"     (komplexere algebraische Struktur, GF(3^k) mit größerem k)")
    if v_s < n_s:
        print(f"  => VES-reiche Rhythmen zeigen geringere Stabilität (Arnold-Zunge ↓)")
        print(f"     (LF/HF-Verhältnisse mit höheren Primzahl-Nennern = fragilere Resonanz)")

    print("\nMethodik:")
    print(f"  Auflösungsgrenze: Δf/f >= {RES_LIMIT*100:.2f}% (Satz B Dok. 359)")
    print(f"  Galois-Raster: Primfaktoren ⊆ {{2,3,5,7,11,13}} (Satz B Dok. 358)")
    print(f"  Stabilität: Arnold-Zungenbreite ≈ 2/(p+q) (Dok. 328)")
    print(f"  Synthetische Daten: LF/HF nach Beta-Verteilung gemäß Task Force 1996")

if __name__ == "__main__":
    run_experiment()
