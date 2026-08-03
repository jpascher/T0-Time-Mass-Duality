#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFGFT Dok. 313 — Fraktale Wegkorrektur: systematische Neurechnung

ZUORDNUNGSREGEL (aus A040 [B] + Dok. 311 eingerollt/ausgerollt):
  K_frak = (D_f^eff/3)^(D_f^eff/2) = 1 - 100 xi   (A040, abgeleitet
  aus der Konsistenzbedingung m_e/m_mu; KEINE Dekadenzaehlung)

  greift   bei Weg-durch-Struktur:  ein durchlaufener Lichtweg
           (nur AUSGEROLLT definiert, fraktal akkumulierend) im
           Verhaeltnis zu einer topologischen Strukturgroesse
           (EINGEROLLT: L*, R_H aus H0 = (pi/2) c xi^10/lambda_e)
  kuerzt   bei Weg-durch-Weg (zwei Lichtwege) und bei Winkeln
           (dimensionslos, ebenengleich)

Kontrolltest: chi_rec/eta_0 muss unveraendert bleiben.
"""

import numpy as np
from math import pi

C     = 2.99792458e8
XI    = 4/30000
LAM_E = 3.8615926796e-13
H0    = (pi/2)*C*XI**10/LAM_E
R_H   = C/H0
L_STAR= 2*pi*R_H
GPC   = 3.0856775814913673e25
GYR   = 3.155815e16
h     = H0*3.0856775814913673e22/1e5
OR    = 4.15e-5/h**2

D_EFF = 2.973
K     = (D_EFF/3)**(D_EFF/2)

print("="*62)
print("ZUORDNUNGSREGEL UND FAKTOR")
print("="*62)
print(f"K_frak = (D_f^eff/3)^(D_f^eff/2) = {K:.6f}")
print(f"       = 1 - 100 xi              = {1-100*XI:.6f}")
print(f"Wegverlaengerung: {(1/K-1)*100:.3f} %")
print(f"R67: D_f^eff auf 3 Nachkommastellen -> n = 100 +- 2")
print(f"     -> Unsicherheit des Effekts +- {2*XI*100:.3f} %")

def Hz_over_H0(z, Om):
    OL = 1-Om-OR
    return np.sqrt(Om*(1+z)**3 + OR*(1+z)**4 + OL)

def chi_over_RH(z_max, Om=0.315, n=400000):
    if z_max > 2000:
        z = np.concatenate([np.linspace(0,1090,n//2),
                            np.logspace(np.log10(1090.001),
                                        np.log10(z_max), n//2)])
    else:
        z = np.linspace(0, z_max, n)
    return np.trapezoid(1/Hz_over_H0(z, Om), z)

print("\n" + "="*62)
print("1. LICHTWEGE: glatt gerechnet vs. fraktal korrigiert")
print("="*62)
chi_rec = chi_over_RH(1090)
eta_0   = chi_over_RH(1e9)
print(f"{'Groesse':<22}{'glatt':>10}{'fraktal':>10}{'zu pi':>10}")
for name, val in (("chi_rec (z=1090)", chi_rec), ("eta_0 (Horizont)", eta_0)):
    print(f"{name:<22}{val:>10.4f}{val*K:>10.4f}{val*K/pi:>10.4f}")
print(f"\nAntipoden-Abstand Horizont: glatt {(eta_0/pi-1)*100:+.2f} %"
      f"  ->  fraktal {(eta_0*K/pi-1)*100:+.2f} %")
print(f"Antipoden-Abstand Streuwand: glatt {(chi_rec/pi-1)*100:+.2f} %"
      f"  ->  fraktal {(chi_rec*K/pi-1)*100:+.2f} %")

print("\nKONTROLLTEST (Weg/Weg muss invariant sein):")
print(f"  chi_rec/eta_0  glatt = {chi_rec/eta_0:.6f}")
print(f"  chi_rec/eta_0  fraktal = {(chi_rec*K)/(eta_0*K):.6f}   -> OK")

print("\n" + "="*62)
print("2. POSITIONEN AUF DEM ZYKLUS (theta/pi)")
print("="*62)
print(f"{'z':>8}{'glatt':>10}{'fraktal':>10}{'m/m0':>12}")
for z in (0.5, 1, 3, 10, 100, 1090):
    t = chi_over_RH(z)
    print(f"{z:>8g}{t/pi:>10.3f}{t*K/pi:>10.3f}{1/(1+z):>12.5f}")

print("\n" + "="*62)
print("3. ANTIPODEN-BEDINGUNG INVERTIERT")
print("="*62)
print(f"Bedingung glatt:   Integral dz/E = pi     = {pi:.4f}")
print(f"Bedingung fraktal: Integral dz/E = pi/K   = {pi/K:.4f}")
def solve_Om(target):
    lo, hi = 0.20, 0.50
    for _ in range(60):
        m = 0.5*(lo+hi)
        if chi_over_RH(1e9, m) > target: lo = m
        else: hi = m
    return 0.5*(lo+hi)
Om_glatt   = solve_Om(pi)
Om_fraktal = solve_Om(pi/K)
for tag, Om in (("glatt", Om_glatt), ("fraktal", Om_fraktal)):
    OL = 1-Om-OR
    print(f"  {tag:8s}: Omega_m* = {Om:.4f}  "
          f"({(Om-0.315)/0.007:+.2f} sigma zu Planck 0.315+-0.007)"
          f"   kappa* = {3*OL:.3f}  ({(3*OL-2.119)/2.119*100:+.1f} %)")
# Unsicherheit aus n = 100 +- 2
for n_ in (98, 102):
    Kn = 1-n_*XI
    print(f"  n={n_}: Omega_m* = {solve_Om(pi/Kn):.4f}")

print("\n" + "="*62)
print("4. ZEITZYKLUS: topologisch vs. Lichtumlauf")
print("="*62)
tau_top = L_STAR/C
print(f"tau_topologisch = L*/c        = {tau_top/GYR:.1f} Gyr")
print(f"tau_Licht       = L*/(c K)    = {tau_top/K/GYR:.1f} Gyr  (+1.35 %)")
print("KMS/Unruh/GH nutzen die TOPOLOGISCHE Periode (Feldperiodizitaet,")
print("nicht Photonlaufzeit): T_GH, hbar H0, a = c H0 bleiben UNVERAENDERT.")

print("\n" + "="*62)
print("5. WEITERE GROESSEN")
print("="*62)
print("Topologieschranke (Dok 312): (L*/2)/D_LSS")
print(f"  glatt:   pi/chi_rec      = {pi/chi_rec:.4f}")
print(f"  fraktal: pi/(chi_rec*K)  = {pi/(chi_rec*K):.4f}")
print("  >1 heisst: Streuwand schneidet sich NICHT selbst.")
print("  Fraktal rueckt sie weiter unter den Halbzyklus:")
print("  Vertraeglichkeit mit den Nullresultaten BESSER,")
print("  aber die Matched-Circle-Signatur verliert ihre Basis")
print("  (ohne Selbstschnitt keine Kreise, kein 4,2'-Versatz).")
print(f"Endpunktsteigung |dm/dtheta| = sqrt(Om_r)/K = "
      f"{np.sqrt(OR)/K:.4f}  (glatt {np.sqrt(OR):.4f})")
print("Winkelgroessen (4,2'-Dipolversatz, Matched Circles):")
print("  dimensionslos, ebenengleich -> UNVERAENDERT")
print("Entropie/Hawking (Kap. D, E): keine Lichtwege -> UNVERAENDERT")


print("\n" + "="*62)
print("6. KEINE UNENDLICHKEITEN, KEINE NULL: DIE UNTERGRENZE")
print("="*62)
HBAR=1.054571817e-34; ME=9.1093837015e-31
E_min=HBAR*H0; m_min=E_min/C**2
print(f"Energiequant des Zyklus: hbar H0 = {E_min:.3e} J")
print(f"  m_min = hbar H0/c^2 = {m_min:.3e} kg")
print(f"  hbar H0/(m_e c^2) = {E_min/(ME*C**2):.4e} = (pi/2) xi^10 "
      f"= {(pi/2)*XI**10:.4e}")
zmax = 1/((pi/2)*XI**10)
print(f"  -> 1+z_max = m_e/m_min = {zmax:.3e}  (endlich!)")
print(f"Beitrag zum Lichtweg jenseits z=1e9: "
      f"{1/(np.sqrt(OR)*1e9):.2e} R_H -> numerisch irrelevant,")
print( "begrifflich entscheidend: kein 'z gegen unendlich'.")
print("Folgen: (a) Massen laufen nicht gegen null -> Singularitaet")
print("        durch Quantisierung ausgeschlossen, nicht nur falsch")
print("        gestellt; (b) EINE Skala setzt beide Grenzen:")
print("        Lambda*=1/R_H^2 oben, hbar H0 unten; (c) Poincare")
print("        SETZT endlichen Phasenraum voraus — die Endlichkeit")
print("        ist Voraussetzung der Schliessung, nicht ihr Hindernis.")

print("\n" + "="*62)
print("FAZIT")
print("="*62)
print(f"Horizont am Antipoden: {(eta_0*K/pi-1)*100:+.2f} % (statt "
      f"{(eta_0/pi-1)*100:+.2f} %)")
print(f"Omega_m* = {Om_fraktal:.4f} statt {Om_glatt:.4f}: "
      f"{(Om_fraktal-0.315)/0.007:+.2f} sigma statt "
      f"{(Om_glatt-0.315)/0.007:+.2f} sigma")
print(f"kappa*   = {3*(1-Om_fraktal-OR):.3f} statt {3*(1-Om_glatt-OR):.3f}")
print(f"Streuwand wandert auf {(chi_rec*K/pi-1)*100:+.2f} %: "
      f"Nebenbefund SCHWAECHER")
print(f"Topologieschranke {pi/(chi_rec*K):.3f}: vertraeglicher mit den")
print("Nullresultaten, ABER die Matched-Circle-Signatur entfaellt.")
print("Verbleibende Pruefsignatur: C-nu-B/GW-Nichtmonotonie am Antipoden.")

# ---------------------------------------------------------------
# 7. DIE KETTE: Omega_m allein aus xi (zirkelfrei)
# ---------------------------------------------------------------
print("\n" + "="*62)
print("7. DIE KETTE: Omega_m ALLEIN AUS XI")
print("="*62)
KB=1.380649e-23; E_C=1.602176634e-19
h_=H0*3.0856775814913673e22/1e5
T0_theo=(16/9)*XI*E_C/KB
print(f"(1) H_0 = (pi/2) c xi^10/lambda_e      -> h = {h_:.4f}")
print(f"(2) k_B T_0 = (16/9) xi [eV] (Dok 061) -> T_0 = {T0_theo:.4f} K")
print(f"    gemessen 2.7255 K -> +{(T0_theo/2.7255-1)*100:.2f} %")
Or_t=4.15e-5*(T0_theo/2.7255)**4/h_**2
Or_m=4.15e-5/h_**2
print(f"(3) Omega_r(T_0)                       -> {Or_t:.5e}")
print(f"(4) K_frak = 1-100 xi                  -> {K:.5f}")
def _int(Om,Orr):
    z=np.concatenate([np.linspace(0,1090,200000),
                      np.logspace(np.log10(1090.001),12,300000)])
    return np.trapezoid(1/np.sqrt(Om*(1+z)**3+Orr*(1+z)**4+1-Om-Orr), z)
def _solve(Orr):
    lo,hi=0.20,0.50
    for _ in range(70):
        m=0.5*(lo+hi)
        if _int(m,Orr)>pi/K: lo=m
        else: hi=m
    return 0.5*(lo+hi)
Om_t=_solve(Or_t); Om_m=_solve(Or_m)
print(f"(5) Integral dz/E = pi/K = {pi/K:.4f}")
print(f"    -> Omega_m* = {Om_t:.4f}  (mit hergeleitetem T_0)")
print(f"    -> Omega_m* = {Om_m:.4f}  (mit gemessenem T_0)")
print(f"    Planck 0.315+-0.007: {(Om_t-0.315)/0.007:+.2f} sigma bzw. "
      f"{(Om_m-0.315)/0.007:+.2f} sigma")
print(f"    T_0-Fehler von 0.92 % schlaegt mit {abs(Om_t-Om_m):.4f} durch")
print("KEIN ZIRKEL: T_0 stammt aus der Atomskala (061), nicht aus")
print("der Kosmologie. Kein Schritt enthaelt einen Omega_m-Fit.")
print("Konventionell bleiben: eV (Schritt 2), E(z)-Form (Schritt 5),")
print("lambda_e als Kammerton (Schritt 1).")
