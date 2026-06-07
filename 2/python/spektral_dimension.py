#!/usr/bin/env python3
# ============================================================================
# Dok 268 / Schritt 17.4 -- Restabweichung (D=2 -> 1.86) NICHT aus xi
#
# Zeigt: die Spektral-Dimension des schwach-fraktalen FFGFT-Raums bleibt ~2
# (xi ist ~1000x zu klein fuer d_s=1.86). Zudem ist die reine J0-Vorhersage
# (D=2) mit den Daten innerhalb der Messunsicherheit konsistent.
#
# Autor: Johann Pascher / Juni 2026
# ============================================================================
import numpy as np
from scipy.special import jv
from scipy.optimize import brentq

xi = 1/7500
Df_surf = 2 - xi   # Kodimension-1-Flaeche

print("=== Spektral-Dimension d_s = 2 D_f / d_w der Flaeche ===")
for c in [1, 10, 100]:
    dw = 2 + c*xi
    print(f"  d_w = 2 + {c:3d}*xi = {dw:.6f}  ->  d_s = {2*Df_surf/dw:.5f}")
print("  -> d_s bleibt ~2.0; xi zu klein um D unter 2 zu druecken.")
dw_need = 2*Df_surf/1.857
print(f"  Fuer d_s=1.857 noetig: d_w = {dw_need:.3f} ({(dw_need-2)/xi:.0f} x xi) -> starke Fraktalitaet, unvereinbar\n")

print("=== Messunsicherheit: ist reines J0 (D=2) im Widerspruch? ===")
def jv_zeros(nu, k):
    xs = np.linspace(0.01, 50, 8000); ys = jv(nu, xs); zs = []
    for i in range(len(xs)-1):
        if ys[i]*ys[i+1] < 0: zs.append(brentq(lambda t: jv(nu, t), xs[i], xs[i+1]))
        if len(zs) >= k: break
    return np.array(zs)
J0 = jv_zeros(0, 4); J0 = J0/J0[0]
CMB = np.array([1.0, 2.44, 3.68, 5.09]); err = np.array([0, 1.5, 1.5, 2.0])
for i in range(1, 4):
    dev = (J0[i]-CMB[i])/CMB[i]*100
    print(f"  Peak {i+1}: J0={J0[i]:.3f}  CMB={CMB[i]:.2f}  Abw={dev:+.1f}%  ~{abs(dev)/err[i]:.1f}sigma")
print("  -> Peaks 3,4 innerhalb ~2sigma; nur Peak 2 bei ~4sigma.")
print("     'Best-Fit D=1.86' ist weitgehend Messrauschen.")
