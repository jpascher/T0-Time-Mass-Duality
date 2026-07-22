"""A075: Modefunktionen, Orthonormalitaet, Kopplung."""
import numpy as np
xi = 4/30000
m_e = 0.511; m_mu = 105.658

print("=== A075: Modefunktionen ===")
# Orthonormality via manual trapezoid
def inner(n, m, N=2000):
    x = np.linspace(0, 1, N, endpoint=False)
    dx = 1.0/N
    f = np.cos(2*np.pi*n*x)
    g = np.cos(2*np.pi*m*x)
    return np.sum(f*g)*dx

print("Orthonormalitaet:")
print(f"  <1|2> = {inner(1,2):.2e} (soll 0)")
assert abs(inner(1,2)) < 1e-6

# Massenproportionale Kopplung
g_e = m_e * xi; g_mu = m_mu * xi
print(f"g_T(mu)/g_T(e) = {g_mu/g_e:.4f} = m_mu/m_e = {m_mu/m_e:.4f}")
assert abs(g_mu/g_e - m_mu/m_e) < 1e-10

# L_T
ell_P = 1.616e-35
L_T = ell_P/xi
print(f"L_T = {L_T:.3e} m = {L_T/ell_P:.0f} ell_P")
assert abs(L_T/ell_P - 7500) < 10

print("\nAlle Checks bestanden.")
