#!/usr/bin/env python3
"""
pruef_341_inverse_minpoly.py
=============================
Inverse eines Multivektors über das Minimalpolynom; Ordnung kommutierender
Produkte (lcm); Konstruktion des nilpotenten M im Zentralisator von r182

Anlass: Doug Matzke, IPI-Mail 13. Sept. 2026, Fragen #1 und #4.

(A) Minimalpolynom aus den Potenzen: kleinstes k mit X^k ∈ span{1,X,…,X^(k-1)}
    über GF(9). Eigenwerte = Nullstellen. Invertierbar ⟺ c₀ ≠ 0 ⟺ 0 kein Eigenwert.
    1/X = -(X^(k-1) + c_(k-1) X^(k-2) + … + c₁)/c₀.
    Beispiel: X = 1+N (N²=0): m(x) = x²+x+1 = (x-1)² mod 3 → 1/X = -(X+1) = 1-N  [K]
    Gegenbeispiel: P = (1+e1)/2 idempotent: m(x) = x²-x, c₀=0 → nicht invertierbar [K]
    → Roots of unity: invertierbar; Nilpotente: nein; Idempotente ≠ 1: NEIN.
(B) ord(A·B) | lcm(ord A, ord B) für [A,B]=0: ord(U6·r182) = lcm(6,182) = 546,
    nicht 1092 (zwei kommutierende Elemente der Ordnung 2 erzeugen keine Ordnung 4) [K]
(C) M im Zentralisator von r182: Y hat auf dem 2-dim Komplement den doppelten
    Eigenwert +1; ker(Y-1) ist 2-dim; M: v2 ↦ v1, v1 ↦ 0, Bild(Y-1) ↦ 0.
    Dann M²=0, [M,Y]=0, (1+M)³=1 — Konstruktion, keine Suche [K]

Autor: Johann Pascher, ORCID 0009-0000-6518-4064 — 13. September 2026
"""
import numpy as np, sympy as sp
from itertools import combinations
class M9:
    def __init__(self, re, im=None):
        self.re=np.array(re,dtype=np.int64)%3
        self.im=np.zeros_like(self.re) if im is None else np.array(im,dtype=np.int64)%3
    @staticmethod
    def eye(n): return M9(np.eye(n,dtype=np.int64))
    @staticmethod
    def zeros(n): return M9(np.zeros((n,n),dtype=np.int64))
    def __matmul__(s,o): return M9(s.re@o.re-s.im@o.im, s.re@o.im+s.im@o.re)
    def __add__(s,o): return M9(s.re+o.re,s.im+o.im)
    def __sub__(s,o): return M9(s.re-o.re,s.im-o.im)
    def __neg__(s): return M9(-s.re,-s.im)
    def scal(s,a,b=0): return M9(a*s.re-b*s.im,a*s.im+b*s.re)
    def __eq__(s,o): return np.array_equal(s.re,o.re) and np.array_equal(s.im,o.im)
    def kron(s,o): return M9(np.kron(s.re,o.re)-np.kron(s.im,o.im),np.kron(s.re,o.im)+np.kron(s.im,o.re))
    def is_zero(s): return not s.re.any() and not s.im.any()
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
def build(terms):
    X=M9.zeros(8)
    for S,c in terms: X=X+blades[S].scal(c[0],c[1])
    return X
def real_rep(X): return np.block([[X.re,(3-X.im)%3],[X.im,X.re]])%3
def rref_mod3(A):
    A=np.array(A,dtype=np.int64)%3; m,n=A.shape; piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None: continue
        A[[r,p]]=A[[p,r]]; A[r]=(A[r]*(1 if A[r,c]==1 else 2))%3
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%3
        piv.append(c); r+=1
        if r==m: break
    return A,piv
def rank_mod3(A): return len(rref_mod3(A)[1])
def nullspace_mod3(A):
    A,piv=rref_mod3(A); n=A.shape[1]; free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        v=np.zeros(n,dtype=np.int64); v[f]=1
        for i,c in enumerate(piv): v[c]=(-A[i,f])%3
        out.append(v)
    return out
def vec(X): return np.concatenate([X.re.flatten(),X.im.flatten()])
def jmul(v): return np.concatenate([(3-v[8:])%3, v[:8]])

# ---------- GF(9)-lineare Abhängigkeit der Potenzen -> Minimalpolynom ----------
def minpoly(X):
    """liefert Koeffizienten c (Liste GF(9)-Paare) mit X^k + c[k-1]X^(k-1)+...+c[0] = 0, k minimal"""
    P=[M9.eye(8)]
    for k in range(1,17):
        P.append(P[-1]@X)
        # Suche a_0..a_{k-1} in GF(9) mit X^k = sum a_i X^i  (GF(9)-linear: Basis {X^i, j·X^i} über GF(3))
        cols=[]
        for i in range(k):
            cols.append(vec(P[i])); cols.append(vec(P[i].scal(0,1)))
        A=np.array(cols).T%3; b=vec(P[k])%3
        aug=np.hstack([A,b.reshape(-1,1)])
        R,piv=rref_mod3(aug)
        if A.shape[1] in piv: continue   # inkonsistent
        sol=np.zeros(A.shape[1],dtype=np.int64)
        for i,c in enumerate(piv): sol[c]=R[i,-1]
        coeffs=[]
        for i in range(k):
            a,b_=sol[2*i],sol[2*i+1]          # X^k = Σ (a+bj) X^i  → c_i = -(a+bj)
            coeffs.append(((-a)%3,(-b_)%3))
        return k,coeffs,P
    raise RuntimeError
def fc(c): r,i=c; return ({0:"",1:"+1",2:"-1"}[r]+{0:"",1:"+i",2:"-i"}[i]) or "0"
def gf9_inv(c):
    for a in range(3):
        for b in range(3):
            if (a,b)==(0,0): continue
            if ((a*c[0]-b*c[1])%3,(a*c[1]+b*c[0])%3)==(1,0): return (a,b)
def inverse_via_minpoly(X):
    k,c,P=minpoly(X)
    if c[0]==(0,0): return None,k,c
    # 1/X = -(X^(k-1) + c_{k-1} X^(k-2) + ... + c_1) / c_0
    S=P[k-1]
    for i in range(1,k): S=S+P[i-1].scal(*c[i])
    inv0=gf9_inv(c[0])
    return (-S).scal(*inv0),k,c

print("="*66); print("(A) Inverse über das Minimalpolynom"); print("="*66)
N=(e[0]+e[1]+e[2])@(e[0]@e[1]@e[2]); X=I8+N
inv,k,c=inverse_via_minpoly(X)
print(f"  X = 1+N (N²=0): Grad k={k}, m(x)= x^{k} "+" ".join(f"{fc(c[i])}·x^{i}" for i in range(k-1,-1,-1)))
print(f"  c₀ = {fc(c[0])} ≠ 0 → invertierbar;  1/X == 1-N: {inv==(I8-N)};  X·(1/X)==1: {(X@inv)==I8}")
assert inv==(I8-N)
P=(I8+e[0]).scal(2,0)
invP,kP,cP=inverse_via_minpoly(P)
print(f"  P=(1+e1)/2 idempotent (P²=P: {(P@P)==P}): m(x)= x^{kP} "+" ".join(f"{fc(cP[i])}·x^{i}" for i in range(kP-1,-1,-1)))
print(f"  c₀ = {fc(cP[0])} → NICHT invertierbar (Eigenwert 0)")
assert invP is None
Y=build([((0,1,2),(0,1)),((0,2,5),(2,0)),((1,2,3),(1,0)),((1,3,5),(2,0)),((3,4,5),(0,2)),((0,1,3,4),(2,0))])
invY,kY,cY=inverse_via_minpoly(Y)
print(f"  Y=r182: Minimalpolynom Grad {kY}, c₀={fc(cY[0])}; 1/Y == Y^181: {invY==mpow(Y,181)}")
assert invY==mpow(Y,181)
print("  → invertierbar ⟺ c₀≠0 ⟺ 0 kein Eigenwert. Roots of unity ja, Nilpotente nein, Idempotente≠1 NEIN.")

print(); print("="*66); print("(B) ord(A·B) | lcm für kommutierende A,B"); print("="*66)
# M aus (C) — erst konstruieren
D=Y-I8; Rr=real_rep(D)
ker=nullspace_mod3(Rr); v1=ker[0]
v2=next(cnd for cnd in ker[1:] if rank_mod3(np.array([v1,jmul(v1),cnd]))==3)
B=[v1,jmul(v1),v2,jmul(v2)]
for wcol in Rr.T:
    if len(B)==16: break
    if rank_mod3(np.array(B+[wcol]))==len(B)+1: B.append(wcol)
Bm=np.array(B).T%3
images=np.array([np.zeros(16,int),np.zeros(16,int),v1,jmul(v1)]+[np.zeros(16,int)]*12).T%3
Binv=np.array(sp.Matrix(Bm.tolist()).inv_mod(3).tolist(),dtype=np.int64)%3
Mr=(images@Binv)%3; M=M9(Mr[:8,:8],Mr[8:,:8])
assert (M@M).is_zero() and (M@Y-Y@M).is_zero()
U3=I8+M; U6=(-I8)+M
def order(X,nexp=2184):
    if not (mpow(X,nexp)==I8): return None
    nn=nexp
    for p in sp.factorint(nexp):
        while nn%p==0 and mpow(X,nn//p)==I8: nn//=p
    return nn
print(f"  ord(U6)={order(U6)}, ord(r182)={order(Y)}, lcm = {sp.ilcm(6,182)};  ord(U6·r182) = {order(U6@Y)}")
print(f"  ord(U3·r182) = {order(U3@Y)},  ord(U3·r182²) = {order(U3@mpow(Y,2))},  ord(U6·r182²) = {order(U6@mpow(Y,2))}")
assert order(U6@Y)==546 and order(U3@Y)==546 and order(U3@mpow(Y,2))==273
print("  → 1092 unmöglich: 2-Anteile von U6 und r182 haben je Ordnung 2; kommutierend → Produkt-2-Anteil ≤ 2.")

print(); print("="*66); print("(C) M-Konstruktion (Schritte)"); print("="*66)
print(f"  dim ker(Y-1) über GF(9) = {len(ker)//2}  (doppelter Eigenwert +1 auf dem 2-dim Komplement)")
print(f"  M: v2↦v1, v1↦0, Bild(Y-1)↦0  ⇒  M²=0: {(M@M).is_zero()},  [M,Y]=0: {(M@Y-Y@M).is_zero()},  (1+M)³=1: {mpow(U3,3)==I8}")
print("\nAlle Assertions bestanden.")
