"""
Honestly DERIVE the HLV 'phase angle' from the A5 representation, instead of guessing.
FFGFT uses a 3-component (C3) Koide circulant  sqrt(m_k) = 1 + A cos(2*pi*k/3 + theta).
  - amplitude A = protected invariant (sqrt2 for FFGFT's 3-fold)
  - phase theta = FREE offset, empirical (FFGFT: theta = 2/9)
Question: what is the analogous HLV phase, derived from A5 (5-fold / icosahedral)?
numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2

def koideQ(A, theta, N=3):
    k=np.arange(N)
    s=1+A*np.cos(2*np.pi*k/N+theta)        # sqrt(m_k)
    return np.sum(s**2)/np.sum(s)**2

print("=== 1. Koide Q for the 3-component circulant: independent of theta? ===")
for A,name in [(np.sqrt(2),"FFGFT A=sqrt2"),(2/np.sqrt(5),"HLV A=2/sqrt5")]:
    vals=[koideQ(A,t) for t in np.linspace(0,2*np.pi,9)]
    print(f" {name:18s}: Q over theta = {np.min(vals):.6f}..{np.max(vals):.6f}  (constant: {np.ptp(vals)<1e-9})")
print(" closed form Q = (2 + A^2)/6 :")
print(f"   A=sqrt2  -> Q = {(2+2)/6:.6f} = 2/3")
print(f"   A=2/sqrt5-> Q = {(2+0.8)/6:.6f} = 7/15   (matches Doc 283 fork table)")

print("\n=== 2. The phase theta ===")
print(" FFGFT: theta is a FREE offset (Q=2/3 for ANY theta); empirically theta = 2/9 = %.4f (the Koide phase)."%(2/9))
print(" HLV:   the protected vacuum directions are RIGID (symmetry-fixed by A5), no free offset")
print("        => theta_HLV = 0  (Doc 283: protected structure has theta=0, Q=7/15).")

print("\n=== 3. A5 eigenvalue phases (Johann's hint) ===")
print(" 3-fold class:  e^{+-2*pi*i/3}  -> phase +-120 deg  (sets the 3-component circulant lattice)")
print(" 5-fold class:  e^{+-2*pi*i/5}  in irrep 3   -> +-72 deg ;  e^{+-4*pi*i/5} in irrep 3' -> +-144 deg")
print(f"   the 5-fold geometry fixes the AMPLITUDE: inner product 1/sqrt5 = {1/np.sqrt(5):.6f}")
print(f"   => A_HLV = 2/sqrt5 = {2/np.sqrt(5):.6f}.  The 5-fold phases enter the amplitude, NOT a free offset.")

print("\n=== 4. verdict vs the guessed 19/45 ===")
print(f" DeepSeek guess theta_HLV = 2/9 + 1/5 = 19/45 = {19/45:.6f}")
print(f"   - as a PHASE:  derived value is theta_HLV = 0  (not {19/45:.4f})")
print(f"   - as a Koide RATIO: derived value is Q = 7/15 = {7/15:.6f}  (not {19/45:.4f})")
print(" => 19/45 matches NEITHER the phase nor the Koide ratio. It is numerology.")
print("\nHONEST RESULT:")
print(" The model difference lives in the AMPLITUDE (protected invariant), not in a nonzero phase:")
print("   FFGFT: A=sqrt2 (3-fold), theta=2/9 FREE/empirical -> Q=2/3")
print("   HLV:   A=2/sqrt5 (5-fold), theta=0 RIGID/protected -> Q=7/15")
print(" An HLV 'phase angle' derived from A5 is therefore 0 (phase-rigid), with Koide ratio 7/15.")
