"""
Test A + B : Algebraic claims of Krueger/Feeney/Wende, Medinformatics 2026.

Paper claims:
  (Sec 2.1)  psi = t + i*phi + j*chi  with  i^2 = j^2 = -1,  ij = -ji,
             "analogous to a reduced bicomplex/octonionic plane".
  (Sec 2.10) full operator promoted to an octonionic 8-component object,
             "octonion non-associativity directly matches empirical psychology"
             and is called "the first physics-based explanation for psychological
             nonlinearity".

We check what these relations ACTUALLY generate.
"""
import numpy as np
np.set_printoptions(suppress=True, precision=3)

# ----------------------------------------------------------------------
# Quaternion multiplication (Hamilton): q = (w, x, y, z) ~ w + x i + y j + z k
# ----------------------------------------------------------------------
def qmul(a, b):
    w1,x1,y1,z1 = a; w2,x2,y2,z2 = b
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2,
    ])

ONE = np.array([1,0,0,0.]); I = np.array([0,1,0,0.])
J   = np.array([0,0,1,0.]); K = np.array([0,0,0,1.])

print("="*70)
print("TEST A  -- the triadic-time relations  i^2=j^2=-1, ij=-ji")
print("="*70)
print("i^2 =", qmul(I,I), "  j^2 =", qmul(J,J))
ij = qmul(I,J); ji = qmul(J,I)
print("ij  =", ij, "   ji =", ji, "   ij == -ji ?", np.allclose(ij, -ji))
# define k := ij and test closure
k = ij
print("k:=ij =", k, "   k^2 =", qmul(k,k), " (=-1 ?)", np.allclose(qmul(k,k), -ONE))
# associativity on the generators
lhs = qmul(qmul(I,J),K); rhs = qmul(I,qmul(J,K))
print("associative on i,j,k:  (ij)k == i(jk) ?", np.allclose(lhs, rhs))
# bicomplex test: a bicomplex plane REQUIRES the two imaginary units to COMMUTE
print("bicomplex would need ij == ji ?", np.allclose(ij, ji),
      " -> so the algebra is NOT bicomplex")
print()
print("VERDICT A: {1,i,j} with i^2=j^2=-1, ij=-ji closes on k=ij into the")
print("           QUATERNIONS H (associative, non-commutative). 'Bicomplex'")
print("           is wrong (those units commute). A 3-term operator t+i*phi+j*chi")
print("           lives in a quaternion sub-algebra; octonions are not needed.")
print()

# ----------------------------------------------------------------------
# Octonions via Cayley-Dickson on quaternion pairs:
#   (a,b)(c,d) = (a c - d~ b ,  d a + b c~)     ~ = quaternion conjugate
# 8-vector stored as concatenation [a(4), b(4)]
# ----------------------------------------------------------------------
def qconj(q): return q*np.array([1,-1,-1,-1.])
def omul(p,q):
    a,b = p[:4], p[4:]; c,d = q[:4], q[4:]
    left  = qmul(a,c) - qmul(qconj(d), b)
    right = qmul(d,a) + qmul(b, qconj(c))
    return np.concatenate([left, right])

def e(n):
    v = np.zeros(8); v[n]=1.0; return v

print("="*70)
print("TEST B  -- octonion claim (Sec 2.10)")
print("="*70)
# check imaginary units square to -1
sq_ok = all(np.allclose(omul(e(n),e(n)), -e(0)) for n in range(1,8))
print("all imaginary units e1..e7 square to -1 ?", sq_ok)
# associator [e1,e2,e4] = (e1 e2) e4 - e1 (e2 e4)
def assoc(x,y,z): return omul(omul(x,y),z) - omul(x,omul(y,z))
A = assoc(e(1),e(2),e(4))
print("associator (e1 e2)e4 - e1(e2 e4) =", A)
print("octonions NON-associative ?", not np.allclose(A, np.zeros(8)))
# but quaternion subalgebra IS associative:
A2 = assoc(e(1),e(2),e(3))
print("associator on a quaternionic triple e1,e2,e3 =", A2,
      " -> zero ?", np.allclose(A2, np.zeros(8)))
print()
print("VERDICT B: octonion non-associativity is mathematically REAL (associator")
print("           nonzero for independent imaginary units). That is a fact about")
print("           the algebra O. The step 'this matches / explains psychological")
print("           nonlinearity' is an interpretive analogy, not a mathematical")
print("           consequence -- nothing in the algebra is derived from or tested")
print("           against psychological data.")
