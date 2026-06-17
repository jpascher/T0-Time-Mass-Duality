#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT -- the Z3 mass operator for ALL THREE fermion sectors
===========================================================
Premise. The Hilbert-space picture of FFGFT (Doc. 282) is a *faithful
translation* of the theory (the T^4 <-> Hilbert bijection, Doc. 270, type III).
If it is faithful, then the masses FFGFT obtains via the xi-route (m = r*xi^p*v,
Doc. 006) -- leptons AND quarks -- must also be expressible as the spectrum of
the Hermitian Z3-circulant operator. This script checks exactly that.

What it shows.
  (1) For each charge sector (charged leptons, up-quarks, down-quarks) the three
      masses are written as the spectrum S^2 of a Hermitian Z3-circulant
          S = circ(t0, t1, t2),  t0 = M,  t1 = (M r / 2) e^{i theta},  t2 = conj(t1),
      with eigenvalues  sqrt(m_j) = M (1 + r cos(theta + 2 pi j / 3)).
  (2) The operator reproduces the masses to MACHINE PRECISION in every sector.
      => the Hilbert-space calculation is universal; quarks are included.

The honest point (this is the whole message).
  The circle parametrisation is a BIJECTION: 3 masses <-> (M, r, theta). So
  "the masses can be written as an operator spectrum" is AUTOMATIC for any
  triplet -- it is not a prediction, it is what "faithful translation" means
  (cf. the xi^N / phi^N triviality, Doc. 190 P35).
  The genuine content is whether the operator parameters are SPECIAL NUMBERS:
    * leptons : r = sqrt(2)  (<=> Koide Q = 2/3, the Z3 + sqrt2 condition,
                Doc. 258/259) AND theta = 2/9 (a clean rational). Two pure numbers.
    * quarks  : r_up ~ 1.76, r_down ~ 1.55 -- NOT sqrt(2); the angles are not
                clean rationals. The operator carries the masses faithfully, but
                with un-special parameters.
  This mirrors the xi-route exactly (Doc. 006): there too the lepton ratios carry
  real structure (Koide), while the quark (r, p) are per-particle classification.
  A faithful translation MUST agree on where the structure is -- and it does.

Consequence. Any attempt to impose the lepton condition r = sqrt(2) (i.e. k = 1,
Koide 2/3) on the quark sectors is falsified by the faithful translation itself:
the up sector needs r ~ 1.76, the down sector r ~ 1.55. There is no room for
sqrt(2), hence no room for a single universal "k = 1" Z3 angle across sectors.

numpy only.
"""

import numpy as np

W = np.exp(2j * np.pi / 3)  # cube root of unity


# --------------------------------------------------------------------------
def circle_params(masses):
    """Inverse map  3 masses -> (M, r, theta)  on the Koide circle.

    Always solvable: with M = mean(sqrt m), the residuals x_j = sqrt(m_j)/M - 1
    satisfy sum_j x_j = 0 and lie on  x_j = r cos(theta + 2 pi j / 3).
    """
    s = np.sqrt(np.sort(masses))
    M = s.mean()
    x = s / M - 1.0
    r = np.sqrt((2.0 / 3.0) * np.sum(x ** 2))     # since sum cos^2 = 3/2
    js = np.arange(3)
    A = np.array([[np.cos(2 * np.pi * j / 3), -np.sin(2 * np.pi * j / 3)] for j in js])
    a, b = np.linalg.lstsq(A, x / r, rcond=None)[0]   # (cos theta, sin theta)
    theta = np.arctan2(b, a)
    return M, r, theta


def build_operator(M, r, theta):
    """Hermitian Z3-circulant S with scale M, spread r, angle theta."""
    t0 = M
    t1 = (M * r / 2.0) * np.exp(1j * theta)
    t2 = np.conj(t1)
    return np.array([[t0, t1, t2],
                     [t2, t0, t1],
                     [t1, t2, t0]], dtype=complex)


def koide_Q(masses):
    s = np.sqrt(np.sort(masses))
    return masses.sum() / s.sum() ** 2


# --------------------------------------------------------------------------
# FFGFT xi-route masses (Doc. 006 / calc-o), in MeV.  Experimental values agree
# to ~1%; the demonstration is identical with either set (only ratios enter).
SECTORS = {
    "charged leptons (e, mu, tau)": np.array([0.51099895, 105.6583755, 1776.86]),
    "up-quarks      (u, c, t)":     np.array([2.272, 1284.077, 171974.543]),
    "down-quarks    (d, s, b)":     np.array([4.734, 94.756, 4260.845]),
}

SQRT2 = np.sqrt(2.0)

print("=" * 74)
print("FFGFT Z3 mass operator -- all three sectors as a spectrum S^2")
print("=" * 74)
print(f"{'sector':30}{'M':>10}{'r':>9}{'theta':>9}{'Koide Q':>10}{'max rel err':>13}")
print("-" * 74)

rows = []
for name, m in SECTORS.items():
    M, r, theta = circle_params(m)
    S = build_operator(M, r, theta)
    herm = np.linalg.norm(S - S.conj().T)
    ev = np.sort(np.linalg.eigvalsh(S))      # = signed sqrt(m)
    m_op = np.sort(ev ** 2)
    m_dat = np.sort(m)
    relerr = float(np.max(np.abs(m_op - m_dat) / m_dat))
    Q = koide_Q(m)
    rows.append((name, M, r, theta, Q, relerr, herm))
    print(f"{name:30}{M:10.3f}{r:9.4f}{theta:9.4f}{Q:10.4f}{relerr:13.1e}")

print("-" * 74)
print(f"sqrt(2) = {SQRT2:.4f},  2/3 = {2/3:.4f},  2/9 = {2/9:.4f}  (lepton reference)")

print("""
READING
  * Every sector: spectrum^2 reproduces the masses to ~1e-14, operator exactly
    Hermitian. The Hilbert-space calculation is UNIVERSAL -- quarks included.
  * That universality is automatic (the circle map is a bijection: 3 masses
    <-> M, r, theta). It is not a prediction; it is what "faithful translation"
    means (Doc. 270, type III; cf. xi^N/phi^N triviality, Doc. 190 P35).
  * The content is the PARAMETERS:
      leptons : r = sqrt(2)  (Koide Q = 2/3, structural) and theta = 2/9 (clean)
                -> two pure numbers (Doc. 282).
      quarks  : r_up ~ 1.76, r_down ~ 1.55 -- not sqrt(2); angles not clean.
  * Same verdict as the xi-route (Doc. 006): real structure at the leptons,
    classification at the quarks. A faithful translation must agree -- and does.

CONSEQUENCE
  Imposing r = sqrt(2) (k = 1, Koide 2/3) on the quark sectors is falsified by
  the translation itself: up needs r ~ 1.76, down r ~ 1.55. No room for a single
  universal Z3 angle with k = 1 across sectors.
""")

# Note on the lepton angle: circle_params places the j=0 origin on a different
# eigenvalue, so it reports theta_lep = 2/9 + 2*pi/3.  The physical angle is 2/9,
# as ffgft_mass_operator_C3.py shows by building S directly with theta = 2/9.
lep_theta = rows[0][3]
print(f"(lepton angle reported as {lep_theta:.4f} = 2/9 + 2pi/3; physical theta = 2/9,")
print(" see ffgft_mass_operator_C3.py which uses theta = 2/9 directly.)")
