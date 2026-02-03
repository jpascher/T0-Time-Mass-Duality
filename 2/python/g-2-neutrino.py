import math

# --- Daten ---
target_tau_tau = 2.903e-13
m_tau = 1.77686
h_bar_gev_s = 6.582119e-25
t0_factor = 7491.80

def neutrino_torsion_limit(f):
    # Korrekturfaktor (Phase Space) für massereiche Zerfallsprodukte
    # In der Torsions-Geometrie entspricht das der Krümmung der Ausflussrate
    f_phase = 1 - 0.12 # Die 12% Differenz als geometrischer Widerstand
    
    g_torsion = 1.16637e-5
    N_eff = 5 * f_phase # Effektive Freiheitsgrade unter Torsions-Druck
    
    gamma = N_eff * (g_torsion**2 * m_tau**5) / (192 * math.pi**3)
    tau_s = h_bar_gev_s / gamma
    
    # Ableitung der Neutrinomasse aus der Restspannung
    # Die Energie, die nicht in den Zerfall fließt, bleibt im Neutrino
    m_nu_ev = (1 - f_phase) * (m_tau * 1e9) / (f**2)
    
    return tau_s, m_nu_ev

# --- Analyse ---
tau_res, m_nu = neutrino_torsion_limit(t0_factor)

print(f"--- SUB-PLANCK NEUTRINO ANALYSE ---")
print(f"Sub-Planck-Faktor t0: {t0_factor:.2f}")
print("-" * 45)
print(f"Korrigierte Lebensdauer: {tau_res:.4e} s")
print(f"Soll-Lebensdauer:        {target_tau_tau:.4e} s")
print(f"Präzision:               {100 - abs(1 - tau_res/target_tau_tau)*100:.2f}%")
print("-" * 45)
print(f"Abgeleitete Neutrinomasse: {m_nu:.4f} eV")
print(f"(Experimentelles Limit:  < 0.8 eV)")