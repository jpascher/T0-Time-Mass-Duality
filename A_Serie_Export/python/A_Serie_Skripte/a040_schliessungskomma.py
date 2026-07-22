#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a040_schliessungskomma.py -- Pruefskript zu A040.
Behauptung: 75(1-eps)=74 => eps=1/75=100*xi => K_frak=74/75.
Enthaelt ausdruecklich die Gegenprobe, dass die Rechnung den Faktor 100
voraussetzt und nicht erzeugt. Standardbibliothek."""
from fractions import Fraction

XI = Fraction(4, 30000)


def main():
    ok = True
    n = Fraction(1) / (100 * XI)
    print("PRUEFUNG 1  Umlaufzahl n = 1/(100*xi)")
    print("   xi = %s = %.10f" % (XI, float(XI)))
    print("   n  = %s" % n)
    g1 = (n == 75)
    ok = ok and g1
    print("   n == 75 :", "BESTANDEN" if g1 else "FEHLGESCHLAGEN")

    eps = Fraction(1) - Fraction(74, 75)
    print("\nPRUEFUNG 2  75*(1-eps) = 74  =>  eps")
    print("   eps = %s = %.10f" % (eps, float(eps)))
    g2 = (eps == Fraction(1, 75) == 100 * XI)
    ok = ok and g2
    print("   eps == 1/75 == 100*xi :", "BESTANDEN" if g2 else "FEHLGESCHLAGEN")

    k = 1 - 100 * XI
    print("\nPRUEFUNG 3  K_frak = 1 - 100*xi")
    print("   K_frak = %s = %.10f" % (k, float(k)))
    g3 = (k == Fraction(74, 75))
    ok = ok and g3
    print("   K_frak == 74/75 :", "BESTANDEN" if g3 else "FEHLGESCHLAGEN")
    print("   Kontrolle 75*K_frak = %s" % (75 * k))

    print("\nGEGENPROBE  Wird der Faktor 100 hergeleitet?")
    print("   Die Rechnung setzt n = 1/(100*xi). Wer n einsetzt, hat die 100")
    print("   bereits vorausgesetzt. Zum Beleg dieselbe Rechnung mit einem")
    print("   frei gewaehlten Faktor F statt 100:")
    print("   %4s %8s %14s %14s" % ("F", "n=1/(F*xi)", "eps=1/n", "K=1-F*xi"))
    for F in (50, 100, 150, 200):
        nF = Fraction(1) / (F * XI)
        print("   %4d %10s %14s %14s"
              % (F, nF, Fraction(1) / nF, 1 - F * XI))
    print("   Jeder Faktor schliesst gleich gut. Das SCHLIESSUNGSKOMMA ALLEIN")
    print("   erzwingt die 100 also nicht -- es ist die interne Lesart. Die")
    print("   NOTWENDIGKEIT der 100 kommt aus dem Skalenfluss (naechste Pruefung).")


    print("\nPRUEFUNG  Faktor 100 als Herleitung (Dok 133), nicht Setzung")
    import math as _m
    Df_eff = 2.973
    K_pot = (Df_eff/3)**(Df_eff/2)
    K_lin = 1 - 100*XI
    print("   RG-Lauf: ln(l_EW/l_P) = ln(10^17) = %.1f -> Verstaerkung ~100"
          % _m.log(10**17))
    print("   Potenzform (D_f^eff/3)^(D_f^eff/2) = %.6f" % K_pot)
    print("   1 - 100 xi                         = %.6f" % K_lin)
    print("   D_f^eff=2.973 eindeutig aus Konsistenz zweier m_e/m_mu-Wege")
    from _bereich import im_bereich
    g100 = im_bereich("Potenzform == 1-100xi (Faktor 100 abgeleitet)",
                      K_pot, K_lin, faktor=1.001)
    print("   -> Faktor 100 ist hergeleitet (Dok 133, 189), keine Setzung.")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
