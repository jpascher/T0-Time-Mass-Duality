"""
Dim-Bridge 2: Dreiecke sind fundamentaler (3 genuegen), Fuenfecke brauchen die 6.
Crystallographic restriction theorem: a rotation of order n is a lattice symmetry
in 2D/3D iff 2 cos(2 pi / n) is an INTEGER.
numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2
print("=== Dim-Bridge 2: 3-fold crystallographic, 5-fold not ===")
print(" n  | 2 cos(2pi/n) | integer? | crystallographic in 3D?")
for n in range(1,9):
    v = 2*np.cos(2*np.pi/n)
    isint = abs(v-round(v))<1e-9
    print(f" {n:>2} | {v:>11.6f} | {str(isint):>7} | {'YES' if isint else 'NO'}")
print()
def rot_z(deg):
    t=np.deg2rad(deg); c,s=np.cos(t),np.sin(t)
    return np.array([[c,-s,0],[s,c,0],[0,0,1.0]])
R3fold = rot_z(120)   # triangle / 3-fold (FFGFT, Z3)
R5fold = rot_z(72)    # pentagon  / 5-fold (HLV)
print(f"3-fold (triangle): trace = {np.trace(R3fold):+.6f}  -> integer, lives in 3D (crystallographic)")
print(f"5-fold (pentagon): trace = {np.trace(R5fold):+.6f}  -> = phi, IRRATIONAL -> no 3D lattice")
print("   but in 6D the 5-fold has integer character (Bridge 1: trace=1) -> a 6D lattice exists.")
print("VERDICT: 3-fold (Z3, Koide) is crystallographic -> 3 dimensions SUFFICE (FFGFT).")
print("         5-fold (icosahedral) is non-crystallographic -> REQUIRES the 6D embedding (HLV).")
print("         The triangle is the more fundamental (minimal) carrier.")
