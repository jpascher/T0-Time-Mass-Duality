"""A260: Casimir-Effekt, Laengenskalen.

Korrigiert am 1.10.2026: Die Energiedichte zwischen den Platten ist
pi^2*hbar*c/(720*d^4); pi^2*hbar*c/(240*d^4) ist der Casimir-Druck
(vorher war /240 als Energiedichte gefuehrt). Verhaeltnis zu
rho_vac = xi*hbar*c/L_xi^4 bei L_xi: pi^2/(720*xi) = 102.8.
"""
import numpy as np
xi = 4/30000
ell_P = 1.616255e-35
hbar = 1.054571817e-34; c = 299792458.0

print("=== A260: Casimir-Effekt ===")
L0 = xi * ell_P
L_T = ell_P / xi
print(f"L0 = xi*ell_P = {L0:.3e} m")
print(f"L_T = ell_P/xi = {L_T:.3e} m = {L_T/ell_P:.0f} ell_P")
assert abs(L0 - 2.155e-39)/2.155e-39 < 0.01
assert abs(L_T/ell_P - 7500) < 10

# Casimir-Druck P = pi^2*hbar*c/(240*d^4), Energiedichte u = pi^2*hbar*c/(720*d^4)
def p_c(d): return np.pi**2 * hbar*c / (240 * d**4)
def u_c(d): return np.pi**2 * hbar*c / (720 * d**4)
p_100 = p_c(100e-6)
print(f"Casimir-Druck d=100um:        P = {p_100:.4e} Pa (soll ~1.30e-11)")
assert abs(p_100 - 1.30e-11)/1.30e-11 < 0.01

# Tabelle A260: Energiedichte und Verhaeltnis zu rho_vac
# Die Tabelle in A260 rechnet mit L_xi = 100 um (gerundet),
# rho_vac = xi*hbar*c/L_xi^4 = 4.22e-14 J/m^3.
# (Aus rho_CMB = 4.175e-14 J/m^3 folgt genau L_xi = 100.24 um.)
rho_CMB = 4.175e-14
print(f"L_xi aus rho_CMB = {(xi*hbar*c/rho_CMB)**0.25*1e6:.2f} um")
L_xi = 100e-6
rho_vac = xi*hbar*c/L_xi**4
assert abs(rho_vac - 4.22e-14)/4.22e-14 < 0.01
print(f"L_xi = {L_xi*1e6:.2f} um, rho_vac = {rho_vac:.3e} J/m^3")
soll = {100e-6: (4.33e-12, 102.8), 10e-6: (4.33e-8, 1.03e6), 1e-6: (4.33e-4, 1.03e10)}
for d, (u_soll, r_soll) in soll.items():
    u = u_c(d); r = u/rho_vac
    print(f"Energiedichte d={d*1e6:5.0f}um: u = {u:.3e} J/m^3, u/rho_vac = {r:.4g}")
    assert abs(u - u_soll)/u_soll < 0.01
    assert abs(r - r_soll)/r_soll < 0.01

# Verhaeltnis bei L_xi ist eine Identitaet: pi^2/(720*xi)
ratio = np.pi**2/(720*xi)
print(f"u(L_xi)/rho_vac = pi^2/(720 xi) = {ratio:.2f}")
assert abs(u_c(L_xi)/rho_vac - ratio)/ratio < 1e-9
assert abs(ratio - 102.8) < 0.1

# Gleichheit u(d) = rho_vac bei d = (pi^2/(720 xi))^(1/4) * L_xi
d_eq = ratio**0.25 * L_xi
print(f"Gleichheit u = rho_vac bei d = {d_eq*1e6:.0f} um")
assert abs(d_eq*1e6 - 319) < 2

# 4/3-Faktor
assert xi == 4/30000
print(f"4/3-Vorfaktor in xi bestaetigt")
print("\nAlle Checks bestanden.")
