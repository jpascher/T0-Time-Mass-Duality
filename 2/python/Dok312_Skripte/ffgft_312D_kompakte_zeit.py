#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 312 — Kapitel "Die kompakte Zeitrichtung" (Punkt D)
Verifikation der Zeitzyklus-Kette.

D1: Zeitzyklus-Laenge tau = 2 pi / H0 (isotroper T4, [K|P20])
    und Energiequant des Zyklus = hbar H0 (Isotropie-Check gegen C1).
D2: KMS/Matsubara-Temperatur der kompakten Zeit
    -> Gibbons-Hawking-Temperatur OHNE Horizont [S].
D3: Unruh-Gleichsetzung -> a = c H0 (Vereinheitlichung mit der
    a0-Kette aus Dok. 308) [S].
D4: CTC-Ordnungspruefung: Periode vs. beobachtbare Zeitspannen;
    Randbedingungs-Kopplung an die Kippgrenze aus Beiblatt 312C.

KEINE Fits. Alles folgt aus xi, lam_e und Naturkonstanten;
[K|P20] bedingt auf den Exponenten 10.
"""

from math import pi

# ---------------------------------------------------------------
# Eingaben
# ---------------------------------------------------------------
XI     = 4 / 30000
C      = 2.99792458e8            # m/s
HBAR   = 1.054571817e-34         # J s
K_B    = 1.380649e-23            # J/K  (exakt, SI)
LAM_E  = 3.8615926796e-13        # m
EV     = 1.602176634e-19         # J
GYR    = 3.155815e16             # s

N_EXP  = 10                      # [SETZUNG, P20]

H0     = (pi/2) * C * XI**N_EXP / LAM_E
R_H    = C / H0
L_STAR = 2*pi*R_H

print("=== Dok. 312 — Kompakte Zeitrichtung: Verifikation ===\n")

# ---------------------------------------------------------------
# D1 — Zeitzyklus [K|P20]
# ---------------------------------------------------------------
tau_cyc = L_STAR / C
print("--- D1: Zeitzyklus [K|P20] ---")
print(f"tau_Zyklus = L*/c = 2 pi/H0 = {tau_cyc:.4e} s = {tau_cyc/GYR:.1f} Gyr")
assert abs(tau_cyc - 2*pi/H0)/tau_cyc < 1e-14

E_time = 2*pi*HBAR/tau_cyc          # Energiequant des Zeitzyklus
E_space = 2*pi*HBAR*C/L_STAR        # Impulsquant der Raumzyklen (C1)
print(f"Energiequant Zeitzyklus  2 pi hbar/tau = {E_time:.4e} J")
print(f"Impulsquant  Raumzyklen  2 pi hbar c/L* = {E_space:.4e} J")
print(f"hbar H0                                = {HBAR*H0:.4e} J")
assert abs(E_time - HBAR*H0)/E_time < 1e-14
assert abs(E_space - HBAR*H0)/E_space < 1e-14
print(">>> Isotropie auf Quantenebene: Zeit- und Raumquant = hbar H0.")

# ---------------------------------------------------------------
# D2 — KMS/Matsubara-Temperatur [S]
# ---------------------------------------------------------------
print("\n--- D2: KMS-Temperatur der kompakten Zeit [S] ---")
# KMS: Periode der euklidischen Zeit beta*hbar  ->  T = hbar/(k_B tau)
T_kms = HBAR / (K_B * tau_cyc)
print(f"T = hbar/(k_B tau_Zyklus) = {T_kms:.4e} K")
T_GH = HBAR * H0 / (2*pi*K_B)       # Gibbons-Hawking (de Sitter)
print(f"Gibbons-Hawking T_GH = hbar H0/(2 pi k_B) = {T_GH:.4e} K")
assert abs(T_kms - T_GH)/T_GH < 1e-14
print(">>> exakt: T_KMS(tau=2 pi/H0) = T_GH — GH-Temperatur OHNE Horizont.")
print(f"    (thermische Energie k_B T = {K_B*T_GH:.3e} J "
      f"= {K_B*T_GH/EV:.2e} eV = hbar H0/(2 pi))")
print("    Vorbehalt [S]: KMS gilt fuer periodische IMAGINAERZEIT;")
print("    Identifikation mit der kompakten Realzeit = Vorwaertspflicht D(i).")

# ---------------------------------------------------------------
# D3 — Unruh-Gleichsetzung -> a0-Kette [S]
# ---------------------------------------------------------------
print("\n--- D3: Unruh-Vereinheitlichung [S] ---")
# T_U = hbar a/(2 pi c k_B)  =  T_GH  =>  a = c H0
a = 2*pi*C*K_B*T_GH/HBAR
print(f"T_U = T_GH  =>  a = {a:.4e} m/s^2")
assert abs(a - C*H0)/a < 1e-14
print(f">>> exakt: a = c H0 = {C*H0:.3e} m/s^2;  a/(2 pi) = "
      f"{C*H0/(2*pi):.3e}  vs. a0_RAR ~ 1.2e-10 (Verhaeltnis "
      f"{(C*H0/(2*pi))/1.2e-10:.2f})")
print("    Dok-308-Anker reproduziert: Kompaktheit der Zeitrichtung")
print("    als strukturelle Quelle der Unruh-Verankerung.")

# ---------------------------------------------------------------
# D4 — CTC-Ordnungspruefung und Randbedingungs-Kopplung
# ---------------------------------------------------------------
print("\n--- D4: CTC-Ordnungspruefung [S/offen] ---")
spans = [("Menschenleben", 100*3.156e7),
         ("Homo sapiens", 3e5*3.156e7),
         ("Sonnensystem", 4.6e9*3.156e7),
         ("aelteste Sterne", 1.34e10*3.156e7)]
for name, t in spans:
    print(f"  tau_Zyklus / {name:<15s} = {tau_cyc/t:.2e}")
print("-> Periode uebersteigt jede beobachtbare Zeitspanne: kein")
print("   empirischer Konflikt; die Kausalitaetsfrage ist strukturell.")
print("\nRandbedingungs-Kopplung an Beiblatt 312C (C1'):")
print("  periodische Felder (Bosonen):  Casimir-Beitrag -pi hbar c/(6L)")
print("  antiperiodische (Fermionen):   Casimir-Beitrag +pi hbar c/(12L)")
print("  Kippgrenze C1': N_casimir(netto) < 12 N_k")
# Beispielzaehlung: n_b periodische Bosonen, n_f antiperiodische Fermionen
print("  Netto-Bedingung: n_b - n_f/2 < 12 N_k  (gleiche Wahl, die")
print("  in D(ii) die Periodizitaet der Felder auf dem Zeitzyklus setzt)")
for n_b, n_f in [(4,0),(4,8),(12,0),(16,4)]:
    net = n_b - n_f/2
    ok = "stabil" if net < 12 else "KIPPT"
    print(f"    n_b={n_b:2d}, n_f={n_f:2d}: netto={net:5.1f}  -> {ok}")

# ---------------------------------------------------------------
# Zusammenfassung
# ---------------------------------------------------------------
print("\n=== Ergebnisse ===")
print(f"D1  tau_Zyklus = 2 pi/H0 = {tau_cyc/GYR:.1f} Gyr;")
print("    Zeit- und Raumquant identisch = hbar H0 (Isotropie).")
print("D2  T = hbar H0/(2 pi k_B) = Gibbons-Hawking ohne Horizont.")
print("D3  Unruh-Gleichsetzung -> a = c H0 (Dok-308-Anker vereinheitlicht).")
print("D4  Keine empirische CTC-Kollision; Kausalitaet = Periodizitaet")
print("    der Felder, gekoppelt an die 312C-Kippgrenze.")
print("Status: D1 [K|P20]; D2/D3 [S]; D4 offen (Punkt D im Register).")
