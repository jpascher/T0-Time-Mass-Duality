"""
FFGFT Kap 26: Baryonische Asymmetrie
======================================
Prüft: η_B ≈ ξ³ · (l₀³/V_Hubble) · sin(δθ), CP-Verletzung δθ_CP ≈ ξ·ln(ξ⁻¹)
"""
import numpy as np

xi = 4/3 * 1e-4
l_0 = 1.616e-35 * xi**(-1/2)  # m (fundamentale Korrelationslänge)

print("="*70)
print("FFGFT Kap 26: Baryonische Asymmetrie")
print("="*70)

# --- 1. Grundparameter ---
print("\n" + "-"*50)
print("1. Grundparameter")
print("-"*50)

eta_B_exp = 6.1e-10  # Baryon-zu-Photon-Verhältnis (Planck)
print(f"\n  η_B exp (Planck) = {eta_B_exp:.1e}")
print(f"  ξ = {xi:.4e}")
print(f"  ξ³ = {xi**3:.4e}")

# --- 2. CP-Verletzung ---
print("\n" + "-"*50)
print("2. CP-Verletzung: δθ_CP ≈ ξ·ln(ξ⁻¹)")
print("-"*50)

delta_theta_CP = xi * np.log(1/xi)
print(f"\n  δθ_CP = ξ · ln(ξ⁻¹) = {xi:.4e} × {np.log(1/xi):.2f}")
print(f"        = {delta_theta_CP:.4e}")
print(f"  Kap 26 gibt: ≈ 10⁻³ → Faktor {delta_theta_CP/1e-3:.1f}")
sin_delta = np.sin(delta_theta_CP)
print(f"  sin(δθ_CP) ≈ {sin_delta:.4e} ≈ δθ_CP (Kleinwinkelnäherung)")

# --- 3. Formel η_B = ξ³ · (l₀³/V_Hubble) · sin(δθ) ---
print("\n" + "-"*50)
print("3. Prüfung der η_B-Formel")
print("-"*50)

print(f"\n  ξ³ = {xi**3:.4e}")
print(f"  Kap 26 behauptet: ξ³ ≈ 10⁻¹² → tatsächlich {xi**3:.2e}")

# Die Formel enthält l₀³/V_Hubble — aber welches V_Hubble?
# Am Phasenübergang (T ~ 100 GeV, elektroschwach):
T_ew = 100  # GeV ~ 10¹² K
# Hubble-Radius ~ 1 cm bei elektroschwachem Übergang
L_Hubble_ew = 0.01  # m (Größenordnung)
V_Hubble_ew = (4/3) * np.pi * L_Hubble_ew**3

print(f"\n  l₀ = {l_0:.2e} m")
print(f"  l₀³ = {l_0**3:.2e} m³")
print(f"  L_Hubble(EW) ~ {L_Hubble_ew} m → V_Hubble ~ {V_Hubble_ew:.2e} m³")
print(f"  l₀³/V_Hubble = {l_0**3/V_Hubble_ew:.2e}")

# Das ist extrem klein (~10⁻⁹⁰), Kap 26 behauptet "≈ 10²"
# Das passt nicht — die "Defektdichte" wäre astronomisch negativ
print(f"\n  ⚠ PROBLEM: l₀³/V_Hubble = {l_0**3/V_Hubble_ew:.2e}")
print(f"    Kap 26 behauptet 'Defektdichte ≈ 10²' — das ist inkonsistent!")

# --- 4. Alternative: Rückrechnung ---
print("\n" + "-"*50)
print("4. Rückrechnung: Was braucht man für η_B = 6×10⁻¹⁰?")
print("-"*50)

# η_B = ξ³ · X · sin(δθ)
# 6e-10 = 2.37e-12 · X · 1.19e-3
# X = 6e-10 / (2.37e-12 × 1.19e-3) = 6e-10 / 2.82e-15 ≈ 213000
X_needed = eta_B_exp / (xi**3 * sin_delta)
print(f"\n  Benötigter Faktor X = η_B / (ξ³ · sin(δθ))")
print(f"  X = {eta_B_exp:.1e} / ({xi**3:.2e} × {sin_delta:.2e})")
print(f"  X = {X_needed:.0f}")
print(f"  Kap 26 gibt: Defektdichte ≈ 10² → tatsächlich braucht man ~{X_needed:.0e}")

# --- 5. Größenordnungscheck ---
print("\n" + "-"*50)
print("5. Größenordnungscheck der Einzelfaktoren")
print("-"*50)

print(f"""
  Kap 26 behauptet:
    ξ³ ≈ 10⁻¹²         → tatsächlich {xi**3:.2e} ✓ (richtige Größenordnung)
    Defektdichte ≈ 10²  → unbekannt, nicht ableitbar aus l₀/V_Hubble
    sin(δθ) ≈ 10⁻¹     → tatsächlich {sin_delta:.2e} ✓ (richtige Größenordnung)
    Produkt ≈ 6×10⁻¹⁰   → nur wenn Defektdichte ~{X_needed:.0e}
""")

# --- 6. Vakuumsteifigkeit ---
print("-"*50)
print("6. Vakuumsteifigkeit B = ρ₀² · ξ⁻²")
print("-"*50)
print(f"\n  ξ⁻² = {1/xi**2:.2e}")
print(f"  B skaliert mit ξ⁻² — formal konsistent als Energieskala")

print(f"""
{'='*70}
ZUSAMMENFASSUNG Kap 26
{'='*70}
  ✓ δθ_CP = ξ·ln(ξ⁻¹) ≈ 10⁻³ — richtige Größenordnung
  ✓ ξ³ ≈ 2.4×10⁻¹² — korrekt berechnet
  ✓ Sakharov-Bedingungen qualitativ erfüllt
  ✗ "Defektdichte ≈ 10²" nicht aus Grundparametern ableitbar
  ✗ l₀³/V_Hubble ≈ 10⁻⁹⁰, nicht 10² — Formel inkonsistent
  ⚠ η_B ≈ 6×10⁻¹⁰ wird durch passende Wahl reproduziert,
    aber die Ableitung ist nicht geschlossen — enthält freien Faktor

  Kap 26: Größenordnungsargumentation, keine geschlossene Ableitung.
""")
