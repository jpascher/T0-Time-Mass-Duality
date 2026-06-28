"""
Dim-Bridge 1: "6 ist die Verdopplung der 3" — exakt: 6 = 3 (+) 3'
Die ikosaedrische (5-zaehlige) Struktur zerfaellt in zwei 3D-Irreps der
Ikosaedergruppe A5, die sich durch phi <-> 1-phi (= -1/phi) unterscheiden.
numpy only.
"""
import numpy as np
phi = (1+5**0.5)/2

def rot_z(deg):
    t = np.deg2rad(deg)
    c,s = np.cos(t), np.sin(t)
    return np.array([[c,-s,0],[s,c,0],[0,0,1.0]])

# 5-fold rotation in the two 3D irreps of A5: geometric (72 deg) and Galois-conjugate (144 deg)
R3  = rot_z(72)     # irrep "3"   (physical icosahedron)
R3p = rot_z(144)    # irrep "3'"  (perp / Galois conjugate)
R6  = np.block([[R3, np.zeros((3,3))],[np.zeros((3,3)), R3p]])  # the 6D rep = 3 (+) 3'

print("=== Dim-Bridge 1: 6 = 3 (+) 3' ===")
print(f"phi = {phi:.6f},  1-phi = {1-phi:.6f},  -1/phi = {-1/phi:.6f}")
print(f"char(5-fold | irrep 3 )  = trace R3  = {np.trace(R3):+.6f}   (= phi)")
print(f"char(5-fold | irrep 3') = trace R3p = {np.trace(R3p):+.6f}   (= 1-phi = -1/phi)")
print(f"char(5-fold | 6D rep   ) = trace R6  = {np.trace(R6):+.6f}   (= 1, INTEGER)")
print(f"orthogonal? R3:{np.allclose(R3@R3.T,np.eye(3))}  R3':{np.allclose(R3p@R3p.T,np.eye(3))}")
print(f"order 5?    R3^5=I:{np.allclose(np.linalg.matrix_power(R3,5),np.eye(3))}  "
      f"R3'^5=I:{np.allclose(np.linalg.matrix_power(R3p,5),np.eye(3))}")
print("VERDICT: the 6D icosahedral rep splits as 3 (+) 3'.  The two 3D blocks differ")
print("         exactly by phi <-> 1-phi.  The 6D character is INTEGER (1) while each")
print("         3D block is IRRATIONAL (phi) -> '6 = doubling of 3' is literal, and the")
print("         golden ratio lives in the split itself (this is HLV's 5-fold / 2/sqrt5).")
