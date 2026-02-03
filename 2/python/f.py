import math
from fractions import Fraction

# --- B18 BASIS-KONSTANTEN ---
# f: sub-Planck length Skalierung (Verhältnis Planck-Zeit zu t0)
f = 7500                         
# xi: Torsionskonstante (Gitterspannung), abgeleitet aus 4/3-Relation
xi = float(Fraction(4, 3) * 1e-4) 

def b18_alpha_berechnung():
    """
    Berechnet den Kehrwert der Feinstrukturkonstante (alpha^-1)
    basierend auf der idealen 4D-Geometrie des B18-Gitters.
    Formel: (f * xi) * pi^4 * sqrt(2)
    """
    
    # 1. Die Gitter-Einheit (Kopplungsdichte)
    # In der B18-Theorie ergibt das Produkt aus Skalierung und Torsion 1.0
    gitter_einheit = f * xi
    
    # 2. Die ideale geometrische Resonanz
    # pi^4: Ausbreitung im 4-dimensionalen Raum
    # sqrt(2): Projektion über die Gitterdiagonale
    ideale_geometrie = math.pi**4 * math.sqrt(2)
    
    # 3. Das theoretische Resultat
    alpha_inv_theo = gitter_einheit * ideale_geometrie
    
    return alpha_inv_theo, gitter_einheit, ideale_geometrie

# --- AUSWERTUNG UND VERGLEICH ---
res, einheit, geom = b18_alpha_berechnung()
ref_codata = 137.035999

# Fehleranalyse
abweichung_absolut = res - ref_codata
praezision = (1 - abs(abweichung_absolut) / ref_codata) * 100

print(f"--- B18: FORMEL-BASIERTE HERLEITUNG (IDEAL) ---")
print(f"Basis f (sub-Planck): {f}")
print(f"Basis xi (Torsion):   {xi:.6e}")
print(f"Gitter-Einheit (f*xi): {einheit:.4f}")
print("-" * 45)
print(f"RESULTAT alpha^-1:    {res:.6f}")
print(f"REFERENZ CODATA:      {ref_codata:.6f}")
print("-" * 45)
print(f"Absoluter Fehler:     {abweichung_absolut:.6f}")
print(f"Relative Präzision:   {praezision:.4f} %")
print("-" * 45)