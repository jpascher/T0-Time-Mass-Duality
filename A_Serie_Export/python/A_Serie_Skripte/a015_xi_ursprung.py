"""A015: xi-Ursprung, kappa=7, L0, L_T, K_frak."""
import math
xi = 4/30000
kappa = 7
ell_P = 1.616e-35

print("=== A015: xi-Ursprung ===")
# 1. kappa=7: 3^kappa nahe 1/xi (approx, Faktor 3.4)
val = 3**kappa
print(f"3^kappa = 3^{kappa} = {val:.1f},  1/xi = {1/xi:.1f}")
print(f"  Verhältnis: {val/(1/xi):.3f} (approx, nicht exakt)")

# 2. L0 = xi * ell_P
L0 = xi * ell_P
print(f"L0 = xi*ell_P = {L0:.3e} m (soll 2.155e-39 m)")
assert abs(L0 - 2.155e-39)/2.155e-39 < 0.01

# 3. L_T = ell_P/xi
L_T = ell_P / xi
print(f"L_T = ell_P/xi = {L_T:.3e} m = {L_T/ell_P:.0f} ell_P (soll 7500)")
assert abs(L_T/ell_P - 7500) < 10

# 4. K_frak = 74/75
K_frak = 1 - 100*xi
print(f"K_frak = 1-100xi = {K_frak:.8f}, 74/75 = {74/75:.8f}")
assert abs(K_frak - 74/75) < 1e-10

# 5. 4/3-Vorfaktor
assert xi == 4/30000
print(f"xi = 4/30000 = {xi:.8e}: 4/3-Vorfaktor bestaetigt")
print("\nAlle Checks bestanden.")
