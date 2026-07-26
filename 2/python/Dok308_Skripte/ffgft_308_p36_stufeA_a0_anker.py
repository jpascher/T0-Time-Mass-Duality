#!/usr/bin/env python3
# ffgft_308_p36_stufeA_a0_anker.py  —  Dok. 307, P36 Stufe A
# ---------------------------------------------------------------------------
# a_0-Anker: MOND-Koinzidenz aus FFGFT xi^10-Kette (K6, Dok. 190).
# Zeigt: a_0 = c*H0/(2*pi) folgt ohne freie Parameter aus
#   H0/c = (pi/2) * xi^10 / lambda_e_bar
# Vergleich mit RAR-Wert (McGaugh, Lelli, Schombert 2016, PRL 117, 201101).
# Konsistenzfolge: baryonische Tully-Fisher v^4 = G*M_b*a_0 fuer DDO 154.
# ---------------------------------------------------------------------------
# Status: [K] Kernableitung (Groessenordnungsniveau)
# Alle Eingaben deklariert, keine freien Parameter, keine Fits.
# ---------------------------------------------------------------------------

import math

# --- Naturkonstanten (SI) ---
c      = 2.99792458e8       # m/s
hbar   = 1.054571817e-34    # J*s
m_e    = 9.1093837015e-31   # kg
G      = 6.67430e-11        # m^3 kg^-1 s^-2
kpc    = 3.08568e19         # m
Msun   = 1.98892e30         # kg

# --- FFGFT-Parameter (deklarierte Setzung, P33) ---
xi = 4.0 / 30000.0          # dimensionslos

# --- Compton-Wellenlaenge des Elektrons ---
lambda_e_bar = hbar / (m_e * c)   # m

# --- H0 aus xi^10-Kette (K6, Dok. 279) ---
H0 = c * (math.pi / 2.0) * xi**10 / lambda_e_bar   # s^-1
H0_kmsMpc = H0 * kpc / 1e3                          # km/s/Mpc

# --- a_0 aus H0 ---
a0_ffgft = c * H0 / (2.0 * math.pi)   # m/s^2

# --- RAR-Wert (externe Referenz, McGaugh+2016) ---
a0_emp = 1.2e-10   # m/s^2

ratio_a0 = a0_ffgft / a0_emp

print("=" * 62)
print(" P36 Stufe A — a_0-Anker aus FFGFT xi^10-Kette")
print("=" * 62)
print(f"  xi               = {xi:.6e}  (4/30000, Setzung P33)")
print(f"  lambda_e_bar     = {lambda_e_bar:.6e} m")
print(f"  H0 (FFGFT)       = {H0_kmsMpc:.4f} km/s/Mpc")
print(f"  a0 (FFGFT)       = c*H0/(2*pi) = {a0_ffgft:.4e} m/s^2")
print(f"  a0 (RAR-Fit emp) = {a0_emp:.4e} m/s^2")
print(f"  ratio            = {ratio_a0:.4f}  (14% Abweichung)")
print()

# --- Baryonische Tully-Fisher: v_flat = (G*M_b*a0)^(1/4) ---
print("Konsistenz baryonische Tully-Fisher v^4 = G*M_b*a_0:")
cases = [
    ("DDO 154",      3.5e8,  47.0, "Carignan+Purton 1998"),
    ("NGC 3198",     1.5e10, 150.0, "van Albada+1985"),
    ("Milchstrasse", 6.0e10, 220.0, "Bland-Hawthorn+Gerhard 2016"),
]
print(f"  {'Galaxie':<20} {'v_FFGFT':>10} {'v_obs':>10} {'ratio':>7}")
print("  " + "-" * 52)
for name, Mb_sol, v_obs, ref in cases:
    Mb = Mb_sol * Msun
    v_flat = (G * Mb * a0_ffgft)**0.25 / 1e3
    print(f"  {name:<20} {v_flat:>10.1f} {v_obs:>10.1f} {v_flat/v_obs:>7.3f}")

print()
print("BEFUND:")
print(f"  MOND-Koinzidenz a0 ~ c*H0 ist in FFGFT keine Koinzidenz,")
print(f"  sondern Konsequenz der xi^10-Kette (K6). Abweichung 14%.")
print(f"  DDO 154 (sauberster Test): ratio = {(G*3.5e8*Msun*a0_ffgft)**0.25/1e3/47:.3f}")
