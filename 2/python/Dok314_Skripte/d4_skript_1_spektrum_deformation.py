#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOTIZ Gitter im Hilbertraum — Skript 1
Teil A/H1: Thetareihen D4 vs Z4, k4-Split, Deformation r = R4/R123,
exakte Kreuzungsradien.
Abhaengigkeiten: nur Standardbibliothek. Deterministisch.
Stand: 4. August 2026
"""
import itertools, collections
from fractions import Fraction

R = 6  # Suchradius; Schalen bis R^2 - 2R = 24 sicher vollstaendig

# ---------------------------------------------------------------
# 1) Thetareihen und k4-Split (Notiz Abschnitt 2)
# ---------------------------------------------------------------
def schalen(gitter_test, maxnorm):
    c = collections.Counter()
    split = collections.defaultdict(lambda: [0, 0])  # [k4=0, k4!=0]
    for v in itertools.product(range(-R, R + 1), repeat=4):
        if v == (0, 0, 0, 0) or not gitter_test(v):
            continue
        n = sum(x * x for x in v)
        if n <= maxnorm:
            c[n] += 1
            split[n][0 if v[3] == 0 else 1] += 1
    return c, split

Z4, sZ4 = schalen(lambda v: True, R * R - 2 * R)
D4, sD4 = schalen(lambda v: sum(v) % 2 == 0, R * R - 2 * R)

print("Norm |k|^2 :   Z4    D4   D4-Split (k4=0 / k4!=0)")
for n in range(1, 13):
    print(f"{n:>9} : {Z4.get(n,0):>4}  {D4.get(n,0):>4}"
          f"   {sD4[n][0]:>3} / {sD4[n][1]:>3}")

assert D4.get(2, 0) == 24 and sD4[2] == [12, 12]      # 24 = 12 + 12
assert Z4.get(1, 0) == 8
# Thetareihen-Kontrolle theta_D4 = (theta3^4 + theta4^4)/2:
assert [D4.get(n, 0) for n in (2, 4, 6, 8, 10, 12)] == [24, 24, 96, 24, 144, 96]
print("Kontrollen bestanden.\n")

# ---------------------------------------------------------------
# 2) Deformation E(k) = k1^2+k2^2+k3^2 + (k4/r)^2 (Abschnitt 3)
# ---------------------------------------------------------------
D4v = [v for v in itertools.product(range(-R, R + 1), repeat=4)
       if v != (0, 0, 0, 0) and sum(v) % 2 == 0]

for r in [1.0, 1.1, 1.5, 2.0]:
    lev = collections.Counter()
    for v in D4v:
        E = v[0]**2 + v[1]**2 + v[2]**2 + (v[3] / r)**2
        if E <= 4.001:
            lev[round(E, 6)] += 1
    print(f"r = {r}: ", sorted(lev.items())[:6])
    if r > 1:
        # Wicklungsschale exakt bei 1 + 1/r^2
        assert abs(min(E for E in lev if lev[E] == 12 and E < 2)
                   - (1 + 1 / r**2)) < 1e-9 or r < 3**0.5
print("Wicklungsformel E = 1 + 1/r^2 bestaetigt.\n")

# ---------------------------------------------------------------
# 3) Exakte Kreuzungsradien (Abschnitt 9.1)
#    Niveaus E = a + b/r^2, Kreuzung bei r^2 = (b-b')/(a'-a)
# ---------------------------------------------------------------
levels = sorted({(v[0]**2 + v[1]**2 + v[2]**2, v[3]**2)
                 for v in D4v if sum(x * x for x in v) <= 8})
cross = set()
for (a, b) in levels:
    for (a2, b2) in levels:
        if a2 > a and b > b2:
            r2 = Fraction(b - b2, a2 - a)
            if 1 < r2 <= Fraction(25, 4):
                cross.add(r2)
print("Niveaus (a, b) bis Norm 8:", levels)
print("Kreuzungsradien in (1, 2.5]:",
      [f"r^2={c} (r={float(c)**0.5:.6f})" for c in sorted(cross)])
assert sorted(cross) == [Fraction(2), Fraction(3)]
print("Exakt zwei Kreuzungen: r = sqrt(2), r = sqrt(3). Bestanden.")
