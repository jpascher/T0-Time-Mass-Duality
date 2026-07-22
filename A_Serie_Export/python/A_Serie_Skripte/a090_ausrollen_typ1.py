#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a090_ausrollen_typ1.py -- Pruefskript zu A090.
Behauptung: das Ausrollen S^1 -> R ist modenerhaltend und verliert nur die
Windungsinformation; die Rueckrichtung ist verlustbehaftet. Standardbibliothek."""
import math

N = 20000


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    ok = True

    print("PRUEFUNG 1  Ausrollen ist lokal treu (Ueberlagerung p: R -> S^1)")
    print("   Geprueft: p(t) = t mod 2pi ist lokal abstandserhaltend.")
    maxfehler = 0.0
    for i in range(N):
        t = 10 * math.pi * i / N
        dt = 1e-7
        d_oben = dt
        a, b = t % (2 * math.pi), (t + dt) % (2 * math.pi)
        d_unten = abs(b - a)
        if d_unten > math.pi:
            d_unten = 2 * math.pi - d_unten
        maxfehler = max(maxfehler, abs(d_oben - d_unten))
    g1 = maxfehler < 1e-12
    ok = ok and g1
    print("   maximaler lokaler Abstandsfehler: %.2e" % maxfehler)
    print("   :", "BESTANDEN" if g1 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 2  Rueckrichtung verliert die Windung")
    print("   Drei Wege auf R mit verschiedener Laenge, alle auf denselben")
    print("   Punkt des Kreises projiziert:")
    ziel = 0.75 * 2 * math.pi
    wege = [ziel, ziel + 2 * math.pi, ziel + 6 * math.pi]
    bilder = [w % (2 * math.pi) for w in wege]
    windungen = [int(w // (2 * math.pi)) for w in wege]
    print("   %14s %14s %10s" % ("t auf R", "p(t) auf S^1", "Windung"))
    for w, b, n in zip(wege, bilder, windungen):
        print("   %14.8f %14.8f %10d" % (w, b, n))
    ununterscheidbar = max(bilder) - min(bilder) < 1e-12
    unterschiedlich = len(set(windungen)) == 3
    g2 = ununterscheidbar and unterschiedlich
    ok = ok and g2
    print("   Bilder identisch, Windungen verschieden :",
          "BESTANDEN" if g2 else "FEHLGESCHLAGEN")
    print("   -> aus dem Bild allein ist die Windung nicht rekonstruierbar.")

    print("\nPRUEFUNG 3  Modenerhaltung")
    print("   Die Eigenfrequenzen e^{i n t} bleiben beim Ausrollen erhalten;")
    print("   verloren geht die Identifikation t ~ t + 2pi, nicht das Spektrum.")
    moden = [1, 2, 3, 5]
    erhalten = all(abs(math.cos(n * 0.3) - math.cos(n * (0.3 + 2 * math.pi)))
                   < 1e-12 for n in moden)
    ok = ok and erhalten
    print("   ganzzahlige Moden 2pi-periodisch :",
          "BESTANDEN" if erhalten else "FEHLGESCHLAGEN")

    print("\nSCHLUSS: hin verlustfrei, zurueck nicht. Die Asymmetrie ist der")
    print("Kern der Projektionskette. WAS DAS SKRIPT NICHT ZEIGT: warum")
    print("ueberhaupt ausgerollt wird und welche Richtung -- das ist in A090")
    print("auf den Messvorgang verschoben und dort ausdruecklich als Luecke")
    print("gebucht, nicht als Ergebnis.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
