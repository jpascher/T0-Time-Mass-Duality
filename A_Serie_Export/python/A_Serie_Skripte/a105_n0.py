#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A105 -- Die Leiter-Grundeinheit N_0.

Prueft: Toleranz N_0 = 38.52 +- 0.21; sigma-Abstaende der Kandidaten;
Zielrueckrechnung Delta = 3/(4pi) gegen die Luecke; Generationenlauf N_g = g*N_0.
Kein Zielwert wird in einen Ausdruck eingesetzt -- die Kandidaten werden
unabhaengig gerechnet und nur MIT dem Band verglichen.
"""
import math
from _bereich import identitaet, im_bereich


def main():
    ok = True
    phi = (1 + math.sqrt(5)) / 2
    pi = math.pi
    N0, sig = 38.52, 0.21

    def sigma(x):
        return (x - N0) / sig

    print("A105 -- Die Leiter-Grundeinheit N_0")
    print("=" * 60)
    print("\nTOLERANZ  N_0 = %.2f +- %.2f  (rel. %.1f%%, aus m_tau +-0.12 MeV)"
          % (N0, sig, 100 * sig / N0))

    print("\nKANDIDATEN (unabhaengig gerechnet, dann mit dem Band verglichen)")
    c = {
        "100/phi^2":            100 / phi ** 2,
        "3*(pi^2/2)*phi^2":     3 * (pi ** 2 / 2) * phi ** 2,
        "ln(M_Pl/v)":           math.log(1.22e19 / 246.0),
        "100/e":                100 / math.e,
    }
    for name, val in c.items():
        drin = abs(sigma(val)) <= 3.0
        print("   %-18s = %8.4f   %+5.2f sigma   %s"
              % (name, val, sigma(val), "im Band" if drin else "AUSSERHALB"))

    # Zulaessig = innerhalb ~2 sigma; 100/e muss ausserhalb liegen
    g1 = im_bereich("3*(pi^2/2)*phi^2 im Band", c["3*(pi^2/2)*phi^2"], N0,
                    faktor=1.0 + 2 * sig / N0)
    g2 = im_bereich("100/phi^2 im Band", c["100/phi^2"], N0,
                    faktor=1.0 + 2 * sig / N0)
    g3 = not (abs(sigma(c["100/e"])) <= 3.0)  # 100/e MUSS draussen sein
    print("   -> 100/e ausserhalb 3 sigma:", "JA (ausgeschlossen)" if g3 else "NEIN")
    ok = ok and g1 and g2 and g3

    print("\nWARNBEISPIEL  Ziel zuerst, Begruendung danach")
    luecke = c["3*(pi^2/2)*phi^2"] - N0
    delta = 3 / (4 * pi)
    print("   Luecke 3*(pi^2/2)*phi^2 - 38.52 = %.4f" % luecke)
    print("   'Anomalie' Delta = 3/(4pi)      = %.4f" % delta)
    g4 = im_bereich("Delta == Luecke (Zielrueckrechnung)", delta, luecke,
                    faktor=1.01)
    ok = ok and g4
    print("   -> auf 3 Stellen gleich: die Anomalie IST die Luecke, nachtraeglich")
    print("      benannt. Ein Loop-Faktor waere 1/(4pi)^2, eine echte Anomalie")
    print("      quantisiert (ganzzahlig) -- der Anstrich passt nicht auf die Zahl.")

    print("\nGENERATIONENLAUF  N_g = g*N_0 (N_0 ist kein fester Faktor)")
    for g in (1, 2, 3):
        print("   g=%d -> N_g = %.1f" % (g, g * N0))
    print("   -> selbst eine geschlossene Form fuer die Basis laesst das")
    print("      Generationengesetz unberuehrt.")

    print("\nMASSSTAB  Das Band (+-0.21) ist breit; viele Ausdruecke treffen es.")
    print("   Bandtreffer ist daher KEIN Test. N_0 ist offen: geschlossen durch")
    print("   eine Vorwaerts-Konstruktion, die haette danebentreffen koennen.")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
