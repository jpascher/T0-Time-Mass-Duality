#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruefrechnung_rest_0p1xi.py -- Der Faden am Rest ~0.1*xi.

Ausgangslage (aus pruefrechnung_p_identitaet.py):
  q*_add = 0.267950715  (Exponent, der K = 74/75 exakt reproduziert)
  2-sqrt3 = 0.267949192
  Rest dq = +1.523e-6 in q  <->  1.36e-5 auf K/m_e-Ebene  ~ 0.10*xi.
  Der Rest ist real (45000x ueber dem m_e-Fehlerboden).

Zwei Hypothesen, beide werden durchgerechnet:
  H1  KORREKTURTERM: q = (2-sqrt3) + c*F(xi) mit einer Theorie-Familie F.
      Fuer jede Familie wird c* gefittet und geprueft, ob c* ein einfacher
      geschlossener Wert ist (Kettenbruch + Konstantenvergleich).
  H2  ANDERER EXAKTER EXPONENT: systematischer, FAIRER Scan quadratischer
      Irrationalitaeten (a+b*sqrt(d))/c und einfacher pi/e/ln-Formen um
      q*_add UND q*_mul. Rangfolge nach Distanz UND Beschreibungslaenge.

Dazu die im Korpus selbst angemahnte Warnung (A130, e^2-Koinzidenz):
Naehe allein ist kein Argument -- deshalb wird am Ende die Trefferdichte
des Kandidatenraums angegeben (wie viele Kandidaten landen ZUFAELLIG so
nah?), damit Signifikanz von Numerologie unterscheidbar bleibt.
Standardbibliothek.
"""
import math
from fractions import Fraction
from itertools import product

# ------------------------------------------------------------ Basiszahlen
XI    = 4.0 / 30000.0
LNXI  = math.log(XI)
ME    = 0.51099895069
K_ADD = 74.0 / 75.0
K_MUL = (1.0 - XI) ** 100
S2, S3 = math.sqrt(2), math.sqrt(3)
Q_GEO = 2.0 - S3

def q_von(K):
    return math.log(ME / (K * 4.0 * S2)) / LNXI

Q_ADD, Q_MUL = q_von(K_ADD), q_von(K_MUL)
DQ = Q_ADD - Q_GEO

print("=" * 74)
print("REST-ANALYSE  dq = q*_add - (2-sqrt3) = %+.6e" % DQ)
print("=" * 74)

# ------------------------------------------------------------ H1: Korrektur
print("\nH1  KORREKTURTERM  q = (2-sqrt3) + c*F(xi):  c* je Familie")
print("-" * 74)
FAMILIEN = {
    "xi":              XI,
    "xi^2":            XI ** 2,
    "(100xi)^2":       (100 * XI) ** 2,
    "(100xi)^3":       (100 * XI) ** 3,
    "xi*ln(1/xi)":     XI * abs(LNXI),
    "xi^(3/2)":        XI ** 1.5,
    "xi/ln(1/xi)":     XI / abs(LNXI),
    "ln(75/74)":       math.log(75 / 74),
    "ln(75/74)^2":     math.log(75 / 74) ** 2,
    "(2-sqrt3)*xi":    Q_GEO * XI,
}
KONSTANTEN = {
    "1": 1.0, "1/2": 0.5, "2": 2.0, "3": 3.0, "1/3": 1/3, "2/3": 2/3,
    "1/4": 0.25, "3/4": 0.75, "1/8": 0.125, "1/12": 1/12, "1/16": 1/16,
    "1/24": 1/24, "1/75": 1/75, "1/100": 0.01, "sqrt2": S2, "sqrt3": S3,
    "1/sqrt2": 1/S2, "1/sqrt3": 1/S3, "sqrt3/2": S3/2, "2-sqrt3": Q_GEO,
    "pi": math.pi, "1/pi": 1/math.pi, "pi^2": math.pi**2, "1/pi^2": 1/math.pi**2,
    "e": math.e, "1/e": 1/math.e, "1/(2e)": 1/(2*math.e),
    "3/(4pi)": 3/(4*math.pi), "8/75": 8/75, "9/75": 9/75, "320": 320.0,
    "600/7": 600/7, "1/87.5=2/175": 2/175, "3/8": 0.375, "5/12": 5/12,
}
for name, F in sorted(FAMILIEN.items(), key=lambda kv: kv[1], reverse=True):
    c = DQ / F
    fr = Fraction(c).limit_denominator(100)
    fr_gut = abs(float(fr) - c) / abs(c) < 2e-3 and fr.denominator <= 100
    naechste = min(KONSTANTEN.items(), key=lambda kv: abs(kv[1] - c))
    k_gut = abs(naechste[1] - c) / abs(c) < 2e-3
    marker = []
    if fr_gut:
        marker.append(f"~ {fr}")
    if k_gut:
        marker.append(f"~ {naechste[0]}")
    print("  F = %-14s  c* = %12.6g   %s"
          % (name, c, ("  ".join(marker) if marker else "kein einfacher Wert")))
print("""  Lesart: nur wenn c* ein EINFACHER Wert ist (kleiner Bruch oder
  benannte Konstante), traegt die Familie als Korrekturterm-Kandidat.""")

# ------------------------------------------------------------ H2: Scan
print("\nH2  ALTERNATIVER EXAKTER EXPONENT -- fairer Scan um beide Ziele")
print("-" * 74)

def kandidaten_erzeugen():
    """Quadratische Irrationalitaeten (a+b*sqrt(d))/c und pi/e/ln-Formen.
    Liefert (wert, label, komplexitaet)."""
    K = []
    for d in (2, 3, 5, 6, 7, 10):
        sq = math.sqrt(d)
        for a, b, c in product(range(-9, 10), range(-9, 10), range(1, 13)):
            if b == 0:
                continue
            v = (a + b * sq) / c
            if 0.25 < v < 0.29:
                kompl = abs(a) + abs(b) + c + {2: 1, 3: 1, 5: 2, 6: 2, 7: 3, 10: 3}[d]
                K.append((v, f"({a}{b:+d}*sqrt{d})/{c}", kompl))
    for a, b in product(range(1, 13), range(1, 40)):
        for v, lbl, k0 in ((a * math.pi / b, f"{a}*pi/{b}", a + b),
                           (a / (b * math.e), f"{a}/({b}e)", a + b),
                           (a * math.log(2) / b, f"{a}ln2/{b}", a + b + 1),
                           (a * math.log(3) / b, f"{a}ln3/{b}", a + b + 1)):
            if 0.25 < v < 0.29:
                K.append((v, lbl, k0))
    return K

KAND = kandidaten_erzeugen()
print(f"  Kandidatenraum: {len(KAND)} Ausdruecke im Fenster (0.25, 0.29)")

def bericht(ziel, name, fenster=3e-6):
    nah = sorted(((abs(v - ziel), v, lbl, kompl) for v, lbl, kompl in KAND
                  if abs(v - ziel) < fenster), key=lambda t: (t[3], t[0]))
    dichte = sum(1 for v, _, _ in KAND if abs(v - ziel) < fenster)
    print(f"\n  Ziel {name} = {ziel:.9f}   (Fenster +-{fenster:.0e},"
          f" Treffer: {dichte})")
    for d, v, lbl, kompl in nah[:6]:
        print(f"    {lbl:22s} = {v:.9f}  Diff {v-ziel:+.2e}  Komplexitaet {kompl}")
    if not nah:
        print("    -- kein Kandidat im Fenster --")
    return dichte

d1 = bericht(Q_ADD, "q*_add")
d2 = bericht(Q_MUL, "q*_mul")
d3 = bericht(Q_GEO, "2-sqrt3 (Kontrolle)", fenster=1e-9)

# Zufallserwartung: Kandidatendichte pro Einheitsintervall * Fensterbreite
breite = 0.29 - 0.25
erw = len(KAND) / breite * 2 * 3e-6
print(f"\n  Zufallserwartung im +-3e-6-Fenster: ~{erw:.1f} Treffer"
      f" (beobachtet: {d1} bei q*_add, {d2} bei q*_mul)")
print("""  -> Liegt die Trefferzahl im Bereich der Zufallserwartung, ist NAEHE
  ALLEIN kein Argument (dieselbe Warnung wie bei e^2 in A130). Ein
  Kandidat zaehlt nur, wenn er zusaetzlich niedrige Komplexitaet hat
  UND eine theorieinterne Begruendung bekommt.""")

# ------------------------------------------------------------ Kettenbruch
print("\nKETTENBRUCH von q*_add (zeigt, ob eine kleine Rationale 'zieht'):")
x, cf = Q_ADD, []
for _ in range(12):
    a = int(x); cf.append(a)
    x = x - a
    if x < 1e-12:
        break
    x = 1 / x
print("  q*_add = [%s]" % ", ".join(map(str, cf)))
konv = []
h1, h0, k1, k0 = 1, 0, 0, 1
for a in cf:
    h1, h0 = a * h1 + h0, h1
    k1, k0 = a * k1 + k0, k1
    konv.append((h1, k1))
print("  Konvergenten:", " ".join(f"{h}/{k}" for h, k in konv[:9]))
print("""  (2-sqrt3 hat Kettenbruch [0;3,1,2,1,2,1,2,...] -- periodisch.
  Bricht q*_add frueh aus diesem Muster aus, ist es KEINE gestoerte
  Version von 2-sqrt3, sondern eine eigene Zahl.)""")

# ------------------------------------------------------------ Fazit
print("\n" + "=" * 74)
print("FAZIT")
print("=" * 74)
print("""\
 Die Zahlen oben entscheiden zwischen drei Lesarten:
 (a) 2-sqrt3 + einfacher Korrekturterm  -> nur haltbar, wenn oben ein
     c* mit kleinem Bruch/benannter Konstante erscheint UND die Familie
     theorieintern begruendbar ist;
 (b) anderer exakter Exponent           -> nur haltbar, wenn ein Kandidat
     deutlich unter der Zufallserwartung UND mit niedriger Komplexitaet
     erscheint;
 (c) q*_add ist schlicht der empirische Wert, 2-sqrt3 eine Naehe ohne
     Status -- die konservative Lesart im Sinne der e^2-Warnung von A130.
 Ohne theorieinterne Herleitung bleibt (c) der korrekte Buchungsstand.""")
