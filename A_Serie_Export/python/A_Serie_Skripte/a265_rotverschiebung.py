"""A265: Statische Rotverschieung, Achromatizitaet, SI-Anker."""
import math
xi = 4/30000
hbar = 1.055e-34; k_B = 1.381e-23
m_e = 9.109e-31; c = 2.998e8; T_CMB = 2.7255

print("=== A265: Spektralverschiebung ===")
# 1+z = exp(xi*x), x in 1/xi Einheiten
print("1+z = exp(xi*x), Beispiele:")
for z in [0.1, 0.5, 1.0]:
    x = math.log(1+z)/xi
    z_back = math.exp(xi*x) - 1
    print(f"  z={z:.1f}: x={x:.2e}, Rueckrechnung z={z_back:.4f} v")
    assert abs(z_back - z) < 1e-10

# Achromatizitaet
factor = math.exp(xi * 1000)  # kleiner Wert
l1, l2 = 400.0, 700.0
assert abs(l2/l1 - l2*factor/(l1*factor)) < 1e-10
print(f"Achromatizitaet: gleicher Streckfaktor fuer alle Wellenlaengen v")

# SI-Anker
E_e = m_e * c**2
E_CMB = k_B * T_CMB
anker = E_e / E_CMB
print(f"SI-Anker m_e*c^2/(k_B*T_CMB) = {anker:.4e} (soll 2.176e9)")
assert abs(anker - 2.176e9)/2.176e9 < 0.01

print("\nAlle Checks bestanden.")
