#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a040_dimensionsdefizit.py -- Pruefskript zu A040.
Behauptung: bei nichtverschwindendem Torus-Mittelwert von f geht die Korrektur
mit xi^1 ein, bei volumenerhaltender Welligkeit erst mit xi^2.
Standardbibliothek."""
import math

M = 4000


def mittel(f):
    return sum(f(2 * math.pi * i / M) for i in range(M)) / M


def verschiebung(f, xi):
    """Eigenwertverschiebung 1. Ordnung, hier als Mittelwert-Integral."""
    return mittel(lambda t: xi * f(t))


def exponent(f):
    """Numerischer Exponent p in delta ~ xi^p."""
    x1, x2 = 1e-4, 1e-5
    d1 = abs(verschiebung(f, x1))
    d2 = abs(verschiebung(f, x2))
    if d1 < 1e-18 or d2 < 1e-18:
        # rein 2. Ordnung: <f>=0, dann traegt erst <f^2>
        d1 = abs(mittel(lambda t: (x1 * f(t)) ** 2))
        d2 = abs(mittel(lambda t: (x2 * f(t)) ** 2))
    return math.log(d1 / d2) / math.log(x1 / x2)


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    defizit = lambda t: 1.0 + 0.3 * math.cos(3 * t)     # <f> = 1  != 0
    welle   = lambda t: math.cos(3 * t)                  # <f> = 0

    print("Fall A  Dimensionsdefizit  f(t) = 1 + 0.3*cos(3t)")
    print("   <f> = %.12f" % mittel(defizit))
    pA = exponent(defizit)
    print("   numerischer Exponent p = %.4f" % pA)

    print("\nFall B  volumenerhaltende Welligkeit  f(t) = cos(3t)")
    print("   <f> = %.12e" % mittel(welle))
    pB = exponent(welle)
    print("   numerischer Exponent p = %.4f" % pB)

    okA = abs(pA - 1.0) < 0.05
    okB = abs(pB - 2.0) < 0.05
    print("\nPRUEFUNG 1  Defizit -> p = 1 :", "BESTANDEN" if okA else "FEHLGESCHLAGEN")
    print("PRUEFUNG 2  Welligkeit -> p = 2 :", "BESTANDEN" if okB else "FEHLGESCHLAGEN")

    print("\nGRENZE: das Skript zeigt den Mechanismus an einer gewaehlten")
    print("Funktion f. Die Funktion f der Theorie ist NICHT bestimmt (A040,")
    print("'Was offen bleibt') -- gezeigt ist der Zusammenhang zwischen")
    print("Mittelwert und Potenz, nicht der konkrete Wert.")
    return 0 if (okA and okB) else 1


if __name__ == "__main__":
    raise SystemExit(main())
