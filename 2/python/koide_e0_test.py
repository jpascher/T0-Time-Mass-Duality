"""
Koide mit Massenverehältnissen und E0
Prüft ob Q exakt aus reinen Verhältnissen berechenbar ist
"""
import math
from fractions import Fraction

xi = 4/30000
v  = 246.22e9  # eV - nur für Referenz

r_e, p_e    = 4/3,  3/2
r_mu, p_mu  = 16/5, 1.0
r_tau, p_tau= 25/9, 2/3

print("="*65)
print("MASSENVERHAELTNISSE UND E0-BERECHNUNG")
print("="*65)

# Massenverhaeltnisse (v kuerzt sich heraus, xi bleibt)
R_mu  = (r_mu/r_e)  * xi**(p_mu  - p_e)   # m_mu/m_e
R_tau = (r_tau/r_e) * xi**(p_tau - p_e)   # m_tau/m_e

print(f"\nMassenverhaeltnisse (v herausgekuerzt):")
print(f"  r_mu/r_e  = {r_mu/r_e:.6f} = {Fraction(16,5)/Fraction(4,3)}")
print(f"  r_tau/r_e = {r_tau/r_e:.6f} = {Fraction(25,9)/Fraction(4,3)}")
print(f"  xi^(p_mu-p_e)  = xi^{p_mu-p_e:.4f} = {xi**(p_mu-p_e):.6f}")
print(f"  xi^(p_tau-p_e) = xi^{p_tau-p_e:.4f} = {xi**(p_tau-p_e):.6f}")
print(f"  R_mu  = m_mu/m_e  = {R_mu:.6f}  (exp: 206.768)")
print(f"  R_tau = m_tau/m_e = {R_tau:.6f}  (exp: 3477.15)")

# Koide aus reinen Verhältnissen (normiert auf m_e=1)
Q_ratio = (1 + R_mu + R_tau) / (1 + math.sqrt(R_mu) + math.sqrt(R_tau))**2
print(f"\nKoide Q aus Verhaeltnissen m_i/m_e:")
print(f"  Q = {Q_ratio:.8f}  Δ = {abs(Q_ratio-2/3)/(2/3)*100:.5f}%")
print(f"  (identisch zu vorher - xi steckt in R_mu, R_tau)")

# E0 = sqrt(m_e * m_mu) als Verhaeltnis
print(f"\nE0 = sqrt(m_e * m_mu):")
E0_ratio_squared = r_e * r_mu * xi**(p_e + p_mu)  # E0^2 / v^2
E0_ratio = math.sqrt(E0_ratio_squared)  # E0 / v
print(f"  E0/v = sqrt(r_e * r_mu * xi^(p_e+p_mu))")
print(f"       = sqrt({r_e:.4f} * {r_mu:.4f} * xi^{p_e+p_mu:.4f})")
print(f"       = {E0_ratio:.8e}")
print(f"  E0   = {E0_ratio * v / 1e6:.4f} MeV  (Sollwert: 7.398 MeV)")

# alpha aus E0 (Test ob Verhältnis stimmt)
alpha_T0 = xi * (E0_ratio * v / 1e6)**2
print(f"\nalpha = xi * (E0/MeV)^2:")
print(f"  = {xi:.6e} * ({E0_ratio * v / 1e6:.4f})^2")
print(f"  = {alpha_T0:.6f}  (Sollwert: 1/137.036 = {1/137.036:.6f})")
print(f"  Abweichung: {abs(alpha_T0 - 1/137.036)/(1/137.036)*100:.4f}%")

# Nun: Koide normiert auf E0
print(f"\nKoide normiert auf E0 = sqrt(m_e * m_mu):")
# m_i / E0 = m_i / sqrt(m_e * m_mu)
Re_E0  = 1 / math.sqrt(R_mu)           # m_e/E0 = 1/sqrt(R_mu)
Rmu_E0 = math.sqrt(R_mu)               # m_mu/E0 = sqrt(R_mu)  
Rta_E0 = R_tau / math.sqrt(R_mu)       # m_tau/E0 = R_tau/sqrt(R_mu)

print(f"  m_e/E0   = {Re_E0:.6f}")
print(f"  m_mu/E0  = {Rmu_E0:.6f}")
print(f"  m_tau/E0 = {Rta_E0:.6f}")

Q_E0 = (Re_E0 + Rmu_E0 + Rta_E0) / (math.sqrt(Re_E0) + math.sqrt(Rmu_E0) + math.sqrt(Rta_E0))**2
print(f"  Q = {Q_E0:.8f}  Δ = {abs(Q_E0-2/3)/(2/3)*100:.5f}%")

# Schlussfolgerung
print(f"\n{'='*65}")
print(f"FAZIT:")
print(f"  Q ist eine Funktion von xi^(1/2) und xi^(1/6)")
print(f"  Diese sind transzendent - keine exakte rationale Darstellung")
print(f"  E0-Normierung aendert Q nicht (Q ist Verhältnis-invariant)")
print(f"  Abweichung 0.16% steckt in xi^(1/2) und xi^(1/6)")
print(f"  Exaktes Q=2/3 erfordert Korrekturen die xi^(1/2) anpassen")

# Welcher xi-Wert wuerde Q=2/3 exakt liefern?
from scipy.optimize import brentq
def Q_of_xi(xi_val):
    R_mu_  = (r_mu/r_e)  * xi_val**(p_mu  - p_e)
    R_tau_ = (r_tau/r_e) * xi_val**(p_tau - p_e)
    return (1 + R_mu_ + R_tau_) / (1 + math.sqrt(R_mu_) + math.sqrt(R_tau_))**2

xi_exact = brentq(lambda x: Q_of_xi(x) - 2/3, 1e-6, 1e-3)
print(f"\n  xi fuer Q=2/3 exakt: {xi_exact:.8e}")
print(f"  xi T0-FFGFT:         {xi:.8e}")
print(f"  Differenz: {abs(xi_exact - xi)/xi*100:.4f}%")
print(f"  --> Rekursionskorrektur muesste xi effektiv um {(xi_exact-xi)/xi*100:+.4f}% verschieben")
print("="*65)
