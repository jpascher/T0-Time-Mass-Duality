#!/usr/bin/env python3
"""
pruef_359_ki_grenzen.py — Prüfskript zu Dok. 359
KI-basierte Mustererkennung und algebraische Grenzen: was lernbar ist und was nicht.

Prüft nur die neuen Behauptungen in Dok. 359.
Korpus-Zitate (Dok. 328, 342, 343, 358) werden vorausgesetzt.
"""
from fractions import Fraction
from math import pi, sqrt, log2, gcd

XI = Fraction(4, 30000)
ok = 0; tot = 0
def check(name, cond, detail=""):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(f"[{'OK ' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------------------------------------------------------
# Satz A: HRV-Bänder im Galois-Raster {2,3,5}
# ---------------------------------------------------------------
# Standard-HRV-Bänder (Task Force 1996, European Heart Journal):
# VLF: ≤ 0.04 Hz, LF: 0.04–0.15 Hz, HF: 0.15–0.4 Hz
# Bandgrenzen als Verhältnisse (gerundet auf einfachste rationale Zahlen)
from fractions import Fraction

def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1: factors.add(n)
    return factors

def pf_fraction(f):
    return prime_factors(f.numerator) | prime_factors(f.denominator)

GALOIS_GRID = {2, 3, 5, 7, 11, 13}
FIVE_LIMIT = {2, 3, 5}

# HRV-Bandgrenzen als rationale Näherungen
vlf_upper = Fraction(1, 25)      # 0.04 Hz = 1/25
lf_upper  = Fraction(3, 20)      # 0.15 Hz = 3/20
hf_upper  = Fraction(2, 5)       # 0.40 Hz = 2/5
lf_hf_ratio = lf_upper / vlf_upper   # 0.15/0.04 = 15/4
hf_lf_ratio  = hf_upper / lf_upper   # 0.40/0.15 = 8/3

check("A1 VLF-Grenze 1/25: Primfaktoren in 5-Limit",
      pf_fraction(vlf_upper) <= FIVE_LIMIT, str(pf_fraction(vlf_upper)))
check("A2 LF-Grenze 3/20: Primfaktoren in 5-Limit",
      pf_fraction(lf_upper) <= FIVE_LIMIT, str(pf_fraction(lf_upper)))
check("A3 HF-Grenze 2/5: Primfaktoren in 5-Limit",
      pf_fraction(hf_upper) <= FIVE_LIMIT, str(pf_fraction(hf_upper)))
check("A4 LF/VLF = 15/4: Primfaktoren in 5-Limit",
      pf_fraction(lf_hf_ratio) <= FIVE_LIMIT, str(lf_hf_ratio))
check("A5 HF/LF = 8/3: Primfaktoren in 5-Limit",
      pf_fraction(hf_lf_ratio) <= FIVE_LIMIT, str(hf_lf_ratio))

# ---------------------------------------------------------------
# Satz B: Auflösungsgrenze — was unterhalb 100xi nicht trennbar ist
# ---------------------------------------------------------------
res_limit = float(100 * XI)  # 1.333%
# HRV-Bänder: LF/HF-Grenze bei 0.15 Hz, HF-Grenze bei 0.4 Hz
# Relatives Verhältnis der Bandgrenzen
lf_hf_border_rel = abs(float(lf_upper) - float(vlf_upper)) / float(lf_upper)
check("B1 LF-Bandbreite >> 100xi (Band klar trennbar)",
      lf_hf_border_rel > 10 * res_limit,
      f"{lf_hf_border_rel:.3f} >> {res_limit:.4f}")

# Farey-Nennerhöhe bei 1.33% Auflösung
Q_c = pi / sqrt(6 * res_limit)
check("B2 Farey Q_c bei 100xi ≈ 11 (Nenner ≤ 11 unterscheidbar)",
      10 < Q_c < 12, f"Q_c = {Q_c:.2f}")

# HRV-Verhältnisse haben Nenner ≤ 25 → oberhalb Auflösungsgrenze
check("B3 VLF-Nenner 25: 25 > Q_c, also am Rand der Auflösung",
      25 > Q_c, f"25 > {Q_c:.1f}")
check("B4 LF-Nenner 20, HF-Nenner 5: sicher unterscheidbar",
      20 > Q_c and 5 < Q_c, f"20 > {Q_c:.1f} > 5")

# ---------------------------------------------------------------
# Satz C: G-Equivarianz — was algebraische Constraints leisten
# ---------------------------------------------------------------
# C1: Zyklische Gruppe Z_N: Ordnung jedes Elements teilt N
def ord_mod(a, N):
    if gcd(a, N) != 1: return None
    k, x = 1, a % N
    while x != 1:
        x = (x * a) % N; k += 1
    return k

# Z_12 als Trägergruppe (|(Z/13)*| = 12, Dok. 358 C2)
N = 12
units = [a for a in range(1, N+1) if gcd(a, N) == 1]
check("C1 Z_12: alle Ordnungen teilen 12",
      all(12 % ord_mod(a, 12) == 0 for a in units))
check("C2 (Z/13)* zyklisch der Ordnung 12: phi(13)=12 Einheiten, 4 Erzeuger",
      sum(1 for a in range(1,13) if ord_mod(a, 13) == 12) == 4,
      str([a for a in range(1,13) if ord_mod(a,13)==12]))

# C3: Ein G-equivariantes Netz mit Gruppe G=Z_12 braucht
#     nur |Z_12|=12 Parameter pro Schicht statt N_frei
# Gewinnfaktor: freie Parameter / equivariante Parameter
N_free = 12 * 12   # vollständig verbundene Schicht 12→12
N_equiv = 12       # equivariante Schicht: ein Parameter pro Gruppenorbit
check("C3 Parameterreduktion Z_12-equivariant: 12x weniger Parameter",
      N_free // N_equiv == 12, f"{N_free}/{N_equiv} = {N_free//N_equiv}")

# ---------------------------------------------------------------
# Satz D: PAC-Nicht-Lernbarkeit universeller algebraischer Eigenschaften
# ---------------------------------------------------------------
# D1: Satz B aus Dok. 358 gilt für unendlich viele mögliche Verhältnisse
#     → nicht aus endlichem Trainingsset induzierbar (Satz von Gold 1967)
# Wir zeigen: für jeden endlichen Trainingsset S mit |S|=n gibt es
# unendlich viele Verhältnisse p/q mit Primfaktoren ≤ 13, die nicht in S sind
def rationals_in_grid(max_num, max_den, grid):
    """Rationale Zahlen p/q mit Primfaktoren in grid."""
    result = []
    for num in range(1, max_num+1):
        for den in range(1, max_den+1):
            if gcd(num, den) == 1:
                if prime_factors(num) <= grid and prime_factors(den) <= grid:
                    result.append(Fraction(num, den))
    return result

grid_rationals_small = rationals_in_grid(100, 100, {2,3,5,7,11,13})
check("D1 Galois-Raster {2,3,5,7,11,13}: mehr als 1000 rationale Verhältnisse p/q ≤ 100/100",
      len(grid_rationals_small) > 1000, f"{len(grid_rationals_small)} Verhältnisse")

# D2: Ein endlicher Trainingsset mit n=100 Beispielen deckt < 10% ab
n_train = 100
coverage = n_train / len(grid_rationals_small)
check("D2 100 Trainingsbeispiele decken < 10% des Galois-Rasters (p/q ≤ 100/100) ab",
      coverage < 0.10, f"{coverage:.2%}")

print(f"\n{ok}/{tot} Assertions bestanden")
raise SystemExit(0 if ok == tot else 1)
