#!/usr/bin/env python3
"""
pruef_341_vakuum_witt_z3.py
============================
Dougs Vakuum-Struktur Vss[0..5] in Cl(6) über GF(9):
Witt-Paare, Zahloperator N, Z3-Trennung gerade/ungerade, Bilaterale

Anlass: Doug Matzke, IPI-Mail 1. Sept. 2026 (22:05):
  - Verifiziert das 5-Blade-Element X**26==1 aus pruef_341/Dok. 341
  - Zeigt 6 Vakua Vss[0..5]: gerade [0,2,4] Kandidat 3 Fermion-Generationen,
    ungerade [1,3,5] Kandidat dark energy/mass
  - Grade-2-Summen: gerade Vakua tragen -i-Koeffizienten, ungerade +i
  - N = (-i·e1^e3)+(-i·e2^e6)+(-i·e4^e5) ist Zahloperator UND Konstruktor:
    (1+N)(1+jE7) == Vss[0]
  - Frage: Gluon-Quark-Transmutation via Bilaterale ap_i*ap_j

ERGEBNISSE (alle numerisch verifiziert):

(A) Konstruktor-Identität [B]:
    In unserer Gamma-Konvention gilt (1+N)(1-jE7) = Vss[0] exakt.
    Das Vorzeichen des Pseudoskalars ist reine Basiskonvention
    (Orientierung von E7); Dougs Identität ist bestätigt.

(B) Witt-Paar-Struktur [B]:
    B1=-i·e1e3, B2=-i·e2e6, B3=-i·e4e5:
    B_k² = +1, paarweise kommutierend, [B_k, jE7]=0.
    Die drei Paare {13},{26},{45} = drei kommutierende Involutionen
    = Cl(6)-Zerlegung in drei komplexe Ebenen (Fock-Raum von 3 Moden).

(C) TRIALITY IST IN Z3C EINGEBAUT [B] — Kernbefund 1:
    Über C hätte N=B1+B2+B3 Eigenwerte {-3,-1,+1,+3}.
    Über GF(9) (Charakteristik 3): -3 ≡ 0 ≡ +3.
    Vakuum (n=0) und Vollzustand (n=3) FALLEN ZUSAMMEN.
    N mod 3 ∈ {0,+1,-1} = FFGFT-Sektoren Δw (Dok. 336: Q_Z3 = N mod 3).
    Eigenraum-Multiplizitäten über GF(9): dim{0}=2, dim{+1}=3, dim{-1}=3.
    Der +1-Eigenraum (Dim 3) = Kandidat 3 Fermion-Generationen.

(D) Z3-TRENNUNG DER VAKUA [B] — Kernbefund 2:
    Die zyklische Witt-Paar-Rotation sigma = (1→2→4)(3→6→5)
    (B1→B2→B3→B1, E7 invariant) wirkt auf die 6 Vakua:
      sigma(Vss[0])=Vss[0], sigma(Vss[2])=Vss[2], sigma(Vss[4])=Vss[4]
      sigma(Vss[1])=Vss[3], sigma(Vss[3])=Vss[5], sigma(Vss[5])=Vss[1]
    GERADE VAKUA = Z3-FIXPUNKTE (einzeln invariant)
    UNGERADE VAKUA = EIN Z3-DREIER-ORBIT
    Das ist strukturell exakt die Frobenius-Trennung aus Dok. 339:
    Fixpunkte = massiver Sektor (Fermion-Generationen [0,2,4]),
    Dreier-Orbit = anderer Sektor (Dougs Dark-Kandidat [1,3,5]).
    Dougs Grade-Paritäts-Aufteilung fällt mit der Z3-Orbitstruktur zusammen.

(E) BILATERALE = SEKTORWECHSLER [B] — Antwort auf Dougs Gluon-Frage:
    ap_i = Witt-Raiser (e_a + i·e_b)/2 der drei Ebenen.
    ap1·ap2 = -(Dougs ap1*ap2) — identisch bis Skalar.
    [N, ap_i·ap_j] = +1·(ap_i·ap_j)  (über C wäre es +2 ≡ -1 mod 3;
    Vorzeichen konventionsabhängig).
    Die Bilaterale verschieben den N-Sektor um ±1 mod 3 = Δw-Wechsler —
    exakt die Rolle der Gluonen in Dok. 339 (Dreier-Orbits).

(F) Konjugation gerade/ungerade [offen]:
    Einfache i→-i-Konjugation bildet Vss[0]→Vss[5] NICHT ab; Dougs
    ±i-Beobachtung gilt für die Grade-2-Teile, die Grade-4-Vorzeichen
    unterscheiden sich zusätzlich. Volle Abbildung = Konjugation +
    Zusatzoperation (Konvention, sekundär).

(G) Projektor-Eigenschaften [B]:
    Vss[0]² = -Vss[0]  (d.h. -Vss[0] = 2·Vss[0] ist idempotent über GF(9))
    N·Vss[0] = 0  — Vss[0] projiziert auf den N=0-Sektor (Vakuum+Vollzustand).

Autor: Johann Pascher, ORCID 0009-0000-6518-4064
Datum: 2. September 2026
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
    def __matmul__(self, o):
        return M9(self.re @ o.re - self.im @ o.im, self.re @ o.im + self.im @ o.re)
    def __add__(self, o): return M9(self.re + o.re, self.im + o.im)
    def __sub__(self, o): return M9(self.re - o.re, self.im - o.im)
    def __neg__(self): return M9(-self.re, -self.im)
    def scal(self, a, b=0): return M9(a*self.re - b*self.im, a*self.im + b*self.re)
    def __eq__(self, o): return np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im)
    def kron(self, o):
        return M9(np.kron(self.re,o.re)-np.kron(self.im,o.im),
                  np.kron(self.re,o.im)+np.kron(self.im,o.re))
    def trace(self): return (int(np.trace(self.re))%3, int(np.trace(self.im))%3)
    def is_zero(self): return not self.re.any() and not self.im.any()

def mpow(X,k):
    R=M9.eye(X.re.shape[0]); B=X
    while k:
        if k&1: R=R@B
        B=B@B; k>>=1
    return R

# Cl(6)-Erzeuger (Pauli-Tensoren), e_i²=+1
I2=M9.eye(2)
sx=M9([[0,1],[1,0]]); sy=M9([[0,0],[0,0]],[[0,2],[1,0]]); sz=M9([[1,0],[0,2]])
e=[sx.kron(I2).kron(I2), sy.kron(I2).kron(I2), sz.kron(sx).kron(I2),
   sz.kron(sy).kron(I2), sz.kron(sz).kron(sx), sz.kron(sz).kron(sy)]
I8=M9.eye(8)

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
def fc(c):
    r,i=c
    s={0:"",1:"+1",2:"-1"}[r]; t={0:"",1:"+i",2:"-i"}[i]
    return (s+t) if (s or t) else "0"
def fb(S): return "1" if not S else "^".join(f"e{x+1}" for x in S)
def build(terms):
    X=M9.zeros(8)
    for S,c in terms: X=X+blades[S].scal(c[0],c[1])
    return X

mj=(0,2); pj=(0,1); p1=(1,0); m1=(2,0)

# Dougs 6 Vakua (IPI-Mail 1. Sept. 2026, Indizes 0-basiert)
Vss = [
 build([((),p1),((0,2),mj),((1,5),mj),((3,4),mj),((0,1,2,5),p1),((0,2,3,4),m1),((1,3,4,5),m1),((0,1,2,3,4,5),mj)]),
 build([((),p1),((0,2),pj),((1,4),pj),((3,5),pj),((0,1,2,4),p1),((0,2,3,5),m1),((1,3,4,5),p1),((0,1,2,3,4,5),mj)]),
 build([((),p1),((0,4),mj),((1,2),mj),((3,5),mj),((0,1,2,4),m1),((0,3,4,5),p1),((1,2,3,5),m1),((0,1,2,3,4,5),mj)]),
 build([((),p1),((0,4),pj),((1,5),pj),((2,3),mj),((0,1,4,5),p1),((0,2,3,4),p1),((1,2,3,5),p1),((0,1,2,3,4,5),mj)]),
 build([((),p1),((0,5),mj),((1,4),mj),((2,3),pj),((0,1,4,5),m1),((0,2,3,5),p1),((1,2,3,4),p1),((0,1,2,3,4,5),mj)]),
 build([((),p1),((0,5),pj),((1,2),pj),((3,4),pj),((0,1,2,5),m1),((0,3,4,5),m1),((1,2,3,4),m1),((0,1,2,3,4,5),mj)]),
]

print("="*66)
print("(A) Konstruktor-Identität")
print("="*66)
N  = blades[(0,2)].scal(0,2) + blades[(1,5)].scal(0,2) + blades[(3,4)].scal(0,2)
E7 = blades[(0,1,2,3,4,5)]
hit = None
for sN,nm in [((1,0),"+N"),((2,0),"-N")]:
    for sE,em in [((0,1),"+jE7"),((0,2),"-jE7")]:
        if (I8 + N.scal(*sN)) @ (I8 + E7.scal(*sE)) == Vss[0]:
            hit=(nm,em)
print(f"  (1{hit[0][0]}N)(1{hit[1][0]}jE7) == Vss[0]  [in unserer Gamma-Konvention: {hit[0]}, {hit[1]}]")
print(f"  → Dougs Identität (1+N)(1+jE7)=Vss[0] bestätigt; Pseudoskalar-")
print(f"    Orientierung ist Basiskonvention.  [B]")
assert hit is not None

print()
print("="*66)
print("(B) Witt-Paar-Struktur")
print("="*66)
B1 = blades[(0,2)].scal(0,2); B2 = blades[(1,5)].scal(0,2); B3 = blades[(3,4)].scal(0,2)
jE7 = E7.scal(0,1)
assert mpow(B1,2)==I8 and mpow(B2,2)==I8 and mpow(B3,2)==I8
assert (B1@B2-B2@B1).is_zero() and (B1@B3-B3@B1).is_zero() and (B2@B3-B3@B2).is_zero()
assert (B1@jE7-jE7@B1).is_zero()
print("  B1²=B2²=B3²=+1, paarweise kommutierend, [B_k,jE7]=0  [B]")
print("  Drei Witt-Paare {13},{26},{45} = Fock-Raum von 3 Moden in Cl(6)")

print()
print("="*66)
print("(C) Triality in Z3C: N-Eigenwerte mod 3")
print("="*66)
mult = {}
for lam,name in [((0,0),"0"),((1,0),"+1"),((2,0),"-1")]:
    M = N - I8.scal(lam[0],lam[1])
    R = np.block([[M.re,(3-M.im)%3],[M.im,M.re]]) % 3
    rank = sp.Matrix(R.tolist()).rank(iszerofunc=lambda x: x % 3 == 0)
    mult[name] = (16-rank)//2
    print(f"  Eigenwert {name}: Multiplizität {mult[name]}")
assert mult == {"0":2, "+1":3, "-1":3}
print("  Über C wären es {-3,-1,+1,+3}; über GF(9): -3≡0≡+3 —")
print("  Vakuum und Vollzustand fallen zusammen, N mod 3 = Δw  [B]")
print("  dim(+1-Eigenraum) = 3 = Kandidat 3 Fermion-Generationen")

print()
print("="*66)
print("(D) Z3-Trennung: sigma=(1→2→4)(3→6→5) auf den Vakua")
print("="*66)
sigma = {0:1, 2:5, 1:3, 5:4, 3:0, 4:2}
def perm_blade(S):
    img=[sigma[s] for s in S]; T=tuple(sorted(img)); a=list(img); sg=1
    for i2_ in range(len(a)):
        for j2_ in range(i2_+1,len(a)):
            if a[i2_]>a[j2_]: a[i2_],a[j2_]=a[j2_],a[i2_]; sg=-sg
    return T,sg
def apply_sigma(X):
    Y=M9.zeros(8)
    for S,c in coeffs(X).items():
        T,sg = perm_blade(S)
        Y = Y + blades[T].scal(c[0]*sg%3, c[1]*sg%3)
    return Y
# B-Zyklus
for nm,S,expect in [("B1",(0,2),"e2^e6"),("B2",(1,5),"e4^e5"),("B3",(3,4),"e1^e3")]:
    T,sg = perm_blade(S)
    assert fb(T)==expect and sg>0
print("  sigma: B1→B2→B3→B1 (zyklisch), E7 invariant  [B]")
mapping = {}
for a in range(6):
    sVa = apply_sigma(Vss[a])
    for b in range(6):
        if sVa == Vss[b]: mapping[a]=b
print(f"  Wirkung auf Vakua: {mapping}")
assert mapping[0]==0 and mapping[2]==2 and mapping[4]==4
assert mapping[1]==3 and mapping[3]==5 and mapping[5]==1
print("  GERADE Vakua [0,2,4]: Z3-FIXPUNKTE (einzeln invariant)")
print("  UNGERADE Vakua [1,3,5]: EIN Z3-DREIER-ORBIT  [B]")
print("  = Frobenius-Trennung Dok. 339: Fixpunkte↔massiv, Orbit↔anderer Sektor")

print()
print("="*66)
print("(E) Bilaterale = Sektorwechsler")
print("="*66)
ap1 = (e[0] + e[2].scal(0,1)).scal(2,0)   # (e1+i·e3)/2
ap2 = (e[3] + e[4].scal(0,1)).scal(2,0)   # (e4+i·e5)/2
ap3 = (e[1] + e[5].scal(0,1)).scal(2,0)   # (e2+i·e6)/2
doug12 = build([((0,3),m1),((0,4),mj),((2,3),mj),((2,4),p1)])
P12 = ap1@ap2
prop=None
for a_ in range(3):
    for b_ in range(3):
        if (a_,b_)!=(0,0) and P12.scal(a_,b_)==doug12: prop=(a_,b_)
assert prop is not None
print(f"  ap1·ap2 = ({fc(prop)})·(Dougs ap1*ap2) — identisch bis Skalar  [B]")
for nm,P in [("ap1·ap2",P12),("ap1·ap3",ap1@ap3),("ap2·ap3",ap2@ap3)]:
    K = N@P - P@N
    hit=None
    for a_ in range(3):
        for b_ in range(3):
            if (a_,b_)!=(0,0) and P.scal(a_,b_)==K: hit=(a_,b_)
    assert hit==(1,0)
    print(f"  [N, {nm}] = (+1)·({nm})")
print("  → Bilaterale verschieben N-Sektor um ±1 mod 3 = Δw-Wechsler")
print("  = Gluon-Rolle aus Dok. 339 (Dreier-Orbits)  [B]")

print()
print("="*66)
print("(F) Konjugation gerade/ungerade [offen]")
print("="*66)
def conj(X): return M9(X.re, (3-X.im)%3)
any_conj = any(conj(Vss[a])==Vss[b] for a in range(6) for b in range(6) if a!=b)
print(f"  Einfache i→-i-Konjugation bildet kein Vakuum auf ein anderes ab: {not any_conj}")
print("  Dougs ±i-Beobachtung gilt für Grade-2-Teile; volle Abbildung braucht")
print("  Konjugation + Zusatzoperation (Konvention, sekundär)")

print()
print("="*66)
print("(G) Projektor-Eigenschaften")
print("="*66)
V0 = Vss[0]
assert (V0@V0) == V0.scal(2,0)
print("  Vss[0]² = -Vss[0]  → -Vss[0] ist idempotent über GF(9)  [B]")
assert (N@V0).is_zero()
print("  N·Vss[0] = 0  → Projektion auf N=0-Sektor (Vakuum+Vollzustand)  [B]")

print()
print("="*66)
print("ZUSAMMENFASSUNG")
print("="*66)
print("""  1. Dougs Konstruktor-Identität bestätigt (Pseudoskalar-Vorzeichen=Konvention)
  2. Triality ist in Z3C eingebaut: N mod 3 = Δw, Vakuum≡Vollzustand
  3. Gerade Vakua = Z3-Fixpunkte, ungerade = Z3-Dreier-Orbit
     (= Frobenius-Trennung Dok. 339, massiv vs. anderer Sektor)
  4. Bilaterale ap_i·ap_j = Δw-Wechsler (Gluon-Rolle)
  5. Vss[0] = Projektor auf N=0

  Alle Assertions bestanden.""")
