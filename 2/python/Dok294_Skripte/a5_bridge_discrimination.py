#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 294 -- a5_bridge_discrimination.py  (UNVERSIEGELT, reproduzierbar)
=====================================================================
Winkelspektrum-Diskriminator fuer das geteilte phi-ikosaedrische Objekt.
Er loest die Achsen-Winkel-Struktur auf, an der theta=2/9 haengt -- genau
das, wofuer der fruehere Homologie-Test (Punktwolke, persistente H1) blind war.

Metrik (klar definiert, reproduzierbar): RMS-Abstand der 15 paarweisen Winkel
der sechs projizierten Achsen zum ikosaedrischen Referenzspektrum, in dem alle
15 Winkel gleich arccos(1/sqrt5)=63.435 Grad sind. Ein exakt ikosaedrisches
Objekt hat Abstand 0; generische Frames liegen in einem breiten Band.

numpy-only, Seed 20780458.
"""
import numpy as np, itertools
np.random.seed(20780458)
phi=(1+np.sqrt(5))/2; w=np.exp(2j*np.pi/3)
REF=np.degrees(np.arccos(1/np.sqrt(5)))   # 63.4349 Grad

def five_axes(tau):
    raw=[(0,1,tau),(1,tau,0),(tau,0,1),(0,1,-tau),(1,-tau,0),(-tau,0,1)]
    return [np.array(a,float)/np.linalg.norm(a) for a in raw]

def spectrum(axes):
    return np.array(sorted(np.degrees(np.arccos(np.clip(abs(np.dot(a,b)),0,1)))
                           for a,b in itertools.combinations(axes,2)))

def rms_distance(axes):
    return float(np.sqrt(np.mean((spectrum(axes)-REF)**2)))

def rot(axis,ang):
    a=np.array(axis,float); a/=np.linalg.norm(a)
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*(K@K)

V=np.array([[1,1,1],[1,w,w**2],[1,w**2,w]],dtype=complex)/np.sqrt(3)
def trivial_share(tau):
    return abs(np.vdot(V[0], rot([0,1,tau],2*np.pi/5)@V[1]))**2

print("="*70)
print(f"Referenzspektrum (ikosaedrisch): alle 15 Winkel = {REF:.4f} Grad, Abstand 0")
print("-"*70)
print(f"{'tau':>18} | {'RMS-Abstand':>11} | {'trivialer Anteil p0':>19} | Winkel")
print("-"*70)
for tau,lab in [(phi,'phi (gold)'),(1+np.sqrt(2),'1+sqrt2 (silber)'),(np.sqrt(2),'sqrt2 (Kontrolle)')]:
    ax=five_axes(tau); d=rms_distance(ax); p0=trivial_share(tau)
    uw=np.unique(np.round(spectrum(ax),2))
    star='  <-- exakt 2/9' if abs(p0-2/9)<1e-9 else ''
    print(f"{lab:>18} | {d:>11.3f} | {p0:>19.5f} | {uw}{star}")
print("-"*70)

# generisches Band: zufaellige 6-Achsen-Frames
N=2000; ds=[]
for _ in range(N):
    ax=[v/np.linalg.norm(v) for v in np.random.normal(size=(6,3))]
    ds.append(rms_distance(ax))
ds=np.array(ds)
print(f"generisches Band ({N} Zufalls-Frames): RMS-Abstand "
      f"Median={np.median(ds):.2f}, 5-95%=[{np.percentile(ds,5):.2f},{np.percentile(ds,95):.2f}]")
print()
print("BEFUND: nur tau=phi macht das Spektrum exakt uniform (Abstand 0) und den")
print("trivialen Anteil exakt 2/9. Silber und sqrt2 sind messbar verschoben und")
print("ergeben nicht 2/9. Die phi-Spezifitaet ist im Winkelspektrum sichtbar --")
print("dort, wo die Punktwolken-Homologie blind war.")
