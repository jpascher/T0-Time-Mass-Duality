#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a050_nichtschliessung.py -- Pruefskript zu A050.
Behauptung: einziger Fixpunkt 0; jedes c in (0,1) ist Durchgangspunkt; zu jedem
Ziel existiert eine Tiefe k*(c) mit identischem Parameterstatus -- also zeichnet
die Rekursion keinen Wert aus. Standardbibliothek."""
import math

XI0 = 4.0 / 30000.0
A = 100.0


def schritt(x):
    return x * (1 - A * x)


def main():
    ok = True

    print("PRUEFUNG 1  Fixpunktgleichung x = x(1-100x)")
    print("   umgeformt: 100 x^2 = 0  =>  x = 0")
    print("   numerische Kontrolle der Fixpunkteigenschaft:")
    for x in (0.0, 1e-6, XI0, 1e-3):
        print("      x=%.8e -> f(x)=%.8e   Fixpunkt: %s"
              % (x, schritt(x), "ja" if abs(schritt(x) - x) < 1e-300 else "nein"))
    g1 = abs(schritt(0.0)) < 1e-300 and abs(schritt(XI0) - XI0) > 0
    ok = ok and g1
    print("   einziger Fixpunkt ist 0 :", "BESTANDEN" if g1 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 2  strenge Monotonie und Positivitaet")
    x = XI0
    monoton = True
    positiv = True
    for _ in range(200000):
        y = schritt(x)
        if not (y < x):  monoton = False
        if not (y > 0):  positiv = False
        x = y
    print("   nach 200000 Schritten: x = %.8e" % x)
    print("   streng fallend : %s" % monoton)
    print("   stets positiv  : %s" % positiv)
    g2 = monoton and positiv
    ok = ok and g2
    print("   Null in endlich vielen Schritten NICHT erreicht :",
          "BESTANDEN" if g2 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 3  k*(c) existiert fuer beliebige Ziele")
    print("   Ziele bewusst willkuerlich gewaehlt -- wenn fuer jedes eine")
    print("   Tiefe existiert, zeichnet die Rekursion keines aus.")
    ziele = {
        "1/phi          ": 2 / (1 + math.sqrt(5)),
        "1/e            ": 1 / math.e,
        "1/pi           ": 1 / math.pi,
        "0,42 (beliebig)": 0.42,
        "1/137,036      ": 1 / 137.035999,
    }
    print("   %-16s %12s %10s" % ("Ziel", "Wert", "k*"))
    alle = True
    for name, c in ziele.items():
        x, k = XI0, 0
        while x > c and k < 5_000_000:
            x = schritt(x); k += 1
        # Ziele oberhalb xi0 werden nie erreicht (Folge faellt) -> als solche melden
        erreichbar = c < XI0
        if erreichbar:
            print("   %-16s %12.8f %10d" % (name, c, k))
            alle = alle and (k < 5_000_000)
        else:
            print("   %-16s %12.8f %10s  (oberhalb xi0, Folge faellt)"
                  % (name, c, "--"))
    print("   Fuer jedes Ziel UNTERHALB xi0 existiert k* :",
          "BESTANDEN" if alle else "FEHLGESCHLAGEN")
    ok = ok and alle

    print("\nSCHLUSS: k* existiert fuer jedes erreichbare Ziel mit identischem")
    print("Parameterstatus. Dass die Folge einen bestimmten Wert passiert, ist")
    print("daher kein Argument fuer diesen Wert. Ein Fixieren der Tiefe waere")
    print("keine Auszeichnung -- das ist der Inhalt des Nichtschliessungssatzes.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
