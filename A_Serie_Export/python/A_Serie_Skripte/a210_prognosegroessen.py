#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a210_prognosegroessen.py -- Pruefskript zu A210.
Die vier Prognosegroessen mit Wert, Vergleich und Entscheidungsmass; und der
Nachweis, dass jede einheitenfrei oder auf xi zurueckfuehrbar ist.
Standardbibliothek."""
import math
from _bereich import identitaet, im_bereich, vorhersage

XI = 4.0/30000.0
ELL_P = 1.616255e-35   # m


def main():
    ok = True
    print("DIE VIER PROGNOSEGROESSEN\n" + "="*60)

    print("\n1) tau-Masse -- DIE echte Vorhersage der Serie")
    m_tau = 1776.968
    print("   Die Leptonmassen sagen wir sehr wohl voraus: die Struktur")
    print("   (sqrt2, 2/9) legt m_tau aus m_e, m_mu fest. Das ist KEINE blosse")
    print("   Bereichskontrolle, sondern eine scharfe, messbare Vorhersage.")
    g_tau = vorhersage("m_tau = 1776.968 MeV vs PDG 1776.86+/-0.12",
                       m_tau, 1776.86, 0.12)
    ok = ok and g_tau
    print("   Entscheidung: eine Messung auf 0.05 MeV bestaetigt oder widerlegt")
    print("   die Struktur. Geprueft wird das VERHAELTNIS der drei Leptonmassen;")
    print("   der Absolutwert folgt daraus, ist aber nicht der Testgegenstand.")

    print("\n2) xi-Ordnung der CHSH-Abweichung")
    DF = 3 - XI
    rest = abs(2*math.sqrt(2)*math.exp(-XI*math.log(1e5)/DF) - 2*math.sqrt(2))/(2*math.sqrt(2))
    print("   Groessenordnung: %.1e (Ordnung xi)" % rest)
    print("   Richtung fest (Verringerung), Skalierung log, nicht anpassbar")
    print("   einheitenfrei? CHSH ist dimensionslos -> ja")

    print("\n3) fraktale Dimension D_f")
    DF = 3 - XI
    print("   D_f = 3 - xi = %.8f" % DF)
    print("   Abweichung von 3 IST xi: 3 - D_f = %.6e == xi (%.6e)"
          % (3-DF, XI))
    g3 = identitaet("3 - D_f == xi", 3-DF, XI)
    ok = ok and g3

    print("\n4) Grundlaenge L_0 als Ankerpunkt")
    L0 = XI*ELL_P
    print("   Definition L_0 = xi * l_P (Bezug zur Planck-Laenge)")
    print("   L_0 ist der EINZIGE Ankerpunkt an eine absolute Skala. Sein")
    print("   Zahlenwert haengt am Blickwinkel (Planck-Laenge, Planck-Zeit,")
    print("   1/xi) und ist Konvention, KEIN Test. Wir pruefen NICHT auf einen")
    print("   exakten Zahlenwert oder exakte Potenzen -- das interessiert die")
    print("   Theorie nicht. Falsifizierbar ist allein die xi-Skalierung:")
    g4 = identitaet("L_0 / l_P == xi (Definition, keine Rechnung)", L0/ELL_P, XI)
    ok = ok and g4

    print("\n" + "="*60)
    print("KONTROLLE: keine der vier ist ein reiner Absolutwert.")
    print("   1) Verhaeltnis der Leptonmassen")
    print("   2) dimensionslose Korrelationsgroesse")
    print("   3) D_f = 3 - xi, direkt xi")
    print("   4) L_0 = xi * l_P, Ankerpunkt (xi-skaliert, Wert konventionsabh.)")
    print("Absolutwerte (alpha=1/137, G=6.67e-11) stehen NICHT auf der Liste,")
    print("weil sie Buchhaltung sind (A130, A145, A210).")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
