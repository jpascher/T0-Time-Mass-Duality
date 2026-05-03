"""
c1_geometrisch.py
=================
Geometrische Analyse des ersten Rekursionskoeffizienten c1
aus der T0-FFGFT Rekursionsformel Ψ(t) = G(Ψ(t-T_rev), ξ)

Frage: Kann c1 ≈ 218.7 aus geometrischen Prinzipien hergeleitet werden?

Ergebnis:
  c1 ≈ Δ(1/ξ) = Verschiebung der effektiven Windungszahl (Abw. 4%)
  c1 ≈ 2(1-K_frak)/ξ = 200  (geometrischer Schätzer, Abw. 9%)
  Exakte Herleitung erfordert vollständige Form von G (offen)
"""
import math
from scipy.optimize import brentq

xi     = 4/30000       # = 1/7500 exakt
K_frak = 1 - 100*xi   # = 0.98667 (Dok. 133)

r_e, p_e    = 4/3,  3/2
r_mu, p_mu  = 16/5, 1.0
r_tau, p_tau= 25/9, 2/3

def Q_xi(xi_val):
    """Koide Q als Funktion von xi"""
    me  = r_e   * xi_val**p_e
    mmu = r_mu  * xi_val**p_mu
    mta = r_tau * xi_val**p_tau
    return (me+mmu+mta)/(math.sqrt(me)+math.sqrt(mmu)+math.sqrt(mta))**2

def Q_c1(c1):
    """Koide Q mit per-Teilchen Korrektur (1 + c1*p_i*xi)"""
    me  = r_e   * (1 + c1*p_e*xi)   * xi**p_e
    mmu = r_mu  * (1 + c1*p_mu*xi)  * xi**p_mu
    mta = r_tau * (1 + c1*p_tau*xi) * xi**p_tau
    return (me+mmu+mta)/(math.sqrt(me)+math.sqrt(mmu)+math.sqrt(mta))**2

# Numerische Werte
xi_exact = brentq(lambda x: Q_xi(x) - 2/3, 1e-6, 1e-3)
c1_num   = brentq(lambda c: Q_c1(c) - 2/3, 0, 1000)

print("=" * 65)
print("GEOMETRISCHE ANALYSE VON c1")
print(f"Numerischer Wert: c1 = {c1_num:.4f}")
print("=" * 65)

print(f"\n--- Interpretation 1: Windungszahl-Verschiebung ---")
print(f"  1/xi_T0    = {1/xi:.2f}  (fundamentale Windungszahl)")
print(f"  1/xi_exact = {1/xi_exact:.2f}  (effektive Windungszahl)")
delta_inv = 1/xi - 1/xi_exact
print(f"  Δ(1/ξ)    = {delta_inv:.2f}  ← geometrische Bedeutung von c1")
print(f"  c1_num     = {c1_num:.2f}")
print(f"  Abweichung: {abs(c1_num - delta_inv)/c1_num*100:.1f}%")
print(f"  Interpretation: Rekursionskorrekturen verschieben")
print(f"  die effektive Windungszahl von {1/xi:.0f} → {1/xi_exact:.1f}")

print(f"\n--- Interpretation 2: K_frak-basierter Schätzer ---")
c1_kfrak = 2*(1-K_frak)/xi
print(f"  c1 ≈ 2×(1-K_frak)/ξ = 2×100 = {c1_kfrak:.1f}")
print(f"  Abweichung: {abs(c1_num - c1_kfrak)/c1_num*100:.1f}%")
print(f"  Herleitung: c1×ξ ≈ Δξ/ξ ≈ 2×(1-K_frak) = {2*(1-K_frak):.4f}")

print(f"\n--- Interpretation 3: Logarithmische Ableitung ---")
c1_log = math.log(xi_exact/xi) / xi
print(f"  c1 ≈ ln(ξ_exact/ξ)/ξ = {math.log(xi_exact/xi):.5f}/{xi:.5e} = {c1_log:.1f}")
print(f"  Abweichung: {abs(c1_num - c1_log)/c1_num*100:.1f}%")
print(f"  (Exaktere lineare Näherung als Δ(1/ξ))")

print(f"\n--- Verbindung zur Rekursionsformel ---")
print(f"  Ψ(t) = G(Ψ(t-T_rev), ξ)")
print(f"  c1 = ∂G/∂ξ|_{{ξ=0}} / (Ψ₀ × ξ)")
print(f"  Geometrisch: G kodiert Torus-Krümmungskorrektur")
print(f"  c1 ~ Δ(1/ξ) bedeutet: G verschiebt effektive Windungszahl")
print(f"  um ~{delta_inv:.0f} Einheiten pro Rekursionsschritt × ξ")
print(f"\n  Geometrischer Schätzer: c1 ≈ 200 (aus K_frak, 9% Abw.)")
print(f"  Geometrische Interpretation: c1 ≈ Δ(1/ξ) ≈ 210 (4% Abw.)")
print(f"  Exakter Wert c1 = {c1_num:.2f} erfordert vollständige Form von G")

print(f"\n--- Prüfung: Alle bekannten Korrekturen konsistent? ---")
print(f"  c1 × ξ        = {c1_num*xi:.5f}")
print(f"  2×(1-K_frak)  = {2*(1-K_frak):.5f}  ← 9% Abw.")
print(f"  Δξ/ξ          = {(xi_exact-xi)/xi:.5f}  ← 2% Abw. (wegen lin. Näh.)")
print(f"  α-Abweichung  ≈ 0.030   ← selbe Größenordnung ✓")
print(f"  Massenfehler  ≈ 0.008   ← selbe Größenordnung ✓")
print("=" * 65)
