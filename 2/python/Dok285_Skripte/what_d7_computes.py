"""
ξ -> masses (FFGFT, 3-fold). What does the d7 model (T^7, A_5, 5-fold) compute?
Honest side-by-side of what each PROTECTED sector outputs. numpy only.
Koide-circulant:  sqrt(m_k) = 1 + A cos(2 pi k/3 + theta),  Q = (2 + A^2)/6  (indep. of theta)
"""
import numpy as np
xi  = 4/30000
phi = (1+5**0.5)/2

def Q(A): return (2+A**2)/6

print("=== protected invariants: what each sector fixes ===")
print(f" FFGFT (3-fold, crystallographic):  A=sqrt2={2**0.5:.5f}  theta=2/9={2/9:.5f}  Q={Q(2**0.5):.5f} (=2/3)")
print(f" d7/HLV (5-fold, icosahedral):      A=2/sqrt5={2/5**0.5:.5f}  theta=0          Q={Q(2/5**0.5):.5f} (=7/15)")
print("   -> the Koide NUMBER for the 5-fold sector is fixed (7/15); the physical CARRIER is open.\n")

print("=== crystallographic test (why masses live in the 3-fold, not the 5-fold) ===")
for n,name in [(3,'3-fold'),(5,'5-fold')]:
    v=2*np.cos(2*np.pi/n); print(f"   2cos(2pi/{n}) = {v:+.5f}  {'integer -> crystallographic' if abs(v-round(v))<1e-9 else 'NON-integer (=1/phi) -> needs the 6D embedding'}  [{name}]")
print("   => mass ratios sit in the crystallographic 3-fold = FFGFT core; d7 CONTAINS it,")
print("      so d7 reproduces those masses THROUGH its FFGFT sub-part, not as new output.\n")

print("=== recursion / ladder scale: xi vs phi ===")
print(f" FFGFT step xi   = {xi:.3e}   |ln xi| = {abs(np.log(xi)):.4f}  -> sparse, near-crystalline")
print(f" d7    step phi  = {phi:.5f}   ln phi  = {np.log(phi):.4f}  -> dense golden tower / log-periodic")
tower=[phi**n for n in range(7)]
print("   golden tower phi^n (n=0..6): "+", ".join(f"{t:.3f}" for t in tower))
print("   (FFGFT ladder is xi^n: 1, 1.3e-4, 1.8e-8, ... -- a different kind of ladder)\n")

print("=== what d7 ACTUALLY computes (different KIND of observable) ===")
print(" 1. protected amplitude 2/sqrt5 and Koide-analog Q=7/15        [derived numbers]")
print(" 2. rigid phase theta_HLV = 0 (no free Koide angle)            [derived]")
print(" 3. golden inflation scale phi; tower phi^n; log-period ln phi [derived]")
print(" 4. aperiodic QUASICRYSTAL gap spectrum w/ phi-scaling          [empirical discriminator,")
print("    vs FFGFT's periodic T^4 harmonic peaks from D=4]            Dok 271/283")
print(" 5. OPEN slot: the 3' perp irrep (char 1-phi=-1/phi) is a second triplet position;")
print("    IF a physical triple sits there it would carry Q=7/15 -- a falsifiable target,")
print("    NOT a derived particle mass. (conjecture, marked)")
print("\n=== what d7 does NOT give ===")
print(" - no second route to the lepton masses (those are the 3-fold/xi output it contains)")
print(" - no phi^N mass formula: writing a mass as phi^N is the P35 numerology trap, no content")
