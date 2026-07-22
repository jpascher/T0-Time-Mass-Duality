#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a080_verhaeltnis_invarianz.py -- Pruefskript zu A080.
Behauptung: dimensionslose Verhaeltnisse sind unabhaengig von der gewaehlten
Bruecken- und Korrekturkonstante; Absolutwerte sind es nicht.
Standardbibliothek."""
from fractions import Fraction

XI = Fraction(4, 30000)
KFRAK = 1 - 100 * XI          # 74/75

# rein geometrische, dimensionslose Strukturzahlen (Beispielwerte)
STRUKTUR = {"m_1": Fraction(1), "m_2": Fraction(207), "m_3": Fraction(3477)}


def absolut(bruecke, kfrak):
    return {k: float(v) * bruecke * float(kfrak) for k, v in STRUKTUR.items()}


def main():
    ok = True
    print("Strukturzahlen (dimensionslos): %s"
          % {k: str(v) for k, v in STRUKTUR.items()})

    faelle = [("E0 = 7,398 MeV, K_frak = 74/75", 7.398, KFRAK),
              ("E0 = 7,348 MeV, K_frak = 74/75", 7.348, KFRAK),
              ("E0 = 1,000 MeV, K_frak = 1    ", 1.000, Fraction(1)),
              ("E0 = 42,00 MeV, K_frak = 1/2  ", 42.00, Fraction(1, 2))]

    print("\n%-34s %14s %14s" % ("Fall", "m_2 absolut", "m_2/m_1"))
    print("-" * 66)
    ref = None
    for name, b, kf in faelle:
        a = absolut(b, kf)
        verh = a["m_2"] / a["m_1"]
        if ref is None:
            ref = verh
        else:
            if abs(verh - ref) / ref > 1e-14:
                ok = False
        print("%-34s %14.6f %14.10f" % (name, a["m_2"], verh))

    print("\nPRUEFUNG 1  Verhaeltnis invariant ueber alle Faelle :",
          "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    spanne = max(absolut(b, kf)["m_2"] for _, b, kf in faelle) / \
             min(absolut(b, kf)["m_2"] for _, b, kf in faelle)
    print("PRUEFUNG 2  Absolutwert NICHT invariant (Spanne %.1f-fach) : %s"
          % (spanne, "BESTANDEN" if spanne > 1.1 else "FEHLGESCHLAGEN"))

    print("\nSCHLUSS: K_frak und die Brueckenkonstante kuerzen sich in jedem")
    print("Verhaeltnis heraus. Eine Abweichung in einem VERHAELTNIS kann daher")
    print("nicht auf die Umrechnung geschoben werden -- sie sitzt im")
    print("geometrischen Kern. Das ist die Diagnoseregel aus A080.")
    return 0 if (ok and spanne > 1.1) else 1


if __name__ == "__main__":
    raise SystemExit(main())
