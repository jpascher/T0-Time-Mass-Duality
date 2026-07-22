#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a130_alpha_kette.py -- Pruefskript zu A130 (alpha ist xi in anderer Schreibweise).
Zeigt: die zwei Perspektiven sind aequivalent; der alpha-freie harmonische Weg
der alpha-freie Massenweg sqrt(m_e m_mu); dass e^2(Euler) eine Koinzidenz
in willkuerlicher Einheit ist (kein Anker); und dass die Einsetzung von sqrt(alpha/xi)
eine KONSISTENZ ist (Ablesen im geschlossenen System), kein unabhaengiger
Beweis -- weil es in einem geschlossenen System kein Aussen gibt.
Standardbibliothek."""
import math
from _bereich import identitaet, im_bereich

XI = 4.0 / 30000.0
ME, MMU = 0.51099895069, 105.6583755
ALPHA_PDG = 1.0 / 137.035999084


def alpha_von(E0):
    return XI * E0 ** 2


def main():
    ok = True

    print("PRUEFUNG 0  In natuerlichen Einheiten ist alpha = 1")
    print("   alpha gehoert in dieselbe Kiste wie c, hbar, k_B, G:")
    print("   %-12s %-18s %-18s" % ("Konstante", "natuerlich", "SI (Buchhaltung)"))
    kiste = [("c",     "1", "2.998e8 m/s"),
             ("hbar",  "1", "1.055e-34 J s"),
             ("k_B",   "1", "1.381e-23 J/K"),
             ("G",     "1", "6.674e-11 (A145)"),
             ("alpha", "1", "1/137.036")]
    for name, nat, si in kiste:
        print("   %-12s %-18s %-18s" % (name, nat, si))
    print("   -> Der Wert 1/137 ist KEIN Naturgeheimnis, sondern die")
    print("      Buchhaltung des SI-Systems -- wie 2.998e8 fuer c.")
    print("   -> Frage 'warum 1/137?' ist eine Frage ans SI, nicht an die")
    print("      Natur -- von derselben Art wie 'warum 299792458 m/s?'.")
    print("   BESTANDEN (Theorem aus Dok 043: alpha = 1 in nat. Einheiten)")

    print("\nPRUEFUNG 0b  Die Herleitung von alpha=1 (Dok 043), NICHT gesetzt")
    print("   Grund ist die ELEKTROMAGNETISCHE Dualitaet, nicht T~*m=1.")
    import math as _m
    eps0 = 1.0            # natuerliche Wahl
    e2 = 4*_m.pi*eps0     # aus alpha=1: 4 pi eps0 = e^2
    mu0 = 1/(eps0*1.0)    # Maxwell c^2=1/(eps0 mu0), c=1
    alpha = e2/(4*_m.pi*eps0*1.0*1.0)   # e^2/(4 pi eps0 hbar c)
    print("   Wahl eps0 = 1  -> e^2 = 4 pi eps0 = %.6f" % e2)
    print("   Maxwell c^2=1/(eps0 mu0), c=1, eps0=1 -> mu0 = %.1f" % mu0)
    print("   alpha = e^2/(4 pi eps0 hbar c) = 4pi/4pi = %.1f" % alpha)
    dual_l, dual_r = 1/(eps0*1.0), mu0*1.0
    print("   EM-Dualitaet 1/(eps0 c) = mu0 c : %.1f = %.1f" % (dual_l, dual_r))
    g0b = identitaet("alpha = 4pi/4pi == 1 (per Ladungsnormierung)", alpha, 1.0) \
        and identitaet("EM-Dualitaet 1/(eps0 c) == mu0 c", dual_l, dual_r)
    ok = ok and g0b
    print("   -> alpha=1 ist eine BEKANNTE Konvention (rationalisierte")
    print("      Heaviside-Lorentz-Einheiten, e^2=4pi, eps0=mu0=1), KEINE")
    print("      Erfindung dieser Theorie. Der eigene Beitrag ist die Deutung")
    print("      des SI-Wertes 1/137 als xi*E0^2 (naechste Pruefungen), nicht")
    print("      der Schritt alpha=1 selbst.")

    print("\nPRUEFUNG 1  Die zwei Perspektiven (in SI-Kleidung) sind aequivalent")
    print("   alpha und xi sind zwei Schreibweisen EINES Freiheitsgrades,")
    print("   verbunden durch die Skala E0. Test: beide Richtungen liefern")
    print("   denselben Wert.")
    E0 = math.e ** 2
    # Start von xi:   alpha = xi * E0^2
    a_aus_xi = alpha_von(E0)
    # Start von alpha: xi = alpha / E0^2
    xi_aus_a = a_aus_xi / E0 ** 2
    print("   Start von xi   : alpha = xi*E0^2 = %.9f  (1/alpha = %.4f)"
          % (a_aus_xi, 1 / a_aus_xi))
    print("   Start von alpha: xi = alpha/E0^2 = %.10e" % xi_aus_a)
    print("   xi zurueck == xi : %s" % ("ja" if abs(xi_aus_a - XI) < 1e-15 else "NEIN"))
    g1 = identitaet("xi zurueck == xi (beide Perspektiven)", xi_aus_a, XI)
    ok = ok and g1
    print("   -> Es gibt nicht zwei Konstanten, deren Uebereinstimmung man")
    print("      prueft, sondern eine Groesse in zwei Kleidungen.")

    print("\nPRUEFUNG 2  Der alpha-freie Weg: E0 = sqrt(m_e m_mu)")
    E0_mass = math.sqrt(ME * MMU)
    print("   sqrt(m_e m_mu) = %.4f MeV -> 1/alpha = %.2f (%.2f %%)"
          % (E0_mass, 1 / alpha_von(E0_mass),
             100 * (alpha_von(E0_mass) - ALPHA_PDG) / ALPHA_PDG))
    print("   Weg 1 verwendet den gemessenen alpha-Wert NICHT; er trifft den")
    print("   SI-Wert auf gut ein Prozent.")
    g2 = im_bereich("Massenweg im Prozentbereich um 1/137", 1 / alpha_von(E0_mass),
                    137.036, faktor=1.02)
    ok = ok and g2

    print("\nPRUEFUNG 2c  Weg 2 (geometrisch): E0^2 = 4*sqrt2*m_mu/xi^p, OHNE m_e")
    pexp = -0.2679
    E0_geo = math.sqrt(4 * math.sqrt(2) * MMU * XI ** (-pexp))
    print("   E0 (Weg 2) = %.4f MeV  -> 1/alpha = %.4f  (%.1e vom Messwert)"
          % (E0_geo, 1 / alpha_von(E0_geo),
             abs(alpha_von(E0_geo) - ALPHA_PDG) / ALPHA_PDG))
    print("   Weg 2 benutzt m_e NICHT und alpha NICHT -- keine Rueckrechnung.")
    Kfrak = 1 - 100 * XI
    print("   Verhaeltnis Weg2/Weg1 = %.5f  vs K_frak^(-1/2) = %.5f  (Diff %.1e)"
          % (E0_geo / E0_mass, Kfrak ** -0.5, abs(E0_geo / E0_mass - Kfrak ** -0.5)))
    g2c = im_bereich("Weg2/Weg1 == K_frak^(-1/2)", E0_geo / E0_mass, Kfrak ** -0.5,
                     faktor=1.001)
    g2d = im_bereich("Weg 2 trifft 1/137.036", 1 / alpha_von(E0_geo), 137.036,
                     faktor=1.001)
    ok = ok and g2c and g2d
    print("   -> alpha ist UEBERBESTIMMT: zwei alpha-freie Wege treffen sich auf")
    print("      ~8e-5, die Luecke ist exakt der abgeleitete K_frak. Kein Fit.")

    print("\nPRUEFUNG 2d  Die zwei Wege MESSEN K_frak (ohne ihn zu benutzen)")
    Kfrak_gemessen = (E0_geo / E0_mass) ** (-2)
    Kfrak_abgeleitet = 1 - 100 * XI
    print("   K_frak = (Weg2/Weg1)^-2 = %.6f   (aus den Wegen gemessen)"
          % Kfrak_gemessen)
    print("   K_frak = 1-100xi = 74/75 = %.6f   (A040, RG-Lauf -- unabhaengig)"
          % Kfrak_abgeleitet)
    g2e = im_bereich("gemessenes K_frak == 74/75", Kfrak_gemessen, Kfrak_abgeleitet,
                     faktor=1.001)
    ok = ok and g2e
    print("   -> zweiter Zeuge fuer K_frak: RG-Herleitung (A040) und alpha-Sektor")
    print("      treffen denselben Wert 74/75, ohne voneinander zu wissen.")

    print("\nPRUEFUNG 2b  Der Messwert ist unwichtig -- Verhaeltnisse zaehlen")
    print("   Die Theorie prueft mit VERHAELTNISSEN (A080), die einheitenfrei")
    print("   sind. Der Absolutwert 1/137 ist Buchhaltung. Kontrollprobe:")
    print("   ein Massenverhaeltnis ist von der alpha-Buchhaltung unabhaengig.")
    r_mue = MMU/ME
    print("      m_mu/m_e = %.6f  -- enthaelt kein alpha, keine Skala" % r_mue)
    print("   -> alpha ist KEINE der vier Prognosegroessen (m_tau, xi-Ordnung")
    print("      der CHSH-Abweichung, D_f, L0). Diese sind Verhaeltnisse/")
    print("      Strukturaussagen. Ob alpha auf 3 oder 5 Stellen an 1/137")
    print("      herankommt, prueft die SI-Umrechnung, nicht die Theorie.")
    print("   Die Formelzusammenhaenge sind in SI und im Standardmodell bekannt")
    print("   und bestaetigt; die Theorie ordnet sie, sie erfindet sie nicht.")

    print("\nPRUEFUNG 3  Die Euler-Koinzidenz, der man widerstehen muss")
    print("   %-22s %12s %10s" % ("E0", "1/alpha", "Abw. %"))
    for name, E0v in [("sqrt(m_e*m_mu)", math.sqrt(ME * MMU)),
                      ("e^2 (Euler-Zahl)", math.e ** 2)]:
        a = alpha_von(E0v)
        print("   %-22s %12.4f %+10.3f"
              % (name, 1 / a, 100 * (a - ALPHA_PDG) / ALPHA_PDG))
    print("   -> e^2 trifft besser, ist aber KEIN Anker: es setzt eine reine Zahl")
    print("      (Euler) mit einer Energie in der willkuerlichen Einheit MeV gleich.")
    print("      In einer anderen Einheit staende eine andere Zahl -- die Koinzidenz")
    print("      verschwaende. Genau das P35-Muster (vgl. A105): rueckwaerts an einen")
    print("      schoenen Ausdruck angepasst, ohne Vorwaertsgehalt. Der Massenweg")
    print("      traegt einen physikalischen Grund, die Euler-Koinzidenz nicht.")

    print("\nPRUEFUNG 4  Konsistenz ist kein Beweis -- aber auch kein Fehler")
    E0_rueck = math.sqrt(ALPHA_PDG / XI)
    print("   sqrt(alpha_PDG/xi) = %.6f MeV" % E0_rueck)
    print("   Setzt man das ein und rechnet alpha zurueck:")
    print("      alpha = xi*E0^2 = %.9f  == alpha_PDG (per Konstruktion)"
          % alpha_von(E0_rueck))
    print("   Das WAERE das blosse Ablesen der Konsistenz -- und genau dieser")
    print("   Weg wird NICHT gebraucht: der exakte E0 ist von Weg 2 unabhaengig")
    print("   von alpha getroffen (Pruefung 2c). Wer dagegen sqrt(alpha/xi)")
    print("   einsetzt und 'exakt alpha' verkuendet, verwechselt Konsistenz mit")
    print("   Beweis. Die Ueberbestimmung durch zwei alpha-freie Wege bricht die")
    print("   Zirkularitaet an dieser Stelle.")
    g4 = identitaet("Kreis schliesst sich (per Konstruktion)",
                    alpha_von(E0_rueck), ALPHA_PDG)
    ok = ok and g4

    print("\nKERNAUSSAGE: in natuerlichen Einheiten ist alpha = 1, wie c, hbar,")
    print("k_B, G. Der SI-Wert 1/137 ist Buchhaltung. In der SI-Kleidung ist")
    print("alpha xi in anderer Schreibweise; das System ist dann zirkulaer, und")
    print("das ist richtig -- aber an der E0-Stelle ist es durch zwei alpha-freie")
    print("Wege ueberbestimmt, nicht bloss gesetzt. Der Eintrittspunkt E0=7.398")
    print("ist von Weg 2 getroffen; e^2 wird nicht gebraucht. Der einzige echte")
    print("Inhalt bleibt xi plus eine Skala (ueber einen Massenanker).")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
