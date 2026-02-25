#!/usr/bin/env python3
"""
Kapitel 36: Warum QFT keine Gravitationstheorie wurde – Formelprüfung
=====================================================================
"""
import numpy as np

xi = 4/3 * 1e-4

print("="*65)
print("Kap 36: QFT und Gravitation – Formelprüfung")
print("="*65)
print(f"ξ = {xi:.6e}")
print()

# 1. Standard-QFT Lagrangian vs T0
print("--- (1) Lagrangian-Vergleich ---")
print("  QFT: L = (∂ρ)² + ρ²(∂θ)² - V(ρ)")
print("  T0:  L = K₀(∂ρ)² + B(∂θ)² - U(ρ)")
print("  → Strukturell identisch wenn K₀=1, B=ρ²")
print("  → Formal korrekt ✓")
print()

# 2. K₀/B ≈ ξ⁻¹
print("--- (2) Steifigkeitsverhältnis: K₀/B ≈ ξ⁻¹ ---")
print(f"  ξ⁻¹ = {xi**-1:.0f}")
print(f"  Behauptung: 'erklärt Hierarchie Gravitation/andere Kräfte'")
print(f"  Exp. Hierarchie: α_EM/α_G ≈ 10³⁶")
print(f"  K₀/B = ξ⁻¹ ≈ 7500")
print(f"  → 7500 ≠ 10³⁶ (Faktor ~10³²)")
print(f"  Gleiche Spannung wie Kap 27!")
print(f"  ABER: Kapitel sagt 'erklärt Hierarchie', nicht '= 10³⁶'")
print(f"  → Qualitativ: K₀ ≫ B erklärt warum ρ-Moden (Gravitation)")
print(f"     steifer/schwerer als θ-Moden (Eichkräfte). ✓ qualitativ")
print()

# 3. g = -ξ · ∇ln(ρ)
print("--- (3) Gravitation: g = -ξ · ∇ln(ρ) ---")
print(f"  Für Punktmasse: ρ(r) = ρ₀(1 + GM/(c²r))")
print(f"  ∇ln(ρ) ≈ GM/(c²r²) für schwache Felder")
print(f"  g = -ξ · GM/(c²r²)")
print()

# Prüfe ob das Newton reproduziert
# g_Newton = GM/r²
# g_T0 = ξ · GM/(c²r²)
# Für g_T0 = g_Newton: ξ/c² = 1 → c² = ξ → NEIN
print(f"  g_Newton = GM/r²")
print(f"  g_T0 = ξ·GM/(c²r²)")
print(f"  Verhältnis: g_T0/g_Newton = ξ/c² = {xi/3e8**2:.2e}")
print(f"  → g_T0 ist um Faktor ~10¹³ zu klein!")
print(f"  ⚠ Die Formel kann Newton NICHT reproduzieren mit ξ-Faktor")
print(f"  → Entweder fehlt ein Faktor oder ρ ist anders skaliert")
print()

# 4. Limes ξ→0
print("--- (4) Limites ---")
print("  ξ → 0: 'Standard-QFT ohne Gravitationseffekte'")
print("  → Trivial korrekt, da alle ξ-Terme verschwinden ✓")
print("  Niederenergie: 'ART-ähnlich'")
print("  → Nicht quantitativ gezeigt")
print()

# 5. Erweiterte Lagrangian
print("--- (5) Erweiterte Lagrangian ---")
print("  L_T0 = K₀(∂ρ)² + B(∂θ)² + ξ·ρ²(∂θ)²·F + L_matter")
print("  F = fraktale Korrekturen")
print("  → Keine explizite Form für F angegeben")
print("  → Nicht numerisch prüfbar")
print()

print("="*65)
print("ZUSAMMENFASSUNG Kap 36")
print("="*65)
print(f"""
Formel                          | Status | Bemerkung
--------------------------------|--------|---------------------------
QFT-Lagrangian ↔ T0-Lagrangian | ✓      | Strukturell identisch
K₀/B ≈ ξ⁻¹ = 7500              | ⚠      | ≠ 10³⁶, aber qualitativ OK
g = -ξ·∇ln(ρ)                  | ✗      | Reproduziert Newton nicht
ξ→0 Limes                      | ✓      | Trivial korrekt
Erweiterte L mit F              | —      | Nicht spezifiziert

Kap 36 ist hauptsächlich konzeptionell/historisch.
Einzige numerisch prüfbare Formel (g = -ξ·∇ln(ρ)) hat Probleme.
Sprachliche Overclaims: "parameterfrei und vereinheitlicht"
""")
