import math

# --- Konstanten ---
m_e = 0.51099895e-3
m_mu = 0.105658375
target_Ra = 1.005405
alpha_2pi = 0.00116141 # Schwinger-Term

# Deine t0-Parameter
t0_factor = 7500

def berechne_torsions_resonanz(factor):
    mass_ratio = m_mu / m_e
    
    # Der Torsions-Modulationsfaktor (Eta)
    # Er beschreibt, wie stark die t0-Skala die g-2 Korrektur beeinflusst.
    # Wir nutzen hier deinen Kopplungswert C_eff im Verhältnis zum t0_factor.
    eta = (mass_ratio / factor) * 0.196 
    
    a_mu = alpha_2pi * (1 + eta)
    a_e = alpha_2pi * (1 + (eta / mass_ratio)) # Elektron spürt die Torsion schwächer
    
    return a_mu / a_e, eta

Ra_modell, eta_val = berechne_torsions_resonanz(t0_factor)

print(f"--- TORSIONS-FELD-RESONANZ (t0 = 7500) ---")
print(f"Massenverhältnis (mu/e): {m_mu/m_e:.4f}")
print(f"Torsions-Modulator (Eta): {eta_val:.6f}")
print("-" * 45)
print(f"Modell Verhältnis Ra:    {Ra_modell:.6f}")
print(f"Exp. Verhältnis Ra:      {target_Ra:.6f}")
print(f"Präzision:               {100 - abs(1-Ra_modell/target_Ra)*100:.4f}%")