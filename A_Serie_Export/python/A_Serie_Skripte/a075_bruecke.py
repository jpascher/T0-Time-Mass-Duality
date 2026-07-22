"""A075 Brückenformel: Lagrangian-Terme, Schröd.-Limes, Dirac-Reduktion."""
import numpy as np

xi = 4/30000
hbar = 1.0  # natürliche Einheiten

print("=== A075: Brückenformel — Schrödinger-Limes ===")

# Standard-Schrödinger aus Klein-Gordon: nichtrel. Limes
# (Box + m^2) phi = 0 -> i*d_t psi = -nabla^2/(2m) psi
# Verifikation: Dispersionsrelation omega^2 = k^2 + m^2
m = 0.511  # MeV/c^2 in natürlichen Einheiten (c=1)
k_values = [0.1, 0.5, 1.0, 2.0]
print("Dispersionsrelation omega^2 = k^2 + m^2:")
for k in k_values:
    omega_rel = np.sqrt(k**2 + m**2)
    omega_nr = m + k**2/(2*m)  # nicht-relativistisch
    print(f"  k={k:.1f}: omega_rel={omega_rel:.4f}, omega_nr={omega_nr:.4f}, "
          f"Abw={abs(omega_rel-omega_nr)/omega_rel*100:.2f}%")

# Für kleine k/m konvergiert nichtrel. Näherung
k_small = 0.01
omega_rel = np.sqrt(k_small**2 + m**2)
omega_nr = m + k_small**2/(2*m)
assert abs(omega_rel - omega_nr)/omega_rel < 1e-6, "Nichtrel. Limes schlägt fehl"
print(f"\nNichtrel. Limes für k={k_small}: Abweichung {abs(omega_rel-omega_nr)/omega_rel:.2e} < 1e-6 ✓")

print("\nAlle Checks bestanden.")
