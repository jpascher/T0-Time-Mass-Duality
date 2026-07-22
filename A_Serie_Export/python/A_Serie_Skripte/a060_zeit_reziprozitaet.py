#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a060_zeit_reziprozitaet.py -- Pruefskript zu A060.
Behauptungen: T*E=1 folgt aus T~*m=1; d_1=100*xi=1/75; Modenperioden sind
kommensurabel. Standardbibliothek."""
from fractions import Fraction

XI = Fraction(4, 30000)


def main():
    ok = True
    print("PRUEFUNG 1  T*E = 1 aus T~*m = 1")
    print("   Im natuerlichen System ist E = m (c = 1).")
    print("   %8s %14s %14s %10s" % ("m", "T~ = 1/m", "E = m", "T~*E"))
    for m in (Fraction(1, 2), Fraction(1), Fraction(7, 3), Fraction(1000)):
        T = 1 / m
        prod = T * m
        gut = (prod == 1)
        ok = ok and gut
        print("   %8s %14s %14s %10s" % (m, T, m, prod))
    print("   T~*E == 1 fuer alle Faelle :", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    print("   HINWEIS: das ist eine Identitaet, keine Ungleichung. Es ist")
    print("   ausdruecklich NICHT die Heisenberg-Relation, die eine Schranke")
    print("   ueber Streuungen ist und keine Gleichung ueber Einzelwerte.")

    print("\nPRUEFUNG 2  kleinstes Inkrement d_1 = 100*xi")
    d1 = 100 * XI
    print("   100*xi = %s = %.10f" % (d1, float(d1)))
    g2 = (d1 == Fraction(1, 75))
    ok = ok and g2
    print("   d_1 == 1/75 :", "BESTANDEN" if g2 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 3  Kommensurabilitaet der Modenperioden")
    print("   Moden mit Massen m_k = k * m_0 haben Perioden T_k = 1/(k*m_0).")
    print("   Kommensurabel heisst: alle Verhaeltnisse T_i/T_j sind rational.")
    m0 = Fraction(1, 75)
    perioden = [1 / (k * m0) for k in (1, 2, 3, 5, 8)]
    print("   %6s %16s" % ("k", "T_k"))
    for k, T in zip((1, 2, 3, 5, 8), perioden):
        print("   %6d %16s" % (k, T))
    alle_rational = all(isinstance(perioden[i] / perioden[j], Fraction)
                        for i in range(len(perioden))
                        for j in range(len(perioden)))
    ok = ok and alle_rational
    print("   alle Verhaeltnisse rational :",
          "BESTANDEN" if alle_rational else "FEHLGESCHLAGEN")
    print("   Beispiel T_1/T_3 = %s" % (perioden[0] / perioden[2]))

    print("\nGRENZE: die Kommensurabilitaet folgt hier aus der ANNAHME")
    print("ganzzahliger Massenverhaeltnisse. Ob die realen Modenmassen diese")
    print("Eigenschaft haben, ist eine Frage des Spektrums (A110), nicht")
    print("dieses Skripts. Aus dem Grundtakt folgt KEINE Prognose -- er ist")
    print("in A060 ausdruecklich als Strukturaussage gebucht.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
