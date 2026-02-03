import math

# --- Fundamentale Daten ---
m_e = 0.51099895e-3
m_mu = 0.105658375
alpha_2pi = 0.00116141 # Schwinger-Term

# Deine t0-Parameter
t0_factor = 7500

def finale_geometrische_torsion(factor):
    mass_ratio = m_mu / m_e
    
    # Geometrische Herleitung der Kopplung:
    # Die Torsion wirkt entlang eines Fadens (1D) auf eine Oberfläche (2D).
    # Der Faktor ergibt sich aus 1 / (2 * pi * sqrt(3)) 
    # (Projektion eines Torsionsvektors auf den Spinraum)
    c_theo = 1 / (math.pi * math.sqrt(3)) # ergibt ca. 0.1838
    
    # Der Torsions-Modulator (Eta)
    # Er ist das Massenverhältnis skaliert durch den t0_factor
    eta = (mass_ratio / factor) * c_theo
    
    # g-2 Berechnung
    a_mu = alpha_2pi * (1 + eta)
    a_e = alpha_2pi * (1 + (eta / mass_ratio))
    
    return a_mu / a_e, eta

Ra_modell, eta_val = finale_geometrische_torsion(t0_factor)
target_Ra = 1.005405

print(f"--- FINALE GEOMETRISCHE TORSION ---")
print(f"Sub-Planck-Faktor t0:    {t0_factor}")
print(f"Torsions-Kopplung (C):   {1/(math.pi*math.sqrt(3)):.6f}")
print("-" * 45)
print(f"Modell Verhältnis Ra:    {Ra_modell:.6f}")
print(f"Exp. Verhältnis Ra:      {target_Ra:.6f}")
print(f"Präzision:               {100 - abs(1-Ra_modell/target_Ra)*100:.5f}%")