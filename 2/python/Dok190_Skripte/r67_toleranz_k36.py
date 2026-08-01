#!/usr/bin/env python3
"""
toleranz_k36.py
---------------
Prueft, ob der Abstand zwischen den beiden Wegen zu 36 innerhalb der
Unsicherheiten der beiden Wege liegt.

Frage: A270 nennt zwei unabhaengige Groessen, die beide auf 36 fuehren.
Sie liegen 0,098 auseinander. Ist das durch ihre eigenen Unsicherheiten
gedeckt, oder ist es ein realer Rest?

Quellen der Zahlenwerte:
  A270  16/pi^2, k*/100 = 36,09, Delta = 0,010 %
  275   k* = log(phi)/xi ~ 3609;  k*_exakt = 3608,51
        r(3609) ~ 1/phi mit absolutem Fehler 4e-5, relativ 6,5e-5
  A040  Faktor 100 aus D_f^eff = 2,973 (drei Nachkommastellen)
        -> n in [98,3, 102,0], siehe r67_faktor100_unsicherheit.py

Nachtrag 1. August (R67): die urspruengliche Fassung behandelte die
100 im Nenner als exakt und fand 16 sigma. Abschnitt 2n ergaenzt die
Nenner-Unsicherheit; das Fazit ist entsprechend korrigiert.
"""

import math

XI   = 4/30000
PHI  = (1 + 5**0.5) / 2
K    = 75/74                    # 1/K_frak
LNK  = math.log(K)
A4   = 16 / math.pi**2          # Kehrwert der D4-Packungsdichte


def trennlinie(t):
    print()
    print("=" * 68)
    print(t)
    print("=" * 68)


# ---------------------------------------------------------------------
trennlinie("1. WEG A -- Packungsdichte: welcher Exponent, wie scharf?")

n_A = math.log(A4) / LNK
print(f"  16/pi^2                      = {A4:.10f}")
print(f"  exakter Exponent n_A         = {n_A:.6f}")
print(f"  Abstand zur Ganzzahl 36      = {abs(n_A-36):.6f}")
print()
print("  Unsicherheit dieses Wegs:")
print("    16/pi^2 ist exakt. K = 75/74 ist exakt. Also ist n_A exakt.")
print("    Die einzige Unsicherheit ist die Rundung auf eine Ganzzahl,")
print("    und die ist keine Messunsicherheit, sondern eine Setzung.")
print()
print(f"    -> sigma_A = 0.  n_A = {n_A:.6f}, punktgenau.")
sigma_A = 0.0


# ---------------------------------------------------------------------
trennlinie("2. WEG B -- Rekursionstiefe: hier sitzt die Unsicherheit")

k_naiv   = math.log(PHI) / XI          # 3609,09
k_exakt  = 3608.51                     # aus Dok. 275
print(f"  k* = ln(phi)/xi              = {k_naiv:.4f}")
print(f"  k*_exakt aus Dok. 275        = {k_exakt:.4f}")
print(f"  Differenz                    = {k_naiv-k_exakt:.4f}")
print()
print("  Dok. 275 sagt ausdruecklich:")
print("    'das exakte reelle k*_exakt = 3608,51 trifft 1/phi identisch'")
print("    r(3609) ~ 1/phi mit absolutem Fehler 4e-5, relativ 6,5e-5")
print()
print("  Das heisst: ln(phi)/xi ist eine NAEHERUNG fuer die Rekursionstiefe,")
print("  nicht ihr exakter Wert. Die Rekursion r(k+1) = r(k)(1-xi) ist")
print("  diskret; die stetige Naeherung exp(-k*xi) weicht davon ab.")
print()
n_B_naiv  = k_naiv / 100
n_B_exakt = k_exakt / 100
print(f"  k*/100      = {n_B_naiv:.6f}   (der in A270 genannte Wert)")
print(f"  k*_exakt/100= {n_B_exakt:.6f}   (der korrekte Wert)")
print(f"  Spanne      = {abs(n_B_naiv-n_B_exakt):.6f}")
sigma_B = abs(n_B_naiv - n_B_exakt)


# ---------------------------------------------------------------------
trennlinie("3. DER VERGLEICH")

d = abs(n_B_naiv - n_A)
d_exakt = abs(n_B_exakt - n_A)
print(f"  Abstand mit naivem k*        |{n_B_naiv:.4f} - {n_A:.4f}| = {d:.6f}")
print(f"  Abstand mit exaktem k*       |{n_B_exakt:.4f} - {n_A:.4f}| = {d_exakt:.6f}")
print()
print(f"  Unsicherheit von Weg B       sigma_B = {sigma_B:.6f}")
print(f"  Unsicherheit von Weg A       sigma_A = {sigma_A:.6f}")
print(f"  kombiniert                   sigma   = {math.hypot(sigma_A,sigma_B):.6f}")
print()
sigma = math.hypot(sigma_A, sigma_B)
print(f"  Abweichung in Einheiten von sigma:")
print(f"    naiv   : {d/sigma:.2f} sigma")
print(f"    exakt  : {d_exakt/sigma:.2f} sigma")
print()
if d_exakt <= sigma:
    print("  ERGEBNIS: mit dem exakten k* liegt die Abweichung INNERHALB")
    print("  der eigenen Unsicherheit des Rekursionswegs.")
else:
    print("  ERGEBNIS: die Abweichung liegt AUSSERHALB der Unsicherheit.")


# ---------------------------------------------------------------------
trennlinie("2n. NACHTRAG (R67) -- die 100 im Nenner ist nicht exakt")

print("  A040 gibt D_f^eff = 2,973 mit drei Nachkommastellen an. Die")
print("  Potenzform (D/3)^(D/2) = 1 - n*xi laesst damit n im Bereich")
print("  [98,3, 102,0] offen -- die 100 ist auf etwa +-2 unbestimmt")
print("  (Rechnung: r67_faktor100_unsicherheit.py).")
print()
dn = 2.0
sigma_nenner = k_naiv / 100**2 * dn        # dn_B = k*/n^2 * dn
print(f"  Fortpflanzung auf n_B = k*/n:")
print(f"    sigma_Nenner = k*/n^2 * {dn:.0f} = {sigma_nenner:.4f}  im Exponenten")
print(f"    sigma_Zaehler (k* naiv vs exakt)   = {sigma_B:.4f}")
sigma_ges = math.hypot(sigma_B, sigma_nenner)
print(f"    kombiniert                         = {sigma_ges:.4f}")
print()
print(f"  Abweichung in Einheiten der Gesamtunsicherheit:")
print(f"    naiv   : {d/sigma_ges:.2f} sigma")
print(f"    exakt  : {d_exakt/sigma_ges:.2f} sigma")
print()
print("  Der Wert, der beide Wege zur Deckung braechte, ist n = 100,273 --")
print("  er liegt bequem im Intervall [98,3, 102,0]. Die 0,098 sind damit")
print("  durch die (unbezifferte) Genauigkeit des Faktors 100 gedeckt.")
print("  Gebucht als R67 in Dok. 190.")


# ---------------------------------------------------------------------
trennlinie("4. WAS DAS FUER DIE 36 BEDEUTET")

print(f"  Weg A verlangt   : {n_A:.4f}   -> rundet auf 36")
print(f"  Weg B naiv       : {n_B_naiv:.4f}   -> rundet auf 36")
print(f"  Weg B exakt      : {n_B_exakt:.4f}   -> rundet auf 36")
print()
print("  Alle drei runden auf 36, und keiner liegt nahe an einer")
print("  Rundungsgrenze:")
for name, v in (("A", n_A), ("B naiv", n_B_naiv), ("B exakt", n_B_exakt)):
    print(f"    {name:<9} Abstand zur naechsten Grenze (35,5 / 36,5): "
          f"{min(abs(v-35.5), abs(v-36.5)):.4f}")
print()
print("  Die Zuordnung zur 36 ist auf beiden Wegen stabil.")
print("  Sie war nie das Problem.")


# ---------------------------------------------------------------------
trennlinie("5. WAS IM WERT ANKOMMT")

print("  Umrechnung Exponent -> Wert: Faktor ln(75/74) = "
      f"{LNK:.6f} pro Einheit.")
print()
for name, v in (("A (exakt)", n_A), ("B naiv", n_B_naiv),
                ("B exakt", n_B_exakt), ("Ganzzahl 36", 36.0)):
    val = K**v
    print(f"    {name:<12} n = {v:8.4f}  ->  {val:.6f}"
          f"   gegen 16/pi^2: {(val-A4)/A4*100:+.4f} %")
print()
print("  Die viel zitierten 0,010 % sind die Zeile 'Ganzzahl 36'.")
print("  Sie messen die Rundung, nicht die Uebereinstimmung der Wege.")


# ---------------------------------------------------------------------
trennlinie("6. FAZIT")

print("  Weg A ist exakt. Weg B ist eine Naeherung mit bekannter Spanne.")
print(f"  Die Spanne betraegt {sigma_B:.4f} im Exponenten.")
print()
print(f"  Der Abstand der beiden Wege ist {d_exakt:.4f} (mit exaktem k*)")
print(f"  bzw. {d:.4f} (mit dem in A270 genannten naiven k*).")
print()
print("  Die Zaehler-Naeherung allein (k* naiv vs exakt) erklaert rund")
print(f"  {sigma_B/d*100:.0f} % des Abstands. Der Rest ist KEIN realer Rest:")
print("  er liegt innerhalb der +-2-Unsicherheit des Faktors 100 im")
print("  Nenner (Abschnitt 2n, R67). Beide Unsicherheiten zusammen")
print(f"  decken den Abstand mit {d_exakt/sigma_ges:.2f} sigma bequem.")
print()
print("  Unberuehrt bleibt in jedem Fall: eine Vorwaerts-Herleitung,")
print("  WARUM eine Rekursionstiefe einer Packungsdichte entsprechen")
print("  sollte, liegt nicht vor (A270, P35).")
