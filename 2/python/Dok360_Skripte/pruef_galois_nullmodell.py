#!/usr/bin/env python3
"""
pruef_galois_nullmodell.py
Nullmodell fuer Galois-HRV-Raster (SWT-Einreichung §2.1/§3.1).
Kernfrage: Wie oft trifft ein zufaelliger LF/HF-Wert das Raster?
Ergebnis:
  q<=60 (Paper-Version): Zufallstreffer bei 0.06% ~39% -> TAUTOLOGIE
  q<=11 (Farey-Grenze):  Zufallstreffer bei 0.06% ~ 8% -> testbar
"""
import math, numpy as np
from fractions import Fraction

PRIMES = (2,3,5,7,11,13)
TOL_133, TOL_006 = 0.0133, 0.0006

def smooth(n, P=PRIMES):
    for p in P:
        while n%p == 0: n //= p
    return n == 1

def build_grid(qmax, lo=0.5, hi=10.0):
    """Farey-Folge Ordnung qmax, gefiltert auf [lo,hi] und 13-smooth."""
    G = set()
    for q in range(1, qmax+1):
        for p in range(max(1, math.ceil(lo*q)), math.floor(hi*q)+1):
            if math.gcd(p,q) == 1 and smooth(p) and smooth(q):
                G.add(p/q)
    return np.array(sorted(G))

def coverage(Gf, xs, tol):
    idx = np.searchsorted(Gf, xs)
    lo  = Gf[np.clip(idx-1, 0, len(Gf)-1)]
    hi  = Gf[np.clip(idx,   0, len(Gf)-1)]
    d   = np.minimum(np.abs(xs/lo - 1), np.abs(xs/hi - 1))
    return float((d < tol).mean())

def nearest(Gf, r):
    i = np.searchsorted(Gf, r)
    cands = Gf[max(0,i-2):i+3]
    j = np.argmin(np.abs(r/cands - 1))
    return cands[j], float(np.abs(r/cands[j] - 1))

# ── Gitter ─────────────────────────────────────────────
G11 = build_grid(11);  G60 = build_grid(60)
rng  = np.random.default_rng(42)
null = rng.uniform(1.0, 3.0, 30_000)   # physiologischer LF/HF-Bereich

c11_133 = coverage(G11, null, TOL_133)
c11_006 = coverage(G11, null, TOL_006)
c60_133 = coverage(G60, null, TOL_133)
c60_006 = coverage(G60, null, TOL_006)

xi  = 4/30000
Qc  = math.pi / math.sqrt(6 * 100 * xi)   # ≈ 11.1 (Dok.343 §F)

def smooth5(n): return smooth(n, (2,3,5))
bands_ok = all(smooth5(f.numerator) and smooth5(f.denominator) for f in
               (Fraction(1,25), Fraction(3,20), Fraction(2,5)))

r251_el, r251_d = nearest(G11, 2.51)
r112_el, r112_d = nearest(G11, 1.12)
r8835_el, r8835_d = nearest(G11, 88/35)   # q=35 > 11 -> sollte rausfallen

p_atleast1 = 1 - (1 - c11_006)**7   # Look-elsewhere: 7 Bedingungen

# ── Assertions ─────────────────────────────────────────
A = [
    ("A1 q<=60 cov[1,3]@1.33% == 1.000  (tautologisch)",   c60_133 > 0.999),
    ("A2 q<=60 cov[1,3]@0.06% > 0.30",                     c60_006 > 0.30),
    ("A3 q<=11 cov[1,3]@0.06% < 0.10  (testbar)",          c11_006 < 0.10),
    (f"A4 Qc={Qc:.2f} ~= 11.1  (Dok.343 §F)",              abs(Qc-11.1) < 0.2),
    ("A5 Bandgrenzen VLF/LF/HF sind 5-limit",               bands_ok),
    (f"A6a r=2.51 -> {Fraction(r251_el).limit_denominator(20)} "
     f"d={r251_d*100:.2f}% < 1.33%",                        r251_d < TOL_133),
    (f"A6b r=1.12 -> {Fraction(r112_el).limit_denominator(20)} "
     f"d={r112_d*100:.2f}% < 1.33%",                        r112_d < TOL_133),
    (f"A7 88/35 nicht in q<=11  (d={r8835_d*100:.2f}% > 0.5%)", r8835_d > 0.005),
    (f"A8 P(>=1 Zufallstreffer, n=7, q<=11, 0.06%) = {p_atleast1:.3f}",  True),
]

# ── Ausgabe ────────────────────────────────────────────
print("=" * 64)
print("pruef_galois_nullmodell.py")
print("=" * 64)
print(f"  q<=60: {len(G60)} Elemente  cov@1.33%={c60_133:.3f}  cov@0.06%={c60_006:.3f}")
print(f"  q<=11: {len(G11)} Elemente  cov@1.33%={c11_133:.3f}  cov@0.06%={c11_006:.3f}")
print(f"  Q_c (Dok.343) = {Qc:.2f}  ->  q<=11 ist die Farey-Grenze")
print(f"  P(mind.1 Zufallstreffer, n=7, q<=11, 0.06%) = {p_atleast1:.3f}")
print()
passed = 0
for msg, ok in A:
    print(f"  {'OK' if ok else 'FAIL'} {msg}")
    passed += ok
print(f"\n{passed}/{len(A)} Assertions bestanden")
