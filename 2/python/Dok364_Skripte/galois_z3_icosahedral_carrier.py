#!/usr/bin/env python3
"""Galois conjugation and Z3 restriction on the OPH twelve-port carrier.

Two exact statements about the icosahedral port module P = A + T1 + T2 + H:

  (1) The Galois automorphism sqrt5 -> -sqrt5 of Q(sqrt5) exchanges the two
      three-dimensional blocks T1 <-> T2 (Laplacian eigenvalues 5-sqrt5 <-> 5+sqrt5)
      and fixes A and H. Hence no structure defined over Q (a lattice, an
      integer character, exact rational repair arithmetic) can distinguish
      T1 from T2. Choosing T1 as "space" is a choice of the sign of sqrt5.
      The sum T1 + T2 is the only 6-dimensional A5-submodule with integer
      character; this is the "doubling" 6 = 3 + 3' of FFGFT Dok. 285.

  (2) Restricting to a 3-fold rotation C3 < A5 (Dok. 293, C3-in-A5 embedding)
      the port space splits into Z3-eigenspaces of dimensions 4 + 4 + 4, with
      blockwise A -> 1, T1 -> 1+w+w^2, T2 -> 1+w+w^2, H -> 1+2w+2w^2.

Reads the seam list from native_trace.json (ipi_native_baseline_2026-09-14)
or falls back to the canonical icosahedron. All arithmetic exact (sympy).

Usage:  python3 galois_z3_icosahedral_carrier.py [path/to/native_trace.json]
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp

n = 12
s5 = sp.sqrt(5)
phi = (1 + s5) / 2
w = sp.exp(2 * sp.pi * sp.I / 3)

# ----------------------------------------------------------------------
# 1. carrier graph
# ----------------------------------------------------------------------
def load_edges(path: Path):
    if path.exists():
        return [tuple(e) for e in json.loads(path.read_text())["seams"]]
    verts = []
    for s1, s2 in itertools.product((1, -1), repeat=2):
        verts += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
    return [(i, j) for i, j in itertools.combinations(range(n), 2)
            if sp.simplify(sum((a - b) ** 2 for a, b in zip(verts[i], verts[j])) - 4) == 0]

edges = load_edges(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("native_trace.json"))
assert len(edges) == 30
adj = {i: set() for i in range(n)}
A = sp.zeros(n, n)
for i, j in edges:
    A[i, j] = A[j, i] = 1
    adj[i].add(j); adj[j].add(i)
L = 5 * sp.eye(n) - A

# ----------------------------------------------------------------------
# 2. automorphism group and its rotation subgroup A5
# ----------------------------------------------------------------------
autos = []
def bt(p, used):
    k = len(p)
    if k == n:
        autos.append(tuple(p)); return
    for v in range(n):
        if v in used: continue
        if all((v in adj[p[i]]) == (k in adj[i]) for i in range(k)):
            bt(p + [v], used | {v})
bt([], set())
assert len(autos) == 120                                   # A5 x Z2

def perm_matrix(p):
    M = sp.zeros(n, n)
    for i in range(n): M[p[i], i] = 1
    return M
def order(p):
    q, k = list(range(n)), 0
    while True:
        q = [p[x] for x in q]; k += 1
        if q == list(range(n)): return k
# every vertex permutation here is even, so parity cannot separate rotations from
# roto-reflections; instead generate A5 from the elements of order 3 and 5, which
# are rotations (the improper elements have orders 2, 6, 10).
def compose(p, q): return tuple(p[q[i]] for i in range(n))
gens = [p for p in autos if order(p) in (3, 5)]
rot = set(gens) | {tuple(range(n))}
frontier = list(rot)
while frontier:
    new_elems = []
    for a in frontier:
        for g in gens:
            c = compose(a, g)
            if c not in rot:
                rot.add(c); new_elems.append(c)
    frontier = new_elems
rot = sorted(rot)
assert len(rot) == 60                                      # A5
orders = sorted(order(p) for p in rot)
assert orders.count(1) == 1 and orders.count(2) == 15 and orders.count(3) == 20 and orders.count(5) == 24
print("Automorphisms 120, rotations 60 = A5 (1+15+20+24 elements of order 1,2,3,5)")

# ----------------------------------------------------------------------
# 3. isotypic projectors of the Laplacian and their A5 characters
# ----------------------------------------------------------------------
# for a graph with 4 distinct Laplacian eigenvalues the spectral projectors are
# polynomials in L, so everything below is exact and fast.
mus = {"A": sp.Integer(0), "T1": 5 - s5, "H": sp.Integer(6), "T2": 5 + s5}
proj = {}
for name, mu in mus.items():
    P = sp.eye(n)
    for other in mus.values():
        if other != mu:
            P = P * (L - other * sp.eye(n)) / (mu - other)
    proj[name] = P.applyfunc(sp.simplify)
for name, P in proj.items():
    assert (P * P - P).applyfunc(sp.simplify) == sp.zeros(n, n)
dims_blocks = {k: sp.simplify(P.trace()) for k, P in proj.items()}
assert dims_blocks == {"A": 1, "T1": 3, "H": 5, "T2": 3}

def char(name, p):
    return sp.simplify((proj[name] * perm_matrix(p)).trace())

g5 = next(p for p in rot if order(p) == 5)
g3 = next(p for p in rot if order(p) == 3)
g2 = next(p for p in rot if order(p) == 2)
ident = tuple(range(n))
chi = {name: {k: char(name, g) for k, g in (("e", ident), ("g2", g2), ("g3", g3), ("g5", g5))}
       for name in proj}
print("Characters on (e, g2, g3, g5):")
for name in ("A", "T1", "T2", "H"):
    print("  ", name, {k: str(v) for k, v in chi[name].items()})

c1, c2 = chi["T1"]["g5"], chi["T2"]["g5"]
assert {sp.simplify(c1), sp.simplify(c2)} == {sp.simplify(phi), sp.simplify(1 - phi)}
assert sp.simplify(c1 + c2) == 1                           # 6D character integer
assert not c1.is_rational and not c2.is_rational
print("chi_T1(g5) + chi_T2(g5) = 1 : the 6 = 3 + 3' character is integral, each half irrational")

# ----------------------------------------------------------------------
# 4. Galois conjugation sqrt5 -> -sqrt5
# ----------------------------------------------------------------------
def galois(x): return sp.simplify(sp.sympify(x).subs(s5, -s5))
assert galois(5 - s5) == 5 + s5 and galois(5 + s5) == 5 - s5
assert galois(6) == 6 and galois(0) == 0
assert galois(c1) == c2 and galois(c2) == c1
assert galois(chi["H"]["g5"]) == chi["H"]["g5"]
assert proj["T1"].applyfunc(galois) == proj["T2"]          # the projectors themselves are swapped
assert proj["H"].applyfunc(galois) == proj["H"]
r1, r2 = (55 + s5) / 60, (55 - s5) / 60
assert galois(r1) == r2
print("Galois sqrt5 -> -sqrt5 swaps T1 <-> T2 (projectors, eigenvalues, characters, damping rates); fixes A, H")

x = sp.Symbol("x")
mp = sp.minimal_polynomial(5 - s5, x)
assert set(sp.roots(mp).keys()) == {5 - s5, 5 + s5}
P6 = (proj["T1"] + proj["T2"]).applyfunc(sp.simplify)
assert all(v.is_rational for v in P6) and not all(v.is_rational for v in proj["T1"])
print("Minimal polynomial over Q of the T1 eigenvalue:", mp, "(roots 5-sqrt5, 5+sqrt5)")
print("=> the projector onto T1+T2 is Q-rational, the projectors onto T1 and T2 separately are not:")
print("   over Q only the 6D block exists (FFGFT Dok. 285: 6 = 3 + 3').")

# ----------------------------------------------------------------------
# 5. restriction to C3 < A5
# ----------------------------------------------------------------------
G3 = perm_matrix(g3)
G3k = [sp.eye(n), G3, G3 * G3]
def z3_counts(P):
    out = {}
    for k, lam in (("1", 1), ("w", w), ("w^2", w ** 2)):
        m = sum(sp.conjugate(lam) ** j * (P * G3k[j]).trace() for j in range(3)) / 3
        out[k] = int(sp.nsimplify(sp.simplify(m)))
    return out
dims = z3_counts(sp.eye(n))
assert dims == {"1": 4, "w": 4, "w^2": 4}
print("Z3-eigenspaces of the port space under a 3-fold rotation:", dims)
expected = {"A": {"1": 1, "w": 0, "w^2": 0}, "T1": {"1": 1, "w": 1, "w^2": 1},
            "T2": {"1": 1, "w": 1, "w^2": 1}, "H": {"1": 1, "w": 2, "w^2": 2}}
for name in ("A", "T1", "T2", "H"):
    got = z3_counts(proj[name])
    assert got == expected[name], (name, got)
    print("  ", name, "| C3 ->", got)
print("Trivial Z3 part: dim 4; non-trivial part: dim 8.")

print("ALL CHECKS PASSED")
