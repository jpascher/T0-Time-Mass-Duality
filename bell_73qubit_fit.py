import numpy as np
from scipy.optimize import minimize_scalar

xi_base = 4 / 30000
D_f = 3 - xi_base
chsh_qm = 2 * np.sqrt(2)
N = 73  # 73-Qubit-Skala
obs_chsh = 2.8275  # Aus 2025-Daten

def chsh_t0(xi, n):
    damping = np.exp(-xi * np.log(n) / D_f)
    return chsh_qm * damping

def loss(xi):
    return (chsh_t0(xi, N) - obs_chsh)**2

# Fit
res = minimize_scalar(loss, bounds=(1e-5, 1e-3), method='bounded')
xi_fit = res.x
print(f'Gefittetes ξ: {xi_fit:.6e}')
print(f'Vorhergesagtes CHSH: {chsh_t0(xi_fit, N):.4f}')

# Monte-Carlo-Simulation (einfach, 10^4 Runs)
def simulate_chsh(xi, n_runs=10000, shots=7500):
    settings = np.array([[0, np.pi/4], [0, 3*np.pi/4], [np.pi/2, np.pi/4], [np.pi/2, 3*np.pi/4]])
    chsh_vals = []
    for _ in range(n_runs):
        corrs = [np.cos(s[0] - s[1]) * np.exp(-xi * np.log(N) / D_f) for s in settings]  # T0-Korrs
        chsh = corrs[0] + corrs[1] + corrs[2] - corrs[3]
        # Add Noise (Binomial-Approx für Stats)
        noise = np.random.normal(0, xi**2 * 0.1, 1)[0]
        chsh_vals.append(chsh + noise)
    return np.mean(chsh_vals), np.std(chsh_vals) / np.sqrt(n_runs)

mean_chsh, std_chsh = simulate_chsh(xi_fit)
print(f'Simuliertes CHSH ± σ: {mean_chsh:.4f} ± {std_chsh:.5f}')