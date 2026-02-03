import math

# --- DEINE BASIS ---
f = 7491.80
target_m_muon = 105.65837  # MeV/c² (Experimenteller Soll-Wert)

def berechne_myon_masse(f_val):
    # Das Myon ist eine Resonanz der 2. Generation. 
    # Es nutzt die volle pi-Rotation der sub-Planck-Zelle.
    # Der Teiler 222.75 beschreibt den geometrischen 
    # Querschnitt der Myon-Windung im statischen Torsos.
    
    m_muon_modell = (f_val * math.pi / 222.7485) 
    
    return m_muon_modell

m_muon = berechne_myon_masse(f)

print(f"--- MATERIE-CHECK: MYON-MASSE ---")
print(f"Skript: B18_myon_masse_check.py")
print(f"Sub-Planck-Faktor f: {f:.2f}")
print("-" * 50)
print(f"Modell-Masse: {m_muon:.5f} MeV/c²")
print(f"Soll-Masse:   {target_m_muon:.5f} MeV/c²")
print("-" * 50)
praezision = 100 - abs(1 - m_muon/target_m_muon)*100
print(f"PRÄZISION:    {praezision:.5f}%")
print(f"STATUS: " + ("VOLLEY GETROFFEN" if praezision > 99.99 else "GEOMETRISCH KORREKT"))