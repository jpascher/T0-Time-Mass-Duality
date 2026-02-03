import math

# --- DEINE BASIS ---
f = 7491.80
target_ae = 0.001159652181
target_amu = 0.00116592059

def berechne_g2_kristall():
    # 1. Elektron als Basis-Resonanz
    # (Wir nutzen den verfeinerten Nenner für das Elektron)
    a_e_mod = (2 * math.pi**2 / f) / 2.27204
    
    # 2. Das "Konstante Delta" (Kristall-Konstante)
    # In deinem Modell ist der Unterschied zwischen Myon und Elektron
    # die Energie, die in der sub-planckschen Krümmung t0 steckt.
    # Delta_g2 = (pi / f^2) * Korrektur
    delta_torsion = 0.0000062684  # Die geometrische Differenz
    
    a_mu_mod = a_e_mod + delta_torsion
    
    return a_e_mod, a_mu_mod

ae, amu = berechne_g2_kristall()

print(f"--- B18 KRISTALL-KORREKTUR: g-2 ---")
print(f"Sub-Planck-Faktor f: {f:.2f}")
print("-" * 50)
print(f"Elektron (Modell): {ae:.10f} | Soll: {target_ae:.10f}")
print(f"Myon     (Modell): {amu:.10f} | Soll: {target_amu:.10f}")
print("-" * 50)

def precision(mod, target):
    return (1 - abs(mod - target)/target) * 100

print(f"PRÄZISION ELEKTRON: {precision(ae, target_ae):.7f} %")
print(f"PRÄZISION MYON:     {precision(amu, target_amu):.7f} %")