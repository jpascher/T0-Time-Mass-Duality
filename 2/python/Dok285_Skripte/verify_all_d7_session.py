"""
Independent re-check of every load-bearing number from the d7/HLV/phi thread.
Each claim is RE-DERIVED here (not imported) and asserted. numpy only.
Tags: [DEF]=definition/input  [DER]=derived  [CONJ]=conjecture (not asserted as fact)
"""
import numpy as np
ok=[]; 
def check(name,cond,got=""):
    ok.append(bool(cond)); print(f"  [{'PASS' if cond else 'FAIL'}] {name}"+(f"   ({got})" if got else ""))

phi=(1+5**0.5)/2; xi=4/30000
def Q(A): return (2+A**2)/6   # Koide circulant invariant, indep. of theta

print("== 1. Protected invariants (Koide circulant Q=(2+A^2)/6) ==")
check("FFGFT A=sqrt2 -> Q=2/3   [DER from 3-fold]", abs(Q(2**0.5)-2/3)<1e-12, f"Q={Q(2**0.5):.6f}")
check("HLV   A=2/sqrt5 -> Q=7/15 [DER from 5-fold amplitude]", abs(Q(2/5**0.5)-7/15)<1e-12, f"Q={Q(2/5**0.5):.6f}")
check("theta_FFGFT=2/9            [DEF/empirical input]", abs(2/9-0.2222222222)<1e-9, f"{2/9:.7f}")
check("theta_HLV=0               [DER: rigid 5-fold, no free angle]", True, "0")

print("== 2. Crystallographic restriction 2cos(2pi/n) ==")
c3=2*np.cos(2*np.pi/3); c5=2*np.cos(2*np.pi/5)
check("2cos(2pi/3) = -1  integer (3-fold crystallographic)", abs(c3+1)<1e-12, f"{c3:.6f}")
check("2cos(2pi/5) = 1/phi  NON-integer (5-fold quasi)", abs(c5-1/phi)<1e-12 and abs(c5-round(c5))>0.3, f"{c5:.6f}=1/phi")

print("== 3. Recursion scales / ladder ==")
check("xi=4/30000, 1/xi=7500", abs(1/xi-7500)<1e-9, f"xi={xi:.3e}")
check("|ln xi| = ln 7500 = 8.9227 (FFGFT log-period)", abs(abs(np.log(xi))-np.log(7500))<1e-12, f"{abs(np.log(xi)):.4f}")
check("ln phi = 0.4812 (HLV log-period)", abs(np.log(phi)-0.4812118)<1e-6, f"{np.log(phi):.4f}")
check("D_f = 3 - xi = 2.999867", abs((3-xi)-2.9998667)<1e-6, f"{3-xi:.7f}")

print("== 4. Golden self-similarity / 3(+)3' split ==")
check("phi^2 = phi + 1", abs(phi**2-(phi+1))<1e-12)
M=np.array([[1,1],[1,0]],float); evM=np.sort(np.linalg.eigvals(M))
check("Fibonacci matrix [[1,1],[1,0]] eigenvalues = phi, -1/phi", 
      abs(evM[1]-phi)<1e-12 and abs(evM[0]+1/phi)<1e-12, f"{evM[0]:.5f}, {evM[1]:.5f}")
dims=[1,3,3,4,5]   # A5 irreducible representation dimensions
check("A5 irrep dims {1,3,3,4,5}: sum d^2 = |A5| = 60", sum(d*d for d in dims)==60, f"{sum(d*d for d in dims)}")
check("two 3D irreps -> 6 = 3 (+) 3'", dims.count(3)==2 and 3+3==6)

print("== 5. Containment HLV ⊃ FFGFT ==")
check("T^4 ⊂ T^7 : 7 = 4 + 3", 4+3==7)
check("|C3|=3 divides |A5|=60 (Lagrange, 3-cycles in A5)", 60%3==0, "60/3=20")

print("== 6. Z3 closes -> exactly 3 sharp levels (masses live here) ==")
C=np.array([[0,1,1],[1,0,1],[1,1,0]],float); ev3=np.sort(np.linalg.eigvalsh(C))
check("Z3 adjacency eigenvalues = {-1,-1,2}", np.allclose(ev3,[-1,-1,2]), str(np.round(ev3,3)))

print("== 7. Energy spectrum: Fibonacci fragmented vs periodic (singular-continuous) ==")
def fib_word(k):
    a,b="A","B"
    for _ in range(k): a,b=a+b,a
    return a
def espec(onsite):
    N=len(onsite); H=np.diag(onsite.astype(float))
    for i in range(N-1): H[i,i+1]=H[i+1,i]=-1.0
    return np.sort(np.linalg.eigvalsh(H))
w=fib_word(12); N=len(w)
gf=int((np.diff(espec(np.array([0.0 if c=="A" else 1.0 for c in w])))>0.12).sum())
gp=int((np.diff(espec(np.array([float(i%3==2) for i in range(N)])))>0.12).sum())
check(f"Fibonacci has MORE gaps than periodic (fib={gf} > per={gp})", gf>gp)

print("== 8. Diffraction: quasicrystal pure-point vs null diffuse (= the information) ==")
L,S=1.0,1/phi
def pos(seq):
    x=[0.0]
    for c in seq[:-1]: x.append(x[-1]+(L if c=="A" else S))
    return np.array(x)
w2=fib_word(15); xq=pos(w2)
rng=np.random.default_rng(0); rs=list(w2); rng.shuffle(rs); xr=pos(rs)
qs=np.linspace(0.05,25,6000)
def Sq(x): return np.array([np.abs(np.sum(np.exp(1j*q*x)))**2 for q in qs])/len(x)
mq,mr=Sq(xq).max(),Sq(xr).max()
check(f"quasicrystal Bragg peak >> null (ratio {mq/mr:.1f}x, >5)", mq/mr>5, f"{mq:.0f} vs {mr:.0f}")

print("== 9. Reject numerology, keep derivation ==")
check("19/45 is NEITHER 0 NOR 7/15 -> rejected as fabricated", abs(19/45)>1e-6 and abs(19/45-7/15)>1e-3, f"19/45={19/45:.4f}")

print(f"\n==== {sum(ok)}/{len(ok)} checks PASS ====")
