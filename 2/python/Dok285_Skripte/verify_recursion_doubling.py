"""
Verification (PASS/FAIL) of the claims in 'The 3' is the first recursion'.
Each claim re-derived and asserted. numpy only.
"""
import numpy as np
ok=[]
def chk(name,cond,got=""):
    ok.append(bool(cond)); print(f"  [{'PASS' if cond else 'FAIL'}] {name}"+(f"   ({got})" if got else ""))

phi=(1+5**0.5)/2
M=np.array([[1,1],[1,0]],float)
ev=np.sort(np.linalg.eigvals(M).real)   # [-1/phi, phi]

print("== the doubling operator M=[[1,1],[1,0]] ==")
chk("eigenvalues = {-1/phi, phi}", np.allclose(ev,[-1/phi,phi]), f"{ev[0]:.5f}, {ev[1]:.5f}")
chk("trace M = 1 (= phi + (-1/phi))", abs(np.trace(M)-1)<1e-12)
chk("det M = -1 (= phi * (-1/phi))", abs(np.linalg.det(M)+1)<1e-9)
chk("characteristic poly lam^2 - lam - 1 = 0 for both", all(abs(l*l-l-1)<1e-9 for l in ev))
chk("golden relation phi^2 = phi + 1", abs(phi**2-(phi+1))<1e-12)

print("== the Galois conjugate that distinguishes 3 and 3' IS the contracting eigenvalue ==")
chk("1 - phi = -1/phi", abs((1-phi)-(-1/phi))<1e-12, f"{1-phi:.5f}")
chk("expanding |phi|>1 (physical '3')", abs(phi)>1, f"{phi:.5f}")
chk("contracting |-1/phi|<1 (internal '3'')", abs(1/phi)<1, f"{-1/phi:.5f}")

print("== M is the Fibonacci operator: M^n = [[F(n+1),F(n)],[F(n),F(n-1)]] ==")
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
fibok=True
for n in [1,2,3,5,8,12]:
    Mn=np.linalg.matrix_power(M,n)
    if not np.allclose(Mn,[[fib(n+1),fib(n)],[fib(n),fib(n-1)]]): fibok=False
chk("M^n entries are Fibonacci numbers (n=1..12)", fibok)

print("== under iteration the internal '3'' branch -> 0 (empty), physical '3' grows ==")
_,U=np.linalg.eig(M); 
vph=U[:,int(np.argmax(np.linalg.eigvals(M).real))]; vin=U[:,int(np.argmin(np.linalg.eigvals(M).real))]
x=np.array([1.0,0.3]); 
ratios=[]
for n in range(0,21):
    y=np.linalg.matrix_power(M,n)@x
    ratios.append(abs(np.dot(y,vin))/abs(np.dot(y,vph)))
geom = all(ratios[n+1] < ratios[n] for n in range(len(ratios)-1))   # monotone decreasing
chk("internal/physical ratio decreases monotonically to 0", geom and ratios[-1]<1e-3, f"n=20: {ratios[-1]:.2e}")
chk("decay rate per step ~ 1/phi^2", abs(ratios[10]/ratios[9]-1/phi**2)<1e-3, f"{ratios[10]/ratios[9]:.4f} vs {1/phi**2:.4f}")

print(f"\n==== {sum(ok)}/{len(ok)} checks PASS ====")
