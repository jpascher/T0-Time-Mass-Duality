#!/usr/bin/env python3
"""
ffgft_311_vier_auf_drei.py
--------------------------
Prueft die Zahlen aus Dok. 311 (Vier auf drei). Standardbibliothek.
"""

import itertools, math, collections

PHI = (1 + 5**0.5) / 2
LNK = math.log(75/74)

print("== Gitterzaehlung ==")
D4 = [v for v in itertools.product([-1, 0, 1], repeat=4)
      if sum(x*x for x in v) == 2]
D3 = [v for v in itertools.product([-1, 0, 1], repeat=3)
      if sum(x*x for x in v) == 2]
print(f"  |D4 kuerzeste|            = {len(D4)}   (erwartet 24)")
print(f"  davon x4 = 0              = {sum(1 for v in D4 if v[3]==0)}   (erwartet 12)")
print(f"  davon x4 != 0             = {sum(1 for v in D4 if v[3]!=0)}   (erwartet 12)")
print(f"  |D3 = FCC kuerzeste|      = {len(D3)}   (erwartet 12)")
print(f"  Projektionsbilder         = {len(set(v[:3] for v in D4))}   (erwartet 18)")
print(f"  Wicklungsrichtungen       = {dict(collections.Counter(v[3] for v in D4 if v[3]!=0))}")

print()
print("== Packungsdichten ==")
d4 = math.pi**2 / 16
d3 = math.pi / (3 * 2**0.5)
print(f"  D4: pi^2/16               = {d4:.6f}")
print(f"  D3: pi/(3 sqrt2)          = {d3:.6f}")

print()
print("== Welche Dichte gehoert in K^-36 ==")
for name, kehr in (("D4  16/pi^2 ", 16/math.pi**2), ("D3  3sqrt2/pi", 3*2**0.5/math.pi)):
    n = math.log(kehr) / LNK
    print(f"  {name}  Kehrwert = {kehr:.7f}  Exponent = {n:8.4f}"
          f"  Abstand zu 36,0909 = {abs(n-36.0909):7.3f}"
          f"  zur Ganzzahl = {abs(n-round(n)):.4f}")
print(f"  (75/74)^36 = {(75/74)**36:.6f}  gegen 16/pi^2 = {16/math.pi**2:.6f}"
      f"  ({((75/74)**36/(16/math.pi**2)-1)*100:+.3f} %)")
print(f"  (75/74)^22 = {(75/74)**22:.6f}  gegen 3sqrt2/pi = {3*2**0.5/math.pi:.6f}"
      f"  ({((75/74)**22/(3*2**0.5/math.pi)-1)*100:+.3f} %)")

print()
print("== Projektionslaengen bei Richtung (1, phi, 0) ==")
e = (1, PHI, 0)
norm = math.sqrt(sum(x*x for x in e))
for v in ((1,0,0), (0,1,0), (1,1,0), (1,-1,0)):
    p = sum(a*b for a, b in zip(v, e)) / norm
    print(f"  {v}  ->  {p:+.6f}")

print()
print("== A120-Gewichte (Fuenffach-Drehung) ==")
p0 = 2/9
p2 = (5 - 3*PHI) / 9
p1 = (2 + 3*PHI) / 9
print(f"  p0 = 2/9          = {p0:.7f}   (rational)")
print(f"  p2 = (5-3phi)/9   = {p2:.7f}")
print(f"  p1 = (2+3phi)/9   = {p1:.7f}")
print(f"  Summe             = {p0+p1+p2:.7f}")

print()
print("== Ikosaeder ==")
print(f"  |Ecke| = sqrt(1+phi^2)    = {math.sqrt(1+PHI**2):.7f}")
print(f"  Umkugel/Kante             = {math.sqrt(1+PHI**2)/2:.7f}")
print(f"  sqrt(phi*sqrt5)/2         = {math.sqrt(PHI*math.sqrt(5))/2:.7f}")

print()
print("== Schaerfe der Zuordnung: Nachbar-Exponenten 34..38 ==")
for n in range(34, 39):
    v = (75/74)**n
    print(f"  n = {n}   (75/74)^n = {v:.6f}   gegen 16/pi^2: "
          f"{(v/(16/math.pi**2)-1)*100:+.3f} %")
print("  Fenster mit zwei Raendern: nur n = 36 trifft; Nachbarn ~100x weiter.")
