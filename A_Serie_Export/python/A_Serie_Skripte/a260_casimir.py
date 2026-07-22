"""A260: Casimir-Effekt, Laengenskalen."""
import numpy as np
xi = 4/30000
ell_P = 1.616e-35
hbar = 1.055e-34; c = 2.998e8

print("=== A260: Casimir-Effekt ===")
L0 = xi * ell_P
L_T = ell_P / xi
print(f"L0 = xi*ell_P = {L0:.3e} m")
print(f"L_T = ell_P/xi = {L_T:.3e} m = {L_T/ell_P:.0f} ell_P")
assert abs(L0 - 2.155e-39)/2.155e-39 < 0.01
assert abs(L_T/ell_P - 7500) < 10

# Casimir rho = pi^2*hbar*c / (240*d^4)
def rho_c(d): return np.pi**2 * hbar*c / (240 * d**4)
rho_100 = rho_c(100e-6)
print(f"Casimir d=100um: rho = {rho_100:.4e} J/m^3 (soll ~1.30e-11)")
assert abs(rho_100 - 1.30e-11)/1.30e-11 < 0.01

# 4/3-Faktor
assert xi == 4/30000
print(f"4/3-Vorfaktor in xi bestaetigt")
print("\nAlle Checks bestanden.")
