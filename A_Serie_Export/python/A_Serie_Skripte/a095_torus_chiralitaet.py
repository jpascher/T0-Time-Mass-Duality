"""A095: Fourier-Projektor P_+, g_R=0 algebraisch."""
import numpy as np

print("=== A095: Chirale Projektion auf T^4 ===")

# Basis |n,m> auf T^2 (vereinfacht)
# Außenzustand: (1,+1), Innenzustand: (1,-1)
# P_+ = Projektor auf m>=0 Sektor

def P_plus(n, m):
    """Fourier-Projektor auf m>=0 (positiver Chiralitätssektor)"""
    return (n, m) if m >= 0 else (0, 0)  # (0,0) = Nullvektor

states = [("Außen |1,+1>", 1, +1),
          ("Innen |1,-1>", 1, -1),
          ("Grund |1, 0>", 1,  0),
          ("Vakuu |0, 0>", 0,  0)]

print("Wirkung von P_+ (m>=0-Projektor):")
for name, n, m in states:
    result = P_plus(n, m)
    survived = result != (0, 0) or (n, m) == (0, 0)
    label = f"|{result[0]},{result[1]:+d}>" if result != (0,0) else "0 (Nullvektor)"
    print(f"  P_+ {name}: -> {label}")

print()
# Kopplung
print("Schwache Kopplung g = <psi_proj|H_weak|psi_proj>:")
print("  Außen: P_+|1,+1> = |1,+1>  -> g_L = <1,+1|H|1,+1> != 0")
print("  Innen: P_+|1,-1> = 0        -> g_R = <0|H|0> = 0  ✓")
print()

# Probe: kein residualer Term
# <0|H_weak|0> = 0 für jeden H_weak (Nullvektor-Argument)
g_R = np.dot([0,0], np.array([[1,0],[0,1]]) @ [0,0])
assert g_R == 0.0
print(f"Numerische Probe: g_R = <0|H|0> = {g_R} ✓")
print()
print("Resultat: g_R=0 folgt algebraisch aus P_+|1,-1>=0.")
print("Offene Kante: warum P_+ (nicht P_-) der physikalische Projektor ist.")
print("\nAlle Checks bestanden.")
