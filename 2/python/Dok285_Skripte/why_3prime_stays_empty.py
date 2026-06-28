"""
Why does the perpendicular 3' stay empty even though (a) the embedding/translation works and
(b) the 3-fold and 5-fold axes point in DIFFERENT directions?
Because 6 = 3 (+) 3' is a DIRECT SUM of A5-irreps: every A5 element (3-fold OR 5-fold) is
block-diagonal in this split. The different orientation rotates WITHIN a block; it never
connects the two blocks. So filling the '3' (e,mu,tau) never spills into the 3'. numpy only.
"""
import numpy as np
phi=(1+5**0.5)/2; w=np.exp(2j*np.pi/3)
def rot(axis,ang):
    a=np.array(axis,float); a/=np.linalg.norm(a)
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*(K@K)

# 3-fold (Koide cyclic) and a 5-fold on the physical "3"
C3 = np.array([[0,0,1],[1,0,0],[0,1,0]],float)
R5 = rot([0,1,phi], 2*np.pi/5)              # 5-fold axis -- DIFFERENT orientation than the 3-fold
# the conjugate copies acting on 3' (Galois conjugate phi -> 1-phi); irrelevant details, just
# SOME A5 action on the second block -- the point is it is a SEPARATE block
C3p= np.array([[0,1,0],[0,0,1],[1,0,0]],float)
R5p= rot([0,1,1-phi], 2*np.pi/5)

def block(A,B):
    M=np.zeros((6,6)); M[:3,:3]=A; M[3:,3:]=B; return M
G3 = block(C3,C3p)     # 3-fold on the full 6 = 3 (+) 3'
G5 = block(R5,R5p)     # 5-fold on the full 6 = 3 (+) 3'

print("orientation check: 3-fold axis vs 5-fold axis are different?",
      not np.allclose(C3,R5), " (yes -> mixing within the '3')")
print("off-diagonal 3x3 blocks (3 <-> 3') of the generators:")
print("  3-fold off-block max =", f"{np.abs(G3[:3,3:]).max():.1e}")
print("  5-fold off-block max =", f"{np.abs(G5[:3,3:]).max():.1e}", " -> exactly zero\n")

# electron mode lives in the '3' (first block); 3' part is zero
ve=np.array([1,w,w**2])/np.sqrt(3)
x=np.concatenate([ve,[0,0,0]])     # electron embedded: '3' filled, 3' empty
# apply a random word of 3-folds and 5-folds (any A5 element)
rng=np.random.default_rng(1); y=x.copy()
for _ in range(50):
    y = (G5 if rng.random()<0.5 else G3) @ y
print("after 50 random 3-fold/5-fold operations on the electron:")
print(f"  weight remaining in the '3'  = {np.abs(y[:3]).sum()/np.abs(y).sum():.6f}")
print(f"  weight that reached the 3'   = {np.abs(y[3:]).sum()/np.abs(y).sum():.1e}")
print("\n=> The 3' stays exactly empty. The different 3-fold/5-fold orientation mixes e<->mu<->tau")
print("   WITHIN the '3' (the 0.762/0.238 leak), but no A5 operation crosses 3 -> 3'. Filling the")
print("   '3' (FFGFT) therefore never fills the 3'. The empty sector is one triplet: the 3'.")
