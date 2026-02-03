import math

# --- Fundamentale Basis ---
m_planck = 1.2209e19  
f = 7491.80           

def run_world_formula():
    # 1. Basis: Higgs-VEV
    rho_4d = m_planck / (f**4)
    vev = (rho_4d / (math.pi / 2)) / 10
    
    # 2. Teilchen-Kaskade (Deine geometrischen Resonanzen)
    results = {
        "Higgs-VEV":  (vev, 246.22),
        "Tau-Lepton": ((vev / (f / (2 * math.pi**2))) * (math.pi * math.sqrt(3) / 2), 1.7768),
        "Myon":       (vev / (f / (math.pi**2)) / math.pi, 0.10566),
        "Elektron":   (vev / (f * (2 * math.pi**3 + 3)), 0.00051099)
    }
    
    print(f"{'TEILCHEN':<15} | {'MODELL (GeV)':<15} | {'SOLL (GeV)':<12} | {'PRÄZISION'}")
    print("-" * 65)
    
    for name, (val, soll) in results.items():
        precision = 100 - abs(1 - val/soll)*100
        print(f"{name:<15} | {val:<15.5f} | {soll:<12.5f} | {precision:.4f}%")

if __name__ == "__main__":
    print(f"--- TORSIONS-EINHEIT: SUB-PLANCK-FAKTOR {f} ---")
    run_world_formula()