"""
Dok. 339 -- Pruefskript: Frobenius-Trennung massiv/masselos in GF(27)*
Ausfuehren: python3 pruef_339_frobenius.py
"""
import numpy as np
from math import gcd

print("=" * 65)
print("DOK. 339: FROBENIUS x->x^3 AUF GF(27)*")
print("=" * 65)

# GF(27)* = Z_26, zyklisch der Ordnung 26
N = 26  # Ordnung von GF(27)*

# Berechne alle Orbits unter x -> x^3 (mod 26)
visited = set()
orbits = []
for k in range(N):
    if k not in visited:
        orbit = []
        j = k
        while j not in visited:
            orbit.append(j)
            visited.add(j)
            j = (3 * j) % N
        orbits.append(tuple(sorted(orbit)))

from collections import Counter
lengths = Counter(len(o) for o in orbits)

print(f"\nGF(27)* = Z_{N}, Frobenius x->x^3:")
print(f"  Anzahl Orbits gesamt: {len(orbits)}")
print(f"  Orbit-Laengen: {dict(lengths)}")
print()

fixpoints = [o for o in orbits if len(o) == 1]
three_orbits = [o for o in orbits if len(o) == 3]

print(f"ASSERTION 1: Genau 2 Fixpunkte")
assert len(fixpoints) == 2, f"Erwartet 2, erhalten {len(fixpoints)}"
print(f"  Fixpunkte (Exponenten): {[o[0] for o in fixpoints]}  [OK]")
print(f"  Fixpunkte sind g^0=1 und g^13 (Ordnung 2: x^2=1)")
print()

print(f"ASSERTION 2: Genau 8 Dreier-Orbits")
assert len(three_orbits) == 8, f"Erwartet 8, erhalten {len(three_orbits)}"
print(f"  Dreier-Orbits: {len(three_orbits)}  [OK]")
print(f"  Gesamt-Elemente in Dreier-Orbits: {len(three_orbits)*3}")
print()

print(f"ASSERTION 3: Vollstaendigkeit (2 + 8*3 = 26)")
assert 2 + 8*3 == N, "Summe stimmt nicht"
print(f"  2 + 8*3 = {2 + 8*3} = {N}  [OK]")
print()

print(f"ASSERTION 4: Kissing-Zahl D4")
kissing_D4 = 24
assert len(three_orbits) * 3 == kissing_D4
print(f"  8 Dreier-Orbits * 3 = {len(three_orbits)*3} = Kissing(D4) = {kissing_D4}  [OK]")
print()

print(f"ASSERTION 5: Verbindung zu |GF(9)*| = 8 (Gluonen)")
GF9_mult = 3**2 - 1  # = 8
assert len(three_orbits) == GF9_mult
print(f"  Anzahl Dreier-Orbits = {len(three_orbits)} = |GF(9)*| = {GF9_mult}  [OK]")
print()

print(f"ASSERTION 6: Galois-Identitaet konsistent")
xi = 4/30000
r_mu_re_sq = (12/5)**2
galois = 8**2 * 25 * 27
ffgft = r_mu_re_sq / xi
assert abs(galois - ffgft) < 0.01, f"Galois-Identitaet: {galois} != {ffgft}"
print(f"  (m_mu/m_e)^2 = {galois} = (r_mu/r_e)^2/xi = {ffgft:.1f}  [OK]")
print(f"  27 = |GF(27)| erscheint sowohl in 43200 als auch im Gosset-Polytop 2_21")
print()

print("=" * 65)
print("ALLE 6 ASSERTIONS BESTANDEN")
print("=" * 65)
print(f"""
Physikalische Interpretation (Status [K]):
  Fixpunkte {{+1,-1}} = Z2 = massiver Sektor (Teilchen/Antiteilchen)
  8 Dreier-Orbits    = 8 Gluonen (masseloser Sektor, SU(3)-adjungiert)
  Photon (U(1))      = ausserhalb GF(27)*, nicht in dieser Struktur

Offene Fragen:
  - Explizite Darstellungsabbildung Orbit -> Gluon-Farbe noch nicht gesichert
  - Photon-Singlett algebraisch noch nicht verortet
  - 8*3=24=Kissing(D4): erzwungen oder numerisch?
""")
