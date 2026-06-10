#!/usr/bin/env python3
"""
WBE Argument on T^4 (FFGFT, static) vs. FLRW (expanding)

Question (from IPI exchange with Onur Teker, June 2026):
  The West-Brown-Enquist argument (WBE, 1997) derives the energy-scaling
  exponent alpha = D/(D+1) for space-filling, minimum-dissipation networks.
  Onur Teker applies it in UIFT to cosmological holography (FLRW).
  His own open posit: whether the argument survives the carry-over to an
  expanding (FLRW) universe -- self-described as 'not closed'.

  Onur's own reflection from the mail (2 June 2026):
  'The impedance-matching argument is on its firmest ground in a static,
   geometric setting like FFGFT's, not in my expanding one.'

  This script checks: are the three WBE preconditions satisfied exactly
  or only approximately on the static, compact T^4 (FFGFT)? And what
  breaks in FLRW?

Single FFGFT parameter: xi = 4/30000 (geometric, Doc. 009).
All other quantities follow from it.

================================================================================
WBE preconditions (West-Brown-Enquist 1997, Science 276:122):
  (A) Fixed-size terminal units
  (B) Space-filling: L proportional to N^(1/D), hence V proportional to N
  (C) Minimum dissipation (impedance matching, stationary state)
  => Result: E proportional to N^alpha, alpha = D/(D+1)
================================================================================
"""

import math

xi  = 4 / 30000.0
D   = 3
D_f = 3 - xi          # fractal dimension FFGFT

print("=" * 70)
print("WBE Argument: T^4 (FFGFT, static) vs. FLRW (expanding)")
print("=" * 70)
print(f"\nFFGFT parameter: xi = {xi:.6e},  D_f = 3 - xi = {D_f:.8f}\n")

# ============================================================
# T^4 (FFGFT): check preconditions
# ============================================================
print("=" * 70)
print("T^4 (FFGFT, static, compact):")
print("=" * 70)

print("""
(A) Terminal units = torus modes, smallest length L_0 = xi * l_P.
    L_0 is a geometric constant -- fixed and time-independent.
    SATISFIED: exactly. No time dependence, no free parameter.""")

print(f"""
(B) Space-filling on T^4:
    Number of modes N ~ (R / L_0)^D_f on the compact torus.
    T^4 is closed -- all modes fill it completely,
    no boundary, no leakage, no excluded regions.
    V ~ N is satisfied by construction (compact phase space).
    SATISFIED: structurally, and more strongly than in open space.""")

print("""
(C) Minimum dissipation:
    In the static T^4 there is no expansion, no cosmological horizon
    swallowing modes. The system is time-independent.
    A time-independent system is by definition in a stationary state --
    the dissipation minimum is not an assumption but a consequence.
    SATISFIED: exactly, by construction.""")

alpha_Df = D_f / (D_f + 1)
alpha_D3 = D   / (D   + 1)
print(f"""
Result on T^4:
  alpha(D_f = 3-xi)  = {alpha_Df:.8f}
  alpha(D = 3 exact) = {alpha_D3:.8f}
  Difference         = {abs(alpha_Df - alpha_D3):.2e}   (~ xi/16, not measurable)
  w_DE = -alpha      = {-alpha_Df:.6f}

  => alpha is a DERIVATION from the geometry in FFGFT, not a posit.
     All three WBE preconditions are satisfied EXACTLY.""")

# ============================================================
# FLRW: check preconditions
# ============================================================
print("\n" + "=" * 70)
print("FLRW (expanding, Onur's framework):")
print("=" * 70)

print("""
(A) Terminal units:
    Planck bits remain fixed by definition -- OK.
    BUT: energy per bit = k_B T ln2 drops with expansion (T ~ 1/a).
    The energy scale of the units is TIME-DEPENDENT.
    APPROXIMATELY satisfied (holds quasi-statically, not exactly).""")

print("""
(B) Space-filling -- THIS IS WHERE THE ARGUMENT BREAKS:
    In expanding FLRW:
      N_bits ~ A_horizon / l_P^2  (Bekenstein-Hawking: bits on the SURFACE)
      V(t) ~ a(t)^3               (volume grows cubically)
      A(t) ~ a(t)^2               (area grows quadratically)
    V ~ N requires N ~ V -- this holds only if bits are distributed
    uniformly throughout the VOLUME. In FLRW they are bound to the
    horizon (SURFACE): area ~ a^2, volume ~ a^3 -> no V ~ N.
    BREAKS: structurally; no workaround without an additional posit.""")

print("""
(C) Minimum dissipation:
    FLRW is dynamic (a(t) time-dependent) -- no stationary state.
    Prigogine's minimum entropy production theorem applies only to
    quasi-static processes near equilibrium. Cosmological expansion
    is not quasi-static everywhere (especially not during inflation).
    APPROXIMATELY satisfied (Prigogine helps but does not close it).""")

print(f"""
Result in FLRW:
  alpha = D/(D+1) = {alpha_D3:.6f} is a POSIT (Onur's own statement).
  Precondition (B) breaks structurally -- Bekenstein contradicts WBE
  in the expanding universe (surface vs. volume scaling).""")

# ============================================================
# Structural asymmetry
# ============================================================
print("\n" + "=" * 70)
print("STRUCTURAL ASYMMETRY (main finding):")
print("=" * 70)
print(f"""
  T^4 (FFGFT):
    (A) exact   (B) exact / stronger   (C) exact
    alpha = {alpha_Df:.6f}  -- DERIVATION from xi and D_f

  FLRW (Onur):
    (A) approx  (B) BREAKS             (C) approx
    alpha = {alpha_D3:.6f}  -- POSIT (self-declared)

  The WBE argument has its natural home in the static, compact T^4 --
  not in the expanding FLRW.

  Onur's intuition from the mail was correct:
  'The impedance-matching argument is on its firmest ground in a
   static, geometric setting like FFGFT's, not in my expanding one.'

  This finding confirms and sharpens it: it is precondition (B)
  (surface vs. volume) that breaks structurally in FLRW -- not a
  numerical imprecision but a conceptual contradiction between
  Bekenstein-Hawking and WBE in the expanding universe.""")

# ============================================================
# Why no plant-like fractality in the cosmos
# ============================================================
print("\n" + "=" * 70)
print("Why cosmic patterns are not WBE fractals:")
print("=" * 70)
print(f"""
  D_f - 3 = -xi = {-xi:.4e}  -- deviation from smooth 3D is tiny.

  Cosmic patterns (spiral galaxies, orbits, large-scale structure)
  are not WBE fractals (self-similarity through iteration over many
  orders of magnitude, as in plants, lungs, blood vessels).

  They are TORUS MODES: projected winding structures of T^4.
    Spiral galaxies  = logarithmic spirals (one winding class)
    Orbits           = closed modes (periodic winding numbers)
    Foam structure   = interference of the mode distribution in 3D section

  This is a structurally different type:
    WBE fractal:    self-similarity through ITERATION
    T^4 pattern:    topology through COMPACTIFICATION

  Consequence: no plant-like fractality in the cosmos, BECAUSE the
  structure is modal (topological) rather than iterative.
  This is consistent with D_f = 3 - xi ~ 3 (nearly smooth).""")

# ============================================================
# Honest limits
# ============================================================
print("\n" + "=" * 70)
print("HONEST LIMITS:")
print("=" * 70)
print("""
  1. This analysis rests on Onur's mail description of Section 3.4
     (Zenodo 10.5281/zenodo.20482718). The full document may contain
     additional material not covered here.

  2. Saying precondition (B) 'breaks' in FLRW applies to the naive
     application. Onur might have a way to count bits in the volume
     rather than on the surface -- but that would be a further posit
     that would need to be stated explicitly.

  3. The connection spirals/orbits = torus modes is an FFGFT claim
     (reduction layer), not a core result. A computed torus-mode
     derivation of a concrete spiral form is still outstanding.

  4. The numerical difference alpha(D_f) vs. alpha(D=3) = 8e-6
     is not measurable -- the structural argument is qualitative.""")
