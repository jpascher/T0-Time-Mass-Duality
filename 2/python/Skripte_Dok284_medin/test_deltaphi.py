"""
Test C/D/E : the instability functional Delta-Phi and the 0.40 threshold.

Paper has TWO definitions, both named Delta-Phi, both assigned critical ~0.40:

  (Sec 2.6)  DeltaPhi = a|dS| + b|dI| + g|dC|,  a+b+g=1, a,b,g>=0,
             each component in [0,1]  ->  DeltaPhi in [0,1]  (weighted L1).
             Symmetric weights + equal deviation d  ->  DeltaPhi = d,
             "reference scale ~ 1/3".
  (Sec 2.5)  "...not imposed as a free tuning parameter ... the operator
             structure enforces the existence of a bounded instability surface."
  (Eq 12/15) DeltaPhi = closed-loop integral of curl(A_HLV) . da
             ~ Im * loop integral <psi|grad theta|psi> d theta   (a Berry phase),
             with critical DeltaPhi <= 0.40.

We test each.
"""
import numpy as np
rng = np.random.default_rng(0)

print("="*70)
print("TEST C  -- DeltaPhi as the weighted-L1 functional (Sec 2.6)")
print("="*70)
N = 200000
w = rng.dirichlet(np.ones(3), size=N)       # random convex weights
d = rng.random((N,3))                         # deviations in [0,1]
dphi = np.sum(w*d, axis=1)
print(f"sampled DeltaPhi range: [{dphi.min():.4f}, {dphi.max():.4f}]  -> bounded in [0,1] ?",
      (dphi.min()>=0 and dphi.max()<=1))
# symmetric weights + equal deviation -> DeltaPhi = d
for dd in (0.2, 1/3, 0.4, 0.8):
    val = np.sum(np.array([1/3,1/3,1/3])*np.array([dd,dd,dd]))
    print(f"  symmetric, equal dev d={dd:.3f}  ->  DeltaPhi = {val:.3f}")
print("So '1/3' is just the value you get at d=1/3. The functional is linear in")
print("each component (slope = weight, constant); d(DeltaPhi)/d(component)=weight.")
print("=> NO intrinsic curvature, NO bifurcation point: the level set DeltaPhi=c is")
print("   a flat polytope facet for every c. A 'critical 0.40' is an imposed")
print("   contour, not a structurally enforced transition. This contradicts the")
print("   Sec 2.5 claim that the operator structure 'enforces' the surface.")
print()

print("="*70)
print("TEST E  -- is 0.40 derived, or a free knob?")
print("="*70)
# Fix the SAME equal deviation d=0.4 on every axis; ANY convex weights give 0.40.
print("With equal deviations d=0.40 on all axes, every convex weight set gives 0.40:")
for _ in range(3):
    ww = rng.dirichlet(np.ones(3))
    print("   weights", np.round(ww,3), "-> DeltaPhi =", round(float(ww@np.array([0.4,0.4,0.4])),3))
# And the symmetric reference moves to 0.40 just by choosing deviations / asymmetry.
print("Conversely, to make a *balanced* reading land on 0.40 instead of 1/3 you")
print("only change the deviation level (0.40) or tilt the weights -- a fit, not a")
print("derivation. The paper itself (Sec 2.6.2) attributes the 0.40-vs-0.333 gap")
print("to 'dataset-specific weighting asymmetry & normalization'. That IS a free")
print("parameter, contradicting Sec 2.5 ('not imposed as a free tuning parameter').")
print()

print("="*70)
print("TEST D  -- DeltaPhi as a Berry phase (Eq 12/15) vs the [0,1] index")
print("="*70)
# Berry phase of a spin-1/2 transported around a cone of half-angle theta on the
# Bloch sphere is  gamma = -(1/2) * solid_angle = -pi*(1 - cos theta).
def berry_spin_half(cone_half_angle):
    return -np.pi*(1 - np.cos(cone_half_angle))
print("cone half-angle (deg) | Berry phase (rad) | |gamma| | in [0,1]? ")
for deg in (10, 30, 60, 90, 120, 150, 179):
    g = berry_spin_half(np.deg2rad(deg))
    print(f"   {deg:6.0f}            | {g:8.3f}        | {abs(g):6.3f} | {0<=abs(g)<=1}")
print("Berry phase is an ANGLE in radians; |gamma| ranges up to ~2*pi (here to ~2pi),")
print("it is NOT a normalized deviation bounded by 1, and there is no reason for it")
print("to sit at 0.40. A loop with |gamma|=0.40 rad is a very SMALL loop")
print(f"   (cone half-angle = {np.rad2deg(np.arccos(1-0.40/np.pi)):.1f} deg),")
print("whereas in the Sec 2.6 reading 0.40 is a 'moderate' deviation near the")
print("symmetric reference. The two DeltaPhi's are different objects (a unitless")
print("[0,1] index vs a radian holonomy); calling both 'DeltaPhi ~ 0.40' is an")
print("equivocation. A single symbol carries two incompatible definitions.")
