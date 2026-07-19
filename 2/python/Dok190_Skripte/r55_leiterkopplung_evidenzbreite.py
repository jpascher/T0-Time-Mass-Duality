#!/usr/bin/env python3
# ffgft_R55_leiterkopplung_evidenzbreite.py
# ---------------------------------------------------------------------------
# PRUEFSKRIPT zu R55 (Dok. 190) — Gegenstand: Dok. 292, Abschnitt
# "Leiterübergreifende Kopplung: ein generationslineares Korrekturgesetz".
#
# FRAGE: Wieviel voneinander unabhaengige Information stuetzt das Gesetz
#        N_g = g * N_0 ?
#
# WAS DAS SKRIPT TUT:
#   (1) rechnet N_g = (1 - K^{p_g})/xi aus den in Dok. 292 angegebenen p_g nach
#       und vergleicht mit den dort genannten N_g;
#   (2) prueft, ob p_3 = p_1 + p_2 eine Identitaet ist (symbolisch, nicht numerisch);
#   (3) prueft, ob daraus N_3 ~ N_1 + N_2 folgt, und in welcher Ordnung in xi;
#   (4) beziffert, wieviel Restabweichung ein gemeinsames N_0 prinzipiell
#       uebriglassen MUSS, und vergleicht das mit dem berichteten "Faktor 300".
#
# WAS ES NICHT TUT:
#   * Es widerlegt das Gesetz nicht. Es misst dessen Evidenzbreite.
#   * Es leitet N_0 nicht her. N_0 bleibt offen (R54, P35).
#   * Es beruehrt die Modus-Trennung (Modus 1 / Modus 2, P42) nicht.
#
# Abhaengigkeiten: sympy, sonst nichts.
# ---------------------------------------------------------------------------

import sympy as sp

XI = sp.Rational(4, 30000)
K = 1 - 100 * XI                      # = 74/75

# Werte wie in Dok. 292 angegeben
P = {1: sp.Float("0.3873"), 2: sp.Float("0.7694"), 3: sp.Float("1.1567")}
N_DOK = {1: 38.89, 2: 77.06, 3: 115.55}
D_ROH = {1: 0.521, 2: 1.038, 3: 1.565}          # Rohabweichungen in Prozent
N0_DOK = 38.65

line = "-" * 74


def N_of_p(p):
    """N ueber die Definition K = 1 - N*xi, angewandt auf K^p."""
    return (1 - K**p) / XI


print(__doc__)
print(line)
print("(1) N_g aus p_g — Nachrechnung")
print(line)
print(f"  {'g':>2} {'p_g':>10} {'N_g berechnet':>15} {'N_g (Dok 292)':>15} {'Abw.':>10}")
for g in (1, 2, 3):
    n = float(N_of_p(P[g]))
    print(f"  {g:>2} {float(P[g]):>10.4f} {n:>15.3f} {N_DOK[g]:>15.2f} "
          f"{(n / N_DOK[g] - 1):>9.4%}")
print("  -> die angegebenen N_g reproduzieren sich aus den p_g. Bestaetigt.\n")

print(line)
print("(2) Ist p_3 = p_1 + p_2 ein Befund oder eine Identitaet?")
print(line)
p1, p2, k = sp.symbols("p_1 p_2 k", positive=True)
lhs = k**p1 * k**p2
rhs = k**(p1 + p2)
print(f"  symbolisch:  K^p1 * K^p2 - K^(p1+p2) = {sp.simplify(lhs - rhs)}")
print("""
  Herleitung: m_tau/m_e = (m_tau/m_mu) * (m_mu/m_e). Eine durchgaengig
  multiplikative Korrektur erfuellt daher K^{p_3} = K^{p_1} * K^{p_2},
  also p_3 = p_1 + p_2 IDENTISCH — unabhaengig von jeder Messung.

  Numerisch: p_1 + p_2 = %s, p_3 = %s, Differenz = %s.
  Die in Dok. 292 genannte Genauigkeit 6e-14 ist Fliesskommagenauigkeit.
  Dok. 292 benennt dies korrekt ("traegt keine neue Information");
  R55 zieht nur die Folgerung fuer N_3 und fuer den Faktor 300.
""" % (float(P[1] + P[2]), float(P[3]), float(P[1] + P[2] - P[3])))

print(line)
print("(3) Folgt daraus N_3 ~ N_1 + N_2 ?")
print(line)
n1, n2, n3 = (float(N_of_p(P[g])) for g in (1, 2, 3))
print(f"  N_1 + N_2 = {n1 + n2:.3f}")
print(f"  N_3       = {n3:.3f}")
print(f"  Differenz = {(n1 + n2) / n3 - 1:.4%}   (2. Ordnung in xi: 100*xi = {float(100*XI):.4f})")
print(f"\n  Verhaeltnisse:  1 : {n2/n1:.4f} : {n3/n1:.4f}")
print(f"  erzwungen:      1 : {n2/n1:.4f} : {1 + n2/n1:.4f}   (= 1 + N_2/N_1)")
print("""
  -> Im Verhaeltnis "1 : 1,981 : 2,971" ist allein die 1,981 gemessen.
     Die dritte Zahl ist Arithmetik. "~1:2:3" ist "~1:2:(1+2)".
""")
print("  Gegenprobe an den Rohabweichungen (Prozent, additiv statt multiplikativ):")
print(f"    d_1 + d_2 = {D_ROH[1]} + {D_ROH[2]} = {D_ROH[1]+D_ROH[2]:.3f}   gegen d_3 = {D_ROH[3]}")
print(f"    d_2 / d_1 = {D_ROH[2]/D_ROH[1]:.4f}\n")

print(line)
print("(4) Woher kommt der berichtete Faktor ~300?")
print(line)
r = n2 / n1
rel = abs(r - 2) / 2
print(f"  Ein gemeinsames N_0 setzt N_1 = N_0 und N_2 = 2*N_0 zugleich an.")
print(f"  Das ist nur soweit erfuellbar, wie N_2/N_1 = {r:.4f} von exakt 2 abweicht.")
print(f"  relative Abweichung von 2 : {rel:.4%}")
print(f"  daraus erwarteter Restfaktor der Groessenordnung : {1/rel:.0f}")
print(f"  berichtet in Dok. 292 : rund 300")
print("""
  -> Der Faktor ist der Kehrwert derselben einen Zahl. Er beziffert, wie nah
     1,9815 an 2 liegt, nicht wie gut das Gesetz traegt. Groessenordnung
     stimmt ueberein; die genaue Zahl haengt daran, ueber welche Stellen und
     mit welchem gemeinsamen N_0 (Dok. 292: 38,65) gemittelt wird.
""")

print(line)
print("(5) Notiz: N_0-Kandidaten (nicht gebucht, vgl. R55 (v))")
print(line)
import math
kand = {"100/e": 100/math.e,
        "100/phi^2": 100/((1+5**0.5)/2)**2,
        "39 (glatt)": 39.0,
        "ln(10^17) = RG-Skalenzahl Dok.133": 17*math.log(10)}
print(f"  {'Kandidat':>36} {'Wert':>10} {'Abw. zu N_0=38,65':>20}")
for name, v in kand.items():
    print(f"  {name:>36} {v:>10.3f} {(v/N0_DOK - 1):>19.2%}")
print("""
  Kein Kandidat trifft nach dem Massstab von Dok. 292 ("nicht genau genug,
  um behauptet zu werden"). Festgehalten ist allein, dass "39" und die
  RG-Skalenzahl ln(10^17) = 39,14 dieselbe Groesse sind und die beiden
  Dokumente nicht aufeinander verweisen. N_0 bleibt offen (R54, P35).
""")

print(line)
print("ERGEBNIS: Das Gesetz N_g = g*N_0 bleibt bestehen. Seine Evidenz ist")
print("          eine gemessene Zahl (N_2/N_1 = 1,9815), nicht drei Stellen")
print("          und nicht zusaetzlich ein Toleranzfaktor.")
print(line)
