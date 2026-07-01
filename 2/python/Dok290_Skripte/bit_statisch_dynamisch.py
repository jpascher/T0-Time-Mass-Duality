#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Statische und dynamische Definition des Bits.

Drei Gesichter eines Bits -- der dimensionslose Zaehlwert ist primaer, die
Konstanten hbar, c, kB kleiden ihn ein (SI-Buchhaltung):

  (1) STATISCH (kombinatorisch, dimensionslos):
        I = log2(M) Bit -- was ein Bit IST (eine Distinktion unter M).
        Geometrisch: Windung Dw=1. Energie pro Bit E0 = hbar*c/L (Betragsseite).

  (2) DYNAMISCH-KINEMATISCH (reversibel, Quanten-Speed-Limit, T~-Seite):
        Ein Flip dauert T~ = hbar/E0 = 1/m0; Rate 1/T~ = E0/hbar.
        E0*T~ = hbar  <=>  T~*m = 1 (Zeit-Masse-Dualitaet, FFGFT-Fundament).
        Margolus-Levitin: tau >= pi*hbar/(2E). Energie SETZT die Uhr -- kein
        Verlust, unitaer. Kosten = ZEIT. Die Rate ist die Kapazitaet (Bit/s, §5).

  (3) DYNAMISCH-THERMODYNAMISCH (irreversibel, Landauer):
        Ein Bit traegt Entropie kB*ln2; LOESCHEN (Vergessen) in ein Bad bei T
        dissipiert kB*T*ln2 Waerme. Haengt an T, NICHT an E0. Kosten = WAERME.
        In FFGFT emergent (Grobkoernung/Bad/Irreversibilitaet), nicht fundamental;
        das fundamentale T^4-Geschehen ist unitaer-reversibel -> (2) ist primaer.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

hbar = 1.054571817e-34
c    = 2.99792458e8
kB   = 1.380649e-23
ln2  = np.log(2)

L  = 1e-9
E0 = hbar*c/L
m0 = E0/c**2
Tt = hbar/E0
rate = 1/Tt

print("(1) STATISCH (dimensionslos):")
print(f"    I = log2(M) Bit; pro Bit E0 = hbar*c/L = {E0:.3e} J, m0 = {m0:.3e} kg")
print()
print("(2) DYNAMISCH-KINEMATISCH (reversibel, T~-Seite):")
print(f"    T~ = hbar/E0 = {Tt:.3e} s ; E0*T~ = {E0*Tt:.3e} = hbar  <=>  T~*m = 1")
print(f"    Rate 1/T~ = {rate:.3e} /s  (= Kapazitaet Bit/s, §5)")
print(f"    Margolus-Levitin: tau >= pi*hbar/(2E0) = {np.pi*hbar/(2*E0):.3e} s ; E setzt die Uhr, kein Verlust")
print()
print("(3) DYNAMISCH-THERMODYNAMISCH (irreversibel, Landauer):")
print(f"    Entropie/Bit = kB*ln2 = {kB*ln2:.3e} J/K (temperatur-unabhaengig)")
for T in [300, 4, 2.7]:
    print(f"    T={T:5.1f} K: Loeschwaerme kB*T*ln2 = {kB*T*ln2:.3e} J")
print(f"    -> Waerme wird DISSIPIERT (Loeschen=Vergessen); haengt an T, NICHT an E0.")
print()
print("BRUECKE -- der dimensionslose Bit wird gekleidet:")
print(f"    x hbar,c -> Energie E0 + Zeit T~     (kinematisch, reversibel: Zeit-Kosten)")
print(f"    x kB     -> Entropie kB*ln2 + Waerme kB*T*ln2 (thermodyn., irreversibel: Waerme-Kosten)")
print(f"    hbar, c, kB = SI-Buchhaltung; der dimensionslose Zaehlwert ist primaer.")
print()
print("Befund: statisch = WAS ein Bit ist (Struktur); dynamisch = was es TUT --")
print("        reversibel kostet es ZEIT T~ (E setzt die Uhr, T~*m=1), irreversibel")
print("        kostet das LOESCHEN WAERME kB*T*ln2 (Landauer, an T, emergent). Energie")
print("        spielt zwei Rollen: Uhr (kinematisch) vs. dissipierte Waerme (thermodyn.).")
