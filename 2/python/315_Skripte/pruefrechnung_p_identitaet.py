#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruefrechnung_p_identitaet.py -- Nachrechnung des offenen Teils aus der
K_frak-Formdiskriminierung: die Identitaet p = -(2-sqrt3).

Ansatz aus A130 (Weg 2):   E0^2 = 4*sqrt(2) * m_mu * xi^q     (q = -p > 0)
Weg 1:                     E0^2 = m_e * m_mu                  (geom. Mittel^2)

Aus  (E0_Weg2/E0_Weg1)^-2 = K  folgt der Exponent q EXAKT als Funktion
der angenommenen K-Form:

    xi^q = m_e * K^-1 / (4*sqrt2)
    q(K) = ln( m_e / (K * 4*sqrt2) ) / ln(xi)

Wir bestimmen q* fuer BEIDE K-Formen (additiv 74/75, multiplikativ
(1-xi)^100), pruefen den Abstand zu 2-sqrt3 und scannen FAIR fuer beide
einen Kandidatenraum geschlossener Ausdruecke und einfacher Brueche:
vielleicht sitzt bei der multiplikativen Form ja ein ebenso schoener
Kandidat -- dann waere das Argument wertlos.
Standardbibliothek, hohe Praezision via mpmath-freiem Decimal wo noetig.
"""
import math
from fractions import Fraction

XI = 4.0 / 30000.0
LNXI = math.log(XI)                       # -8.9227...
ME, ME_REL  = 0.51099895069, 3.0e-10      # CODATA 2022
MMU, MMU_REL = 105.6583755, 2.2e-8        # (nur zur Doku; m_mu kuerzt sich!)

K_ADD = 74.0 / 75.0
K_MUL = (1.0 - XI) ** 100

def q_von(K):
    """Exakter Exponent q, damit Weg2/Weg1 die Form K reproduziert.
    m_mu kuerzt sich heraus -- q haengt nur an m_e, K, 4sqrt2, xi."""
    return math.log(ME / (K * 4.0 * math.sqrt(2))) / LNXI

Q_ADD = q_von(K_ADD)
Q_MUL = q_von(K_MUL)
Q_GEO = 2.0 - math.sqrt(3.0)              # Kandidat 2-sqrt3 = tan(15 Grad)

# Unsicherheitsboden: nur m_e geht ein (m_mu kuerzt sich!)
DQ_MASS = ME_REL / abs(LNXI)              # ~3.4e-11 -- praktisch exakt

print("=" * 74)
print("NACHRECHNUNG: die p-Identitaet  q = 2-sqrt3  (p = -q)")
print("=" * 74)
print(f"Hebel:  dK/K = |ln xi| * dq = {abs(LNXI):.4f} * dq")
print(f"m_mu kuerzt sich im Verhaeltnis heraus -> q* haengt NUR an m_e, xi,")
print(f"dem Praefaktor 4*sqrt2 und der angenommenen K-Form.")
print(f"Unsicherheitsboden aus m_e: dq = {DQ_MASS:.1e}  (q* ist damit scharf)")
print()
print(f"q* (additiv,  K=74/75)      = {Q_ADD:.9f}")
print(f"q* (multipl., K=(1-xi)^100) = {Q_MUL:.9f}")
print(f"Kandidat 2-sqrt3            = {Q_GEO:.9f}")
print()
d_add = Q_ADD - Q_GEO
d_mul = Q_MUL - Q_GEO
print(f"Abstand q*_add zu 2-sqrt3   = {d_add:+.3e}"
      f"   (-> auf K-Ebene {abs(LNXI)*abs(d_add):.2e})")
print(f"Abstand q*_mul zu 2-sqrt3   = {d_mul:+.3e}"
      f"   (-> auf K-Ebene {abs(LNXI)*abs(d_mul):.2e})")
print(f"Verhaeltnis                 = {abs(d_mul/d_add):.1f} : 1")

# ---------------------------------------------------------------- Fairness
print("\n" + "-" * 74)
print("FAIRNESS-SCAN: sitzt bei q*_add ODER q*_mul ein geschlossener")
print("Ausdruck? Beide Ziele bekommen denselben Kandidatenraum.")
print("-" * 74)

s2, s3, s5 = math.sqrt(2), math.sqrt(3), math.sqrt(5)
KANDIDATEN = {
    "2-sqrt3 (= tan 15deg = 1/(2+sqrt3))": 2 - s3,
    "sqrt3 - sqrt2":            s3 - s2,
    "(sqrt5-1)/2 - 1/3":        (s5 - 1) / 2 - 1 / 3,
    "1 - 1/e^(1/3)":            1 - math.exp(-1/3),
    "ln(4/3)":                  math.log(4/3),
    "ln(2)*0.386...? -> ln2/e": math.log(2)/math.e,
    "1/(2e) + 1/8? -> 1/(2e)":  1/(2*math.e),
    "pi/12":                    math.pi/12,
    "e/10":                     math.e/10,
    "3/2 - 4/pi? -> 4/15":      4/15,
    "27/100.77? -> 0.268=67/250": 67/250,
    "sqrt(2)/e - ? -> sqrt2/e": s2/math.e,
    "1/4 + xi*135? -> 1/4":     0.25,
    "(3-e)":                    3 - math.e,
    "1 - ln(2) - xi? -> 1-ln2": 1 - math.log(2),
    "sin(pi/12)+? -> sin15deg": math.sin(math.pi/12),
    "cos(74.45deg)? weglassen": None,
    "10*(3-D_eff), D_eff=2.973": 10*(3-2.973),
}

def scan(ziel, name):
    print(f"\n  Ziel {name} = {ziel:.9f}")
    treffer = []
    for label, wert in KANDIDATEN.items():
        if wert is None:
            continue
        d = wert - ziel
        if abs(d) < 2e-3:
            treffer.append((abs(d), label, wert, d))
    for absd, label, wert, d in sorted(treffer)[:5]:
        print(f"    {label:38s} = {wert:.9f}   Diff {d:+.2e}")
    # Brueche: beste rationale Naeherungen (Kettenbruch), Nenner <= 2000
    fr = Fraction(ziel).limit_denominator(2000)
    print(f"    beste rationale Naeherung (Nenner<=2000): {fr} = {float(fr):.9f}"
          f"   Diff {float(fr)-ziel:+.2e}")

scan(Q_ADD, "q*_add")
scan(Q_MUL, "q*_mul")

# ---------------------------------------------------------------- Restanalyse
print("\n" + "-" * 74)
print("RESTANALYSE: selbst q*_add trifft 2-sqrt3 nicht exakt.")
print("-" * 74)
print(f"  Rest dq = {d_add:+.3e}; Unsicherheitsboden {DQ_MASS:.0e} ->")
print(f"  der Rest ist REAL (Faktor {abs(d_add)/DQ_MASS:.0f} ueber dem Boden).")
print(f"  Auf K-Ebene: {abs(LNXI)*abs(d_add):.2e}; auf m_e-Ebene dieselbe Zahl,")
print(f"  denn m_e geht linear ein.")
print("  Vergleich mit Theorie-internen Kleingroessen:")
rest_K = abs(LNXI) * abs(d_add)
for label, wert in (("xi", XI), ("xi/10", XI/10), ("100*xi^2", 100*XI**2),
                    ("xi*ln(1/xi)", XI*abs(LNXI)), ("(100xi)^2/13.3", (100*XI)**2/13.3)):
    print(f"    Rest / {label:14s} = {rest_K/wert:8.3f}")
print("""  -> Kein offensichtlicher Theorie-Term erklaert den Rest exakt;
     rest_K ~ 0.10*xi bleibt als beobachteter Ueberschuss stehen.""")

# ---------------------------------------------------------------- Praefaktor
print("-" * 74)
print("GEGENPROBE PRAEFAKTOR: erzwingt man q = 2-sqrt3 EXAKT, welcher")
print("Praefaktor C ersetzt dann 4*sqrt2 (additiv)?")
C_add = ME / (K_ADD * XI ** Q_GEO)
C_mul = ME / (K_MUL * XI ** Q_GEO)
print(f"  C_add = {C_add:.7f}   4sqrt2 = {4*s2:.7f}   C/4sqrt2-1 = {C_add/(4*s2)-1:+.2e}")
print(f"  C_mul = {C_mul:.7f}   4sqrt2 = {4*s2:.7f}   C/4sqrt2-1 = {C_mul/(4*s2)-1:+.2e}")
print("""  -> Der Praefaktor-Fehlbetrag ist mit dem q-Rest austauschbar
     (ein Freiheitsgrad, zwei Schreibweisen); die Konstruktion fixiert
     nur das PRODUKT 4sqrt2 * xi^q.""")

# ---------------------------------------------------------------- Fazit
print("\n" + "=" * 74)
print("FAZIT DER NACHRECHNUNG")
print("=" * 74)
print(f"""\
 1. q* ist scharf bestimmbar (m_mu kuerzt sich, m_e-Fehler ~1e-10):
    q*_add = {Q_ADD:.7f},  q*_mul = {Q_MUL:.7f}.
 2. 2-sqrt3 liegt {abs(d_mul/d_add):.0f}x naeher an q*_add als an q*_mul.
    Der Fairness-Scan findet fuer q*_mul KEINEN vergleichbar einfachen
    geschlossenen Ausdruck in gleicher Naehe.
 3. ABER: auch q*_add trifft 2-sqrt3 nicht exakt (Rest {d_add:+.1e} in q,
    {rest_K:.1e} auf K-Ebene, weit ueber dem m_e-Fehlerboden). Die
    Identitaet p = -(2-sqrt3) ist damit NAHELIEGEND, aber NICHT exakt
    erfuellt -- entweder ist der Praefaktor 4sqrt2 nur naeherungsweise
    richtig, oder q hat einen anderen exakten Wert, oder es fehlt ein
    Term der Ordnung ~0.1*xi.
 4. Konsequenz fuer die Formfrage: Das 7.5:1-Argument zugunsten additiv
    bleibt als RELATIVE Aussage bestehen (additiv passt deutlich besser
    zu 2-sqrt3), wird aber nicht zur exakten Identitaet aufgewertet.
    Status von Weg 2 damit praezisiert: [B]-Konstruktion mit einem
    empirisch bestimmten Exponenten nahe 2-sqrt3, Restterm offen.""")
