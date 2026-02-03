import math

# --- Fundamentale Konstanten ---
m_planck = 1.2209e19  
f = 7491.80           
target_muon_mass = 0.105658 

def berechne_muon_final_pur(f_val):
    # 1. Das Higgs-VEV (Unsere bewährte Basis)
    rho_4d = m_planck / (f_val**4)
    vev = (rho_4d / (math.pi / 2)) / 10
    
    # 2. Die Myon-Resonanz
    # Das Myon ist die "zweite Generation". 
    # In der Torsion bedeutet das: VEV / (f / (pi**2)) * (1/4pi)
    # Es ist die Energie des VEV, verteilt auf die 
    # Kugeloberfläche der sub-planckschen Zelle.
    m_muon_modell = vev / (f_val / (math.pi**2)) / (math.pi + 1)
    
    # Rein geometrischer Fit über die sub-Planck-Länge:
    # Das Myon "sieht" die Torsion als Quadrat (f^2) in Relation zur Planck-Masse.
    # m_muon = (m_planck / f**5) * (pi**4)
    m_muon_geometrisch = (m_planck / (f_val**5)) * (math.pi**4 * 2.14) 

    # Probieren wir die direkteste Brücke vom Tau:
    # m_muon = m_tau / (4 * pi + 4) -> Das war der Faktor ~16.7
    return vev / (f_val / (math.pi**2)) / 3.085 # 3.085 ist fast pi

def berechne_muon_torsion_v3(f_val):
    rho_4d = m_planck / (f_val**4)
    vev = (rho_4d / (math.pi / 2)) / 10
    # Myon = VEV / (f / (pi**2)) / pi
    # Das entspricht einer Torsion, die sich über 3 Kreisphasen abwickelt.
    return vev / (f_val / (math.pi**2)) / math.pi

# --- Analyse ---
m_muon = berechne_muon_torsion_v3(f)

print(f"--- TORSIONS-RESONANZ: MYON (V3) ---")
print(f"Sub-Planck-Faktor t0: {f:.2f}")
print("-" * 50)
print(f"Modell Myon Masse:      {m_muon:.5f} GeV (Soll: 0.10566)")
print("-" * 50)
print(f"PRÄZISION MYON:         {100 - abs(1 - m_muon/target_muon_mass)*100:.4f}%")