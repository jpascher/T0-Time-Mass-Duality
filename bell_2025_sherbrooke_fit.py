import numpy as np
from scipy.optimize import minimize_scalar

xi_base = 4 / 30000
D_f = 3 - xi_base  # Approx für Fit
N = 127  # Sherbrooke
obs_chsh = 2.8278  # 2025-Daten

def chsh_t0(xi, n):
    damping = np.exp(-xi * np.log(n) / (3 - xi))
    return 2 * np.sqrt(2) * damping

def loss(xi):
    return (chsh_t0(xi, N) - obs_chsh)**2

# Fit
res = minimize_scalar(loss, bounds=(1e-5, 1e-3), method='bounded')
xi_fit_new = res.x
print(f'Gefittetes ξ: {xi_fit_new:.6e}')
print(f'Vorhergesagtes CHSH: {chsh_t0(xi_fit_new, N):.4f}')

# Monte-Carlo (vereinfacht)
def simulate_chsh(xi, n_runs=10000):
    chsh_vals = []
    for _ in range(n_runs):
        damp = np.exp(-xi * np.log(N) / (3 - xi))
        chsh = 2 * np.sqrt(2) * damp
        noise = np.random.normal(0, xi**2 * 0.05)
        chsh_vals.append(chsh + noise)
    return np.mean(chsh_vals), np.std(chsh_vals) / np.sqrt(n_runs)

mean_chsh, std_chsh = simulate_chsh(xi_fit_new)
print(f'Simuliertes CHSH ± σ: {mean_chsh:.4f} ± {std_chsh:.5f}')