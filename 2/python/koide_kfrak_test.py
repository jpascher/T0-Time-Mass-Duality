"""
Koide-Formel mit K_frak Korrekturen
Testet verschiedene Anwendungsweisen der fraktalen Korrektur
"""
import math
from decimal import Decimal, getcontext
getcontext().prec = 50

xi = 4/30000
K_frak = 1 - 100*xi          # = 0.98667 (uniform)
K_frak_32 = K_frak**(3/2)    # = 0.98007 (3D Projektion)

v = 246.22e9  # eV

# Ideale Massen
r_e, p_e    = 4/3,  3/2
r_mu, p_mu  = 16/5, 1.0
r_tau, p_tau= 25/9, 2/3

def koide(me, mmu, mta):
    Q = (me + mmu + mta) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mta))**2
    return Q

def show(label, me, mmu, mta):
    Q = koide(me, mmu, mta)
    d = abs(Q - 2/3)/(2/3)*100
    print(f"  {label:<45} Q={Q:.8f}  Δ={d:.5f}%")

print("=" * 75)
print("KOIDE-FORMEL: VERGLEICH MIT K_frak KORREKTUREN")
print(f"  K_frak   = 1 - 100ξ = {K_frak:.6f}")
print(f"  K_frak^(3/2) = {K_frak_32:.6f}")
print("=" * 75)

# 1. Ideal (keine Korrektur)
me0  = r_e   * xi**p_e   * v
mmu0 = r_mu  * xi**p_mu  * v
mta0 = r_tau * xi**p_tau * v
show("Ideal (keine Korrektur)", me0, mmu0, mta0)

# 2. Uniform: alle × K_frak (kürzt sich raus!)
show("Alle × K_frak (uniform)", me0*K_frak, mmu0*K_frak, mta0*K_frak)

# 3. Pro Generation: K_frak^p_i (skalenabhängig)
# Idee: je höher p (mehr unterdrückt), desto mehr Korrektur
me3  = r_e   * xi**p_e   * v * K_frak**p_e
mmu3 = r_mu  * xi**p_mu  * v * K_frak**p_mu
mta3 = r_tau * xi**p_tau * v * K_frak**p_tau
show("K_frak^p_i (skalenabhängig)", me3, mmu3, mta3)

# 4. K_frak^(3/2) uniform (3D Projektion)
show("Alle × K_frak^(3/2)", me0*K_frak_32, mmu0*K_frak_32, mta0*K_frak_32)

# 5. K_frak^(p_i * 3/2) (kombiniert)
me5  = r_e   * xi**p_e   * v * K_frak**(p_e * 3/2)
mmu5 = r_mu  * xi**p_mu  * v * K_frak**(p_mu * 3/2)
mta5 = r_tau * xi**p_tau * v * K_frak**(p_tau * 3/2)
show("K_frak^(p_i × 3/2)", me5, mmu5, mta5)

# 6. Rekursive Korrektur 1. Ordnung: r_eff = r × (1 + c1 × xi)
# c1 unbekannt — was müsste c1 sein damit Q = 2/3 exakt?
# Suche c1 numerisch
print(f"\n  Suche c1 sodass Q = 2/3 exakt:")
from scipy.optimize import brentq
def Q_minus_23(c1):
    me  = r_e   * (1 + c1*xi)**1 * xi**p_e   * v
    mmu = r_mu  * (1 + c1*xi)**1 * xi**p_mu  * v
    mta = r_tau * (1 + c1*xi)**1 * xi**p_tau * v
    return koide(me, mmu, mta) - 2/3

try:
    # Uniform c1 kürzt sich raus → kein Effekt
    print(f"  Uniformes c1: kürzt sich in Q heraus → kein Effekt")
    
    # Per-Teilchen c1 unterschiedlich
    # Versuche c1_e, c1_mu, c1_tau getrennt
    # Einfachster Ansatz: c1_i proportional zu p_i
    def Q_c1_prop(c1):
        me  = r_e   * (1 + c1*p_e*xi)  * xi**p_e   * v
        mmu = r_mu  * (1 + c1*p_mu*xi) * xi**p_mu  * v
        mta = r_tau * (1 + c1*p_tau*xi)* xi**p_tau * v
        return koide(me, mmu, mta) - 2/3
    
    c1_sol = brentq(Q_c1_prop, -1000, 1000)
    print(f"  c1 (proportional zu p_i): c1 = {c1_sol:.2f}")
    me_s  = r_e   * (1 + c1_sol*p_e*xi)   * xi**p_e   * v
    mmu_s = r_mu  * (1 + c1_sol*p_mu*xi)  * xi**p_mu  * v
    mta_s = r_tau * (1 + c1_sol*p_tau*xi) * xi**p_tau * v
    show(f"  Mit c1={c1_sol:.1f}×p_i×ξ", me_s, mmu_s, mta_s)
except:
    print("  scipy nicht verfügbar")

# PDG Referenz
print(f"\n  PDG-Messwerte (Referenz):", end="")
show("", 0.51099895e6, 105.6583755e6, 1776.86e6)

print("=" * 75)
print(f"\nFazit:")
print(f"  Uniforme Korrekturen kürzen sich in Q heraus — kein Effekt.")
print(f"  Nur skalenabhängige (per-Teilchen) Korrekturen können Q verbessern.")
print(f"  Dies entspricht genau den c_k-Koeffizienten aus der Rekursionsformel.")
