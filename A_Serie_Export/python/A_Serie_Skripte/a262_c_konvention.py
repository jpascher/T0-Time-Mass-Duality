"""A262 Prüfskript: E=mc²=E=m, c-Konvention, Zeitstandard-Reduktion."""
import math

c = 2.998e8  # m/s
hbar = 1.055e-34  # J·s

print("=== A262: c-Konvention und E=m ===")

# 1. E=mc² = E=m in natürlichen Einheiten
m_e_kg = 9.109e-31  # kg
m_e_J = m_e_kg * c**2
m_e_MeV = m_e_J / 1.602e-13
print(f"m_e = {m_e_kg:.4e} kg")
print(f"E = m_e*c² = {m_e_J:.4e} J = {m_e_MeV:.4f} MeV")
print(f"In nat. Einheiten (c=1): E = m = {m_e_MeV:.4f} MeV ✓")
assert abs(m_e_MeV - 0.511)/0.511 < 0.001

# 2. Länge aus Zeit: L = c*t
t = 1.0  # s
L = c * t
print(f"\nLänge aus Zeit: L = c*t = {c:.3e} m (für t=1s)")
print(f"Lichtjahr: {c * 3.156e7 / 9.461e15:.4f} ly ✓")

# 3. Compton-Periode als Zeitstandard für m_e
lambda_C = hbar / (m_e_kg * c)
T_C = lambda_C / c
print(f"\nCompton-Wellenlänge: lambda_C = {lambda_C:.4e} m")
print(f"Compton-Periode: T_C = lambda_C/c = {T_C:.4e} s")
print(f"m_e = hbar/(T_C * c²) = {hbar/(T_C * c**2):.4e} kg ≈ {m_e_kg:.4e} kg ✓")
assert abs(hbar/(T_C * c**2) - m_e_kg)/m_e_kg < 1e-6

print("\nAlle Checks bestanden.")
