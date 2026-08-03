#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 313 — Hawking-Strahlung auf dem Zeitzyklus
H1  Ein Prinzip, drei Gesichter: KMS-Regel T = hbar/(k_B tau)
    fuer Unruh, Gibbons-Hawking und Hawking — eine Formel.
H2  Membran-Thermometer: Periode der lokalen Zeitstruktur an der
    Membran 8 pi G M / c^3 -> T_H; Zahlenleiter.
H3  Familienleiter: T_H = T_GH  <->  r_s = R_H/2; Quermassen-Check.
H4  Was Hawking NICHT leisten kann: Verdampfungszeiten vs. tau_c;
    Grenzmasse M*, die in einem Zyklus verdampft; FFGFT-Korrektur
    (1 - xi ln(M/M_P)) aus Kap. 04 des Narrativs.
H5  Informationsseite: feinkoernige Konstanz (R3) = Membran-
    Korrelationen (Kap. 04) — dieselbe Aussage, zwei Sprachen.
"""

from math import pi, log, log10

C    = 2.99792458e8
G    = 6.67430e-11
HBAR = 1.054571817e-34
K_B  = 1.380649e-23
XI   = 4/30000
LAM_E= 3.8615926796e-13
H0   = (pi/2)*C*XI**10/LAM_E
R_H  = C/H0
TAU_C= 2*pi/H0
M_SUN= 1.98892e30
M_PL = 2.176434e-8
YR   = 3.155815e7

# ---------------------------------------------------------------
# H1 — Ein Prinzip, drei Gesichter
# ---------------------------------------------------------------
print("=== H1: KMS-Regel T = hbar/(k_B tau) — drei Gesichter ===")
def T_of_tau(tau): return HBAR/(K_B*tau)
rows = [
 ("Kosmos (kompakte Zeit)", TAU_C, "T_GH"),
 ("Schwarzes Loch M_sun",   8*pi*G*M_SUN/C**3, "T_H"),
 ("Unruh a=9.81 m/s^2",     2*pi*C/9.81, "T_U"),
]
for name, tau, lbl in rows:
    print(f"  {name:<26s} tau = {tau:9.3e} s  ->  {lbl} = "
          f"{T_of_tau(tau):9.3e} K")
# Gegenprobe Standardformeln:
T_GH = HBAR*H0/(2*pi*K_B)
T_H  = HBAR*C**3/(8*pi*G*M_SUN*K_B)
print(f"  Kontrolle: T_GH = hbar H0/(2 pi k_B) = {T_GH:.3e} K")
print(f"             T_H(M_sun) Standard      = {T_H:.3e} K")
print(">>> EINE Regel: periodische Zeitstruktur liest sich als")
print(">>> Waerme. 312 hat sie fuer den Kosmos geerdet (kompakte")
print(">>> Zeit, ohne Horizont); Hawking ist der lokale Fall.")

# ---------------------------------------------------------------
# H2 — Membran-Thermometer: Zahlenleiter
# ---------------------------------------------------------------
print("\n=== H2: Membran-Thermometer T_H(M) ===")
for name, M in [("PBH 1e12 kg", 1e12), ("Mond", 7.35e22),
                ("Erde", 5.97e24), ("Sonne", M_SUN),
                ("Sgr A* (4e6 Msun)", 4e6*M_SUN),
                ("SMBH 1e9 Msun", 1e9*M_SUN)]:
    T = HBAR*C**3/(8*pi*G*M*K_B)
    print(f"  {name:<20s} T_H = {T:9.3e} K")
print(">>> T ~ 1/M: die Landkartenstauchung (T*m=1) an der Membran")
print(">>> setzt die Periode, die Periode die Temperatur.")

# ---------------------------------------------------------------
# H3 — Familienleiter: T_H = T_GH
# ---------------------------------------------------------------
print("\n=== H3: Wo trifft die Leiter den Kosmos? ===")
M_eq = C**3/(4*G*H0)
r_s  = 2*G*M_eq/C**2
print(f"T_H = T_GH  ->  M = c^3/(4 G H0) = {M_eq:.3e} kg "
      f"= {M_eq/M_SUN:.2e} M_sun")
print(f"r_s = 2GM/c^2 = {r_s:.3e} m = R_H * {r_s/R_H:.3f}")
M_hub = C**3/(2*G*H0)   # Masse im Hubble-Volumen bei rho_c
print(f"Quermassen-Check: kritische Masse im R_H-Volumen "
      f"= c^3/(2 G H0) = {M_hub:.3e} kg -> Verhaeltnis "
      f"{M_eq/M_hub:.2f}")
print(">>> Der Horizont des 'Gleichgewichts-Lochs' liegt bei R_H/2;")
print(">>> seine Masse ist die halbe kritische Hubble-Masse. Der")
print(">>> Kosmos ist das groesste Familienmitglied der Leiter. [S]")

# ---------------------------------------------------------------
# H4 — Was Hawking NICHT leisten kann
# ---------------------------------------------------------------
print("\n=== H4: Verdampfung vs. Zeitzyklus ===")
def t_evap(M): return 5120*pi*G**2*M**3/(HBAR*C**4)
for name, M in [("PBH 1e12 kg", 1e12), ("Sonne", M_SUN),
                ("SMBH 1e9 Msun", 1e9*M_SUN)]:
    t = t_evap(M)
    print(f"  {name:<16s} t_evap = {t:9.3e} s = 10^{log10(t/YR):5.1f} yr"
          f"   t/tau_c = 10^{log10(t/TAU_C):5.1f}")
M_star = (TAU_C*HBAR*C**4/(5120*pi*G**2))**(1/3)
print(f"\nGrenzmasse (verdampft in EINEM Zyklus): "
      f"M* = {M_star:.2e} kg  (~ Asteroid)")
print(f"Sonnenmassen-Loch: {log10(t_evap(M_SUN)/TAU_C):.0f} dex "
      f"zu langsam fuer den Zyklus.")
# FFGFT-Korrektur aus Kap. 04 (Narrativ): P = P_std (1 - xi ln(M/M_P))
print("\nFFGFT-Korrektur (Kap. 04): P = P_std * (1 - xi ln(M/M_P))")
for name, M in [("PBH 1e12 kg",1e12),("Sonne",M_SUN),
                ("SMBH 1e9 Msun",1e9*M_SUN)]:
    corr = XI*log(M/M_PL)
    print(f"  {name:<16s} xi ln(M/M_P) = {corr:.4f}  "
          f"({corr*100:.2f} % Reduktion)")
print(">>> Prozent-Korrektur; am 56-dex-Befund aendert sie nichts.")
print(">>> KONSEQUENZ fuer D(ii): Nur PBH < M* schliessen via")
print(">>> Hawking; stellare und supermassive Loecher — Traeger")
print(">>> des 1e104-Entropiebudgets — muessen auf der Rueckkehr-")
print(">>> Haelfte anders zurueckgebaut werden. Hawking verschaerft")
print(">>> den grobkoernigen Kern von D(ii), er loest ihn nicht.")

# ---------------------------------------------------------------
# H5 — Informationsseite
# ---------------------------------------------------------------
print("\n=== H5: Information — zwei Sprachen, eine Aussage ===")
S_sun = 4*pi*G*M_SUN**2*K_B/(HBAR*C)
print(f"S_BH(M_sun) = 4 pi G M^2 k_B/(hbar c) = {S_sun/K_B:.2e} k_B")
print("Kap. 04 (Narrativ): Strahlung korreliert mit der fraktalen")
print("Membranstruktur — nichts geht verloren.")
print("Dok. 313 R3: feinkoernige Entropie unter unitaerer Evolution")
print("konstant — Periodizitaet mikroskopisch zulaessig.")
print(">>> Dieselbe Aussage: Informationserhalt lokal (Membran) und")
print(">>> global (Zyklus) sind konsistent; offen bleibt allein die")
print(">>> GROBkoernige Schliessung (R3).")

print("\n=== Fazit ===")
print("H1 Eine KMS-Regel, drei Temperaturen — GH aus 312 geerdet [K]")
print("H2 Membran-Thermometer: T ~ 1/M aus der Zeitlandkarte [S]")
print(f"H3 T_H=T_GH bei r_s = R_H/2; M = halbe Hubble-Masse [S]")
print(f"H4 M* = {M_star:.1e} kg; Sonnenmasse 56 dex zu langsam:")
print("   Hawking verschaerft D(ii), loest es nicht [K]")
print("H5 Informationserhalt lokal = global konsistent [S]")
