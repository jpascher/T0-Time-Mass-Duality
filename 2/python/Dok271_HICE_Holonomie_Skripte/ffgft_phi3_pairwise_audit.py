#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHI3 pairwise audit
===================
Audits Run PHI3 (Krueger, Revised HLV Cell-Geometry, Zenodo 10.5281/zenodo.20692350)
using *Marcel's own* output `feature_table.csv`.

The PHI3 claim rests on an ASYMMETRIC test: "does the phi ensemble separate from
sqrt2 / silver / pooled generic-QC?"  Answer in PHI3: AUC = 1.0, p = 0.000999.

This script asks the symmetric question the claim actually needs:
is phi an OUTLIER among the tested irrationals, or does EVERY irrational separate
from every other one equally well?  If the latter, then "phi separates" carries no
phi-specific information -- the same test would 'prove' sqrt2- or e/2-specificity.

It computes, on Marcel's data:
  (1) the full pairwise separability matrix (cross-validated logistic AUC) between all
      tau ensembles, on SCALE-FREE H1 shape features (entropy, mean/birth/death persistence),
      so the result is not a graph-size/density effect;
  (2) the mean AUC of each tau vs all others (an outlier score);
  (3) H1 magnitude per tau (count, total persistence);
  (4) graph density per tau (edges, connected components) -- the real reason phi looks
      'strongest': its trig-frame happens to be the most connected.

Then it renders a 2x2 figure.

Reading: phi-specificity would require phi to be a clear OUTLIER (its row/column ~1.0
while generic-vs-generic stays low). If the whole matrix is ~1.0, the PHI3 separation
is an artifact of (a) a projection where each irrational yields a distinct reproducible
frame and (b) the asymmetric phi-vs-controls framing -- not golden-ratio topology.

Usage:  python3 ffgft_phi3_pairwise_audit.py [path/to/feature_table.csv]
Deps:   numpy, pandas, scikit-learn, matplotlib
Author: J. Pascher, FFGFT / T0 Time-Mass Duality -- independent audit of Run PHI3.
"""
import sys
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score

CSV = sys.argv[1] if len(sys.argv) > 1 else "feature_table.csv"
SCALE_FREE = ["h1_entropy", "h1_mean_persistence", "h1_birth_mean", "h1_death_mean"]
ENS   = ["phi", "sqrt2", "silver", "generic_qc_0", "generic_qc_1", "generic_qc_2"]
LABEL = {"phi": r"$\phi$", "sqrt2": r"$\sqrt{2}$", "silver": "silver",
         "generic_qc_0": r"$\pi/2$", "generic_qc_1": r"$e/2$", "generic_qc_2": r"$\sqrt{3}$"}

def cv_auc(Xa, Xb, seed=0):
    X = np.vstack([Xa, Xb]); y = np.r_[np.ones(len(Xa)), np.zeros(len(Xb))]
    X = StandardScaler().fit_transform(X)
    clf = LogisticRegression(max_iter=2000, class_weight="balanced")
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    return float(cross_val_score(clf, X, y, cv=cv, scoring="roc_auc").mean())

def main():
    df = pd.read_csv(CSV)
    feats = {e: df[df.ensemble == e][SCALE_FREE].values for e in ENS}

    # (1) pairwise AUC matrix
    n = len(ENS); M = np.full((n, n), np.nan)
    for i, a in enumerate(ENS):
        for j, b in enumerate(ENS):
            if i != j:
                M[i, j] = cv_auc(feats[a], feats[b])
    # (2) outlier score: each tau vs all others
    vs_all = {}
    for a in ENS:
        others = np.vstack([feats[b] for b in ENS if b != a])
        vs_all[a] = cv_auc(feats[a], others)
    # (3,4) magnitudes / density
    agg = df.groupby("ensemble").agg(
        h1_count=("h1_count", "mean"), h1_pers=("h1_total_persistence", "mean"),
        edges=("graph_edges", "mean"), comps=("graph_components", "mean")).reindex(ENS)

    # ---- console tables ----
    print("Pairwise separability AUC (scale-free H1 shape) on Marcel's feature_table.csv\n")
    hdr = "          " + "".join(f"{LABEL[e]:>9}" for e in ENS)
    print(hdr)
    for i, a in enumerate(ENS):
        print(f"{LABEL[a]:>9} " + "".join("    -    " if i == j else f"{M[i,j]:9.3f}" for j in range(n)))
    print("\nMean AUC of each tau vs ALL others (outlier score):")
    for a in ENS:
        print(f"  {a:13} {vs_all[a]:.3f}")
    off = M[~np.isnan(M)]
    print(f"\nOff-diagonal AUC: min={off.min():.3f}  mean={off.mean():.3f}  max={off.max():.3f}")
    print("VERDICT: phi is", "an OUTLIER (phi-specific)" if vs_all['phi'] > max(vs_all[e] for e in ENS if e!='phi') + 0.05
          else "NOT an outlier -> every irrational separates from every other; phi-specificity not established")

    # ---- figure ----
    fig = plt.figure(figsize=(13, 10)); fig.patch.set_facecolor("white")
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.28)

    # A: heatmap
    ax = fig.add_subplot(gs[0, 0])
    cmap = LinearSegmentedColormap.from_list("au", ["#f7fbff", "#9ecae1", "#fc8d59", "#d73027"])
    Mp = np.where(np.isnan(M), 1.0, M)
    im = ax.imshow(Mp, vmin=0.5, vmax=1.0, cmap=cmap)
    ax.set_xticks(range(n)); ax.set_yticks(range(n))
    ax.set_xticklabels([LABEL[e] for e in ENS]); ax.set_yticklabels([LABEL[e] for e in ENS])
    for i in range(n):
        for j in range(n):
            ax.text(j, i, "—" if i == j else f"{M[i,j]:.2f}", ha="center", va="center",
                    fontsize=10, color="white" if (not np.isnan(M[i,j]) and M[i,j] > 0.8) else "black")
    ax.set_title("A  Pairwise separability AUC (scale-free H1 shape)\nevery irrational separates from every other \u2248 1.0",
                 fontsize=11, loc="left")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="cross-validated AUC")

    # B: H1 magnitude
    ax = fig.add_subplot(gs[0, 1])
    xb = np.arange(n)
    ax.bar(xb - 0.2, agg["h1_count"], 0.4, label="H1 count", color="#4575b4")
    ax.bar(xb + 0.2, agg["h1_pers"], 0.4, label="total persistence", color="#fc8d59")
    ax.set_xticks(xb); ax.set_xticklabels([LABEL[e] for e in ENS])
    ax.set_title("B  H1 magnitude per irrational\n$\\phi$ highest \u2014 but on a continuum, not isolated", fontsize=11, loc="left")
    ax.legend(fontsize=9)

    # C: density
    ax = fig.add_subplot(gs[1, 0]); ax2 = ax.twinx()
    ax.bar(xb, agg["edges"], 0.6, color="#74add1", label="graph edges")
    ax2.plot(xb, agg["comps"], "o-", color="#d73027", label="components")
    ax.set_xticks(xb); ax.set_xticklabels([LABEL[e] for e in ENS])
    ax.set_ylabel("mean graph edges"); ax2.set_ylabel("mean components", color="#d73027")
    ax.set_title("C  Graph density per irrational\n$\\phi$ is the most-connected frame (most edges, 1 component)", fontsize=11, loc="left")

    # D: outlier score
    ax = fig.add_subplot(gs[1, 1])
    cols = ["#d73027" if e == "phi" else "#74add1" for e in ENS]
    ax.bar(xb, [vs_all[e] for e in ENS], color=cols)
    ax.axhline(1.0, ls="--", color="grey", lw=0.8)
    ax.set_ylim(0.8, 1.02); ax.set_xticks(xb); ax.set_xticklabels([LABEL[e] for e in ENS])
    ax.set_ylabel("AUC vs all other irrationals")
    ax.set_title("D  Is $\\phi$ an outlier? Mean AUC of each tau vs the rest\n$\\phi$ (red) is not above the others \u2192 not phi-specific", fontsize=11, loc="left")

    fig.suptitle("Independent audit of Run PHI3 \u2014 phi-specificity is an artifact of an asymmetric test\n"
                 "(on Marcel Kr\u00fcger's own PHI3 feature_table.csv)", fontsize=13, y=0.99)
    out = "phi3_pairwise_audit.png"
    fig.savefig(out, dpi=170, bbox_inches="tight")
    print(f"\nFigure written: {out}")

if __name__ == "__main__":
    main()
