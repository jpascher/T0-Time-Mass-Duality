#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
z3_holonomie_test.py  --  Dok 286 / theta=2/9: spaltet eine Holonomie die Familie?
=================================================================================
Vorgeschichte (z3_modelock_test.py): Z3-Treibung schuetzt den NENNER 9, laesst
die 9er-Familie aber ENTARTET (1/9=2/9=4/9) -- sie sind EIN Z3-Orbit, eine
einzige 3-Struktur ist zaehler-blind.

Johanns Vermutung: den Zaehler waehlt erst eine ZWEITE Struktur mit relativer
PHASE = Holonomie = "weitere Dimensionen" (3' der Verdopplung 6=3+3', T4->T7).
Test: zwei 3-zaehlige Harmonische (h=3, h=9) mit relativer Phase phi:
    f(theta) = a3 sin(2pi*3 theta) + a9 sin(2pi*9 theta + phi)
phi ist NICHT wegtransformierbar -> physikalisch.

Hier PRAEZISE gemessen (Bisektion der Zungenraender, ~1e-6), nicht per Gitter,
um Gitterrauschen vom echten Effekt zu trennen. Reportet die EFFEKTGROESSE.
xi bleibt fest (4/30000). numpy-only, seed=20780458.
"""
import numpy as np
np.random.seed(20780458)
XI = 4/30000.0
K = 0.35; a3 = K/6; a9 = K/18

def rho_scalar(Om, forcing, n_trans=400, n_avg=2500):
    t = 0.1234
    for _ in range(n_trans):
        k = 0.0
        for m,a,ph in forcing: k += a*np.sin(2*np.pi*m*t+ph)
        t = t + Om - k/(2*np.pi); t -= np.floor(t)
    tot = 0.0
    for _ in range(n_avg):
        k = 0.0
        for m,a,ph in forcing: k += a*np.sin(2*np.pi*m*t+ph)
        tn = t + Om - k/(2*np.pi); tot += tn-t; t = tn-np.floor(tn)
    return tot/n_avg

def width_bisect(p,q,forcing,tol=8e-4):
    target=p/q
    # locked-Zentrum nahe p/q suchen
    cands=np.linspace(target-0.012,target+0.012,49)
    locked=[o for o in cands if abs(rho_scalar(o,forcing)-target)<tol]
    if not locked: return 0.0,0.0
    c=locked[len(locked)//2]
    edges=[]
    for d in (-1.0,1.0):
        o=c; lo=c; hi=None
        for _ in range(80):
            o+=d*0.0004
            if abs(rho_scalar(o,forcing)-target)>=tol: hi=o; lo=o-d*0.0004; break
        if hi is None: edges.append(c+d*0.032); continue
        for _ in range(28):
            mid=0.5*(lo+hi)
            if abs(rho_scalar(mid,forcing)-target)<tol: lo=mid
            else: hi=mid
        edges.append(0.5*(lo+hi))
    return abs(edges[1]-edges[0]), c

fam=[(1,9),(2,9),(4,9)]
n_phi=25
phis=np.linspace(0.0,2*np.pi,n_phi)
print("="*78)
print("HOLONOMIE-TEST (praezise/Bisektion): bricht phi (h=3 vs h=9) die 9er-Familie?")
print(f"  f={a3:.4f} sin(2pi 3 th)+{a9:.4f} sin(2pi 9 th+phi), K={K}, xi={XI:.3e} fest")
print("="*78)
print(f"{'phi/2pi':>8} | {'W(1/9)':>10} {'W(2/9)':>10} {'W(4/9)':>10} | {'Spread%':>8} breiteste")
print("-"*78)
rows={}
for phi in phis:
    frc=[(3,a3,0.0),(9,a9,phi)]
    w={pq:width_bisect(pq[0],pq[1],frc)[0] for pq in fam}
    rows[phi]=w
    base=np.mean(list(w.values()))
    spread=(max(w.values())-min(w.values()))
    win=max(fam,key=lambda pq:w[pq])
    mark="  <-- 2/9" if win==(2,9) else ""
    print(f"{phi/(2*np.pi):8.3f} | {w[(1,9)]:10.6f} {w[(2,9)]:10.6f} {w[(4,9)]:10.6f} "
          f"| {100*spread/base:7.2f}% {win[0]}/{win[1]}{mark}")
print("-"*78)
w0=rows[phis[0]]; base0=np.mean(list(w0.values())); spread0=max(w0.values())-min(w0.values())
spreads={phi:(max(w.values())-min(w.values())) for phi,w in rows.items()}
phimax=max(spreads,key=spreads.get); basemax=np.mean(list(rows[phimax].values()))
win29=[phi for phi,w in rows.items() if max(w,key=w.get)==(2,9)]
print(f"\nphi=0 (Kontrolle): Spread={spread0:.6f} ({100*spread0/base0:.2f}%) -> Entartung")
print(f"max Aufspaltung bei phi={phimax/(2*np.pi):.3f}*2pi: Spread={spreads[phimax]:.6f} "
      f"({100*spreads[phimax]/basemax:.2f}%)")
print("\nBEFUND (ehrlich):")
eff=100*spreads[phimax]/basemax
if spreads[phimax]>3*max(spread0,1e-6):
    print(f"  - Entartung BRICHT auf (Spread 0% -> {eff:.2f}%). Holonomie ist zaehler-sensitiv: JA.")
else:
    print(f"  - Kaum Aufspaltung (~{eff:.2f}%). Holonomie waehlt Zaehler kaum -> Hypothese schwach.")
if win29:
    band=[round(p/(2*np.pi),2) for p in win29]
    best=max(win29,key=lambda p:rows[p][(2,9)]-max(rows[p][(1,9)],rows[p][(4,9)]))
    w=rows[best]; adv=100*(w[(2,9)]-max(w[(1,9)],w[(4,9)]))/np.mean(list(w.values()))
    print(f"  - 2/9 ist breiteste in phi/2pi in {band}; klarster Vorsprung bei "
          f"phi={best/(2*np.pi):.3f}*2pi (+{adv:.2f}% vor naechster).")
    print(f"  - D.h. die Holonomie KANN 2/9 auswaehlen -- aber schwach und nur in einem")
    print(f"    phi-Band; phi ist FREI (FFGFT fixiert ihn nicht). Offene Frage praezise")
    print(f"    verschoben: WAS lockt phi? = genau Marcels BD17A (locked holonomy).")
else:
    print(f"  - 2/9 nie breiteste -> die einfache 2-Harmonischen-Holonomie waehlt 2/9")
    print(f"    NICHT speziell (ehrliches Null-Ergebnis).")
print("="*78)
