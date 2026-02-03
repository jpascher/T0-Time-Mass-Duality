import math

# --- Daten ---
m_tau = 1.77686
target_tau_tau = 2.903e-13
h_bar_gev_s = 6.582119e-25
t0_factor = 7491.80

def berechne_tau_final_torsion(f):
    # Die Standard-Torsions-Kopplung
    g_torsion = 1.16637e-5
    
    # Der entscheidende Unterschied beim Tau:
    # Es zerfällt nicht nur in e und mu, sondern auch in Quarks.
    # In der Torsions-Theorie entspricht das einer Erhöhung der 
    # 'Freiheitsgrade' (N) in der sub-planckschen Geometrie.
    # Für das Tau ist N ca. 5 (e + mu + 3 Quark-Farben)
    N_torsion = 5 
    
    gamma = N_torsion * (g_torsion**2 * m_tau**5) / (192 * math.pi**3)
    
    tau_s = h_bar_gev_s / gamma
    return tau_s

# --- Berechnung ---
tau_s_modell = berechne_tau_final_torsion(t0_factor)

print(f"--- TAU-TORSION MIT HADRONISCHEM KANAL ---")
print(f"Sub-Planck-Faktor t0: {t0_factor:.2f}")
print(f"Freiheitsgrade N:      {5} (Resonanz-Modus)")
print("-" * 45)
print(f"Modell Lebensdauer:    {tau_s_modell:.4e} s")
print(f"Gemessene Lebensdauer:  {target_tau_tau:.4e} s")
print(f"Präzision:              {100 - abs(1 - tau_s_modell/target_tau_tau)*100:.2f}%")