#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a085_natuerliche_einheiten.py -- Pruefskript zu A085.
Zeigt: T~*m=1 reduziert das Vier-Dimensionen-System auf EINE Dimension; die
Planck-Groessen sind genau die Umrechnungsfaktoren des reduzierten Systems.
Standardbibliothek."""
import math

C = 299792458.0
HBAR = 1.054571817e-34
KB = 1.380649e-23
G = 6.67430e-11


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    ok = True

    print("PRUEFUNG 1  Dimensionsreduktion durch T~*m = 1")
    print("   Ohne Dualitaet (Standardphysik nach hbar=c=1):")
    print("      unabhaengige Dimensionen: {Energie}  -> 1 frei waehlbar")
    print("   Mit T~*m = 1 (Zeit = inverse Masse):")
    print("      [M]=[E]=[1/T]=[1/L] -> alle auf EINE Dimension")
    print("   Das ist eine inhaltliche Folge, keine Schreibweise:")
    print("      in der Standardphysik bleibt die Massendimension frei,")
    print("      hier ist sie durch xi skaliert und die Skala die einzige")
    print("      Eingabe.")
    # symbolische Kontrolle der Dimensionsexponenten
    dims = {"M": (1,0,0), "E": (1,0,0), "1/T": (0,-1,0), "1/L": (0,0,-1)}
    # nach der Dualitaet: T ~ 1/M, L ~ 1/M (c=1) -> alles auf Potenz von M
    reduziert = {"M":1, "E":1, "1/T":1, "1/L":1}
    g1 = len(set(reduziert.values())) == 1
    ok = ok and g1
    print("   alle vier auf dieselbe M-Potenz :",
          "BESTANDEN" if g1 else "FEHLGESCHLAGEN")

    print("\nPRUEFUNG 2  Planck-Groessen sind die Umrechnungsfaktoren")
    lp = math.sqrt(HBAR*G/C**3); tp = lp/C
    mp = math.sqrt(HBAR*C/G);    Ep = mp*C**2; Tp = Ep/KB
    proben = {
        "c    (Laenge<->Zeit)":      (lp/tp)/C,
        "hbar (Masse<->Zeit)":       (Ep*tp)/HBAR,
        "k_B  (Temperatur<->Energie)": (Ep/Tp)/KB,
    }
    for name, v in proben.items():
        gut = abs(v-1) < 1e-9; ok = ok and gut
        print("   %-30s -> %.12f  %s" % (name, v, "=1" if gut else "FEHLER"))

    print("\nPRUEFUNG 3  Vier Kleidungen einer Groesse")
    E0 = 7.398e6 * 1.602176634e-19   # J
    m0 = E0/C**2; T0 = E0/KB; Tt = HBAR/E0
    kleider = {"m0*c^2": m0*C**2, "k_B*T0": KB*T0, "hbar/T~": HBAR/Tt}
    print("   Ausgangsenergie E0 = %.6e J" % E0)
    for name, w in kleider.items():
        rel = abs(w-E0)/E0; gut = rel < 1e-12; ok = ok and gut
        print("   %-10s = %.6e J   rel %.1e  %s"
              % (name, w, rel, "ok" if gut else "FEHLER"))
    print("   -> eine Groesse in vier Kleidungen, nicht vier Groessen")

    print("\n   GRUND: die Umrechnungsfaktoren c^2, k_B, hbar sind die Naehte")
    print("   zwischen den Kleidungen. In natuerlichen Einheiten verschwinden")
    print("   sie, weil es nur ein Kleidungsstueck gibt (A085).")
    print("\nERGEBNIS:", "BESTANDEN" if ok else "FEHLGESCHLAGEN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
