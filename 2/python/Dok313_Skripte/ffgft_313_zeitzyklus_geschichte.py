#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 313 — Kein Anfang: Die thermische Geschichte auf dem
Zeitzyklus. Rechnungen zu Pflicht D(ii).

Frage: Koennen die Feldkonfigurationen auf dem 92-Gyr-Zyklus
periodisch schliessen UND die beobachtete thermische Abfolge tragen?

R1  Antipoden-Befund: Wo sitzt die beobachtbare Geschichte auf dem
    Zyklus? (Partikelhorizont vs. halbe Zyklenlaenge)
R2  Schliessungsprofil: Massenlauf m(theta) entlang des Zyklus;
    Steigung am Umkehrpunkt vs. glatte periodische Schliessung.
R3  Entropie-Hindernis: exakte tau_c-Periodizitaet vs.
    Poincare-Wiederkehr — Groessenordnung der Diskrepanz.
R4  Pruefflaechen: was koennte hinter die Wand sehen?

Eingaben: Dok-312-Kette [K|P20] und Planck-LCDM-Parameter fuer die
z->chi-Abbildung (die Abbildung selbst ist lesartunabhaengig, da nur
dimensionslose Verhaeltnisse eingehen; Dok 267/312 Statik-Kapitel).
"""

from math import pi, log10
from numpy import sqrt

C   = 2.99792458e8
XI  = 4/30000
LAM_E = 3.8615926796e-13
H0  = (pi/2)*C*XI**10/LAM_E          # 1/s   (66.82 km/s/Mpc)
R_H = C/H0
L_STAR = 2*pi*R_H
TAU_C  = L_STAR/C                     # = 2 pi / H0
MPC = 3.0856775814913673e22
GPC = 1e3*MPC
GYR = 3.155815e16

# LCDM-Abbildung z -> chi (nur fuer die dimensionslose Zuordnung)
OM, OR, OL = 0.315, 9.2e-5, 0.685 - 9.2e-5

def Hz(z):
    return H0*sqrt(OM*(1+z)**3 + OR*(1+z)**4 + OL)

def chi(z, n=400000):
    # mitbewegte Distanz, einfache Integration
    import numpy as np
    zz = np.linspace(0, z, n)
    return np.trapezoid(C/Hz(zz), zz)

import numpy as np

print("=== Dok. 313 — Rechnungen zu D(ii) ===\n")
print(f"tau_c = 2 pi/H0 = {TAU_C/GYR:.1f} Gyr;  L* = {L_STAR/GPC:.2f} Gpc;"
      f"  L*/2 = {L_STAR/2/GPC:.2f} Gpc")

# ---------------------------------------------------------------
# R1 — Antipoden-Befund
# ---------------------------------------------------------------
print("\n--- R1: Wo sitzt die Geschichte auf dem Zyklus? ---")
chi_rec = chi(1090)
# Partikelhorizont: z -> unendlich; Integration bis z=1e8 genuegt
zz = np.logspace(np.log10(1090), 8, 200000)
eta0 = chi_rec + np.trapezoid(C/Hz(zz), zz)
half = L_STAR/2
print(f"chi(Rekombination, z=1090) = {chi_rec/GPC:6.2f} Gpc"
      f"  ->  Anteil der Halbzyklus-Distanz: {chi_rec/half:.4f}")
print(f"Partikelhorizont eta_0     = {eta0/GPC:6.2f} Gpc"
      f"  ->  Anteil: {eta0/half:.4f}")
print(">>> Die GESAMTE beobachtbare Geschichte (bis z->unendlich)")
print(f">>> fuellt {eta0/half*100:.1f}% des HALBEN Zeitzyklus:")
print(">>> Die letzte Streuflaeche sitzt am Antipoden (98%), der")
print(">>> formale 'Anfang' 2% dahinter. [K|P20 x LCDM-Abbildung]")

# Winkelpositionen auf dem Zyklus (theta = chi/R_H)
print("\nPositionen auf dem Zyklus (theta in Einheiten von pi):")
for z in (0.5, 1, 3, 10, 100, 1090):
    th = chi(z)/R_H
    print(f"  z={z:6g}: theta = {th/pi:.3f} pi   m(z)/m0 = {1/(1+z):.4g}")

# ---------------------------------------------------------------
# R2 — Schliessungsprofil und Steigung am Umkehrpunkt
# ---------------------------------------------------------------
print("\n--- R2: Glatte periodische Schliessung? ---")
# Massenlauf-Lesart (Dok 312, Statik): m(theta)/m0 = 1/(1+z(theta)).
# Periodizitaet verlangt m stetig auf dem Kreis; einfachste
# Schliessung: gerades Profil um den Antipoden (Minimum dort).
# Bedingung fuer GLATTE Schliessung: dm/dtheta -> 0 am Endpunkt.
# Analytisch: Strahlungsaera H ~ H0 sqrt(OR) (1+z)^2
#   -> eta0 - chi = c/(H0 sqrt(OR)) * 1/(1+z)
#   -> m/m0 = 1/(1+z) = (eta0-chi) * H0 sqrt(OR)/c
#   -> dm/dtheta|_Ende = sqrt(OR) * (R_H H0/c) = sqrt(OR)
slope_end = sqrt(OR)
print(f"Analytisch: |dm/dtheta| am Endpunkt = sqrt(Omega_r) "
      f"= {slope_end:.4f}")
# Numerische Kontrolle:
z1, z2 = 5e6, 1e7
m1, m2 = 1/(1+z1), 1/(1+z2)
t1, t2 = chi(z1)/R_H, chi(z2)/R_H
print(f"Numerisch (z=5e6..1e7):    |dm/dtheta| = "
      f"{abs((m2-m1)/(t2-t1)):.4f}")
print(">>> Das beobachtete Profil laeuft mit Steigung ~0.01 in den")
print(">>> Endpunkt — auf 1% erfuellt es die Glattheitsbedingung")
print(">>> dm/dtheta = 0 einer geraden periodischen Schliessung.")
print(">>> Die Rueckkehr-Haelfte ist exakt die photonisch")
print(">>> unbeobachtbare Haelfte (hinter der Streuwand). [K]")

# ---------------------------------------------------------------
# R3 — Entropie-Hindernis (die eigentliche Verschaerfung von D)
# ---------------------------------------------------------------
print("\n--- R3: Entropie-Hindernis [K] ---")
S_cmb = 1e89      # k_B, Photonen im beobachtbaren Volumen
S_bh  = 1e104     # k_B, dominiert von supermassiven SL
print(f"Entropiebudget (beobachtbar): CMB ~ 1e89 k_B, "
      f"SL ~ 1e104 k_B")
print(f"Poincare-Wiederkehrzeit ~ exp(S/k_B) ~ 10^(10^104) tau_dyn")
print(f"Zyklus tau_c ~ 10^{log10(TAU_C):.1f} s")
print(">>> log10(t_Poincare/tau_c) ~ 10^104: exakte tau_c-Periodi-")
print(">>> zitaet ist dynamisch NICHT generisch — sie muss als")
print(">>> Randbedingung GESETZT werden (Auswahl periodischer")
print(">>> Loesungen). Feinkoernige Entropie: unter unitaerer")
print(">>> Evolution konstant — Periodizitaet zulaessig [K].")
print(">>> Grobkoernige Entropie (2. Hauptsatz): muss auf der")
print(">>> Rueckkehr-Haelfte abnehmen — beobachterrelativ moeglich,")
print(">>> aber unbewiesen. DAS ist der harte Kern von D(ii).")

# ---------------------------------------------------------------
# R4 — Pruefflaechen
# ---------------------------------------------------------------
print("\n--- R4: Was koennte hinter die Wand sehen? [S] ---")
z_nu, z_gw = 6e9, 1e25  # Entkopplung Neutrinos; GW aus Planck-Aera (nominell)
for name, z in (("C-nu-B (Neutrino-Hintergrund)", z_nu),
                ("primordiale GW", z_gw)):
    th = eta0/R_H  # praktisch identisch mit Horizont
    print(f"  {name}: entkoppelt bei z~{z:.0e} -> sitzt bei "
          f"theta ~ {th/pi:.3f} pi (am/hinter dem Antipoden)")
print(">>> Photonen enden an der Wand (0.984 pi); Neutrino- und")
print(">>> GW-Hintergruende stammen vom Antipoden selbst. Eine")
print(">>> nicht-monotone Signatur dort (Umkehr des Massenlaufs)")
print(">>> waere die prinzipielle Pruefflaeche fuer die Schliessung.")

# ---------------------------------------------------------------
# R5 — Die Antipoden-Bedingung invertiert: Omega_m-Vorhersage
# ---------------------------------------------------------------
print("\n--- R5: Antipoden-Bedingung als Vorhersage [S->pruefbar] ---")
def eta_H0(Om):
    OLx = 1 - Om - OR
    z = np.concatenate([np.linspace(0,1090,200000),
                        np.logspace(np.log10(1090.001),9,200000)])
    E = np.sqrt(Om*(1+z)**3 + OR*(1+z)**4 + OLx)
    return np.trapezoid(1/E, z)
print(f"eta0*H0/c (Om=0.315, Planck) = {eta_H0(0.315):.4f}  vs pi = {pi:.4f}")
# Bisektion: eta0*H0/c = pi
lo, hi = 0.2, 0.5
for _ in range(60):
    mid = 0.5*(lo+hi)
    if eta_H0(mid) > pi: lo = mid
    else: hi = mid
Om_star = 0.5*(lo+hi)
OL_star = 1 - Om_star - OR
print(f"Bedingung eta0 = pi*R_H exakt  ->  Omega_m* = {Om_star:.4f}")
print(f"  Planck: 0.315 +/- 0.007  ->  Abstand {(Om_star-0.315)/0.007:+.1f} sigma")
print(f"  Omega_L* = {OL_star:.4f}  ->  kappa* = 3*Omega_L* = {3*OL_star:.3f}")
print(f"  gemessen (Dok 312, Pflicht B): kappa = 2.12  ->  Abw. "
      f"{(3*OL_star-2.119)/2.119*100:+.1f} %")
print("Gegenprobe (keine Zirkelrechnung): kappa=2.119 -> Om=0.294")
print(f"  -> eta0*H0/c = {eta_H0(0.294):.4f} != pi: echte 4%-Spannung.")
print(">>> Pflicht B und die Antipoden-Koinzidenz verschmelzen zu")
print(">>> EINER Bedingung; Om* = 0.325 ist falsifizierbar (DESI/Euclid).")
# T0-Offenheit (R61-Disziplin: kein Fit)
kT0_me = 1.380649e-23*2.7255/(9.1093837015e-31*C**2)
import math
print(f"\nOffen: k_B T0/(m_e c^2) = {kT0_me:.3e}; log_xi = "
      f"{math.log(kT0_me)/math.log(XI):.2f} — keine ganze xi-Potenz:")
print("T0 (Antipoden-Temperatur / Photon-Baryon-Entropie) unangebunden.")

print("\n=== Fazit ===")
print("R1 Beobachtbare Geschichte = ein Halbzyklus (auf 2%) [K|P20]")
print("R2 Endpunktsteigung sqrt(Omega_r)~0.01: glatte gerade")
print("   Schliessung um den Antipoden auf 1% erfuellt [K]")
print("R3 Periodizitaet = Randbedingung, nicht Dynamik; grob-")
print("   koernige Entropie-Schliessung offen — Kern von D(ii) [K]")
print("R4 Pruefflaechen: C-nu-B/GW vom Antipoden [S]")
print("R5 Antipoden-Bedingung invertiert: Omega_m* = 0.325 (+1.4 sigma");
print("   zu Planck), kappa* = 2.03 (Kandidat fuer Pflicht B); T0 offen")
