import math

# --- Eingangsdaten ---
m_mu = 0.105658375    # Myon-Masse in GeV
E_planck = 1.2209e19  # Standard Planck-Energie in GeV
t0_factor = 7500      # Deine Definition: t0 ist 7500-mal kleiner
E_t0 = E_planck * t0_factor  # Energie auf der Sub-Planck-Skala

# Fermilab 2025 Anomalie (Delta a_mu = Exp - SM)
# Wir nehmen den Wert der Spannung: ca. 260.5 x 10^-11
delta_a_mu = 260.5e-11

# --- Die Formel ---
# Delta a_mu = C * (m_mu / E_t0)^2
# Wir loesen nach C auf:
C = delta_a_mu / (m_mu / E_t0)**2

print(f"--- Kopplungsanalyse: Sub-Planck-Länge (t0) ---")
print(f"Energie auf der t0-Skala: {E_t0:.2e} GeV")
print(f"Messwert der Anomalie:     {delta_a_mu:.2e}")
print(f"\nBerechneter Kopplungsfaktor C: {C:.2e}")

# Interpretation
if C > 1:
    print("\nInterpretation: Die Kopplung müsste verstärkt werden (unwahrscheinlich).")
else:
    print(f"\nInterpretation: Ein Effekt der Stärke 10^{math.log10(C):.0f}")
    print("müsste von der Sub-Planck-Ebene 'hochskalieren'.")