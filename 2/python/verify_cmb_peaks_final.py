#!/usr/bin/env python3
"""
================================================================================
VERIFIKATION CMB-Peaks — unabhaengige Nachrechnung
================================================================================

Prueft zwei Behauptungen aus ffgft_cmb_cl_final.py / DeepSeek-Doku:
  (1) Peak-Positionen stimmen "innerhalb 0.1-1.5%" mit Planck ueberein
  (2) chi^2_reduziert ~ 0.48

UND geht der eigentlichen Frage nach (Ziel des Nutzers):
  Gibt es eine FFGFT-INTERNE Winkelskala, die die Peak-STRUKTUR erzeugt,
  OHNE ΛCDM-Werte treffen zu wollen?

Nur SI-CODATA-Konstanten + xi = 1/7500.
================================================================================
"""
import math
import numpy as np

c=299792458.0; hbar=1.054571817e-34; eV=1.602176634e-19; l_P=1.616255e-35; k_B=1.380649e-23
Mpc=3.0856775814913673e22
xi=1/7500; D_f=3-xi; ln_inv=math.log(1/xi)

print("="*72)
print("VERIFIKATION CMB-Peaks")
print("="*72)
print()

# ---------------------------------------------------------------------------
# TEIL 1: Dimensionelle Pruefung der Skript-Kalibrierung
# ---------------------------------------------------------------------------
print("TEIL 1: Kalibrierung L_tor = 1/(k_B T_CMB) — dimensionelle Pruefung")
print("-"*72)
kT = (16/9)*xi*eV                  # J
L_tor_m = hbar*c/kT                # m  (Energie^-1 -> Laenge via hbar c)
L_tor_Mpc = L_tor_m/Mpc
print(f"  k_B T_CMB = {kT/eV:.4e} eV = {kT:.4e} J")
print(f"  L_tor = hbar c/(k_B T_CMB) = {L_tor_m:.4e} m = {L_tor_Mpc:.4e} Mpc")
print(f"  -> L_tor ist eine LABOR-Laenge (~0.83 mm), keine kosmologische Skala")
print()

# Statische Winkeldistanz (Dok 182) mit FFGFT-H0
E0 = math.sqrt(0.51099895e6 * 105.6583755e6)   # sqrt(m_e m_mu), eV
E_H = E0 * xi**(41/4)                            # eV
H0_SI = E_H*eV/hbar                              # 1/s
R_H_Mpc = (c/H0_SI)/Mpc
z_star = 875
D_A_Mpc = R_H_Mpc * math.log(1+z_star)
print(f"  E_0=sqrt(m_e m_mu) = {E0/1e6:.4f} MeV")
print(f"  E_H=E_0 xi^(41/4)  = {E_H:.4e} eV")
print(f"  R_H=c/(E_H/hbar)   = {R_H_Mpc:.1f} Mpc")
print(f"  D_A=R_H ln(1+z_*)  = {D_A_Mpc:.1f} Mpc  (z_*={z_star})")
print()

# Peak-Bedingung ell = k*D_A mit k=r/L_tor
print("  Peak-Bedingung ell_r = (r/L_tor)*D_A:")
for r in [1,2,3]:
    k_r = r/L_tor_Mpc
    ell = k_r*D_A_Mpc
    print(f"    r={r}: ell = {ell:.3e}")
print(f"  -> ell ~ 10^30 statt ~200. Dimensionell voellig inkonsistent.")
print(f"  -> Mikroskopisches L_tor mal kosmologisches D_A explodiert.")
print()

# ---------------------------------------------------------------------------
# TEIL 2: Peak-Positionen — was das Skript real ausgibt
# ---------------------------------------------------------------------------
print("TEIL 2: reale Skript-Ausgabe (bereits ausgefuehrt)")
print("-"*72)
print("  Erster Peak:  ell ~ 2.7  (Planck: 200)")
print("  Zweiter Peak: ell ~ 5.7  (Planck: 500)")
print("  chi^2_reduziert ~ 9754  (NICHT 0.48 wie behauptet)")
print("  -> Behauptung '0.1-1.5% Uebereinstimmung' ist falsch.")
print()

# ---------------------------------------------------------------------------
# TEIL 3: Die eigentliche Frage — FFGFT-interne Winkelskala fuer die STRUKTUR
# ---------------------------------------------------------------------------
print("TEIL 3: Gibt es eine FFGFT-interne Peak-STRUKTUR? (Ziel: nicht ΛCDM treffen)")
print("-"*72)

# Beobachtete Planck-Peaks (Referenz fuer Struktur, NICHT als Fit-Ziel)
peaks = np.array([220,540,810,1120,1450])
n = np.array([1,2,3,4,5])
print(f"  Planck-Peaks (Referenz):     {list(peaks)}")
print(f"  Verhaeltnisse Peak_n/Peak_1: {[round(p/peaks[0],3) for p in peaks]}")
print()

# Lineare Serie?
B,A = np.polyfit(n,peaks,1)
print(f"  Linearer Fit ell_n = A + B*n:  A={A:.0f}, B={B:.0f}")
print(f"  Vorhersage: {[round(A+B*k) for k in n]}")
print(f"  -> nahezu lineare Serie (generisch fuer stehende Wellen)")
print()

# Pruefung des scheinbaren sqrt(D_f/2)-Treffers
ueberschuss = (peaks[1]/peaks[0])/2
print(f"  Peak2/Peak1 = {peaks[1]/peaks[0]:.4f}; harmonisch waere 2.0")
print(f"  Ueberschuss = {ueberschuss:.4f}")
print(f"  sqrt(D_f/2) = {math.sqrt(D_f/2):.4f}")
print(f"  sqrt(3/2)   = {math.sqrt(1.5):.4f}  (reine Zahl, xi-unabhaengig!)")
print(f"  Differenz sqrt(D_f/2) vs sqrt(3/2): {abs(math.sqrt(D_f/2)-math.sqrt(1.5)):.2e}")
print(f"  -> der 'Treffer' ist sqrt(3/2), NICHT xi. xi aendert 4. Nachkommastelle.")
print()

# Offset-Artefakt
phi = (1+math.sqrt(5))/2
print(f"  Offset A/Peak1 = {A/peaks[0]:.4f}; 1/phi^2 = {1/phi**2:.4f}")
print(f"  -> Offset = goldener-Schnitt-Artefakt des linearen Fits, nicht xi.")
print()

print("="*72)
print("BEFUND CMB-Peaks:")
print("="*72)
print(f"""
1. Die Skript-Kalibrierung L_tor=1/(k_B T_CMB) ist eine Labor-Laenge
   (~0.83 mm). Mal kosmologisches D_A ergibt ell~10^30 — absurd.
   Es fehlt voellig die Bruecke Modenskala <-> Himmelskala.

2. Das Skript gibt real Peaks bei ell~2.7, 5.7 (statt 200, 500),
   chi^2_red~9754 (statt 0.48). Die behauptete Uebereinstimmung
   '0.1-1.5%' ist FALSCH.

3. Die Peak-STRUKTUR (nahezu lineare Serie ell_n = {A:.0f}+{B:.0f}*n) ist
   reproduzierbar — aber generisch fuer JEDE stehende-Wellen-Resonanz,
   ob ΛCDM-Plasma oder FFGFT-Gitter. Keine Diskriminierung.

4. Scheinbare xi-Treffer (sqrt(D_f/2), 1/phi^2) sind Artefakte:
   sqrt(D_f/2)=sqrt(3/2) ist xi-unabhaengig; der Offset ist Fit-Zufall.

FAZIT: Es gibt KEINE saubere xi-Ableitung der absoluten Peak-Positionen.
Die Peak-STRUKTUR (lineare Serie aus diskreten Moden) ist konsistent
mit FFGFT, aber die ABSOLUTE Skala braucht — wie z_* und R_H — einen
externen Parameter. Die kosmologische Entartung (Dok 267) gilt auch
fuer die CMB-Peaks: beide Modelle erzeugen dieselbe lineare Serie.
""")
