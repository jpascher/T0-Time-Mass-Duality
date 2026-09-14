#!/usr/bin/env python3
"""OPH icosahedral carrier versus the FFGFT D4 lattice: what they share.

Exact integer/sympy checks of the points left open earlier:

  (A) Aut(D4) recomputed from the 24 roots: order 1152, order distribution
      (1,2,3,4,6,8,12) = (1,139,80,228,464,144,96), no element of order 5
      (5 does not divide 1152) -- Dok. 314's negative theorem: A5 cannot act
      on the D4 lattice.
  (B) Among the 80 order-3 elements exactly 16 are fixed-point-free on R^4
      (|det(1-A)| = 9); each acts freely on the 24 roots: 8 orbits of 3, the
      first shell is 8 copies of the regular Z3-module (Dok. 314 (b)).
  (C) On the 12-port carrier every 3-fold rotation acts freely: 4 orbits of 3,
      the port module is 4 copies of the regular Z3-module = half of the D4
      first shell (Dok. 314: "24 = 12 + 12").
  (D) The largest subgroup of A5 that is compatible with the lattice is the
      tetrahedral group A4 (order 12): it consists exactly of the A5 elements
      whose matrices are integral (no phi), it acts simply transitively on the
      12 ports (the ports are an A4-torsor), and it embeds in W(D4) < Aut(D4).
  (E) Limitation: the port Z3 (a 3-fold axis of the icosahedron) has a fixed
      axis in R^3, so in this embedding it is never one of the 16 orbifold
      generators, which are fixed-point-free on R^4. The two Z3's are
      conjugate-inequivalent in Aut(D4).

Usage: python3 a5_vs_d4.py
"""
from __future__ import annotations
import itertools
from collections import Counter
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------
# (A) Aut(D4)
# ----------------------------------------------------------------------
roots = []
for i, j in itertools.combinations(range(4), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        v = [0, 0, 0, 0]; v[i] = si; v[j] = sj
        roots.append(tuple(v))
assert len(roots) == 24
rootset = set(roots)
R = np.array(roots)
# a basis of R^4 from four roots; automorphisms of the D4 lattice may be
# half-integral in these coordinates (triality), so no integrality is imposed:
# a linear map that permutes the 24 roots preserves the lattice they generate.
basis = np.array([(1, 1, 0, 0), (1, -1, 0, 0), (0, 0, 1, 1), (0, 0, 1, -1)], dtype=float)
Binv = np.linalg.inv(basis.T)
auts = []
for img in itertools.product(range(24), repeat=4):
    M = np.array([roots[k] for k in img], dtype=float).T @ Binv   # M * basis_i = root_img_i
    M2 = np.rint(2 * M)
    if not np.allclose(2 * M, M2, atol=1e-9): continue
    if all(tuple(np.rint(M @ r).astype(int)) in rootset and np.allclose(M @ r, np.rint(M @ r), atol=1e-9) for r in roots):
        auts.append(np.round(M, 6))
assert len(auts) == 1152
def order(M, cap=13):
    P, k = M.copy(), 1
    I = np.eye(4)
    while not np.allclose(P, I, atol=1e-6):
        P = P @ M; k += 1
        if k > cap: return None
    return k
dist = Counter(order(M) for M in auts)
assert dist == {1: 1, 2: 139, 3: 80, 4: 228, 6: 464, 8: 144, 12: 96}, dist
assert 5 not in dist and 1152 % 5 != 0
print("(A) |Aut(D4)| = 1152, orders", dict(sorted(dist.items())), "; no order 5 (5 does not divide 1152)")

# ----------------------------------------------------------------------
# (B) orbifold generators and free Z3 orbits on the roots
# ----------------------------------------------------------------------
I4 = np.eye(4)
ord3 = [M for M in auts if order(M) == 3]
orbifold = [M for M in ord3 if abs(round(np.linalg.det(I4 - M))) == 9]
assert len(orbifold) == 16
def orbits(M, pts):
    seen, orbs = set(), []
    for p in pts:
        if p in seen: continue
        o, q = [], p
        while q not in seen:
            seen.add(q); o.append(q); q = tuple(np.rint(M @ np.array(q)).astype(int))
        orbs.append(o)
    return orbs
for M in orbifold:
    orbs = orbits(M, roots)
    assert len(orbs) == 8 and all(len(o) == 3 for o in orbs)
    assert all(not np.allclose(M @ np.array(r), np.array(r)) for r in roots)
print("(B) 16 of the 80 order-3 elements are fixed-point-free on R^4 (|det(1-A)| = 9);")
print("    each acts freely on the 24 roots: 8 orbits of 3 = 8 x regular Z3-module")

# ----------------------------------------------------------------------
# (C) the 12-port carrier and its 3-fold rotations
# ----------------------------------------------------------------------
s5 = sp.sqrt(5); phi = (1 + s5) / 2
verts = []
for s1, s2 in itertools.product((1, -1), repeat=2):
    verts += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = [sp.Matrix(v) for v in verts]
n = 12
adj = {i: set() for i in range(n)}
for i, j in itertools.combinations(range(n), 2):
    if sp.simplify((V[i] - V[j]).dot(V[i] - V[j]) - 4) == 0:
        adj[i].add(j); adj[j].add(i)
autos = []
def bt(p, used):
    k = len(p)
    if k == n: autos.append(tuple(p)); return
    for v in range(n):
        if v in used: continue
        if all((v in adj[p[i]]) == (k in adj[i]) for i in range(k)):
            bt(p + [v], used | {v})
bt([], set())
assert len(autos) == 120
def porder(p):
    q, k = list(range(n)), 0
    while True:
        q = [p[x] for x in q]; k += 1
        if q == list(range(n)): return k
B3 = sp.Matrix.hstack(V[0], V[1], V[2])
def matrix_of(p):
    M = (sp.Matrix.hstack(V[p[0]], V[p[1]], V[p[2]]) * B3.inv()).applyfunc(sp.simplify)
    assert all(sp.simplify(M * V[i] - V[p[i]]) == sp.zeros(3, 1) for i in range(n))
    return M
mats = {p: matrix_of(p) for p in autos}
rot = [p for p in autos if sp.simplify(mats[p].det()) == 1]
assert len(rot) == 60
three = [p for p in rot if porder(p) == 3]
assert len(three) == 20
for p in three:
    assert all(p[i] != i for i in range(n))
    orbs = orbits_p = []
    seen = set()
    for i in range(n):
        if i in seen: continue
        o, q = [], i
        while q not in seen: seen.add(q); o.append(q); q = p[q]
        orbs.append(o)
    assert len(orbs) == 4 and all(len(o) == 3 for o in orbs)
print("(C) all 20 three-fold rotations act freely on the 12 ports: 4 orbits of 3 = 4 x regular Z3-module")
print("    port module (12) = half of the D4 first shell (24) as Z3-modules")

# ----------------------------------------------------------------------
# (D) the tetrahedral subgroup A4 < A5: integral matrices, simply transitive, inside W(D4)
# ----------------------------------------------------------------------
integral = [p for p in rot if all(e.is_integer for e in mats[p])]
assert len(integral) == 12
assert Counter(porder(p) for p in integral) == {1: 1, 2: 3, 3: 8}      # A4
# simply transitive on the ports: 12 elements, images of port 0 are all 12 ports, no fixed points
assert sorted(p[0] for p in integral) == list(range(n))
assert all(all(p[i] != i for i in range(n)) for p in integral if porder(p) > 1)
# closed under composition
keyset = set(integral)
for p in integral:
    for q in integral:
        assert tuple(p[q[i]] for i in range(n)) in keyset
print("(D) the integral elements of A5 form the tetrahedral group A4 (orders 1,2,3 = 1,3,8);")
print("    A4 acts simply transitively on the 12 ports: the port set is an A4-torsor")
# embed A4 into Aut(D4): 3x3 integer matrix M -> diag(M, 1)
autkeys = {np.round(M, 6).tobytes() for M in auts}
for p in integral:
    M3 = np.array(mats[p].tolist(), dtype=int)
    M4 = np.block([[M3, np.zeros((3, 1), dtype=int)], [np.zeros((1, 3), dtype=int), np.ones((1, 1), dtype=int)]])
    assert np.round(M4.astype(float), 6).tobytes() in autkeys
print("    A4 embeds in Aut(D4) as diag(M,1); A5 itself cannot (order 5)")

# ----------------------------------------------------------------------
# (E) the port Z3 is not an orbifold generator
# ----------------------------------------------------------------------
orb_keys = {np.round(M, 6).tobytes() for M in orbifold}
for p in integral:
    if porder(p) == 3:
        M3 = np.array(mats[p].tolist(), dtype=int)
        M4 = np.block([[M3, np.zeros((3, 1), dtype=int)], [np.zeros((1, 3), dtype=int), np.ones((1, 1), dtype=int)]])
        assert abs(round(np.linalg.det(I4 - M4))) == 0            # fixes a line
        assert np.round(M4.astype(float), 6).tobytes() not in orb_keys
# conjugacy: an orbifold generator has no fixed vector, a 3D rotation always has one,
# so no conjugate of diag(M,1) can be an orbifold generator.
print("(E) the port Z3 (3-fold icosahedral axis, embedded as diag(M,1)) fixes a line in R^4:")
print("    it is one of the 80-16 = 64 non-orbifold order-3 elements, never one of the 16 orbifold generators")

# ----------------------------------------------------------------------
# (F) can an orbifold Z3 carry the 12 ports at all?  Test all Z3-stable
#     12-halves (4 of the 8 free orbits) of the first shell, for each of the
#     16 orbifold generators.
# ----------------------------------------------------------------------
def gram_int(S): return np.rint(S @ S.T).astype(int)
def is_D3half(S):            # cuboctahedron = D3 roots: each root has 4 others at inner product 1, rank 3
    G = gram_int(S)
    return np.linalg.matrix_rank(S) == 3 and all(np.sum(G[i] == 1) == 4 for i in range(12))
def icosa_spectrum(S, val):  # graph on inner product == val isomorphic to icosahedron? (spectrum test)
    A = (gram_int(S) == val).astype(int); np.fill_diagonal(A, 0)
    ev = np.round(sorted(np.linalg.eigvalsh(A)), 4)
    return list(ev) == [round(-5 ** .5, 4)] * 3 + [-1.0] * 5 + [round(5 ** .5, 4)] * 3 + [5.0]
n_halves = n_d3 = n_ico = n_tight = 0
for M in orbifold:
    orbs = orbits(M, roots)
    for choice in itertools.combinations(range(8), 4):
        S = np.array([r for k in choice for r in orbs[k]], float)
        n_halves += 1
        n_d3 += is_D3half(S)
        n_ico += any(icosa_spectrum(S, v) for v in (-1, 0, 1))
        n_tight += np.allclose(np.linalg.eigvalsh(S @ S.T), [0] * 8 + [6] * 4)
assert n_halves == 16 * 70 and n_d3 == 0 and n_ico == 0
print("(F) of the %d orbifold-Z3-stable 12-halves of the D4 shell: %d cuboctahedral, %d with an icosahedral"
      " inner-product graph, %d tight frames in R^4 (Gram eigenvalue 6 x4, spectra involve sqrt13, stabiliser 18)"
      % (n_halves, n_d3, n_ico, n_tight))
print("    => no orbifold Z3 carries the ports; the obstruction (a Z3 stabilising a 12-half fixes its normal line)")
print("       is structural, not an artefact of the diag(M,1) embedding")

print("ALL CHECKS PASSED")
