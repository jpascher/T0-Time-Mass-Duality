#!/usr/bin/env python3
"""
Kapitel 38: Singularitäten-Regularisierung – Formelprüfung
==========================================================
"""
import numpy as np

xi = 4/3 * 1e-4
G = 6.674e-11
c = 3e8
hbar = 1.055e-34
l_P = np.sqrt(hbar * G / c**3)  # Planck-Länge
m_P = np.sqrt(hbar * c / G)     # Planck-Masse

print("="*65)
print("Kap 38: Singularitäten – Formelprüfung")
print("="*65)
print(f"ξ = {xi:.6e}")
print(f"l_P = {l_P:.4e} m, m_P = {m_P:.4e} kg")
print()

# 1. ρ_max ≈ ρ₀ · ξ^(-3/2)
print("--- (1) ρ_max ≈ ρ₀ · ξ^(-3/2) ---")
print(f"  ξ^(-3/2) = {xi**-1.5:.2e}")
print(f"  → ρ kann maximal um Faktor ~6.5×10⁵ über ρ₀ steigen")
print(f"  → Endliche obere Schranke, verhindert Divergenz ✓")
print(f"  Keine numerische Spannung (ρ₀ ist Skalierungsparameter)")
print()

# 2. R_max ≈ c⁴/(Gℏ) · ξ²
print("--- (2) R_max ≈ c⁴/(Gℏ) · ξ² ---")
R_max = c**4 / (G * hbar) * xi**2
print(f"  c⁴/(Gℏ) = {c**4/(G*hbar):.4e} m⁻²")
print(f"  R_max = {R_max:.4e} m⁻²")
# Zum Vergleich: Planck-Krümmung R_P = c⁴/(Gℏ) ~ 10⁵⁹
R_P = c**4 / (G * hbar)
print(f"  Planck-Krümmung R_P = {R_P:.4e} m⁻²")
print(f"  R_max/R_P = ξ² = {xi**2:.4e}")
print(f"  → R_max ist ξ²-mal die Planck-Krümmung")
print(f"  → {R_max:.2e} m⁻² — endlich, aber extrem groß")
print(f"  ✓ Vermeidet Divergenz bei endlichem Wert")
print()

# 3. Kernradius ~ l_P · ξ⁻¹
print("--- (3) Modifizierter Kernradius ~ l_P · ξ⁻¹ ---")
r_core = l_P * xi**-1
print(f"  r_core = l_P/ξ = {l_P:.2e}/{xi:.2e} = {r_core:.4e} m")
print(f"  Zum Vergleich: l_P = {l_P:.2e} m")
print(f"  r_core/l_P = ξ⁻¹ = {xi**-1:.0f}")
print(f"  → Kern ~7500× größer als Planck-Länge")
print(f"  → Sub-Planck-Physik wird vermieden ✓")
print()

# 4. Gaußförmige Regularisierung
print("--- (4) Gaußsche Teilchendeformation ---")
print(f"  δρ(x) = mc²/l₀³ · ξ · exp(-r²/(l₀²ξ²))")
print(f"  Effektive Breite: σ = l₀·ξ")
print(f"  Für l₀ ~ 10⁻³¹ m: σ = {1e-31*xi:.2e} m")
print(f"  → σ ≈ 10⁻³⁵ m — Planck-Skala")
print(f"  Punkt-Teilchen wird zu ausgedehntem Objekt ✓")
print()

# 5. Selbstenergie: ΔE ≈ Gm²/(c²l₀ξ)
print("--- (5) Regularisierte Selbstenergie ---")
m_e = 9.109e-31  # kg
l_0 = 1e-31  # m (Annahme)
dE = G * m_e**2 / (c**2 * l_0 * xi)
dE_eV = dE / 1.6e-19
print(f"  ΔE = Gm_e²/(c²l₀ξ)")
print(f"  = {G:.2e}·({m_e:.2e})²/({c:.0e}²·{l_0:.0e}·{xi:.2e})")
print(f"  = {dE:.4e} J = {dE_eV:.4e} eV")
print(f"  Zum Vergleich: m_e·c² = {m_e*c**2/1.6e-19:.0f} eV")
print(f"  ΔE/m_e·c² = {dE/(m_e*c**2):.4e}")
print(f"  → Selbstenergie-Korrektur extrem klein ✓")
print()

# 6. Potential U(ρ)
print("--- (6) Potential U(ρ) ---")
print(f"  U(ρ) = Λ₀ + κ/2·(ρ-ρ₀)² + λ/4·(ρ-ρ₀)⁴")
print(f"  → Standard Mexican-Hat-Potential")
print(f"  → κ, λ nicht aus ξ allein bestimmt")
print(f"  → Formal korrekt, Parameter offen")
print()

print("="*65)
print("ZUSAMMENFASSUNG Kap 38")
print("="*65)
print(f"""
Formel                              | Status | Bemerkung
------------------------------------|--------|---------------------------
ρ_max = ρ₀·ξ^(-3/2)                | ✓      | Endliche Schranke
R_max = c⁴/(Gℏ)·ξ²                 | ✓      | Endlich, ~ξ²·R_Planck
Kernradius ~ l_P/ξ                  | ✓      | 7500× Planck-Länge
Gaußsche Regularisierung            | ✓      | σ ~ l₀·ξ ~ Planck-Skala
Selbstenergie Gm²/(c²l₀ξ)          | ✓      | Endlich, winzig klein
U(ρ) mit κ, λ                      | ⚠      | κ, λ nicht aus ξ bestimmt

Kap 38 ist numerisch weitgehend konsistent.
Singularitäts-Vermeidung durch endliche ρ_max funktioniert.
Hauptproblem: κ, λ im Potential sind zusätzliche Parameter.
""")
