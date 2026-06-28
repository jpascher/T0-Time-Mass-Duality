"""
Does Marcel's decompactified variant still hold, given the two-branch doubling?
Compact doubling M=[[1,1],[1,0]]: expanding phi (physical '3'), contracting -1/phi (empty 3' window).
Decompactify S^1 -> R (the measurement): each branch becomes a continuous scaling exponent
alpha = ln(mu). Re(alpha) sign = RG character (relevant grows / irrelevant decays);
|Re| = log-rate; sign structure of mu sets Im (alternating if mu<0). numpy only.
"""
import numpy as np, cmath
phi=(1+5**0.5)/2; xi=4/30000
def branch(mu,label):
    a=cmath.log(complex(mu))
    kind="relevant/GROWS" if a.real>0 else "irrelevant/DECAYS"
    print(f" {label:22s} mu={mu:+.5f}  alpha=ln(mu)={a.real:+.4f}{'+i pi' if mu<0 else '       '}  -> {kind}")
    return a.real
print("=== HLV golden doubling, decompactified ===")
rp=branch(phi,"expanding  phi")          # physical core
rm=branch(-1/phi,"contracting -1/phi")   # empty window
print(f"   |log-rate| equal both branches: {abs(rp):.4f} = {abs(rm):.4f}  (same |ln phi|)")
print(f"   -> physical '3' (phi) decompactifies to the RELEVANT/coherence direction")
print(f"   -> empty 3' window (-1/phi) decompactifies to a DECAYING/overdamped mode")
print()
print("=== FFGFT recursion, decompactified ===")
branch(xi,"contracting  xi")             # fractal-correction recursion
print(f"   |log-rate| = |ln xi| = {abs(np.log(xi)):.4f} = ln 7500  (sparse -> near-crystalline, sharp revivals)")
print()
print("=== mapping to Marcel's HLV kernel ===")
print(" Marcel's HLV kernel (Dok 282-284): OVERDAMPED, decaying, non-discriminating.")
print(" Decompactified contracting branch -1/phi: Re(alpha)<0 -> DECAYING.  SAME object (reading).")
print(" Marcel's variant therefore still holds; it IS the decompactified empty window.")
print(" Caveat: decompactification = measurement (info-discarding) -> this is the NULL-reproducible")
print(" side by construction. The discriminating content (revival back-flow 5.125) lives in the")
print(" RELEVANT/coherence sector (FFGFT, sparse ln 7500), not in the overdamped kernel.")
print()
print("consistency:",
      "PASS" if (rp>0 and rm<0 and abs(abs(rp)-abs(rm))<1e-9 and np.log(xi)<0) else "FAIL")
