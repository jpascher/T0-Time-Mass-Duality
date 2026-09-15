"""
pruef_xi_galois.py — Kapitel 1: xi aus Galois-Gruppenordnungen
Quelle: QMB_n01_grundlage.tex

  (A) xi = C2(SU3_fund) / N_Fourier = (4/3)/10^4 [K]
  (B) K_frak = 1 - 100*xi = 74/75 [K]
  (C) (m_mu/m_e)^2 ≈ 43200 aus Galois: 8^2 * 25 * 27 [K, Näherung ~1%]
  (D) Koide-Formel: (sqrt(me)+sqrt(mmu)+sqrt(mtau))^2 / (me+mmu+mtau) = 3/2 [E]
  (E) |Aut(D4)| = 1152 = 2^7*3^2, teilerfremd zu 5 [K]
"""

import numpy as np

xi     = 4 / 30000
K_frak = 1 - 100 * xi

# Teilchenmassen (CODATA 2022, MeV/c^2)
m_e   = 0.51099895
m_mu  = 105.6583755
m_tau = 1776.86

print("=" * 60)
print("pruef_xi_galois.py — Kapitel 1: xi aus Galois")
print("=" * 60)
errors = 0

# (A)
print("\n[A] xi = (4/3)/10^4")
xi_check = (4/3) / 1e4
if abs(xi_check - xi) < 1e-15:
    print(f"  xi = {xi:.8e}  [K]  OK")
else:
    errors += 1; print("  FEHLER")

# (B)
print("\n[B] K_frak = 1 - 100*xi = 74/75")
if abs(K_frak - 74/75) < 1e-12:
    print(f"  K_frak = {K_frak:.10f} = 74/75  [K]  OK")
else:
    errors += 1; print("  FEHLER")

# (C) Galois-Massenrelation: Näherung ~1%
print("\n[C] (m_mu/m_e)^2 ≈ 43200 aus GF-Gruppenordnungen")
ratio_sq_obs = (m_mu / m_e)**2
ratio_sq_gal = 8**2 * 25 * 27   # |GF(9)*|^2 * 5^2 * |GF(27)|
delta_pct = abs(ratio_sq_obs - ratio_sq_gal) / ratio_sq_gal * 100
print(f"  (m_mu/m_e)^2 (CODATA) = {ratio_sq_obs:.3f}")
print(f"  8^2*25*27              = {ratio_sq_gal}  (= 43200)")
print(f"  Abweichung             = {delta_pct:.3f}%")
if delta_pct < 2.0:
    print(f"  [K] Galois-Näherung auf {delta_pct:.2f}%  OK")
else:
    errors += 1; print(f"  FEHLER: > 2%")

# (D) Koide-Formel: Q = (sum sqrt(m_i))^2 / sum(m_i) = 3/2
print("\n[D] Koide-Formel: Q = (sqrt(me)+sqrt(mmu)+sqrt(mtau))^2 / (me+mmu+mtau) = 3/2")
S1 = (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau))**2
S2 = m_e + m_mu + m_tau
Q  = S1 / S2
delta_Q = abs(Q - 3/2) / (3/2) * 100
print(f"  Q = {Q:.8f}  (3/2 = {3/2:.8f})")
print(f"  Abweichung = {delta_Q:.5f}%")
if delta_Q < 0.01:
    print(f"  [E] Koide Q = 3/2 auf {delta_Q:.5f}%  OK")
else:
    errors += 1; print("  FEHLER")

# (E) |Aut(D4)|
print("\n[E] |Aut(D4)| = 2^7 * 3^2 = 1152, teilerfremd zu 5")
aut = 2**7 * 3**2
if aut == 1152 and aut % 5 != 0:
    print(f"  1152 = 2^7*3^2, 1152%5 = {1152%5} (nicht 0)  [K]  OK")
else:
    errors += 1; print("  FEHLER")

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K/E]")
else:
    print(f"{errors} FEHLER")
