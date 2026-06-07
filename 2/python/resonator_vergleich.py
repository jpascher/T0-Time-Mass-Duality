#!/usr/bin/env python3
# ============================================================================
# Dok 268 / Schritt 17.2 -- Resonator-Vergleich: Anharmonizitaet ist geometrisch
#
# Zeigt forward (ohne Fit): die flache 2D-Kreismembran (J0-Bessel) trifft die
# anharmonische CMB-Serie auf ~5%, waehrend Kugel/Rohr (harmonisch) und die
# gekruemmte 2-Sphaere/S3 daneben liegen.
#
# Autor: Johann Pascher / Juni 2026
# ============================================================================
import numpy as np
from scipy.special import jn_zeros

CMB = np.array([1.0, 2.44, 3.68, 5.09, 6.56])

def show(name, vals):
    r = np.array(vals[:5], dtype=float); r = r/r[0]
    n = min(len(r), len(CMB))
    dev = (r[:n]-CMB[:n])/CMB[:n]*100
    print(f"  {name:34s} {' : '.join(f'{x:.2f}' for x in r)}")
    print(f"  {'':34s} Abw: {' '.join(f'{d:+.0f}%' for d in dev)}")

print("ZIEL CMB:  1 : 2.44 : 3.68 : 5.09 : 6.56\n")
show("Rohr/Kugel j0 (harmonisch)", [n*np.pi for n in range(1, 6)])
show("Kreismembran 2D (J0)  <-- passt", jn_zeros(0, 5))
show("S3-Laplace sqrt(l(l+2))", [np.sqrt(l*(l+2)) for l in range(1, 6)])
show("S2 (Y_lm) sqrt(l(l+1))", [np.sqrt(l*(l+1)) for l in range(1, 6)])
show("T4 {3,18,42,78} (Retrodiktion)", [np.sqrt(m) for m in [3, 18, 42, 78]])
print("\n  -> Die flache Membran (J0) trifft forward & parameterfrei auf ~5%.")
print("     Die gekruemmte 2-Sphaere (Y_lm) gibt 1:1.73:... -> FALSCH.")
print("     Erwartung ist eine flache begrenzte Scheibe, keine Sphaere.")
