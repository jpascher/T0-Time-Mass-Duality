#!/usr/bin/env python3
# ============================================================================
# Dok 268 / Schritt 17.1 -- Was T4 FORWARD erzeugt (ohne Datenblick)
#
# Zeigt: T4 gibt forward ein DICHTES Spektrum bzw. (symmetrische Resonanz)
# die HARMONISCHE Reihe 1:2:3:4:5 -- NICHT die spaerliche Serie {3,18,42,78}.
# Die Folge {1,6,14,26} ist weder T4- noch T3-Forward-Maxima.
#
# Autor: Johann Pascher / Juni 2026
# ============================================================================
import numpy as np
from collections import defaultdict

xi = 1/7500
NMAX2 = 90
R = int(np.sqrt(NMAX2)) + 1

# --- Jacobi-Entartung des vollen T4 (Summe von 4 Quadraten) ---
def jacobi_g(m):
    return 8*sum(d for d in range(1, m+1) if m % d == 0 and d % 4 != 0)

def I4(m):  # thermisch gewichtetes T4-Spektrum
    if m < 1: return 0.0
    r = np.sqrt(m)
    return jacobi_g(m)*r/(np.exp(r)-1)

print("=== Forward: lokale Maxima des vollen T4-Spektrums ===")
t4 = [m for m in range(1, NMAX2+1) if I4(m) > I4(m-1) and I4(m) > I4(m+1)]
print(f"  {t4}")
print("  -> dicht; {1,6,14,26} ist KEINE saubere Teilmenge (1 kein Max, 10 fehlt)\n")

# --- 3+Zeit: T3-Raumspektrum (Summe von 3 Quadraten) ---
r3 = defaultdict(int)
for n1 in range(-R, R+1):
    for n2 in range(-R, R+1):
        for n3 in range(-R, R+1):
            m = n1*n1+n2*n2+n3*n3
            if 1 <= m <= NMAX2: r3[m] += 1
def I3(m):
    if r3[m] == 0: return 0.0
    r = np.sqrt(m); return r3[m]*r/(np.exp(r)-1)
t3 = [m for m in range(1, NMAX2+1) if I3(m) > I3(m-1) and I3(m) > I3(m+1)]
print("=== Forward 3+Zeit: lokale Maxima des T3-Raumspektrums ===")
print(f"  {t3}")
print("  -> ebenfalls dicht, und NICHT {1,6,14,26}\n")

# --- Symmetrische Raumresonanz (n,n,n): k^2 = 3 n^2 ---
print("=== Forward: symmetrische Resonanz (n,n,n), k^2 = 3 n^2 ===")
ks = [3*n*n for n in range(1, 6)]
ratios = [np.sqrt(k/ks[0]) for k in ks]
print(f"  k^2_obs = {ks}")
print(f"  Verhaeltnisse sqrt: {' : '.join(f'{x:.3f}' for x in ratios)}  (= 1:2:3:4:5, HARMONISCH)")
print("  -> harmonisches Rueckgrat, 'zu sauber'; CMB ist anharmonisch\n")

print("=== |n|^2 = 30 (Teker): erfuellt Faktor-3, ist thermisch stark ===")
for m in [30, 42, 78]:
    print(f"  I4({m}) = {I4(m):6.2f}   (30 = 3x10, 10 lokales Max: {10 in t4})")
print("  -> I(30) > I(42) > I(78), trotzdem kein CMB-Peak: Selektion ungeklaert")
