"""
Unify the RECURSION in the compact picture for both models.
FFGFT recursion: xi^n (recursion R / fractal correction), D_f = 3 - xi.
HLV recursion:   phi^n -- the golden inflation of the icosahedral quasicrystal,
                 with phi^2 = phi + 1 (Fibonacci substitution).
Claim: both are a self-similar dilation lambda^n by a PROTECTED eigenvalue lambda.
numpy only, fixed values.
"""
import numpy as np
xi = 4/30000
phi = (1+5**0.5)/2

print("=== FFGFT recursion: lambda = xi ===")
print(f" xi = 4/30000 = {xi:.8f}")
Df = 3 - xi
print(f" D_f = 3 - xi = {Df:.6f}   (corpus value 2.999867: {abs(Df-2.999867)<5e-7})")
print(f" recursion xi^n: " + ", ".join(f"{xi**n:.3e}" for n in range(1,5)))
print(" -> contracting only, vanishes fast => near-crystalline, dimension just below 3.")

print("\n=== HLV recursion: lambda = phi (icosahedral / Fibonacci inflation) ===")
print(f" phi = {phi:.8f}")
print(f" recursion relation phi^2 = phi + 1 ?  {np.isclose(phi**2, phi+1)}  ({phi**2:.6f} = {phi+1:.6f})")
M = np.array([[1,1],[1,0]])          # Fibonacci / inflation substitution matrix
ev = np.sort(np.linalg.eigvals(M.astype(float)))
print(f" inflation matrix [[1,1],[1,0]] eigenvalues: {ev[1]:+.6f} (= phi, expanding), {ev[0]:+.6f} (= -1/phi, contracting)")
print(f"   check: phi = {phi:.6f}, -1/phi = {-1/phi:.6f}")
print(f" recursion phi^n: " + ", ".join(f"{phi**n:.4f}" for n in range(1,5)))
print(f" relation to protected invariant: 2/sqrt5 = {2/np.sqrt(5):.6f}; sqrt5 = 2*phi-1 = {2*phi-1:.6f}")
print(" -> expanding(phi)+contracting(-1/phi): self-similar at ALL scales => aperiodic quasicrystal.")
print("    the two eigenvalues phi / -1/phi ARE the physical/perp (3 (+) 3') split.")

print("\n=== unified statement ===")
print(" Recursion in the compact model = self-similar dilation lambda^n by a protected eigenvalue:")
print(f"   FFGFT: lambda = xi  = {xi:.6e}  -> D_f = 3 - xi (near-crystalline, tiny fractal correction)")
print(f"   HLV:   lambda = phi = {phi:.6f}      -> golden inflation phi^2=phi+1 (full quasicrystal)")
print(" Same structure (lambda^n), different lambda -- the fork once more, now in the recursion:")
print(" xi (tiny -> almost integer dimension) vs phi (golden -> genuinely self-similar).")
print(" In each model ONE number governs BOTH the protected geometry AND the recursion.")
