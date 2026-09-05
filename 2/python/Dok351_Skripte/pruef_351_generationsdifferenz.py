#!/usr/bin/env python3
"""
pruef_351_generationsdifferenz.py
===================================
Dok. 351 — Zwei orthogonale Achsen: Differenz und Summe der Logarithmen
Johann Pascher, 5. September 2026

Die PDG-Massen mₑ und mμ definieren zwei unabhängige logarithmische
Projektionen auf die Galois-Identitäten:

  Differenz-Achse: ln(mμ/mₑ / √43200)  = εμ − εₑ  ≈ −39·ξ
  Summen-Achse:   ln(mₑ·mμ / 54 MeV²) = εₑ + εμ  ≈ −1.2·ξ

Linear und Quadrat sind exakt dieselbe Differenz-Achse — nur verdoppelt.
"""
from decimal import Decimal, getcontext
getcontext().prec = 40
D = Decimal
SEP = "─" * 70
xi = D(4)/D(30000)

m_e  = D("0.51099895000")
m_mu = D("105.6583755")

print(SEP)
print("ZWEI ORTHOGONALE ACHSEN: DIFFERENZ UND SUMME")
print("Dok. 351 · Johann Pascher · 5. September 2026")
print(SEP)

print("\n1. DIFFERENZ-ACHSE: ln(mμ/mₑ / √43200) = εμ − εₑ\n")
diff = (m_mu/m_e / D(43200).sqrt()).ln()
print(f"   ln((mμ/mₑ)/√43200) = {diff/xi:+.4f}·ξ")
print(f"   Linear:  (mμ/mₑ)/√43200 − 1 = {((m_mu/m_e)/D(43200).sqrt()-1)*100:+.5f}%")
print(f"   Quadrat: (mμ/mₑ)²/43200 − 1 = {((m_mu/m_e)**2/D(43200)-1)*100:+.5f}%")
print()
print("   Quadrat = 2 × Linear (logarithmisch exakt):")
print(f"   2·diff = {2*diff/xi:+.4f}·ξ = ln((mμ/mₑ)²/43200) ✓")
print()
print("   → Linear und Quadrat sind EINE Achse, EINE Zahl, EIN Befund.")
print(f"   → −38.99·ξ: empirisch, kein Galois-Integer [S]")

assert abs(2*diff - ((m_mu/m_e)**2/D(43200)).ln()) < D("1e-30")
print(f"   Exakte Identität 2·diff = ln(quadrat): [PASS]")

print(f"\n{SEP}")
print("\n2. SUMMEN-ACHSE: ln(mₑ·mμ / 54 MeV²) = εₑ + εμ\n")
summ = (m_e*m_mu/D(54)).ln()
print(f"   ln(mₑ·mμ/54) = {summ/xi:+.4f}·ξ")
print(f"   Produkt: mₑ·mμ/54 − 1 = {(m_e*m_mu/D(54)-1)*100:+.5f}%")
print()
print("   εₑ ≈ +18.9·ξ  und  εμ ≈ −20.1·ξ  →  fast gleich groß, entgegengesetzt")
print("   Deshalb: Summe ≈ −1.2·ξ  (fast vollständige Auslöschung)")
print()
print("   → Das Produkt isoliert die gemeinsame Skalenabweichung.")
print(f"   → −1.206·ξ: SI-Projektions-Ordnung [K]")

assert abs(D("0.5")) < abs(summ/xi) < D("5")
print(f"   Produktrest in Ordnung ξ: [PASS]")

print(f"\n{SEP}")
print("\n3. ORTHOGONALITÄT: DIE ZWEI ACHSEN SIND UNABHÄNGIG\n")
print("   Differenz  εμ−εₑ ≈ −39·ξ:  misst Generationenspannung  [S]")
print("   Summe      εₑ+εμ ≈ −1.2·ξ: misst SI-Projektion         [K]")
print()
print("   Aus Differenz folgt NICHT die Summe und umgekehrt.")
print("   Zwei Gleichungen, zwei unabhängige physikalische Informationen.")
print()
print("   Verhältnis |Differenz/Summe| ≈", abs(diff/summ).to_eng_string()[:5],
      "→ Faktor ~32 (nicht Verstärkung, sondern Auslöschung in Summe)")

print(f"\n{SEP}")
print("\n4. TABELLE\n")
print(f"  {'Kombination':<30} {'Achse':<12} {'Log-Rest':<14} {'Status'}")
print(f"  {'-'*70}")
print(f"  {'ln(mμ/mₑ / √43200)':<30} {'Differenz':<12} {diff/xi:+.3f}·ξ   empirisch [S]")
print(f"  {'ln((mμ/mₑ)² / 43200)':<30} {'2×Differenz':<12} {2*diff/xi:+.3f}·ξ   exakt =2× oben")
print(f"  {'ln(mₑ·mμ / 54 MeV²)':<30} {'Summe':<12} {summ/xi:+.3f}·ξ    SI-Projektion [K]")

print(f"\n{SEP}")
print("Alle Assertionen bestanden. [PASS]")
