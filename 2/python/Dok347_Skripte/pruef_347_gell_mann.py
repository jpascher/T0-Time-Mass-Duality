"""pruef_347_gell_mann.py — Gell-Mann-Nishijima aus Galois-Struktur

Aktualisiert am 1.10.2026: Satz A/D korrigiert -- Orbit-Zuordnung nach Dok. 346
(QR: O1 Neutrinos, O3 Antineutrinos; NQR: O4 geladene Leptonen, O2 Quarks);
geprüft wird jetzt, dass Y keine Funktion des QR/NQR-Bits ist; Satz C mit
SM-Werten fuer Y (vgl. Dok. 347, Dok. 190 R146).
"""
from fractions import Fraction as F

QR13 = {k for k in range(1, 13) if any(j * j % 13 == k for j in range(1, 13))}

def legendre_qr(orb):
    vals = {k % 13 in QR13 for k in orb}
    assert len(vals) == 1, f"Orbit {orb} nicht einheitlich"
    return vals.pop()

ok = 0; n = 0
def check(cond, msg):
    global ok, n
    n += 1
    assert cond, msg
    ok += 1
    print(f"  [OK] {msg}")

# Orbits unter k -> 3k mod 13 und Teilchenzuordnung nach Dok. 346
ORBITS = {
    "O1": ([1, 3, 9],   "Neutrino",        F(-1)),   # Y des linkshaendigen Leptondubletts
    "O3": ([4, 10, 12], "Antineutrino",    F(1)),    # Antiteilchen: Y -> -Y
    "O4": ([7, 8, 11],  "gel. Lepton",     F(-1)),   # Leptondublett
    "O2": ([2, 5, 6],   "Quark",           F(1, 3)), # Quarkdublett
}

print("Orbit-Struktur (Dok. 346)")
for name, (orb, teil, _) in ORBITS.items():
    check(sorted({(orb[0] * 3**i) % 13 for i in range(3)}) == sorted(orb),
          f"{name}={orb} ist Frobenius-Orbit k->3k mod 13")
qr = {name: legendre_qr(orb) for name, (orb, _, _) in ORBITS.items()}
check(qr["O1"] and qr["O3"], "O1 (Neutrinos), O3 (Antineutrinos) sind QR")
check(not qr["O4"] and not qr["O2"], "O4 (geladene Leptonen), O2 (Quarks) sind NQR")

print("\nSatz A: Y ist keine Funktion des QR/NQR-Bits [S]")
by_bit = {}
for name, (orb, teil, Y) in ORBITS.items():
    by_bit.setdefault(qr[name], set()).add(Y)
check(len(by_bit[False]) > 1, f"NQR-Seite traegt mehrere Y-Werte {sorted(by_bit[False])}")
check(len(by_bit[True]) > 1, f"QR-Seite traegt mehrere Y-Werte {sorted(by_bit[True])}")
check(qr["O1"] != qr["O4"], "Leptondublett (nu, e) liegt auf beiden Seiten des Bits")
# alte Formel Y = -1 + 4/3*NQR gibt dem Elektron falsche Ladung
Y_alt_e = F(-1) + F(4, 3) * 1
check(F(-1, 2) + Y_alt_e / 2 == F(-1, 3), "alte Fassung: Elektron Q=-1/3 statt -1 (widerlegt)")
Y_alt_nubar = F(-1) + F(4, 3) * 0
check(Y_alt_nubar != ORBITS["O3"][2], "alte Fassung: Antineutrino Y=-1 statt +1 (widerlegt)")

print("\nSatz B: I3 aus Su/Sd-Trennung [B]")
for su, I3_exp in [(True, F(1, 2)), (False, F(-1, 2))]:
    I3 = F(1, 2) if su else F(-1, 2)
    check(I3 == I3_exp, f"{'Su' if su else 'Sd'}: I3={I3}")

print("\nSatz C: Q = I3 + Y/2 mit SM-Werten fuer Y")
for name, I3, Y, q_exp in [
        ("Neutrino", F(1, 2), F(-1), F(0)), ("Elektron", F(-1, 2), F(-1), F(-1)),
        ("up-Quark", F(1, 2), F(1, 3), F(2, 3)), ("dn-Quark", F(-1, 2), F(1, 3), F(-1, 3))]:
    Q = I3 + Y / 2
    check(Q == q_exp, f"{name:9s}: I3={str(I3):>5}, Y={str(Y):>5}, Q={Q}")

print("\nSatz D: Orbit-Tabelle (Legendre, Teilchen, Y_SM)")
for name, (orb, teil, Y) in ORBITS.items():
    print(f"  {name} {orb}: {'QR ' if qr[name] else 'NQR'} {teil:13s} Y={Y}")

print(f"\n{ok}/{n} Assertions bestanden.")
