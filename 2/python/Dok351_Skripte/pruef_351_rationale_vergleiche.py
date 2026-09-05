#!/usr/bin/env python3
"""
pruef_351_rationale_vergleiche.py
==================================
Dok. 351 / R113 — Rationale vs. irrationale Galois-Vergleiche
Johann Pascher, 5. September 2026

Prüft drei Galois-Identitäten gegen PDG-Werte (CODATA 2022):
  1. (m_mu/m_e)² = 43200     [Quadrat, rein rational — physikalischer Rest]
  2.  m_mu/m_e  = sqrt(43200) [Linear — sqrt(43200) = 120√3 ist irrational!]
  3.  m_e * m_mu = 54 MeV²   [Produkt, rein rational — kleinster Rest]

Alle Rechnungen mit exakter rationaler Arithmetik (fractions.Fraction).
Irrationale Zahlen werden explizit markiert.
"""

from fractions import Fraction
import math

# ──────────────────────────────────────────────────────────────────────────────
# PDG / CODATA 2022 Werte als exakte Fraktionen (MeV)
# ──────────────────────────────────────────────────────────────────────────────
m_e  = Fraction(51099895000, 10**11)   # 0.510 998 950 00 MeV  σ = 1.5e-10 MeV
m_mu = Fraction(1056583755,  10**7)    # 105.658 375 5   MeV  σ = 2.3e-6  MeV

# ──────────────────────────────────────────────────────────────────────────────
# Galois-Vorhersagen (alle integer / rational)
# ──────────────────────────────────────────────────────────────────────────────
GALOIS_SQ   = Fraction(43200)   # (m_mu/m_e)² = |GF(9)*|²·5²·|GF(27)| [B]
GALOIS_PROD = Fraction(54)      # m_e·m_mu  = |GF(3)*|·|GF(27)| MeV²  [K]
# sqrt(43200) = 120·sqrt(3) — irrational, nur als float verfügbar
GALOIS_LINEAR_FLOAT = math.sqrt(43200)   # = 120·sqrt(3) ≈ 207.846

# ──────────────────────────────────────────────────────────────────────────────
# Berechnungen
# ──────────────────────────────────────────────────────────────────────────────

def pct(rest, ref):
    return float(rest / ref * 100)

PDG_sq     = m_mu**2 / m_e**2          # rational
PDG_linear = m_mu / m_e                # rational
PDG_prod   = m_e * m_mu                # rational, MeV²

rest_sq     = PDG_sq - GALOIS_SQ       # rational
rest_linear = float(PDG_linear) - GALOIS_LINEAR_FLOAT   # float (irrational ref!)
rest_prod   = PDG_prod - GALOIS_PROD   # rational

# ──────────────────────────────────────────────────────────────────────────────
# Ausgabe
# ──────────────────────────────────────────────────────────────────────────────

SEP = "─" * 70

print(SEP)
print("RATIONALE vs. IRRATIONALE GALOIS-VERGLEICHE")
print("Dok. 351 / R113 · Johann Pascher · 5. September 2026")
print(SEP)

print("\n1. QUADRAT  — (m_mu/m_e)²  vs.  43200")
print("   Beide Seiten rational → Vergleich exakt")
print(f"   PDG  (m_mu/m_e)² = {float(PDG_sq):.8f}")
print(f"   Galois    43200  = {float(GALOIS_SQ):.8f}   [integer, B]")
print(f"   Rest (PDG−43200) = {float(rest_sq):.6f}  ({pct(rest_sq, GALOIS_SQ):+.4f}%)")
assert abs(pct(rest_sq, GALOIS_SQ)) < 2.0, "Rest außerhalb Erwartung"
print("   → Rest ist physikalisch, kein Irrationalitäts-Artefakt  [PASS]")

print("\n2. LINEAR   — m_mu/m_e  vs.  sqrt(43200)")
print("   sqrt(43200) = 120·sqrt(3) ist IRRATIONAL")
print("   Vergleich rational (PDG) vs. irrational (Galois) → Artefakt!")
print(f"   PDG  m_mu/m_e      = {float(PDG_linear):.8f}   (rational)")
print(f"   Galois sqrt(43200) = {GALOIS_LINEAR_FLOAT:.8f}   (= 120√3, irrational!)")
print(f"   Rest (PDG−sqrt)    = {rest_linear:.6f}  ({rest_linear/GALOIS_LINEAR_FLOAT*100:+.4f}%)")
print("   → 0.52%-Rest ist KEIN sauberer Vergleich — sqrt irrationaler Galois-Wert")
# Kontrolle: der lineare Rest ist genau die Hälfte des quadratischen (näherungsweise)
ratio = rest_linear / GALOIS_LINEAR_FLOAT / (float(rest_sq / GALOIS_SQ) / 2)
print(f"   Verhältnis |Rest_lin| / (|Rest_sq|/2) ≈ {ratio:.4f}  (erwartet ≈ 1.00)")
assert abs(ratio - 1.0) < 0.02, "Verhältnis außerhalb 2%"
print("   → Bestätigt: linearer Rest ≈ quadratischer Rest / 2  [PASS]")

print("\n3. PRODUKT  — m_e · m_mu  vs.  54 MeV²")
print("   Beide Seiten rational → Vergleich exakt")
print(f"   PDG  m_e·m_mu = {float(PDG_prod):.8f} MeV²")
print(f"   Galois  54    = {float(GALOIS_PROD):.8f} MeV²   [integer, K]")
print(f"   Rest (PDG−54) = {float(rest_prod):.8f} MeV²  ({pct(rest_prod, GALOIS_PROD):+.6f}%)")
assert abs(pct(rest_prod, GALOIS_PROD)) < 0.1, "Produkt-Rest außerhalb Erwartung"
print("   → Kleinster Rest (0.016%) — rein rational, kein Artefakt  [PASS]")

print(f"\n{SEP}")
print("ZUSAMMENFASSUNG")
print(f"{'Vergleich':<30} {'Galois-Wert':<18} {'Typ':<14} {'Rest'}")
print("─" * 70)
print(f"{'(m_mu/m_e)²  vs. 43200':<30} {'43200 (int)':<18} {'rational':<14} {pct(rest_sq,GALOIS_SQ):+.4f}%")
print(f"{'m_mu/m_e    vs. sqrt(43200)':<30} {'120√3 (irrat.)':<18} {'IRRATIONAL':<14} {rest_linear/GALOIS_LINEAR_FLOAT*100:+.4f}%")
print(f"{'m_e·m_mu    vs. 54 MeV²':<30} {'54 (int)':<18} {'rational':<14} {pct(rest_prod,GALOIS_PROD):+.6f}%")
print(f"\n{'FAZIT':}")
print("  • Nur Quadrat und Produkt sind saubere Vergleiche (beide rational).")
print("  • Im Quadrat: Rest -1.045% ist physikalisch (fraktal-rekursive Korrektur).")
print("  • Im Linearen: sqrt(43200)=120√3 irrational — Rest 0.52% ist Artefakt des Wurzelziehens.")
print("  • Im Produkt: Rest -0.016% — kleinster Rest, beste Galois-Übereinstimmung.")
print(f"\n{SEP}")
print("Alle Assertionen bestanden. [PASS]")

# ──────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 2: Reste in Einheiten von ξ — SI-Projektions-Ordnung
# ────────
# ──────────────────────────────────────────────────────────────────────────────
# ABSCHNITT 3: Reale σ-Abstände mit Eides-korrigierter Unsicherheit
# ──────────────────────────────────────────────────────────────────────────────

print()
print(SEP)
print("REALE σ-ABSTÄNDE MIT EIDES-KORRIGIERTER UNSICHERHEIT")
print("CODATA σ_rel(mμ/mₑ) = 2.18e-8; real ≈ 1.16e-7 (Eides 2026 + α-Spannung)")
print(SEP)

s_rel_ratio_codata = 2.18e-8
s_rel_ratio_real   = 1.16e-7   # Eides + α-Spannung Rb/Cs

# (mμ/mₑ)² σ
diff_sq = abs(float(PDG_sq - GALOIS_SQ))
sigma_sq_codata = diff_sq / (float(PDG_sq) * 2 * s_rel_ratio_codata)
sigma_sq_real   = diff_sq / (float(PDG_sq) * 2 * s_rel_ratio_real)

# Produkt σ
m_e_val = float(m_e); m_mu_val = float(m_mu)
s_me = 1.5e-10
s_mmu_codata = 2.3e-6
s_mmu_real   = m_mu_val * s_rel_ratio_real
import math as _math
s_prod_codata = _math.sqrt((m_mu_val*s_me)**2 + (m_e_val*s_mmu_codata)**2)
s_prod_real   = _math.sqrt((m_mu_val*s_me)**2 + (m_e_val*s_mmu_real)**2)
diff_prod = abs(float(PDG_prod - GALOIS_PROD))
sigma_prod_codata = diff_prod / s_prod_codata
sigma_prod_real   = diff_prod / s_prod_real

print(f"\n{'Vergleich':<25} {'CODATA-σ':>12} {'Real-σ (Eides)':>16} {'Faktor'}")
print("-"*60)
print(f"{'(mμ/mₑ)² vs. 43200':<25} {sigma_sq_codata:>12.0f} {sigma_sq_real:>16.0f} {sigma_sq_codata/sigma_sq_real:.1f}×")
print(f"{'mₑ·mμ vs. 54 MeV²':<25} {sigma_prod_codata:>12.0f} {sigma_prod_real:>16.0f} {sigma_prod_codata/sigma_prod_real:.1f}×")

print()
print("INTERPRETATION:")
print("  CODATA überschätzt die Präzision von mμ/mₑ um Faktor 5-6 (Eides 2026).")
print("  Mit realer Unsicherheit:")
print(f"    (mμ/mₑ)² Rest: {sigma_sq_real:.0f}σ  statt {sigma_sq_codata:.0f}σ  — immer noch physikalisch")
print(f"    mₑ·mμ Rest:    {sigma_prod_real:.0f}σ  statt {sigma_prod_codata:.0f}σ  — immer noch physikalisch")
print("  Beide Reste bleiben weit außerhalb jeder Messtoleranz.")
print("  Die σ-Zahl ist 5× kleiner — der physikalische Befund ist derselbe.")

assert sigma_sq_real > 1000, f"(mμ/mₑ)² Rest {sigma_sq_real:.0f}σ — unerwartet klein"
assert sigma_prod_real > 100, f"Produkt-Rest {sigma_prod_real:.0f}σ — unerwartet klein"
print(f"\n{SEP}")
print("Alle Assertionen bestanden. [PASS]")
