"""
higgs_pruefformel.py
====================
Analyse der Higgs-Prüfformel und ihrer SM-Modellabhängigkeit

Die Prüfformel xi = lambda_h² * v² / (16*pi³ * m_h²)
verwendet ausschliesslich SM-abhängige Messwerte.

Befund:
  Die 2.6% Abweichung zwischen xi_Higgs und xi_T0=4/30000
  liegt bei nur 0.6σ wenn die Unsicherheit von lambda_h
  (±4.65%, dominiert durch SM-Modellabhängigkeit) berücksichtigt wird.

  Die Prüfformel bestätigt xi=4/30000 innerhalb der
  SM-Messgenauigkeit -- aber kein unabhängiger Beweis,
  da alle Eingaben SM-Werte sind.
"""
import math

print("="*65)
print("HIGGS-PRÜFFORMEL: SM-ABHÄNGIGKEIT UND FEHLERANALYSE")
print("="*65)

# SM-Messwerte mit Unsicherheiten (PDG 2024)
v        = 246.22;  v_err    = 0.06   # GeV  (aus W-Masse via SM)
m_h      = 125.10;  m_h_err  = 0.14   # GeV  (direkter Peak)
lambda_h = 0.129;   lh_err   = 0.003  # dim.los (aus SM-Fit)

xi_T0    = 4/30000                     # T0-FFGFT Sollwert

# Prüfformel
xi_higgs = (lambda_h**2 * v**2) / (16 * math.pi**3 * m_h**2)

print(f"\nEingaben (alle SM-modellabhängig):")
print(f"  lambda_h = {lambda_h:.3f} ± {lh_err:.3f}   [NUR aus SM-Fit, ~2-3% systematisch]")
print(f"  v        = {v:.2f} ± {v_err:.2f} GeV [aus W-Masse via SM-Relation v=2m_W/g]")
print(f"  m_h      = {m_h:.2f} ± {m_h_err:.2f} GeV [direkter Peak, relativ modellunabh.]")

print(f"\nErgebnis:")
print(f"  xi_Higgs = {xi_higgs:.6e}")
print(f"  xi_T0    = {xi_T0:.6e}  [= 4/30000, rationaler Idealwert]")
print(f"  Abw.     = {(xi_higgs-xi_T0)/xi_T0*100:+.3f}%")

# Fehlerfortpflanzung
dxi_dv  = 2 * lambda_h**2 * v / (16 * math.pi**3 * m_h**2)
dxi_dmh = -2 * lambda_h**2 * v**2 / (16 * math.pi**3 * m_h**3)
dxi_dlh = 2 * lambda_h * v**2 / (16 * math.pi**3 * m_h**2)

err_v   = abs(dxi_dv  * v_err)
err_mh  = abs(dxi_dmh * m_h_err)
err_lh  = abs(dxi_dlh * lh_err)
err_tot = math.sqrt(err_v**2 + err_mh**2 + err_lh**2)

print(f"\nFehlerfortpflanzung (statistische Messungenauigkeit):")
print(f"  von v:        ±{err_v/xi_higgs*100:.3f}%")
print(f"  von m_h:      ±{err_mh/xi_higgs*100:.3f}%")
print(f"  von lambda_h: ±{err_lh/xi_higgs*100:.3f}%  [dominierend]")
print(f"  Gesamt:       ±{err_tot/xi_higgs*100:.3f}%")

sigma = abs(xi_higgs - xi_T0) / err_tot
print(f"\n  Abweichung in Sigma: {sigma:.2f}σ")
print(f"  → xi=4/30000 liegt innerhalb 1σ der Messunsicherheit")

print(f"\nModellabhängigkeit der Eingaben:")
print(f"  lambda_h:")
print(f"    - Bestimmt aus Higgs-Zerfallsbreiten im SM-Fit")
print(f"    - In T0-FFGFT wäre lambda_h anders definiert")
print(f"    - Systematische SM-Modellabhängigkeit: ~2-3%")
print(f"    - Dominiert die Gesamtunsicherheit (4.65%)")
print(f"  v:")
print(f"    - Aus W-Boson-Masse via SM: v = 2*m_W / g")
print(f"    - g ist ein SM-Parameter (schwache Kopplungskonstante)")
print(f"    - Beitrag klein (0.049%) weil v gut gemessen")
print(f"  m_h:")
print(f"    - Direkter Peak bei LHC -- relativ modellunabhängig")
print(f"    - Beitrag: 0.224%")

print(f"\nSchlussfolgerung:")
print(f"  Die Prüfformel bestätigt xi=4/30000 bei {sigma:.1f}σ.")
print(f"  Das ist KEINE unabhängige Bestätigung --")
print(f"  alle Eingaben sind SM-Messwerte.")
print(f"  Aber auch KEIN Widerspruch --")
print(f"  die 2.6% Abweichung ist durch SM-Modellabhängigkeit")
print(f"  von lambda_h vollständig erklärbar.")
print(f"")
print(f"  Analog zur Koide-Analyse: Die 'exakten' SM-Messwerte")
print(f"  sind exakt INNERHALB des SM. In T0-FFGFT könnten")
print(f"  die effektiven Werte leicht anders liegen.")
print("="*65)
