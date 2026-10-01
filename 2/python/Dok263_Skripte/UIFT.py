#!/usr/bin/env python3
"""
FFGFT - CMB-Temperatur aus xi und die formale Bruecke zu UIFT

================================================================================
WAS DIESES SKRIPT ZEIGT (und was nicht)
================================================================================

Aktualisiert am 1.10.2026: "FFGFT-Seite vollständig verifizierbar" und "keine
offene Lücke" durch die R137(i)-Einstufung ersetzt (T_CMB = (16/9) xi stimmt nur
in der Einheit eV mit dem Messwert überein, einheitenabhängige Übereinstimmung,
keine Herleitung, Frage offen); Casimir/CMB-Zusatz gestrichen (R136: Identität,
kein Messvergleich); Vergleich mit gemessenem T_CMB (Faktor 418518) ergänzt
(vgl. Dok. 263 bzw. Dok. 190, R136/R137).

Es besteht eine BRUECKENFORMEL zwischen FFGFT und der UIFT-Groesse xi_UIFT.
Diese Bruecke ist von der FFGFT-Seite her nachrechenbar (Rechenschritte aus
xi); die T_CMB-Relation selbst ist aber eine einheitenabhaengige Ueberein-
stimmung (Zahl erst in eV), keine Herleitung (R137 i). Die UIFT-Seite koennen wir NICHT verifizieren -- die
UIFT-Formel stammt aus Onur Tekers Arbeit. Die Bruecke ist daher FORMAL,
nicht empirisch.

Einziger Parameter: xi = 1/7500 = 4/30000 (geometrisch, Dok. 009).

WICHTIG -- zwei getrennte Dinge:
 (1) ERSTE ORDNUNG:  T_CMB/E_xi = (16/9) xi   (Modenzaehlung, Dok. 025).
     Das ist die Verhaeltnis-Aussage, auf der die Bruecke beruht.
 (2) FRAKTALE KORREKTUR K_frak (Dok. 133): 1 - 100 xi = 74/75 ~ 0.9867,
     aus dem kumulativen RG-Lauf. Sie betrifft den ABSOLUTEN Kelvin-Wert,
     nicht die Bruecke.

Zum absoluten Kelvin-Wert (Dok. 190, Praezisierung 11):
 - erste Ordnung allein:    2.7507 K  (+0.93 % zum Planck-Wert)
 - mit K_frak (Dok 133):    2.7140 K  (-0.42 %)
 Nach Anwendung von K_frak bleibt eine Restdifferenz zum Messwert. Nach
 R137(i) ist die Uebereinstimmung einheitenabhaengig (reine Zahl, erst in eV
 mit dem Messwert vergleichbar), keine Herleitung; die Frage ist OFFEN (R70).
 Der Planck-Wert 2.72548 K ist unter
 LambdaCDM aus dem Spektrum extrahiert -- kein modellunabhaengiger absoluter
 Referenzwert. Die Theorie muss ihn nicht exakt treffen.
 Der oft genannte Ausdruck (1 - 275/4 xi) traefe ihn numerisch exakt, ist aber
 NICHT erforderlich und hat keine geometrische Herleitung -- daher hier weg-
 gelassen, um nicht zu unterstellen, der Messwert sei der zu treffende Wert.
================================================================================
"""

from fractions import Fraction
from math import log

# ============================================================================
# Einziger Parameter
# ============================================================================
xi = Fraction(1, 7500)
xif = float(xi)

print("=" * 70)
print("FFGFT - CMB-Temperatur und formale Bruecke zu UIFT")
print("=" * 70)
print()
print(f"Einziger Parameter (geometrisch): xi = {xi} = {xif:.10e}")
print()

# ============================================================================
# (1) Erste Ordnung -- Basis der Bruecke
# ============================================================================
T1 = (16/9) * xif   # in natuerlichen Einheiten (eV-Skala, E_xi gesetzt)
print("-" * 70)
print("(1) ERSTE ORDNUNG (Modenzaehlung, Dok. 025) -- Basis der Bruecke")
print("-" * 70)
print(f"  T_CMB(1.Ord)/E_xi = (16/9) xi = {T1:.10e}")
print()

# ============================================================================
# (2) Fraktale Korrektur K_frak (Dok. 133) -- separat, fuer absoluten Wert
# ============================================================================
K_frak = 1 - 100*xif    # = 74/75, primaere Definition Dok. 133
print("-" * 70)
print("(2) FRAKTALE KORREKTUR K_frak (Dok. 133, kumulativer RG-Lauf) -- separat")
print("-" * 70)
print(f"  K_frak = 1 - 100 xi = {Fraction(1)-100*xi} = {K_frak:.10f}")
print(f"  Hinweis: Dok 003 nennt eine zweite Form 1-(D_f-2)/68; laut Dok 190 P11")
print(f"  ist Dok 133 die PRIMAERE Definition, Dok 003 nur heuristische Motivation.")
print()

# ============================================================================
# Absoluter Kelvin-Wert: erste Ordnung und mit K_frak (SI-Umrechnung)
# ============================================================================
kB = 1.380649e-23; eV_J = 1.602176634e-19
T1_K = T1 * eV_J / kB
Tk_K = T1 * K_frak * eV_J / kB
T_planck = 2.72548

print("-" * 70)
print("Absoluter Kelvin-Wert (SI-Umrechnung; Planck nur als Referenz)")
print("-" * 70)
print(f"  erste Ordnung:        {T1_K:.4f} K   ({100*(T1_K/T_planck-1):+.3f} %)")
print(f"  mit K_frak (Dok133):  {Tk_K:.4f} K   ({100*(Tk_K/T_planck-1):+.3f} %)")
print(f"  Planck 2018 (LambdaCDM-extrahiert, kein absoluter Wert): {T_planck} K")
print(f"  -> Einstufung (R137 i): einheitenabhaengige Uebereinstimmung (Zahl erst in eV),")
print(f"     keine Herleitung; Frage offen.")
print()

# ============================================================================
# Die Bruecke zu UIFT -- beruht auf der ERSTEN ORDNUNG
# ============================================================================
print("=" * 70)
print("BRUECKE zu UIFT (Onur Teker) -- formal, beruht auf erster Ordnung")
print("=" * 70)
print()
m_e_c2_eV = 510998.9461   # m_e c^2 in eV
ln2 = log(2)

# UIFT-Formel (von Onur): xi_UIFT = k_B T_CMB ln2 / (m_e c^2)
# Einsetzen der FFGFT-ERSTEN-ORDNUNG fuer T_CMB:
xi_UIFT = T1 * ln2 / m_e_c2_eV
ratio = xif / xi_UIFT
ratio_closed = m_e_c2_eV / ((16/9) * ln2)   # identische geschlossene Form

print("  UIFT-Formel (von Onur Teker, von uns NICHT pruefbar):")
print("     xi_UIFT = k_B T_CMB ln2 / (m_e c^2)")
print()
print("  Einsetzen der FFGFT-ersten-Ordnung T_CMB = (16/9) xi:")
print(f"     xi_UIFT          = {xi_UIFT:.10e}")
print(f"     xi_FFGFT/xi_UIFT = {ratio:.3f}")
print(f"     geschlossene Form= (m_e c^2)/((16/9) ln2) = {ratio_closed:.3f}")
print("     -> die beiden sind identisch: das Verhaeltnis ist ein fester")
print("        Umrechnungsfaktor, KEIN empirisches Resultat.")
print()
print("  Die Bruecke nutzt NUR die erste Ordnung, nicht K_frak und nicht den")
print("  absoluten Kelvin-Wert -- die 0.4%-Frage ist fuer die Bruecke irrelevant.")
print()
# Vergleich: Faktor 414684 entspricht k_B T_CMB = (16/9) xi eV (Dok. 263 Vermerk);
# mit dem gemessenen T_CMB ergibt sich ein anderer Faktor.
T_meas = 2.7255   # gerundeter Messwert wie im Vermerk Dok. 263
kT_meas_eV = T_meas * kB / eV_J
ratio_meas = xif / (kT_meas_eV * ln2 / m_e_c2_eV)
print(f"  Zum Vergleich mit gemessenem T_CMB = {T_meas} K (k_B T = {kT_meas_eV:.6e} eV):")
print(f"     xi_FFGFT/xi_UIFT = {ratio_meas:.0f}   (statt {ratio:.0f})")
print("     -> 414684 gilt nur fuer k_B T_CMB = (16/9) xi eV, nicht fuer den Messwert.")
assert abs(ratio - ratio_closed) < 1e-6 * ratio
assert round(ratio) == 414684 and abs(ratio_meas - 418518) < 1
print()

# ============================================================================
# Verifizierbarkeit: unsere Seite ja, UIFT-Seite nein
# ============================================================================
print("=" * 70)
print("VERIFIZIERBARKEIT DER BRUECKE")
print("=" * 70)
print()
print("  FFGFT-Seite (Rechenschritte nachrechenbar; Einstufung R137 i):")
print("    - xi = 1/7500 geometrisch")
print("    - T_CMB(1.Ord) = (16/9) xi  (Modenzaehlung) -- einheitenabhaengige")
print("      Uebereinstimmung in eV, keine Herleitung, offen")
print("    - m_e c^2 in FFGFT aus der Leptonen-Hierarchie")
print("    - jeder kann xi_FFGFT/xi_UIFT = 414684 nachrechnen")
print()
print("  UIFT-Seite (NICHT verifizierbar):")
print("    - die Formel xi_UIFT = k_B T_CMB ln2/(m_e c^2) stammt von Onur Teker")
print("    - ob sie korrekt oder empirisch validiert ist, koennen wir nicht pruefen")
print()
print("  => Die Bruecke ist FORMAL: WENN Onurs Formel gilt UND die FFGFT-Werte")
print("     gelten, DANN verknuepft ein fester Faktor beide xi. Nachrechenbar ist")
print("     damit die FFGFT-Rechnung -- die T_CMB-Relation bleibt offen (R137 i),")
print("     die UIFT-Seite ist nicht pruefbar.")
print("=" * 70)
