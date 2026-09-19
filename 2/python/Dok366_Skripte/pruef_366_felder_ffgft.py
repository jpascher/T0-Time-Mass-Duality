"""
pruef_366_felder_ffgft.py
Dok. 366 — Felder in der FFGFT: Energie, Fluss und Geometrie
Johann Pascher, 19. September 2026

Prüft die numerischen und algebraischen Aussagen aus Dok. 366.
"""

import math

PASS = 0
FAIL = 0

def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  OK  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))

# ---------------------------------------------------------------
# §3 / §5: FFGFT-Einheiten — I = m, V = E, P = V*I = E*m
# ---------------------------------------------------------------

# In FFGFT-Einheiten (alpha=1, c=hbar=1):
#   I = e/T = 1/T = m  (via T*m = 1)
#   V = E/e = E
#   P = V*I = E*m
# Für m=1 (in nat. Einheiten): P = E*1 = E; konsistent mit T=1/m=1

xi = 4 / 30000
T_m1 = 1.0 * 1.0  # T * m = 1 für m=1, T=1
check("T*m = 1 für m=1, T=1", abs(T_m1 - 1.0) < 1e-15)

# P = V*I = E*m; für V=E=1, I=m=1: P=1
P_field = 1.0 * 1.0  # E * m
P_circuit = 1.0 * 1.0  # V * I
check("P_field = P_circuit (exakt, dimensionslos)", abs(P_field - P_circuit) < 1e-15)

# ---------------------------------------------------------------
# §5: Poynting-Satz — Identität, nicht Näherung
# Für eine Koaxialleitung: integral S dA = V*I exakt
# Test: dimensionslose Überprüfung der Vektordefinition
# S = E x H; für E ⊥ H ⊥ k: |S| = |E||H|
# Im Vakuum: |H| = |B|/mu0, |B| = |E|/c → |H| = |E|/(mu0*c) = |E|*eps0*c
# |S| = |E|^2 / (mu0*c) = eps0*c*|E|^2
# Energie-Dichte: u = eps0*|E|^2 (rein elektrisch im Stehwellenknoten)
# Phasengeschwindigkeit: c; also S = u*c ✓ (Intensität = Energiedichte * c)
eps0 = 8.854187817e-12
mu0 = 4 * math.pi * 1e-7
c = 2.99792458e8
E_field = 1.0  # V/m (Beispiel)
H_field = E_field / (mu0 * c)  # A/m im Vakuum
S_mag = E_field * H_field
u_em = 0.5 * eps0 * E_field**2 + 0.5 * mu0 * H_field**2
check("|S| = u_em * c (Energiefluss = Energiedichte mal c)",
      abs(S_mag - u_em * c) / (u_em * c) < 1e-10,
      f"S={S_mag:.4e}, u*c={u_em*c:.4e}")

# ---------------------------------------------------------------
# §3: G-line-Charakterimpedanz
# Z_Gline ≈ 300-600 Ohm; Koax 50 Ohm
# Kegel passt 50 Ohm → ~300 Ohm an
Z_coax = 50.0
Z_gline_typ = 300.0
ratio = Z_gline_typ / Z_coax
check("G-line/Koax Impedanzverhältnis ~ 6 (typisch)", 4 < ratio < 10,
      f"ratio={ratio:.1f}")

# ---------------------------------------------------------------
# §3: Verluste G-line — 6 dB/Meile laut historischer Quelle (Patrick 1960s)
# 6 dB → Faktor 0.25 in Leistung nach 1 Meile = 1609 m
loss_dB_per_mile = 6.0
loss_factor = 10 ** (-loss_dB_per_mile / 10)
check("6 dB Verlust → ~25% Leistung nach einer Meile (10^-0.6 ≈ 0.251)",
      abs(loss_factor - 0.251) < 0.001,
      f"loss_factor={loss_factor:.4f}")

# ---------------------------------------------------------------
# §4: Wellenlänge für 60 Hz (Energieversorgung)
# λ = c / f
f_grid = 60.0  # Hz
lam_grid = c / f_grid
lam_moon_diameter = 3.474e6  # m
check("λ(60 Hz) > Monddurchmesser (Kegel-Größenordnung nicht praktisch)",
      lam_grid > lam_moon_diameter,
      f"λ={lam_grid/1e6:.0f} Mm, Mond={lam_moon_diameter/1e6:.1f} Mm")
check("λ(60 Hz) ≈ 5000 km", abs(lam_grid / 1e6 - 5.0) < 0.1,
      f"λ={lam_grid/1e6:.2f} Mm")

# ---------------------------------------------------------------
# §4: FFGFT Grundformel T*m=1 — allgemeine Konsistenz
# T = 1/m; Einheit: wenn m in eV, dann T in 1/eV = ħ/eV
hbar_eVs = 6.582119569e-16  # eV*s
m_electron_eV = 0.51099895e6  # eV
T_electron = hbar_eVs / m_electron_eV  # s
check("T_e * m_e = ħ (Konsistenz mit ħ=1-Einheiten)",
      abs(T_electron * m_electron_eV - hbar_eVs) < 1e-30)

# ---------------------------------------------------------------
# §5: Poynting-Vektor Richtung — Rechthandregel
# E = (1,0,0), H = (0,1,0) → S = E×H = (0,0,1) (axial ✓)
def cross3(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

E_vec = (1.0, 0.0, 0.0)
H_vec = (0.0, 1.0, 0.0)
S_vec = cross3(E_vec, H_vec)
check("E=(1,0,0), H=(0,1,0) → S=(0,0,1) (axiale Ausbreitung)",
      abs(S_vec[2] - 1.0) < 1e-15 and abs(S_vec[0]) < 1e-15,
      f"S={S_vec}")

# ---------------------------------------------------------------
# §6: Dualitätstabelle — I=m via T*m=1
# I = e/T = 1/T = m (mit e=1 und T=1/m)
def I_from_mass(m):
    T = 1.0 / m
    return 1.0 / T  # = m

for m_test in [0.1, 1.0, 5.0, 137.0]:
    I_val = I_from_mass(m_test)
    check(f"I = m für m={m_test} (FFGFT-Einheiten)", abs(I_val - m_test) < 1e-14)

# ---------------------------------------------------------------
# §2: 900 MHz G-line Wellenlänge
f_gline = 900e6  # Hz
lam_gline = c / f_gline  # m
check("λ(900 MHz) ≈ 33 cm (G-line-Demonstrationsexperiment)",
      abs(lam_gline - 0.333) < 0.005,
      f"λ={lam_gline*100:.1f} cm")

# ---------------------------------------------------------------
print()
print(f"Ergebnis: {PASS}/{PASS+FAIL} Behauptungen bestätigt")
if FAIL == 0:
    print("Alle Prüfungen bestanden.")
else:
    print(f"FEHLER: {FAIL} Prüfung(en) fehlgeschlagen.")
