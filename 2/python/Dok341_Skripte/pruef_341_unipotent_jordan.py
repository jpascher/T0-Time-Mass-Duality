#!/usr/bin/env python3
"""
pruef_341_unipotent_jordan.py
==============================
Unipotente Einheitswurzeln (Ordnung 3^k), Jordan-Zerlegung, r273/r546 in G(6),
Unmöglichkeit von r729 in G(6), Euler-φ als Zahl der primitiven Wurzeln

Anlass: Doug Matzke, IPI-Mail 12. Sept. 2026:
  (1) r3c=(1+N), r6c=(-1+N) mit N=(a+b+c)(abc)=ab-ac+bc, N²=0: r3c³=1, r6c⁶=1.
      "even grade → commute with ALL other roots" — zu präzisieren.
  (2) r273, r546 "use 9 dims" — in G(6) möglich?
  (3) "interesting to find r729, since 3^6=729 leading to GF(729)" — zu korrigieren.
  (4) 32 von 80 bzw. 72 von 182 Ringelementen sind "80th/182nd roots" — Euler-φ.

ERGEBNISSE:
(A) N = e1e2 - e1e3 + e2e3: N² = 0; (1+N)³ = 1; (-1+N)³ = -1, (-1+N)⁶ = 1 [K].
    In Char. 3: (1±N)³ = ±1 + N³ = ±1 (Frobenius: Binomialkoeffizienten 3,3 ≡ 0).
    Ordnung 3 ist UNIPOTENT (Eigenwert 1, Jordan-Block), nie halbeinfach:
    3 ∤ 3^k-1 für alle k (vgl. pruef_341_primordnung).
(B) Kommutation: N kommutiert mit allen Elementen in disjunkten Erzeugern
    (e4,e5,e6); NICHT mit e1 und nicht einmal mit e1e2 [K].
    Dougs "9 dims" = disjunkte Erzeugermengen {a,b,c} ∪ 6 weitere.
(C) Jordan-Zerlegung X = S·U (S halbeinfach, U unipotent, [S,U]=0):
    ord(X) = ord(S)·ord(U), ord(S) | (3^k-1)-Struktur, ord(U) = 3^j.
    In G(6) = M_8(GF(9)): S auf 6-dim Block (ord | 728) ⊕ U auf 2-dim Jordan-Block
    (ord 3) → r273 = 3·91, r546 = 3·182, r2184 = 3·728 existieren in G(6) [K].
    Doug braucht keine 9 Dimensionen.
(D) r729 in G(6) UNMÖGLICH [K]: 729 = 3^6 ist reine 3-Potenz → unipotent.
    (1+N)^(3^j) = 1 + N^(3^j); in M_8 ist N^8 = 0, also (1+N)^9 = 1 immer.
    Maximale unipotente Ordnung in M_n(GF(9)) = kleinste 3-Potenz ≥ n:
    M_8 → 9, M_16 → 27, M_32 → 81, M_128 → 243, M_256 → 729 (= Cl(16)).
    Zudem: 729 hat mit GF(729) nichts zu tun — |GF(729)*| = 728.
(E) Dougs Zählungen 32/80 und 72/182 = φ(80) = 32, φ(182) = 72 [K]:
    Anzahl der Generatoren (primitiven Wurzeln) der zyklischen Gruppe ⟨X⟩.

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 12. September 2026
"""
import numpy as np, sympy as sp
from itertools import combinations

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
    def __sub__(self,o): return M9(self.re-o.re, self.im-o.im)
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
        tr=(X@blade_inv[S]).trace(); c=((2*tr[0])%3,(2*tr[1])%3)
        if c!=(0,0): out[S]=c
    return out
def fc(c): r,i=c; return ({0:"",1:"+1",2:"-1"}[r]+{0:"",1:"+i",2:"-i"}[i]) or "0"
def fb(S): return "1" if not S else "^".join(f"e{x+1}" for x in S)
def galg(X): return " ".join(f"({fc(c)})*{fb(S)}" for S,c in sorted(coeffs(X).items(), key=lambda t:(len(t[0]),t[0])))
def build(terms):
    X=M9.zeros(8)
    for S,c in terms: X=X+blades[S].scal(c[0],c[1])
    return X
N_EXP=1
for k in range(1,9): N_EXP=int(sp.ilcm(N_EXP,3**k-1))
N_EXP*=9
def order_m9(X, nexp=N_EXP):
    n=X.re.shape[0]; I=M9.eye(n)
    if not (mpow(X,nexp)==I): return None
    nn=nexp
    for p in sp.factorint(nexp):
        while nn%p==0 and mpow(X,nn//p)==I: nn//=p
    return nn
def commute(A,B): return (A@B-B@A).is_zero()

# ============================================================
print("="*66); print("(A) Dougs r3c / r6c: unipotente Trine / Anti-Trine"); print("="*66)
a,b,c = e[0],e[1],e[2]
N = (a+b+c)@(a@b@c)
print(f"  N = (a+b+c)(abc) = {galg(N)}")
assert (N@N).is_zero()
print(f"  N² = 0  [K]")
r3c = I8+N; r6c = (-I8)+N
assert mpow(r3c,3)==I8 and not (mpow(r3c,1)==I8)
assert mpow(r6c,3)==(-I8) and mpow(r6c,6)==I8
print(f"  (1+N)³ = 1,  (-1+N)³ = -1,  (-1+N)⁶ = 1   [K]")
print(f"  Grund (Char. 3): (x+N)³ = x³ + 3x²N + 3xN² + N³ = x³  → ±1")
print(f"  Ordnung 3 ist UNIPOTENT (Eigenwert 1 mit Jordan-Block) — kein Element")
print(f"  von GF(3^k)* hat Ordnung 3, da 3 ∤ 3^k-1 (pruef_341_primordnung).")

# ============================================================
print(); print("="*66); print("(B) Kommutation von N"); print("="*66)
print(f"  [N, e4] = 0: {commute(N,e[3])}   [N, e5e6] = 0: {commute(N,e[4]@e[5])}   (disjunkte Erzeuger)")
print(f"  [N, e1] = 0: {commute(N,e[0])}   [N, e1e2] = 0: {commute(N,e[0]@e[1])}   [N, e1e4] = 0: {commute(N,e[0]@e[3])}")
assert commute(N,e[3]) and commute(N,e[4]@e[5]) and not commute(N,e[0]) and not commute(N,e[0]@e[1])
print("  → 'even grade commutes with ALL roots' gilt NUR für Elemente in disjunkten")
print("    Erzeugern — nicht einmal für e1e2 (gerade, gleiche Erzeuger). Daher Dougs '9 dims':")
print("    {a,b,c} für r3c ⊕ 6 weitere für r91/r182 — disjunkt → kommutierend.  [K]")

# ============================================================
print(); print("="*66); print("(C) Jordan-Zerlegung: r273, r546, r2184 direkt in G(6)"); print("="*66)
print("  X = S·U, [S,U]=0, S halbeinfach (ord | 3^k-1-Struktur), U unipotent (ord 3^j)")
print("  → ord(X) = ord(S)·ord(U).  Konstruktion: S auf 6-dim Block ⊕ U auf 2-dim Jordan-Block.")
# primitives Polynom Grad 6 über GF(3) → Companion-Matrix ord 728
x=sp.Symbol('x')
prim=None
for coeffs_ in __import__('itertools').product(range(3),repeat=6):
    p=x**6+sum(coeffs_[i]*x**i for i in range(6))
    if coeffs_[0]==0: continue
    if not sp.Poly(p,x,modulus=3).is_irreducible: continue
    C=np.zeros((6,6),dtype=np.int64)
    for i in range(5): C[i+1,i]=1
    C[:,5]=[(-coeffs_[i])%3 for i in range(6)]
    if order_m9(M9(C), nexp=728)==728: prim=(p,C); break
p,C=prim
print(f"  primitives Polynom über GF(3): {p}  → Companion C mit ord(C) = 728")
def block(S6, U2):
    X=M9.zeros(8); X.re[0:6,0:6]=S6.re; X.im[0:6,0:6]=S6.im; X.re[6:8,6:8]=U2.re; X.im[6:8,6:8]=U2.im; return X
J2=M9([[1,1],[0,1]])   # Jordan-Block, ord 3
res={}
for name,k in [("r273 = 3·91",8),("r546 = 3·182",4),("r2184 = 3·728",1)]:
    S6=mpow(M9(C),k)          # ord 728/k
    X=block(S6,J2)
    o=order_m9(X)
    res[name]=o
    print(f"  {name}: S=C^{k} (ord {order_m9(S6,728)}) ⊕ J₂ (ord 3) → ord(X) = {o},  {len(coeffs(X))} Blades")
assert res["r273 = 3·91"]==273 and res["r546 = 3·182"]==546 and res["r2184 = 3·728"]==2184
X273=block(mpow(M9(C),8),J2)
print(f"\n  r273 in G(6), Blade-Form ({len(coeffs(X273))} Terme):")
print("  " + galg(X273))
print(f"  Kontrolle: r273^91 hat ord {order_m9(mpow(X273,91))} (=3, unipotenter Teil),")
print(f"             r273^3  hat ord {order_m9(mpow(X273,3))} (=91, halbeinfacher Teil)  [K]")
print("  → r273/r546 brauchen KEINE 9 Dimensionen; G(6) genügt.")

# ============================================================
print(); print("="*66); print("(D) r729 in G(6) unmöglich"); print("="*66)
print("  729 = 3^6: reine 3-Potenz → Element muss unipotent sein (X = 1+N, N nilpotent).")
print("  (1+N)^(3^j) = 1 + N^(3^j)  (Frobenius in Char. 3).")
print("  In M_8: N^8 = 0 ⇒ (1+N)^9 = 1 + N^9 = 1.  Also ord(U) ≤ 9 für alle Unipotenten.")
J8=np.eye(8,dtype=np.int64); 
for i in range(7): J8[i,i+1]=1
U8=M9(J8)
print(f"  Voller Jordan-Block J₈: (1+N)³ = 1? {mpow(U8,3)==I8};  (1+N)⁹ = 1? {mpow(U8,9)==I8}  → ord 9 (Maximum)")
assert not (mpow(U8,3)==I8) and mpow(U8,9)==I8
print("\n  Maximale unipotente Ordnung in M_n(GF(9)) = kleinste 3-Potenz ≥ n:")
for n,cl in [(2,"Cl(2)"),(4,"Cl(4)"),(8,"Cl(6)=G(6)"),(16,"Cl(8)"),(32,"Cl(10)"),(64,"Cl(12)"),(128,"Cl(14)"),(256,"Cl(16)")]:
    m=1
    while m<n: m*=3
    print(f"    M_{n:<3d} ({cl:12s}): max ord(U) = {m}")
print("  → r729 erst in M_256(GF(9)) = Cl(16).  In G(6) maximal r9 (unipotent).")
print("  → 729 hat mit GF(729) nichts zu tun: |GF(729)*| = 728. Die 728er-Struktur")
print("    ist halbeinfach (Eigenwerte), die 3^j-Struktur unipotent (Jordan) —")
print("    zwei verschiedene Mechanismen, die in der Jordan-Zerlegung X=S·U getrennt sind.")
print(f"  Maximale Gesamtordnung in G(6) mit 2-dim Jordan-Rest: 728·3 = 2184 (siehe C).")

# ============================================================
print(); print("="*66); print("(E) Dougs Zählungen = Euler-φ"); print("="*66)
print(f"  φ(80) = {sp.totient(80)}  (Doug: 32 von 80)")
print(f"  φ(182) = {sp.totient(182)}  (Doug: 72 von 182)")
assert sp.totient(80)==32 and sp.totient(182)==72
print("  → Anzahl der Generatoren (primitiven n-ten Wurzeln) in der zyklischen Gruppe ⟨X⟩")
print("    ist φ(n): X^m ist Generator ⟺ gcd(m,n)=1.  [K]")
print("  Ring ⟨X⟩ = {X^0,…,X^(n-1)} ≅ Z_n; das 'Spektrum' im engeren Sinn ist die")
print("  Eigenwertmenge von X (⊂ GF(3^k)), nicht die Potenzmenge — beides hängt zusammen,")
print("  ist aber nicht dasselbe.")

print("\nAlle Assertions bestanden.")
