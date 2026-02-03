import math

# --- Konstanten und t0-Parameter ---
m_mu = 0.105658375         # Myon-Masse in GeV
planck_length = 1.616e-35  # in Metern
t0_factor = 7500           # t0 ist 7500-mal kleiner als Planck
l_t0 = planck_length / t0_factor # Deine Sub-Planck-Länge

# Myon-Radius (Compton-Wellenlänge als Näherung für den Wirkungsbereich)
# h_bar / (m_mu * c)
h_bar_c = 1.973e-16        # in GeV * m
r_mu = h_bar_c / m_mu      # Myon-Compton-Radius in Metern

# --- Torsions-Volumen-Analyse ---
# Wir berechnen, wie viele t0-Einheiten ("Torsions-Zellen") 
# in das "Volumen" des Myons passen.
vol_t0 = l_t0**3
vol_mu = (4/3) * math.pi * r_mu**3

N_t0 = vol_mu / vol_t0     # Anzahl der Torsions-Zellen

# Dein berechneter Kopplungsfaktor C aus der vorherigen Rechnung
C_calc = 1.96e39

print(f"--- Torsions-Analyse auf Sub-Planck-Skala ---")
print(f"Sub-Planck-Länge l_t0:  {l_t0:.2e} m")
print(f"Myon-Radius r_mu:       {r_mu:.2e} m")
print(f"\nAnzahl der t0-Zellen im Myon (N_t0): {N_t0:.2e}")
print(f"Dein Kopplungsfaktor C:              {C_calc:.2e}")
print(f"\nVerhältnis N_t0 / C: {N_t0 / C_calc:.2f}")