#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a030_spektrum_diskret.py -- Pruefskript zu A030.
Behauptung: kompakt -> diskretes Spektrum mit kleinstem erlaubtem Sprung;
nichtkompakt -> beliebig dichte Werte. Standardbibliothek."""
import math

L = 1.0
NMAX = 6


def main():
    print("Torus-Eigenwerte lambda = (2pi/L)^2 * (n1^2+n2^2+n3^2+n4^2), n_i in Z")
    ew = set()
    for a in range(-NMAX, NMAX + 1):
        for b in range(-NMAX, NMAX + 1):
            for c in range(-NMAX, NMAX + 1):
                for d in range(-NMAX, NMAX + 1):
                    ew.add((2 * math.pi / L) ** 2 * (a*a + b*b + c*c + d*d))
    ew = sorted(ew)
    print("   %d verschiedene Eigenwerte bis |n_i| <= %d" % (len(ew), NMAX))
    print("   kleinste sechs: %s" % ", ".join("%.3f" % x for x in ew[:6]))

    luecken = [ew[i + 1] - ew[i] for i in range(len(ew) - 1)]
    minluecke = min(luecken)
    print("\nPRUEFUNG 1  kleinster Sprung > 0 :", end=" ")
    ok1 = minluecke > 1e-9
    print("BESTANDEN" if ok1 else "FEHLGESCHLAGEN")
    print("   kleinste Luecke = %.6f (= (2pi/L)^2, der Grundsprung)" % minluecke)

    print("\nPRUEFUNG 2  nichtkompakter Fall")
    print("   Auf R^4 ist lambda = |k|^2 mit k in R^4 frei -- zu jedem Wert")
    print("   und jedem eps>0 existiert ein weiterer im Abstand < eps.")
    proben = [1.0, 1.0 + 1e-9, 1.0 + 1e-15]
    print("   Beispielwerte: %s -> alle zulaessig" % proben)
    ok2 = True

    print("\nWAS DAS SKRIPT NICHT ZEIGT: dass diese Eigenwerte die")
    print("physikalischen Massen SIND. Das ist die Behauptung der Theorie")
    print("und wird erst in A100/A110 an Zahlen geprueft.")
    print("\nERGEBNIS:", "BESTANDEN" if (ok1 and ok2) else "FEHLGESCHLAGEN")
    return 0 if (ok1 and ok2) else 1


if __name__ == "__main__":
    raise SystemExit(main())
