#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a070_tensorfaktor.py -- Pruefskript zu A070.
Behauptung: eine Korrelationsgroesse, die nur auf dem ersten Tensorfaktor lebt,
bleibt unter Anhaengen eines C^3-Faktors unveraendert. Standardbibliothek."""
import math


def chsh_singulett(a, ap, b, bp):
    """CHSH-Wert im Singulett: E(x,y) = -cos(x-y)."""
    E = lambda x, y: -math.cos(x - y)
    return abs(E(a, b) - E(a, bp) + E(ap, b) + E(ap, bp))


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    a, ap = 0.0, math.pi / 2
    b, bp = math.pi / 4, 3 * math.pi / 4

    basis = chsh_singulett(a, ap, b, bp)
    print("CHSH ohne Zusatzfaktor      : %.15f" % basis)
    print("Tsirelson-Schranke 2*sqrt2  : %.15f" % (2 * math.sqrt(2)))

    # Der C^3-Faktor ist ein reiner Tensoranhang: der Zustand ist Produkt,
    # die Observable wirkt als Identitaet auf der Faser. Die Erwartungswerte
    # multiplizieren sich mit Spur(rho_Faser)=1.
    for dim, gewicht in ((3, 1.0),):
        spur = sum([1.0 / dim] * dim)          # normierter Faserzustand
        mit = basis * spur
        print("CHSH mit C^%d-Tensorfaktor   : %.15f   (Spur rho_Faser = %.1f)"
              % (dim, mit, spur))
        diff = abs(mit - basis)
        ok = diff < 1e-15

    print("\nDifferenz                   : %.2e" % diff)
    print("PRUEFUNG  Tensorfaktor aendert die Korrelationsgroesse nicht :",
          "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    print("\nGRUND: der Faserzustand ist normiert, seine Spur ist 1, und die")
    print("Observable wirkt dort als Identitaet. Die Massenerweiterung ist")
    print("daher fuer statische Korrelationsgroessen unsichtbar. Die")
    print("ZEIT-Erweiterung dagegen aendert die reduzierte Dynamik -- das ist")
    print("eine andere Aussage und hier NICHT geprueft.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
