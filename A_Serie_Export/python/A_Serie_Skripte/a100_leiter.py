#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a100_leiter.py -- Pruefskript zu A100 (xi-Leiter im Leptonsektor).
Rechnet alle Zahlen des Dokuments nach: Leiterverhaeltnisse gegen PDG,
Reverse-xi, Brueckenkonstante je Lepton, und die FEHLGESCHLAGENE
K_frak-Gegenprobe. Standardbibliothek."""
from fractions import Fraction

XI = 4.0 / 30000.0
KFRAK = 1 - 100 * XI

ME, MMU, MTAU = 0.51099895069, 105.6583755, 1776.86     # MeV, PDG
V_HIGGS = 246.22                                        # GeV

LEITER = {"e": (Fraction(4, 3), Fraction(3, 2)),
          "mu": (Fraction(16, 5), Fraction(1)),
          "tau": (Fraction(25, 9), Fraction(2, 3))}


def main():
    ok = True
    print("xi = %.10e   K_frak = 1-100xi = %.6f (%.3f %%)"
          % (XI, KFRAK, 100 * (KFRAK - 1)))

    print("\nPRUEFUNG 1  Leiterverhaeltnisse gegen PDG")
    faelle = [("m_mu/m_e",   Fraction(12, 5),   -0.5,       MMU / ME),
              ("m_tau/m_mu", Fraction(125, 144), -1.0 / 3,  MTAU / MMU),
              ("m_tau/m_e",  Fraction(25, 12),  -5.0 / 6,   MTAU / ME)]
    soll = [(207.85, 206.77, 0.52), (16.992, 16.817, 1.04), (3532, 3477, 1.57)]
    print("   %-12s %10s %10s %10s %10s" % ("", "Leiter", "PDG", "Abw. %", "Doku"))
    for (name, r, p, pdg), (dl, dp, da) in zip(faelle, soll):
        wert = float(r) * XI ** p
        abw = 100 * (wert - pdg) / pdg
        stimmt = abs(abw - da) < 0.02
        ok = ok and stimmt
        print("   %-12s %10.4f %10.4f %+10.2f %10.2f  %s"
              % (name, wert, pdg, abw, da, "ok" if stimmt else "ABWEICHUNG"))
    print("   Dokumentwerte reproduziert :", "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 2  Reverse-xi: was die Daten zurueckgeben")
    print("   %-12s %14s %10s" % ("aus", "xi_zurueck", "Abw. %"))
    xis = []
    for name, r, p, pdg in faelle:
        xi_r = (pdg / float(r)) ** (1.0 / p)
        xis.append(xi_r)
        print("   %-12s %14.6e %+10.2f" % (name, xi_r, 100 * (xi_r - XI) / XI))
    streuung = 100 * (max(xis) - min(xis)) / (sum(xis) / 3)
    print("   Streuung der drei Werte untereinander: %.2f %%" % streuung)
    g2 = 1.0 < streuung < 3.0
    ok = ok and g2
    print("   kein einheitliches xi (Streuung ~2 %%) :",
          "BESTANDEN" if g2 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 3  Brueckenkonstante je Lepton")
    massen = {"e": ME, "mu": MMU, "tau": MTAU}
    print("   %-6s %14s %10s" % ("Lepton", "v_eff [GeV]", "Abw. %"))
    for k, (r, p) in LEITER.items():
        v = massen[k] / (float(r) * XI ** float(p)) / 1000.0
        print("   %-6s %14.2f %+10.2f" % (k, v, 100 * (v - V_HIGGS) / V_HIGGS))
    print("   -> Restabweichung wird in die Bruecke absorbiert (A080).")

    print("\nPRUEFUNG 4  K_frak-Gegenprobe -- ERWARTET WIRD FEHLSCHLAG")
    print("   Kandidaten fuer eine einzelne K_frak-Potenz:")
    for p in (0.5, 1.0, 1.5, 2.0):
        print("      K_frak^%.1f  ->  %+7.3f %%" % (p, 100 * (KFRAK ** p - 1)))
    print("   Gemessene Abweichungen: +0.52 %% und +1.04 %%")
    print("   Alle Kandidaten sind NEGATIV, die Messwerte POSITIV.")
    passt = any(abs(100 * (KFRAK ** p - 1) - 0.52) < 0.1 for p in
                (0.5, 1.0, 1.5, 2.0))
    g4 = not passt
    ok = ok and g4
    print("   Gegenprobe schlaegt fehl (wie im Dokument gebucht) :",
          "BESTANDEN" if g4 else "FEHLGESCHLAGEN")
    print("   -> Der naheliegende Erklaerungsversuch ist geprueft und")
    print("      gescheitert. Er wird NICHT durch einen freien Exponenten")
    print("      gerettet.")

    print("\nVERDOPPLUNG IST ARITHMETISCH ERZWUNGEN")
    a1 = 100 * (float(Fraction(12, 5)) * XI ** -0.5 - MMU / ME) / (MMU / ME)
    a2 = 100 * (float(Fraction(125, 144)) * XI ** (-1.0/3) - MTAU / MMU) / (MTAU / MMU)
    a3 = 100 * (float(Fraction(25, 12)) * XI ** (-5.0/6) - MTAU / ME) / (MTAU / ME)
    print("   Abw(mu/e)=%.3f%%  Abw(tau/mu)=%.3f%%  Abw(tau/e)=%.3f%%"
          % (a1, a2, a3))
    print("   Abw(tau/mu)/Abw(mu/e) = %.3f  (~2, Verdopplung)" % (a2/a1))
    print("   Abw(mu/e)+Abw(tau/mu) = %.3f  vs Abw(tau/e) = %.3f  -> additiv"
          % (a1+a2, a3))
    from _bereich import im_bereich
    gadd = im_bereich("log-Abweichungen addieren sich (nur eine unabhaengig)",
                      a1+a2, a3, faktor=1.02)
    ok = ok and gadd
    print("   Grund: entlang der Leiter m_tau/m_e=(m_tau/m_mu)(m_mu/m_e) addieren")
    print("   sich die log-Abweichungen. Nur EINE ist unabhaengig gemessen.")
    print("   WICHTIG: das gilt fuer JEDE multiplikative Korrektur, unabhaengig")
    print("   von deren Wert -- also KEIN Beleg fuer K_frak (den die Gegenprobe")
    print("   verwirft). Die Verdopplung zeichnet keine Korrektur aus.")
    print("   Der Leiterschritt N_0~39 (pro Generation) ist eine ANDERE Groesse")
    print("   als die feste RG-Skala 100 in K_frak (getrennt, R54); N_0 ist offen.")

    print("\nEXPONENTEN AUS WICKLUNGSZAHLEN (log-Torus, Schritt 1/3)")
    P = {"e": 1.5, "mu": 1.0, "tau": 2.0/3}
    print("   p: e=%.3f mu=%.3f tau=%.3f" % (P["e"], P["mu"], P["tau"]))
    print("   Stufen: p_e-p_mu=%.3f (geom. Mitte), p_mu-p_tau=%.3f (Terz 1/3)"
          % (P["e"]-P["mu"], P["mu"]-P["tau"]))
    print("   -> dieselbe Quelle wie r_i = n_phi^2/n_theta (A110): hergeleitet,")
    print("      nicht frei.")

    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
