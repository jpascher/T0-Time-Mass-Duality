"""
Dim-Bridge 3: Beide reduzieren auf DASSELBE 3+1 (ambient) -- aber ist es nur
eine mathematische Transformation? Test am geschuetzten Invariant.
Cut-and-project ratio r(tau)=2 tau/(1+tau^2): the space of cut-and-project
"mathematical transformations". HLV protected = 2/sqrt5 ; FFGFT needs sqrt2.
numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2
r = lambda tau: 2*tau/(1+tau**2)
taus=np.linspace(0,8,100001)
rmax=r(taus).max(); tau_at_max=taus[np.argmax(r(taus))]
hlv=2/np.sqrt(5); ffgft=np.sqrt(2)
print("=== Dim-Bridge 3: same ambient 3+1, but is the structure transformable? ===")
print(f"cut-and-project ratio r(tau)=2tau/(1+tau^2):  max = {rmax:.6f} at tau = {tau_at_max:.4f}")
print(f"   r(phi)   = {r(phi):.6f}   target HLV  2/sqrt5 = {hlv:.6f}   -> reached at tau=phi")
print(f"   FFGFT target sqrt2          = {ffgft:.6f}   -> r(tau) max is {rmax:.4f} < sqrt2 -> NEVER reached")
# is sqrt2 anywhere in the achievable range?
reach_ffgft = np.any(np.isclose(r(taus), ffgft, atol=1e-3))
print(f"   sqrt2 achievable by ANY cut-and-project tau in [0,8]? {reach_ffgft}")
print()
print("INTERPRETATION:")
print(" - AMBIENT space: both models end in R^3 x R_t (3+1). At the level of the bare")
print("   coordinate manifold this IS just a (lossless) representational transformation.")
print(" - STRUCTURE on it: HLV puts an icosahedral (5-fold, 2/sqrt5, reached at tau=phi)")
print("   structure; FFGFT puts a Z3 (3-fold, Koide 2/3, sqrt2) structure.")
print("   sqrt2 lies OUTSIDE the entire cut-and-project range (r<=1) -> NO cut-and-project")
print("   transformation maps HLV's structure onto FFGFT's.")
print("VERDICT: same ambient 3+1 (transformable), but the two STRUCTURES are inequivalent")
print("         -- the fork (Doc 283) is structural, NOT a coordinate artifact.")
print("         'Only mathematical transformations' holds for the embedding, not the physics.")
