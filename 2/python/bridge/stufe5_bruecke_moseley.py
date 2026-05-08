#!/usr/bin/env python3
"""
FFGFT — Stufe 5: Bruecke zur Moseley-ITR-Frequenz nu_M

Ziel:
  George Moseleys ITR-Formulierung postuliert eine fundamentale
  "Substrat-Taktrate"
      nu_M  ~=  8.23 THz
  als die Frequenz, mit der das Vakuum-Substrat "tickt".

  FFGFT hat eine entsprechende Groesse:
      T_rev  =  xi * l_P / c     (Rekursions-Zeit der xi-Stufe)
      t_coh  =  T_rev / xi  =  l_P / c  =  t_P  (Planck-Zeit)

  Wenn beide Frameworks dieselbe Physik beschreiben, sollte
  Moseleys nu_M aus FFGFT-Groessen rekonstruierbar sein —
  und zwar nicht als willkuerliche Anpassung, sondern als
  algebraische Konsequenz.

  Dieses Skript prueft systematisch:
    (a) welche Skala in FFGFT bei ~8.23 THz liegt
    (b) ob nu_M mit einer geometrisch begruendbaren Verbindung
        zur Planck-Skala identifiziert werden kann
    (c) was passiert, wenn man die ξ-Rekursion auf der Frequenz-
        seite betrachtet
"""

import numpy as np
import sympy as sp

print("=" * 70)
print("FFGFT  —  Stufe 5: Bruecke zu Moseley nu_M = 8.23 THz")
print("=" * 70)

# ----------------------------------------------------------------------
# 5.1  Konstanten und Eingabe
# ----------------------------------------------------------------------
# CODATA 2022
hbar    = 1.054571817e-34   # J s
c       = 2.99792458e8      # m/s
G       = 6.67430e-11       # m^3 / (kg s^2)
k_B     = 1.380649e-23      # J/K
eV      = 1.602176634e-19   # J

# Planck-Groessen
m_P  = np.sqrt(hbar * c / G)              # Planck-Masse, kg
l_P  = np.sqrt(hbar * G / c**3)           # Planck-Laenge, m
t_P  = np.sqrt(hbar * G / c**5)           # Planck-Zeit, s
E_P  = m_P * c**2                         # Planck-Energie, J
T_P  = E_P / k_B                          # Planck-Temperatur, K
f_P  = 1 / t_P                            # Planck-Frequenz, Hz

# FFGFT
xi   = 4.0 / 30000.0
D_f  = 3 - xi
T_rev = xi * l_P / c                       # = xi * t_P
t_coh = T_rev / xi                         # = t_P

# Moseley
nu_M_target = 8.23e12                      # Hz, ~8.23 THz

print(f"\n5.1  Konstanten und Eingabewerte:")
print(f"     Planck-Zeit       t_P = {t_P:.6e} s")
print(f"     Planck-Frequenz   f_P = {f_P:.6e} Hz")
print(f"     FFGFT xi              = {xi:.6e}")
print(f"     FFGFT T_rev           = {T_rev:.6e} s")
print(f"     Moseley nu_M          = {nu_M_target:.6e} Hz")

# ----------------------------------------------------------------------
# 5.2  Suche das Skalenverhaeltnis
# ----------------------------------------------------------------------
ratio_M_to_P = nu_M_target / f_P
print(f"\n5.2  Verhaeltnis nu_M / f_P = {ratio_M_to_P:.6e}")
print(f"     log10(nu_M / f_P)      = {np.log10(ratio_M_to_P):+.4f}")

# Wenn nu_M = xi^n * f_P fuer ein n, dann log_xi(ratio) = n
log_xi = np.log(ratio_M_to_P) / np.log(xi)
print(f"     log_xi(nu_M / f_P)      = {log_xi:.4f}")
print(f"     (sollte ganzzahlig oder einfacher Bruch sein, falls FFGFT-Skala)")

# Naechste ganzzahlige Vielfache pruefen
for n in range(0, 10):
    cand = xi**n * f_P
    err  = abs(np.log10(cand / nu_M_target))
    print(f"       xi^{n} * f_P = {cand:.4e} Hz   "
          f"|log10-Abweichung| = {err:.4f}")

# ----------------------------------------------------------------------
# 5.3  Energie-/Frequenz-Skala  bei  m_e (Elektron)
# ----------------------------------------------------------------------
# In FFGFT geht eine fundamentale Beziehung:
#   T~ * m = 1   (mit T~ = h_bar / (m c^2)  = Compton-Periode)
# Compton-Frequenz des Elektrons:
m_e = 9.1093837015e-31   # kg
nu_C_electron = m_e * c**2 / hbar / (2 * np.pi)
nu_C_electron_alt = m_e * c**2 / (2 * np.pi * hbar)

print(f"\n5.3  Compton-Frequenzen typischer Skalen:")
print(f"     Elektron Compton  nu = m_e c^2 / (2 pi hbar) = {nu_C_electron:.4e} Hz")
print(f"     Verhaeltnis dieser zu nu_M = {nu_C_electron / nu_M_target:.4e}")

# Was hat 8.23 THz fuer eine Energie?
E_M = 2 * np.pi * hbar * nu_M_target  # = h * nu_M
E_M_eV = E_M / eV
T_M_K  = E_M / k_B
print(f"\n     Moseley-Frequenz als Energie:")
print(f"       E_M = h * nu_M       = {E_M:.4e} J")
print(f"                            = {E_M_eV:.4e} eV  =  {E_M_eV*1000:.2f} meV")
print(f"       T_M = E_M / k_B      = {T_M_K:.2f} K")
print(f"     Vergleich: Raumtemperatur ~ 300 K, kosmischer Mikrowellen-")
print(f"                hintergrund ~ 2.7 K, Helium-Verfluessigung ~ 4 K")

# ----------------------------------------------------------------------
# 5.4  Schluessel-Erkenntnis: 8.23 THz ist KEINE Planck-Skala!
# ----------------------------------------------------------------------
print(f"\n5.4  Diagnose:")
print(f"     8.23 THz entspricht 34 meV ~ 395 K — eine THERMISCHE Skala,")
print(f"     keine Quantengravitations-Skala.")
print(f"     Das ist nicht das xi*t_P-Regime der FFGFT.")
print(f"")
print(f"     Moegliche Interpretationen:")
print(f"     (1) Moseley misst eine emergente (kondensierte-Materie-aehnliche)")
print(f"         Frequenz, nicht eine fundamentale.")
print(f"     (2) nu_M koennte ein Resonanz-Modus eines makroskopischen")
print(f"         Vakuum-Effekts sein (z.B. eine kosmische Kohaerenz-Laenge).")
print(f"     (3) Die '8.23 THz' selbst koennte eine Anpassung an eine")
print(f"         beobachtete Groesse sein, deren Herkunft erst zu klaeren ist.")

# Vermutung: 8.23 THz ~ Photon-Frequenz bei einer makroskopischen Laenge L
# nu * L = c  =>  L = c / nu
L_M = c / nu_M_target
print(f"\n     Moseley-Wellenlaenge: lambda_M = c / nu_M = {L_M*1e6:.2f} um (Mikrometer)")
print(f"     Das ist die Skala mittlerer Infrarot-Strahlung.")

# ----------------------------------------------------------------------
# 5.5  Eine andere Bruecke: nu_M und der Hubble-Skala
# ----------------------------------------------------------------------
# Hubble-Frequenz:
H0_kms_Mpc = 67.4   # km/s/Mpc, Planck-CMB
H0_Hz = H0_kms_Mpc * 1e3 / (3.0857e22)   # Hz
print(f"\n5.5  Hubble-Skala:")
print(f"     H_0 = {H0_Hz:.4e} Hz   (Planck-CMB)")
print(f"     nu_M / H_0 = {nu_M_target / H0_Hz:.4e}")
print(f"     log10(nu_M / H_0) = {np.log10(nu_M_target/H0_Hz):.2f}")

# Die FFGFT-Zahl ξ liegt eher bei kleinen Vielfachen von 10^-4
# nu_M / f_P ist jedoch ~10^-31, also etwa xi^7 ... das ist eine viel
# tiefere Hierarchie als wir vorerst rechtfertigen koennen.

# ----------------------------------------------------------------------
# 5.6  Fazit dieser Stufe (Vorsicht!)
# ----------------------------------------------------------------------
print(f"\n5.6  Fazit:")
print(f"     Die Moseley-Frequenz nu_M = 8.23 THz laesst sich")
print(f"     NICHT direkt aus FFGFTs xi und Planck-Groessen rekonstruieren —")
print(f"     der Hierarchie-Sprung von ~10^31 ist zu gross fuer einfache")
print(f"     xi-Potenzen.")
print(f"")
print(f"     Das heisst NICHT, dass die beiden Frameworks unvereinbar sind.")
print(f"     Es heisst: nu_M ist (wahrscheinlich) keine fundamentale FFGFT-")
print(f"     Skala, sondern eine emergente / makroskopische Groesse, deren")
print(f"     Herleitung Moseley separat begruenden muesste.")
print(f"")
print(f"     Diese Bruecke ist also OFFEN: sie zeigt, dass die zwei")
print(f"     Frameworks bisher NICHT auf dieselbe Geometrie zeigen,")
print(f"     wenn man nu_M ernst nimmt.")

# ----------------------------------------------------------------------
# 5.7  Ehrlicher Test: koennte es zu einer SPAETEREN Bruecke kommen?
# ----------------------------------------------------------------------
# Suche, ob nu_M zufaellig mit einer Kombination aus xi und einer
# Standard-Energie-Skala uebereinstimmt.
print(f"\n5.7  Sondiere weitere Kombinationen:")

# Idee: Vielleicht ist nu_M ~ alpha * xi * f_P oder so etwas?
alpha = 1 / 137.035999
candidates = {
    "alpha * xi * f_P":       alpha * xi * f_P,
    "alpha^2 * xi * f_P":     alpha**2 * xi * f_P,
    "xi^3 * alpha * f_P":     xi**3 * alpha * f_P,
    "xi * f_P":               xi * f_P,
    "xi^2 * f_P":             xi**2 * f_P,
    "xi * H_0 ":              xi * H0_Hz,
    "1/xi * H_0":             H0_Hz / xi,
    "H_0 / xi^2":             H0_Hz / xi**2,
    "H_0 * f_P (geom mean)":  np.sqrt(H0_Hz * f_P),
    "xi * sqrt(H_0 * f_P)":   xi * np.sqrt(H0_Hz * f_P),
}
print(f"     Kandidat                    Wert (Hz)         |log10(K/nu_M)|")
print(f"     ----------------------------|-----------------|--------------")
for name, val in candidates.items():
    devlog = abs(np.log10(val / nu_M_target))
    flag = "  <<< nahe!" if devlog < 0.3 else ""
    print(f"     {name:<27} {val:.4e}    {devlog:.4f}{flag}")

print(f"\n     Wenn ein Kandidat innerhalb |log10| < 0.3 liegt, ist er")
print(f"     eine ernsthafte Vermutung wert. Sonst: keine triviale Bruecke.")

# ----------------------------------------------------------------------
# Ergebnis
# ----------------------------------------------------------------------
print(f"\n{'=' * 70}")
print(f"Stufe 5 — ERGEBNIS:")
print(f"   Moseley nu_M = 8.23 THz ist ~10^-31 mal die Planck-Frequenz —")
print(f"   eine zu grosse Hierarchie fuer einfache xi-Potenzen.")
print(f"")
print(f"   Eine direkte FFGFT-Bruecke konnte NICHT etabliert werden.")
print(f"   Das ist ein wichtiges, aber NEGATIVES Ergebnis: es zeigt,")
print(f"   dass Moseleys ITR und FFGFT nicht trivial dieselbe Skala")
print(f"   beschreiben.")
print(f"")
print(f"   Empfehlung: in der Brueckenkarte als 'offen / nicht trivial")
print(f"   verbunden' markieren. Das ist genau die Art von Befund,")
print(f"   der ein ehrlicher Test liefern soll.")
print(f"{'=' * 70}")
