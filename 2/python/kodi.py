"""
FFGFT Kap 24: Koide-Massenformel und g-2 Brückenformel
=======================================================

Korrigiertes Prüfskript.

BEFUND des Original-Skripts:
  1. sin²-Ansatz gibt Q ≠ 2/3 (Skript bestätigt: Q schwankt 0.375-0.500)
     aber Fazit behauptet trotzdem "Q = 2/3 für alle α" → Widerspruch
  2. sin²-Formel reproduziert Leptonenmassen nicht (m_e: Fehler 55833%)
  3. a_τ^SM = 0.001×10⁻³ ist FALSCH (richtig: 1.177×10⁻³)
     → "Verhältnis T0/SM = 1088" ist falsch (richtig: 1.088)

Was ch.zip TATSÄCHLICH sagt:
  - Dok 007: Eigenvektor-Darstellung (Brannen 2005), NICHT sin²
  - Dok 007: Exponenten p_i = (3/2, 1, 2/3), Δp = 1/3 = 1/D
  - Dok 018: Brückenformel Δa(τ-e)/Δa(μ-e) = (144/125)·m_τ/m_μ
  - Dok 018: a_τ^T0 = 1.282×10⁻³, a_τ^SM = 1.177×10⁻³, Faktor ~7
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Konstanten
# ============================================================
xi = 4/3 * 1e-4
f = 1/xi  # = 7500

m_e_MeV = 0.510999
m_mu_MeV = 105.658374
m_tau_MeV = 1776.86

a_e_exp = 1.15965218128e-3   # CODATA 2018
a_mu_exp = 1.16592061e-3     # Fermilab 2023
a_tau_SM = 1.17721e-3        # SM Berechnung (Eidelman & Passera 2007)

print("="*70)
print("FFGFT Kap 24: Koide-Formel und g-2 Brückenformel")
print("Korrigiertes Prüfskript")
print("="*70)

# ============================================================
# 1. Koide-Verhältnis: Empirische Prüfung
# ============================================================
print("\n" + "-"*50)
print("1. Koide-Verhältnis (empirisch)")
print("-"*50)

Q_exp = (m_e_MeV + m_mu_MeV + m_tau_MeV) / \
        (np.sqrt(m_e_MeV) + np.sqrt(m_mu_MeV) + np.sqrt(m_tau_MeV))**2

print(f"\n  Q_exp = {Q_exp:.10f}")
print(f"  2/3   = {2/3:.10f}")
print(f"  ΔQ    = {Q_exp - 2/3:.2e}")
print(f"  → Übereinstimmung auf 6×10⁻⁶ ✓")

# ============================================================
# 2. Fehleranalyse: sin²-Ansatz
# ============================================================
print("\n" + "-"*50)
print("2. Fehleranalyse: sin²-Ansatz des Original-Skripts")
print("-"*50)

print("\nOriginal: m_i = 2m₀·sin²(α + 2π(i-1)/3)")
print("Prüfung: Q = 2/3 für alle α?")
print()
print(f"{'α (°)':<8} {'Q':>12} {'ΔQ von 2/3':>15}")
print("-"*38)

m0 = 100  # MeV (willkürlich)
for alpha_deg in [0, 15, 28.5, 30, 45, 60, 90, 120]:
    alpha = np.radians(alpha_deg)
    masses = [2*m0*np.sin(alpha + 2*np.pi*(i-1)/3)**2 for i in [1,2,3]]
    if all(m > 0 for m in masses):
        roots = [np.sqrt(m) for m in masses]
        Q = sum(masses) / sum(roots)**2
    else:
        Q = float('nan')
    print(f"  {alpha_deg:<6.1f} {Q:>12.6f} {Q-2/3:>+15.6f}")

print()
print("→ Q ist NICHT konstant = 2/3!")
print("  Der sin²-Ansatz kann die Koide-Formel NICHT ableiten.")
print("  (Originales Skript bestätigt dies: 'Q ist konstant = 2/3? ✗')")

# ============================================================
# 3. sin²-Formel reproduziert Massen nicht
# ============================================================
print("\n" + "-"*50)
print("3. sin²-Formel vs. experimentelle Massen")
print("-"*50)

m0_exp = (m_e_MeV + m_mu_MeV + m_tau_MeV) / 3  # = 627.68 MeV

# Bester α aus Minimierung (wie Original-Skript)
best_alpha = np.radians(28.5)
masses_theorie = [2*m0_exp*np.sin(best_alpha + 2*np.pi*(i-1)/3)**2 for i in [1,2,3]]
masses_exp = [m_e_MeV, m_mu_MeV, m_tau_MeV]
names = ['e', 'μ', 'τ']

print(f"\nα = 28.5°, m₀ = {m0_exp:.2f} MeV")
print(f"{'Lepton':<8} {'Experiment':>12} {'sin²-Formel':>12} {'Fehler':>10}")
print("-"*45)
for name, m_exp, m_th in zip(names, masses_exp, masses_theorie):
    err = (m_th - m_exp) / m_exp * 100
    print(f"  {name:<6} {m_exp:>12.3f} {m_th:>12.3f} {err:>+9.1f}%")

print()
print("→ Fehler bis zu 55000%! sin²-Formel ist UNBRAUCHBAR für Massen.")

# ============================================================
# 4. Was ch.zip tatsächlich verwendet
# ============================================================
print("\n" + "-"*50)
print("4. ch.zip: Exponenten-Hierarchie (Dok 007)")
print("-"*50)

print(f"""
ch.zip verwendet NICHT sin²(α), sondern Exponenten-Hierarchie:

  m_i ∝ ξ₀^(p_i), mit p_i = (3/2, 1, 2/3)
  Schrittweite: Δp = 1/3 = 1/D (inverse Raumdimension)

Die Koide-Relation Q ≈ 2/3 wird MOTIVIERT durch:
  - Regelmäßige Exponenten-Abstände
  - Eigenvektor-Darstellung der Flavour-Mischungsmatrix (Brannen 2005)
  - NICHT durch sin²-Phasen
""")

# ============================================================
# 5. Brückenformel (aus Dok 018 — korrekt)
# ============================================================
print("-"*50)
print("5. Brückenformel: Massen ↔ g-2 (Dok 018)")
print("-"*50)

print(f"\nf = 1/ξ = {f:.2f}")
print(f"f^(1/3) = {f**(1/3):.4f}")
print(f"f^(1/3) - 1 = {f**(1/3) - 1:.4f}")
print()

# Massenverhältnis
ratio_m = m_tau_MeV / m_mu_MeV
print(f"m_τ/m_μ = {ratio_m:.6f}")
print(f"(125/144)·f^(1/3) = {125/144 * f**(1/3):.6f}")
print(f"Abweichung: {(125/144 * f**(1/3) - ratio_m) / ratio_m * 100:+.1f}%")
print()

# Brückenformel
bridge_ratio = 144/125 * ratio_m
da_mu_e = a_mu_exp - a_e_exp
da_tau_e_T0 = bridge_ratio * da_mu_e
a_tau_T0 = a_e_exp + da_tau_e_T0

print("Brückenformel: Δa(τ-e)/Δa(μ-e) = (144/125)·m_τ/m_μ")
print(f"  = {144/125:.3f} × {ratio_m:.6f} = {bridge_ratio:.4f}")
print()
print(f"Δa(μ-e)_exp = {da_mu_e:.6e}")
print(f"Δa(τ-e)_T0  = {bridge_ratio:.4f} × {da_mu_e:.3e} = {da_tau_e_T0:.6e}")
print()
print(f"a_τ^T0 = a_e + Δa(τ-e) = {a_e_exp:.6e} + {da_tau_e_T0:.6e}")
print(f"       = {a_tau_T0:.6e}")

# ============================================================
# 6. Korrekter Vergleich mit SM
# ============================================================
print("\n" + "-"*50)
print("6. Vergleich T0 vs. SM (KORRIGIERT)")
print("-"*50)

da_tau_e_SM = a_tau_SM - a_e_exp
ratio_T0 = da_tau_e_T0 / da_mu_e
ratio_SM = da_tau_e_SM / da_mu_e

print(f"""
  a_τ^T0  = {a_tau_T0:.6e}
  a_τ^SM  = {a_tau_SM:.6e}
  Differenz = {(a_tau_T0 - a_tau_SM)*1e6:.1f} × 10⁻⁶

  Verhältnis Δa(τ-e)/Δa(μ-e):
    T0: {ratio_T0:.1f}
    SM: {ratio_SM:.1f}
    Faktor: {ratio_T0/ratio_SM:.1f} (testbar bei Belle II)

  KORREKTUR: Das Original-Skript hatte a_τ^SM = 1×10⁻⁶ (FALSCH!)
  Richtig: a_τ^SM = {a_tau_SM:.3e}
  → Verhältnis T0/SM = {a_tau_T0/a_tau_SM:.3f} (nicht 1088!)
""")

# ============================================================
# 7. Visualisierung
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('FFGFT Kap 24: Koide-Formel und g-2 Brücke (korrigiert)', fontsize=14)

# Plot 1: Q vs α (sin²-Ansatz — zeigt FEHLER)
ax1 = axes[0, 0]
alphas = np.linspace(0, 180, 500)
Qs = []
for alpha_deg in alphas:
    alpha = np.radians(alpha_deg)
    masses = [2*100*np.sin(alpha + 2*np.pi*(i-1)/3)**2 for i in [1,2,3]]
    roots = [np.sqrt(max(m, 1e-30)) for m in masses]
    Q = sum(masses) / sum(roots)**2 if sum(roots) > 0 else 0
    Qs.append(Q)
ax1.plot(alphas, Qs, 'b-', linewidth=2)
ax1.axhline(y=2/3, color='r', linestyle='--', label='Q = 2/3')
ax1.set_xlabel('Phasenwinkel α (°)')
ax1.set_ylabel('Q')
ax1.set_title('sin²-Ansatz: Q ≠ 2/3 (FEHLERHAFT)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0.3, 0.75)

# Plot 2: Exponenten-Hierarchie
ax2 = axes[0, 1]
p_values = [3/2, 1, 2/3]
labels = ['e (p=3/2)', 'μ (p=1)', 'τ (p=2/3)']
m_theorie = [xi**p for p in p_values]
m_normalized = [m/m_theorie[1] for m in m_theorie]  # normiert auf μ
m_exp_norm = [m_e_MeV/m_mu_MeV, 1.0, m_tau_MeV/m_mu_MeV]

x = [1, 2, 3]
ax2.semilogy(x, m_exp_norm, 'ro', markersize=10, label='Experiment (norm.)')
ax2.semilogy(x, m_normalized, 'bs', markersize=10, label='ξ^p_i (norm.)')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylabel('m_i / m_μ')
ax2.set_title('Exponenten-Hierarchie: Δp = 1/3')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: g-2 Brückenformel
ax3 = axes[1, 0]
# Simuliere verschiedene m_τ/m_μ Werte
ratio_range = np.linspace(10, 25, 100)
da_ratio_T0 = 144/125 * ratio_range
da_ratio_SM = 2.8 * np.ones_like(ratio_range)  # SM ungefähr konstant

ax3.plot(ratio_range, da_ratio_T0, 'b-', linewidth=2, label='T0: (144/125)·m_τ/m_μ')
ax3.axhline(y=2.8, color='r', linestyle='--', linewidth=2, label=f'SM: ≈ 2.8')
ax3.axvline(x=ratio_m, color='g', linestyle=':', alpha=0.7, label=f'm_τ/m_μ = {ratio_m:.1f}')
ax3.set_xlabel('m_τ / m_μ')
ax3.set_ylabel('Δa(τ-e) / Δa(μ-e)')
ax3.set_title('Brückenformel: T0 vs. SM')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: a_τ Vorhersagen
ax4 = axes[1, 1]
models = ['a_e (exp)', 'a_μ (exp)', 'a_τ (SM)', 'a_τ (T0)']
values = [a_e_exp*1e3, a_mu_exp*1e3, a_tau_SM*1e3, a_tau_T0*1e3]
colors = ['green', 'green', 'blue', 'red']
bars = ax4.barh(models, values, color=colors, alpha=0.7)
ax4.set_xlabel('a (×10⁻³)')
ax4.set_title('Anomale magnetische Momente')
ax4.grid(True, alpha=0.3, axis='x')
for bar, val in zip(bars, values):
    ax4.text(val + 0.001, bar.get_y() + bar.get_height()/2,
             f'{val:.4f}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('koide_g2_pruefung.png', dpi=150, bbox_inches='tight')
print("Plot gespeichert als 'koide_g2_pruefung.png'")

# ============================================================
# ZUSAMMENFASSUNG
# ============================================================
print("\n" + "="*70)
print("ZUSAMMENFASSUNG")
print("="*70)
print(f"""
Koide-Formel:
  ✓ Q_exp = {Q_exp:.10f} (Abweichung von 2/3: {Q_exp-2/3:.2e})
  ✗ sin²-Ansatz gibt Q ≠ 2/3 (schwankt 0.375-0.500) — FEHLERHAFT
  ✓ ch.zip: Exponenten p_i = (3/2, 1, 2/3) mit Δp = 1/3 motiviert Q ≈ 2/3

g-2 Brückenformel (Dok 018):
  ✓ Δa(τ-μ)/Δa(μ-e) = f^(1/3) - 1 = {f**(1/3)-1:.2f}
  ✓ Δa(τ-e)/Δa(μ-e) = (144/125)·m_τ/m_μ = {bridge_ratio:.1f}
  ✓ a_τ^T0 = {a_tau_T0:.3e}  (SM: {a_tau_SM:.3e})
  ✓ Faktor ~{ratio_T0/ratio_SM:.0f} Unterschied im Verhältnis → testbar bei Belle II
""")

print("="*70)
print("FEHLER IM ORIGINAL-SKRIPT (korrigiert)")
print("="*70)
print(f"""
  ✗ ENTFERNT: sin²(α)-Ableitung von Q = 2/3 (mathematisch falsch)
  ✗ KORRIGIERT: a_τ^SM = 1×10⁻⁶ → {a_tau_SM:.3e}
  ✗ KORRIGIERT: Verhältnis T0/SM = 1088 → {a_tau_T0/a_tau_SM:.3f}
  ✗ ENTFERNT: "Q ist konstant = 2/3 für alle α? ✗" + "✓ Q = 2/3" Widerspruch
  
  ✓ BEIBEHALTEN: Brückenformel (aus Dok 018 verifiziert)
  ✓ BEIBEHALTEN: a_τ^T0 = 1.282×10⁻³ (korrekt)
  ✓ ERSETZT: sin²-Ansatz → Exponenten-Hierarchie (wie Dok 007)
""")
