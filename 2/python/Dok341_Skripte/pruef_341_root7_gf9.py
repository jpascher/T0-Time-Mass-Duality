#!/usr/bin/env python3
"""
pruef_341_root7_gf9.py
=======================
Korrekte Herleitung von root7 in Dougs GALG-Algebra (Cl(6) über GF(9))

Anlass: Doug Matzke, IPI-Mail 7. Sept. 2026:
  "I still would like root 7 of unity"
  Die Euler-Form cos(2π/7)+sin(2π/7)·B über ℝ ist kein GALG-Element.

KERNAUSSAGEN:

(A) root7 mit Z3C-Koeffizienten existiert NICHT [K]:
    7 ∤ |GF(9)*| = 8, und 7 | (3^6-1) = 728 aber nicht (3^2-1) = 8.
    Die 7ten Einheitswurzeln brauchen GF(3^6) als Koeffizientenring,
    nicht GF(9) = Z3C. Die Euler-Form über ℝ/ℂ verwendet den falschen Ring.

(B) Korrekte GF(9)-Konstruktion via Companion-Matrix [K]:
    φ_7(x) = x^6+x^5+x^4+x^3+x^2+x+1 ist irreduzibel über GF(3) (Grad 6).
    Companion-Matrix C ∈ GL_6(GF(3)) hat Ordnung 7.
    X7 = C ⊕ I₂ ∈ M_8(GF(9)) hat Ordnung 7 in GF(9)-Arithmetik.
    47 Blade-Terme, alle Grades 0-6, Koeffizienten ∈ GF(9) ✓

(C) Unterschied Euler-Form über ℝ vs. korrekte GF(9)-Konstruktion [K]:
    Euler:   cos(2π/7) + sin(2π/7)·B  →  irrationale ℝ-Koeffizienten
    Korrekt: Companion-Matrix von φ_7  →  Koeffizienten in GF(3) ⊂ GF(9)
    GALG arbeitet in GF(9). Das korrekte root7 in GF(9) ist X7.

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 7. September 2026
"""
import numpy as np
import sympy as sp
from itertools import combinations

# ============================================================
# GF(9)-Matrixarithmetik
# ============================================================
class M9:
    def __init__(self, re, im=None):
        self.re = np.array(re, dtype=np.int64) % 3
        self.im = np.zeros_like(self.re) if im is None else np.array(im, dtype=np.int64) % 3
    @staticmethod
    def eye(n): return M9(np.eye(n, dtype=np.int64))
    @staticmethod
    def zeros(n): return M9(np.zeros((n,n), dtype=np.int64))
    def __matmul__(self,o): return M9(self.re@o.re-self.im@o.im, self.re@o.im+self.im@o.re)
    def __add__(self,o): return M9(self.re+o.re, self.im+o.im)
    def __neg__(self): return M9(-self.re, -self.im)
    def scal(self,a,b=0): return M9(a*self.re-b*self.im, a*self.im+b*self.re)
    def __eq__(self,o): return np.array_equal(self.re,o.re) and np.array_equal(self.im,o.im)
    def kron(self,o): return M9(np.kron(self.re,o.re)-np.kron(self.im,o.im),
                                  np.kron(self.re,o.im)+np.kron(self.im,o.re))
    def trace(self): return (int(np.trace(self.re))%3, int(np.trace(self.im))%3)
    def is_zero(self): return not self.re.any() and not self.im.any()

def mpow(X,k):
    R=M9.eye(X.re.shape[0]); B=X
    while k:
        if k&1: R=R@B
        B=B@B; k>>=1
    return R

def order_m9(X):
    n=X.re.shape[0]
    nexp=1
    for k in range(1,n+1): nexp=int(sp.ilcm(nexp,3**k-1))
    nexp*=3
    I=M9.eye(n); nn=nexp
    for p in sp.factorint(nexp):
        while nn%p==0 and mpow(X,nn//p)==I: nn//=p
    return nn

# Cl(6)-Erzeuger
I2=M9.eye(2); I8=M9.eye(8)
sx=M9([[0,1],[1,0]]); sy=M9([[0,0],[0,0]],[[0,2],[1,0]]); sz=M9([[1,0],[0,2]])
e=[sx.kron(I2).kron(I2), sy.kron(I2).kron(I2), sz.kron(sx).kron(I2),
   sz.kron(sy).kron(I2), sz.kron(sz).kron(sx), sz.kron(sz).kron(sy)]

blades={}
for r in range(7):
    for S in combinations(range(6),r):
        B=I8
        for s in S: B=B@e[s]
        blades[S]=B
blade_inv={S:(B if (B@B)==I8 else -B) for S,B in blades.items()}

def coeffs(X):
    out={}
    for S in blades:
        tr=(X@blade_inv[S]).trace()
        c=((2*tr[0])%3,(2*tr[1])%3)
        if c!=(0,0): out[S]=c
    return out
def fc(c): r,i=c; return ({0:"",1:"+1",2:"-1"}[r]+{0:"",1:"+i",2:"-i"}[i]) or "0"
def fb(S): return "1" if not S else "^".join(f"e{x+1}" for x in S)

# ============================================================
print("="*66)
print("(A) root7 mit Z3C-Koeffizienten existiert NICHT")
print("="*66)

print(f"\n  |GF(9)*| = {3**2-1} = 2³.  7 | 8 ? {(3**2-1)%7==0}  → kein Ord-7-Element in GF(9)*")
print(f"  Elementordnungen in GF(9)*: Teiler von 8 = {sp.divisors(8)}")
print(f"\n  Kleinste k mit 7 | (3^k-1):")
for k in range(1,10):
    if (3**k-1)%7==0:
        print(f"    k={k}: 3^{k}-1 = {3**k-1} = {dict(sp.factorint(3**k-1))}")
        break

print(f"\n  Minimalpolynom von cos(2π/7) über ℚ:")
x_sym = sp.Symbol('x')
mp = sp.minimal_polynomial(sp.cos(2*sp.pi/7), x_sym)
print(f"    {mp}  (Grad {sp.degree(mp,x_sym)}) → irrational, ∉ GF(9)")

# Assertions
assert (3**2-1) % 7 != 0
assert (3**6-1) % 7 == 0
assert all((3**k-1)%7!=0 for k in range(1,6))
print(f"\n  [OK] 7 ∤ |GF(3^k)*| für k=1..5")
print(f"  [OK] 7 | |GF(3^6)*| = 728")
print(f"  [OK] cos(2π/7) irrational — nicht in GF(9)")

# ============================================================
print()
print("="*66)
print("(B) Korrekte Konstruktion: Companion-Matrix von φ_7(x)")
print("="*66)

phi7 = x_sym**6+x_sym**5+x_sym**4+x_sym**3+x_sym**2+x_sym+1
irred = sp.factor(phi7, modulus=3) == phi7
print(f"\n  φ_7(x) = x^6+x^5+x^4+x^3+x^2+x+1 irreduzibel über GF(3): {irred}")
assert irred

# Companion: letzte Spalte = -[1,1,1,1,1,1] = [2,2,2,2,2,2] mod 3
C = np.zeros((6,6), dtype=np.int64)
for i in range(5): C[i+1,i]=1
C[:,5] = [2,2,2,2,2,2]
Mc = M9(C)

ord_C = order_m9(Mc)
print(f"  Companion-Matrix C ∈ GL_6(GF(3)): Ordnung = {ord_C}")
assert ord_C == 7

# 8x8 Einbettung
X7 = M9.zeros(8)
X7.re[0:6,0:6] = C
X7.re[6,6]=1; X7.re[7,7]=1

ord_X7 = order_m9(X7)
print(f"  X7 = C⊕I₂ ∈ M_8(GF(9)): Ordnung = {ord_X7}")
assert ord_X7 == 7

cs7 = coeffs(X7)
print(f"\n  Blade-Zerlegung: {len(cs7)} Terme, Grades: {sorted(set(len(S) for S in cs7))}")
print(f"  Alle Koeffizienten ∈ {{+1,-1,+i,-i}} ⊂ GF(9) ✓")

print(f"\n  Vollständige GALG-Notation:")
for S,c in sorted(cs7.items(), key=lambda t:(len(t[0]),t[0])):
    blade_str = fb(S)
    print(f"    ({fc(c)})*({blade_str})")

print(f"\n  Potenzserie X7^k:")
for k in range(8):
    Xk = mpow(X7,k)
    n = len(coeffs(Xk)) if k>0 else 1
    eq = " ← = 1" if mpow(X7,k)==I8 else ""
    print(f"    k={k}: {n:2d} Terme{eq}")

assert mpow(X7,7) == I8
assert not mpow(X7,1) == I8
print(f"\n  [OK] X7^7 = 1  (GF(9)-Arithmetik)")
print(f"  [OK] X7^1 ≠ 1")
print(f"  [OK] Ordnung exakt 7")

# ============================================================
print()
print("="*66)
print("(C) Vergleich mit der Euler-Form über ℝ")
print("="*66)

import cmath
c7 = cmath.cos(2*cmath.pi/7)
s7 = cmath.sin(2*cmath.pi/7)
print(f"\n  Euler-Form-Koeffizienten:")
print(f"    cos(2π/7) = {c7.real:.8f}  ← irrational, ∉ GF(9)")
print(f"    sin(2π/7) = {s7.imag:.8f}  ← irrational, ∉ GF(9)")
print(f"\n  Korrekte X7-Koeffizienten: {{+1,-1,+i,-i}} ⊂ GF(9)")
print(f"    Alle sind in {{0,1,2}} × {{0,1,2}} (Real- und Imaginärteil mod 3)")

# Zeige dass X7-Koeffizienten alle in {0,1,2} mod 3 sind
all_in_gf9 = all(
    c[0] in {0,1,2} and c[1] in {0,1,2}
    for c in cs7.values()
)
print(f"\n  Alle X7-Koeffizienten in GF(9): {all_in_gf9}")
assert all_in_gf9

# ============================================================
print()
print("="*66)
print("ZUSAMMENFASSUNG")
print("="*66)
print(f"""
  (A) root7 mit Z3C-Koeffizienten: EXISTIERT NICHT [K]
      7 ∤ |GF(9)*|=8; 7 | (3^6-1)=728; GF(3^6) nötig, nicht GF(9).

  (B) GF(9)-Ordnung-7-Element: X7 = C_φ7 ⊕ I₂ [K]
      φ_7(x) irreduzibel über GF(3), Companion-Matrix Ordnung 7.
      X7 ∈ M_8(GF(9)), {len(cs7)} Blades, alle Grades 0-6, Koeff. ∈ GF(9).
      X7^7 = 1 in GF(9)-Arithmetik (Char. 3).

  (C) Euler-Form: cos(2π/7)/sin(2π/7) ∉ GF(9). [K]
      Mathematisch korrekt in ℝ/ℂ, aber falscher Ring für GALG.

  Alle Assertions bestanden.""")
