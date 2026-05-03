"""
koide_korrekt.py
================
Koide-Formel in T0-FFGFT: korrekte Behandlung der Einheiten

WICHTIG: r_i * xi^p_i sind unteilbare Einheiten.
Brüche dürfen NICHT separat gekürzt werden -- Einheitenfehler!

Korrekte Formel (v kürzt sich heraus, xi bleibt):
  Q = (r_e*xi^(3/2) + r_mu*xi + r_tau*xi^(2/3)) /
      (sqrt(r_e*xi^(3/2)) + sqrt(r_mu*xi) + sqrt(r_tau*xi^(2/3)))^2

Q ist eine Funktion von xi -- xi kürzt sich NICHT heraus,
da die drei Exponenten p_e=3/2, p_mu=1, p_tau=2/3 verschieden sind.
Das ist keine Näherung sondern die exakte Struktur der Theorie.
"""
from fractions import Fraction
import math

print("="*60)
print("KOIDE-FORMEL IN T0-FFGFT (korrekte Einheiten)")
print("="*60)

# Exakte Parameter (Brüche als unteilbare Einheiten)
xi  = Fraction(4, 30000)   # = 1/7500 exakt
r_e   = Fraction(4, 3)
r_mu  = Fraction(16, 5)
r_tau = Fraction(25, 9)    # Korrektur K2 (Dok. 186)
p_e   = Fraction(3, 2)
p_mu  = Fraction(1, 1)
p_tau = Fraction(2, 3)

print(f"\nParameter (exakte Brüche):")
print(f"  xi    = {xi} = {float(xi):.8e}")
print(f"  r_e   = {r_e},  p_e   = {p_e}")
print(f"  r_mu  = {r_mu},  p_mu  = {p_mu}")
print(f"  r_tau = {r_tau}, p_tau = {p_tau}")

# Unteilbare Einheiten: r_i * xi^p_i
xi_f = float(xi)
Ae = float(r_e)   * xi_f**float(p_e)    # r_e * xi^(3/2)
Am = float(r_mu)  * xi_f**float(p_mu)   # r_mu * xi^1
At = float(r_tau) * xi_f**float(p_tau)  # r_tau * xi^(2/3)

print(f"\nUnteilbare Einheiten r_i * xi^p_i (v herausgekürzt):")
print(f"  r_e  * xi^(3/2) = {Ae:.8e}  [= m_e/v]")
print(f"  r_mu * xi^1     = {Am:.8e}  [= m_mu/v]")
print(f"  r_tau* xi^(2/3) = {At:.8e}  [= m_tau/v]")

# Koide Q
Z = Ae + Am + At
N = (math.sqrt(Ae) + math.sqrt(Am) + math.sqrt(At))**2
Q = Z / N

print(f"\nKoide Q:")
print(f"  Zähler = {Z:.10e}")
print(f"  Nenner = {N:.10e}")
print(f"  Q      = {Q:.8f}")
print(f"  2/3    = {2/3:.8f}")
print(f"  ΔQ     = {abs(Q-2/3)/(2/3)*100:.4f}%")

print(f"\nVergleich:")
print(f"  T0-FFGFT Vorhersage: Q = {Q:.6f}")
print(f"  PDG Messwerte:       Q = 0.666661  (Koide 1981, empirisch)")
print(f"  Sollwert:            Q = 2/3 = {2/3:.6f}")

print(f"\n{'='*60}")
print(f"INTERPRETATION:")
print(f"  Q = {Q:.6f} ist die EXAKTE T0-FFGFT-Vorhersage.")
print(f"  Sie ist keine Näherung -- sie folgt aus xi = {xi}")
print(f"  und den unteilbaren Einheiten r_i * xi^p_i.")
print(f"")
print(f"  Die 0.16% Abweichung von 2/3 zeigt:")
print(f"  Entweder ist Q=2/3 kein exaktes Ergebnis der Theorie,")
print(f"  oder es gibt eine tiefere geometrische Bedingung")
print(f"  zwischen r_e, r_mu, r_tau und xi die wir noch nicht kennen.")
print(f"")
print(f"  Die Koide-Formel (1981) wurde empirisch aus Messwerten")
print(f"  gewonnen -- ihr Wert 0.000009% Abw. ist kein unabhängiger")
print(f"  Test, sondern eine Tautologie.")
print("="*60)
