#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT <-> HLV bridge probe -- the complete check
================================================
Pascher's three-part criterion for a genuine model connection:
  (1) the SAME structural object derived from each model's own geometry,
  (2) an explicit map between the two derivations,
  (3) a divergence point (so it is not mere shared Stufe-0 scaffolding).

HLV (Kruger) builds space as a 6D->3D ICOSAHEDRAL (5-fold) cut-and-project
quasicrystal. Kruger's exact projector (_icosahedral_projectors):

    P(tau) = [[ 1, -1,  0,  0, tau, tau],
              [tau, tau, 1, -1,  0,  0],
              [ 0,  0, tau, tau, 1, -1]]   (columns normalised)

tau = phi (golden) in physical/parallel space, tau = sigma = -1/phi in the
hidden/perpendicular space.

FFGFT builds the generation sector as a hermitian Z3-circulant mass operator on
C^3, eigenvalues M(1 + r cos(theta + 2 pi k/3)), with r = sqrt(2) (Koide Q = 2/3)
and theta = 2/9.

The cyclic coordinate map (x,y,z)->(z,x,y) is an order-3 (C3) icosahedral
rotation; it splits the 6 columns into two 3-cycles. The Gram matrix of one
3-cycle is, by the C3 symmetry, a real Z3-circulant -- the same object type as
FFGFT's mass operator. The five checks below establish whether the two models
meet (criteria 1+2) and where they diverge (criterion 3).

numpy only.
"""

import numpy as np
import itertools

PHI = (1 + np.sqrt(5)) / 2
SIGMA = -1.0 / PHI
R3 = np.array([[0, 0, 1.], [1, 0, 0], [0, 1, 0]])     # C3 rotation (x,y,z)->(z,x,y)


def projector(tau):
    P = np.array([[1.0, -1.0, 0.0, 0.0, tau, tau],
                  [tau, tau, 1.0, -1.0, 0.0, 0.0],
                  [0.0, 0.0, tau, tau, 1.0, -1.0]])
    return P / np.linalg.norm(P, axis=0, keepdims=True)   # 3 x 6, unit columns


def koide(r):
    return (1 + r**2 / 2) / 3


def c3_orbits():
    cols = projector(PHI).T
    perm = [int(np.argmin(np.linalg.norm(cols - R3 @ v, axis=1))) for v in cols]
    seen, orbits = set(), []
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j); cyc.append(j); j = perm[j]
        orbits.append(cyc)
    return orbits


print("=" * 74)
print(" CHECK 1 -- a Z3 circulant inside HLV's own geometry (criteria 1 + 2)")
print("=" * 74)
orbits = c3_orbits()
print(f"  C3 axis splits the 6 columns into two 3-cycles: {orbits}")
for name, tau in [("parallel (physical) tau=phi", PHI),
                  ("perpendicular (hidden) tau=sigma", SIGMA)]:
    V = projector(tau).T[orbits[0]]
    G = V @ V.T
    g0, g1 = np.mean(np.diag(G)), np.mean(G[~np.eye(3, dtype=bool)])
    is_circ = np.std(np.diag(G)) < 1e-12 and np.std(G[~np.eye(3, dtype=bool)]) < 1e-12
    r = 2 * g1 / g0
    print(f"  {name}: Gram=circ({g0:.5f},{g1:.5f},{g1:.5f}) circulant={is_circ}"
          f" r={r:+.5f} Q={koide(r):.5f} theta=0")
print("  => a real Z3 circulant DOES live on HLV's C3 axis. Same object type as FFGFT.")

print("\n" + "=" * 74)
print(" CHECK 2 -- but HLV's protected directions give ONLY 1/sqrt5")
print("=" * 74)
G6 = projector(PHI).T @ projector(PHI)
mags = sorted(set(np.round(np.abs(G6[~np.eye(6, dtype=bool)]), 5)))
print(f"  all 6x6 inner-product magnitudes of the columns: {mags}")
print(f"  => one value only, 1/sqrt5 = {1/np.sqrt(5):.5f}. Every protected 3-orbit -> r=2/sqrt5.")

print("\n" + "=" * 74)
print(" CHECK 3 -- no cut-and-project parameter tau ever reaches r = sqrt2")
print("=" * 74)
print("  closed form from the projector:  r(tau) = 2 tau /(1 + tau^2)")
for name, tau in [("cubic tau=1", 1.0), ("golden phi", PHI),
                  ("sqrt2", np.sqrt(2)), ("silver 1+sqrt2", 1 + np.sqrt(2))]:
    print(f"    {name:16s}: r = {2*tau/(1+tau**2):.5f}")
ts = np.linspace(0.001, 60, 400000)
print(f"  max over ALL tau: r_max = {np.max(2*ts/(1+ts**2)):.5f} (at tau=1). "
      f"FFGFT needs r = sqrt2 = {np.sqrt(2):.5f}")
print("  => r(tau) <= 1 for every tau. sqrt2 > 1 is OUTSIDE the reachable range.")

print("\n" + "=" * 74)
print(" CHECK 4 -- sqrt2 IS reachable, but only with 3-fold (not 5-fold) geometry")
print("=" * 74)


def r_cyclic(a, b, c):
    g0, g1 = a*a + b*b + c*c, a*b + b*c + c*a
    return 2 * g1 / g0


t = np.sqrt(2) - 2**0.25                        # solves (1+2t)/(2+t^2) = 1/sqrt2
print("  general 3-fold cyclic orbit (a,b,c): r = 2(ab+bc+ca)/(a^2+b^2+c^2), range [-1,2]")
print(f"    v=(1,1,{t:.4f}) [3-fold]      : r = {r_cyclic(1,1,t):.5f}  (= sqrt2)  -> reachable")
print(f"    v=(1,phi,0)    [HLV 5-fold]   : r = {r_cyclic(1,PHI,0):.5f}  (= 2/sqrt5)")
print(f"    v=(1,0,0)      [cubic, orth.] : r = {r_cyclic(1,0,0):.5f}  (decoupled)")
ev = np.linalg.eigvalsh([[1, 1/np.sqrt(2), 1/np.sqrt(2)],
                         [1/np.sqrt(2), 1, 1/np.sqrt(2)],
                         [1/np.sqrt(2), 1/np.sqrt(2), 1]])
print(f"  FFGFT Gram circ(1,1/sqrt2,1/sqrt2) eigenvalues {np.round(ev,4)} -> PSD {np.all(ev>=-1e-9)}")
print("  => FFGFT's Koide point is geometrically legitimate -- it just needs a 3-fold column.")

print("\n" + "=" * 74)
print(" CHECK 5 -- protected vs generic: sqrt2 in HLV is only a Stufe-0 coincidence")
print("=" * 74)
N = np.array(list(itertools.product(range(-3, 4), repeat=6)), dtype=float)
sel = np.linalg.norm(N @ projector(SIGMA).T, axis=1) < 2.2          # acceptance window
xpar = (N @ projector(PHI).T)[sel]
xpar = xpar[np.linalg.norm(xpar, axis=1) > 0.3]
rr = np.array([(x @ (R3 @ x)) / (x @ x) for x in xpar])
hits = int(np.sum(np.abs(rr - 1/np.sqrt(2)) < 0.02))
print(f"  {len(xpar)} projected HLV points: C3-orbit g1/g0 fills [{rr.min():.3f},{rr.max():.3f}] "
      f"(theory [-0.5,1.0])")
print(f"    -> generic points sit at every angle; near 1/sqrt2 (r=sqrt2): {hits} hits")
gen_vals = sorted(set(np.round([(v@(R3@v))/(v@v) for v in projector(PHI).T], 5)))
print(f"  protected 6 generators -> g1/g0 in {gen_vals} (only +-1/sqrt5)")
print("  => sqrt2 appears only as an UNPROTECTED generic angle (true of any dense 3-fold set);")
print("     the protected structure gives 1/sqrt5. sqrt2 is not a structural feature of HLV.")

print("\n" + "=" * 74)
print(" CHECK 6 -- a compactified HLV: the rational (Fibonacci) approximant")
print("=" * 74)


def Ppar_raw(tau):
    return np.array([[1., -1., 0., 0., tau, tau],
                     [tau, tau, 1., -1., 0., 0.],
                     [0., 0., tau, tau, 1., -1.]])


print("  replace golden phi by Fibonacci ratios tau_n = F_{n+1}/F_n -> phi:")
print("  rational tau=p/q  =>  q*P_par integer  =>  Z^6 image on (1/q)Z^3 (periodic, compact)")
print(f"  {'tau':>7} {'q*P int':>8} {'r(C3)':>9} {'Koide':>8}")
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55]
for a, b in zip(fib[1:], fib[:-1]):
    tau = a / b
    intok = np.allclose(Ppar_raw(tau) * b, np.round(Ppar_raw(tau) * b))
    r = 2 * tau / (1 + tau**2)
    print(f"  {f'{a}/{b}':>7} {str(intok):>8} {r:9.5f} {koide(r):8.5f}")
rphi = 2 * PHI / (1 + PHI**2)
print(f"  {'phi':>7} {'False':>8} {rphi:9.5f} {koide(rphi):8.5f}  (no integer factor -> dense -> decompact)")
print("  => rational tau: periodic crystal on T^3 (compact, discrete modes -> a mass scale)")
print("     -> closes the compactness layer of the fork.")
print("     But r -> 2/sqrt5, Koide -> 7/15, theta stays 0: the 5-fold/phi heritage survives.")
print("  => the comparison is now FAIR (compact vs compact) and CONFIRMS the fork: even compact,")
print("     HLV gives Koide 7/15, not FFGFT's 2/3. The divergence is NOT a compact/decompact artefact.")

print("""
VERDICT (Pascher's three-part criterion)
  (1) SAME OBJECT  : YES -- a Z3 circulant lives in HLV's own geometry (Check 1).
  (2) MAP          : the C3-axis embedding, FFGFT Z3 <-> a 3-fold axis of HLV's
                     icosahedral group.
  (3) DIVERGENCE   : FUNDAMENTAL, at the symmetry order itself.
        HLV  (protected): r = 2/sqrt5 = 0.894, theta = 0  , Koide Q = 7/15  [5-fold/phi]
        FFGFT           : r = sqrt2  = 1.414, theta = 2/9, Koide Q = 2/3   [3-fold/Koide]
      HLV's protected directions give only 1/sqrt5 (Check 2); no tau reaches sqrt2
      (Check 3); sqrt2 needs 3-fold geometry (Check 4); in HLV it occurs only as an
      unprotected generic angle (Check 5).

  A GENUINE connection (shared Z3-circulant family + explicit C3 map) with a
  FUNDAMENTAL fork (5-fold/phi vs 3-fold/sqrt2), NOT shared scaffolding and NOT an
  identity. The two models sit at two incompatible points of the same family; no
  parameter of HLV's construction bridges to FFGFT's protected Koide point.
""")
