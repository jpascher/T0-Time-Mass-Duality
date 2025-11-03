import numpy as np

xi = 1.340e-4
D_f = 3 - xi
phi = (1 + np.sqrt(5)) / 2
delta_m31 = 2.520e-3  # eV² T0
theta13 = np.arcsin(np.sqrt(0.0220))  # rad
L = 1300  # km
E_nu = 3.0  # GeV

def P_mue_T0(E, delta_m, th13, xi, D_f, L=1300):
    phase = 1.27 * delta_m * L / E  # Standard sin²
    damp = np.exp(-xi * (L / (1.97e-13))**2 / D_f)  # Fraktal (λ~ħc)
    return np.sin(2 * th13)**2 * np.sin(phase)**2 * damp

P_t0 = P_mue_T0(E_nu, delta_m31, theta13, xi, D_f)
P_std = np.sin(2 * theta13)**2 * np.sin(1.27 * delta_m31 * L / E_nu)**2

print(f'P(ν_μ → ν_e)^T0 bei {E_nu} GeV: {P_t0:.3f} (vs. Std: {P_std:.3f}, Δ: {((P_t0 - P_std)/P_std * 100):.2f}%)')