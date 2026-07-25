#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a273_rechenkugel.py  --  Pruefskript zu FFGFT A273 "Die Rechenkugel"

Prueft alle numerischen Aussagen des Dokuments mit Assertions.
Jede Setzung (Parameterwahl) ist als SETZUNG markiert und frei aenderbar;
jedes Ergebnis folgt daraus rechnerisch.

Autor: Johann Pascher -- ORCID 0009-0000-6518-4064
Aufruf:  python3 a273_rechenkugel.py
"""

import math

# ============================================================
# Naturkonstanten (CODATA 2018, exakt definiert)
# ============================================================
k_B = 1.380649e-23        # J/K, exakt seit SI-Revision 2019
h   = 6.62607015e-34      # J s, exakt
g   = 9.80665             # m/s^2, Normfallbeschleunigung

# ============================================================
# SETZUNGEN -- deklarierte Parameter, keine Messwerte
# ============================================================
T          = 300.0        # K    Umgebungstemperatur
m_kugel    = 0.5e-3       # kg   Masse einer Abakuskugel
d_weg      = 0.01         # m    Verschiebeweg (1 cm)
mu_reib    = 0.3          # --   Reibungszahl Kugel/Stab
M_molar    = 0.100        # kg/mol  molare Masse (Holz/Kunststoff, Naeherung)
S_molar    = 50.0         # J/(mol K)  molare Entropie eines Festkoerpers (Naeherung)
E_cmos_lo  = 1e-17        # J    CMOS-Schaltvorgang, untere Angabe (A271)
E_cmos_hi  = 1e-16        # J    CMOS-Schaltvorgang, obere Angabe (A271)

results = {}

def check(name, value, expected, rel_tol=0.02, unit=""):
    """Vergleicht Rechenwert mit der im Dokument gedruckten Zahl."""
    ok = math.isclose(value, expected, rel_tol=rel_tol)
    results[name] = (value, expected, ok)
    status = "OK " if ok else "ABW"
    print(f"[{status}] {name:<52} {value:12.4e} {unit}  (Dok: {expected:.4e})")
    assert ok, f"{name}: gerechnet {value:.6e}, im Dokument {expected:.6e}"


print("=" * 78)
print("A273 -- Die Rechenkugel: Pruefskript")
print("=" * 78)
print(f"Setzungen: T = {T} K, m = {m_kugel*1e3} g, d = {d_weg*100} cm, mu = {mu_reib}")
print("-" * 78)

# ------------------------------------------------------------
# Check 1 -- Landauer-Grenze bei T
# ------------------------------------------------------------
Q_landauer = k_B * T * math.log(2)
check("1  Landauer-Grenze kT ln2 bei 300 K", Q_landauer, 2.871e-21, unit="J")

# ------------------------------------------------------------
# Check 2 -- Arbeit beim Verschieben einer Abakuskugel
#            Gleitreibung: W = mu * m * g * d
# ------------------------------------------------------------
W_kugel = mu_reib * m_kugel * g * d_weg
check("2  Arbeit je Kugelverschiebung", W_kugel, 1.471e-5, unit="J")

# ------------------------------------------------------------
# Check 3 -- Vielfaches der Landauer-Grenze: Kugel
# ------------------------------------------------------------
faktor_kugel = W_kugel / Q_landauer
check("3  Kugel als Vielfaches von kT ln2", faktor_kugel, 5.126e15)

# ------------------------------------------------------------
# Check 4 -- Vielfaches der Landauer-Grenze: CMOS
# ------------------------------------------------------------
faktor_cmos_lo = E_cmos_lo / Q_landauer
faktor_cmos_hi = E_cmos_hi / Q_landauer
check("4a CMOS 1e-17 J als Vielfaches", faktor_cmos_lo, 3.483e3)
check("4b CMOS 1e-16 J als Vielfaches", faktor_cmos_hi, 3.483e4)

# ------------------------------------------------------------
# Check 5 -- Abstand Kugel/CMOS: elf Groessenordnungen
# ------------------------------------------------------------
abstand = faktor_kugel / faktor_cmos_hi
check("5  Kugel/CMOS-Abstand (Dekaden)", math.log10(abstand), 11.17, rel_tol=0.02)

# ------------------------------------------------------------
# Check 6 -- Eigenentropie der Kugel
#            n = m/M ; S = n * S_molar
# ------------------------------------------------------------
n_mol   = m_kugel / M_molar
S_kugel = n_mol * S_molar
check("6a Eigenentropie der Kugel", S_kugel, 0.250, unit="J/K")
S_kugel_in_k = S_kugel / k_B
check("6b Eigenentropie in Einheiten von k", S_kugel_in_k, 1.811e22)

# ------------------------------------------------------------
# Check 7 -- Anteil des Positions-Bits an der Eigenentropie
#            Das Bit traegt ln2 * k ; die Kugel traegt S_kugel
# ------------------------------------------------------------
anteil = math.log(2) / S_kugel_in_k
check("7  Anteil Positions-Bit an Eigenentropie", anteil, 3.827e-23)

# ------------------------------------------------------------
# Check 8 -- Barriere der Kugelposition in Einheiten von kT
#            -> thermische Umbesetzung ausgeschlossen
# ------------------------------------------------------------
barriere_kT = W_kugel / (k_B * T)
check("8a Barriere der Kugelposition", barriere_kT, 3.553e15, unit="kT")
# Arrhenius-Lebensdauer waere exp(barriere_kT) -- jenseits jeder Darstellbarkeit
assert barriere_kT > 1e12, "Barriere muss thermische Umbesetzung ausschliessen"
print(f"[OK ] 8b Arrhenius-Exponent exp({barriere_kT:.2e}) numerisch nicht darstellbar")

# ------------------------------------------------------------
# Check 9 -- Grenzuebergang: Bei welcher Masse wird die Barriere ~ kT?
#            mu * m * g * d = k_B * T  ->  m = k_B T / (mu g d)
# ------------------------------------------------------------
m_kritisch = k_B * T / (mu_reib * g * d_weg)
check("9a Kugelmasse fuer Barriere = kT", m_kritisch, 1.407e-19, unit="kg")
# Zum Vergleich: Beruets Kolloid, Silika, Durchmesser 2 um, rho = 2000 kg/m^3
r_kolloid   = 1e-6
rho_silika  = 2000.0
m_kolloid   = (4.0/3.0) * math.pi * r_kolloid**3 * rho_silika
check("9b Masse eines 2-um-Silika-Kolloids", m_kolloid, 8.378e-15, unit="kg")
print(f"      -> Die kritische Masse liegt {m_kolloid/m_kritisch:.1e}x unter dem Kolloid;")
print(f"         das Kolloid haelt seine Position nicht durch Reibung, sondern")
print(f"         durch die optische Falle -- deren Barriere ist auf wenige kT")
print(f"         einstellbar. Genau das macht es zur Brownschen Rechenkugel.")

# ------------------------------------------------------------
# Check 10 -- Kombinatorik gilt exakt, unabhaengig vom Traeger
#             N Kugeln auf 2 Positionen -> Ruecksetzen auf eine
# ------------------------------------------------------------
for N in (1, 8, 64):
    W_vorher, W_nachher = 2**N, 1
    dS_ueber_k = math.log(W_vorher / W_nachher)
    erwartet   = N * math.log(2)
    assert math.isclose(dS_ueber_k, erwartet, rel_tol=1e-12)
print(f"[OK ] 10 Kombinatorik dS/k = N ln2 fuer N = 1, 8, 64 -- exakt")

# ------------------------------------------------------------
# Check 11 -- Rueckkopplungsschranke (A272, Gl. 7):
#             Q_min = kT (ln2 - I) ; der Rechner kennt die Konfiguration
# ------------------------------------------------------------
def Q_min(I_nat):
    return k_B * T * (math.log(2) - I_nat)

assert math.isclose(Q_min(0.0), Q_landauer, rel_tol=1e-12)
assert math.isclose(Q_min(math.log(2)), 0.0, abs_tol=1e-30)
print(f"[OK ] 11 Q_min(I=0) = kT ln2 ; Q_min(I=ln2) = 0")
print(f"      -> Wer die Kugeln selbst gesetzt hat, kennt die Konfiguration:")
print(f"         I = ln2, also Q_min = 0. Der Abakus faellt unter Landauers")
print(f"         eigenen Ensemble-Vorbehalt (A272, Abschnitt 5).")


# ------------------------------------------------------------
# Check 12-14 -- Zwei Boeden: hbar*c/L (quantengeometrisch) vs k_B*T (thermisch)
#                Aufloesung der Diskrepanz zu Dok. 302 (E_bit = hbar*c/L)
# ------------------------------------------------------------
hbar = 1.054571817e-34
c_l  = 299792458.0

# 12: fuer massive mechanische Traeger ist hbar*c/L NICHT die einschlaegige
#     Quantenskala; einschlaegig ist hbar^2/(2 m L^2) -- und die ist irrelevant
E_q_kugel   = hbar**2 / (2 * m_kugel * d_weg**2)
E_q_kolloid = hbar**2 / (2 * m_kolloid * (1e-6)**2)
check("12a Kugel  hbar^2/(2mL^2) in kT", E_q_kugel/(k_B*T),   2.69e-41)
check("12b Kolloid hbar^2/(2mL^2) in kT", E_q_kolloid/(k_B*T), 1.60e-22)
assert E_q_kugel/(k_B*T) < 1e-30, "quantengeometrischer Boden muss hier irrelevant sein"

# 13: Schnittpunkt der beiden Boeden bei Raumtemperatur
L_cross = hbar * c_l / (k_B * T)
check("13 Schnittpunkt hbar c/(kT) bei 300 K", L_cross, 7.63e-6, unit="m")

# 14: Qubit -- der Fall, in dem der quantengeometrische Boden fuehrt
f_qubit, T_mix = 5e9, 0.010
check("14 Qubit hf/kT bei 5 GHz und 10 mK", h*f_qubit/(k_B*T_mix), 24.0)
print("      -> Kugel/Kolloid: thermischer Boden fuehrt allein (Dok-302-Kriterium")
print("         nicht einschlaegig). Qubit: quantengeometrischer Boden fuehrt.")
print("         Die zwei Kriterien sind zwei Boeden, kein Widerspruch.")

# ------------------------------------------------------------
print("-" * 78)
n_ok = sum(1 for v in results.values() if v[2])
print(f"Alle Checks bestanden: {n_ok}/{len(results)} numerische Vergleiche")
print("=" * 78)
print()
print("BEFUND")
print("  Die Buchhaltung (Check 10) gilt exakt und traegerunabhaengig.")
print("  Die thermische Umrechnung (Checks 2,3,7,8) gilt fuer die Kugel nicht:")
print("  das Positions-Bit traegt 4e-23 der Eigenentropie der Kugel, und die")
print("  Barriere liegt bei 3.6e15 kT. Beide Haelften von Landauers Argument")
print("  sind unabhaengig; der Token-Rechner trennt sie sichtbar.")
