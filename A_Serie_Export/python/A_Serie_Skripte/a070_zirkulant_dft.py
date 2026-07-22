#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a070_zirkulant_dft.py -- Pruefskript zu A070.
Behauptung: ein Z_3-Zirkulant wird von der DFT diagonalisiert; die Eigenwerte
sind die Fourier-Koeffizienten der ersten Zeile. Standardbibliothek (cmath)."""
import cmath

W = cmath.exp(2j * cmath.pi / 3)


def zirkulant(c):
    return [[c[(j - i) % 3] for j in range(3)] for i in range(3)]


def dft_eigenwerte(c):
    return [sum(c[k] * W ** (k * n) for k in range(3)) for n in range(3)]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def main():
    print("[A220: Dieses Skript verifiziert mathematische Identitaeten /"
          " Bereiche. Die Theorie berechnet nichts -- gepruefte"
          " Gleichheit ist Algebra-Kontrolle, kein exaktes Ergebnis.]")
    ok = True
    faelle = [(1.0, 0.3, 0.3), (2.0, -0.5, 0.25), (0.0, 1.0, 1.0)]
    print("%-22s %-34s %10s" % ("erste Zeile c", "DFT-Eigenwerte", "max Rest")) 
    for c in faelle:
        M = zirkulant(c)
        ew = dft_eigenwerte(c)
        # Probe: det(M - lambda I) = 0 fuer jeden DFT-Eigenwert
        reste = []
        for lam in ew:
            A = [[M[i][j] - (lam if i == j else 0) for j in range(3)]
                 for i in range(3)]
            reste.append(abs(det3(A)))
        rest = max(reste)
        gut = rest < 1e-12
        ok = ok and gut
        print("%-22s %-34s %10.2e" %
              (str(c), ", ".join("%.4f" % e.real if abs(e.imag) < 1e-12
                                 else "%.3f%+.3fi" % (e.real, e.imag)
                                 for e in ew), rest))
    print("\nPRUEFUNG  DFT-Werte sind Eigenwerte (det(M-lambda I)=0) :",
          "BESTANDEN" if ok else "FEHLGESCHLAGEN")

    print("\nWAS DAS ZEIGT: kein charakteristisches Polynom noetig, die")
    print("Eigenwerte sind direkt die Fourier-Koeffizienten der ersten Zeile.")
    print("WAS ES NICHT ZEIGT: dass diese Eigenwerte die Teilchenmassen sind.")
    print("Die Diagonalisierung ist eine Uebersetzung, keine Begruendung")
    print("(A070, Abschnitt 'Was die Uebersetzung nicht leistet').")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
