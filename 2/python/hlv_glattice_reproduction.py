#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Independent reconstruction of the HLV G-lattice spectrum (FFGFT-side check).

Rebuilds Marcel Krueger's cut-and-project G-lattice directly from the C++
definitions in HLV-G-Lattice-Simulation-Lab (exact Z^6 icosahedral projection
matrices in GLatticeGenerator.hpp + k-NN graph rule), in pure NumPy, WITHOUT
running the upstream engine. Runs the identical analyze_spectrum() pipeline
(from hlv_ffgft_spectral.py) on the reconstructed spectrum alongside periodic
(T^3) and random (Erdos-Renyi) controls.

First result (R6=4, icosahedral ball window, N~1985, k=12, combinatorial Laplacian):
  - clearly NOT periodic (zero degeneracy vs ~0.95 for the torus);
  - bulk level-spacing ratio <r> ~ 0.525 == GOE == the random control: <r> does
    NOT separate the quasicrystal from random here (k-NN graph disorder dominates
    the bulk);
  - weak aperiodic signature only in gap structure (gap_rich 0.051 vs 0.029) and
    the low-energy sector (<r> 0.50 vs 0.54; a cluster-then-jump in the lowest
    eigenvalue ratios).
  - sanity: spectral dimension d_s ~ 2.7, same ballpark as the reported 2.49.

Conclusion for the joint test: the discriminator is the IDS/gap structure and the
low-mode sector, not bulk <r>; needs Marcel's actual weighted-Laplacian spectrum
for the matched run. Falsification before interpretation.

Requires hlv_ffgft_spectral.py in the same folder. Seed 20260609. numpy only.
"""

import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hlv_ffgft_spectral import analyze_spectrum, torus_laplacian_eigs, erdos_renyi_laplacian_eigs, print_row

RNG = np.random.default_rng(20260609)
tau = (1+np.sqrt(5))/2; nf = 1/np.sqrt(2*(2+tau))
P_phys = nf*np.array([[1,tau,0,-1,tau,0],[tau,0,1,tau,0,-1],[0,1,tau,0,-1,tau]])
P_int  = nf*np.array([[-tau,1,0,tau,1,0],[1,0,-tau,1,0,tau],[0,-tau,1,0,tau,1]])

R6=4; TARGET_N=2000; K=12
vals=np.arange(-R6,R6+1)
grids=np.meshgrid(*([vals]*6), indexing='ij')
pts=np.stack([g.ravel() for g in grids],axis=1).astype(float)
internal=pts@P_int.T; physical=pts@P_phys.T
r_int=np.linalg.norm(internal,axis=1)
thr=np.sort(r_int)[TARGET_N]; mask=r_int<thr
G=physical[mask]; N=len(G)
print(f"HLV G-lattice reproduction: Z^6 R6={R6}, icosahedral ball window, N={N}, k-NN k={K}")

G2=(G**2).sum(1); D2=G2[:,None]+G2[None,:]-2*G@G.T; np.fill_diagonal(D2,np.inf)
nn=np.argsort(D2,axis=1)[:,:K]
A=np.zeros((N,N))
for i in range(N): A[i,nn[i]]=1
A=np.maximum(A,A.T); deg=A.sum(1); L=np.diag(deg)-A
ev=np.sort(np.linalg.eigvalsh(L))
nz=ev[ev>1e-9]; lo=nz[:max(20,N//15)]; ds=2*np.polyfit(np.log(lo),np.log(np.arange(1,len(lo)+1)),1)[0]
print(f"  lambda_2={nz[0]:.6f}  d_s~{ds:.2f}  (reported run: 0.017966, 2.49 -- diff params)")

print("\n=== identical analyze_spectrum pipeline ===")
for d in (analyze_spectrum(torus_laplacian_eigs(3,8),"periodic T^3 (control)"),
          analyze_spectrum(erdos_renyi_laplacian_eigs(N,6,RNG),f"random ER (control,N={N})"),
          analyze_spectrum(ev,"HLV G-lattice (reproduced)")):
    print_row(d)

def sector_stats(ev,name,frac=0.10):
    nz=ev[ev>1e-9]; lo=nz[:max(30,int(len(nz)*frac))]; s=np.diff(lo)
    a,b=s[:-1],s[1:]; mx=np.maximum(a,b)
    r=np.mean(np.where(mx>0,np.minimum(a,b)/np.where(mx>0,mx,1),0))
    print(f"  low {int(frac*100)}% {name:22s}: <r>={r:.3f} gap_rich={np.mean(s>3*s.mean()):.3f}")
print("\n=== low-energy sector ===")
sector_stats(erdos_renyi_laplacian_eigs(N,6,np.random.default_rng(7)),"random ER")
sector_stats(ev,"HLV G-lattice")
