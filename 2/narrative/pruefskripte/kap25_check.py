"""
FFGFT Kap 25: Neutrinomassen-Problem
=====================================
Prüft: m_ν = ξ²/2 · m_e, Koide-Erweiterung, Oszillationsspannung
Referenz: Dok 007, 047
"""
import numpy as np

xi = 4/3 * 1e-4
m_e_MeV = 0.510999  # MeV
m_e_eV = m_e_MeV * 1e6  # eV

print("="*70)
print("FFGFT Kap 25: Neutrinomassen-Problem")
print("="*70)

# --- 1. Grundformel ---
print("\n" + "-"*50)
print("1. Grundformel: m_ν = ξ²/2 · m_e")
print("-"*50)

m_nu = xi**2 / 2 * m_e_eV  # eV
m_nu_meV = m_nu * 1e3

print(f"\n  ξ² = {xi**2:.4e}")
print(f"  ξ²/2 = {xi**2/2:.4e}")
print(f"  m_ν = {xi**2/2:.4e} × {m_e_eV:.0f} eV = {m_nu:.4e} eV = {m_nu_meV:.2f} meV")
print(f"  Kap 25 gibt: 4.54 meV → Δ = {abs(m_nu_meV - 4.54):.2f} meV")

# --- 2. Geschwindigkeitsabweichung ---
print("\n" + "-"*50)
print("2. Geschwindigkeitsabweichung")
print("-"*50)

delta_v = xi**2 / 2
print(f"\n  Δv/c = ξ²/2 = {delta_v:.2e}")
print(f"  Kap 25 gibt: 8.89×10⁻⁹ → Δ = {abs(delta_v - 8.89e-9):.2e}")
print(f"  v_ν/c = 1 - {delta_v:.4e} = {1-delta_v:.10f}")

# --- 3. Kosmologische Kompatibilität ---
print("\n" + "-"*50)
print("3. Kosmologische Kompatibilität")
print("-"*50)

sum_m_T0 = 3 * m_nu_meV  # Einfachster Fall: 3 gleiche Massen
print(f"\n  Σm_ν (3 gleich) = 3 × {m_nu_meV:.2f} meV = {sum_m_T0:.1f} meV")
print(f"  KATRIN Obergrenze: < 800 meV → ✓ (Faktor {800/m_nu_meV:.0f}×)")
print(f"  Planck Obergrenze: < 120 meV → ✓ (Faktor {120/sum_m_T0:.0f}×)")
print(f"  DESI+Planck:       < 70 meV  → ✓ (Faktor {70/sum_m_T0:.0f}×)")

# --- 4. Koide-Erweiterung ---
print("\n" + "-"*50)
print("4. Koide-Erweiterung: quasi-entartetes Spektrum")
print("-"*50)

delta = xi**(1/3)
print(f"\n  δ = ξ^(1/3) = {delta:.4f}")
print(f"  Kap 25 gibt: δ ≈ 0.051 → Δ = {abs(delta - 0.051):.3f}")

m1 = 4.20  # meV (aus Kap 25)
m2 = 4.54  # meV
m3 = 5.12  # meV
sum_koide = m1 + m2 + m3
print(f"\n  m₁ = {m1} meV, m₂ = {m2} meV, m₃ = {m3} meV")
print(f"  Σm_ν = {sum_koide:.2f} meV = {sum_koide/1000:.4f} eV")

# Koide-Quotient
sqrt_sum = np.sqrt(m1) + np.sqrt(m2) + np.sqrt(m3)
Q = (m1 + m2 + m3) / sqrt_sum**2
print(f"\n  Koide-Quotient Q = Σm / (Σ√m)² = {Q:.4f}")
print(f"  Quasi-entartet → Q → 1/3 = {1/3:.4f} ✓")

# --- 5. Oszillationsspannung (ZENTRAL) ---
print("\n" + "-"*50)
print("5. KRITISCH: Spannung mit Oszillationsdaten")
print("-"*50)

dm21_exp = 7.53e-5  # eV²
dm32_exp = 2.44e-3  # eV²

dm21_T0 = (m2**2 - m1**2) * 1e-6  # meV² → eV²
dm32_T0 = (m3**2 - m2**2) * 1e-6

print(f"\n  Δm²₂₁ exp = {dm21_exp:.2e} eV²")
print(f"  Δm²₂₁ T0  = {dm21_T0:.2e} eV²")
print(f"  Faktor: {dm21_exp/dm21_T0:.0f}× zu klein ✗")

print(f"\n  Δm²₃₂ exp = {dm32_exp:.2e} eV²")
print(f"  Δm²₃₂ T0  = {dm32_T0:.2e} eV²")
print(f"  Faktor: {dm32_exp/dm32_T0:.0f}× zu klein ✗")

# Minimale Massensumme aus Oszillationen
m2_min_NH = np.sqrt(dm21_exp)
m3_min_NH = np.sqrt(dm32_exp)
sum_min_NH = m2_min_NH + m3_min_NH
print(f"\n  Mindest Σm_ν (NH): ≥ {sum_min_NH*1000:.0f} meV")
print(f"  T0 Σm_ν:           {sum_koide:.0f} meV")
print(f"  Faktor: {sum_min_NH*1000/sum_koide:.1f}× zu klein")

# --- 6. Geometrische Oszillationshypothese ---
print("\n" + "-"*50)
print("6. Geometrische Oszillationshypothese (spekulativ)")
print("-"*50)

T_x = 1 / (m_nu)  # eV⁻¹
T_x_s = T_x * 6.582e-16  # eV⁻¹ → s (ℏ = 6.582×10⁻¹⁶ eV·s)
print(f"\n  T_x = 1/m_ν = {T_x:.0f} eV⁻¹ = {T_x_s:.2e} s")
print(f"  Kap 25 gibt: 220 eV⁻¹, 1.45×10⁻¹³ s")

f_vals = {"ν_e": 1, "ν_μ": 64, "ν_τ": 91.125}
print(f"\n  Geometrische Phasenfaktoren f(n,ℓ,j):")
for name, f in f_vals.items():
    print(f"    {name}: f = {f}")

print(f"""
{'='*70}
ZUSAMMENFASSUNG Kap 25
{'='*70}
  ✓ m_ν = ξ²/2 · m_e = {m_nu_meV:.2f} meV — konsistente Formel
  ✓ Kosmologisch kompatibel (11-20% der Obergrenzen)
  ✓ Koide-Quotient Q→1/3 für quasi-entartet korrekt
  ✗ Δm²₂₁ Faktor ~25× zu klein vs. Oszillation
  ✗ Δm²₃₂ Faktor ~435× zu klein vs. Oszillation  
  ✗ Σm_ν Faktor ~4-7× zu klein vs. Mindestmasse aus Oszillation
  ⚠ Geometrische Oszillationshypothese spekulativ, nicht bestätigt

  Kap 25 ist TRANSPARENT über Spannungen — ehrliche Darstellung.
""")
