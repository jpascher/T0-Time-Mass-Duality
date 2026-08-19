#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""z12_gitterfaktor_waermekern.py -- Herkunft des Gitterfaktors und
Charakter der Waermekern-Differenz.

Zwei Fragen, die die Faktorisierung
    Z_{Z^4}(s) = 8 (1 - 4^{1-s}) zeta(s) zeta(s-1)
und der Waermekern-Vergleich aus Dok. 314 aufwerfen:

  TEIL A  Woher kommt der Faktor (1 - 4^{1-s})? Hat seine
          Nullstellenleiter s = 1 + 2*pi*i*k/ln4 eine Bedeutung im
          Rahmen?
  TEIL B  Der D4/Z^4-Unterschied im Waermekern ist exponentiell klein.
          Steckt darin eine Feinstruktur, die als Pruefflaeche taugt?

Beide Antworten sind negativ und haben eine einfache Ursache: der
Faktor ist die Dirichlet-Signatur des Jacobischen Vier-Quadrate-Satzes,
und der Gitterunterschied ist eine Paritaetsbedingung.
Nur Standardbibliothek.
"""
import math
from itertools import product

XI = 4.0 / 30000.0


def r4_gezaehlt(n):
    """Anzahl der Darstellungen von n als Summe von vier Quadraten,
    direkt abgezaehlt."""
    c = 0
    L = math.isqrt(n)
    for a in range(-L, L + 1):
        a2 = a * a
        for b in range(-L, L + 1):
            ab = a2 + b * b
            if ab > n:
                continue
            for d in range(-L, L + 1):
                abd = ab + d * d
                if abd > n:
                    continue
                rest = n - abd
                w = math.isqrt(rest)
                if w * w == rest:
                    c += 1 if w == 0 else 2
    return c


def r4_jacobi(n):
    """Jacobi 1834: r_4(n) = 8 * sum_{d|n, 4 nicht teilt d} d."""
    return 8 * sum(d for d in range(1, n + 1) if n % d == 0 and d % 4 != 0)


def schalen(gitter, R=12):
    """Schalenbesetzung: Norm -> Anzahl Gittervektoren."""
    d = {}
    for k in product(range(-R, R + 1), repeat=4):
        if gitter == "D4" and sum(k) % 2:
            continue
        n = sum(x * x for x in k)
        if 0 < n <= R * R:
            d[n] = d.get(n, 0) + 1
    return d


if __name__ == "__main__":
    print("=" * 74)
    print("Z12 -- GITTERFAKTOR UND WAERMEKERN-DIFFERENZ")
    print("=" * 74)

    # ---------------------------------------------------- TEIL A
    print("\nTEIL A: Woher kommt (1 - 4^{1-s})?")
    print("-" * 74)
    print("""   Die Faktorisierung laesst den Faktor 4 wie eine freie Struktur
   aussehen. Er ist es nicht: er folgt aus dem Jacobischen
   Vier-Quadrate-Satz. Mit r_4(n) als Anzahl der Darstellungen von n
   als Summe von vier Quadraten gilt

       r_4(n) = 8 * sum_{d|n, 4 nicht teilt d} d        (Jacobi 1834)

   und daraus fuer die Dirichlet-Reihe

       sum_n r_4(n) n^{-s} = 8 zeta(s) zeta(s-1) (1 - 4^{1-s}).

   Der Faktor kodiert also die Bedingung '4 teilt d nicht' -- eine
   Teilbarkeitsbedingung, keine geometrische Struktur.""")
    print(f"\n   Verifikation:")
    print(f"   {'n':>4} {'abgezaehlt':>12} {'Jacobi':>10}  Uebereinstimmung")
    for n in range(1, 13):
        a, b = r4_gezaehlt(n), r4_jacobi(n)
        print(f"   {n:>4} {a:>12} {b:>10}  {'ja' if a == b else 'NEIN'}")
        assert a == b, f"Jacobis Satz verletzt bei n={n}"

    print("\n   Die Nullstellenleiter des Faktors:")
    leiter = 2 * math.pi / math.log(4.0)
    print(f"     1 - 4^{{1-s}} = 0  <=>  s = 1 + 2*pi*i*k/ln4")
    print(f"     Sprossenabstand 2pi/ln4 = pi/ln2 = {leiter:.6f}")
    print(f"\n   Hat diese Zahl eine Bedeutung im Rahmen?")
    kandidaten = {
        "4 (Vorfaktor in L*, R73)": 4.0,
        "2pi": 2 * math.pi,
        "ln(1/xi)": -math.log(XI),
        "16/pi^2 = 1/Delta(D4)": 16 / math.pi ** 2,
        "D4-Kusszahl 24": 24.0,
        "Bulk-Exponent 36": 36.0,
    }
    print(f"   {'Groesse':>26} {'Wert':>12} {'Verhaeltnis':>12}")
    beste = None
    for name, v in sorted(kandidaten.items(),
                          key=lambda x: abs(math.log(x[1] / leiter))):
        rel = v / leiter
        if beste is None:
            beste = abs(rel - 1)
        print(f"   {name:>26} {v:12.6f} {rel:12.4f}")
    print(f"\n   naechste Groesse liegt {beste:.0%} daneben.")
    assert beste > 0.10, "Unerwartet enger Treffer -- pruefen"
    print("""   => kein Treffer, und es waere auch keiner zu erwarten:
      ln4 = 2 ln2 stammt aus der Teilbarkeitsbedingung, nicht aus
      einer Laenge des Rahmens. Die 4 ist zwar die Zahl der Quadrate
      und damit die Dimension, wirkt hier aber arithmetisch.""")

    # ---------------------------------------------------- TEIL B
    print("\nTEIL B: Der D4/Z^4-Unterschied im Waermekern")
    print("-" * 74)
    sZ, sD = schalen("Z4"), schalen("D4")
    print(f"   {'Norm n':>7} {'Z^4':>8} {'D4':>8}  Bemerkung")
    for n in range(1, 13):
        a, b = sZ.get(n, 0), sD.get(n, 0)
        bem = "D4 leer (ungerade Norm)" if b == 0 else (
            "Kusszahl 24" if n == 2 else "identisch")
        print(f"   {n:>7} {a:>8} {b:>8}  {bem}")
        if n % 2:
            assert b == 0, "D4 duerfte keine ungeraden Normen haben"
        else:
            assert a == b, "bei geraden Normen sollten beide gleich sein"
    print("""
   => D4 besetzt ausschliesslich GERADE Normen; bei den geraden
      stimmen beide Gitter exakt ueberein. Das ist der gesamte
      Unterschied -- eine Paritaetsbedingung, keine Feinstruktur.""")

    print("\n   Waermespur Theta(t) = sum e^{-n t} ueber die Schalen:")
    print(f"   {'t':>7} {'Theta_Z4 - 1':>16} {'Theta_D4 - 1':>16} "
          f"{'rel. Diff.':>12}")
    for t in (0.05, 0.1, 0.3, 1.0, 3.0, 8.0):
        TZ = sum(c * math.exp(-n * t) for n, c in sZ.items())
        TD = sum(c * math.exp(-n * t) for n, c in sD.items())
        print(f"   {t:7.2f} {TZ:16.6e} {TD:16.6e} {(TZ-TD)/TZ:12.4f}")
    print("""
   Bei kleinem t dominiert der Weyl-Term beide Reihen gleichermassen;
   bei grossem t sind beide exponentiell klein. Dazwischen waechst
   der relative Unterschied zwar, aber es gibt keine Groesse des
   Rahmens, die die Waermespur bei mittlerem t abbildet: Die
   physikalisch ausgewertete Stelle ist der Casimir-Punkt
   s = -1/2, also die Mellin-Transformierte, und dort liegt die
   Auswertung in Dok. 314 bereits vor.""")

    print("\n" + "=" * 74)
    print("ERGEBNIS Z12")
    print("=" * 74)
    print("""   [K] Der Gitterfaktor (1 - 4^{1-s}) ist die Dirichlet-Signatur
   des Jacobischen Vier-Quadrate-Satzes. Seine Nullstellenleiter
   ist eine Eigenschaft der Summe von vier Quadraten und hat keinen
   Bezug zum Vorfaktor 4 in L* (R73) oder zur D4-Struktur.

   [K] Die Waermekern-Differenz zwischen D4 und Z^4 beruht auf einer
   Paritaetsbedingung: D4 besetzt nur gerade Normen, bei diesen sind
   beide Gitter identisch. Eine Pruefflaeche entsteht daraus nicht;
   die aussagekraeftige Stelle ist der Casimir-Punkt, und der ist
   ausgewertet.""")
    print("\nAlle Checks bestanden.")
