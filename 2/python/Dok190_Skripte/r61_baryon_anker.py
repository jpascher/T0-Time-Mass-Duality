"""R61: Dok-005-Proton-Rechnung — Anker-Diagnose und -Reparatur (m_mu -> pi^2/2)."""
import math

xi = 4/30000
K_frak = 1 - 100*xi
D_f = 3 - xi
Lambda_QCD = 0.217
N_c, alpha_s = 3, 0.118
m_mu = 0.105658
m_p_exp = 0.938272

# Druckwerte aus Dok. 005 (Proton-Beispielrechnung)
K_corr_p, QZ, RG, D_bar_p, f_NN = 0.985, 0.532, 1.00007, 0.363, 1.00002

# (i) Diagnose: Produkt mit m_mu verfehlt das gedruckte Ergebnis
prod_wrong = m_mu*K_corr_p*QZ*RG*D_bar_p*f_NN
missing = 0.938100/prod_wrong
print(f"Produkt mit m_mu: {prod_wrong:.5f} GeV (gedruckt: 0.93810)")
print(f"Fehlfaktor: {missing:.4f}")
assert abs(missing - 46.672) < 0.01

# Anker-Identifikation: pi^2/2 / m_mu trifft Fehlfaktor auf 0.07%
anchor = math.pi**2/2
ratio = anchor/m_mu
print(f"(pi^2/2)/m_mu = {ratio:.4f}  Delta zum Fehlfaktor: {(ratio-missing)/missing*100:+.3f}%")
assert abs(ratio - missing)/missing < 0.002

# (ii) Reparatur: unveraenderte Druckwerte mit pi^2/2-Anker
m_p_rep = anchor*K_corr_p*QZ*RG*D_bar_p*f_NN
print(f"Reparierte Formel: m_p = {m_p_rep:.5f} GeV")
print(f"  vs PDG {m_p_exp}: Delta = {(m_p_rep-m_p_exp)/m_p_exp*100:+.3f}%")
print(f"  vs Dok-005-Ergebnis 0.93810: Delta = {(m_p_rep-0.93810)/0.93810*100:+.3f}%")
assert abs(m_p_rep - m_p_exp)/m_p_exp < 0.001
assert abs(m_p_rep - 0.93810)/0.93810 < 0.001

# Dimensionsbilanz: pi^2/2, K_corr, QZ, RG, f_NN dimensionslos; D_baryon in GeV
D_bar_calc = N_c*(1+alpha_s)*math.exp(-(xi/4)*N_c)*0.5*Lambda_QCD
print(f"D_baryon = {D_bar_calc:.4f} GeV (Druckwert 0.363; einziger Einheitentraeger)")
assert abs(D_bar_calc - 0.363)/0.363 < 0.005

# (iii) Strukturnotiz: (pi^2/2)*(16/pi^2) = 8 exakt
acht = anchor * 16/math.pi**2
print(f"(pi^2/2)*(16/pi^2) = {acht:.12f}")
assert abs(acht - 8) < 1e-12

# (iv) Sekundaerbefund: K_corr Druckwert vs Formel
K_corr_formula = K_frak**(D_f*(1-(xi/4)*2))
print(f"K_corr Formel = {K_corr_formula:.5f} vs Druckwert 0.985 "
      f"(Delta {(0.985-K_corr_formula)/K_corr_formula*100:+.2f}%)")
assert abs(K_corr_formula - 0.9605) < 0.001

# (v) QZ-Kandidat 8/15 (ungebucht P35)
print(f"QZ=0.532 vs 8/15={8/15:.4f} (Delta {(0.532-8/15)/(8/15)*100:+.2f}%; ungebucht P35)")

print("\nAlle Checks bestanden.")
