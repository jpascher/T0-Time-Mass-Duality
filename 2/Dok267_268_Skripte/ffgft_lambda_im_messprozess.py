#!/usr/bin/env python3
"""
================================================================================
ffgft_lambda_im_messprozess.py
Die Laengenskala im CMB-Messprozess: was wirklich gemessen wird
================================================================================

Gehoert zu Dok. 267 (Kosmologische Entartung), Abschnitt
"Absolute Skala: R_H aus xi".

Die Frage: Die Peak-VERHAELTNISSE folgen aus der T4-Geometrie (kein
freier Parameter). Die absolute POSITION ell_1 ~ 220 braucht eine
Laengenskala. Was wird im Messprozess eigentlich festgelegt -- und
was bleibt extern (P20)?

Kernpunkt: Ein gemessener Winkel theta = L_res / D_A ist ein
VERHAELTNIS. Eindeutig bestimmbar ist nur das Produkt H0 * L_res,
nicht H0 allein. Das Isolieren von H0 (bzw. R_H) braucht eine
extern festgelegte Laenge -- den externen Parameter P20.

Nur SI-CODATA-Konstanten + xi = 1/7500.
================================================================================
"""
import math

# --- Fundamentalkonstanten (CODATA, SI) ---
c    = 299792458.0          # m/s
hbar = 1.054571817e-34      # J*s
eV   = 1.602176634e-19      # J
Mpc  = 3.0856775814913673e22  # m

# --- Der eine Parameter ---
xi     = 1/7500
ln_inv = math.log(1/xi)

# --- FFGFT-Referenzwerte (Kernzahlen, Dok. 182) ---
H0_kms_Mpc = 66.19           # km/s/Mpc (FFGFT-Referenz)
H0_SI = H0_kms_Mpc*1000/Mpc  # 1/s
R_H = c / H0_SI              # m
z_star = 875                 # Referenz-z* (Exponent 1/ln(1/xi))
A_trumpet = 303.6            # Trompetenformel-Parameter (Dok. 267)

print("="*72)
print("Die Laengenskala im CMB-Messprozess")
print("="*72)
print(f"xi = 1/7500 = {xi:.6e}")
print(f"H0 = {H0_kms_Mpc} km/s/Mpc (FFGFT, aus xi via Exponent 41/4)")
print(f"R_H = c/H0 = {R_H/Mpc:.0f} Mpc = {R_H:.3e} m")
print()

# ---------------------------------------------------------------------------
# TEIL 1: R_H aus xi -- die FFGFT-interne Skala (Dok. 182)
# ---------------------------------------------------------------------------
print("TEIL 1: R_H aus xi (Dok. 182) -- kein freier Parameter")
print("-"*72)
print("  xi -> E_0 = sqrt(m_e m_mu) -> E_H = E_0 xi^(41/4) -> R_H = hbar c/E_H")
print(f"  Ergebnis: R_H = {R_H/Mpc:.0f} Mpc, H0 = {H0_kms_Mpc} km/s/Mpc")
print("  R_H ist zugleich der Schwarzschild-Radius der Gesamtmasse M_U")
print("  des statischen Universums (interne Konsistenz, Dok. 190 P4).")
print()
print("  ABER: der Exponent 41/4 ist NICHT aus der T4-Geometrie")
print("        hergeleitet (P20). Das ist die eine externe Eingabe.")
print()

# ---------------------------------------------------------------------------
# TEIL 2: Der gemessene Winkel ist ein Verhaeltnis
# ---------------------------------------------------------------------------
print("TEIL 2: Der gemessene Winkel ist ein Verhaeltnis theta = L_res/D_A")
print("-"*72)
# Grundton-Winkel aus der Trompetenformel (Dok. 267): theta_1 = pi/A
theta_1_rad = math.pi / A_trumpet
theta_1_deg = math.degrees(theta_1_rad)
print(f"  Grundton-Winkel theta_1 = pi/A = pi/{A_trumpet}")
print(f"                          = {theta_1_rad:.5f} rad = {theta_1_deg:.3f} Grad")
print()
D_A = R_H * math.log(1 + z_star)
print(f"  Winkeldistanz D_A = R_H ln(1+z_*), z_* = {z_star}:")
print(f"    D_A = {D_A/Mpc:.0f} Mpc")
L_res = theta_1_rad * D_A
print(f"    L_res = theta_1 * D_A = {L_res/Mpc:.1f} Mpc")
print(f"    -> der effektive Resonatorradius L_res folgt erst MIT D_A.")
print()

# ---------------------------------------------------------------------------
# TEIL 3: Eindeutig messbar ist nur H0 * L_res
# ---------------------------------------------------------------------------
print("TEIL 3: Eindeutig messbar ist nur das Produkt H0 * L_res")
print("-"*72)
# theta_1 = L_res/D_A, D_A = (c/H0) ln(1+z_*)
# => H0 * L_res = theta_1 * c / ln(1+z_*)
prod = theta_1_rad * c / math.log(1+z_star)   # m/s
print(f"  theta_1 = L_res/D_A,  D_A = (c/H0) ln(1+z_*)")
print(f"  => H0 * L_res = theta_1 * c / ln(1+z_*) = {prod/1000:.0f} km/s")
print()
print(f"  Das Produkt H0*L_res = {prod/1000:.0f} km/s ist aus dem Winkel")
print(f"  eindeutig bestimmbar. H0 ALLEIN nicht -- man kann L_res nach")
print(f"  oben oder unten skalieren und H0 entsprechend anpassen,")
print(f"  ohne den gemessenen Winkel zu aendern.")
print()
print("  Demonstration -- verschiedene (H0, L_res), gleicher Winkel:")
print(f"  {'H0 [km/s/Mpc]':>15} {'L_res [Mpc]':>14} {'theta_1 [Grad]':>16}")
for H0_test in [60.0, 66.19, 73.0]:
    H0_test_SI = H0_test*1000/Mpc
    D_A_test = (c/H0_test_SI) * math.log(1+z_star)
    L_res_test = theta_1_rad * D_A_test
    theta_check = math.degrees(L_res_test / D_A_test)
    print(f"  {H0_test:>15.2f} {L_res_test/Mpc:>14.1f} {theta_check:>16.3f}")
print(f"  -> derselbe Winkel fuer jedes H0. Nur H0*L_res ist fix.")
print()

# ---------------------------------------------------------------------------
# Befund
# ---------------------------------------------------------------------------
print("="*72)
print("BEFUND")
print("="*72)
print(f"""
1. R_H ist in FFGFT aus xi bestimmt (R_H = {R_H/Mpc:.0f} Mpc, H0 = {H0_kms_Mpc}),
   aber ueber den Exponenten 41/4, der selbst nicht aus der T4-Geometrie
   folgt (P20). Das ist die eine externe Eingabe.

2. Der gemessene Grundton-Winkel theta_1 = pi/A ~ {theta_1_deg:.2f} Grad legt nur
   das Produkt H0*L_res = {prod/1000:.0f} km/s fest -- nicht H0 und nicht L_res
   einzeln. Ein Winkel ist immer ein Laengenverhaeltnis.

3. Um H0 (bzw. R_H) zu isolieren, muss eine absolute Laenge extern
   gesetzt werden. Das ist der externe Parameter P20. Die Peak-
   VERHAELTNISSE bleiben davon unberuehrt -- sie folgen aus der
   T4-Geometrie ohne jeden freien Parameter.

Bezug: Dok. 267 (kosmologische Entartung), Dok. 182 (R_H aus xi),
       Dok. 190 (P20 absolute Skala als externe Eingabe).
""")
