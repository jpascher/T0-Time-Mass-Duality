#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a080_vier_kleidungen.py -- Pruefskript zu A080.
Behauptung: m0*c^2 = E0 = kB*T0 = hbar/T~ ist eine EXAKTE Identitaet; die
relative Abweichung ist Null bis auf Rundung. Standardbibliothek."""
C = 299792458.0
HBAR = 1.054571817e-34
KB = 1.380649e-23
EV = 1.602176634e-19

E0_MEV = 7.398          # geometrischer Weg (A130), hier nur als Zahlenanker


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    E0 = E0_MEV * 1e6 * EV          # Joule
    m0 = E0 / C ** 2                # kg
    T0 = E0 / KB                    # Kelvin
    Ttilde = HBAR / E0              # Sekunden

    print("Ausgangsgroesse  E0 = %.6f MeV = %.6e J\n" % (E0_MEV, E0))
    print("%-28s %18s" % ("Kleidung", "Wert"))
    print("-" * 48)
    print("%-28s %18.6e kg" % ("Masse    m0 = E0/c^2", m0))
    print("%-28s %18.6e K" % ("Temperatur T0 = E0/kB", T0))
    print("%-28s %18.6e s" % ("Zeit     T~ = hbar/E0", Ttilde))

    kandidaten = {
        "m0*c^2   ": m0 * C ** 2,
        "kB*T0    ": KB * T0,
        "hbar/T~  ": HBAR / Ttilde,
    }
    print("\nRueckrechnung auf E0:")
    ok = True
    for name, wert in kandidaten.items():
        rel = abs(wert - E0) / E0
        gut = rel < 1e-14
        ok = ok and gut
        print("   %s = %.10e J   rel. Abw. %.2e   %s"
              % (name, wert, rel, "ok" if gut else "FEHLER"))

    print("\nPRUEFUNG  Identitaet exakt (rel. Abw. < 1e-14) :",
          "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    print("\nSCHLUSS: die Umrechnung selbst traegt KEINE Abweichung. Wer eine")
    print("Diskrepanz zwischen Theorie und Messung findet, kann sie nicht hier")
    print("verorten. Sie sitzt entweder im geometrischen Kern oder in der")
    print("Verkleidungsschicht -- diese Diagnose ist der Zweck von A080.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
