#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Periodenzahl/Fensterlaenge nicht intrinsisch; und: ein Quant ist ein
ZAEHLWERT, nicht "ein Bit".

Teil 1: weder die Periodenzahl N noch die Fensterlaenge dt ist dem Photon eigen.
        N = f*dt wird vom Emissions-/Praeparationsprozess gesetzt:
          - monochromatische Mode  -> N = unendlich (ebene Welle)
          - spontane Emission      -> Atom legt f0 UND tau fest, N = f0*tau = Q/2pi
          - technisches Paket       -> Experimentator legt dt ODER N fest, Rest folgt
        Intrinsisch ist die dimensionslose Gestalt N (Df/f = 1/N), dt = N/f ist ihre
        dimensionale Einkleidung. Spannweite: ~2 (Few-Cycle) ... 5e6 (schmale Linie).

Teil 2: "1 Quant = 1 Bit" ist KEINE allgemeine Gleichung. Ein Quant ist ein
        ZAEHLWERT (eine Anregung). Sein INFORMATIONSGEHALT ist log2(M) Bit, wenn es
        aus M unterscheidbaren Moden gewaehlt ist -- variabel, pro Freiheitsgrad
        gedeckelt bei I1 = log2(1/xi). "1 Quant = 1 Bit" gilt NUR fuer M=2 (Mode auf
        ein Binaer-Alphabet fixiert) -- eine Kodierkonvention, kein Naturgesetz.
        Zaehlwert (Quantenzahl) und Bitgehalt sind verschiedene Achsen.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

c  = 2.99792458e8
xi = 4/30000.0

print("Teil 1 -- N = f*dt: weder N noch dt ist intrinsisch")
cases = [("Few-Cycle-Puls (800 nm, 5 fs)", c/800e-9, 5e-15),
         ("schmale Atomlinie (tau=10 ns, f0=5e14)", 5e14, 10e-9),
         ("monochromatische Mode", 5e14, np.inf)]
for name, f, dt in cases:
    N = f*dt
    print(f"  {name:40s} N = {N:.3g}")
print("  -> Spannweite ~1.9 ... 5e6 ... unendlich; gesetzt vom Prozess, nicht vom 'Photon-Sein'.")
print("     Intrinsisch: die dimensionslose Zahl N (Df/f = 1/N); dt = N/f ist Einkleidung.")
print()

print("Teil 2 -- ein Quant ist ein Zaehlwert, kein 'Bit'")
I1 = np.log2(1/xi)
print("  Informationsgehalt eines Quants = log2(M) Bit (M = unterscheidbare Moden):")
for M in [2, 4, 100, 1/xi]:
    tag = ""
    if M == 2:            tag = "  <- M=2: hier (und nur hier) gilt '1 Quant = 1 Bit'"
    if abs(M-1/xi) < 1:   tag = "  <- = I1 (xi-Decke pro Freiheitsgrad)"
    print(f"     M = {M:7.0f} -> {np.log2(M):6.3f} Bit{tag}")
print()
print("  Zaehlwert != Bitgehalt (verschiedene Achsen):")
print(f"     1 Quant in 2^13 Moden -> {np.log2(2**13):.0f} Bit  (1 Anregung, 13 Bit)")
print(f"     13 Quanten binaer      -> 13 Bit             (13 Anregungen, 13 Bit)")
print("     gleiche Bitzahl, verschiedene Quantenzahl -> Bit ist nicht die Quantenzahl.")
print()
print("Befund: ein Quant ist EINE Anregung (Zaehlwert 1). Sein Informationsgehalt ist")
print("        log2(M) Bit, variabel, pro Freiheitsgrad gedeckelt bei I1 = log2(1/xi)")
print(f"        = {I1:.3f} Bit. '1 Quant = 1 Bit' ist der Spezialfall M=2, kein Gesetz.")
print("        Zaehlwert (Quant) und Informationsgehalt (Bit) sind nicht dasselbe.")
