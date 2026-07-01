#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- ist ein Photon das kleinste Paket, und gilt die Informationsmenge
fuer alle Frequenzen?

DREI Groessen sind zu trennen (nicht zu verwechseln):
  - Informations-ZAHL pro Quant : Mode besetzt/leer = 1 Bit -> frequenz-UNABHAENGIG
  - ENERGIE pro Bit             : E = hbar*omega = hbar c / L -> frequenz-ABHAENGIG
  - KAPAZITAET (Bits pro Zeit)  : Shannon C = B log2(1+SNR)  -> frequenz-ABHAENGIG
                                  (Bandbreite B waechst mit der Traegerfrequenz)

Und: ein lokalisiertes Photon ist ein Wellenpaket; lokalisieren kostet
Bandbreite (Delta x * Delta k >= 1/2). Es bleibt EIN Quant (ein Besetzungs-Bit).

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

hbar = 1.054571817e-34   # J s
c    = 2.99792458e8      # m/s
eV   = 1.602176634e-19   # J
hbarc = hbar*c
xi   = 4/30000.0

scales = [("Radio", 1e3), ("Mikrowelle", 1e-2), ("Infrarot", 1e-5),
          ("sichtbar", 5e-7), ("Roentgen", 1e-9), ("Gamma", 1e-12)]

print("(1) E_bit = hbar c / L ueber Skalen -- Energie variiert, ZAHL bleibt 1 Bit")
print(f"{'Bereich':12s} {'L (m)':>10s} {'E_bit (eV)':>14s} {'Bits/Quant':>11s}")
for name, L in scales:
    print(f"{name:12s} {L:10.0e} {hbarc/L/eV:14.3e} {1:>11d}")
print("-> Energie spannt ~15 Groessenordnungen; die Informationszahl ist")
print("   konstant 1 Bit pro Quant, unabhaengig von der Frequenz.")
print()

print("(2) Wellenpaket: lokalisieren kostet Bandbreite (Delta x * Delta k >= 1/2)")
lam = 5e-7; k = 2*np.pi/lam
print(f"   Traegerwellenlaenge {lam*1e9:.0f} nm,  k = {k:.3e} /m")
print(f"{'Delta x':>12s} {'Delta k_min':>14s} {'Delta k / k':>12s} {'Quanten':>9s}")
for dx in [1e-3, 1e-5, 1e-6, 5e-7]:
    dk = 1/(2*dx)
    print(f"{dx:12.0e} {dk:14.3e} {dk/k:12.4f} {1:>9d}")
print("-> enger lokalisiert = breiteres Band; mehr Moden, aber EIN Quant = EIN Bit.")
print()

print("(3) KAPAZITAET C = B log2(1+SNR), B = eta * f  (feste fraktionale Bandbreite)")
eta = 0.1; SNR = 100.0           # 10% Bandbreite, 20 dB
print(f"   eta = {eta},  SNR = {SNR:.0f}  (=> log2(1+SNR) = {np.log2(1+SNR):.2f} Bit/Symbol)")
print(f"{'Bereich':12s} {'f (Hz)':>12s} {'C (bit/s)':>14s} {'Bits/Quant':>11s}")
for name, L in scales:
    f = c/L; C = eta*f*np.log2(1+SNR)
    print(f"{name:12s} {f:12.3e} {C:14.3e} {1:>11d}")
print("-> Kapazitaet ~ Frequenz (mehr Moden/s), waehrend die Zahl pro Quant 1 bleibt.")
print()
print(f"(4) FFGFT-Decke: n_max ~ 1/xi = {1/xi:.0f} (Wicklungs-Cutoff, Dok 243/009).")
print("    |W| ist dadurch endlich -> die Kapazitaet waechst mit der Frequenz, saettigt")
print("    aber an der xi-Skala. xi setzt kleinste Skala UND maximale Kapazitaet.")
print()
print(f"(5) Absolute Informationsmenge pro Freiheitsgrad: I1 = log2(1/xi)")
I1 = np.log2(1/xi)
print(f"    I1 = log2(1/xi) = log2({1/xi:.0f}) = {I1:.3f} Bit  (dimensionslos, frequenz-")
print(f"    unabhaengig, von xi gesetzt). Gesamt ~ N_max * I1 (Zellen x Tiefe, Dok 251).")
print(f"    Hinweis: der Wert {I1:.2f} ist nicht 'magisch' -- der Gehalt ist Endlichkeit")
print(f"    + xi-Verankerung; ohne die xi-Schranke divergiert I (Dok 243).")
print()
print("Befund: drei getrennte Groessen -- ZAHL (1 Bit/Quant, frequenz-unabhaengig,")
print("        relational), ENERGIE (hbar c/L) und KAPAZITAET (~f, Modenzahl); die")
print("        beiden letzten skalieren mit der Frequenz, die erste nicht.")
