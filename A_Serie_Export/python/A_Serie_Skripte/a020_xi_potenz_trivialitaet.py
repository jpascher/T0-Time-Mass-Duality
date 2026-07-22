#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a020_xi_potenz_trivialitaet.py -- Pruefskript zu A020, "Dritte Setzung"

Behauptung im Text:
  Ein Ausdruck der Form X = xi^N ist bei freiem Exponenten aussagelos, weil
  sich zu JEDER positiven Zielgroesse ein passendes N finden laesst.

Gegenprobe, nicht Illustration: das Skript nimmt Zielgroessen, die mit der
Theorie erkennbar nichts zu tun haben, und zeigt, dass auch sie sich als
xi-Potenz schreiben lassen. Wenn das gelingt, traegt die blosse Darstellbarkeit
keine Information.

Reine Standardbibliothek.
"""
import math

XI = 4.0 / 30000.0

# Zielgroessen: bewusst theoriefremd gewaehlt.
ZIELE = {
    "Feinstrukturkonstante 1/137,036": 1.0 / 137.035999,
    "Verhaeltnis Proton/Elektron":     1836.152673,
    "Koerpergroesse in Lichtjahren":   1.80 / 9.4607e15,
    "Preis eines Kaffees in Euro":     3.50,
    "Zahl pi":                         math.pi,
    "Anteil 1/3":                      1.0 / 3.0,
}


def exponent_fuer(x):
    """N mit xi^N = x, also N = ln(x)/ln(xi)."""
    return math.log(x) / math.log(XI)


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    print("xi = %.12e   ln(xi) = %.12f\n" % (XI, math.log(XI)))
    print("%-34s %14s %10s %12s" % ("Zielgroesse", "Wert", "N", "Rueckprobe"))
    print("-" * 74)

    alle_ok = True
    for name, x in ZIELE.items():
        N = exponent_fuer(x)
        zurueck = XI ** N
        rel = abs(zurueck - x) / abs(x)
        ok = rel < 1e-12
        alle_ok = alle_ok and ok
        print("%-34s %14.6e %10.4f %12.2e" % (name, x, N, rel))

    print("\nPRUEFUNG  jede Zielgroesse als xi-Potenz darstellbar :",
          "BESTANDEN" if alle_ok else "FEHLGESCHLAGEN")

    print("\nSCHLUSS: Auch der Kaffeepreis ist eine xi-Potenz. Die Darstellung")
    print("X = xi^N traegt daher fuer sich keine Information. Sie wird erst zu")
    print("einer Aussage, wenn N unabhaengig festgelegt ist -- durch Geometrie,")
    print("Abzaehlung oder Rekursionstiefe. Das ist der Inhalt von P35.")

    print("\nGRENZE DES SKRIPTS: es widerlegt keine einzige konkrete")
    print("xi-Potenz-Relation des Korpus. Es zeigt nur, dass die blosse Form")
    print("nichts beweist. Ob ein bestimmtes N unabhaengig begruendet ist,")
    print("muss an der jeweiligen Stelle geprueft werden.")

    return 0 if alle_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
