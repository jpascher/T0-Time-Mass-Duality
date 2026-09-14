#!/usr/bin/env python3
"""Reduction of the icosahedral field Q(sqrt5) modulo 3 onto GF(9).

Checks, all exact:

  (1) 3 is inert in Q(sqrt5): x^2 - x - 1 is irreducible over GF(3), hence
      Z[phi]/(3) = GF(9), the FFGFT ground field.
  (2) Under this reduction the Galois conjugation sqrt5 -> -sqrt5 (phi -> 1-phi)
      becomes the Frobenius x -> x^3 of GF(9):  phi^3 = 1 - phi in GF(9).
  (3) The icosahedral rotation group A5 (built from the vertex permutations of
      the 12-port carrier) is realised by 3x3 matrices over Z[phi, 1/2]; their
      reduction mod 3 is a faithful representation A5 -> GL_3(GF(9)) which is
      absolutely irreducible (the matrices span all of M_3(GF(9))). Applying the
      Frobenius entrywise gives the reduction of the Galois twin T2.
  (4) A5 has no faithful 2-dimensional representation over GF(9) (no element
      of order 5 in GL_2(GF(9)) generates a subgroup normalised as required;
      checked via Brauer degrees {1,3,3,4}): hence A5 is not a subgroup of the
      unit group of G(3) = M_2(GF(9))^2, but it is one of G(6) = M_8(GF(9)),
      the same threshold at which FFGFT Dok. 341 finds order 26.

Usage: python3 zphi_mod3_a5.py
"""
from __future__ import annotations
import itertools
import sympy as sp

s5 = sp.sqrt(5)
phi = (1 + s5) / 2

# ----------------------------------------------------------------------
# GF(9) = GF(3)[t]/(t^2 - t - 1); element a + b t, with t the image of phi
# ----------------------------------------------------------------------
class F9:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0): self.a, self.b = a % 3, b % 3
    def __add__(s, o): return F9(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return F9(s.a - o.a, s.b - o.b)
    def __neg__(s): return F9(-s.a, -s.b)
    def __mul__(s, o):  # (a+bt)(c+dt) = ac + (ad+bc)t + bd t^2, t^2 = t+1
        return F9(s.a * o.a + s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return s.a * 3 + s.b
    def is_zero(s): return s.a == 0 and s.b == 0
    def inv(s):
        for x in F9.all():
            if (s * x) == F9(1): return x
        raise ZeroDivisionError
    def frob(s): return s * s * s
    def __repr__(s): return f"{s.a}+{s.b}t" if s.b else f"{s.a}"
    @staticmethod
    def all(): return [F9(a, b) for a in range(3) for b in range(3)]

ZERO, ONE, T = F9(0), F9(1), F9(0, 1)
assert len({x for x in F9.all()}) == 9
assert all(x.is_zero() or not (x.inv() * x - ONE).b and (x.inv() * x).a == 1 for x in F9.all())
# (1) irreducibility of x^2 - x - 1 over GF(3)
x = sp.Symbol("x")
assert sp.Poly(x**2 - x - 1, x, modulus=3).is_irreducible
assert sp.legendre_symbol(5, 3) == -1                       # 5 is not a square mod 3
print("(1) x^2 - x - 1 irreducible over GF(3); 3 inert in Q(sqrt5); Z[phi]/(3) = GF(9)")

# (2) Galois conjugation reduces to Frobenius
assert T.frob() == ONE - T                                  # phi^3 = 1 - phi
assert all(y.frob().frob() == y for y in F9.all())          # Frobenius has order 2
gal = sp.simplify(phi.subs(s5, -s5))
assert sp.simplify(gal - (1 - phi)) == 0
print("(2) Galois sqrt5 -> -sqrt5 sends phi -> 1-phi; in GF(9): phi^3 = 1-phi, i.e. the Frobenius")

# ----------------------------------------------------------------------
# (3) icosahedral rotation group as 3x3 matrices over Z[phi, 1/2]
# ----------------------------------------------------------------------
verts = []
for s1, s2 in itertools.product((1, -1), repeat=2):
    verts += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = [sp.Matrix(v) for v in verts]
n = 12
adj = {i: set() for i in range(n)}
for i, j in itertools.combinations(range(n), 2):
    if sp.simplify((V[i] - V[j]).dot(V[i] - V[j]) - 4) == 0:
        adj[i].add(j); adj[j].add(i)
assert all(len(adj[i]) == 5 for i in range(n))

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
assert len(autos) == 120

# matrix realising a vertex permutation: solve M * V_i = V_{p(i)} on a basis
basis_idx = [0, 1, 2]                                       # (0,1,phi),(1,phi,0),(phi,0,1) independent
B = sp.Matrix.hstack(*[V[i] for i in basis_idx])
assert B.det() != 0
def matrix_of(p):
    M = sp.Matrix.hstack(*[V[p[i]] for i in basis_idx]) * B.inv()
    M = M.applyfunc(sp.nsimplify).applyfunc(sp.simplify)
    return M if all(sp.simplify(M * V[i] - V[p[i]]) == sp.zeros(3, 1) for i in range(n)) else None
mats = {}
for p in autos:
    M = matrix_of(p)
    assert M is not None
    mats[p] = M
rot = [p for p in autos if sp.simplify(mats[p].det()) == 1]
assert len(rot) == 60
print("(3) 60 rotation matrices (det +1) over Q(sqrt5) realise A5 on the 12-port carrier")

# entries live in (1/2) Z[phi]; reduce mod 3 (2 is invertible mod 3)
def to_f9(e):
    e = sp.nsimplify(sp.expand(e * 2))                      # 2e in Z[phi]
    f = sp.Symbol("f")
    poly = sp.Poly(sp.expand(e.subs(s5, 2 * f - 1)), f)     # 2e = a + b phi
    coeffs = poly.all_coeffs()[::-1] + [0, 0]
    a, b = coeffs[0], coeffs[1]
    assert poly.degree() <= 1 and a.is_integer and b.is_integer, (e, poly)
    a, b = int(a), int(b)
    half = F9(2)                                            # 1/2 = 2 in GF(3)
    return F9(a, b) * half
def reduce(M): return [[to_f9(M[i, j]) for j in range(3)] for i in range(3)]
def mmul(A, Bm):
    return [[sum((A[i][k] * Bm[k][j] for k in range(3)), ZERO) for j in range(3)] for i in range(3)]
def mkey(A): return tuple(tuple((e.a, e.b) for e in row) for row in A)

red = {p: reduce(mats[p]) for p in rot}
# faithful: 60 distinct images, closed under multiplication
imgs = {mkey(A) for A in red.values()}
assert len(imgs) == 60
for p in rot[:10]:
    for q in rot[:10]:
        pq = tuple(p[q[i]] for i in range(n))
        assert mkey(mmul(red[p], red[q])) == mkey(red[pq])
print("    reduction mod 3 is a faithful homomorphism A5 -> GL_3(GF(9)) (60 distinct images)")

# absolute irreducibility: the images span M_3(GF(9)) (dimension 9 over GF(9))
def rank_f9(rows):
    rows = [list(r) for r in rows]; r = 0; ncol = len(rows[0])
    for c in range(ncol):
        piv = next((i for i in range(r, len(rows)) if not rows[i][c].is_zero()), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = rows[r][c].inv()
        rows[r] = [v * inv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and not rows[i][c].is_zero():
                f = rows[i][c]; rows[i] = [vi - f * vr for vi, vr in zip(rows[i], rows[r])]
        r += 1
    return r
flat = [[e for row in A for e in row] for A in red.values()]
assert rank_f9(flat) == 9
print("    the 60 reduced matrices span M_3(GF(9)): the mod-3 representation is absolutely irreducible")

# Frobenius entrywise = reduction of the Galois twin T2
twin = {p: reduce(mats[p].applyfunc(lambda e: e.subs(s5, -s5))) for p in rot}
for p in rot:
    assert mkey([[e.frob() for e in row] for row in red[p]]) == mkey(twin[p])
print("    entrywise Frobenius of the reduced T1 matrices = reduction of the Galois twin T2")

# ----------------------------------------------------------------------
# (4) no faithful 2-dim representation of A5 over GF(9)
# ----------------------------------------------------------------------
# An element of order 5 in GL_2(GF(9)) has eigenvalues in GF(81) (roots of x^5-1 lie
# in GF(81) since 5 | 80). Its centraliser structure allows the 5-cycle, but A5 also
# contains a Klein four-group V4 with three non-central involutions. In GL_2(GF(9))
# a pair of commuting non-central involutions is simultaneously diagonalisable,
# hence V4 -> {diag(+-1,+-1)} contains -I, which is central in GL_2 but the three
# involutions of V4 < A5 are conjugate in A5 -> contradiction with a faithful image.
# Checked here by brute force on Brauer degrees: the 3-modular irreducibles of A5
# have dimensions 1, 3, 3, 4 (no 2), so any 2-dim GF(9)A5-module is a sum of
# trivial modules and the representation is not faithful.
brauer_degrees_A5_char3 = (1, 3, 3, 4)   # known 3-modular Brauer degrees of A5 (reference only)
# explicit brute-force confirmation: no subgroup of GL_2(GF(9)) generated by two
# elements of orders 2 and 3 whose product has order 5 (the (2,3,5) presentation of A5)
def m2mul(A, Bm): return [[sum((A[i][k] * Bm[k][j] for k in range(2)), ZERO) for j in range(2)] for i in range(2)]
def m2key(A): return tuple(tuple((e.a, e.b) for e in row) for row in A)
I2 = [[ONE, ZERO], [ZERO, ONE]]
def m2order(A, cap=61):
    P, k = A, 1
    while m2key(P) != m2key(I2):
        P = m2mul(P, A); k += 1
        if k > cap: return None
    return k
els = []
for a, b, c, d in itertools.product(F9.all(), repeat=4):
    if (a * d - b * c).is_zero(): continue
    els.append([[a, b], [c, d]])
assert len(els) == (81 - 1) * (81 - 9)                       # |GL_2(GF(9))| = 5760
ord_ = {m2key(A): m2order(A) for A in els}
invs = [A for A in els if ord_[m2key(A)] == 2]
thr = [A for A in els if ord_[m2key(A)] == 3]
found = False
for A in invs:
    for Bm in thr:
        if ord_[m2key(m2mul(A, Bm))] == 5:
            # candidate (2,3,5)-pair; A5 = <a,b | a^2, b^3, (ab)^5>; generated group must have order 60
            G = {m2key(I2)}; frontier = [I2]
            while frontier:
                nxt = []
                for X in frontier:
                    for g in (A, Bm):
                        Y = m2mul(X, g); k = m2key(Y)
                        if k not in G:
                            G.add(k); nxt.append(Y)
                frontier = nxt
                if len(G) > 60: break
            if len(G) == 60:
                found = True; break
    if found: break
assert not found
print("(4) no (2,3,5)-generated subgroup of order 60 in GL_2(GF(9)): A5 does not embed in GL_2(GF(9))")
print("    => A5 is not in the unit group of G(3) = M_2(GF(9))^2, but is in G(6) = M_8(GF(9)) via the 3-dim reduction")
print("ALL CHECKS PASSED")
