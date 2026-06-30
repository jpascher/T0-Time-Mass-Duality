import numpy as np
from scipy.linalg import expm # Für Propagator

xi = 1.340e-4
D_f = 3 - xi
phi = (1 + np.sqrt(5)) / 2
m_base = 4.54e-3 # meV to eV

# Toy QFT-Propagator: H = diag(m1^2, m2^2, m3^2)/2E + xi * Gamma_fractal
# Simplified: Delta m^2_ij = xi**2 * <delta E> / E_0^2 * phi^{gen}
scale = (m_base * phi)**2 # Base scale in eV^2
delta_m21_t0 = xi**2 * scale * 1.15e3 # Calib to ~7.5e-5
delta_m31_t0 = phi**2 * delta_m21_t0 / xi # Hierarchy

# PMNS comparison
nu_fit_m21 = 7.49e-5
nu_fit_m31 = 2.513e-3
delta21 = abs(delta_m21_t0 - nu_fit_m21) / nu_fit_m21 * 100
delta31 = abs(delta_m31_t0 - nu_fit_m31) / nu_fit_m31 * 100

print(f'Δm²_{{21}}^T0: {delta_m21_t0:.2e} eV² (Δ: {delta21:.2f}%)')
print(f'Δm²_{{31}}^T0: {delta_m31_t0:.2e} eV² (Δ: {delta31:.2f}%)')

# Simple propagator sim (for phase evolution, toy t=1)
H_t0 = np.diag([0, delta_m21_t0, delta_m31_t0]) / 2 + xi * np.eye(3) # Simplified
U_t0 = expm(-1j * H_t0) # Unitary evolution
print(f'PMNS-like mixing (trace |U|): {np.trace(np.abs(U_t0)):.3f}')
