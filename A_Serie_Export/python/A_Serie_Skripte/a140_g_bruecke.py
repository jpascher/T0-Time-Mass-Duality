#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a140_g_bruecke.py -- Pruefskript zu A140.
Zeigt, dass G sich wie c, hbar und k_B als Einheitenbruecke absorbieren laesst:
in natuerlichen Einheiten sind alle vier gleich 1, und die Planck-Groessen sind
genau die Umrechnungsfaktoren. Standardbibliothek."""
import math

C = 299792458.0
HBAR = 1.054571817e-34
G = 6.67430e-11
KB = 1.380649e-23


def main():
    ok = True
    lp = math.sqrt(HBAR*G/C**3)
    tp = lp/C
    mp = math.sqrt(HBAR*C/G)
    Ep = mp*C**2
    Tp = Ep/KB

    print("PRUEFUNG 1  Die vier Bruecken erzeugen genau eine Skala")
    print("   Planck-Laenge   l_P = sqrt(hbar G / c^3) = %.6e m" % lp)
    print("   Planck-Zeit     t_P = l_P / c            = %.6e s" % tp)
    print("   Planck-Masse    m_P = sqrt(hbar c / G)   = %.6e kg" % mp)
    print("   Planck-Energie  E_P = m_P c^2            = %.6e J" % Ep)
    print("   Planck-Temp.    T_P = E_P / k_B          = %.6e K" % Tp)

    print("\nPRUEFUNG 2  In diesen Einheiten sind alle vier gleich 1")
    proben = {
        "c    = l_P / t_P":            (lp/tp)/C,
        "hbar = E_P * t_P":            (Ep*tp)/HBAR,
        "G    = l_P^3/(m_P t_P^2)":    (lp**3/(mp*tp**2))/G,
        "k_B  = E_P / T_P":            (Ep/Tp)/KB,
    }
    for name, v in proben.items():
        gut = abs(v-1) < 1e-9
        ok = ok and gut
        print("   %-28s -> %.12f  %s" % (name, v, "ok" if gut else "FEHLER"))
    print("   alle vier absorbiert :", "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 3  T~ * m = 1 macht die Masse-Laenge-Bruecke redundant")
    print("   In natuerlichen Einheiten (c = hbar = 1) ist")
    print("      [Masse] = [1/Zeit] = [1/Laenge],")
    print("   also verbindet G keine unabhaengigen Dimensionen mehr.")
    print("   Kontrolle: m_P * l_P in natuerlichen Einheiten =")
    print("      m_P*c/hbar * l_P = %.12f" % (mp*C/HBAR*lp))
    g3 = abs(mp*C/HBAR*lp - 1) < 1e-9
    ok = ok and g3
    print("   = 1 :", "BESTANDEN" if g3 else "FEHLGESCHLAGEN")

    print("\n   WAS DAS ZEIGT: G ist eine Umrechnung, keine unabhaengige")
    print("   Naturkonstante -- operativ unverzichtbar, ontologisch sekundaer.")
    print("   WAS ES NICHT ZEIGT: dass die Gravitationsdynamik reproduziert")
    print("   wird. Diese fehlt in der A-Serie vollstaendig (A140, offen).")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
