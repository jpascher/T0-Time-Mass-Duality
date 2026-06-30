#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ikosaeder_winkel_2_9.py  --  ist theta=2/9 ein Ikosaeder-Achsenwinkel?
======================================================================
Stand: theta ist angular; alle FFGFT-Werkzeuge sind radial. Das angulare Prinzip
soll (Dok 283 §8) mit HLVs schief-adjungierter dynamischer Phase R zu tun haben.
Dok 283: FFGFTs 3-Zaehligkeit (C3) und HLVs 5-Zaehligkeit (C5) leben BEIDE in der
Ikosaedergruppe A5 (C3<A5: 120°-Achse + 72°-Achse). HLVs eigener Z3-Zirkulant ist
REELL (theta=0, r=2/sqrt5); FFGFTs hat theta=2/9.

PRINCIPLED FRAGE: ist theta=2/9 rad (oder ein einfaches Vielfaches/Differenz) ein
GEOMETRISCHER Winkel zwischen Ikosaeder-Symmetrieachsen -- der gemeinsamen 3-5-
Buehne? Ein solcher Winkel waere angular, FEST (durch A5), und transzendent --
genau die gesuchte Art Prinzip. STRENG geprueft: 'nah dran' zaehlt NICHT.

numpy-only, seed=20780458.
"""
import numpy as np
from itertools import combinations
np.random.seed(20780458)
phi = (1+np.sqrt(5))/2
DEG = 180/np.pi
theta29 = 2/9.0
print("="*74)
print("IST theta=2/9 rad EIN IKOSAEDER-ACHSENWINKEL? (streng geprueft)")
print(f"  theta=2/9 = {theta29:.5f} rad = {theta29*DEG:.4f} grad")
print("="*74)

# Ikosaeder: 12 Ecken (zyklische Permutationen von (0,+-1,+-phi))
V = []
for s1 in (-1,1):
    for s2 in (-1,1):
        V += [(0, s1, s2*phi), (s1, s2*phi, 0), (s2*phi, 0, s1)]
V = np.unique(np.array(V, float), axis=0)
V = V/np.linalg.norm(V[0])                       # auf Einheitskugel
assert len(V)==12, len(V)

# C5-Achsen = Eckenrichtungen (6, paarweise antipodal -> 6 Achsen)
def axisset(vecs):
    out=[]
    for v in vecs:
        v=v/np.linalg.norm(v)
        if not any(np.allclose(v,a) or np.allclose(v,-a) for a in out):
            out.append(v)
    return np.array(out)
C5 = axisset(V)

# Flaechen (20) -> C3-Achsen: Mittelpunkte von Dreiecken naechster Ecken
from scipy.spatial import ConvexHull
try:
    hull = ConvexHull(V)
    faces = hull.simplices
    centroids = np.array([V[f].mean(axis=0) for f in faces])
    C3 = axisset(centroids)
except Exception:
    # Fallback ohne scipy: C3-Achsen sind (+-1,+-1,+-1)-Typ und perms -> 10 Achsen
    c3=[]
    for s in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]:
        c3.append(s)
    C3 = axisset(np.array(c3,float))

# C2-Achsen = Kantenmittelpunkte (Mittel benachbarter Ecken)
edges=[]
for i,j in combinations(range(12),2):
    d=np.linalg.norm(V[i]-V[j])
    edges.append((d,i,j))
dmin=min(e[0] for e in edges)
mids=[ (V[i]+V[j]) for d,i,j in edges if abs(d-dmin)<1e-6 ]
C2 = axisset(np.array(mids,float))

print(f"\nAchsen gefunden: C5={len(C5)}, C3={len(C3)}, C2={len(C2)}")

def angles_between(A,B,sameset=False):
    out=set()
    pairs = combinations(range(len(A)),2) if sameset else ((i,j) for i in range(len(A)) for j in range(len(B)))
    for i,j in pairs:
        a=A[i]; b=B[j] if not sameset else A[j]
        c=abs(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
        c=min(1.0,c)
        out.add(round(np.degrees(np.arccos(c)),4))
    return sorted(out)

groups = {"C5-C5":angles_between(C5,C5,True),"C3-C3":angles_between(C3,C3,True),
          "C2-C2":angles_between(C2,C2,True),"C5-C3":angles_between(C5,C3),
          "C5-C2":angles_between(C5,C2),"C3-C2":angles_between(C3,C2)}
print("\nAlle Achsenwinkel (grad):")
for k,v in groups.items():
    print(f"  {k}: {v}")

# strenge Pruefung gegen 2/9 rad und einfache Varianten
targets = {"theta=2/9": theta29*DEG, "2*theta=4/9": 2*theta29*DEG,
           "theta/2=1/9": 0.5*theta29*DEG, "Koide 45": 45.0,
           "arccos(1/sqrt5)=63.43": np.degrees(np.arccos(1/np.sqrt(5)))}
allang = sorted(set(a for v in groups.values() for a in v))
print("\nSTRENGE PRUEFUNG (Treffer nur wenn |Diff| < 0.05 grad):")
for name,t in targets.items():
    near = min(allang, key=lambda a: abs(a-t)) if allang else None
    diff = abs(near-t) if near is not None else 99
    hit = "TREFFER" if diff < 0.05 else "kein Treffer"
    print(f"  {name:24} = {t:8.4f} grad  -> naechster Achsenwinkel {near:8.4f}  (Diff {diff:.4f})  {hit}")

print("\n" + "="*74)
print("BEFUND (ehrlich, streng):")
print("="*74)
print("""
- Die Ikosaeder-Achsenwinkel sind die festen Winkel der gemeinsamen A5-Buehne
  (C3 und C5 koexistieren). Sie sind transzendent (phi steckt drin) -- die
  richtige ART Zahl fuer einen angularen Wert.
- ABER: liegt KEIN Achsenwinkel innerhalb 0.05 grad an 2/9 rad (oder 2x, 1/2x),
  dann ist theta=2/9 KEIN direkter statisch-geometrischer Ikosaeder-Achsenwinkel.
  'Nah dran' wuerde NICHT zaehlen -- das waere Numerologie.
- Konsequenz bei Nicht-Treffer: das angulare Prinzip ist NICHT der statische
  Achsenwinkel, sondern (Dok 283) die DYNAMISCHE schief-adjungierte Phase R --
  ein akkumulierter (Berry-artiger) Winkel, kein fester Geometrie-Winkel. Das
  ist genau BD17A (HLV-Seite), und es bleibt damit -- strukturell, nicht als
  Ausrede -- auf Marcels dynamischer Phase, nicht auf FFGFTs Geometrie.
- Bei Treffer: echter Kandidat fuer eine geometrische Herleitung von theta,
  streng weiterzupruefen (welche zwei Achsen, und warum genau die).
""")
