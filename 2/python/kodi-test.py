"""
Koide-Formel Test mit exakter Bruch-Arithmetik
Prüft ob Q = 2/3 exakt aus T0-FFGFT Verhältnissen folgt
"""
from fractions import Fraction
import math
from decimal import Decimal, getcontext
getcontext().prec = 50  # 50 Dezimalstellen

print("=" * 65)
print("KOIDE-FORMEL: EXAKTER TEST MIT VERHÄLTNISSEN")
print("=" * 65)

# Exakte Parameter als Brüche
xi = Fraction(4, 30000)  # = 1/7500 exakt
r_e   = Fraction(4, 3)
r_mu  = Fraction(16, 5)
r_tau = Fraction(25, 9)
p_e   = Fraction(3, 2)
p_mu  = Fraction(1, 1)
p_tau = Fraction(2, 3)

print(f"\nParameter:")
print(f"  ξ = {xi} = {float(xi):.8e}")
print(f"  r_e = {r_e}, p_e = {p_e}")
print(f"  r_mu = {r_mu}, p_mu = {p_mu}")
print(f"  r_tau = {r_tau}, p_tau = {p_tau}")

# Massen als Vielfache von v (v kürzt sich in Q heraus!)
# m_i = r_i * xi^p_i * v  →  m_i/v = r_i * xi^p_i
# Q hängt nicht von v ab!

xi_f = float(xi)
me_v  = float(r_e)   * xi_f**float(p_e)    # m_e / v
mmu_v = float(r_mu)  * xi_f**float(p_mu)   # m_mu / v
mta_v = float(r_tau) * xi_f**float(p_tau)  # m_tau / v

print(f"\nMassen/v (dimensionslos):")
print(f"  m_e/v   = {me_v:.10e}")
print(f"  m_mu/v  = {mmu_v:.10e}")
print(f"  m_tau/v = {mta_v:.10e}")

print(f"\nVerhältnisse (v kürzt sich heraus):")
print(f"  m_mu/m_e   = {mmu_v/me_v:.6f}")
print(f"  m_tau/m_mu = {mta_v/mmu_v:.6f}")
print(f"  m_tau/m_e  = {mta_v/me_v:.6f}")

# Koide mit normalem float
Q_float = (me_v + mmu_v + mta_v) / \
          (math.sqrt(me_v) + math.sqrt(mmu_v) + math.sqrt(mta_v))**2
print(f"\nKoide Q (float, 64-bit):")
print(f"  Q = {Q_float:.10f}")
print(f"  2/3 = {2/3:.10f}")
print(f"  Δ = {abs(Q_float - 2/3)/(2/3)*100:.6f}%")

# Koide mit Decimal (hohe Präzision)
xi_d  = Decimal(4) / Decimal(30000)
me_d  = Decimal(4)/Decimal(3)   * xi_d**Decimal('1.5')
mmu_d = Decimal(16)/Decimal(5)  * xi_d**Decimal('1')
mta_d = Decimal(25)/Decimal(9)  * xi_d**(Decimal(2)/Decimal(3))

Q_dec = (me_d + mmu_d + mta_d) / \
        (me_d.sqrt() + mmu_d.sqrt() + mta_d.sqrt())**2
print(f"\nKoide Q (Decimal, 50 Stellen):")
print(f"  Q = {Q_dec}")
print(f"  2/3 = {Decimal(2)/Decimal(3)}")
print(f"  Δ = {abs(Q_dec - Decimal(2)/Decimal(3))/(Decimal(2)/Decimal(3))*100:.8f}%")

# Analytische Vereinfachung: v kürzt sich raus
# Q = (r_e·ξ^(3/2) + r_mu·ξ + r_tau·ξ^(2/3)) /
#     (sqrt(r_e)·ξ^(3/4) + sqrt(r_mu)·ξ^(1/2) + sqrt(r_tau)·ξ^(1/3))^2
# Teile Zähler und Nenner durch ξ^(2/3):
# Zähler: r_e·ξ^(5/6) + r_mu·ξ^(1/3) + r_tau
# Nenner: (sqrt(r_e)·ξ^(1/12) + sqrt(r_mu)·ξ^(-1/6) + sqrt(r_tau)·ξ^(-1/3))^2·ξ^(2/3)
# Hmm, kompliziert. Versuche symbolisch ob 2/3 exakt möglich ist.

print(f"\n=== Symbolische Analyse ===")
print(f"Q hängt von ξ ab — es ist KEIN reines Verhältnis!")
print(f"Zähler ~ r_e·ξ^(3/2) + r_mu·ξ + r_tau·ξ^(2/3)")
print(f"Diese drei Terme haben VERSCHIEDENE ξ-Potenzen.")
print(f"Q = 2/3 exakt würde eine spezielle Beziehung zwischen")
print(f"den drei ξ-Potenzen 3/2, 1, 2/3 erfordern.")
print(f"\nDie Abweichung ist daher KEIN Rundungsfehler,")
print(f"sondern zeigt dass Q=2/3 nicht exakt aus den")
print(f"T0-FFGFT-Idealwerten folgt — es ist eine Näherung.")

print(f"\n=== Vergleich mit PDG-Messwerten ===")
me_p  = 0.51099895e6
mmu_p = 105.6583755e6
mta_p = 1776.86e6
Q_pdg = (me_p + mmu_p + mta_p) / \
        (math.sqrt(me_p) + math.sqrt(mmu_p) + math.sqrt(mta_p))**2
print(f"Q (PDG) = {Q_pdg:.10f}")
print(f"Δ = {abs(Q_pdg - 2/3)/(2/3)*100:.6f}%")
print(f"\nDie PDG-Messwerte treffen Q=2/3 VIEL genauer als die")
print(f"T0-Idealwerte — das ist physikalisch bedeutsam.")
print("=" * 65)