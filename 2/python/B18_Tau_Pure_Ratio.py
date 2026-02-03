import math

f = 7491.80
m_e = 0.51099895
m_mu = 105.658375
m_tau = 1776.86  # Masse der 3. Generation (Exp. Wert)

def b18_g2_pure_ratio(m_target, m_reference):
    # Basis-Hülle
    huelle = 2 * math.pi**2
    # Kalibrierte Kristall-Basis
    basis = 2.259822
    
    # Rein geometrisches Verhältnis der Massen-Windungen im Kristall
    # Keine Feinstrukturkonstante, nur das logarithmische Verhältnis
    daempfung = basis * (1 + (math.log(m_reference / m_target) * 0.0010155))
    
    return (huelle / f) / daempfung

# Wir berechnen Tau im Verhältnis zum Myon
g2_tau_pred = b18_g2_pure_ratio(m_tau, m_mu)

print(f"--- B18 PURE RATIO: TAU-PROGNOSE ---")
print(f"Masse Tau: {m_tau} MeV/c²")
print(f"B18 g-2 Prognose: {g2_tau_pred:.10f}")
print("-" * 45)
print("Logik: Rein geometrische Massen-Verhältnisse.")