import math

# Deine Ergebnisse
N_t0 = 2.73e72
C_target = 1.96e39

# 1. Lineare Zellen (entlang des Durchmessers)
N_linear = N_t0**(1/3)

# 2. Oberflächen-Zellen (Fläche des Myons)
N_surface = N_t0**(2/3)

print(f"--- Struktur der Torsions-Kopplung ---")
print(f"Ziel-Kopplung C:         {C_target:.2e}")
print(f"Lineare t0-Elemente:     {N_linear:.2e}")
print(f"Oberflächen t0-Elemente: {N_surface:.2e}")
print(f"\nVerhältnis C / N_surface: {C_target / N_surface:.5f}")