#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doc 283 -- plots of the results
===============================
Reads nothing external: re-derives the same numbers as the Dok283 scripts and
draws them. Produces one overview figure plus standalone panels in ./figures/.
matplotlib + numpy (+ scipy for the kernel fit if present).

Panels:
  A  r(tau) = 2 tau/(1+tau^2) is capped at 1  -> FFGFT's sqrt2 is unreachable
  B  Koide Q per charge sector vs the 3 reference orders (only leptons at 2/3)
  C  crystallographic restriction: 2cos(2pi/n), 5-fold forbidden, 2cos72=1/phi
  D  chi-memory kernel vs baselines (generic biexponential reproduces it)
  E  connection-Laplace witness: blind to gauge, detects flux (Stufe-0)
  F  the 6x6 column inner products: a single magnitude 1/sqrt5
  G  generic projected points fill g1/g0 in [-1/2,1]; protected give only +-1/sqrt5
  H  rational approximant: r, Koide Q converge to 2/sqrt5, 7/15
"""
import numpy as np, os, itertools
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    from scipy.optimize import curve_fit; HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False

os.makedirs("figures", exist_ok=True)
HLV, FFG, NEU, GEN = "#c2410c", "#1d4ed8", "#475569", "#94a3b8"   # colours
PHI = (1+np.sqrt(5))/2; SIGMA = -1/PHI
R3 = np.array([[0,0,1.],[1,0,0],[0,1,0]])
def projector(tau):
    P = np.array([[1.,-1,0,0,tau,tau],[tau,tau,1,-1,0,0],[0,0,tau,tau,1,-1]])
    return P/np.linalg.norm(P,axis=0,keepdims=True)
def koide(r): return (1+r**2/2)/3

# ---------- A: r(tau) cap ----------
def panel_A(ax):
    t = np.linspace(0.02, 8, 400); r = 2*t/(1+t*t)
    ax.plot(t, r, color=HLV, lw=2)
    ax.axhline(1, ls=":", color=GEN); ax.axhline(np.sqrt(2), ls="--", color=FFG)
    ax.scatter([PHI], [2/np.sqrt(5)], color=HLV, zorder=5)
    ax.annotate("HLV  $r=2/\\sqrt{5}$\n(at $\\tau=\\varphi$)", (PHI, 2/np.sqrt(5)),
                xytext=(PHI+1.2, 0.62), color=HLV, fontsize=8,
                arrowprops=dict(arrowstyle="->", color=HLV))
    ax.text(5.2, np.sqrt(2)+0.03, "FFGFT  $r=\\sqrt{2}$  (unreachable)", color=FFG, fontsize=8)
    ax.text(5.2, 1.02, "cap $r\\leq1$", color=GEN, fontsize=8)
    ax.set_xlabel("$\\tau$ (cut-and-project parameter)"); ax.set_ylabel("$r$")
    ax.set_title("A  No $\\tau$ reaches $\\sqrt{2}$", fontsize=10, loc="left")
    ax.set_ylim(0, 1.6)

# ---------- B: sector Koide ----------
SECTORS = {"leptons\n$e\\mu\\tau$":[0.51099895,105.6583755,1776.86],
           "up\n$uct$":[2.16,1270.,172690.], "down\n$dsb$":[4.67,93.4,4180.],
           "vec.mes.\n$\\rho\\omega\\phi$":[775.26,782.66,1019.461],
           "baryons\n$pn\\Lambda$":[938.272,939.565,1115.683],
           "$\\nu$ (NO)\n$m_1{=}0$":[0.0,8.678e-3,4.953e-2]}
def panel_B(ax):
    names=list(SECTORS); Q=[np.sum(m)/np.sum(np.sqrt(m))**2 for m in SECTORS.values()]
    cols=[FFG if n.startswith("leptons") else (NEU if n.startswith("$\\nu$") else HLV) for n in names]
    ax.bar(range(len(Q)), Q, color=cols, width=0.62, zorder=3)
    for ref,lab,c in [(2/3,"3-fold $2/3$",FFG),(7/15,"5-fold $7/15$",HLV),(1/3,"degenerate $1/3$",GEN)]:
        ax.axhline(ref, ls="--", color=c, lw=1)
        ax.text(len(Q)-0.4, ref+0.004, lab, color=c, fontsize=7, ha="right")
    ax.set_xticks(range(len(Q))); ax.set_xticklabels(names, fontsize=7)
    ax.set_ylabel("Koide $Q$"); ax.set_ylim(0.30, 0.92)
    ax.set_title("B  Only the charged leptons sit at $Q=2/3$", fontsize=10, loc="left")

# ---------- C: crystallographic restriction ----------
def panel_C(ax):
    ns=np.arange(1,13); t=2*np.cos(2*np.pi/ns)
    cryst=[abs(v-round(v))<1e-9 for v in t]
    ax.axhspan(-2,2, color="#dcfce7", alpha=0.5, zorder=0)
    for n,v,c in zip(ns,t,cryst):
        ax.scatter([n],[v], color=(FFG if c else HLV), zorder=3,
                   s=(70 if n in (3,6) else 45))
    ax.axhline(round(t[4]),ls=":",color=GEN)
    ax.annotate("5-fold forbidden\n$2\\cos72°=1/\\varphi$", (5,t[4]),
                xytext=(6.2,0.05), color=HLV, fontsize=8,
                arrowprops=dict(arrowstyle="->",color=HLV))
    ax.text(3,-1.0,"3,6: hexagonal", color=FFG, fontsize=8)
    ax.set_xlabel("rotation order $n$"); ax.set_ylabel("$2\\cos(2\\pi/n)$")
    ax.set_title("C  Crystallographic iff $2\\cos(2\\pi/n)\\in\\mathbb{Z}$", fontsize=10, loc="left")
    ax.set_xticks(ns)

# ---------- D: memory kernel vs baselines ----------
def panel_D(ax):
    t=np.linspace(0,12,400)
    K=sum(w*np.exp(-t/s) for w,s in zip([0.6,0.3,0.1],[0.8,2.5,6.0])); K/=K[0]
    ax.plot(t,K, color="k", lw=2.4, label="target (FFGFT/HLV 3-mode)")
    m_single=lambda t,A,a:A*np.exp(-t/a)
    m_biexp =lambda t,A,a,B,b:A*np.exp(-t/a)+B*np.exp(-t/b)
    def fit(model,p0,bnds):
        if HAVE_SCIPY:
            try: p,_=curve_fit(model,t,K,p0=p0,bounds=bnds,maxfev=200000); return model(t,*p)
            except Exception: pass
        return None
    ys=fit(m_single,[1,1.],([0,.05],[5,50]))
    if ys is not None: ax.plot(t,ys, ls="--", color=HLV, lw=1.6, label="single-exp (weak null)")
    yb=fit(m_biexp,[.6,.8,.4,3.],([0,.05,0,.05],[5,50,5,50]))
    if yb is not None: ax.plot(t,yb, ls=":", color=FFG, lw=2, label="biexponential (generic)")
    ax.set_xlabel("$t$"); ax.set_ylabel("$K(t)$"); ax.legend(fontsize=7, frameon=False)
    ax.set_title("D  Generic biexponential reproduces the kernel", fontsize=10, loc="left")

# ---------- E: connection-Laplace Stufe-0 ----------
def panel_E(ax):
    rng=np.random.default_rng(0)
    def claplace(E,n,ph):
        L=np.zeros((n,n),complex)
        for (i,j),th in zip(E,ph):
            L[i,i]+=1;L[j,j]+=1;L[i,j]+=-np.exp(1j*th);L[j,i]+=-np.exp(-1j*th)
        return (L+L.conj().T)/2
    low=lambda L:float(np.linalg.eigvalsh(L).min())
    def cubic(L_=3):
        idx=lambda x,y,z:(x*L_+y)*L_+z; E=[]
        for x in range(L_):
         for y in range(L_):
          for z in range(L_):
           for d in [(1,0,0),(0,1,0),(0,0,1)]:
            E.append((idx(x,y,z),idx((x+d[0])%L_,(y+d[1])%L_,(z+d[2])%L_)))
        return E,L_**3
    def ring(n=27): return [(i,(i+1)%n) for i in range(n)],n
    carr={"cubic $T^3$":cubic(3), "ring $T^1$":ring(27)}
    EPS=0.8; labels=[]; wg=[]; wf=[]
    for name,(E,n) in carr.items():
        m=len(E); pot=rng.standard_normal(n)
        ctx=np.array([pot[j]-pot[i] for (i,j) in E]); W0=low(claplace(E,n,ctx))
        p2=rng.standard_normal(n)
        wg.append(abs(low(claplace(E,n,ctx+EPS*np.array([p2[j]-p2[i] for (i,j) in E])))-W0)+1e-16)
        wf.append(abs(low(claplace(E,n,ctx+EPS*np.ones(m)))-W0)); labels.append(name)
    x=np.arange(len(labels))
    ax.bar(x-0.2, wg, 0.4, color=GEN, label="pure gauge (exact)")
    ax.bar(x+0.2, wf, 0.4, color=FFG, label="non-exact flux")
    ax.set_yscale("log"); ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("$|\\Delta\\lambda_{\\min}|$"); ax.legend(fontsize=7, frameon=False)
    ax.set_title("E  Witness blind to gauge, detects flux (Stufe-0)", fontsize=10, loc="left")

# ---------- F: 6x6 inner products ----------
def panel_F(ax):
    G6=projector(PHI).T@projector(PHI)
    im=ax.imshow(G6, cmap="RdBu", vmin=-1, vmax=1)
    for i in range(6):
        for j in range(6):
            ax.text(j,i,f"{G6[i,j]:+.2f}",ha="center",va="center",fontsize=6.5,
                    color="white" if abs(G6[i,j])>0.6 else "black")
    ax.set_xticks(range(6)); ax.set_yticks(range(6))
    ax.set_title("F  All off-diagonals $=\\pm1/\\sqrt{5}=\\pm0.447$", fontsize=10, loc="left")
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

# ---------- G: generic vs protected histogram ----------
def panel_G(ax):
    N=np.array(list(itertools.product(range(-3,4),repeat=6)),dtype=float)
    sel=np.linalg.norm(N@projector(SIGMA).T,axis=1)<2.2
    x=(N@projector(PHI).T)[sel]; x=x[np.linalg.norm(x,axis=1)>0.3]
    rr=np.array([(v@(R3@v))/(v@v) for v in x])
    ax.hist(rr, bins=60, color=GEN, alpha=0.8)
    ax.axvline(1/np.sqrt(2), color=FFG, ls="--"); ax.axvline(1/np.sqrt(5), color=HLV)
    ax.axvline(-1/np.sqrt(5), color=HLV)
    ax.text(1/np.sqrt(2)+0.02, ax.get_ylim()[1]*0.8, "$1/\\sqrt{2}$\n($r{=}\\sqrt{2}$)", color=FFG, fontsize=7)
    ax.text(1/np.sqrt(5)+0.02, ax.get_ylim()[1]*0.5, "protected\n$\\pm1/\\sqrt{5}$", color=HLV, fontsize=7)
    ax.set_xlabel("$g_1/g_0$ of a $C_3$ orbit"); ax.set_ylabel("generic points")
    ax.set_title("G  Generic fills $[-\\frac{1}{2},1]$; protected rigid $\\pm1/\\sqrt{5}$", fontsize=10, loc="left")

# ---------- H: approximant convergence ----------
def panel_H(ax):
    F=[1,1]
    for _ in range(11): F.append(F[-1]+F[-2])
    taus=[(F[k+1],F[k]) for k in range(1,11)]
    def orbit_r(tau):
        cols=projector(PHI).T
        perm=[int(np.argmin(np.linalg.norm(cols-R3@v,axis=1))) for v in cols]
        seen=set();orb=[]
        for i in range(6):
            if i in seen: continue
            c,j=[],i
            while j not in seen: seen.add(j);c.append(j);j=perm[j]
            orb.append(c)
        V=projector(tau).T[orb[0]];G=V@V.T
        g0=np.mean(np.diag(G));g1=np.mean(G[~np.eye(3,dtype=bool)]);return 2*g1/g0
    tv=[p/q for p,q in taus]; rv=[orbit_r(p/q) for p,q in taus]; Qv=[koide(r) for r in rv]
    ax.plot(tv, rv, "o-", color=HLV, label="$r$ ($C_3$)")
    ax.plot(tv, Qv, "s-", color=FFG, label="Koide $Q$")
    ax.axhline(2/np.sqrt(5), ls=":", color=HLV); ax.axhline(7/15, ls=":", color=FFG)
    ax.axvline(PHI, ls="--", color=GEN)
    ax.text(PHI-0.02, 0.55, "$\\to\\varphi$", color=GEN, fontsize=8, ha="right")
    ax.text(tv[0], 2/np.sqrt(5)+0.01, "$2/\\sqrt{5}$", color=HLV, fontsize=7)
    ax.text(tv[0], 7/15-0.03, "$7/15$", color=FFG, fontsize=7)
    ax.set_xlabel("$\\tau=F_{n+1}/F_n$"); ax.legend(fontsize=7, frameon=False)
    ax.set_title("H  Compact approximant $\\to 2/\\sqrt{5}$, $7/15$", fontsize=10, loc="left")

panels=[("A",panel_A),("B",panel_B),("C",panel_C),("D",panel_D),
        ("E",panel_E),("F",panel_F),("G",panel_G),("H",panel_H)]

# individual PNGs
for name,fn in panels:
    fig,ax=plt.subplots(figsize=(5,3.6)); fn(ax); fig.tight_layout()
    fig.savefig(f"figures/283_{name}.png", dpi=140); plt.close(fig)
    print(f"  wrote figures/283_{name}.png")

# overview montage
fig,axs=plt.subplots(2,4, figsize=(19,9))
for (name,fn),ax in zip(panels, axs.ravel()): fn(ax)
fig.suptitle("FFGFT $\\leftrightarrow$ HLV (Doc 283): genuine $Z_3$ bridge, 5-fold/3-fold fork, hexagonal not pentagonal",
             fontsize=13)
fig.tight_layout(rect=[0,0,1,0.97])
fig.savefig("figures/283_overview.png", dpi=130); plt.close(fig)
print("  wrote figures/283_overview.png")
print("done.")
