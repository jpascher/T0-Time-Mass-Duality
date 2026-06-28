"""
Does the quasicrystal spectrum carry information? A quasicrystal has TWO different spectra:
 (a) STRUCTURE/diffraction spectrum S(q) = |sum exp(i q x_n)|^2  -> PURE POINT (sharp Bragg
     peaks) for a quasicrystal, FLAT/diffuse for a random null. This is the information that
     distinguishes the substrate from a null model -- exactly Marcel's HLV point.
 (b) ENERGY/Laplacian spectrum -> singular-continuous (Cantor), no sharp levels -> why no masses.
The 'no content' caveat (P35) applies ONLY to fitting a single target number as phi^N, not to (a).
numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2
def fib_word(k):
    a,b="A","B"
    for _ in range(k): a,b=a+b,a
    return a
w=fib_word(15); L,S=1.0,1/phi
def positions(seq):
    x=[0.0]
    for c in seq[:-1]: x.append(x[-1]+(L if c=="A" else S))
    return np.array(x)
xq=positions(w)
rng=np.random.default_rng(0); rseq=list(w); rng.shuffle(rseq); xr=positions(rseq)
def Sq(x,qs): return np.array([np.abs(np.sum(np.exp(1j*q*x)))**2 for q in qs])/len(x)
qs=np.linspace(0.05,25,6000)
Q=Sq(xq,qs); R=Sq(xr,qs)
print(f"chain length N={len(xq)} (same tiles, same composition for both)")
print("(a) STRUCTURE / diffraction spectrum:")
print(f"   Fibonacci quasicrystal: max S(q)={Q.max():.1f}  sharp peaks (S>3): {(Q>3).sum()}  -> PURE POINT")
print(f"   random null (shuffled):  max S(q)={R.max():.1f}  sharp peaks (S>3): {(R>3).sum()}  -> diffuse")
print(f"   contrast ratio (quasicrystal/null peak): {Q.max()/max(R.max(),1e-9):.1f}x")
top=qs[np.argsort(Q)[::-1][:5]]; print(f"   top quasicrystal peak q-values: {np.round(np.sort(top),3)}")
print("   => the substrate IS strongly distinguishable from the null model: that is the information.\n")
print("(b) ENERGY spectrum (from spectrum_to_mass.py): singular-continuous (Cantor), no sharp")
print("    isolated levels -> no mass readout. DIFFERENT spectrum from (a).\n")
print("Resolution: information lives in the STRUCTURE spectrum (pure point, relational/long-range")
print("order), not in individual energy levels. Marcel's substrate-distinguishability stands;")
print("the 'no masses' point was only about the energy spectrum. phi^N-fitting a single number")
print("is the only thing that is content-free (P35).")
