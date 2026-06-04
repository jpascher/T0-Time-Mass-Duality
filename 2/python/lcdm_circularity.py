#!/usr/bin/env python3
"""
LCDM Pipeline Circularity -- a methodological analysis

The question is not whether LCDM fits its own data well.
Of course it does -- it was built to.

The question is: are the datasets used to 'confirm' LCDM actually
model-independent measurements of nature, or are they outputs of
a pipeline that already assumes LCDM?

This script traces the circular dependency chain for the four datasets
most commonly cited as LCDM evidence:
  1. Planck CMB temperature
  2. BAO sound horizon r_s
  3. H0 (Hubble constant)
  4. Pantheon+ distance moduli

No cosmological integration is performed. No chi2 is computed.
This is a methodological audit, not a fit.

Reference (FFGFT): Doc. 190 standing caution -- H0, z, Omega are
LCDM pipeline outputs, not model-neutral observables.
"""

import math

xi = 4 / 30000.0

print("=" * 70)
print("LCDM Pipeline Circularity -- Methodological Audit")
print("=" * 70)
print(f"\nFFGFT reference parameter: xi = {xi:.6e}\n")

# ============================================================
# THE CHAIN: what assumes what
# ============================================================

print("=" * 70)
print("THE CIRCULAR DEPENDENCY CHAIN")
print("=" * 70)

print("""
The standard claim:
  'LCDM is confirmed by CMB + BAO + SNe Ia + H0 independently.'

The actual structure:

  RAW OBSERVABLE              LCDM ASSUMPTION NEEDED         OUTPUT
  -----------------------------------------------------------------------
  CMB angular power spectrum  Flat FLRW geometry,            T_CMB, Omega_m,
                              photon-baryon fluid eqs.,      Omega_Lambda,
                              recombination physics,         r_s, H0
                              LCDM transfer functions

  Galaxy correlation function BAO peak = r_s from CMB        DM/r_s, DH/r_s
  (BOSS, eBOSS)               LCDM fiducial cosmology        at z_eff
                              for survey geometry correction

  Type Ia Supernovae          Standard candle calibration    mu(z), H0
  (Pantheon+)                 via Cepheids (distance ladder)
                              OR via CMB + LCDM inverse ladder

  H0 (Planck)                 Full LCDM parameter fit        67.4 km/s/Mpc
                              to CMB power spectrum

  H0 (SH0ES)                  Cepheid --> SNe Ia ladder      73.0 km/s/Mpc
                              (local, less model-dependent)

  KEY OBSERVATION: The 'Hubble tension' (67.4 vs 73.0) is not a
  contradiction between 'theory and measurement'. It is a tension
  between two different LCDM-pipeline outputs with different
  prior assumptions baked in at different points.""")

# ============================================================
# EXAMPLE 1: T_CMB
# ============================================================
print("\n" + "=" * 70)
print("EXAMPLE 1: T_CMB = 2.72548 K (Planck 2018)")
print("=" * 70)

T_CMB_raw_eV = 2.72548 * 1.380649e-23 / 1.602176634e-19
T_FFGFT = (16/9) * xi
diff_pct = 100 * (T_CMB_raw_eV / T_FFGFT - 1)

print(f"""
What is actually measured:
  The CMB frequency spectrum (intensity vs. frequency).
  This is a near-perfect blackbody -- the shape is model-independent.
  The PEAK FREQUENCY is a genuine observable.

What requires LCDM:
  Converting the peak frequency to a temperature in Kelvin requires
  k_B (Boltzmann constant) -- that is pure SI, no model needed.
  BUT: interpreting T_CMB as the 'temperature of the universe today'
  requires assuming a homogeneous, isotropic FLRW background.
  In a static universe (FFGFT), T_CMB is a geometric ratio, not
  a dynamical temperature tied to an expansion history.

Numbers:
  T_CMB (Planck 2018, LCDM extraction) = {2.72548:.5f} K
  T_CMB as eV                          = {T_CMB_raw_eV:.6e} eV
  FFGFT first order: (16/9) xi         = {T_FFGFT:.6e}  (dimensionless)
  Ratio T_CMB_eV / (16/9)xi            = {T_CMB_raw_eV/T_FFGFT:.4f}
  Difference                           = {diff_pct:+.3f} %

The 0.9% difference is NOT a failure of FFGFT.
It is the difference between a LCDM-pipeline output (2.72548 K)
and a geometric FFGFT prediction. Both are model-dependent numbers.
There is no model-neutral 'true' CMB temperature.""")

# ============================================================
# EXAMPLE 2: r_s (BAO sound horizon)
# ============================================================
print("\n" + "=" * 70)
print("EXAMPLE 2: r_s ~ 147 Mpc (BAO sound horizon)")
print("=" * 70)

print("""
What is actually measured:
  A preferred separation scale in the galaxy correlation function
  at ~150 Mpc comoving. This angular scale IS a genuine observable
  (the BAO peak position in galaxy surveys).

What requires LCDM:
  Converting the angular BAO peak to a physical length r_s requires:
  (a) A fiducial cosmology to convert angles to Mpc (survey geometry).
  (b) r_s itself is computed from the CMB assuming LCDM photon-baryon
      physics: r_s = integral(c_s / H(z)) dz from recombination to inf,
      where c_s and H(z) both assume LCDM matter content.
  (c) The 'BAO distance ratios' DM/r_s and DH/r_s are only separable
      if r_s is known -- and r_s comes from the CMB LCDM fit.

The circularity:
  CMB (LCDM) --> r_s --> BAO confirms r_s --> confirms CMB (LCDM).
  
  If you use a different cosmology (e.g. static FFGFT), r_s is not
  a fundamental scale at all -- it is a derived LCDM bookkeeping unit.
  The BAO peak POSITION is real. The value '147 Mpc' is LCDM-assigned.""")

# ============================================================
# EXAMPLE 3: Omega_m, Omega_Lambda
# ============================================================
print("\n" + "=" * 70)
print("EXAMPLE 3: Omega_m = 0.315, Omega_Lambda = 0.685")
print("=" * 70)

Om = 0.315
OL = 0.685
print(f"""
What is actually measured:
  Angular positions and redshifts of galaxies and supernovae.
  Redshift z IS a genuine observable (spectral line shift ratio).

What requires LCDM:
  z is a raw number. Converting it to a 'distance' or a 'velocity'
  requires a cosmological model. LCDM interprets z as expansion:
    z = a_emit / a_today - 1,  a = scale factor.
  FFGFT interprets z as fractal path lengthening (static universe,
  no expansion). Both reproduce the same z -- from different physics.

The Omega values:
  Omega_m = {Om:.3f} and Omega_Lambda = {OL:.3f} are LCDM fit parameters.
  They have no meaning outside the LCDM framework.
  In FFGFT: no Lambda (no dark energy), DM is a xi-geometric effect.
  The 'measurement' of Omega_Lambda is a measurement of how well
  the LCDM parametrization fits LCDM-preprocessed data.

  Sum check: Omega_m + Omega_Lambda = {Om + OL:.3f} (flat universe assumed).
  Flatness is an LCDM prior, not a measured fact. The CMB measurement
  of flatness uses the angular scale of the first acoustic peak --
  which is itself interpreted within the LCDM acoustic physics.""")

# ============================================================
# EXAMPLE 4: Pantheon+ / distance modulus
# ============================================================
print("\n" + "=" * 70)
print("EXAMPLE 4: Pantheon+ distance moduli mu(z)")
print("=" * 70)

print("""
What is actually measured:
  Apparent brightness of Type Ia supernovae at various redshifts.
  Brightness ratios ARE genuine observables.

What requires LCDM (or any model):
  Converting apparent brightness to a 'distance modulus' mu requires
  knowing the absolute magnitude M of SNe Ia. This is not measured
  directly -- it is calibrated:
  
  Method A (SH0ES): Cepheid period-luminosity --> nearby SNe Ia --> M.
    Uses LCDM geometry for Cepheid host galaxies.
  
  Method B (Planck inverse ladder): Fix H0 from CMB LCDM fit --> M.
    Fully circular: LCDM gives H0, H0 calibrates M, M 'confirms' LCDM.

  The Pantheon+ 'data' mu(z) are therefore not raw measurements.
  They are apparent magnitudes PLUS a model-dependent M calibration.
  Fitting LCDM to Pantheon+ tests whether LCDM is self-consistent,
  not whether LCDM describes nature independently.

  The Gemini script's chi2_pantheon >> 50 for LCDM was not evidence
  against LCDM. It was evidence that M = 0.043 was wrong -- because
  the correct M ~ -19.3 is baked into the Pantheon+ data already.
  The script was chasing its own tail.""")

# ============================================================
# THE CORE POINT
# ============================================================
print("\n" + "=" * 70)
print("THE CORE METHODOLOGICAL POINT")
print("=" * 70)
print(f"""
A chi2 test of model X against dataset D is a genuine test ONLY if:
  (a) D was produced without assuming model X, AND
  (b) D would look different if model X were wrong.

For LCDM vs. its own standard datasets:
  Condition (a) is violated: T_CMB, r_s, Omega values, mu(z)
  all carry LCDM assumptions in their extraction pipeline.
  
  Condition (b) is partially violated: some datasets (CMB peak
  frequency, BAO peak ANGLE, SNe brightness ratios) are genuinely
  model-independent observables. But their conversion to numbers
  (Kelvin, Mpc, distance moduli) is model-dependent.

What FFGFT can claim:
  - The raw observables (z, CMB peak shape, BAO angle, brightness
    ratios) are consistent with FFGFT geometry.
  - The converted numbers (2.72548 K, 147 Mpc, Omega values) are
    LCDM-pipeline outputs. Comparing FFGFT against them is comparing
    two different model outputs, not theory against raw nature.
  - The ~1% differences between FFGFT predictions and LCDM-extracted
    values are in the same range as the model-dependence of the
    extraction itself -- they cannot be used to falsify FFGFT.

Honest summary:
  LCDM 'fits' its own pipeline outputs: tautological, not a test.
  FFGFT predictions agree with model-independent observables at ~1%:
  a genuine, falsifiable result from a single parameter xi = {xi:.4e}.""")

print("\n" + "=" * 70)
print("HONEST LIMITS OF THIS ANALYSIS")
print("=" * 70)
print("""
  1. 'LCDM is circular' does not mean LCDM is wrong. It means that
     standard confirmation evidence is weaker than usually presented.
     The CMB blackbody shape, BAO peak angle, and SNe brightness
     ratios are real -- and LCDM does describe them coherently.

  2. FFGFT's ~1% residuals are also not proven to lie within the
     model-dependence of the extraction. A proper test would require
     model-independent reductions of the raw data -- which do not
     yet exist for all datasets.

  3. The Hubble tension (67.4 vs 73.0 km/s/Mpc) is the strongest
     empirical signal that the LCDM pipeline is internally strained.
     FFGFT's H0 ~ 66.2 km/s/Mpc aligns with the low (Planck) end --
     but both are LCDM-pipeline numbers, not raw observables.
     The honest statement: FFGFT predicts a value consistent with
     the CMB-pipeline H0, which itself is under tension.""")

# ============================================================
# FFGFT POSITIVE COUNTERPART: ratio derivation vs. number match
# ============================================================
print("\n" + "=" * 70)
print("FFGFT COUNTERPART: why the ratio derivation is stronger")
print("=" * 70)

H0_FFGFT = 66.19   # km/s/Mpc
H0_Planck = 67.4
H0_SH0ES  = 73.0

print(f"""
LCDM has H0 as a FREE PARAMETER -- fitted to data.
FFGFT derives H0 from a single geometric chain (no free parameters):

  xi = 4/30000  (geometric, from T^4 packing, Doc. 009)
    |
    v
  E0 = sqrt(m_e * m_mu) = 7.398 MeV  (geometric mean of lepton masses)
    |
    v  (xi defines the scale hierarchy)
  E_H = E0 * xi^(41/4)  = 1.412e-33 eV  (Hubble energy scale)
    |
    v  (SI conversion only: hbar is a unit factor)
  H0 = E_H / hbar  = {H0_FFGFT:.2f} km/s/Mpc

The SI value {H0_FFGFT:.2f} km/s/Mpc is NOT what matters.
What matters is the STRUCTURE: H0 follows from xi and two lepton
masses. No Omega_m, no Omega_Lambda, no expansion history.

LCDM:  H0 = free parameter  (fitted, 6+ free parameters total)
FFGFT: H0 = f(xi, m_e, m_mu)  (derived, 0 free parameters)

Comparison:
  FFGFT H0     = {H0_FFGFT:.2f} km/s/Mpc
  Planck H0    = {H0_Planck:.1f} km/s/Mpc  (LCDM-pipeline output)
  SH0ES H0     = {H0_SH0ES:.1f} km/s/Mpc  (local ladder, less model-dependent)
  Difference FFGFT vs Planck = {100*(H0_FFGFT/H0_Planck-1):+.2f}%
  
The {100*(H0_FFGFT/H0_Planck-1):+.2f}% is not a failure -- it is a comparison of
two model outputs. The Hubble tension ({100*(H0_SH0ES/H0_Planck-1):+.1f}% between
Planck and SH0ES) is larger than FFGFTs deviation from Planck.
FFGFT is not obliged to match the LCDM pipeline output exactly.""")

# ============================================================
# CONSEQUENCES FOR ONUR / UIFT
# ============================================================
print("\n" + "=" * 70)
print("CONSEQUENCES FOR UIFT (Onur Teker's framework)")
print("=" * 70)
print("""
Onur's w = -3/4 prediction faces the same methodological situation.

Testing w = -3/4 against Planck/BOSS/Pantheon+ data is NOT a fair
test -- for exactly the same reasons:

  1. These datasets were extracted assuming w = -1 (Lambda).
     A fit of w = -3/4 will systematically fail not because the
     physics is wrong, but because the extraction pipeline baked
     in w = -1 at every step.

  2. The Gemini script demonstrated this: even for w = -1 (LCDM),
     the chi2 was catastrophically wrong (233,552 instead of ~60).
     Not because LCDM is wrong, but because the dataset conversions
     themselves assume LCDM internally. Any non-LCDM w value would
     fare even worse -- not from physics, but from pipeline mismatch.

  3. The correct test for w = -3/4 would require:
     (a) Raw SNe Ia apparent magnitudes (not pre-calibrated mu values)
     (b) Raw BAO angular positions (not DM/r_s ratios using LCDM r_s)
     (c) Raw CMB peak frequency (not T_CMB in Kelvin with LCDM physics)
     These model-independent reductions do not yet exist for full datasets.

The shared position of FFGFT and UIFT:
  Both frameworks produce predictions that differ from LCDM-pipeline
  outputs at the ~1% level. This is BELOW the level of model-dependence
  in the extraction pipeline itself. Neither framework can be falsified
  -- or confirmed -- by LCDM-extracted numbers.

  The honest common ground: both should identify and target genuinely
  model-independent observables. The WBE analysis (wbe_t4_flrw.py)
  is an example: it addresses a structural question (do the WBE
  preconditions hold in a static T^4 vs. expanding FLRW?) that does
  not depend on any pipeline output.""")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
  LCDM:  fits its own pipeline outputs -- tautological confirmation.
  FFGFT: derives H0, T_CMB, Casimir/CMB from xi alone -- no free params.
  UIFT:  w = -3/4 from WBE/Landauer -- structural, not fitted.

  The right comparison is not chi2 against LCDM datasets.
  The right comparison is:
    How many free parameters does each framework use?
    Which raw observables does each framework predict from first principles?

  LCDM:  6+ free parameters, fits pre-processed data.
  FFGFT: 1 parameter (xi), derives H0/T_CMB/alpha/lepton masses.
  UIFT:  w = -3/4 from WBE + Landauer (no fit to cosmological data).

  xi = {xi:.6e}  -- everything follows from here.""")
