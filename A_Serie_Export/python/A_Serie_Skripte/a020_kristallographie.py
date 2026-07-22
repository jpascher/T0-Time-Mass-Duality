#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a020_kristallographie.py -- Pruefskript zu A020, Abschnitt "Zweite Setzung"

Behauptung im Text:
  Die kristallographische Restriktion 2*cos(2*pi/n) in Z erlaubt genau
  n in {1,2,3,4,6}. Die Fuenfzaehligkeit ist ausgeschlossen, die
  Dreizaehligkeit zugelassen.

Das Skript prueft die Behauptung, statt sie zu illustrieren: es rechnet die
Bedingung fuer alle n bis n_max aus und meldet die Menge der Loesungen.
Reine Standardbibliothek, kein Zufall, kein Seed noetig.
"""
import math

TOL = 1e-12
N_MAX = 100


def ist_ganzzahlig(x, tol=TOL):
    return abs(x - round(x)) < tol


def main():
    loesungen = []
    print("n    2*cos(2*pi/n)      ganzzahlig?")
    print("-" * 42)
    for n in range(1, N_MAX + 1):
        w = 2 * math.cos(2 * math.pi / n)
        ok = ist_ganzzahlig(w)
        if ok:
            loesungen.append(n)
        if n <= 12:
            print("%-4d %16.12f   %s" % (n, w, "ja" if ok else "nein"))

    print("\nLoesungsmenge bis n = %d: %s" % (N_MAX, loesungen))

    erwartet = [1, 2, 3, 4, 6]
    print("\nPRUEFUNG 1  Loesungsmenge == {1,2,3,4,6} :",
          "BESTANDEN" if loesungen == erwartet else "FEHLGESCHLAGEN")

    fuenf = 2 * math.cos(2 * math.pi / 5)
    print("PRUEFUNG 2  n=5 ausgeschlossen           :",
          "BESTANDEN" if not ist_ganzzahlig(fuenf) else "FEHLGESCHLAGEN")
    print("            2*cos(72 Grad) = %.12f = 1/phi" % fuenf)
    phi = (1 + math.sqrt(5)) / 2
    print("            1/phi          = %.12f" % (1 / phi))

    drei = 2 * math.cos(2 * math.pi / 3)
    print("PRUEFUNG 3  n=3 zugelassen               :",
          "BESTANDEN" if ist_ganzzahlig(drei) else "FEHLGESCHLAGEN")
    print("            2*cos(120 Grad) = %.1f" % drei)

    print("\nWAS DAS SKRIPT NICHT ZEIGT: warum von den erlaubten Werten")
    print("{1,2,3,4,6} gerade n=3 realisiert ist. Die Restriktion schliesst")
    print("aus, sie waehlt nicht aus. Siehe A020, 'Was offen bleibt'.")

    return 0 if (loesungen == erwartet and not ist_ganzzahlig(fuenf)
                 and ist_ganzzahlig(drei)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
