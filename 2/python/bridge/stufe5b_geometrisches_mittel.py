#!/usr/bin/env python3
"""
FFGFT — Stufe 5b: Vertiefung des geometrischen-Mittel-Befunds

In Stufe 5 hat sich gezeigt, dass das geometrische Mittel
sqrt(H_0 * f_P) sehr nahe an Moseleys nu_M = 8.23 THz liegt
(log10-Abweichung 0.11, Faktor 1.3).

Das ist physikalisch nicht zufaellig: in einer Theorie mit
zwei natuerlichen Skalen — UV-Cutoff (Planck) und IR-Cutoff
(Hubble) — ist das geometrische Mittel die natuerlichste
"mittlere" Skala.

Wir pruefen hier, ob FFGFTs ξ-Rekursion genau in diese
Mittelpunkt-Skala faellt.
"""

import numpy as np

print("=" * 70)
print("FFGFT  —  Stufe 5b: Das geometrische Mittel  sqrt(H_0 * f_P)")
print("=" * 70)

# Konstanten
hbar = 1.054571817e-34
c    = 2.99792458e8
G    = 6.67430e-11
k_B  = 1.380649e-23
eV   = 1.602176634e-19

# Planck-Skalen
t_P  = np.sqrt(hbar * G / c**5)
f_P  = 1 / t_P
l_P  = np.sqrt(hbar * G / c**3)

# Hubble (Planck-CMB)
H0_kms_Mpc = 67.4
H0 = H0_kms_Mpc * 1e3 / (3.0857e22)  # Hz
t_H = 1 / H0  # Hubble-Zeit, ~ Alter des Universums

# FFGFT
xi = 4.0 / 30000.0
T_rev = xi * t_P

# Moseley
nu_M = 8.23e12

# ----------------------------------------------------------------------
# 5b.1  Das geometrische Mittel
# ----------------------------------------------------------------------
nu_geom = np.sqrt(H0 * f_P)
t_geom  = 1 / nu_geom

print(f"\n5b.1  Skalen-Hierarchie:")
print(f"      Planck    f_P  = {f_P:.4e} Hz   (UV-Cutoff)")
print(f"      Hubble    H_0  = {H0:.4e} Hz   (IR-Cutoff)")
print(f"      Mittel    sqrt(H_0*f_P) = {nu_geom:.4e} Hz   <-- geometrisches Mittel")
print(f"      Moseley   nu_M = {nu_M:.4e} Hz")
print(f"")
print(f"      Verhaeltnis nu_M / sqrt(H_0*f_P) = {nu_M / nu_geom:.4f}")
print(f"      log10(nu_M / sqrt(H_0*f_P))      = {np.log10(nu_M / nu_geom):+.4f}")

# ----------------------------------------------------------------------
# 5b.2  Was bedeutet das geometrische Mittel?
# ----------------------------------------------------------------------
# Die Skala 1/sqrt(H_0 * f_P) ist die mittlere Zeitspanne zwischen
# einer Planck-Periode und dem Hubble-Alter:
#   t_geom = sqrt(t_P * t_H)
# Das ist die SKALA, auf der UV- und IR-Effekte sich gleichberechtigt
# begegnen — eine Art "kosmische Resonanzfrequenz".

print(f"\n5b.2  Interpretation:")
print(f"      t_geom = sqrt(t_P * t_H) = {t_geom:.4e} s")
print(f"             = {t_geom * 1e15:.2f} fs (Femtosekunden)")
print(f"      Auf dieser Skala begegnen UV (Planck) und IR (Hubble)")
print(f"      sich symmetrisch.")

# Wie viele Hubble-Zeiten ist das? Wie viele Planck-Zeiten?
print(f"")
print(f"      t_geom / t_P = sqrt(t_H / t_P) = {np.sqrt(t_H / t_P):.4e}")
print(f"      t_H / t_geom = sqrt(t_H / t_P) = {np.sqrt(t_H / t_P):.4e}")
print(f"      (Symmetrie: t_geom liegt EXAKT in der Mitte auf log-Skala)")

# ----------------------------------------------------------------------
# 5b.3  Wo faellt FFGFTs xi in diese Hierarchie?
# ----------------------------------------------------------------------
# xi = 4/30000 ist eine reine Zahl, keine Frequenz.
# Aber xi tritt in T_rev = xi * t_P auf, und in der Schicht-Hierarchie
# (1-xi)^(n/3).
# Wir muessen pruefen, ob die ξ-Rekursion eine charakteristische
# Iterations-Tiefe N hat, bei der man von t_P zu t_geom gelangt.
#
# Mit (1-xi)^(N/3) als Skalenverkleinerung pro Iteration:
#   t_iteriert = t_P * (1-xi)^(N/3)
# fuer xi << 1 ist  (1-xi)^(N/3) = exp(-N*xi/3) in fuehrender Ordnung
# Wir brauchen exp(-N*xi/3) = t_geom / t_P
#   -> N = -3/xi * log(t_geom / t_P)
N_iter = -3 / xi * np.log(t_geom / t_P)
print(f"\n5b.3  Wie viele FFGFT-Iterationen fuehren von Planck zu t_geom?")
print(f"      N = -3/xi * log(t_geom / t_P) = {N_iter:.4e}")
print(f"      Das ist eine sehr grosse Zahl — die Multiplikative")
print(f"      Hierarchie ist viel feiner als jede sinnvolle Iterationstiefe.")
print(f"")
print(f"      Erkenntnis: die geometrisch-mittlere Skala ist nicht durch")
print(f"      einfache ξ-Rekursion erreichbar. Sie ist eine SEKUNDAERE")
print(f"      Skala, die aus dem Zusammenspiel von UV und IR entsteht —")
print(f"      keine direkte FFGFT-Stufe.")

# ----------------------------------------------------------------------
# 5b.4  Aber: ist nu_M nahe an einer SI-Standard-Materie-Skala?
# ----------------------------------------------------------------------
# 8.23 THz ~ 34 meV. Pruefen wir: ist das vielleicht die thermische
# Energie irgendeiner relevanten Skala?
T_M = 2 * np.pi * hbar * nu_M / k_B   # Temperatur, K
E_M_meV = 2 * np.pi * hbar * nu_M / eV * 1000

print(f"\n5b.4  Materie-Skalen bei 8.23 THz:")
print(f"      E = h*nu_M = {E_M_meV:.2f} meV")
print(f"      T = E/k_B  = {T_M:.2f} K")
print(f"")
print(f"      Vergleich mit bekannten meV-Skalen:")
print(f"        Debye-Frequenzen typischer Festkoerper: ~10-30 THz")
print(f"        Phonon-Frequenzen, Roto-Schwingungen:    1-30 THz")
print(f"        Molekuelschwingungen IR:                 1-100 THz")
print(f"        Thermische Energie bei 300 K:             6.2 THz")
print(f"        Thermische Energie bei 400 K:             8.3 THz <-- TREFFER!")
print(f"")
print(f"      Beobachtung: 8.23 THz entspricht GENAU der thermischen")
print(f"      Schwingungs-Skala bei T ~ 395 K (was Moseleys Ableitung")
print(f"      explizit gibt).")
print(f"")
print(f"      Diagnose: Moseleys nu_M ist (kommt aus einer Phaenomenologie,")
print(f"      die mit thermischen Vakuum-Effekten verwandt ist — nicht aus")
print(f"      einer Quantengravitations- oder Kosmologie-Ableitung.")
print(f"")
print(f"      Fuer FFGFT bedeutet das:")
print(f"      Eine direkte Bruecke zu Moseley nu_M ist NICHT zwingend,")
print(f"      und auch nicht angemessen — die Frameworks beschreiben")
print(f"      verschiedene Regime des Vakuums.")

# ----------------------------------------------------------------------
# Ergebnis
# ----------------------------------------------------------------------
print(f"\n{'=' * 70}")
print(f"Stufe 5b — ERGEBNIS:")
print(f"   Der 'nahe' Treffer in Stufe 5 mit dem geometrischen Mittel")
print(f"   sqrt(H_0 * f_P) ist eine UV-IR-Resonanzfrequenz, aber sie")
print(f"   ist nicht durch FFGFTs xi-Rekursion erzeugt.")
print(f"")
print(f"   Moseleys 8.23 THz ist eine THERMISCHE Vakuum-Skala bei ~395 K,")
print(f"   nicht eine fundamentale Quantengravitations-Skala.")
print(f"")
print(f"   FAZIT der Bruecke:")
print(f"     FFGFT (Quantengravitation, Planck-Skala)")
print(f"     vs.")
print(f"     Moseley ITR (thermische Vakuum-Phaenomenologie)")
print(f"")
print(f"     Die zwei Theorien beschreiben VERSCHIEDENE REGIME.")
print(f"     Das ist kein Widerspruch, sondern Klaerung der Zustaendigkeiten.")
print(f"{'=' * 70}")
