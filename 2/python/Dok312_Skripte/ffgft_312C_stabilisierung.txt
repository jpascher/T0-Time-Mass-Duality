#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 312 — Beiblatt C: Berechnungen zur Stabilitätsfrage
(kompaktifiziert oder ausgerollt?)

C1: Radius-Stabilisierung als Windungs-/Impulsmoden-Gleichgewicht
    (Spielzeugmodell, Brandenberger-Vafa-Typ) — invers gerechnet:
    Welche Windungsspannung ERZWINGT das Minimum bei L* = 2 pi R_H?
C2: Eddington-Kontrast: klassische Einstein-Loesung (instabil,
    Zeitkonstante) vs. Torus-Minimum (V'' > 0).
C3: Beobachtungsgrenze: Zyklenlaenge vs. CMB-Topologiesuchen.

Alle Ergebnisse [K|P20] bedingt (Exponent 10) und [S] fuer das
Spielzeugmodell (1 Zyklus, feste Quantenzahlen N_w, N_k).
KEINE Fits: T_w wird invers bestimmt und dann auf der xi-Leiter
gebucht; der Treffer auf Stufe xi^20 ist Ergebnis, nicht Eingabe.
"""

from math import pi, sqrt, log10

# ---------------------------------------------------------------
# Eingaben (wie Dok. 312 Hauptskript)
# ---------------------------------------------------------------
XI     = 4 / 30000
C      = 2.99792458e8            # m/s
HBAR   = 1.054571817e-34         # J s
LAM_E  = 3.8615926796e-13        # m   (Kammerton)
E_E    = HBAR * C / LAM_E        # J   (= m_e c^2)
GPC    = 3.0856775814913673e25   # m
GYR    = 3.155815e16             # s

N_EXP  = 10                      # [SETZUNG, P20]

H0     = (pi/2) * C * XI**N_EXP / LAM_E
R_H    = C / H0
LAM_ST = 1 / R_H**2              # Abschlussskala Lambda*
L_STAR = 2 * pi * R_H            # Ziel-Zyklenlaenge (Torusumfang)

print("=== Beiblatt C — Stabilitaet der statischen Konfiguration ===\n")
print(f"R_H     = {R_H:.4e} m")
print(f"L*      = 2 pi R_H = {L_STAR:.4e} m  (Identitaet: 4 lam_e/xi^10)")
assert abs(L_STAR - 4*LAM_E/XI**N_EXP)/L_STAR < 1e-12

# ===============================================================
# C1 — Windungs-/Impulsmoden-Gleichgewicht (Spielzeugmodell)
# ===============================================================
# Effektives Potential fuer die Zyklenlaenge L (1 Zyklus):
#   V(L) = N_w * T_w * L  +  N_k * 2 pi hbar c / L   (+ Casimir, klein)
# Windung: Energie ~ Spannung x Laenge (topologisch, nicht deformierbar)
# Impuls:  N_k feste Quanten mit E = 2 pi hbar c / L pro Quant
# Minimum: L* = sqrt( 2 pi N_k hbar c / (N_w T_w) )   -> V''(L*) > 0
#
# INVERSE Rechnung: T_w so, dass L* = 2 pi R_H (N_w = N_k = 1):
N_w, N_k = 1, 1
T_w = 2*pi * N_k * HBAR * C / (N_w * L_STAR**2)

print("\n--- C1: erforderliche Windungsspannung [K|P20, S] ---")
print(f"T_w = 2 pi hbar c / L*^2 = {T_w:.4e} N")

# Buchung auf der xi-Leiter (Kammerton-Spannungseinheit E_e/lam_e):
T_kam = E_E / LAM_E
ratio = T_w / T_kam
pred  = (pi/8) * XI**(2*N_EXP)
print(f"Kammerton-Spannung E_e/lam_e = {T_kam:.4e} N")
print(f"T_w / (E_e/lam_e) = {ratio:.4e}")
print(f"(pi/8) xi^20      = {pred:.4e}   rel. Abw. {abs(ratio-pred)/pred:.1e}")
assert abs(ratio - pred)/pred < 1e-12
print(">>> exakt:  T_w = (pi/8) (E_e/lam_e) xi^20        [Stufe 20 = 2x P20]")

# Direkter Zusammenhang mit der Abschlussskala:
T_via_L = HBAR * C * LAM_ST / (2*pi) * (N_k/N_w) * (2*pi)**2 / (2*pi)
# sauber: 1/L*^2 = Lambda*/(4 pi^2)  =>  T_w = hbar c Lambda* / (2 pi)
T_lam = HBAR * C * LAM_ST / (2*pi)
print(f"hbar c Lambda*/(2 pi) = {T_lam:.4e} N   rel. Abw. {abs(T_w-T_lam)/T_w:.1e}")
assert abs(T_w - T_lam)/T_w < 1e-12
print(">>> exakt:  T_w = hbar c Lambda* / (2 pi)")
print("    Eine Skala, zwei Rollen: dieselbe Stufe xi^20 traegt")
print("    Abschlussskala UND Stabilisierungsspannung. [S]")

# Gleichverteilung am Minimum (BV-Eigenschaft):
E_wind = N_w * T_w * L_STAR
E_mom  = N_k * 2*pi*HBAR*C / L_STAR
print(f"\nE_Windung(L*) = {E_wind:.4e} J")
print(f"E_Impuls (L*) = {E_mom:.4e} J   (Gleichverteilung: Abw. "
      f"{abs(E_wind-E_mom)/E_wind:.1e})")
print(f"Impulsquant am Minimum: 2 pi hbar c/L* = hbar c/R_H = hbar H0 "
      f"= {HBAR*H0:.4e} J = {HBAR*H0/1.602176634e-19:.2e} eV")
print(">>> Selbstkonsistenz: das Impulsquant am Minimum ist exakt hbar H0.")

# Stabilitaet:
Vpp = 2 * N_k * 2*pi*HBAR*C / L_STAR**3
print(f"\nV''(L*) = {Vpp:.4e} J/m^2  > 0  -> Minimum stabil (im Modell)")

# Casimir-Korrektur (masseloser Boson-Freiheitsgrad, periodisch):
E_cas = -pi*HBAR*C/(6*L_STAR)
print(f"Casimir-Term |E_C|/E_Impuls = {abs(E_cas)/E_mom:.3f} "
      f"(= 1/12 pro Freiheitsgrad) -> kleine Korrektur, kein Umkippen")

# Verschiebung des Minimums durch Casimir (N_c Freiheitsgrade netto):
for N_c in (0, 4, 24):
    # V = T_w L + (2 pi N_k - pi N_c/6) hbar c / L
    coef = 2*pi*N_k - pi*N_c/6
    if coef > 0:
        L_min = sqrt(coef*HBAR*C/(N_w*T_w))
        print(f"  N_casimir={N_c:2d}: L_min/L* = {L_min/L_STAR:.4f}")
    else:
        print(f"  N_casimir={N_c:2d}: kein Minimum (Casimir dominiert) -> Kollaps")

# ===============================================================
# C2 — Eddington-Kontrast
# ===============================================================
print("\n--- C2: Eddington-Kontrast [K] ---")
# Klassische Einstein-Loesung: Stoerung waechst ~ exp(t/tau),
# tau = 1/(c sqrt(Lambda))  (Groessenordnung; Eddington 1930)
tau = 1/(C*sqrt(LAM_ST))
print(f"Einstein-statisch: tau_instab = 1/(c sqrt(Lambda*)) "
      f"= {tau:.3e} s = {tau/GYR:.2f} Gyr = R_H/c")
print("-> Die klassische Loesung kippt auf der Hubble-Zeitskala:")
print("   kein Modell kann sich dahinter verstecken.")
print("Torus-Modell: V''(L*) > 0 -> Oszillation statt Runaway.")
print("   (Frequenz haengt an der Modulus-Traegheit M_mod: OFFEN;")
print("    entscheidend ist hier nur das Vorzeichen von V''.)")

# ===============================================================
# C3 — CMB-Topologiegrenze
# ===============================================================
print("\n--- C3: Beobachtungsgrenze (Ordnungspruefung) [S] ---")
CHI_LSS = 13.9 * GPC   # mitbewegte Distanz zur letzten Streuflaeche (LCDM)
D_LSS   = 2*CHI_LSS
print(f"L* = {L_STAR/GPC:.2f} Gpc   vs.   D_LSS = {D_LSS/GPC:.2f} Gpc")
print(f"L*/D_LSS = {L_STAR/D_LSS:.3f}")
print("Matched-Circles-Suchen (Planck) schliessen Zyklenlaengen")
print("deutlich UNTER D_LSS aus; L* liegt ~2% DARUEBER:")
print("-> knapp konsistent, hart an der Grenze — falsifizierbar.")
print("Vorbehalt: Distanzmasse sind in der statischen Lesart neu zu")
print("interpretieren; dies ist eine Ordnungspruefung, kein Endtest.")

# ===============================================================
# Zusammenfassung
# ===============================================================
print("\n=== Ergebnisse ===")
print("C1  T_w = hbar c Lambda*/(2 pi) = (pi/8)(E_e/lam_e) xi^20")
print("    -> Stabilisierung bei R_H erzwingt Spannung auf Stufe xi^20;")
print("       Impulsquant am Minimum = hbar H0 (Selbstkonsistenz).")
print("C2  Torus: V''>0 (stabil im Modell) | Einstein-statisch: tau=R_H/c.")
print("C3  L*/D_LSS = 1.01..1.02 — an der Beobachtungsgrenze, testbar.")
print("Status: alles [K|P20] x [S] (Spielzeugmodell); Vorwaertspflicht:")
print("  T_w aus T4/Z3-Windungsdynamik ableiten (dann C1 geschlossen).")
