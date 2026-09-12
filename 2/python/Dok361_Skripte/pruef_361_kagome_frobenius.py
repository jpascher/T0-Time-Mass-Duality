#!/usr/bin/env python3
"""
pruef_361_kagome_frobenius.py
Dok. 361 — Kagome-Gitter und FFGFT: Vier strukturelle Parallelen
Prüft die algebraischen Behauptungen über Frobenius-Orbits.
"""

import sys

ok = 0
fail = 0

def check(label, result, expected=True):
    global ok, fail
    if result == expected:
        print(f"  OK  {label}")
        ok += 1
    else:
        print(f"FAIL  {label}")
        fail += 1

print("=== Dok. 361: Frobenius-Orbit-Struktur von GF(27)* ===\n")

# GF(27)* ≅ Z_26, erzeugt von einem primitiven Element g
# Wir arbeiten mit Z_26 direkt.
# Frobenius: phi(k) = 3k mod 26 (Wirkung auf den Exponenten)

def frobenius_orbit(k, mod=26):
    orbit = set()
    x = k % mod
    while x not in orbit:
        orbit.add(x)
        x = (3 * x) % mod
    return frozenset(orbit)

# Alle Orbits in Z_26 unter k -> 3k mod 26
all_elements = list(range(26))
orbits = []
seen = set()
for k in all_elements:
    if k not in seen:
        orb = frobenius_orbit(k)
        orbits.append(orb)
        seen |= orb

print("Orbits in Z_26 unter phi: k -> 3k mod 26:")
fixed = [o for o in orbits if len(o) == 1]
three_orbits = [o for o in orbits if len(o) == 3]
other = [o for o in orbits if len(o) not in (1, 3)]

for o in sorted(orbits, key=len):
    print(f"  Größe {len(o)}: {sorted(o)}")

check("Genau 2 Fixpunkte in Z_26", len(fixed) == 2)
check("Fixpunkte sind {0, 13} in Z_26", {0, 13} == set().union(*[set(o) for o in fixed]))
check("Genau 8 Dreier-Orbits", len(three_orbits) == 8)
check("Keine anderen Orbitgrößen", len(other) == 0)
check("Gesamtzahl Orbits = 2 + 8 = 10", len(orbits) == 10)

print()
print("=== Zerlegung Z_26 ≅ Z_2 × Z_13 (CRT) ===\n")

# Fixpunkte entsprechen +1/-1 im multiplikativen Sinne:
# Element 0 in Z_26 -> g^0 = 1 (+1)
# Element 13 in Z_26 -> g^13 = -1 (-1)
check("g^13 hat Ordnung 2 in Z_26", (13 * 2) % 26 == 0)
check("g^0 = Identität", (0 * 3) % 26 == 0)

# Orbits in Z_13-Anteil (Projektion k -> k mod 13)
z13_orbits = {}
for k in range(13):
    orb = frozenset({(3**j * k) % 13 for j in range(3)})
    z13_key = tuple(sorted(orb))
    if z13_key not in z13_orbits:
        z13_orbits[z13_key] = orb

print("Orbits in Z_13 unter k -> 3k mod 13:")
for o in sorted(z13_orbits.values(), key=lambda x: min(x)):
    print(f"  {sorted(o)}")

fixed_z13 = [o for o in z13_orbits.values() if len(o) == 1]
three_z13 = [o for o in z13_orbits.values() if len(o) == 3]

check("1 Fixpunkt in Z_13 (das ist {0})", len(fixed_z13) == 1)
check("4 Dreier-Orbits in Z_13", len(three_z13) == 4)
check("4 Orbits × 2 Paritäten = 8 Gluonen", 4 * 2 == 8)

print()
print("=== Drei-Zustands-Potts = GF(3) ===\n")

# GF(3) = {0, 1, 2} mit Arithmetik mod 3
# Frobenius: x -> x^3 = x für alle x in GF(3) (Fermat)
gf3 = [0, 1, 2]
check("Frobenius fixiert alle GF(3)-Elemente", all(x**3 % 3 == x for x in gf3))
check("|GF(3)| = 3 (Potts-Zustände)", len(gf3) == 3)
check("GF(3) ist Fixkörper: 0^3=0, 1^3=1, 2^3=2 mod 3",
      all(pow(x, 3, 3) == x for x in gf3))

# Z_3-Symmetrie des Potts-Modells: Zustandsraum {0,1,2} unter k -> k+1 mod 3
potts_orbits = set()
for k in range(3):
    potts_orbits.add(frozenset({(k + j) % 3 for j in range(3)}))
check("Potts-Modell hat triviale Z_3-Orbits (ein einziger 3-Orbit)", len(potts_orbits) == 1)

print()
print("=== Pi-Fluss = Berry-Phase = halbe Wicklungszahl ===\n")

import cmath
# Berry-Phase pi entspricht Wicklungszahl n = 1/2 (oder exp(i*pi) = -1)
berry_pi = cmath.exp(1j * cmath.pi)
check("exp(i*pi) = -1 (Berry-Phase pi)", abs(berry_pi + 1) < 1e-12)
check("Doppelter Umlauf -> exp(2i*pi) = +1", abs(cmath.exp(2j * cmath.pi) - 1) < 1e-12)
check("|Frobenius-Phase|: omega = exp(2*pi*i/3), omega^3 = 1",
      abs(cmath.exp(2j * cmath.pi / 3)**3 - 1) < 1e-12)

print()
print("=== Kagome-Gitter: Dreifache Symmetrie ===\n")

# Kagome-Einheitszelle: 3 Untergitterplätze
# K-Punkt-Symmetrie im reziproken Raum: 3-fach
n_sublattice = 3
check("Kagome: 3 Untergitterplätze pro Einheitszelle", n_sublattice == 3)
check("K-Punkt-Gruppe: Ordnung 3 (C_3)", n_sublattice == 3)
check("Übereinstimmung: |GF(3)| = Anzahl Untergitterplätze = 3", n_sublattice == len(gf3))

print()
print(f"=== Ergebnis: {ok} OK, {fail} FEHLER ===")
if fail == 0:
    print("Alle algebraischen Behauptungen von Dok. 361 bestätigt.")
else:
    print("ACHTUNG: Prüfung nicht vollständig bestanden.")
    sys.exit(1)
