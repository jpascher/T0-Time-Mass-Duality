#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Das Bit in SI-Zahlen.

Verankert an der charakteristischen Energie des Rahmens, E0 = sqrt(m_e*m_mu)
(koppelt ueber alpha = xi*E0^2 an die Feinstrukturkonstante). Das generische
E0 = hbar*c/L aus Dok 290 faellt mit diesem charakteristischen E0 genau bei
L = L0 = hbar*c/E0 zusammen. Damit werden alle Bit-Groessen (Energie, Laenge,
Masse, dynamische Zeit, Rate) und die thermodynamische Loeschwaerme konkret.

Ehrlich: die zwei E0-Definitionen sqrt(m_e*m_mu) und sqrt(alpha/xi) sind NICHT
exakt gleich (~0.7% Spannung) -- beide werden ausgewiesen.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

hbar = 1.054571817e-34   # J*s
c    = 2.99792458e8      # m/s
kB   = 1.380649e-23      # J/K
ln2  = np.log(2)
MeV  = 1.602176634e-13   # J

me, mmu = 0.51099895, 105.6583755   # MeV/c^2
xi      = 4/30000.0
alpha   = 7.2973525693e-3

print(f"hbar*c = {hbar*c:.5e} J*m = {hbar*c/(MeV*1e-15):.3f} MeV*fm")
print()
E0_mass  = np.sqrt(me*mmu)
E0_alpha = np.sqrt(alpha/xi)
print("Charakteristische Energie E0 (zwei Definitionen, NICHT exakt gleich):")
print(f"  E0 = sqrt(me*mmu)   = {E0_mass:.4f} MeV")
print(f"  E0 = sqrt(alpha/xi) = {E0_alpha:.4f} MeV   (Abweichung {100*(E0_alpha-E0_mass)/E0_mass:+.2f}%)")
print()

E0  = E0_mass
E0J = E0*MeV
L0  = hbar*c/E0J
m0  = E0J/c**2
Tt  = hbar/E0J
rate = 1/Tt
print(f"DAS BIT bei E0 = {E0:.4f} MeV in SI:")
print(f"  Energie  E0 = {E0J:.4e} J     (= {E0:.3f} MeV)")
print(f"  Laenge   L0 = hbar*c/E0 = {L0:.4e} m  (= {L0/1e-15:.2f} fm)")
print(f"  Masse    m0 = E0/c^2    = {m0:.4e} kg (= {E0:.3f} MeV/c^2)")
print(f"  Zeit     T~ = hbar/E0   = {Tt:.4e} s  (= L0/c)")
print(f"  Rate   1/T~ = {rate:.4e} /s")
print(f"  Probe E0*T~ = {E0J*Tt:.4e} = hbar = {hbar:.4e}  -> T~*m = 1 OK")
print()

T = 300; Q = kB*T*ln2
print(f"THERMODYNAMISCH (Landauer, T = {T} K):")
print(f"  Entropie/Bit = kB*ln2   = {kB*ln2:.4e} J/K")
print(f"  Loeschwaerme = kB*T*ln2 = {Q:.4e} J  (= {Q/MeV*1e6:.4f} eV)")
print(f"  Q/E0 = {Q/E0J:.3e} ; E0/Q = {E0J/Q:.3e} = 10^{np.log10(E0J/Q):.2f}")
print(f"     -> gut acht Groessenordnungen (NICHT neun: 2.4e-9 hat Mantisse 2.4)")
print()
print("Befund: zwei 'Energien' eines Bits, gut acht Groessenordnungen auseinander:")
print(f"  was es IST  -> E0 = 7.35 MeV (statisch, Eigenenergie, MeV-Skala)")
print(f"  was sein LOESCHEN kostet -> kB*T*ln2 = 18 meV (thermodynamisch, an T).")
