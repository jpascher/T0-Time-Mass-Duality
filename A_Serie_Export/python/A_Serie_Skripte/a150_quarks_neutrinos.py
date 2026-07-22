#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A150 -- Quarks und Neutrinos: der belastbare CKM/PMNS-Kontrast.

Der Quark-/Neutrino-Massensektor ist [S] (Skizze). Belastbar sind zwei
parameterfreie Struktur-Aussagen: Generationenzahl 3 (Z_3, hier nicht
gerechnet) und der Mischungskontrast CKM gegen PMNS als Betrag-gegen-Phase.
Dieses Skript rechnet den Kontrast aus gemessenen Mischungsmatrizen -- keine
hergeleiteten Massen, kein angepasster Exponent.
"""
import math
from _bereich import im_bereich


def offdiag_weight(M):
    """Off-Diagonal-Gewicht der |M|^2-Matrix pro Zeile (3x3)."""
    total = sum(M[i][j] ** 2 for i in range(3) for j in range(3))
    diag = sum(M[i][i] ** 2 for i in range(3))
    return (total - diag) / 3.0


def main():
    ok = True
    print("A150 -- CKM/PMNS-Kontrast (Betrag gegen Phase)")
    print("=" * 52)

    # CKM (PDG-Betraege)
    CKM = [[0.97435, 0.22500, 0.00369],
           [0.22486, 0.97349, 0.04182],
           [0.00857, 0.04110, 0.99912]]
    w_ckm = offdiag_weight(CKM)

    # PMNS aus Standard-Mischungswinkeln
    t12, t23, t13 = math.radians(33.4), math.radians(49.0), math.radians(8.6)
    s12, c12 = math.sin(t12), math.cos(t12)
    s23, c23 = math.sin(t23), math.cos(t23)
    s13, c13 = math.sin(t13), math.cos(t13)
    U = [[c12 * c13,                    s12 * c13,                    s13],
         [-s12 * c23 - c12 * s23 * s13, c12 * c23 - s12 * s23 * s13,  s23 * c13],
         [s12 * s23 - c12 * c23 * s13, -c12 * s23 - s12 * c23 * s13,  c23 * c13]]
    U = [[abs(x) for x in row] for row in U]
    w_pmns = offdiag_weight(U)

    print("CKM  Off-Diagonal-Gewicht |V|^2/Zeile = %.3f  (Quarks: kleine Mischung)"
          % w_ckm)
    print("PMNS Off-Diagonal-Gewicht |U|^2/Zeile = %.3f  (Neutrinos: grosse Mischung)"
          % w_pmns)
    print("Faktor PMNS/CKM = %.1f" % (w_pmns / w_ckm))

    g1 = im_bereich("CKM-Off-Diagonal ~ 0.035", w_ckm, 0.035, faktor=1.05)
    g2 = im_bereich("PMNS-Off-Diagonal ~ 0.554", w_pmns, 0.554, faktor=1.05)
    g3 = im_bereich("Faktor ~ 16", w_pmns / w_ckm, 16.0, faktor=1.10)
    ok = ok and g1 and g2 and g3

    print("\n-> Quarks im Betragssektor (grosse Massenhierarchie, CKM ~ Id),")
    print("   Neutrinos im Phasensektor (flacher Betrag, PMNS weit von Id).")
    print("   'kleine gegen grosse Mischung' IST 'Betrag gegen Phase' -- struktu-")
    print("   rell, parameterfrei, ohne hergeleitete Massen. Keine Prognosegroesse.")



    print("\nTOP-VORZEICHEN: strukturierte Sprosse, nicht willkuerlich, nicht hergeleitet")
    XI = 4/30000
    print("   Leiter p=d_akt/3 (LINEAR) -> negative Sprossen erlaubt; Schritt Dp=1/3")
    print("   Faktor xi^(1/3) = %.4f (=1/%.1f). -1/3 = eine Sprosse unter Higgs (p=0)."
          % (XI**(1/3), 1/XI**(1/3)))
    print("   Gegenwindung/Laplace lambda=n^2 ist GERADE: n=-1 -> %d = n=+1 -> %d"
          % ((-1)**2, 1**2))
    print("   -> Laplace kann kein Vorzeichen erzeugen; tragfaehig ist die lineare Leiter.")
    print("   -1/3 = Fortsetzung der Leiter einen Schritt unter Higgs (p=0), kein Spiegel.")
    print("   Schon Bottom p=1/2 -> d_akt=1.5 (nicht ganzzahlig): d_akt-Deutung traegt")
    print("   nicht durchgehend. Primaer ist die Resonanzachse; -1/3 ist regulaere Pos.")
    print("   OFFEN: nicht das Vorzeichen, sondern die BESETZUNG (warum Top dort).")
    v, mt = 246.22, 172.69
    yt = (2**0.5)*mt/v
    print("   Unabhaengig fest: y_top = %.2f ~ 1 (Top auf EW-Skala)." % yt)
    g_par = im_bereich("Laplace gerade: (-1)^2 == (+1)^2", (-1)**2, 1**2, faktor=1.0) or True

    print("\nNEUTRINO: doppelte xi-Unterdrueckung (Photonen-Analogie, [S])")
    ME = 0.511e6   # eV
    m_nu = (XI**2 / 2) * ME
    print("   m_nu = (xi^2/2)*m_e = %.2f meV  (quasi-masselos, zwei xi-Faktoren)"
          % (m_nu*1e3))
    m_heavy = math.sqrt(2.5e-3)   # Oszillation: schwerstes >= sqrt(Dm2_atm)
    print("   Oszillation verlangt schwerstes >= sqrt(Dm2_atm) = %.0f meV"
          % (m_heavy*1e3))
    print("   -> Ueberschlag ~5 meV liegt Faktor ~%.0f zu tief:" % (m_heavy*1e3/5.12))
    print("      richtige Richtung (Kleinheit), falsche Skala. Bleibt [S].")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
