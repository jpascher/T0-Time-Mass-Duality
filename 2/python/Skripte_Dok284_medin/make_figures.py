import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---- shared dynamics (same coefficients as test_dynamics.py) ----
a1,b1=1.0,0.5; a2,b2,c2=1.0,0.3,0.2; a3,c3,d3=1.0,0.2,0.2; g=0.3
def V(x):
    E,M,I=x
    return a1*E**2+b1*E**4+a2*M**2+b2*M**3+c2*E*M+a3*I**2+c3*E*I+d3*M*I+g*E*M*I
def gradV(x):
    E,M,I=x
    return np.array([2*a1*E+4*b1*E**3+c2*M+c3*I+g*M*I,
                     2*a2*M+3*b2*M**2+c2*E+d3*I+g*E*I,
                     2*a3*I+c3*E+d3*M+g*E*M])
rhs=lambda t,x:-gradV(x)
rng=np.random.default_rng(2)

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(11,4.3))
for _ in range(12):
    x0=rng.uniform(-1,1,3)
    s=solve_ivp(rhs,[0,40],x0,t_eval=np.linspace(0,40,800),rtol=1e-8,atol=1e-10)
    ax1.plot(s.y[0],s.y[1],lw=1,alpha=.8)
    ax1.plot(s.y[0,0],s.y[1,0],'o',ms=3,color='k')
    ax1.plot(s.y[0,-1],s.y[1,-1],'*',ms=9,color='crimson')
    ax2.plot(s.t,[V(s.y[:,k]) for k in range(s.y.shape[1])],lw=1,alpha=.8)
ax1.set_xlabel("E  (emotional)"); ax1.set_ylabel("M  (meaning)")
ax1.set_title("Gradient flow -dV: trajectories relax to fixed points\n(* ) - no closed orbits, no sustained spiral")
ax2.set_xlabel("t"); ax2.set_ylabel("V(t)")
ax2.set_title("V(t) monotonically decreasing  ->  Lyapunov function\n=> limit cycles impossible (theorem)")
fig.tight_layout(); fig.savefig("outputs/fig_dynamics.png",dpi=130)
print("wrote outputs/fig_dynamics.png")

# ---- Berry phase vs the [0,1] L1 index ----
ang=np.linspace(0,np.pi,400)
gamma=np.abs(-np.pi*(1-np.cos(ang)))
fig2,ax=plt.subplots(figsize=(6.6,4.3))
ax.plot(np.rad2deg(ang),gamma,lw=2,color='navy',label=r'$|\gamma|$ Berry phase (rad)')
ax.axhspan(0,1,color='green',alpha=.12,label='range of the L1 index  $\\Delta\\Phi\\in[0,1]$')
ax.axhline(0.40,color='crimson',ls='--',lw=1.2,label=r'claimed critical 0.40')
ax.axhline(2*np.pi,color='gray',ls=':',lw=1,label=r'$2\pi$')
ax.set_xlabel("loop cone half-angle (deg)"); ax.set_ylabel("value")
ax.set_title("Two incompatible $\\Delta\\Phi$ definitions\nradian holonomy (0..2$\\pi$)  vs  unitless index (0..1)")
ax.legend(fontsize=8,loc='upper left'); fig2.tight_layout()
fig2.savefig("outputs/fig_deltaphi.png",dpi=130)
print("wrote outputs/fig_deltaphi.png")
