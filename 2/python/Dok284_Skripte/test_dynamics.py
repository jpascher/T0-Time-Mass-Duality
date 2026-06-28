"""
Test F : the dynamical phenomenology (Sec 2.2.3, 2.9, 3.2).

Paper claims the (phi,chi) / (E,M,I) dynamics show:
  - healthy cognition  -> stable INWARD SPIRALS
  - trauma loops       -> LIMIT CYCLES around fixed chi basins
  - identity collapse  -> drift
The only explicitly specified dynamical mechanism with explicit potentials is
the gradient-flow part of the master equation (Eq 3/10/11):
      d Psi / dt = - grad_Psi V_DLHR ( + diffusion + advection + Gamma_axon )
with the DLHR potentials given in Sec 2.4:
   V1(E)=a1 E^2 + b1 E^4
   V2(M)=a2 M^2 + b2 M^3 + c2 E M
   V3(I)=a3 I^2 + c3 E I + d3 M I
   Vcross = g E M I
We integrate the 0-D gradient flow and test for spirals / limit cycles.

KEY FACT (gradient systems): if  dx/dt = -grad V(x)  then
      dV/dt = grad V . dx/dt = -|grad V|^2 <= 0,
so V is a strict Lyapunov function off equilibria. A function that only
decreases cannot return to a previous value => NO periodic orbits, NO limit
cycles, NO sustained spirals are possible. Trajectories go to fixed points
(or diverge). This is independent of the coefficient values.
"""
import numpy as np
from scipy.integrate import solve_ivp
rng = np.random.default_rng(1)

# representative coefficients (any choice; the conclusion is coefficient-independent)
a1,b1 = 1.0,0.5
a2,b2,c2 = 1.0,0.3,0.2
a3,c3,d3 = 1.0,0.2,0.2
g = 0.3

def V(x):
    E,M,I = x
    return (a1*E**2 + b1*E**4
            + a2*M**2 + b2*M**3 + c2*E*M
            + a3*I**2 + c3*E*I + d3*M*I
            + g*E*M*I)

def gradV(x):
    E,M,I = x
    dE = 2*a1*E + 4*b1*E**3 + c2*M + c3*I + g*M*I
    dM = 2*a2*M + 3*b2*M**2 + c2*E + d3*I + g*E*I
    dI = 2*a3*I + c3*E + d3*M + g*E*M
    return np.array([dE,dM,dI])

def rhs(t,x): return -gradV(x)

print("="*70)
print("TEST F  -- does the specified gradient flow produce spirals/limit cycles?")
print("="*70)
n_traj = 40
monotone_violations = 0
endpoints = []
diverged = 0
for _ in range(n_traj):
    x0 = rng.uniform(-1.0,1.0,size=3)
    sol = solve_ivp(rhs,[0,60],x0,t_eval=np.linspace(0,60,1200),rtol=1e-8,atol=1e-10)
    if not sol.success or np.max(np.abs(sol.y))>1e3:
        diverged += 1
        continue
    Vt = np.array([V(sol.y[:,k]) for k in range(sol.y.shape[1])])
    # V must be (weakly) monotonically decreasing
    if np.max(np.diff(Vt)) > 1e-6:
        monotone_violations += 1
    endpoints.append(sol.y[:,-1])

endpoints = np.array(endpoints)
print(f"trajectories integrated      : {n_traj}")
print(f"diverged (runaway)           : {diverged}   <- note: V has a cubic M^3 term,")
print(f"                                  so V is NOT bounded below -> some runaways")
print(f"V(t) non-monotone (any rise) : {monotone_violations}  (should be 0 for a gradient flow)")

# Limit-cycle detector: does any converged trajectory return near an earlier,
# non-initial point (closed orbit)? For a gradient flow it must not.
def has_closed_orbit(y, tol=1e-2):
    T = y.shape[1]
    late = y[:, T//2:]                     # ignore transient
    # check recurrence: min distance between well-separated late samples
    from scipy.spatial.distance import pdist, squareform
    D = squareform(pdist(late.T))
    np.fill_diagonal(D, np.inf)
    # mask near-diagonal (consecutive) samples
    for k in range(D.shape[0]):
        lo,hi = max(0,k-20), min(D.shape[0],k+20)
        D[k,lo:hi] = np.inf
    return D.min() < tol and np.ptp(late,axis=1).max() > 5*tol  # recurs AND still moving

closed = 0
for _ in range(20):
    x0 = rng.uniform(-0.8,0.8,size=3)
    sol = solve_ivp(rhs,[0,80],x0,t_eval=np.linspace(0,80,2000),rtol=1e-9,atol=1e-11)
    if sol.success and np.max(np.abs(sol.y))<1e3:
        if has_closed_orbit(sol.y): closed += 1
print(f"trajectories showing a closed orbit / limit cycle : {closed}  (expected 0)")
print()
print("VERDICT F: the gradient-flow master equation with the paper's own DLHR")
print("           potentials produces only relaxation to fixed points (V strictly")
print("           decreasing) or runaway (the M^3 term makes V unbounded below).")
print("           It CANNOT produce limit cycles or sustained spirals -- a theorem")
print("           for gradient systems. The 'healthy inward spirals / trauma limit")
print("           cycles' phenomenology therefore does NOT follow from the specified")
print("           equations; it would require the advection (lambda_phi d_phi,")
print("           lambda_chi d_chi) or W_oct terms, which are never given concretely.")
print("           As written, the central dynamical picture is asserted, not derived.")
