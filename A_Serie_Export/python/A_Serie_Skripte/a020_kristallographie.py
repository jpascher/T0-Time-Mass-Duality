#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a020_kristallographie.py -- Pruefskript zu A020, Abschnitt "Zweite Setzung"

Aktualisiert am 1.10.2026: 4D-Kriterium (GL(4,Z)) ergaenzt; die
Fuenfzaehligkeit ist auf T^4 gittervertraeglich, die 2D-Restriktion
grenzt n=3 dort nicht ab (vgl. Dok. A020).

Behauptung im Text:
  In 2D/3D erlaubt die kristallographische Restriktion 2*cos(2*pi/n) in Z
  genau n in {1,2,3,4,6}. Auf T^4 (Gitter Z^4, Automorphismen GL(4,Z)) sind
  die Ordnungen {1,2,3,4,5,6,8,10,12} zulaessig, also auch n=5
  (Begleitmatrix von Phi_5, A_4-Gitter). Ausgeschlossen waere n=5 nur bei
  hyperkubischer Metrik (Punktgruppe B_4). Die Dreizaehligkeit ist zugelassen.

Das Skript prueft die Behauptung, statt sie zu illustrieren: es rechnet die
Bedingung fuer alle n bis n_max aus und meldet die Menge der Loesungen.
Reine Standardbibliothek, kein Zufall, kein Seed noetig.
"""
import itertools
import math

TOL = 1e-12
N_MAX = 100


def ist_ganzzahlig(x, tol=TOL):
    return abs(x - round(x)) < tol


def psi(n):
    """Kleinste Dimension, in der Z^d einen Automorphismus der Ordnung n hat."""
    if n in (1, 2):
        return 0
    f, m, p = {}, n, 2
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    s = sum((p - 1) * p ** (k - 1) for p, k in f.items())
    if f.get(2) == 1:
        s -= 1
    return s


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def det4(M):
    if len(M) == 1:
        return M[0][0]
    return sum((-1) ** j * M[0][j] * det4([r[:j] + r[j + 1:] for r in M[1:]])
               for j in range(len(M)))


def main():
    loesungen = []
    print("n    2*cos(2*pi/n)      ganzzahlig?")
    print("-" * 42)
    for n in range(1, N_MAX + 1):
        w = 2 * math.cos(2 * math.pi / n)
        ok = ist_ganzzahlig(w)
        if ok:
            loesungen.append(n)
        if n <= 12:
            print("%-4d %16.12f   %s" % (n, w, "ja" if ok else "nein"))

    print("\nLoesungsmenge 2D/3D bis n = %d: %s" % (N_MAX, loesungen))
    erwartet = [1, 2, 3, 4, 6]
    p1 = loesungen == erwartet
    print("\nPRUEFUNG 1  2D/3D: Loesungsmenge == {1,2,3,4,6} :",
          "BESTANDEN" if p1 else "FEHLGESCHLAGEN")

    # 4D: Ordnungen endlicher Elemente in GL(4,Z) sind genau die n mit psi(n) <= 4
    ord4 = [n for n in range(1, N_MAX + 1) if psi(n) <= 4]
    p2 = ord4 == [1, 2, 3, 4, 5, 6, 8, 10, 12]
    print("PRUEFUNG 2  4D: Ordnungen in GL(4,Z) == {1,2,3,4,5,6,8,10,12} :",
          "BESTANDEN" if p2 else "FEHLGESCHLAGEN", ord4)

    # explizit: Begleitmatrix von Phi_5 = x^4+x^3+x^2+x+1
    C = [[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]]
    I4 = [[int(i == j) for j in range(4)] for i in range(4)]
    P_ = I4
    potenzen = []
    for k in range(1, 6):
        P_ = matmul(P_, C)
        potenzen.append(P_ == I4)
    p3 = (det4(C) == 1 and potenzen == [False, False, False, False, True])
    print("PRUEFUNG 3  n=5 auf T^4 gitterv. (C ganzzahlig, det 1, C^5=I) :",
          "BESTANDEN" if p3 else "FEHLGESCHLAGEN")

    # hyperkubisches T^4: Punktgruppe B_4 (vorzeichenbehaftete Permutationen)
    ordB4 = set()
    anzahl = 0
    for perm in itertools.permutations(range(4)):
        for s in itertools.product((1, -1), repeat=4):
            M = [[s[i] if perm[i] == j else 0 for j in range(4)] for i in range(4)]
            anzahl += 1
            Q, k = M, 1
            while Q != I4:
                Q, k = matmul(Q, M), k + 1
            ordB4.add(k)
    p4 = anzahl == 384 and sorted(ordB4) == [1, 2, 3, 4, 6, 8]
    print("PRUEFUNG 4  hyperkubisch (B_4, 384 El.): Ordnungen ohne 5   :",
          "BESTANDEN" if p4 else "FEHLGESCHLAGEN", sorted(ordB4))

    drei = 2 * math.cos(2 * math.pi / 3)
    p5 = ist_ganzzahlig(drei) and 3 in ord4
    print("PRUEFUNG 5  n=3 zugelassen (2D und 4D)              :",
          "BESTANDEN" if p5 else "FEHLGESCHLAGEN")

    print("\nWAS DAS SKRIPT NICHT ZEIGT: warum von den erlaubten Werten")
    print("gerade n=3 realisiert ist. Auf T^4 grenzt die Gitterbedingung n=3")
    print("nicht gegen n=5 ab. Siehe A020, 'Was offen bleibt'.")
    alle = [p1, p2, p3, p4, p5]
    print("\nErgebnis: %d/%d bestanden" % (sum(alle), len(alle)))
    return 0 if all(alle) else 1

if __name__ == "__main__":
    raise SystemExit(main())
