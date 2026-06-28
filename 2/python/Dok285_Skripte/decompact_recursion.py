"""
Decompactified version of the recursive time.
Compact: time = mass-circle S^1; recursion = discrete dilation lambda^n (n in Z) -- a
         DISCRETE SCALE INVARIANCE (invariance under scaling by lambda only).
Decompactify S^1 -> R (the measurement): the discrete recursion becomes a CONTINUOUS
         dilation flow t -> lambda*t, i.e. t = t0 * lambda^s, s in R. A discrete scale
         invariance in the continuum produces LOG-PERIODICITY of period |ln lambda|
         (equivalently complex scaling exponents spaced 2*pi/|ln lambda|). Standard result.
numpy only.
"""
import numpy as np
xi  = 4/30000
phi = (1+5**0.5)/2

def decompact(lam,label):
    P = abs(np.log(lam))                 # log-period in ln(t)
    dom = 2*np.pi/P                       # spacing of complex exponents Im(alpha)
    print(f" {label}: lambda={lam:.6g}")
    print(f"   continuous flow  t -> lambda*t  (t = t0 * lambda^s, s in R)")
    print(f"   log-period  P = |ln lambda| = {P:.4f}   (period in ln t)")
    print(f"   complex exponents  alpha = alpha0 + i*k*2pi/P,  spacing {dom:.4f}")
    return P

print("=== Decompactified recursive time: discrete lambda^n  ->  continuous log-periodicity ===\n")
print("FFGFT (lambda = xi, contracting):")
Pf = decompact(xi,"FFGFT")
print(f"   ln(1/xi) = ln(7500) = {np.log(1/xi):.4f}  -> VERY long log-period")
print("   => self-similar repeat only every ~8.9 e-folds: barely log-periodic = near-crystalline")
print("   (same discrete scale invariance that gives D_f = 3 - xi)\n")
print("HLV (lambda = phi, golden inflation):")
Ph = decompact(phi,"HLV")
print(f"   ln(phi) = {np.log(phi):.4f}  -> SHORT log-period")
print("   => self-similar repeat every ~0.48 e-folds: dense log-periodicity = full quasicrystal\n")

print("=== unified statement ===")
print(" COMPACT (S^1):        recursion = discrete dilation lambda^n  (discrete scale invariance)")
print(" DECOMPACT (R, =meas): recursion = continuous dilation t->lambda*t = RG/scale flow,")
print("                       seen as LOG-PERIODICITY of period |ln lambda|.")
print(f"   FFGFT |ln xi| = {Pf:.3f} (long, near-crystalline)   HLV |ln phi| = {Ph:.3f} (short, quasicrystal)")
print(" The fork persists: same structure (log-periodic RG flow), different log-period.")
print(" Note: FFGFT's 'recursion R' IS this -- discrete (xi^n) compact, continuous RG-flow decompactified.")
