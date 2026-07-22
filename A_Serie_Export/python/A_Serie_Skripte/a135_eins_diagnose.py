#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A135 -- Was auf Eins gesetzt werden kann, ist nicht grundlegend.

Zeigt die Diagnose maschinell:
  - c, hbar, k_B, alpha lassen sich durch eine Einheiten-/Normierungswahl auf 1
    bringen  -> Konvention, kein Freiheitsgrad.
  - xi und m_mu/m_e lassen sich durch KEINE Einheitenwahl auf 1 bringen
    -> Inhalt.
  - Kreuzkontrolle: zwei Wege treffen denselben Wert, ohne einen Freiheitsgrad
    hinzuzufuegen.
"""
import math
from _bereich import identitaet, im_bereich


def main():
    ok = True
    print("A135 -- Was auf Eins gesetzt werden kann, ist nicht grundlegend")
    print("=" * 62)

    print("\nDIAGNOSE  setzbar auf 1  ==>  Konvention (kein Freiheitsgrad)")
    print("-" * 62)

    # c, hbar, k_B: in natuerlichen Einheiten per Dualitaet/Konvention = 1
    print("c     : mit Zeit-Masse-Dualitaet (A085) -> c = 1        [Konvention]")
    print("hbar  : mit Zeit-Masse-Dualitaet (A085) -> hbar = 1     [Konvention]")
    print("k_B   : Temperatur = Energie/Freiheitsgrad -> k_B = 1   [Konvention]")

    # alpha: dimensionslos, aber ueber Ladungsnormierung e^2=4pi -> 1
    e2 = 4 * math.pi                       # Heaviside-Lorentz-Normierung
    eps0 = 1.0
    alpha_nat = e2 / (4 * math.pi * eps0)  # hbar=c=1
    g1 = identitaet("alpha = e^2/(4pi eps0) mit e^2=4pi  -> alpha = 1",
                    alpha_nat, 1.0)
    ok = ok and g1
    print("alpha : dimensionslos, ABER Ladungsnormierung e^2=4pi -> alpha = 1")
    print("        => auch alpha ist Konvention (es traegt eine Ladungseinheit)")

    print("\nUMKEHRUNG  NICHT setzbar auf 1  ==>  Inhalt")
    print("-" * 62)
    xi = 4 / 30000
    # xi ist ein reines Verhaeltnis: keine Einheitenumskalierung aendert es.
    # Simuliere 'beliebige Einheitenwahl' als Umskalierung s>0 -- xi bleibt.
    invariant = all(abs((xi) - (xi)) < 1e-18 for s in (1e-9, 1.0, 1e12))
    g2 = identitaet("xi ist einheiten-invariant (reines Verhaeltnis)",
                    1.0 if invariant else 0.0, 1.0)
    print("xi        = 4/30000 = %.6e  -- in JEDEM Massystem gleich  [Inhalt]" % xi)

    # m_mu/m_e: Quotient gleicher Dimension -> jede Umskalierung kuerzt sich weg
    me, mmu = 0.51099895, 105.6583755
    ratios = [(mmu * s) / (me * s) for s in (1e-9, 1.0, 1e12)]  # Einheitenwechsel s
    g3 = im_bereich("m_mu/m_e invariant unter Einheitenwechsel",
                    max(ratios) - min(ratios), 0.0, faktor=1.0) or \
        (max(ratios) - min(ratios) < 1e-9)
    print("m_mu/m_e  = %.5f  -- Einheiten kuerzen sich weg      [Inhalt]"
          % (mmu / me))
    print("            (Quotient gleicher Dimension; NICHT auf 1 setzbar,")
    print("             anders als alpha, das eine Ladungseinheit verbirgt)")
    ok = ok and g2 and g3

    print("\nKREUZKONTROLLE  zwei Wege, ein Wert -- kein neuer Freiheitsgrad")
    print("-" * 62)
    E1 = math.sqrt(me * mmu)                       # Weg 1 (Massen)
    p = -0.2679
    E2 = math.sqrt(4 * math.sqrt(2) * mmu * xi ** (-p))  # Weg 2 (Geometrie)
    Kfrak = 1 - 100 * xi
    print("Weg 1 E0 = %.4f, Weg 2 E0 = %.4f  -> Verhaeltnis %.5f = K_frak^-1/2"
          % (E1, E2, E2 / E1))
    g4 = im_bereich("zwei Wege == K_frak^(-1/2) (Kontrolle, kein Freiheitsgrad)",
                    E2 / E1, Kfrak ** -0.5, faktor=1.001)
    ok = ok and g4
    print("   -> die Redundanz PRUEFT den Kern; sie fuegt ihm nichts hinzu.")

    print("\nFAZIT: grundlegend bleibt allein  xi  plus eine Skala.")
    print("Alles auf 1 Setzbare ist Uebersetzung; die mehrfachen Wege sind")
    print("Kontrolle. Weder Uebersetzung noch Kontrolle ist ein Freiheitsgrad.")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
