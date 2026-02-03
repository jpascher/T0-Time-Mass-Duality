import math
from ffgft_constants import F_REAL, T0_ANKER

def berechne_torsion():
    # Die Hüllenspannung des 4D-Torsos
    huelle = 2 * math.pi**2
    # Torsionsdichte im Verhältnis zum Anker
    torsions_dichte = F_REAL / T0_ANKER
    return huelle * torsions_dichte

torsion = berechne_torsion()
print(f"Reale Gitter-Torsion: {torsion:.4f}")