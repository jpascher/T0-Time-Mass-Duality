#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 312 — Abschnitt "Die Grenze bei c: relational, nicht innerlich"
Zahlen zu den drei harten Grenzen (Beschleunigung, Energie, Umgebung)
und zur gamma-Ko-Aenderung (kinetische Fassung von T*m = 1).

Annahmen offen deklariert:
- Organismus: Masse 70 kg, Querschnittsflaeche 0.7 m^2, ungeschirmt
- Interstellares Medium: n = 1 H-Atom/cm^3 (Groessenordnung, lokal)
- Letale Ganzkoerperdosis: ~5 Gy (Groessenordnung)
- CMB: T = 2.725 K; Blueshift frontal ~ 2*gamma (Doppler head-on)
Alles Ordnungsrechnungen [S]; die Ko-Aenderungs-Identitaeten sind [K].
"""

from math import sqrt, cosh, acosh, e, pi

C    = 2.99792458e8        # m/s
M_P  = 1.67262192e-27      # kg  (Proton)
E_P0 = M_P*C**2            # J   (938 MeV)
EV   = 1.602176634e-19
K_B  = 1.380649e-23
G0   = 9.80665             # m/s^2
YR   = 3.155815e7          # s

M_ORG = 70.0               # kg
A_ORG = 0.7                # m^2
N_ISM = 1e6                # H/m^3  (1/cm^3)
D_LET = 5.0                # Gy (J/kg), Groessenordnung letal
T_CMB = 2.725              # K

def v_of_gamma(g): return C*sqrt(1-1/g**2)

print("=== Grenze bei c: die drei harten Grenzen ===\n")

# ---------------------------------------------------------------
# Ko-Aenderung [K]: T ~ 1/gamma, E ~ gamma, Produkt invariant
# ---------------------------------------------------------------
print("--- Ko-Aenderung (kinetische Fassung von T*m=1) [K] ---")
print(f"{'gamma':>8} {'v/c':>10} {'Takt 1/g':>10} {'E/E0 = g':>10} {'Produkt':>9}")
for g in (1.005, 2, 7, 22.4, 100, 1000):
    print(f"{g:8.3f} {v_of_gamma(g)/C:10.6f} {1/g:10.4f} {g:10.3f} {1.0:9.3f}")
print("-> de Broglie 1924 (Harmonie der Phasen): innere Uhr /gamma,")
print("   Phasenfrequenz *gamma — Relation bleibt geschlossen; im")
print("   mitbewegten System aendert sich NICHTS: keine innere Grenze.")

# ---------------------------------------------------------------
# Grenze 1: Beschleunigung (1g-Reise) [K]
# ---------------------------------------------------------------
print("\n--- Grenze 1: Beschleunigung (konstant 1g, Eigenzeit) [K] ---")
tau_e = C/G0   # Eigenzeit pro Faktor e in gamma (asymptotisch)
print(f"c/g = {tau_e:.3e} s = {tau_e/YR:.2f} Jahre  (~1 Jahr pro Faktor e)")
print(f"{'gamma':>8} {'tau [Jahre]':>12}")
for g in (2, 7, 22.4, 100, 1000):
    tau = (C/G0)*acosh(g)
    print(f"{g:8.1f} {tau/YR:12.2f}")
print("-> Der ZUSTAND kostet nichts, der UEBERGANG Jahre bei 1g;")
print("   physiologisch begrenzt ist nur die Aenderungsrate.")

# ---------------------------------------------------------------
# Grenze 2: Energie [K]
# ---------------------------------------------------------------
print("\n--- Grenze 2: Energie (70 kg Organismus) [K] ---")
print(f"{'gamma':>8} {'E_kin [J]':>12} {'Vergleich':>34}")
refs = [(2, "Jahresverbrauch Kleinstadt"),
        (7, "~ Jahresstromverbrauch Deutschlands"),
        (22.4, "mehrere Weltjahres-Strommengen"),
        (100, "~ Weltjahres-PRIMAERenergie x10"),
        (1000, "Groessenordnung Supernova-Bruchteil")]
for g, note in refs:
    E = (g-1)*M_ORG*C**2
    print(f"{g:8.1f} {E:12.3e} {note:>34}")
print(f"(gamma=10: {(10-1)*M_ORG*C**2:.2e} J ~ Weltjahresenergieverbrauch)")

# ---------------------------------------------------------------
# Grenze 3: Umgebung (ISM-Strahl, ungeschirmt) [S]
# ---------------------------------------------------------------
print("\n--- Grenze 3: Umgebung — ISM als Teilchenstrahl [S] ---")
print("Reisendensystem: Dichte gamma*n, Fluss ~ gamma*n*v,")
print("Protonenergie (gamma-1)*m_p*c^2; Dosisleistung = Fluss*E*A/M.")
print(f"{'gamma':>8} {'E_p [GeV]':>10} {'Fluss [1/cm^2 s]':>17} "
      f"{'Dosis [Gy/s]':>13} {'t_letal':>12}")
for g in (2, 7, 22.4, 100, 1000):
    v = v_of_gamma(g)
    flux = g*N_ISM*v                    # 1/m^2/s
    Ep   = (g-1)*E_P0                   # J
    dose = flux*Ep*A_ORG/M_ORG          # Gy/s (voll absorbiert)
    t_let = D_LET/dose
    unit = "s"
    t = t_let
    if t < 1e-3: t, unit = t*1e6, "us"
    elif t < 1: t, unit = t*1e3, "ms"
    print(f"{g:8.1f} {Ep/EV/1e9:10.2f} {flux/1e4:17.2e} "
          f"{dose:13.2e} {t:9.2f} {unit:>2}")
print("-> Schon bei v=0.99c (gamma~7) letale Dosis in unter einer")
print("   Millisekunde, ungeschirmt. DIES ist die Naturgrenze —")
print("   nicht der Organismus, sondern seine Beziehung zum Medium.")

# ---------------------------------------------------------------
# Unbelebte Struktur: Elektronik bei 0.2c (Starshot-Regime) [S]
# ---------------------------------------------------------------
print("\n--- Elektronik ist nicht immun: 0.2c (Starshot-Regime) [S] ---")
v02 = 0.2*C
g02 = 1/sqrt(1-0.2**2)
Ep02 = (g02-1)*E_P0
flux02 = g02*N_ISM*v02
print(f"gamma(0.2c) = {g02:.4f};  E_Proton = {Ep02/EV/1e6:.1f} MeV")
print("  -> Bereich maximaler Verlagerungsschaeden in Halbleitern")
print(f"Protonenfluss = {flux02/1e4:.2e} /cm^2 s")
# Dosisleistung in Silizium-Elektronik (voll absorbiert, pro kg):
dose02 = flux02*Ep02  # J/m^2/s; pro kg haengt an Geometrie -> Fluenz angeben
fluence_20yr = flux02*20*YR
print(f"Fluenz ueber 20 Jahre Flug: {fluence_20yr/1e4:.2e} p/cm^2")
print("  (Vergleich: Schadensschwellen Halbleiter ~1e10..1e14 p/cm^2 —")
print("   um Groessenordnungen ueberschritten -> Opferschicht/Haertung")
print("   zwingend; Starshot: Kante voraus, mm-Abtragsschicht)")
E_dust = 0.5*1e-12*v02**2
print(f"Staubkorn 1 ng bei 0.2c: E_kin = {E_dust:.0f} J (~ Gewehrkugel)")
print("Dosistoleranz: Mensch ~5 Gy | Elektronik ~1e2..1e5 Gy (Haertung)")
print("-> Grenze trifft JEDE strukturtragende Materie; immun ist nur")
print("   das masselose, strukturlose Photon (dtau=0).")

# CMB als Roentgenquelle bei sehr grossem gamma
print("\nCMB-Blueshift (frontal ~2*gamma):")
E_cmb0 = 2.701*K_B*T_CMB   # mittlere Photonenergie ~2.7 k_B T
for target, name in [(1e3, "1 keV (Roentgen)"), (1e6, "1 MeV (Gamma)")]:
    g_need = target*EV/(2*E_cmb0)
    print(f"  mittleres CMB-Photon -> {name}: gamma ~ {g_need:.1e}")

# ---------------------------------------------------------------
# Asymptote
# ---------------------------------------------------------------
print("\n=== Asymptote ===")
print("Photon: m=0, dtau=0 — Grenzfall, den Materie nie erreicht.")
print("T->0 hiesse m->infty: c ist keine erreichbare Geschwindigkeit,")
print("sondern die Asymptote der Relation T*m=1 selbst.")
