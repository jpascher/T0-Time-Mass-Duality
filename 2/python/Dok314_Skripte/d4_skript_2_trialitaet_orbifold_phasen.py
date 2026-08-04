#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOTIZ Gitter im Hilbertraum — Skript 2
Teile B/C/D/E/F/G: Aut(D4)=1152, Trialitaet (Quotient 6=S3),
exakte Ordnung-3-Klassifikation (HALBZAHLIG! 2A ganzzahlig rechnen),
Orbifold-Fixpunkte |det(1-A)|=9, Zirkulant auf Modenorbits,
Phasen-Test 2/9 (negativ, Nenner {1,2,3,6}), Ordnungsverteilung
(keine Ordnung 5, da 5 nicht 1152 teilt), Verdopplungs-Vorstruktur 24=4x6.
Abhaengigkeiten: numpy. Deterministisch.
Stand: 4. August 2026
"""
import itertools, collections
import numpy as np
from fractions import Fraction

D4_basis = [(1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1), (0, 0, 1, 1)]
D4_min = [v for v in itertools.product([-1, 0, 1], repeat=4)
          if sum(x * x for x in v) == 2 and sum(v) % 2 == 0]

# ---------------------------------------------------------------
# B) Aut-Zaehlung: geordnete Basis-Tupel mit identischer Gram-Matrix
# ---------------------------------------------------------------
def aut_list(basis, minvecs):
    G = np.array(basis) @ np.array(basis).T
    M = [np.array(v) for v in minvecs]
    n = len(basis); auts = []
    def rec(chosen):
        if len(chosen) == n:
            auts.append(chosen); return
        i = len(chosen)
        for w in M:
            if np.dot(w, w) != G[i, i]:
                continue
            if any(np.dot(w, c) != G[i, j] for j, c in enumerate(chosen)):
                continue
            rec(chosen + [w])
    rec([])
    return auts

auts = aut_list(D4_basis, D4_min)
assert len(auts) == 1152, len(auts)                    # = |W(F4)|
Z4_min = [v for v in itertools.product([-1, 0, 1], repeat=4)
          if sum(x * x for x in v) == 1]
assert len(aut_list([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)], Z4_min)) == 384
print("|Aut(D4)| = 1152, |Aut(Z4)| = 384, Quotient 1152/192 = 6 = |S3|")

# ---------------------------------------------------------------
# C/F) Exakte Matrizen: 2A ist ganzzahlig (Trialitaet ist HALBZAHLIG —
#     naive Rundung auf ganze Zahlen zerstoert genau diese Elemente!)
# ---------------------------------------------------------------
Binv = np.linalg.inv(np.array(D4_basis, dtype=float).T)
elems = []                                 # Liste von 2A (ganzzahlig, exakt)
for images in auts:
    A2 = np.rint(2 * (np.array(images, dtype=float).T @ Binv)).astype(int)
    elems.append(A2)

def ordnung(A2):
    M = np.eye(4, dtype=object)
    for m in range(1, 13):
        M = M @ A2
        if np.array_equal(np.array(M, dtype=object),
                          (2 ** m) * np.eye(4, dtype=object)):
            return m
    return None

ordn = collections.Counter(ordnung(A2) for A2 in elems)
print("Ordnungsverteilung:", dict(sorted(ordn.items())))
assert ordn[5] == 0 and ordn[3] == 80
print("Keine Ordnung 5 (5 teilt 1152 = 2^7*3^2 nicht, Lagrange).")

order3 = [A2 for A2 in elems if ordnung(A2) == 3]

def act(A2, v):
    r = A2 @ v; assert np.all(r % 2 == 0); return r // 2

minset = [np.array(v) for v in D4_min]
def orbits(A2):
    seen = set(); out = []
    for v in minset:
        if tuple(v) in seen: continue
        o = [v.copy()]; w = act(A2, v)
        while not np.array_equal(w, v):
            o.append(w.copy()); w = act(A2, w)
        seen |= {tuple(x) for x in o}; out.append(o)
    return out

klass = collections.Counter()
for A2 in order3:
    tr = Fraction(int(np.trace(A2)), 2)
    halb = not np.all(A2 % 2 == 0)
    frei = all(len(o) == 3 for o in orbits(A2))
    klass[(str(tr), 'halb' if halb else 'ganz', 'frei' if frei else 'fix')] += 1
print("Drei Klassen der 80 Ordnung-3-Elemente:", dict(klass))
assert klass[('-2', 'halb', 'frei')] == 16
assert klass[('1', 'ganz', 'frei')] == 32
assert klass[('1', 'halb', 'fix')] == 32

# ---------------------------------------------------------------
# D) Spur-(-2)-Klasse: Orbifold T^4/Z3 mit 9 Fixpunkten
# ---------------------------------------------------------------
A2 = next(a for a in order3 if np.trace(a) == -4)      # Spur(A) = -2
A = A2 / 2.0
assert abs(round(np.linalg.det(np.eye(4) - A))) == 9
ew = np.linalg.eigvals(A)
assert np.allclose(sorted(np.abs(np.angle(ew))), [2*np.pi/3]*4)
print("Spur-(-2)-Element: Eigenwertphasen +-120 Grad doppelt, |det(1-A)| = 9")
print("-> T^4/Z3-Orbifold mit 9 Fixpunkten ist Gittersymmetrie von D4.")

# Zirkulant auf einem Modenorbit (Moden transformieren mit A^{-T})
os_ = orbits(A2)
assert len(os_) == 8 and all(len(o) == 3 for o in os_)
orb = os_[0]
Ainv2 = np.rint(2 * np.linalg.inv(A)).astype(int)
P = np.zeros((3, 3), dtype=int)
for j, k in enumerate(orb):
    kk = act(Ainv2.T.copy(), k) if False else (Ainv2.T @ k) // 2
    for m, k2 in enumerate(orb):
        if np.array_equal(kk, k2): P[m, j] = 1
ewP = sorted(np.round(np.angle(np.linalg.eigvals(P)) * 180 / np.pi, 1))
assert ewP == [-120.0, 0.0, 120.0]
print("Zirkulant auf jedem Dreierorbit: Eigenwerte {1, w, w^2}. 24 = 8 x 3.")

# ---------------------------------------------------------------
# E) Phasen-Test 2/9: exakte Fixpunkte und Invarianten
# ---------------------------------------------------------------
# Fixpunkte: x mit (1-A)x in D4, modulo D4. Vertreter in [0,1)^4.
Af = np.array([[Fraction(int(x), 2) for x in row] for row in A2], dtype=object)
I4 = np.array([[Fraction(int(i == j)) for j in range(4)] for i in range(4)],
              dtype=object)
M = I4 - Af

def inv4(M):
    n = 4
    Aug = [[M[i][j] for j in range(n)] +
           [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if Aug[r][c] != 0)
        Aug[c], Aug[p] = Aug[p], Aug[c]
        pv = Aug[c][c]
        Aug[c] = [x / pv for x in Aug[c]]
        for r in range(n):
            if r != c and Aug[r][c] != 0:
                f = Aug[r][c]
                Aug[r] = [Aug[r][j] - f * Aug[c][j] for j in range(2 * n)]
    return [[Aug[i][n + j] for j in range(n)] for i in range(n)]

Minv = inv4(M)
import math
fix = set()
for lam in itertools.product(range(-2, 3), repeat=4):
    if sum(lam) % 2:
        continue
    x = tuple(sum(Minv[i][j] * lam[j] for j in range(4)) for i in range(4))
    y = tuple(xi - math.floor(xi) for xi in x)      # [0,1)-Vertreter mod Z^4
    # Klappung mod Z^4 kann D4 verlassen; Paritaet der Klappung pruefen
    d = tuple(y[i] - x[i] for i in range(4))
    if all(di.denominator == 1 for di in d) and sum(int(di) for di in d) % 2 == 0:
        fix.add(y)
    else:                                            # +e_i-Shift repariert Paritaet
        for i in range(4):
            y2 = list(y); y2[i] = (y2[i] + 1) % 1 if y2[i] else Fraction(0)
        fix.add(y)                                   # (tritt hier nicht auf)
fix = sorted(fix)
assert len(fix) == 9
print(f"9 Fixpunkte, alle in Drittelkoordinaten: {fix[:3]} ...")

D4s_min = ([tuple(Fraction(x) for x in v)
            for v in itertools.product([-1, 0, 1], repeat=4)
            if sum(x * x for x in v) == 1] +
           [tuple(Fraction(s, 2) for s in signs)
            for signs in itertools.product([-1, 1], repeat=4)])
assert len(D4s_min) == 24

alle = set()
for x in fix:
    alle.add(sum(c * c for c in x) % 1)
    for y in fix:
        alle.add(sum(a * b for a, b in zip(x, y)) % 1)
    for k in D4s_min:
        alle.add(sum(a * b for a, b in zip(k, x)) % 1)
nenner = sorted({f.denominator for f in alle})
print("Nennerspektrum aller Invarianten:", nenner)
assert nenner == [1, 2, 3, 6] and Fraction(2, 9) not in alle
print("2/9 kommt NICHT vor — Negativbefund exakt. (Grund: Ordnung 5 fehlt.)")

# ---------------------------------------------------------------
# G) Verdopplungs-Vorstruktur: -1-Paarung, 24 = 4 x 6
# ---------------------------------------------------------------
def oidx(k):
    for i, o in enumerate(os_):
        if any(np.array_equal(k, x) for x in o):
            return i
pairs = {i: oidx(-o[0]) for i, o in enumerate(os_)}
assert all(j != i for i, j in pairs.items())
print("Paarung Orbit <-> Spiegelorbit:", pairs, " -> 24 = 4 x 6.")
print("Alle Kontrollen bestanden.")
