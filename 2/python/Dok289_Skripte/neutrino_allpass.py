#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 289 -- die Neutrinos als reiner Allpass-Sektor.

FFGFT-Hypothese (Dok 007/047): die drei Neutrino-Massen sind (nahezu) gleich
-> FLACHES Betragsspektrum; die Oszillation kommt aus einer geometrischen
PHASE, nicht aus Massendifferenzen.

Nachrichtentechnisch ist das ein Allpass: |H| = 1 (flach), nichttriviale Phase.
Ein flaches Betragsspektrum traegt KEINE Oszillation -- nur die Phase tut es.

Dieses Skript macht die Testforderung konkret: welche Phasendifferenz muesste
die geometrische Phase liefern, um die GEMESSENE Standard-Oszillation
(aus Delta m^2) zu reproduzieren?

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

# 1) Entartung = flaches Betragsspektrum -> keine Oszillation aus |.|
m_nu = 0.015  # eV, ein plausibler Zielwert (kosmologische Grenze, Dok 007)
masses = np.array([m_nu, m_nu, m_nu])      # entartet
print("entartete Massen (eV):", masses)
print("Betragsspektrum (Massen) flach? max-min =", f"{masses.max()-masses.min():.2e}  -> ja, flach")
print("-> ein flaches Betragsspektrum kann keine Oszillation kodieren.")
print()

# 2) Standard-Oszillationsphase aus Delta m^2 bei Benchmark L/E
#    Delta phi_ij = 1.267 * Delta m^2[eV^2] * L[km] / E[GeV]   (Standardformel)
dm2_21, dm2_31 = 7.5e-5, 2.5e-3   # eV^2
for (L, E, tag) in [(295, 0.6, "T2K-artig (L/E~490)"),
                    (1.0, 0.004, "Reaktor-nah")]:
    p21 = 1.267 * dm2_21 * L / E
    p31 = 1.267 * dm2_31 * L / E
    print(f"{tag}: L={L} km, E={E} GeV")
    print(f"   benoetigte Phasendifferenzen: dphi21={p21:.4f} rad, dphi31={p31:.4f} rad")
print()
print("FFGFT-Testforderung: die geometrische Phase (aus T.m=1, Quantenzahlen n,l,j)")
print("MUSS exakt diese L/E-abhaengigen Phasen reproduzieren. Das ist falsifizierbar.")
print()

# 3) Allpass-Demonstration: |H|=1, Phase nichttrivial; Mischung steckt rein in der Phase
phis = np.array([0.0, 0.7, 1.9])           # drei Phasen (Platzhalter, Allpass)
H = np.exp(1j*phis)
print("Allpass H_k = exp(i phi_k):  |H_k| =", np.round(np.abs(H), 6), " (alle 1)")
print("   arg(H_k)          =", np.round(np.angle(H), 4), " (traegt die ganze Physik)")
print()
print("Befund: Neutrinos sind in dieser Lesart der reine Allpass/Phasen-Sektor --")
print("        Betrag flach, alles in der Phase. (Hypothese spekulativ, Dok 007.)")
