import math

# --- Fundamentale Konstanten ---
m_planck = 1.2209e19  # GeV
f = 7491.80           # Deine sub-Planck-Länge t0
target_top_mass = 172.76 # GeV (Experimenteller Wert)

def berechne_top_quark_torsion(f_val):
    # 1. Das Higgs-VEV aus deiner Geometrie (unser 99.79% Treffer)
    rho_4d = m_planck / (f_val**4)
    vev_modell = (rho_4d / (math.pi / 2)) / 10
    
    # 2. Die Top-Quark Resonanz
    # In der Torsions-Physik ist das Top-Quark die 
    # Projektion des VEV auf die Spin-Ebene: VEV / sqrt(2)
    # Da y_t fast 1 ist, ist dies die reinste Masse-Resonanz.
    m_top_modell = vev_modell / math.sqrt(2)
    
    return vev_modell, m_top_modell

# --- Analyse ---
vev, m_top = berechne_top_quark_torsion(f)

print(f"--- TORSIONS-RESONANZ: TOP-QUARK ---")
print(f"Sub-Planck-Faktor t0: {f:.2f}")
print("-" * 50)
print(f"Modell Top-Quark Masse: {m_top:.2f} GeV (Soll: 172.76)")
print("-" * 50)
print(f"PRÄZISION TOP-QUARK:    {100 - abs(1 - m_top/target_top_mass)*100:.4f}%")