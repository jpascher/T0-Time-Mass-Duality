#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Die Temperaturskala des Bits.

Dieselbe charakteristische Energie E0 = sqrt(m_e*m_mu) kleidet sich mit je EINER
Buchhaltungskonstante in Masse, Zeit und Temperatur:

        m0*c^2 = E0 = kB*T0 = hbar/T~ .

  /c^2  -> Masse        m0 = E0/c^2
  /hbar -> Zeit         T~ = hbar/E0   (Zeit-Masse-Dualitaet T~*m=1)
  /kB   -> Temperatur   T0 = E0/kB

T0 ist NICHT die Temperatur, die EIN Bit "hat" (Temperatur ist eine Reservoir-/
Ensemble-Groesse), sondern die Temperatur-SKALA des Bits: die Schwelle, an der
die thermische Energie kB*T gleich der Struktur-Energie E0 wird. Darueber waescht
die Waerme die Distinktion (Windung/Mode) aus.

Brueckenschluss: die thermische Zeit bei T0, hbar/(kB*T0), IST die Dual-Zeit T~
(KMS / Connes-Rovelli: Temperatur = inverse imaginaere Zeit). Und die Landauer-
Loeschwaerme relativ zur Eigenenergie ist schlicht das Temperaturverhaeltnis:

        Q/E0 = kB*T*ln2 / (kB*T0) = (T/T0)*ln2 .

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

hbar=1.054571817e-34; c=2.99792458e8; kB=1.380649e-23; ln2=np.log(2)
eV=1.602176634e-19; MeV=1e6*eV
me,mmu=0.51099895,105.6583755
E0=np.sqrt(me*mmu)*MeV

m0=E0/c**2; Tt=hbar/E0; T0=E0/kB
print("Vier Kleidungen derselben Energie  m0*c^2 = E0 = kB*T0 = hbar/T~ :")
print(f"  E0      = {E0/MeV:.4f} MeV = {E0:.4e} J")
print(f"  m0*c^2  = {m0*c**2:.4e} J   (m0 = {m0:.4e} kg)")
print(f"  kB*T0   = {kB*T0:.4e} J   (T0 = E0/kB = {T0:.4e} K)")
print(f"  hbar/T~ = {hbar/Tt:.4e} J   (T~ = {Tt:.4e} s)")
print()
print("Brueckenschluss thermische Zeit = Dual-Zeit (KMS):")
print(f"  hbar/(kB*T0) = {hbar/(kB*T0):.4e} s ;  T~ = {Tt:.4e} s ;  Diff = {abs(hbar/(kB*T0)-Tt):.1e} s")
print()
print("Kreisschluss Landauer: Q/E0 = (T/T0)*ln2")
for T in [300.0, T0]:
    Q=kB*T*ln2
    print(f"  T={T:.3e} K: Q/E0 = {Q/E0:.4e} = (T/T0)*ln2 = {(T/T0)*ln2:.4e}"
          + ("   <- bei T0: Q/E0 = ln2 = 0.69" if abs(T-T0)<1 else ""))
print()
EQ=E0/(kB*300*ln2)
print(f"Abstand bei Raumtemperatur: E0/Q = {EQ:.3e} = 10^{np.log10(EQ):.2f}  (gut acht Groessenordnungen)")
print(f"  = (T0/T)/ln2 mit T0/300 = {T0/300:.3e}; Raumtemperatur liegt ~8,5 Dekaden unter T0.")
print()
print(f"Einordnung: T0 ~ {T0:.1e} K (MeV-Skala; QCD-Uebergang ~1.7e12 K/150 MeV; Sonnenkern ~1.5e7 K).")
