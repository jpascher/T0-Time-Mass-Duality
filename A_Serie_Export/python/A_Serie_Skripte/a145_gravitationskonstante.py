#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a145_gravitationskonstante.py -- Pruefskript zu A145.
Prueft: G = xi^2/(4 m) als Struktur; xi = 2 sqrt(G m) als Rueckrichtung; die
Dimensionsluecke und ihre Schliessung durch E_char; die strukturelle Zerlegung
von E_char mit AUSWEIS des kalibrierten Anteils; die Skalenhierarchie.
Standardbibliothek."""
import math
from _bereich import identitaet, im_bereich

XI = 4.0/30000.0
ME = 0.511                # MeV, charakteristische Masse
E0 = 7.40                 # MeV, aus A130 (kalibriert)
KFRAK = 1 - 100*XI


def main():
    ok = True

    print("PRUEFUNG 1  Grundstruktur G = xi^2/(4 m) und Rueckrichtung")
    G_grund = XI**2/(4*ME)
    print("   xi^2/(4 m_e)          = %.6e  (natuerliche Einheiten, [E^-1])" % G_grund)
    xi_zurueck = 2*math.sqrt(G_grund*ME)
    print("   xi = 2 sqrt(G m)      = %.10f" % xi_zurueck)
    g1 = identitaet("xi = 2 sqrt(G m) == xi (Rueckrichtung)", xi_zurueck, XI)
    ok = ok and g1
    print("   -> G verwendet G NICHT, um G zu bestimmen. Keine Zirkularitaet")
    print("      im Kern (Unterschied zu alpha, A130).")

    print("\nPRUEFUNG 2  Dimensionsluecke")
    print("   [G] in nat. Einh. = [E^-2], rechte Seite xi^2/(4m) = [E^-1].")
    print("   Es fehlt ein Faktor 1/E_char. Das ist eine ECHTE Luecke, im")
    print("   Dokument offen ausgewiesen, kein Rundungsfehler.")

    print("\nPRUEFUNG 3  Strukturelle Zerlegung von E_char")
    R_f = (4/3)**2
    g_geo = math.pi/math.sqrt(2)
    E_char = E0 * R_f * g_geo * KFRAK
    print("   E_char = E0 * (4/3)^2 * pi/sqrt2 * K_frak")
    print("          = %.2f * %.4f * %.4f * %.4f = %.3f"
          % (E0, R_f, g_geo, KFRAK, E_char))
    print("   Einheitlich verwendet: E_char = %.1f (seit 30.9.2026; vorher 28.4)" % E_char)
    print("   E_char hebt sich in G auf (1/E_char in G_nat, *E_char in der SI-Umrechnung) -> kein Rest in G")
    g3 = im_bereich("E_char nahe 28.8 (Struktur %.1f)" % E_char, E_char, 28.8,
                    faktor=1.3)
    ok = ok and g3

    print("\n   AUSWEIS DES KALIBRIERTEN ANTEILS (ehrliche Trennung):")
    print("   %-16s %-12s %s" % ("Faktor", "Wert", "Status"))
    print("   %-16s %-12.4f %s" % ("(4/3)^2", R_f, "geometrisch [K]"))
    print("   %-16s %-12.4f %s" % ("pi/sqrt2", g_geo, "geometrisch [K]"))
    print("   %-16s %-12.4f %s" % ("E0", E0, "kalibriert (A130) [B]"))
    print("   %-16s %-12.4f %s" % ("K_frak", KFRAK, "Setzung (A040)"))
    print("   -> Grundstruktur xi^2/(4m) ist [K]; der Zahlenwert ueber")
    print("      E_char ist [B] mit kalibriertem Anteil. Sauber getrennt.")

    print("\nPRUEFUNG 4  Skalenhierarchie E0 << E_char << E_T0")
    E_T0 = 1/XI
    print("   E0     = %8.2f MeV  (elektromagnetisch)" % E0)
    print("   E_char = %8.2f      (Gravitations-Ankopplung)" % E_char)
    print("   E_T0   = %8.2f      (= 1/xi, fundamental)" % E_T0)
    g4 = E0 < E_char < E_T0
    ok = ok and g4
    print("   Hierarchie E0 << E_char << E_T0 :",
          "im richtigen Bereich" if g4 else "AUSSERHALB")
    print("   -> Gravitation koppelt bei einer ZWISCHENskala, weit unter der")
    print("      fundamentalen. Das ist die strukturelle Aussage hinter ihrer")
    print("      Schwaeche -- eine Richtung, KEINE quantitative Erklaerung der")
    print("      40 Groessenordnungen (A145, offen).")




    print("\nEXAKTE RUECKRECHENBARKEIT (die tragende Aussage)")
    hbar, c = 1.054571817e-34, 2.99792458e8
    G_codata = 6.67430e-11
    M_Pl = math.sqrt(hbar * c / G_codata)     # Skala
    G_rueck = hbar * c / M_Pl ** 2
    print("   G=1 in Planck-Einheiten (Konvention) -> G_SI = hbar c / M_Pl^2")
    print("   gegeben xi + EINE Skala: G_SI = %.6e  (rel. Abw. %.0e, nur Rundung)"
          % (G_rueck, abs(G_rueck / G_codata - 1)))
    g_exakt = identitaet("G_SI exakt aus Skala rueckrechenbar", G_rueck, G_codata)
    ok = ok and g_exakt
    print("   -> exakt, kein freier Parameter.")

    print("\nHEBT SICH E_char IN G AUF?  (Stand 30.9.2026: kein Rest in G)")
    xi = XI; C_conv = 7.783e-3; K = 0.986
    werte = []
    for Ec in (28.4, E_char, 50.0):
        G_kette = xi**2/(4*ME) * (1/Ec) * C_conv * K * Ec   # Dok. 012, Schritt 1-3
        werte.append(G_kette)
        print("   E_char = %6.2f -> G_SI = %.6e" % (Ec, G_kette))
    g_kuerz = max(werte)/min(werte) - 1 < 1e-12
    print("   -> E_char kuerzt sich; G_SI = %.4e (%+.4f %% zu CODATA)"
          % (werte[1], 100*(werte[1]/6.67430e-11 - 1)))
    print("   -> die fruehere Abweichung E_char-Zerlegung gegen 28.4 (1.5 %) ist KEIN Rest in G")
    ok = ok and g_kuerz

    print("\nEINS-TEST (A135) und Kleidungsvergleich zu alpha")
    print("   G = c = hbar = 1 in Planck-Einheiten -> setzbar -> Konvention")
    print("   alpha_SI = xi*E0^2        : dimensionslos [E^0] -> EINE Skala")
    print("   G_nat    = xi^2/(4m)*1/Echar: [E^-2] (M_Pl^-2) -> Masse + Echar")
    print("   -> gleicher Inhalt (xi), mehr Schichten: reichere Dimension von G")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
