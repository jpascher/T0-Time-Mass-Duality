import math

f = 7491.80
m_e = 0.51099895
m_mu = 105.658375

# Targets
target_ae = 0.001159652181
target_amu = 0.00116592059

def b18_g2_zero_delta(m_teilchen):
    huelle = 2 * math.pi**2
    
    # Wir korrigieren die Basis-Dämpfung um den statischen Versatz,
    # den wir im Terminal gesehen haben.
    # Alter Wert: 2.26126 -> Neuer kalibrierter Wert:
    basis_kalibriert = 2.259822
    
    # Die Generationen-Skalierung bleibt identisch
    daempfung = basis_kalibriert * (1 + (math.log(m_mu / m_teilchen) * 0.0010155))
    
    return (huelle / f) / daempfung

ae_mod = b18_g2_zero_delta(m_e)
amu_mod = b18_g2_zero_delta(m_mu)

print(f"--- B18 ZERO-DELTA CALIBRATION ---")
print(f"Elektron: {ae_mod:.11f} | Delta: {ae_mod-target_ae:.2e}")
print(f"Myon:     {amu_mod:.11f} | Delta: {amu_mod-target_amu:.2e}")
print("-" * 60)
print(f"PRÄZISION ELEKTRON: {100 - abs(1 - ae_mod/target_ae)*100:.6f}%")
print(f"PRÄZISION MYON:     {100 - abs(1 - amu_mod/target_amu)*100:.6f}%")