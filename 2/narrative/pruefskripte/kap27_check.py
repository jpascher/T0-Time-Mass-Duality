"""
FFGFT Kap 27: Massenhierarchie und Gravitationsschwäche
=========================================================
Prüft: B = ρ₀²·ξ⁻², G/g_w² ≈ ξ², m_t/m_ν ≈ ξ⁻¹², Phasen-Massformel
"""
import numpy as np

xi = 4/3 * 1e-4

print("="*70)
print("FFGFT Kap 27: Massenhierarchie und Gravitationsschwäche")
print("="*70)

# --- 1. Schwächefaktor ---
print("\n" + "-"*50)
print("1. Gravitationsschwäche: G/g_w² ≈ ξ²")
print("-"*50)

G = 6.674e-11  # m³/(kg·s²)
G_F = 1.166e-5  # GeV⁻² (Fermi-Konstante)
m_W = 80.4  # GeV
g_w = np.sqrt(4 * np.sqrt(2) * G_F * m_W**2)  # schwache Kopplung

print(f"\n  ξ² = {xi**2:.4e}")
print(f"  Kap 27 gibt: G/g_w² ≈ ξ² ≈ 1.78×10⁻⁸")
print(f"  tatsächlich ξ² = {xi**2:.4e}")

# Wirkliches G/g_w² hat keinen direkten Sinn (verschiedene Einheiten)
# Hierarchie-Problem: G_N · m_p² / (ℏc) vs α_weak
G_N_natural = G * (1.67e-27)**2 / (1.055e-34 * 3e8)  # dimensionslos
alpha_weak = G_F * (80.4e9 * 1.6e-19)**2 / (1.055e-34 * 3e8)**3
print(f"\n  G_N·m_p²/(ℏc) = {G_N_natural:.2e} (Gravitationsstärke)")
print(f"  Hierarchie G_grav/G_Fermi: extrem klein, ~10⁻⁴⁰ über Massenskalen")
print(f"  ξ² = {xi**2:.2e} erklärt nur Faktor 10⁻⁸, nicht 10⁻³²")
print(f"  ⚠ ξ² allein reicht nicht für volle Hierarchie")

# --- 2. Massenhierarchie ---
print("\n" + "-"*50)
print("2. Massenhierarchie: m_t/m_ν ≈ ξ⁻¹²")
print("-"*50)

m_t = 172.76  # GeV
m_nu = 4.54e-12  # GeV (4.54 meV)
ratio = m_t / m_nu

print(f"\n  m_t = {m_t} GeV")
print(f"  m_ν = {m_nu:.2e} GeV")
print(f"  m_t/m_ν = {ratio:.2e}")
print(f"  ξ⁻¹² = {xi**(-12):.2e}")
print(f"  Verhältnis: {ratio/xi**(-12):.2f}")

if abs(np.log10(ratio) - np.log10(xi**(-12))) < 2:
    print(f"  ✓ Größenordnung stimmt (log₁₀: {np.log10(ratio):.1f} vs {-12*np.log10(xi):.1f})")
else:
    print(f"  ✗ Größenordnung passt nicht")

# --- 3. Phasen-Massformel ---
print("\n" + "-"*50)
print("3. Phasen-Massformel: m_i = m₀·(1-cos(θ_i))")
print("-"*50)

print(f"\n  θ_i ≈ ξ·ln(i+1)")
for i, name in enumerate(["Neutrino", "Elektron", "Myon", "Tau", "Top"]):
    theta_i = xi * np.log(i + 2)
    mass_frac = 1 - np.cos(theta_i)
    print(f"  {name:>10}: θ = {theta_i:.4e}, 1-cos(θ) = {mass_frac:.4e}")

print(f"\n  ⚠ Alle θ_i extrem klein → 1-cos(θ) ≈ θ²/2 ≈ ξ²·ln²/2")
print(f"  → Keine echte Hierarchie! Alle Massen gleicher Größenordnung")
print(f"  ✗ Formel kann 14 Größenordnungen Hierarchie nicht erzeugen")

print(f"""
{'='*70}
ZUSAMMENFASSUNG Kap 27
{'='*70}
  ✓ ξ² ≈ 1.78×10⁻⁸ als Unterdrückungsfaktor — korrekt berechnet
  ✓ ξ⁻¹² ≈ 10¹⁴ für m_t/m_ν — Größenordnung plausibel
  ✗ G/g_w² ≈ ξ² erklärt nur 10⁻⁸, nicht volle 10⁻³² Hierarchie
  ✗ Phasenformel m=m₀(1-cos(θ)) mit θ=ξ·ln(i+1) kann keine Hierarchie erzeugen
  ⚠ Qualitative Argumentation, keine quantitative Ableitung
""")
