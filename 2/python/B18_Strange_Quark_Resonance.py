import math

f = 7491.80
target_strange = 95.0 
phi = (1 + math.sqrt(5)) / 2

def b18_strange_phi():
    huelle = 2 * math.pi**2
    
    # Der Teiler für das Strange-Quark (Generation 2)
    # Wir nutzen die Hülle skaliert durch den Goldenen Schnitt phi,
    # da Quarks die pentagonale Symmetrie des Torsos anders "brechen" als Leptonen.
    teiler = (huelle**2 / (phi * 3.125)) 
    
    m_strange_modell = f / teiler
    
    return m_strange_modell

m_s = b18_strange_phi()

print(f"--- B18 STRANGE PHI-RESONANCE ---")
print(f"Sub-Planck-Faktor f: {f}")
print(f"Modell Masse s:      {m_s:.2f} MeV/c²")
print(f"Experiment-Soll:     {target_strange:.2f} MeV/c²")
print("-" * 50)
print(f"PRÄZISION: {100 - abs(1 - m_s/target_strange)*100:.6f}%")