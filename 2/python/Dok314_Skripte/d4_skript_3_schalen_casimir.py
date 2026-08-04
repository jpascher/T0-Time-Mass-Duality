#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOTIZ Gitter im Hilbertraum — Skript 3
Teile H2-H4: Schalensaetze (Gleichverteilung/6er-Bloecke generisch),
Epstein-Zeta bei s=-1/2 (Casimir D4-Torus vs Z4-Torus, Kovolumen 1),
Waermekern-Beobachtbarkeitsgrenze.
Abhaengigkeiten: numpy, mpmath. Deterministisch.
Stand: 4. August 2026
"""
import itertools, collections
import numpy as np
from mpmath import mp, mpf, gammainc, gamma, pi, power, sqrt, exp
from mpmath import zeta as riemann_zeta

mp.dps = 30

# ---------------------------------------------------------------
# H2) Schalensaetze unter Trialitaets-Z3 und -1 (bis Norm 20)
# ---------------------------------------------------------------
A2x = np.array([[-1, 1, 1, 1], [-1, -1, -1, 1],
                [-1, 1, -1, -1], [-1, -1, 1, -1]])   # = 2A, Spur(A) = -2

def act(v):
    r = A2x @ v; assert np.all(r % 2 == 0); return r // 2

shells = collections.defaultdict(list)
for v in itertools.product(range(-5, 6), repeat=4):
    if v == (0, 0, 0, 0) or sum(v) % 2:
        continue
    n = sum(x * x for x in v)
    if n <= 20:
        shells[n].append(np.array(v))

print(f"{'Norm':>4} {'N':>5} {'Orbits':>7} {'je Chi':>7} {'6er':>5}")
for n in sorted(shells):
    vecs = shells[n]; seen = set(); orbs = []
    for v in vecs:
        if tuple(v) in seen: continue
        o = [v.copy()]; w = act(v)
        while not np.array_equal(w, v):
            o.append(w.copy()); w = act(w)
        seen |= {tuple(x) for x in o}; orbs.append(o)
    assert all(len(o) == 3 for o in orbs)            # A ohne Eigenwert 1
    def oidx(k):
        for i, o in enumerate(orbs):
            if any(np.array_equal(k, x) for x in o): return i
    assert all(oidx(-o[0]) != i for i, o in enumerate(orbs))  # -1 fixpunktfrei
    N = len(vecs); assert N % 6 == 0
    print(f"{n:>4} {N:>5} {len(orbs):>7} {N//3:>7} {N//6:>5}")
print("Satz bestaetigt: jede Schale = freie Dreierorbits, Charaktere N/3 je,")
print("6er-Bloecke N/6. Struktur GENERISCH — selektiert keine Schale.\n")

# ---------------------------------------------------------------
# H3) Epstein-Zeta, Kovolumen 1 (unimodulare Spektralgitter):
#   Z4-Torus:  M = Z4 (selbstdual)
#   D4-Torus:  M = 2^(1/4) D4*  (Normen sqrt2*m, Anzahl N_D4(2m));
#              M* isometrisch zu M
#   zeta_M(s) = pi^s/Gamma(s) [A(s) + A*(2-s) + 1/(s-2) - 1/s],
#   A(s) = Sum' N (pi n)^(-s) Gamma(s, pi n)  (obere unvollstaendige)
# ---------------------------------------------------------------
def counts(pred, maxnorm, R):
    c = collections.Counter()
    for v in itertools.product(range(-R, R + 1), repeat=4):
        if v == (0, 0, 0, 0) or not pred(v): continue
        n = sum(x * x for x in v)
        if n <= maxnorm: c[n] += 1
    return c

Z4c = counts(lambda v: True, 120, 11)
D4c = counts(lambda v: sum(v) % 2 == 0, 120, 11)
Z4_norms = {mpf(n): N for n, N in Z4c.items()}
D4M_norms = {sqrt(2) * mpf(m): D4c[2 * m]
             for m in range(1, 61) if 2 * m in D4c}

def A(nc, s):
    return sum(N * power(pi * n2, -s) * gammainc(s, pi * n2)
               for n2, N in nc.items())

def zeta_M(nc, s):        # A* = A (selbstduale Struktur, Kovolumen 1)
    return power(pi, s) / gamma(s) * (A(nc, s) + A(nc, mpf(2) - s)
                                      + 1 / (s - 2) - 1 / s)

# Verifikation 1: s = 4, 5 gegen (langsam konvergente) Direktsumme
for s in (mpf(4), mpf(5)):
    direct = sum(N * power(n2, -s) for n2, N in Z4_norms.items())
    assert abs(zeta_M(Z4_norms, s) - direct) < mpf('1e-3')
# Verifikation 2: Z4 exakt gegen 8(1-4^(1-s)) zeta(s) zeta(s-1)
for s in (mpf(4), mpf(5), mpf('-0.5')):
    ana = 8 * (1 - power(4, 1 - s)) * riemann_zeta(s) * riemann_zeta(s - 1)
    assert abs(zeta_M(Z4_norms, s) - ana) < mpf('1e-25'), s
print("Zeta-Formel verifiziert (Direktsumme; Jacobi-Identitaet auf 25+ Stellen).")

s_c = mpf('-0.5')
zZ4, zD4 = zeta_M(Z4_norms, s_c), zeta_M(D4M_norms, s_c)
print(f"zeta_Z4(-1/2)  = {zZ4}")
print(f"zeta_D4T(-1/2) = {zD4}")
EZ4, ED4 = pi * zZ4, pi * zD4
print(f"Casimir E = pi*zeta:  Z4 {EZ4}   D4 {ED4}")
assert EZ4 < ED4
print("-> Z4-Torus liegt TIEFER (dichtestes Gitter hat groesste")
print("   Spektralluecke sqrt2 und damit weniger negative Nullpunktsenergie).")
print("   Fuer s > 0 ist die Ordnung invertiert; zeta(0) = -1 universell.\n")

# ---------------------------------------------------------------
# H4) Waermekern (Modulartransformation theta(t) = t^-2 theta*(1/t))
# ---------------------------------------------------------------
print("t^2 * theta(t), Kovolumen 1:")
for t in (mpf('0.5'), mpf('0.2'), mpf('0.1'), mpf('0.05')):
    thZ = power(t, -2) * (1 + sum(N * exp(-pi / t * n2)
                                  for n2, N in Z4_norms.items()))
    thD = power(t, -2) * (1 + sum(N * exp(-pi / t * n2)
                                  for n2, N in D4M_norms.items()))
    print(f"  t={float(t):<5} Z4 {float(t**2*thZ):.12f}  "
          f"D4 {float(t**2*thD):.12f}  relDiff {float((thD-thZ)/thZ):.3e}")
print("Weyl-Term identisch; Gitterunterschied exponentiell unterdrueckt.")
print("Alle Kontrollen bestanden.")
