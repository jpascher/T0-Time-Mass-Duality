#!/usr/bin/env python3
"""Phases as roots of unity: which symmetry lives in which channel over GF(3^k).

Exact checks (Dok. 364, section "Phasen als Einheitswurzeln"):

  (1) phi mod 3 is a primitive element of GF(9)*: phi^4 = -1, order 8.
  (2) The 72-degree rotation has characteristic polynomial (x-1)(x^2-(phi-1)x+1);
      mod 3 the quadratic factor has no root in GF(9); its roots lie in GF(81)
      and have order 5 (5 | 80). Five-fold symmetry exists only as a phase in
      the quadratic extension, never in GF(9) itself.
  (3) 13 | 728 = |GF(729)*| but 13 does not divide 80: order 26 needs the cubic
      extension (Dok. 341).
  (4) In characteristic 3 there is no primitive cube root of unity:
      x^3 - 1 = (x-1)^3. A Z3 action is unipotent, never a phase omega.
  (5) Lattice channel versus field channel: 5 does not divide |Aut(D4)| = 1152,
      but 5 | 80; 3 | 1152 but no cube root of unity in GF(3^k) for any k.

Usage: python3 phasen_einheitswurzeln.py
"""
import sympy as sp

# ---------------- GF(9) = GF(3)[t]/(t^2 - t - 1), t = phi mod 3 ----------------
class F9:
    def __init__(s, a, b=0): s.a, s.b = a % 3, b % 3
    def __add__(s, o): return F9(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return F9(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return F9(s.a * o.a + s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return 3 * s.a + s.b
ZERO, ONE, PHI = F9(0), F9(1), F9(0, 1)
ALL = [F9(a, b) for a in range(3) for b in range(3)]

def order(x, mul, one):
    p, k = x, 1
    while not p == one:
        p = mul(p, x); k += 1
        assert k < 1000
    return k

# (1)
assert PHI * PHI == PHI + ONE
assert PHI * PHI * PHI * PHI == F9(2)                       # phi^4 = -1
assert order(PHI, lambda a, b: a * b, ONE) == 8
print("(1) phi mod 3: phi^4 = -1, order 8 -> primitive element of GF(9)*")

# (2)
c = PHI - ONE                                               # 2 cos 72deg = phi - 1
roots_in_9 = [x for x in ALL if x * x - c * x + ONE == ZERO]
assert roots_in_9 == []
# GF(81) = GF(9)[y]/(y^2 - c y + 1), elements (u, v) = u + v y
def mul81(p, q):
    u1, v1 = p; u2, v2 = q
    return (u1 * u2 - v1 * v2, u1 * v2 + u2 * v1 + v1 * v2 * c)
one81 = (ONE, ZERO); y = (ZERO, ONE)
assert order(y, mul81, one81) == 5
assert 80 % 5 == 0
print("(2) x^2-(phi-1)x+1 has no root in GF(9); its root in GF(81) has order 5 -> five-fold symmetry is a phase in the quadratic extension")

# (3)
assert 728 % 13 == 0 and 80 % 13 != 0
print("(3) 13 | 728 = |GF(729)*|, 13 does not divide 80 -> order 26 needs the cubic extension (Dok. 341)")

# (4)
x = sp.Symbol("x")
assert sp.factor_list(x**3 - 1, modulus=3)[1] == [(x - 1, 3)] or \
       sp.Poly(x**3 - 1, x, modulus=3).factor_list()[1] == [(sp.Poly(x - 1, x, modulus=3), 3)]
for k in (1, 2, 3, 4, 6):
    assert (3**k - 1) % 3 != 0                              # no element of order 3 in GF(3^k)*
print("(4) x^3 - 1 = (x-1)^3 over GF(3): no primitive cube root of unity in any GF(3^k); Z3 acts unipotently")

# (5)
assert 1152 % 5 != 0 and 1152 % 3 == 0
print("(5) lattice channel: 3 | 1152 = |Aut(D4)|, 5 does not; field channel: 5 | 80, 3 never divides 3^k - 1")
print("    => three-fold symmetry must be lattice structure, five-fold symmetry must be a phase; the prime 3 decides")
print("ALL CHECKS PASSED")
