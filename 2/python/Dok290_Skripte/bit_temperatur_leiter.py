#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Die Leiter der Temperaturen: Fraktal-Boden und die drei Baeder.

Zwei Dinge werden hier festgenagelt.

(1) E0 ist eine SPROSSE, nicht der Boden. Der geometrische Boden des Rahmens ist
    die Sub-Planck-Laenge L0 = xi * ell_P (Dok 163) -- die kleinste Laenge, unter
    der die Raumzeit keine wohldefinierten Freiheitsgrade mehr traegt. Weil sie um
    den Faktor xi UNTER der Planck-Laenge liegt, steht der Boden in den "harten"
    Kleidungen (Energie/Temperatur/Frequenz/Masse) um 1/xi = 7500 UEBER Planck.
    Der Boden wird in ALLEN Kleidungen ausgedrueckt (Laenge, Dauer/Zeit, Frequenz,
    Energie, Temperatur, Masse). "Boden" = feinste Aufloesung / UV-Maximum, NICHT
    kleinste Energie.

(2) Die Landauer-Temperatur ist die des BADES, nicht die des Bits. Drei Baeder
    werden gerechnet: Raumtemperatur (realer Computer), CMB (kaeltester
    natuerlicher Boden, UIFT-Wahl), T0 (kein Bad -- Grenzfall "Bad so heiss wie das
    Bit"). Invariant ist allein das Verhaeltnis Q/E0 = (T/T0)*ln2.

Und: die Zahl der Fraktal-Zwischenschritte pro Hauptstufe, log2(1/xi) = log2(7500)
~ 12.87, IST die Informationsdecke I1 pro Freiheitsgrad aus Dok 290.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

# --- Konstanten (CODATA) ---
xi   = 4/30000
c    = 2.99792458e8
hbar = 1.054571817e-34
kB   = 1.380649e-23
qe   = 1.602176634e-19
MeV  = 1e6 * qe
# Planck-Einheiten
ellP = 1.616255e-35      # m
tP   = 5.391247e-44      # s
mP   = 2.176434e-8       # kg
EP   = mP * c**2         # J
TP   = EP / kB           # K

ln2 = np.log(2)

def line(): print("-" * 70)

# --- charakteristische Bit-Skala E0 (empirisch, fuer SI-Vergleich) ---
me, mmu = 0.51099895, 105.6583755          # MeV
E0 = np.sqrt(me*mmu) * MeV                  # J
T0 = E0 / kB
Ttilde = hbar / E0
L0_bit = hbar*c / E0

print("Teil 1 -- Der Fraktal-Boden xi*ell_P in ALLEN Kleidungen")
line()
L0   = xi*ellP
t0   = xi*tP
fmax = 1.0/t0
Emax = hbar/t0
Tmax = Emax/kB
mmax = Emax/c**2
print(f"  xi = 4/30000 = {xi:.6e},  1/xi = {1/xi:.0f} = 30000/4")
print(f"  Laenge      L0     = xi*ell_P      = {L0:.4e} m       (kleinste Laenge)")
print(f"  Dauer/Zeit  t0     = xi*t_P        = {t0:.4e} s       (kuerzeste Zeit)")
print(f"  Frequenz    f_max  = 1/t0          = {fmax:.4e} Hz      (hoechste Frequenz)")
print(f"  Energie     E_max  = hbar/t0       = {Emax:.4e} J = {Emax/MeV/1e3:.4e} GeV")
print(f"  Temperatur  T_max  = E_max/kB      = {Tmax:.4e} K       (hoechste Temperatur)")
print(f"  Masse       m_max  = E_max/c^2     = {mmax:.4e} kg")
# Kontrolle: harte Kleidungen = 1/xi * Planck
print(f"  Kontrolle:  E_max/E_Planck = {Emax/EP:.1f},  T_max/T_Planck = {Tmax/TP:.1f}  (= 1/xi)")
assert abs(Emax/EP/(1/xi) - 1) < 1e-3 and abs(Tmax/TP/(1/xi) - 1) < 1e-3

print()
print("Teil 2 -- E0 ist eine Sprosse, 25 Dekaden ueber dem Boden")
line()
print(f"  Bit-Sprosse E0 = sqrt(m_e m_mu) = {E0/MeV:.3f} MeV, T0 = {T0:.3e} K, L0 = {L0_bit*1e15:.2f} fm")
span = L0_bit / L0
print(f"  Spannweite Boden..Bit-Skala:  {span:.3e}  = {np.log10(span):.1f} Dekaden (Laenge)")
Nsub = np.log2(1/xi)
print(f"  Fraktal-Faktor pro Hauptstufe: 1/xi = {1/xi:.0f} (Dok 146)")
print(f"  sqrt2-Zwischenschritte/Stufe:  log2(1/xi) = log2(7500) = {Nsub:.4f}")
print(f"  --> = I1 (Informationsdecke pro Freiheitsgrad, Dok 290): {Nsub:.2f} Bit")

print()
print("Teil 3 -- Landauer: welche Temperatur? Die des BADES.")
line()
print("  Q = kB*T*ln2  haengt an der BAD-Temperatur T (Umgebung), nicht am Bit.")
print(f"  {'Bad':<26}{'T [K]':>12}{'Q [J]':>13}{'Q [meV]':>11}{'Q/E0':>12}{'T/T0':>12}")
for name, T in [("Raumtemperatur (Computer)", 300.0),
                ("CMB (kosm. Boden, UIFT)",   2.725),
                ("T0 (Bit-Eigenskala, kein Bad)", T0)]:
    Q = kB*T*ln2
    print(f"  {name:<26}{T:>12.3e}{Q:>13.3e}{Q/qe*1e3:>11.3g}{Q/E0:>12.3e}{T/T0:>12.3e}")
print(f"  Bei T=T0:  Q = E0*ln2 = {ln2:.4f} E0  (intrinsisch = Bit-Entropie ln2, KEINE CMB)")
print("  Invariant und aufbau-UNabhaengig ist allein das Verhaeltnis Q/E0 = (T/T0)*ln2.")

print()
print("Teil 4 -- Die Problematik: eine Leiter DEFINITER Temperaturen,")
print("          aber KEINE ist die Landauer-Temperatur.")
line()
print(f"  Sprosse T0     = {T0:.3e} K   (definit, = E0/kB)")
print(f"  Boden   T_max  = {Tmax:.3e} K   (definit, = TP/xi)")
print(f"  Leiter-Spannweite: {np.log10(Tmax/T0):.1f} Dekaden zwischen Sprosse und Boden.")
print("  Intrinsische Skala in Q=kB*T*ln2 eingesetzt -> Grenzfall oder Unsinn:")
print(f"    mit T0    -> Q = {kB*T0*ln2/E0:.3f} E0   (Referenz)")
print(f"    mit T_max -> Q = {kB*Tmax*ln2/E0:.3e} E0   (absurd gross)")
print(f"    mit T_CMB -> xi_UIFT = kB*T_CMB*ln2/(m_e c^2) = {kB*2.725*ln2/(me*MeV):.3e}  (Dok 013/243)")
print(f"  FFGFTs geometrisches xi = {xi:.3e} -- andere Groesse (Kategorienunterschied).")
print("  Real zaehlt das Bad (Computer ~300 K). Definite Energie + Skalen-Temperatur")
print("  je Sprosse; einen definiten Loeschpreis gibt es erst mit einer Umgebung.")
