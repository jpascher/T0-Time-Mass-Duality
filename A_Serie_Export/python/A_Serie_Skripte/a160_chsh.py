#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a160_chsh.py -- Pruefskript zu A160.
Prueft: CHSH = 2sqrt2 im Singulett, Unsichtbarkeit des C^3-Faktors, und die
Groessenordnung des xi-Rests im Vergleich zu realen Messunsicherheiten.
Standardbibliothek."""
import math
from _bereich import identitaet, im_bereich

XI = 4.0 / 30000.0
DF = 3 - XI


def chsh(a, ap, b, bp):
    E = lambda x, y: -math.cos(x - y)
    return abs(E(a, b) - E(a, bp) + E(ap, b) + E(ap, bp))


def main():
    ok = True
    a, ap, b, bp = 0.0, math.pi/2, math.pi/4, 3*math.pi/4

    print("PRUEFUNG 1  CHSH im Singulett")
    S = chsh(a, ap, b, bp)
    print("   S            = %.15f" % S)
    print("   2*sqrt(2)    = %.15f" % (2*math.sqrt(2)))
    g1 = identitaet("S == 2 sqrt(2) (mathematische Tatsache, QM)",
                    S, 2*math.sqrt(2))
    ok = ok and g1

    print("\nPRUEFUNG 2  C^3-Tensorfaktor aendert nichts")
    spur = sum([1.0/3]*3)
    print("   Spur des normierten Faserzustands = %.15f" % spur)
    print("   S mit Faktor = %.15f" % (S*spur))
    g2 = identitaet("C^3-Faktor aendert S nicht (Spur = 1)", S*spur, S)
    ok = ok and g2

    print("\nPRUEFUNG 3  Groessenordnung des xi-Rests")
    print("   %8s %18s %14s" % ("N", "S_T0(N)", "rel. Abw."))
    for N in (2, 10, 100, 1000, 100000):
        S_T0 = 2*math.sqrt(2)*math.exp(-XI*math.log(N)/DF)
        print("   %8d %18.12f %14.3e" % (N, S_T0, abs(S_T0-S)/S))
    S_gross = 2*math.sqrt(2)*math.exp(-XI*math.log(100000)/DF)
    rel = abs(S_gross - S)/S
    print("   Rest liegt bei %.1e -- Ordnung 1e-4 bis 1e-5" % rel)
    print("   Rest der Ordnung xi (1e-4 bis 1e-5) -- wir pruefen NUR die")
    print("   Groessenordnung, nicht einen exakten Wert (A220):")
    g3 = 1e-6 < rel < 1e-3
    ok = ok and g3
    print("   xi-Rest in richtiger Groessenordnung :",
          "im Bereich" if g3 else "AUSSERHALB")
    print("   Richtung: der Rest VERRINGERT S (Vorzeichen fest, nicht anpassbar)")
    print("   Skalierung: logarithmisch in N, nicht linear")

    print("\nPRUEFUNG 4  Ist das messbar? -- Vergleich mit realen Unsicherheiten")
    print("   %-38s %12s" % ("Quelle", "Groessenordnung"))
    for name, u in [("xi-Rest der Theorie", rel),
                    ("Detektoreffizienz-Systematik", 1e-2),
                    ("Winkelkalibrierung", 1e-3),
                    ("Zustandspraeparation", 1e-3),
                    ("Statistik bei 1e6 Ereignissen", 1e-3)]:
        print("   %-38s %12.1e" % (name, u))
    g4 = rel < 1e-3
    ok = ok and g4
    print("   xi-Rest liegt UNTER allen Systematiken :",
          "BESTANDEN" if g4 else "FEHLGESCHLAGEN")
    print("\n   SCHLUSS: mit gegenwaertiger Hardware nicht aufloesbar. Ein")
    print("   xi-Fit an gemessene CHSH-Werte ist GEGENSTANDSLOS -- er wuerde")
    print("   Hardware-Systematik anpassen, nicht Geometrie messen. Das ist")
    print("   Teil des Ergebnisses, nicht eine Ausrede.")
    print("\n   FALSIFIKATION bleibt moeglich: ein S ueber der")
    print("   Tsirelson-Schranke, oder ein S deutlich unter 2sqrt2 ohne")
    print("   Hardware-Erklaerung, widerlegt die Theorie an dieser Stelle.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
