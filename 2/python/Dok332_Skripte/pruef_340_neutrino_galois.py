# -*- coding: utf-8 -*-
"""
Dok. 340 -- Prüfskript: Neutrino-Massenhierarchie aus GF(27)*
Ausfuehren: python3 pruef_340_neutrino_galois.py

Aktualisiert am 1.10.2026: m_ee ohne nu_3-Term (nu_3 Dirac), m_ee ≈ 6,0 meV, destruktiv 0,13 meV, Obergrenze 14,4 meV; KamLAND-Zen-Grenze 28-122 meV (vgl. Dok. 340, D94; Dok. 343/344/345).
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

print("\nASSERTION 10: m_ee ohne nu_3-Beitrag, unter KamLAND-Zen Grenze [K]")
# Zuordnung (Variablennamen oben): m_nu1 = m1 = m_nu, m_nu2 = m3 = sqrt(14/3) m_nu,
# m_nu3 = m2 = 11 m_nu. Korrigiert: nu_3 ist Dirac (Dok. 343, Satz D''') ->
# kein s13^2*m_nu3-Term in m_ee.
m_nu1, m_nu2, m_nu3 = m1, m3, m2
c12sq = 1-s12sq_exp; c13sq = 1-s13sq_exp
t1 = c12sq*c13sq*m_nu1
t2 = s12sq_exp*c13sq*m_nu2
m_ee     = abs(t1 + t2)          # Majorana-Phasen null
m_ee_min = abs(t1 - t2)          # destruktive Interferenz
m_ee_max = m_nu1 + m_nu2         # Obergrenze ohne nu_3
t3_alt   = s13sq_exp*m_nu3       # ausgeschlossener Term (alter Stand)
print(f"  c12^2 c13^2 m_1 = {t1*1e3:.3f} meV,  s12^2 c13^2 m_2 = {t2*1e3:.3f} meV")
assert abs(m_nu1*1e3 - 4.54) < 0.01 and abs(m_nu2*1e3 - 9.81) < 0.01, "m_1/m_2 != 4.54/9.81 meV"
assert abs(m_ee*1e3 - 6.02) < 0.02, f"m_ee = {m_ee*1e3:.3f} meV != 6.02 meV"
assert abs(m_ee_min*1e3 - 0.13) < 0.01, f"m_ee,min = {m_ee_min*1e3:.3f} meV != 0.13 meV"
assert abs(m_ee_max*1e3 - 14.4) < 0.1, f"Obergrenze {m_ee_max*1e3:.2f} meV != 14.4 meV"
assert abs(t3_alt*1e3 - 1.10) < 0.01, "ausgeschlossener nu_3-Term != 1.10 meV"
assert m_ee*1e3 < 28, f"m_ee = {m_ee*1e3:.1f} meV > 28 meV"
print(f"  m_ee (ohne nu_3)     = {m_ee*1e3:.3f} meV  (Dok. 340: ≈ 6.0 meV)  [OK]")
print(f"  m_ee,min (destruktiv) = {m_ee_min*1e3:.3f} meV  (Dok. 340: ≈ 0.13 meV)  [OK]")
print(f"  Obergrenze m_1+m_2   = {m_ee_max*1e3:.2f} meV  (Dok. 340: 14.4 meV)  [OK]")
print(f"  (ausgeschlossen: s13^2 m_3 = {t3_alt*1e3:.2f} meV, nu_3 Dirac)")
print(f"  m_ee < 28-122 meV (KamLAND-Zen, NME-abhaengig)  [OK]")

print()
print("=" * 65)
# (wird durch Assertion 11+12 am Ende ersetzt)
print("=" * 65)

print()
print("ASSERTION 11: theta_13 aus Summenregel [K]")
Rnu = (11/3)/120  # dm2_sol/dm2_atm in Galois-Einheiten
s13sq_pred = 2/3 * Rnu
s13sq_exp  = 0.0220
err13 = abs(s13sq_pred - s13sq_exp)/s13sq_exp
assert err13 < 0.10, f"theta_13 Abw {err13*100:.1f}% > 10%"
print(f"  sin²(theta_13) = 2/3 * R_nu = 2/3 * 11/360 = {s13sq_pred:.5f}")
print(f"  Gemessen:        {s13sq_exp:.4f}")
print(f"  Abweichung:      {err13*100:.1f}%  [OK]")

print()
print("ASSERTION 12: theta_12 Konsistenz (Summenregel vs. Galois) [K]")
import numpy as np
s12_sumrule = 1/(3 - 2*Rnu)
s12_galois  = np.cos(2*np.pi*2/13)**2
konsistenz  = abs(s12_sumrule - s12_galois)/s12_galois
assert konsistenz < 0.10, f"theta_12 Konsistenz {konsistenz*100:.1f}% > 10%"
print(f"  sin²(theta_12) Summenregel: {s12_sumrule:.4f}")
print(f"  sin²(theta_12) Galois:      {s12_galois:.4f}")
print(f"  Konsistenz:                 {konsistenz*100:.1f}%  [OK]")

print()
print("=" * 65)
# ersetzt durch Assertion 13

print()
print("ASSERTION 13: theta_13 aus Galois-Formel (25*xi)^(1/3) [K]")
xi = 1/7500
val25 = (25*xi)**(1/3)
s13sq_galois = val25**2
s13sq_exp = 0.0220
err = abs(s13sq_galois - s13sq_exp)/s13sq_exp
assert err < 0.02, f"theta_13 Galois Abw {err*100:.1f}% > 2%"
print(f"  sin²(theta_13) = (25*xi)^(2/3) = (1/300)^(2/3) = {s13sq_galois:.5f}")
print(f"  Gemessen: {s13sq_exp:.4f}")
print(f"  Abweichung: {err*100:.1f}%  [OK]")
print()
print("=" * 65)
print("ALLE 13 ASSERTIONS BESTANDEN")
print("=" * 65)
