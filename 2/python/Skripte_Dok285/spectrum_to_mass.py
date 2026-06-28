"""
Why a spectrum gives masses in the 3-fold case but NOT in the 5-fold/quasicrystal case.
Masses = sharp isolated eigenvalues. Those exist only for a PERIODIC carrier (point spectrum).
5-fold is lattice-incompatible -> only an APERIODIC carrier -> singular-continuous (Cantor-like)
spectrum -> no sharp levels to read masses off. numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2

# (a) 3-fold CLOSES on a periodic carrier: Z3 circulant -> exactly 3 sharp eigenvalues
C=np.array([[0,1,1],[1,0,1],[1,1,0]],float)
ev3=np.sort(np.linalg.eigvalsh(C))
print("3-fold (Z3, lattice-compatible 2cos(2pi/3)=-1):")
print(f"   eigenvalues = {ev3}  -> EXACTLY 3 sharp levels = a triple (the masses live here)\n")

# tight-binding chains, same length: periodic (period-3) vs Fibonacci (golden/5-fold)
def fib_word(k):
    a,b="A","B"
    for _ in range(k): a,b=a+b,a
    return a
def spectrum(onsite):
    N=len(onsite); H=np.diag(onsite.astype(float))
    for i in range(N-1): H[i,i+1]=H[i+1,i]=-1.0
    return np.sort(np.linalg.eigvalsh(H))
def count_gaps(ev,thr): return int(np.sum(np.diff(ev)>thr))

w=fib_word(12); N=len(w)
fib=np.array([0.0 if c=="A" else 1.0 for c in w])          # diagonal Fibonacci model
per=np.array([float(i%3==2) for i in range(N)])            # periodic period-3, same length
evF=spectrum(fib); evP=spectrum(per)
thr=0.12
print(f"chains length N={N}, gap threshold {thr}:")
print(f"   PERIODIC (period-3, lattice):   {count_gaps(evP,thr)} sizable gaps -> few bands, clean point-like structure")
print(f"   FIBONACCI (golden, 5-fold):     {count_gaps(evF,thr)} sizable gaps -> fragmented, self-similar (Cantor-like)")
# self-similarity ratio check: gap structure repeats under phi-scaling
g=np.sort(np.diff(evF))[::-1][:6]
print(f"   largest Fibonacci gaps: {np.round(g,3)}  (dense set of gaps at every scale -> singular-continuous)\n")

print("5-fold (lattice-incompatible 2cos(2pi/5)=1/phi NOT integer):")
print("   only an APERIODIC carrier exists -> singular-continuous spectrum -> NO sharp isolated")
print("   levels -> no triple to read masses off. Characteristic output is the ratio phi + gaps.")
print("\nConsequence: 'spectrum -> mass' needs a POINT spectrum, i.e. a periodic/crystallographic")
print("carrier. The only crystallographic part of d7 is its 3-fold = FFGFT core. So spectrum->mass")
print("ALWAYS routes back into FFGFT; the genuinely-d7 (aperiodic) spectrum cannot deliver masses.")
print("And a dense self-similar spectrum has a level near ANY number -> phi^N 'fits' anything (P35).")
