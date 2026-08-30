# -*- coding: utf-8 -*-
"""
Dok. 340 -- Prüfskript: Neutrino-Massenhierarchie aus GF(27)*
Ausfuehren: python3 pruef_340_neutrino_galois.py
"""
import numpy as np

print("=" * 65)
print("DOK. 340: NEUTRINO-MASSENHIERARCHIE AUS GF(27)*")
print("=" * 65)

xi    = 1/7500
m_e   = 510998.95      # eV
m_nu  = xi**2/2*m_e    # eV

# Experimentelle Werte (PDG 2023)
dm2_atm_exp = 2.500e-3  # eV^2
dm2_sol_exp = 7.530e-5  # eV^2
s12sq_exp   = 0.307
s23sq_exp   = 0.545
s13sq_exp   = 0.0220

print(f"\nm_nu = xi^2/2 * m_e = {m_nu*1e3:.4f} meV")
print()

# --- Orbit-Struktur ---
print("ASSERTION 1: Orbit4 = inv(2) * Orbit1 in Z_13 [B]")
orbit1 = {1,3,9}
orbit4_computed = {(7*k)%13 for k in orbit1}
orbit4_actual   = {7,8,11}
assert orbit4_computed == orbit4_actual, f"{orbit4_computed} != {orbit4_actual}"
print(f"  7 * {{1,3,9}} mod 13 = {orbit4_computed} = {{7,8,11}}  [OK]")

print("\nASSERTION 2: Orbit2 und Orbit4 sind invers in Z_13 [B]")
assert pow(2,-1,13) == 7, "2^-1 != 7"
assert pow(7,-1,13) == 2, "7^-1 != 2"
print(f"  2^(-1) mod 13 = {pow(2,-1,13)} (in Orbit4)  [OK]")
print(f"  7^(-1) mod 13 = {pow(7,-1,13)} (in Orbit2)  [OK]")

print("\nASSERTION 3: Orbit3 ist selbstinvers [B]")
orbit3 = [4,10,12]
for k in orbit3:
    inv_k = pow(k,-1,13)
    assert inv_k in orbit3, f"{k}^-1 = {inv_k} nicht in Orbit3"
print(f"  4^-1=10, 10^-1=4, 12^-1=12 -- alle in Orbit3  [OK]")

print("\nASSERTION 4: sum(Orbit3) = 26 = |GF(27)*| [B]")
assert sum(orbit3) == 26
print(f"  4+10+12 = {sum(orbit3)} = |GF(27)*|  [OK]")

print("\nASSERTION 5: dm2_atm = 120*m_nu^2 [K]")
dm2_atm_pred = 120 * m_nu**2
err_atm = abs(dm2_atm_pred - dm2_atm_exp)/dm2_atm_exp
assert err_atm < 0.02, f"Abweichung {err_atm*100:.1f}% > 2%"
print(f"  (11^2-1)*m_nu^2 = 120*m_nu^2 = {dm2_atm_pred:.4e} eV^2")
print(f"  Gemessen:          {dm2_atm_exp:.4e} eV^2")
print(f"  Abweichung:        {err_atm*100:.2f}%  [OK]")

print("\nASSERTION 6: dm2_sol = (11/3)*m_nu^2 [K]")
dm2_sol_pred = 11/3 * m_nu**2
err_sol = abs(dm2_sol_pred - dm2_sol_exp)/dm2_sol_exp
assert err_sol < 0.02, f"Abweichung {err_sol*100:.1f}% > 2%"
print(f"  (|Z_13|-2)/3 * m_nu^2 = 11/3 * m_nu^2 = {dm2_sol_pred:.4e} eV^2")
print(f"  Gemessen:               {dm2_sol_exp:.4e} eV^2")
print(f"  Abweichung:             {err_sol*100:.2f}%  [OK]")

print("\nASSERTION 7: Neutrinomassen und Kosmologie [K]")
m1 = m_nu
m3 = np.sqrt(14/3)*m_nu
m2 = 11*m_nu
sum_m = (m1+m2+m3)*1e3  # meV
assert sum_m < 120, f"sum = {sum_m:.1f} meV > 120 meV!"
print(f"  m1={m1*1e3:.4f} meV, m3={m3*1e3:.4f} meV, m2={m2*1e3:.4f} meV")
print(f"  sum = {sum_m:.2f} meV < 120 meV (Planck)  [OK]")

print("\nASSERTION 8: Mischungswinkel aus Orbit-2-Elementen [K]")
sin2_th12_pred = np.cos(2*np.pi*2/13)**2
sin2_th23_pred = np.cos(2*np.pi*5/13)**2
err12 = abs(sin2_th12_pred - s12sq_exp)/s12sq_exp
err23 = abs(sin2_th23_pred - s23sq_exp)/s23sq_exp
assert err12 < 0.10, f"theta12 Abw {err12*100:.1f}% > 10%"
assert err23 < 0.05, f"theta23 Abw {err23*100:.1f}% > 5%"
print(f"  cos^2(2*pi*2/13) = {sin2_th12_pred:.4f}  (s12sq={s12sq_exp}, Abw {err12*100:.1f}%)  [OK]")
print(f"  cos^2(2*pi*5/13) = {sin2_th23_pred:.4f}  (s23sq={s23sq_exp}, Abw {err23*100:.1f}%)  [OK]")

print("\nASSERTION 9: dm2-Ratio [K]")
ratio_pred = 3*(11**2-1)/11
ratio_exp  = dm2_atm_exp/dm2_sol_exp
err_ratio  = abs(ratio_pred-ratio_exp)/ratio_exp
assert err_ratio < 0.02
print(f"  3*(11^2-1)/11 = {ratio_pred:.4f}")
print(f"  Gemessen:       {ratio_exp:.4f}")
print(f"  Abweichung:     {err_ratio*100:.2f}%  [OK]")

print("\nASSERTION 10: m_ee unter KamLAND-Zen Grenze [K]")
c12sq = 1-s12sq_exp; c13sq = 1-s13sq_exp
m_ee = abs(c12sq*c13sq*m1 + (1-c12sq)*c13sq*m3 + s13sq_exp*m2)
assert m_ee*1e3 < 36, f"m_ee = {m_ee*1e3:.1f} meV > 36 meV"
print(f"  m_ee = {m_ee*1e3:.3f} meV < 36 meV (KamLAND-Zen)  [OK]")

print()
print("=" * 65)
print("ALLE 10 ASSERTIONS BESTANDEN")
print("=" * 65)
