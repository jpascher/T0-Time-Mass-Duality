import numpy as np
from scipy.optimize import minimize_scalar

xi_base = 4 / 30000  # ≈1.333e-4
xi_fit = 1.340e-4
D_f_base = 3 - xi_base
D_f_fit = 3 - xi_fit

# Beispiel: CHSH-Loss-Funktion (aus 3.6)
def chsh_loss(xi, obs=2.8275, N=73):
    chsh_qm = 2 * np.sqrt(2)
    damping = np.exp(-xi * np.log(N) / (3 - xi))
    return (chsh_qm * damping - obs)**2

loss_base = chsh_loss(xi_base)
loss_fit = chsh_loss(xi_fit)
delta_improvement = (loss_base - loss_fit) / loss_base * 100

print(f'Basis-ξ: {xi_base:.6e}, Loss: {loss_base:.6f}')
print(f'Fit-ξ: {xi_fit:.6e}, Loss: {loss_fit:.6f}')
print(f'Verbesserung: {delta_improvement:.1f}%')

# Sensitivität: ∂Loss/∂ξ ≈ 2 (chsh - obs) * ∂chsh/∂ξ
sens = 2 * (2*np.sqrt(2) * np.exp(-xi_fit * np.log(N) / D_f_fit) - obs) * (-np.log(N) / D_f_fit)
print(f'Sensitivität (∂Loss/∂ξ): {sens:.2e}')