"""
Does the 'electron' mode have an image in D7? YES (T^4 ⊂ T^7). But 'electron' is a C_3-protected
label, not an A_5-protected one: a 5-fold element of A_5 rotates the electron mode into a
muon/tau mixture, so reading it AS the electron (a sharp mass) requires the C_3 frame = the D4
core. numpy only.
"""
import numpy as np
w=np.exp(2j*np.pi/3); phi=(1+5**0.5)/2
# C_3-protected (Koide/Fourier) modes -- the basis in which masses are sharp
V=np.array([[1,1,1],[1,w,w**2],[1,w**2,w]],dtype=complex)/np.sqrt(3)  # rows v_0,v_1,v_2
# Koide circulant masses  sqrt(m_k)=1+sqrt2 cos(2pi k/3 + 2/9)
A,th=np.sqrt(2),2/9
sm=np.array([1+A*np.cos(2*np.pi*k/3+th) for k in range(3)])
m=sm**2
e_idx=int(np.argmin(m))                      # electron = smallest mass
print("C_3 modes and masses (ratios):")
for k in range(3): print(f"  v_{k}: sqrt(m)={sm[k]:+.4f}  m={m[k]:.5f}{'   <- electron' if k==e_idx else ''}")
v_e=V[e_idx]

# (1) embedding T^4 -> T^7: the electron mode is a D7 mode supported on the T^4 block,
#     zero winding on the extra 3 circles. Its Laplacian eigenvalue (mass) is unchanged.
print("\n(1) Embedding: electron mode lifts to D7 as (D4 winding, 0,0,0) on the extra circles.")
print("    It sits in the periodic '3' irrep block -> point spectrum -> mass unchanged.")

# (2) a genuine 5-fold (icosahedral) rotation about a vertex axis (0,1,phi)
a=np.array([0,1,phi]); a=a/np.linalg.norm(a); t=2*np.pi/5
K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
R5=np.eye(3)+np.sin(t)*K+(1-np.cos(t))*(K@K)
order5=np.allclose(np.linalg.matrix_power(R5,5),np.eye(3))
P=np.array([[0,0,1],[1,0,0],[0,1,0]],float)   # C_3 generator (cyclic)
noncomm=not np.allclose(P@R5,R5@P)
print(f"\n(2) 5-fold R5: order-5 = {order5},  commutes with C_3 = {not noncomm}")

# (3) apply R5 to the electron mode: overlaps onto the C_3 modes
Rve=R5@v_e
c=np.array([np.vdot(V[k],Rve) for k in range(3)])
p=np.abs(c)**2; p/=p.sum()
print("    R5 . (electron) decomposed in the C_3 basis  |<v_k|R5 v_e>|^2:")
for k in range(3): print(f"      onto v_{k}: {p[k]:.3f}{'  (electron)' if k==e_idx else ''}")
print(f"    electron stays pure under C_3 frame, but the 5-fold mixes it: leakage out of the")
print(f"    electron direction = {1-p[e_idx]:.3f} into the mu/tau directions.")

# (4) reading the mass back = project onto the C_3 frame (= go back to D4)
print("\n(4) To read it AS the electron (sharp mass) you must use the C_3 eigenbasis = the D4 core.")
print("    The mode exists in D7; the sharp 'electron' label is a C_3-frame statement.")
print("    Choosing that frame is again the measurement (which directions count as the 3-fold).")
