"""
What could sit in the empty 3'? OPEN question -- a conditional target, not a prediction.
Discriminator = Koide ratio Q = sum(m) / (sum(sqrt m))^2.  Conditional 3' target: Q = 7/15.
Check the candidate physical triples. numpy only. Masses approximate (PDG-ish).
"""
import numpy as np
def Q(m):
    m=np.array(m,float); return m.sum()/ (np.sqrt(m).sum()**2)
target=7/15
print(f"conditional 3' target  Q = 7/15 = {target:.4f}\n")
print("measured triples (the '3' is the charged leptons, Q=2/3):")
for name,m in [("charged leptons e,mu,tau (MeV)",[0.51099895,105.6583755,1776.86]),
               ("up quarks u,c,t (MeV)",        [2.16,1273.0,172570.0]),
               ("down quarks d,s,b (MeV)",      [4.67,93.4,4180.0])]:
    q=Q(m); print(f"  {name:32s} Q = {q:.4f}   {'<- = target' if abs(q-target)<0.01 else ('far above target' if q>target+0.05 else '')}")
print("  => leptons/up/down all give Q >= 0.67: none matches 7/15. Excluded as a 7/15 carrier.\n")

print("neutrinos: absolute scale unknown -> Q not fixed. Scan lightest mass m0 (normal ordering):")
d21,d31=7.42e-5,2.515e-3   # eV^2
def Qnu(m0):
    m1=m0; m2=np.sqrt(m0**2+d21); m3=np.sqrt(m0**2+d31); return Q([m1,m2,m3]),(m1+m2+m3)
prev=None; cross=None
for m0 in np.linspace(0,0.02,4001):
    q,s=Qnu(m0)
    if prev is not None and (prev[0]-target)*(q-target)<=0 and cross is None:
        cross=(m0,q,s)
    prev=(q,s)
q0,s0=Qnu(0.0)
print(f"  m0 = 0 (hierarchical): Q = {q0:.4f}, sum m_nu = {s0*1000:.2f} meV")
if cross: print(f"  Q = 7/15 reached at m0 ~ {cross[0]*1000:.2f} meV  (sum m_nu ~ {cross[2]*1000:.1f} meV, within cosmology bound ~120 meV)")
print("  => neutrinos are the only NON-excluded candidate; Q=7/15 would fix the absolute scale.\n")

print("STATUS (disciplined):")
print(" - up/down quarks and charged leptons: excluded as 7/15 carriers (measured Q too high).")
print(" - neutrinos: the open candidate; Q=7/15 translates into a specific lightest-nu mass.")
print(" - BUT Q sweeps continuously with m0, so hitting 7/15 is only meaningful if 7/15 is")
print("   independently fixed by a specified dynamics (the missing piece) and beats a null.")
print(" - So: carrier candidate = neutrinos, observable = Koide Q, null control = vs generic.")
print("   Conditional target, NOT a prediction. Needs the dynamics (Dok 285 'gap' section).")
