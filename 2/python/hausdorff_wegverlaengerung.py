#!/usr/bin/env python3
"""
Fractal Path Lengthening from Hausdorff Metric -- New Derivation
=================================================================

Question: How does light propagate on a manifold with fractal dimension
D_f = 3 - xi? What is the effective path length -- derived from geometry,
not from old formulas?

Starting point: Hausdorff scaling of geodesic length on D_f-dimensional
manifold. No prior assumption about the result.

Single FFGFT parameter: xi = 4/30000 (geometric, Doc. 009).
"""

import math

xi  = 4 / 30000.0
D_f = 3 - xi

print("=" * 70)
print("Fractal Path Lengthening from Hausdorff Metric")
print("=" * 70)
print(f"\nxi = {xi:.6e},  D_f = 3 - xi = {D_f:.8f}\n")

# ============================================================
# Derivation
#
# On a smooth 3D manifold: L_eff = R  (trivial)
#
# On a fractal D_f-manifold, the Hausdorff measure scales as:
#   mu(r) ~ r^D_f  (instead of r^3)
#
# A 1D geodesic (topological dimension D_top = 1) embedded in
# a D_f-dimensional space has an effective length:
#
#   L_eff(R) = L_0 * (R/L_0)^(D_top * 3/D_f)
#            = R * (R/L_0)^(3/D_f - 1)
#
# Exponent: 3/D_f - 1 = (3 - D_f)/D_f = xi/D_f ≈ xi/3
#
# For D_f = 3 (smooth): exponent = 0, L_eff = R  (correct limit)
# For D_f = 3-xi:       exponent = xi/D_f  (small, positive)
# ============================================================

exponent = 3/D_f - 1   # = xi/D_f exactly
exponent_approx = xi/3

print("Derivation:")
print("  On a D_f = 3-xi manifold, a 1D geodesic over distance R has:")
print()
print("      L_eff(R) = R * (R/L_0)^(xi/D_f)")
print()
print("  This is a POWER LAW, not an exponential.")
print(f"  Exponent: xi/D_f = {exponent:.8f}")
print(f"  Approx:   xi/3   = {exponent_approx:.8f}")
print(f"  Limit D_f->3: exponent -> 0, L_eff -> R  (smooth space, correct)")
print()

# ============================================================
# Fractional path lengthening: L_eff/R - 1
# ============================================================
print("Fractional path lengthening: L_eff/R - 1 = (R/L_0)^(xi/D_f) - 1")
print()
print(f"{'Scale':<22} {'R':>12} {'L_0':>14} {'ln(R/L_0)':>12} {'L_eff/R - 1':>14}")
print("-" * 78)

l_P  = 1.616255e-35  # m
L_0_planck = xi * l_P
a    = 10.2e-10      # m  (crystal lattice constant, ~10 Angstrom)
R_H  = 1.4e26        # m  (Hubble radius)

scales = [
    ("Lattice (1 unit cell)", a,   xi*a,        "xi*a"),
    ("Planck -> Planck",      l_P, L_0_planck,  "xi*l_P"),
    ("Planck -> Hubble",      R_H, L_0_planck,  "xi*l_P"),
]

for name, R, L0, L0_label in scales:
    ln_r = math.log(R/L0)
    frac = math.exp(exponent * ln_r) - 1
    print(f"{name:<22} {R:>12.3e} {L0:>14.3e} {ln_r:>12.2f} {frac:>14.8f}")

print()

# ============================================================
# Universal structure
# ============================================================
print("=" * 70)
print("Universal structure -- scale-independent")
print("=" * 70)
print(f"""
  L_eff/R = (R/L_0)^(xi/D_f)

  Three quantities:
    R   -- target distance (any scale)
    L_0 -- characteristic lower bound of that scale
    xi/D_f ≈ xi/3 -- universal fractal correction factor

  The formula is scale-independent.
  The EFFECT is scale-dependent, because ln(R/L_0) grows with scale:

    Lattice scale:    ln(a / xi*a) = ln(1/xi) = {math.log(1/xi):.2f}
    Hubble scale:     ln(R_H / xi*l_P)         = {math.log(R_H/L_0_planck):.2f}

  Same formula, same xi -- different ln(R/L_0) explains why the
  effect is small in the crystal and measurable at cosmological distances.
""")

# ============================================================
# What this means for lambda_b/lambda_e
# ============================================================
print("=" * 70)
print("Connection to lambda_b/lambda_e")
print("=" * 70)
print(f"""
  The fractional path lengthening IS the wavelength ratio:

      lambda_b/lambda_e = L_eff/R = (R/L_0)^(xi/D_f)

  This is a NEW formula -- derived from Hausdorff geometry,
  not from exp(d/R_H) or exp(xi*N).

  For cosmological distances (R = R_H, L_0 = xi*l_P):
    lambda_b/lambda_e = (R_H / (xi*l_P))^(xi/D_f)
                      = {(R_H/L_0_planck)**exponent:.6f}
    z = lambda_b/lambda_e - 1 = {(R_H/L_0_planck)**exponent - 1:.6f}

  Compare with Doc. 182 (exponential formula):
    lambda_b/lambda_e = exp(R_H/R_H) = exp(1) = {math.exp(1):.6f}
    z = {math.exp(1)-1:.6f}

  The two formulas give different values at R = R_H:
    Hausdorff (power law): z = {(R_H/L_0_planck)**exponent - 1:.4f}
    Doc. 182 (exponential): z = {math.exp(1)-1:.4f}

  They are NOT the same formula.
  The Hausdorff derivation gives a DIFFERENT prediction than Doc. 182.
  This is a genuine new result that needs to be checked against the
  cosmological data independently.
""")

# ============================================================
# Honest limits
# ============================================================
print("=" * 70)
print("HONEST LIMITS")
print("=" * 70)
print(f"""
  1. The Hausdorff scaling argument assumes that geodesics on a D_f
     manifold scale as r^(3/D_f). This is standard for Hausdorff
     dimension, but its application to light propagation requires
     a full geometric derivation (not done here).

  2. L_0 is not uniquely determined by the formula.
     The choice L_0 = xi*l_P (Planck scale) is natural for the vacuum.
     For the crystal lattice, L_0 = xi*a is a hypothesis, not derived.

  3. The formula lambda_b/lambda_e = (R/L_0)^(xi/D_f) differs from
     Doc. 182. One of them is wrong, or both are limiting cases of
     a deeper formula. This needs resolution before either can be
     used as a prediction.

  4. The connection to the observable wavelength ratio in the crystal
     (SNP polarization matrix) is structural (Z2xZ2, P''=0) but
     not yet quantitative. The power-law lengthening
     L_eff/a - 1 = {(1/xi)**exponent - 1:.6f} per unit cell
     would need to appear as a measurable phase shift or polarization
     rotation to be testable in the Qureshi experiment.
""")
