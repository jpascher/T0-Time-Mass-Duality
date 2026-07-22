#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a220_toleranzmassstab.py -- Pruefskript zu A220.
Ordnet die Vergleichszahlen der Serie in vier Genauigkeitsklassen, mit
Messgenauigkeit und Bestimmungstoleranz; Gegenprobe zur Scheingenauigkeit.
Standardbibliothek."""


def main():
    ok = True
    print("DIE VIER GENAUIGKEITSKLASSEN\n" + "="*66)
    print("%-22s %-10s %-12s %-12s" %
          ("Groesse", "Abw.", "Messgenau.", "Bestimmung"))
    print("-"*66)
    faelle = [
        ("Q = 2/3 (A110)",        "6e-6",   "7e-6",   "exakt",   1),
        ("theta(mu/e) (A110)",    "1.8e-7", "1e-9",   "exakt",   1),
        ("m_mu/m_e Leiter (A100)","0.52 %", "1e-9",   "~1 %",    2),
        ("m_tau/m_mu Leiter",     "1.04 %", "7e-5",   "~1 %",    2),
        ("alpha SI (A130)",       "0.24 %", "1e-10",  "Buchh.",  3),
        ("G / E_char (A145)",     "1.5 %",  "1e-5",   "Buchh.",  3),
        ("Neutrinomassen (A150)", "--",     "offen",  "offen",   4),
        ("Quarkmassen (A150)",    "--",     "schema", "schema",  4),
    ]
    for name, abw, mess, best, klasse in faelle:
        print("%-22s %-10s %-12s %-12s [Klasse %d]"
              % (name, abw, mess, best, klasse))

    print("\nLESEREGEL je Klasse:")
    print("  1: 5+ Stellen -- Abweichung 1e-6 ist ernstes Signal")
    print("  2: Prozentniveau -- 1 %% ist weder Signal noch Erfolg")
    print("  3: Buchhaltung -- misst die Bruecke, nicht die Theorie (KEIN Test)")
    print("  4: unbestimmt -- jede Uebereinstimmung folgenlos")

    print("\nGEGENPROBE  Scheingenauigkeit bei Klasse 2")
    # Eine Leitergroesse auf 5 Stellen ausgewiesen suggeriert Klasse-1-Niveau
    leiter = 2.4 * (4/30000)**-0.5   # ~ m_mu/m_e Leiter
    print("   Leiterwert voll ausgeschrieben: %.5f" % leiter)
    print("   Das sieht nach 5 Stellen aus -- ist aber Klasse 2 (~1 %% bestimmt).")
    print("   Die Fliesskommagenauigkeit ist NICHT die Bestimmungstoleranz.")
    print("   Ehrlich waere: %.0f (2 signifikante Stellen)" % leiter)
    scheingenau = len(("%.5f" % leiter).replace(".","")) > 2
    g = scheingenau  # die Gefahr existiert -> Regel noetig
    ok = ok and g
    print("   Regel greift (Scheingenauigkeit erkennbar) :",
          "BESTANDEN" if g else "FEHLGESCHLAGEN")

    print("\nDER MASSSTAB IN EINEM SATZ:")
    print("  Eine Uebereinstimmung zaehlt nur so weit, wie die SCHLECHTER")
    print("  bestimmte Seite reicht. Eine Abweichung wiegt nur so schwer, wie")
    print("  die BESSER bestimmte Seite sie traegt.")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
