#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 289 -- der CKM/PMNS-Kontrast als Betrag-gegen-Phase.

Quarks: kleine Mischung (CKM nahe Identitaet) + starke Massenhierarchie
        -> betrags-dominiert.
Neutrinos: grosse Mischung (PMNS weit von Identitaet) + flacher Betrag
        -> phasen-dominiert.

Mass: Off-Diagonal-Gewicht der |U|^2-Matrix (0 = Identitaet/keine Mischung,
gross = starke Mischung). numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

def U_pmns(t12, t13, t23, dcp=0.0):
    s12,c12=np.sin(t12),np.cos(t12); s13,c13=np.sin(t13),np.cos(t13); s23,c23=np.sin(t23),np.cos(t23)
    e=np.exp(-1j*dcp)
    U=np.array([
        [c12*c13,                 s12*c13,                  s13*np.conj(e)],
        [-s12*c23-c12*s23*s13*e,  c12*c23-s12*s23*s13*e,    s23*c13],
        [ s12*s23-c12*c23*s13*e, -c12*s23-s12*c23*s13*e,    c23*c13],
    ])
    return U

def offdiag_weight(U):
    P=np.abs(U)**2
    return 1 - np.trace(P)/3      # 0 = Identitaet, gross = stark gemischt

d=np.pi/180
# CKM (Quark-Mischung): kleine Winkel
ckm = U_pmns(13.0*d, 0.20*d, 2.4*d)
# PMNS (Neutrino-Mischung): grosse Winkel
pmns = U_pmns(33.4*d, 8.6*d, 49.0*d)

print(f"CKM  (Quarks)    Off-Diagonal-Gewicht = {offdiag_weight(ckm):.4f}  -> kleine Mischung")
print(f"PMNS (Neutrinos) Off-Diagonal-Gewicht = {offdiag_weight(pmns):.4f}  -> grosse Mischung")
print(f"Verhaeltnis PMNS/CKM = {offdiag_weight(pmns)/offdiag_weight(ckm):.1f}x")
print()
print("Karte:")
print("  Quarks    : Betrag stark (Hierarchie), Phase/Mischung klein  -> betrags-dominiert")
print("  Leptonen  : Betrag speziell (r=sqrt2),  Phase klein (theta=2/9) -> betrags-dominiert")
print("  Neutrinos : Betrag flach (entartet),    Mischung gross        -> phasen-dominiert")
