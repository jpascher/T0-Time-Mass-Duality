import numpy as np

xi_base = 4 / 30000  # Fraktal-Basis
xi_fit = 1.340e-4    # Fit
D_f_base = 3 - xi_base
D_f_fit = 3 - xi_fit

def fractal_correction(scale, xi, D_f):
    return np.exp(-xi * scale**2 / D_f)  # z.B. scale=n=6 für QM

def loss_with_fit(obs, xi, scale=6, N=73):  # Kombiniert
    damp_qm = fractal_correction(scale, xi, 3 - xi)
    damp_bell = np.exp(-xi * np.log(N) / (3 - xi))
    chsh = 2 * np.sqrt(2) * damp_bell  # Toy
    return (chsh - obs)**2 + (1 - damp_qm)**2  # Multi-Loss

obs_chsh = 2.8275
loss_fractal = loss_with_fit(obs_chsh, xi_base)
loss_fit = loss_with_fit(obs_chsh, xi_fit)

print(f'Loss mit Basis-ξ (Fraktal): {loss_fractal:.6f}')
print(f'Loss mit Fit-ξ: {loss_fit:.6f}')
print(f'Reduktion durch Fit: {((loss_fractal - loss_fit)/loss_fractal * 100):.1f}%')