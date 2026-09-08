#!/usr/bin/env python3
"""
galois_hrv_preprocess.py — Galois-informierter Vorverarbeitungsfilter für HRV-Daten
Dok. 360, Johann Pascher, 8. September 2026

Implementiert:
  1. Auflösungsfilter: Delta_f/f >= 100*xi ~ 1.33%
  2. HRV-Bandgrenzen als algebraische Konstanten (5-Limit)
  3. Galois-Projektion: Frequenzverhältnisse -> nächstes Raster-Element
  4. Orbit-Typ-Klassifikation: GF(3^k)-Tiefe des dominanten Verhältnisses
  5. Arnold-Zungenbreite als Stabilitätsbewertung (Dok. 328)

Abhängigkeiten: numpy, scipy (Standard)
"""

import numpy as np
from fractions import Fraction
from math import gcd, pi, sqrt, log2
from typing import Optional

# ---------------------------------------------------------------
# Algebraische Konstanten (aus FFGFT-Korpus)
# ---------------------------------------------------------------

XI = Fraction(4, 30000)
RES_LIMIT = float(100 * XI)          # 1.333...%  — Auflösungsgrenze Dok. 343
FAREY_QC  = pi / sqrt(6 * RES_LIMIT) # ≈ 11.1     — maximaler Nenner trennbar

# HRV-Bandgrenzen als algebraische Konstanten (5-Limit, Satz A Dok. 359)
HRV_BANDS = {
    "VLF": (0.0,    float(Fraction(1, 25))),   # 0.000–0.040 Hz
    "LF":  (float(Fraction(1, 25)),
            float(Fraction(3, 20))),             # 0.040–0.150 Hz
    "HF":  (float(Fraction(3, 20)),
            float(Fraction(2, 5))),              # 0.150–0.400 Hz
}

# Galois-Raster: rationale Zahlen p/q mit Primfaktoren in {2,3,5,7,11,13}
# bis Nenner 60 (ausreichend für HRV-Verhältnisse)
GALOIS_GRID_SIZE = 60
GALOIS_PRIMES = {2, 3, 5, 7, 11, 13}

def _prime_factors(n: int) -> set:
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d); n //= d
        d += 1
    if n > 1: factors.add(n)
    return factors

def _build_galois_grid(max_den: int = GALOIS_GRID_SIZE) -> list:
    """Erstellt sortierte Liste aller Galois-Raster-Verhältnisse p/q."""
    rationals = set()
    for den in range(1, max_den + 1):
        if not _prime_factors(den) <= GALOIS_PRIMES:
            continue
        for num in range(1, den * 4 + 1):  # bis 4:1
            if gcd(num, den) == 1 and _prime_factors(num) <= GALOIS_PRIMES:
                rationals.add(Fraction(num, den))
    return sorted(rationals)

GALOIS_GRID = _build_galois_grid()
GALOIS_FLOATS = np.array([float(r) for r in GALOIS_GRID])

# Galois-Tiefe: Primzahl p hat Tiefe ord_p(3)
def _order_mod(a: int, n: int) -> Optional[int]:
    if gcd(a, n) != 1: return None
    k, x = 1, a % n
    while x != 1:
        x = (x * a) % n; k += 1
        if k > n: return None
    return k

PRIME_DEPTH = {p: _order_mod(3, p) for p in GALOIS_PRIMES if p > 2}
# {3: None (teilt Gruppenordnung), 5: 4, 7: 6, 11: 5, 13: 3}

def galois_depth(ratio: Fraction) -> int:
    """Galois-Tiefe k eines Verhältnisses: max ord_p(3) über Primfaktoren."""
    pf = _prime_factors(ratio.numerator) | _prime_factors(ratio.denominator)
    pf -= {2}  # 2 ist in allen Schichten
    if not pf: return 1  # reine Zweierpotenz: k=1
    depths = [PRIME_DEPTH.get(p, 99) for p in pf if PRIME_DEPTH.get(p) is not None]
    return max(depths) if depths else 1

# ---------------------------------------------------------------
# 1. Auflösungsfilter
# ---------------------------------------------------------------

def resolution_filter(freqs: np.ndarray, psd: np.ndarray,
                       center_freq: Optional[float] = None) -> tuple:
    """
    Unterdrückt Frequenzkomponenten die innerhalb der Galois-Auflösungsgrenze
    Delta_f/f >= 100*xi ~ 1.33% liegen.

    Parameters
    ----------
    freqs : Frequenzachse (Hz)
    psd   : Leistungsdichtespektrum
    center_freq : Referenzfrequenz (Standard: Median der HRV-Bänder)

    Returns
    -------
    freqs_filtered, psd_filtered, mask
    """
    if center_freq is None:
        center_freq = (HRV_BANDS["LF"][0] + HRV_BANDS["HF"][1]) / 2

    # Minimaler Frequenzabstand = RES_LIMIT * center_freq
    df_min = RES_LIMIT * center_freq

    # Ausdünnung: nur Frequenzen behalten die >= df_min voneinander entfernt sind
    mask = np.zeros(len(freqs), dtype=bool)
    last_kept = -np.inf
    for i, f in enumerate(freqs):
        if f - last_kept >= df_min:
            mask[i] = True
            last_kept = f

    return freqs[mask], psd[mask], mask

# ---------------------------------------------------------------
# 2. Galois-Projektion
# ---------------------------------------------------------------

def galois_project(ratio: float) -> tuple:
    """
    Projiziert ein Frequenzverhältnis auf das nächste Galois-Raster-Element.

    Returns
    -------
    projected_ratio (float), galois_fraction (Fraction),
    distance (float, relativ), in_grid (bool within RES_LIMIT)
    """
    if ratio <= 0:
        return ratio, Fraction(1), float('inf'), False

    idx = np.argmin(np.abs(GALOIS_FLOATS - ratio))
    nearest = GALOIS_GRID[idx]
    nearest_f = float(nearest)
    dist = abs(ratio - nearest_f) / nearest_f

    return nearest_f, nearest, dist, dist <= RES_LIMIT

def galois_project_band_ratio(psd: np.ndarray, freqs: np.ndarray) -> dict:
    """
    Berechnet LF/HF-Verhältnis und projiziert auf Galois-Raster.

    Returns dict mit:
      lf_power, hf_power, lf_hf_ratio (float),
      galois_ratio (Fraction), galois_depth (int),
      distance (float), in_grid (bool),
      stability (float) — Arnold-Zungenbreite-Schätzung
    """
    lf_mask = (freqs >= HRV_BANDS["LF"][0]) & (freqs < HRV_BANDS["LF"][1])
    hf_mask = (freqs >= HRV_BANDS["HF"][0]) & (freqs < HRV_BANDS["HF"][1])

    lf_power = float(np.trapezoid(psd[lf_mask], freqs[lf_mask])) if lf_mask.any() else 0.0
    hf_power = float(np.trapezoid(psd[hf_mask], freqs[hf_mask])) if hf_mask.any() else 0.0

    if hf_power <= 0:
        return {"lf_power": lf_power, "hf_power": hf_power,
                "lf_hf_ratio": float('inf'), "galois_ratio": None,
                "galois_depth": None, "distance": float('inf'),
                "in_grid": False, "stability": 0.0}

    ratio = lf_power / hf_power
    proj, frac, dist, in_grid = galois_project(ratio)
    depth = galois_depth(frac)
    stability = arnold_tongue_width(frac)

    return {
        "lf_power": lf_power,
        "hf_power": hf_power,
        "lf_hf_ratio": ratio,
        "galois_ratio": frac,
        "galois_depth": depth,
        "distance": dist,
        "in_grid": in_grid,
        "stability": stability,
    }

# ---------------------------------------------------------------
# 3. Orbit-Typ-Klassifikation
# ---------------------------------------------------------------

ORBIT_LABELS = {
    1: "O1 (k=1, GF(3): 2-Limit)",
    2: "O2 (k=2, GF(9): 2,3-Limit)",
    3: "O3 (k=3, GF(27): +13)",   # Leptonentiefe
    4: "O4 (k=4, GF(81): +5)",
    5: "O5 (k=5, GF(243): +11)",
    6: "O6 (k=6, GF(729): +7)",   # CKM/PMNS-Kandidat
}

def classify_orbit(lf_hf_ratio: float) -> dict:
    """
    Klassifiziert ein LF/HF-Verhältnis nach Galois-Orbit-Tiefe.

    Returns dict mit orbit_k, orbit_label, galois_ratio, distance, stability
    """
    proj, frac, dist, in_grid = galois_project(lf_hf_ratio)
    k = galois_depth(frac)
    return {
        "orbit_k": k,
        "orbit_label": ORBIT_LABELS.get(k, f"O? (k={k})"),
        "galois_ratio": frac,
        "galois_float": float(frac),
        "distance": dist,
        "in_grid": in_grid,
        "stability": arnold_tongue_width(frac),
    }

# ---------------------------------------------------------------
# 4. Arnold-Zungenbreite (Dok. 328)
# ---------------------------------------------------------------

def arnold_tongue_width(ratio: Fraction) -> float:
    """
    Schätzt die Arnold-Zungenbreite für ein Frequenzverhältnis p/q.
    Breite ~ 1/(p*q) für einfache Verhältnisse (Farey-Näherung).
    Normiert auf [0,1]: 1 = maximale Stabilität (1:1), 0 = instabil.

    Exakte Berechnung erfordert Kopplungsstärke (hier: strukturelle Breite).
    """
    p, q = ratio.numerator, ratio.denominator
    # Farey-Breite: Abstand zu benachbarten Farey-Termen
    # Näherung: width ~ 2 / (p + q) für kleine p, q
    width = 2.0 / (p + q)
    # Normiert: 1:1 hat width=1, grosse p,q haben width->0
    return min(1.0, width)

# ---------------------------------------------------------------
# 5. Vollständige Pipeline
# ---------------------------------------------------------------

def hrv_galois_pipeline(rr_intervals: np.ndarray,
                         fs: float = 4.0,
                         verbose: bool = True) -> dict:
    """
    Vollständige Galois-HRV-Pipeline.

    Parameters
    ----------
    rr_intervals : RR-Intervalle in ms
    fs           : Resamplingfrequenz (Hz), Standard 4 Hz
    verbose      : Ausgabe

    Returns
    -------
    dict mit allen Kenngrößen
    """
    from scipy import signal as sp_signal
    from scipy.interpolate import interp1d

    # Resampling auf gleichmäßiges Zeitgitter
    t_rr = np.cumsum(rr_intervals) / 1000.0  # ms -> s
    t_grid = np.arange(t_rr[0], t_rr[-1], 1.0 / fs)
    interp = interp1d(t_rr, rr_intervals, kind='cubic',
                      bounds_error=False, fill_value='extrapolate')
    rr_resampled = interp(t_grid)

    # Spektrum (Welch)
    nfft = min(len(rr_resampled), 256)
    freqs, psd = sp_signal.welch(rr_resampled, fs=fs,
                                  nperseg=nfft, nfft=nfft * 4)

    # Auflösungsfilter
    freqs_f, psd_f, mask = resolution_filter(freqs, psd)

    # Band-Kenngrößen
    band_result = galois_project_band_ratio(psd_f, freqs_f)

    # Orbit-Klassifikation
    orbit = classify_orbit(band_result["lf_hf_ratio"]) \
            if band_result["lf_hf_ratio"] != float('inf') else {}

    result = {
        "n_rr": len(rr_intervals),
        "duration_s": float(t_rr[-1] - t_rr[0]),
        "freqs_raw": freqs,
        "psd_raw": psd,
        "freqs_filtered": freqs_f,
        "psd_filtered": psd_f,
        "resolution_limit_pct": RES_LIMIT * 100,
        "farey_qc": FAREY_QC,
        **band_result,
        "orbit": orbit,
    }

    if verbose:
        print(f"\n{'='*55}")
        print(f"  Galois-HRV-Pipeline  (Dok. 359/360, FFGFT)")
        print(f"{'='*55}")
        print(f"  Aufzeichnung:  {result['n_rr']} RR-Intervalle, "
              f"{result['duration_s']:.1f} s")
        print(f"  Auflösung:     Delta_f/f >= {RES_LIMIT*100:.2f}% "
              f"(Farey Q_c = {FAREY_QC:.1f})")
        print(f"\n  LF-Leistung:   {band_result['lf_power']:.4f} ms²")
        print(f"  HF-Leistung:   {band_result['hf_power']:.4f} ms²")
        print(f"  LF/HF (roh):   {band_result['lf_hf_ratio']:.4f}")
        if band_result['galois_ratio']:
            print(f"  LF/HF (Galois):{float(band_result['galois_ratio']):.4f} "
                  f"= {band_result['galois_ratio']}")
            print(f"  Distanz:       {band_result['distance']*100:.2f}%  "
                  f"({'im Raster' if band_result['in_grid'] else 'ausserhalb'})")
            print(f"  Stabilität:    {band_result['stability']:.3f}  "
                  f"(Arnold-Zungenbreite)")
        if orbit:
            print(f"\n  Orbit-Typ:     {orbit['orbit_label']}")
            print(f"  Galois-Tiefe:  k = {orbit['orbit_k']}")
        print(f"{'='*55}\n")

    return result

# ---------------------------------------------------------------
# Selbsttest
# ---------------------------------------------------------------

if __name__ == "__main__":
    print("Galois-HRV-Preprocessing — Selbsttest")
    print(f"Auflösungsgrenze: {RES_LIMIT*100:.4f}%")
    print(f"Farey Q_c: {FAREY_QC:.2f}")
    print(f"Galois-Raster: {len(GALOIS_GRID)} Verhältnisse bis {GALOIS_GRID_SIZE}/{1}")
    print(f"HRV-Bänder: {HRV_BANDS}")
    print()

    # Testfälle Galois-Projektion
    tests = [
        (1.5,  Fraction(3,2),  "Quinte — stabil"),
        (1.333, Fraction(4,3), "Quarte — stabil"),
        (2.0,  Fraction(2,1),  "Oktave — sehr stabil"),
        (1.545, None,          "Zwischenwert"),
        (0.909, Fraction(1,1), "Nahe 1:1"),
    ]
    ok = 0
    for ratio, expected, label in tests:
        proj, frac, dist, in_grid = galois_project(ratio)
        k = galois_depth(frac)
        stab = arnold_tongue_width(frac)
        match = (expected is None) or (frac == expected)
        ok += match
        print(f"  {ratio:.3f} -> {frac} (k={k}, dist={dist*100:.2f}%, "
              f"stab={stab:.3f}) {'OK' if match else 'FAIL'}  [{label}]")

    print()

    # Synthetischer RR-Test
    np.random.seed(42)
    rr_base = 800.0  # ms (75 bpm)
    # Dominante LF-Oszillation bei 0.1 Hz, HF bei 0.25 Hz
    t = np.cumsum(np.ones(300) * rr_base)
    lf = 30 * np.sin(2 * pi * 0.10 * t / 1000)
    hf = 15 * np.sin(2 * pi * 0.25 * t / 1000)
    noise = np.random.normal(0, 5, 300)
    rr = rr_base + lf + hf + noise

    result = hrv_galois_pipeline(rr, verbose=True)

    # Prüfungen
    checks = [
        ("Auflösungsgrenze korrekt", abs(result["resolution_limit_pct"] - 1.333) < 0.01),
        ("LF-Leistung > 0", result["lf_power"] > 0),
        ("HF-Leistung > 0", result["hf_power"] > 0),
        ("LF/HF > 0", result["lf_hf_ratio"] > 0),
        ("Galois-Ratio vorhanden", result["galois_ratio"] is not None),
        ("Orbit-Klassifikation vorhanden", bool(result["orbit"])),
        ("Orbit-k in 1..6", 1 <= result["orbit"].get("orbit_k", 0) <= 6),
        ("Stabilität in [0,1]", 0 <= result["stability"] <= 1),
    ]

    print("Prüfungen:")
    all_ok = True
    for name, cond in checks:
        print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
        all_ok = all_ok and cond

    print(f"\n{'ALLE PRÜFUNGEN OK' if all_ok else 'FEHLER'}")
    raise SystemExit(0 if all_ok else 1)
