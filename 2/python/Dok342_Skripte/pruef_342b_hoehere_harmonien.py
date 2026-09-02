"""
pruef_342b_hoehere_harmonien.py
Höhere GF(3^k)-Harmonische, Primzahl-Eintritt, Polynomklassen,
und Test: welche Massenverhältnisse sind Galois-Produkte?
"""
from math import gcd, isqrt
from fractions import Fraction
from itertools import product as iproduct, combinations_with_replacement
from collections import Counter

def factorize(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d]+=1; n//=d
        d += 1
    if n > 1: f[n]+=1
    return f

def phi(n):
    r = n
    for p in factorize(n): r = r//p*(p-1)
    return r

def fstr(f): return "·".join(f"{p}^{e}" if e>1 else f"{p}" for p,e in sorted(f.items()))

print("="*70)
print("TEIL A: GF(3^k)* — Ordnung, Primfaktoren, Eintritt neuer Primzahlen")
print("="*70)
seen = set()
rows = []
for k in range(1, 13):
    N = 3**k - 1
    f = factorize(N)
    new = sorted(set(f) - seen); seen |= set(f)
    z3ok = [p for p in f if p%3==1]
    nprim = phi(N)//k           # primitive Polynome vom Grad k
    nirr  = sum(  # Zahl irreduzibler Polys Grad k über GF(3) (Möbius)
        0 for _ in [0])  # placeholder
    rows.append((k, N, f, new, z3ok, nprim))
    print(f"k={k:2d}  |GF(3^{k})*|={N:7d} = {fstr(f):22s}  neu: {new}   prim.Polys Grad {k}: {nprim}")

print("""
Lesart (harmonisch):  k = Obertonnummer der Z₃-Windungsstruktur.
  k=1  → 2           Oktave
  k=2  → 8=2³        GF(9), Matzke Z3C
  k=3  → 26=2·13     GF(27): 13-limit  (Leptonen)
  k=4  → 80=2⁴·5     GF(81): 5-limit   (Quintschicht, Dougs G(3)-Ordnungen)
  k=5  → 242=2·11²   GF(243): 11-limit — 11 ist Neutrino-Prim (Dok.340)!
  k=6  → 728=2³·7·13 GF(729): 7- und 13-limit gemeinsam
  k=7  → 2186=2·1093 (1093 = Wieferich-Prim!) — keine kleine Harmonik
  k=8  → 6560=2⁵·5·41
  k=9  → 19682=2·13·757
  k=10 → 59048=2³·11²·61
  k=12 → 531440=2⁴·5·7·13·73
Beobachtung: Die kleinen Harmonik-Primen 5,7,11,13 treten in k=3..6 ALLE ein.
""")

# Erster Eintritt pro Primzahl
print("Erster Eintritt der harmonischen Primen p in GF(3^k)*:")
first = {}
for k,N,f,new,z3,npr in rows:
    for p in new: first[p]=k
for p in [2,5,7,11,13,17,19,23]:
    k = first.get(p)
    # Ordnung von 3 mod p = kleinstes k mit p | 3^k-1
    print(f"  p={p:2d}: k={k}   (= ord_p(3))   p≡{p%3} mod 3   Z₃-kompatibel: {p%3==1}")
print("Regel [B]: p tritt bei k = ord_p(3) ein (multiplikative Ordnung von 3 mod p).")
print("           p≡1 mod 3 ⇔ Z₃ ⊂ GF(p)*  ⇔ k | (p−1)/... (Quadratwurzel-Kriterium hier nicht nötig)")

print()
print("="*70)
print("TEIL B: Irreduzible/primitive Polynome je Grad (Möbius-Formel)")
print("="*70)
def mobius(n):
    f = factorize(n)
    if any(e>1 for e in f.values()): return 0
    return (-1)**len(f)
for k in range(1,9):
    nirr = sum(mobius(d)*3**(k//d) for d in range(1,k+1) if k%d==0)//k
    npr  = phi(3**k-1)//k
    print(f"  Grad {k}: irreduzibel={nirr:5d}   primitiv={npr:5d}   Anteil prim {npr/nirr:.2f}")
print("  → Grad 3: 8 irreduzibel, 4 primitiv (Dok.342a bestätigt). Grad 6: 116 irreduzibel, 48 primitiv.")

print()
print("="*70)
print("TEIL C: 'Akkorde' — Elementordnungen in G(6)=M_8(GF(9)) sind kgV von Teilern")
print("="*70)
# In M_8(GF(9)) ist χ ein Produkt irreduzibler Polys über GF(9), Grade summieren zu 8.
# Halbeinfache Ordnungen: kgV der Ordnungen der Wurzeln, Wurzel-Ordnung teilt 9^d-1.
# Über GF(3)-Polynome: Grade d summieren zu 8, Wurzeln in GF(3^d).
possible = set()
def parts(n, maxd):
    if n==0: yield []; return
    for d in range(min(n,maxd),0,-1):
        for rest in parts(n-d, d): yield [d]+rest
for P in parts(8,8):
    # jede Wurzel-Ordnung teilt 3^d - 1; kgV über die Teile → Maximalordnung
    from math import lcm
    m = 1
    for d in P: m = lcm(m, 3**d-1)
    possible.add((tuple(P), m))
# maximale halbeinfache Ordnung über GF(3) in GL_8
maxord = max(m for _,m in possible)
print("Partitionen von 8 (Grade der GF(3)-Faktoren) → maximale halbeinfache Ordnung:")
for P,m in sorted(possible, key=lambda x:-x[1])[:10]:
    print(f"  {str(P):28s} kgV(3^d−1) = {m:8d} = {fstr(factorize(m))}")
print(f"\nGrößte: {maxord} = {fstr(factorize(maxord))}  (Partition (8) → GF(6561)*)")
print("Harmonisch: Partition = Akkord aus Obertönen k∈P; Ordnung = gemeinsame Periode.")
print("  (3,3,1,1): 26   Dok.341 (reiner GF(27)-Akkord)")
print("  (6,2)    : kgV(728,8)=728   GF(729)+GF(9): 7·13-Akkord")
print("  (5,3)    : kgV(242,26)=3146=2·11²·13: Neutrino-11 mit Lepton-13")
print("  (4,3,1)  : kgV(80,26,2)=1040=2⁴·5·13: Quint-5 mit Lepton-13")

print()
print("="*70)
print("TEIL D: Sind weitere Massenverhältnisse Galois-Produkte? (offener Test)")
print("="*70)
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
mu, md, ms, mc, mb, mt = 2.16, 4.70, 93.5, 1273., 4183., 172570.  # MeV, PDG-artig
print("Vorlage [K] Dok.338: (m_μ/m_e)² = 43200 = 8²·5²·27 = |GF9*|²·5²·|GF27|")
print(f"   numerisch: {(mmu/me)**2:.1f}\n")

# Bausteine: Ordnungen & Körpergrößen aus GF(3^k), k≤6, plus 5,7,11,13 einzeln
blocks = {"|GF3*|=2":2,"|GF9*|=8":8,"|GF9|=9":9,"|GF27*|=26":26,"|GF27|=27":27,
          "|GF81*|=80":80,"|GF81|=81":81,"|GF243*|=242":242,"|GF729*|=728":728,
          "5":5,"7":7,"11":11,"13":13,"3":3}
names = list(blocks); vals = [blocks[n] for n in names]
targets = {"(m_τ/m_μ)²":(mtau/mmu)**2, "(m_τ/m_e)²":(mtau/me)**2,
           "m_τ/m_μ":mtau/mmu, "m_τ/m_e":mtau/me, "m_μ/m_e":mmu/me,
           "m_t/m_c":mt/mc, "m_c/m_u":mc/mu, "m_b/m_s":mb/ms, "m_s/m_d":ms/md,
           "(m_t/m_b)":mt/mb}
print("Suche: Produkte/Quotienten von ≤3 Bausteinen (Exponent −1..+2), Toleranz 0,5%")
print("Achtung [S]: Look-elsewhere — bei ~10⁴ Kombinationen sind Zufallstreffer bei 0,5% ERWARTET.")
import itertools
combos = []
for r in (1,2,3):
    for idx in itertools.combinations(range(len(vals)), r):
        for exps in itertools.product((-1,1,2), repeat=r):
            v = 1.0; lab=[]
            for i,e in zip(idx,exps):
                v *= vals[i]**e; lab.append(f"{names[i]}^{e}" if e!=1 else names[i])
            combos.append((v," · ".join(lab)))
print(f"Kombinationen: {len(combos)}")
for tname,t in targets.items():
    hits = [(abs(v/t-1),v,lab) for v,lab in combos if abs(v/t-1)<0.005]
    hits.sort()
    print(f"\n  {tname} = {t:.4f}   Treffer: {len(hits)}")
    for dev,v,lab in hits[:4]:
        print(f"     {lab:45s} = {v:.4f}  ({dev*100:.2f}%)")

print("""
Einordnung: Die Trefferzahl pro Ziel bei 0,5 % zeigt die Zufallsrate.
Ein Treffer ist nur dann [K]-Kandidat, wenn er (a) mit ≤2 Bausteinen,
(b) mit Exponent ≤1 und (c) ≤0,05 % auskommt UND geometrisch begründbar ist
(wie 43200 in Dok.338 über ξ). Alles andere bleibt [S].
""")

# Schärferer Test für Tau
print("Schärfer (0,05 %) für den Tau-Sektor:")
for tname in ["(m_τ/m_μ)²","(m_τ/m_e)²","m_τ/m_μ","m_τ/m_e"]:
    t=targets[tname]
    hits=sorted([(abs(v/t-1),v,lab) for v,lab in combos if abs(v/t-1)<0.0005])
    print(f"  {tname}={t:.4f}: {len(hits)} Treffer", *[f"\n     {lab} = {v:.4f} ({d*100:.3f}%)" for d,v,lab in hits[:3]])

print()
print("="*70)
print("TEIL E: Koide-Check im Galois-Bild")
print("="*70)
Q = (me+mmu+mtau)/(( me**0.5+mmu**0.5+mtau**0.5)**2)
print(f"Koide Q = {Q:.6f}  (2/3 = {2/3:.6f}, Abw. {abs(Q-2/3)/(2/3)*100:.4f} %)")
print("2/3 = |GF(3)*| / 3 = (Fixpunkte)/(Charakteristik)  — Z₃-Trialität, Dok.159 (1/3-Schritte)")
print("Im GF(3)-Bild: 2/3 = 1 − 1/3 = Anteil der Nicht-Null-Elemente von GF(3).  [B trivial, Deutung S]")
