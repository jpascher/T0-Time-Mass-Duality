#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HICE pilot — independent implementation of M. Krueger's Hybrid HLV cell architecture
(concept manuscript, June 2026).  This is the "independent codebase" that HICE7 asks for.

It implements the ADMISSIBLE carrier and the decisive gates, faithfully to the manuscript:
  * native 6D parent-lattice backbone  (Z^6 cut-and-project, shell-set adjacency S6)
        -- NO projected-kNN surrogate  (HICE0 rule)
  * U(1) fibre connection on edges + holonomy on short cycles (non-exact channel)
  * connection Laplacian L_A  (Hermitian)
  * HICE1 gauge-null   : exact gradient phase  =>  isospectral to phase-free L_0
  * HICE2 benign-stab. : small benign window shift must NOT be separable (target AUC ~0.5-0.65)
  * HICE3 destructive  : removing holonomy must change the witness
  * HICE4 null-model   : carrier must separate from a degree-matched random graph (AUC high)
  * claim-state ledger : combines the gates per the manuscript's Table 4 logic

Witness (scalar, UNFITTED -> honest AUC, no overfitting):
  lambda2 = spectral gap (2nd-smallest eigenvalue) of the connection Laplacian.

NOTE on phi: per Krueger's PHI5 (negative for phi uniqueness) the projection split is
phi-AGNOSTIC here -- a fixed generic 6D->3D orthogonal split. The test is about holonomy/
stability, not golden-ratio specificity.
"""
import itertools, numpy as np

rng_global = np.random.default_rng(0)

# ---------- fixed generic 6D -> (3+3) orthogonal split (phi-agnostic) ----------
def make_projection(seed=0):
    Q,_ = np.linalg.qr(np.random.default_rng(seed).standard_normal((6,6)))
    return Q[:3], Q[3:]                       # P_par, P_perp  (3x6 each)
PPAR, PPERP = make_projection(0)

# ---------- shell set S6 in Z^6 : norm^2 in {1,2} ----------
def shell_set():
    S=[]
    for i in range(6):
        for s in (1,-1):
            v=[0]*6; v[i]=s; S.append(tuple(v))
    for i,j in itertools.combinations(range(6),2):
        for si in (1,-1):
            for sj in (1,-1):
                v=[0]*6; v[i]=si; v[j]=sj; S.append(tuple(v))
    return S
S6 = shell_set()                              # 12 + 60 = 72 vectors

# ---------- native 6D cut-and-project backbone ----------
def build_backbone(center=np.zeros(3), radius=0.62, N=2):
    rng_pts = np.array(list(itertools.product(range(-N,N+1), repeat=6)), dtype=float)
    perp = rng_pts @ PPERP.T
    acc  = np.linalg.norm(perp - center, axis=1) <= radius
    V    = rng_pts[acc].astype(int)
    idx  = {tuple(n): k for k,n in enumerate(map(tuple, V))}
    edges=set()
    for n in map(tuple, V):
        a=idx[n]
        for s in S6:
            m=tuple(n[i]+s[i] for i in range(6))
            if m in idx:
                b=idx[m]
                if a<b: edges.add((a,b))
    return V, sorted(edges), idx

# ---------- U(1) connection Laplacian ----------
def connection_laplacian(nV, edges, phases):
    L=np.zeros((nV,nV), dtype=complex)
    for (a,b),A in zip(edges, phases):
        U=np.exp(1j*A)
        L[a,a]+=1; L[b,b]+=1
        L[a,b]+=-U; L[b,a]+=-np.conj(U)
    return L

def lambda2(L):
    w=np.linalg.eigvalsh(L); w=np.sort(w.real)
    return w[1] if len(w)>1 else w[0]

def random_phases(nE, seed):       return np.random.default_rng(seed).uniform(-np.pi,np.pi,nE)
def gradient_phases(V, edges, seed):
    th=np.random.default_rng(seed).uniform(-np.pi,np.pi,len(V))
    return np.array([th[b]-th[a] for (a,b) in edges])

# ---------- AUC (rank-based Mann-Whitney, no fitting) ----------
def auc(x_pos, x_neg):
    x_pos=np.asarray(x_pos); x_neg=np.asarray(x_neg)
    allx=np.concatenate([x_pos,x_neg]); r=allx.argsort().argsort()+1
    rp=r[:len(x_pos)].sum()
    a=(rp-len(x_pos)*(len(x_pos)+1)/2)/(len(x_pos)*len(x_neg))
    return max(a,1-a)              # symmetric separability

# ===================================================================
print("="*72); print("HICE PILOT — independent Hybrid-HLV carrier test"); print("="*72)
V, edges, idx = build_backbone()
nV, nE = len(V), len(edges)
print(f"Native 6D backbone: |V|={nV} accepted nodes, |E|={nE} shell edges "
      f"(S6 norm^2 in {{1,2}}); NO projected-kNN. [HICE0 construction]")

# ---- HICE1 gauge-null ----
L0  = connection_laplacian(nV, edges, np.zeros(nE))
errs=[]
for s in range(20):
    LA = connection_laplacian(nV, edges, gradient_phases(V, edges, s))
    errs.append(np.max(np.abs(np.sort(np.linalg.eigvalsh(LA).real)
                              -np.sort(np.linalg.eigvalsh(L0).real))))
p95=np.percentile(errs,95)
gauge_pass = p95 < 1e-9
print(f"\n[HICE1] gauge-null  exact-gradient isospectrality:  p95 err = {p95:.2e}  "
      f"-> {'PASS' if gauge_pass else 'FAIL'}")

# ---- witness ensembles ----
M=20
base   = [lambda2(connection_laplacian(nV, edges, random_phases(nE, 100+s)))   for s in range(M)]

# benign: small window-center shift (harmless)  -> new graph, same rule
Vb, eb, _ = build_backbone(center=np.array([0.05,0.0,0.0]))
benign = [lambda2(connection_laplacian(len(Vb), eb, random_phases(len(eb), 200+s))) for s in range(M)]

# null: degree-matched random rewire of base graph
def degree_matched(nV, edges, seed):
    rg=np.random.default_rng(seed); stubs=[]
    for a,b in edges: stubs+= [a,b]
    rg.shuffle(stubs); ne=set()
    for i in range(0,len(stubs)-1,2):
        a,b=stubs[i],stubs[i+1]
        if a!=b and (min(a,b),max(a,b)) not in ne: ne.add((min(a,b),max(a,b)))
    return sorted(ne)
null = []
for s in range(M):
    en=degree_matched(nV, edges, 300+s)
    null.append(lambda2(connection_laplacian(nV, en, random_phases(len(en), 300+s))))

# destructive: remove holonomy (A=0) vs with-holonomy
destr_off=[lambda2(L0)]*M
withhol = base

auc_benign = auc(base, benign)
auc_null   = auc(base, null)
auc_destr  = auc(withhol, destr_off)

print(f"\n[HICE2] benign-stability  AUC(base vs benign window-shift) = {auc_benign:.3f}  "
      f"target 0.50-0.65  -> {'PASS' if auc_benign<=0.65 else 'FAIL (too separable)'}")
print(f"[HICE4] null-model        AUC(base vs degree-matched rand)= {auc_null:.3f}  "
      f"want HIGH         -> {'PASS' if auc_null>=0.75 else 'WEAK'}")
print(f"[HICE3] destructive       AUC(holonomy on vs off)         = {auc_destr:.3f}  "
      f"want HIGH         -> {'PASS' if auc_destr>=0.75 else 'WEAK'}")

# ---- claim-state ledger (manuscript Table 4) ----
print("\n"+"="*72); print("CLAIM-STATE LEDGER")
print("="*72)
if not gauge_pass:
    state="REJECTED (gauge-null failed)"
elif auc_benign>0.65:
    state="PRECONDITION NOT SATISFIED (benign-stability fail: carrier over-sensitive)"
elif auc_null>=0.75 and auc_destr>=0.75:
    state="CANDIDATE CARRIER (gauge-null + benign-stable + destructive + null-sep all pass)"
else:
    state="INCONCLUSIVE (null/destructive separation too weak)"
print("  ->", state)
print("\nNote: 'candidate carrier' is the strongest admissible status; NOT physical")
print("spacetime, NOT a phi claim (PHI5 negative). HICE5/6/7 (scaling, feature-")
print("attribution, independent backend) remain required before any fingerprint claim.")

# ---- plot ----
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(12,4.8)); fig.patch.set_facecolor("white")
ax[0].hist(base,bins=12,alpha=.6,label="base carrier",color="#1f77b4")
ax[0].hist(benign,bins=12,alpha=.6,label="benign window shift",color="#2ca02c")
ax[0].hist(null,bins=12,alpha=.6,label="degree-matched null",color="#c0392b")
ax[0].set_title(f"Witness λ₂  (HICE2 benign AUC={auc_benign:.2f}, HICE4 null AUC={auc_null:.2f})")
ax[0].set_xlabel("spectral gap λ₂ of connection Laplacian"); ax[0].legend(fontsize=8)
gates=["HICE1\ngauge-null","HICE2\nbenign-stab","HICE3\ndestructive","HICE4\nnull-sep"]
vals=[1.0 if gauge_pass else 0.0, auc_benign, auc_destr, auc_null]
cols=["#2ca02c" if gauge_pass else "#c0392b",
      "#2ca02c" if auc_benign<=0.65 else "#c0392b","#2ca02c","#2ca02c"]
ax[1].bar(gates,vals,color=cols); ax[1].axhline(0.65,ls="--",color="#888",lw=1)
ax[1].text(1.0,0.67,"benign ceiling 0.65",fontsize=8,color="#888")
ax[1].set_ylim(0,1.1); ax[1].set_ylabel("AUC / pass"); ax[1].set_title("HICE gates")
fig.tight_layout(); fig.savefig("hice_pilot.png",dpi=160,bbox_inches="tight")
print("\nplot -> hice_pilot.png")
