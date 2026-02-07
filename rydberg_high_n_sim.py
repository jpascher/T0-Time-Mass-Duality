import numpy as np

xi = 1.340e-4
D_f = 3 - xi
phi = (1 + np.sqrt(5)) / 2

def E_standard(n):
  return -13.6 / n**2

def E_ext(n, gen=0):
  return E_standard(n) * phi**gen * np.exp(-xi * n**2 / D_f)

ns = np.arange(7,21)
E_std = E_standard(ns)
E_ext_vals = E_ext(ns)

delta_ext = np.abs((E_ext_vals - E_std) / E_std * 100)

print('n | E_std (eV) | E_ext (eV) | Δ_ext (%)')
for i in range(len(ns)):
  print(f'{ns[i]} | {E_std[i]:.4f} | {E_ext_vals[i]:.4f} | {delta_ext[i]:.4f}')
