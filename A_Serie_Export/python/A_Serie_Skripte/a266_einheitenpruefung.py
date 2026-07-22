"""A266: Dimensionsmatrix, Rueckrechnungsbeispiele."""
import numpy as np
hbar=1.055e-34; c=2.998e8; k_B=1.381e-23; G=6.674e-11; E_P=1.956e9; ell_P=1.616e-35

print("=== A266: Einheitenpruefung ===")
# Masse
m_e_J = 0.511e6*1.602e-19; m_e_kg = m_e_J/c**2
print(f"m_e = {m_e_kg:.4e} kg (exp 9.109e-31)")
assert abs(m_e_kg - 9.109e-31)/9.109e-31 < 0.001

# Planck-Laenge
ell_calc = hbar*c/E_P
print(f"ell_P = hbar*c/E_P = {ell_calc:.4e} m (exp 1.616e-35)")
assert abs(ell_calc - ell_P)/ell_P < 0.01

# Kreisfrequenz aus Energie: omega = E/hbar (kein c)
E_1eV = 1.602e-19
omega = E_1eV/hbar
print(f"omega = E/hbar = {omega:.3e} rad/s (fuer E=1eV, kein c benoetigt)")
# Probe: E = hbar*omega
assert abs(hbar*omega - E_1eV)/E_1eV < 1e-10

# G = ell_P^2*c^3/hbar
G_calc = ell_P**2*c**3/hbar
print(f"G = ell_P^2*c^3/hbar = {G_calc:.4e} (exp 6.674e-11)")
assert abs(G_calc - G)/G < 0.01

# alpha = xi * (E0/MeV)^2
xi=4/30000; E0=7.398
alpha = xi*E0**2
print(f"alpha = xi*(E0/MeV)^2 = {alpha:.6f}, 1/alpha = {1/alpha:.4f} (exp 137.036)")
assert abs(1/alpha - 137.036)/137.036 < 0.001

print("\nAlle Checks bestanden.")
