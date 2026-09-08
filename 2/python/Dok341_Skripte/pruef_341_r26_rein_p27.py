#!/usr/bin/env python3
"""
pruef_341_r26_rein_p27.py
==========================
Dougs Einwand gegen r26 (Signatur-Mischung), reine Koeffizienten,
p27-Projektoren als Körperturm-Hierarchie, und die X7-Diskrepanz

Anlass: Doug Matzke, IPI-Mails 7. Sept. 2026:
  (1) "p27 satisfies X^27 = X — a direct generalization of tripotents"
  (2) "r26 contains BOTH -(e1^e2) AND -j·(e1^e2) via -(1+j)·(e1^e2).
       This mixes two signature configurations ... structurally artificial."
  (3) Mein X7 (root7) ergab bei Doug p27**27 == p27, aber p27**n != 1 —
      also NICHT das von mir berechnete Element.

ERGEBNISSE:

(A) 1+j ist Generator von GF(9)* (Ordnung 8, Norm -1) — Dougs eigener
    Generator (a+ja)^8=1 mit a=1. -(1+j)·B ist Skalar·Blade. [K]

(B) Dougs Signatur-Lesart: (e1^e2)²=-1, (j·e1^e2)²=+1. Daraus folgt eine
    PHYSIKALISCHE Reinheitsforderung: Blade-Koeffizient ∈ {±1} ∪ {±j},
    nie a+bj mit a,b≠0. Das ist keine algebraische Einschränkung. [B]

(C) root26 mit REINEN Koeffizienten existiert reichlich (5 Blades: ~2.4%).
    Festes Beispiel: X = i·e3 + i·e2e5 + i·e3e6 + e4e6 + e3e5e6, ord=26. [B]
    → Dougs Reinheitskriterium ist erfüllbar; r26 war nur ein gemischter Vertreter.

(D) X7 (Companion φ_7 ⊕ I₂) hat 0 gemischte Koeffizienten — bereits rein. [K]

(E) X^27 = X ⟺ Spektrum ⊂ GF(27)  (x^27-x = ∏_{a∈GF(27)}(x-a)).
    Körperturm-Hierarchie: X^3=X (GF(3)) ⊂ X^9=X (GF(9)) ⊂ X^27=X (GF(27))
    ⊂ X^729=X (GF(729)). N: ab X^3. r26: ab X^27. X7: erst X^729 (7∤26). [K]

(F) DISKREPANZ AUFGEKLÄRT: Doug definiert E7 = -(e1^...^e6).
    Mein Term "(+i)·E7" meinte +i·e1…e6; mit Dougs E7 wird das Vorzeichen
    des Pseudoskalar-Terms umgedreht → anderes Element X7' mit
    X7'^7 ≠ 1, aber X7'^27 = X7' — exakt Dougs Befund. [K]
    Korrektur für GALG: letzter Term muss (-1j)*E7 lauten (Dougs E7).

(G) root7 aus beliebigem Y mit 7 | ord(Y): X = Y^(ord(Y)/7) hat Ordnung 7.
    Liefert weitere, teils sparsamere root7-Kandidaten mit reinen Koeff. [B]

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 8. September 2026
"""
import numpy as np, sympy as sp, random
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
def galg(X):
    return " ".join(f"({fc(c)})*{fb(S)}" for S,c in sorted(coeffs(X).items(), key=lambda t:(len(t[0]),t[0])))
def build(terms):
    X=M9.zeros(8)
    for S,c in terms: X=X+blades[S].scal(c[0],c[1])
    return X
N_EXP=1
for k in range(1,9): N_EXP=int(sp.ilcm(N_EXP,3**k-1))
N_EXP*=9
N_FAC=sp.factorint(N_EXP)
def order_m9(X):
    if not (mpow(X,N_EXP)==I8): return None
    nn=N_EXP
    for p in N_FAC:
        while nn%p==0 and mpow(X,nn//p)==I8: nn//=p
    return nn
def n_mixed(X): return sum(1 for c in coeffs(X).values() if c[0]!=0 and c[1]!=0)

# ============================================================
print("="*66); print("(A) 1+j in GF(9)"); print("="*66)
def gf9_mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
u=(1,1); p=(1,0); ordu=None
for k in range(1,9):
    p=gf9_mul(p,u)
    if p==(1,0): ordu=k; break
print(f"  ord(1+j) in GF(9)* = {ordu} = |GF(9)*|  → Generator (Dougs (a+ja)^8=1)")
print(f"  Norm(1+j) = 1-j² = 2 = -1 (mod 3)")
assert ordu==8

# ============================================================
print(); print("="*66); print("(B) Signatur-Lesart"); print("="*66)
B=blades[(0,1)]; jB=B.scal(0,1)
assert (B@B)==(-I8) and (jB@jB)==I8
print("  (e1^e2)² = -1,   (j·e1^e2)² = +1   [B]")
print("  Dougs Forderung 'rein': Koeffizient ∈ {±1}∪{±j}, nicht a+bj (a,b≠0).")

# ============================================================
print(); print("="*66); print("(C) root26 mit reinen Koeffizienten"); print("="*66)
rng=random.Random(2026); blist=list(blades.keys()); pure=[(1,0),(2,0),(0,1),(0,2)]
stat={}
for supp in (5,6,7):
    hits=0
    for _ in range(3000):
        X=build([(S,rng.choice(pure)) for S in rng.sample(blist,supp)])
        if mpow(X,26)==I8 and not (mpow(X,13)==I8) and not (mpow(X,2)==I8): hits+=1
    stat[supp]=hits
    print(f"  Support {supp}: {hits}/3000 Elemente mit Ordnung exakt 26 (reine Koeff.)")
assert stat[5]>0
# Festes Beispiel (aus Suche, Seed 2026, Lauf 8.9.2026)
X26p = build([((2,),(0,1)),((1,4),(0,1)),((2,5),(0,1)),((3,5),(1,0)),((2,4,5),(1,0))])
print(f"\n  Festes reines Beispiel:  X = {galg(X26p)}")
o=order_m9(X26p)
print(f"  ord = {o},  gemischte Koeffizienten: {n_mixed(X26p)}")
assert o==26 and n_mixed(X26p)==0
print("  GALG-Check: X = (1j)*e3 + (1j)*(e2^e5) + (1j)*(e3^e6) + (e4^e6) + (e3^e5^e6);  X**26==1, X**13!=1")

# ============================================================
print(); print("="*66); print("(D) X7 rein?"); print("="*66)
C=np.zeros((6,6),dtype=np.int64)
for i in range(5): C[i+1,i]=1
C[:,5]=[2]*6
X7=M9.zeros(8); X7.re[0:6,0:6]=C; X7.re[6,6]=1; X7.re[7,7]=1
assert order_m9(X7)==7
print(f"  X7: ord={order_m9(X7)}, {len(coeffs(X7))} Blades, gemischte Koeff.: {n_mixed(X7)}  → rein [K]")

# ============================================================
print(); print("="*66); print("(E) X^q = X ⟺ Spektrum ⊂ GF(q)"); print("="*66)
r26=build([((0,1),(2,2)),((0,1,2,5),(1,1)),((0,1,4,5),(1,2)),((0,3,4,5),(1,1)),((0,1,2,3,5),(2,0))])
N=blades[(0,2)].scal(0,2)+blades[(1,5)].scal(0,2)+blades[(3,4)].scal(0,2)
rows={}
for nm,X in [("N",N),("r26",r26),("X26p",X26p),("X7",X7)]:
    rows[nm]={q:(mpow(X,q)==X) for q in (3,9,27,81,729)}
    print(f"  {nm:5s}: " + "  ".join(f"X^{q}=X:{'✓' if rows[nm][q] else '✗'}" for q in (3,9,27,81,729)))
assert rows["N"][3] and rows["r26"][27] and not rows["r26"][9]
assert rows["X7"][729] and not rows["X7"][27]
print("  → p27 = Spektrum in GF(27); Tripotent = Spektrum in GF(3); X7 braucht GF(729) (7∤26).")

# ============================================================
print(); print("="*66); print("(F) Diskrepanz: Dougs E7 = -(e1^...^e6)"); print("="*66)
cs=coeffs(X7); E7=(0,1,2,3,4,5)
print(f"  Mein X7 hat Pseudoskalar-Term ({fc(cs[E7])})·e1…e6 ; ich schrieb '(+i)·E7'.")
print(f"  Doug: E7 = -(e1^…^e6)  →  er setzt (+i)·(-e1…e6) = (-i)·e1…e6 ein.")
X7d = X7 - blades[E7].scal(*cs[E7]) + blades[E7].scal(cs[E7][0]*2%3, cs[E7][1]*2%3)  # Vorzeichen des E7-Terms gedreht
od=order_m9(X7d)
print(f"  X7' (E7-Term negiert): X7'^7=1: {mpow(X7d,7)==I8},  X7'^27=X7': {mpow(X7d,27)==X7d},  ord={od}")
print(f"  X7'^n = 1 für n≤27: {any(mpow(X7d,n)==I8 for n in range(1,28))}")
assert not (mpow(X7d,7)==I8) and mpow(X7d,27)==X7d
print("  → EXAKT Dougs Befund (p27**27==p27, kein p27**n==1). Diskrepanz = E7-Konvention. [K]")
print("  Korrekte GALG-Eingabe des letzten Terms: (-1j)*E7   [mit Dougs E7 = -(e1^…^e6)]")

# ============================================================
print(); print("="*66); print("(G) root7 aus Y mit 7 | ord(Y)"); print("="*66)
rng=random.Random(7)
best=None
for supp in (6,8,10,12):
    for _ in range(1200):
        Y=build([(S,rng.choice(pure)) for S in rng.sample(blist,supp)])
        o=order_m9(Y)
        if o and o%7==0:
            X=mpow(Y,o//7)
            assert order_m9(X)==7
            key=(n_mixed(X),len(coeffs(X)))
            if best is None or key<best[0]: best=(key,X,Y,supp,o)
if best:
    (nm_,nb),X,Y,supp,o=best
    print(f"  Y mit {supp} reinen Blades, ord(Y)={o};  X=Y^{o//7}: ord 7, {nb} Blades, gemischt: {nm_}")
    print(f"  Y = {galg(Y)}")
    print(f"  X = Y**{o//7} = {galg(X)}")
    print(f"  X**7 == 1: {mpow(X,7)==I8},  X**1 == 1: {mpow(X,1)==I8}")
    print(f"  ord(Y) = {o} = {dict(sp.factorint(o))}  (7 und 13 gemeinsam: Y lebt in GF(729)*)")
    # Festes Beispiel (Seed 7) als Assertion sichern
    Yfix = build([((0,1,2),(0,1)),((0,2,5),(2,0)),((1,2,3),(1,0)),((1,3,5),(2,0)),((3,4,5),(0,2)),((0,1,3,4),(2,0))])
    assert order_m9(Yfix)==182 and order_m9(mpow(Yfix,26))==7 and n_mixed(mpow(Yfix,26))==0
    print("  [OK] Festes Beispiel: Y (6 reine Blades), ord 182; X=Y**26, ord 7, rein")
    assert order_m9(X)==7
print("\nAlle Assertions bestanden.")
