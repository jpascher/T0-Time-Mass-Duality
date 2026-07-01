#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Praezisierung: "Betrag legt Phase nicht fest" gilt nur bis auf einen
Allpass-Faktor.

Jede stabile Transferfunktion zerfaellt in H = H_min * H_allpass:
  - H_min  (minimalphasig): die Phase ist durch den Betrag FESTGELEGT
           (Bode-/Hilbert-/Kramers-Kronig-Relation: arg = Hilbert{log|H|}).
  - H_ap   (Allpass, |H_ap|=1): traegt nichttriviale Phase, die der Betrag
           NICHT festlegt.
Also: der Betrag legt den minimalphasigen Anteil fest; frei -- und damit das
Offene (die theta-Holonomie) -- ist der Allpass-Anteil. Das ist genau die
Lesart Minimalphase(FFGFT) x Allpass(HLV-R) aus Dok 288.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

N = 4096
w = 2*np.pi*np.arange(N)/N
z = np.exp(1j*w)

Hmin = 1 - 0.5*z**-1                       # Nullstelle bei 0.5 (innerhalb) -> minimalphasig
a = 0.7
Aap  = (z**-1 - a)/(1 - a*z**-1)           # Allpass, |Aap| = 1
H    = Hmin*Aap                            # gleicher Betrag wie Hmin, andere Phase

print("(1) Allpass erhaelt den Betrag exakt:")
print(f"    max |  |H| - |Hmin|  | = {np.max(np.abs(np.abs(H)-np.abs(Hmin))):.2e}")
print(f"    max |arg(Aap)|        = {np.max(np.abs(np.angle(Aap))):.3f} rad  (nichttrivial bei |Aap|=1)")
print()

# Minimalphasen-Phase ALLEIN aus dem Betrag rekonstruieren (Cepstrum-Methode)
logmag = np.log(np.abs(H))
cep    = np.fft.ifft(logmag).real
lwin   = np.zeros(N); lwin[0] = 1; lwin[1:N//2] = 2; lwin[N//2] = 1
phase_recon = np.fft.fft(lwin*cep).imag

uw = np.unwrap
err_min = np.max(np.abs(uw(phase_recon) - uw(np.angle(Hmin))))
resid   = uw(np.angle(H)) - uw(phase_recon)
err_ap  = np.max(np.abs(uw(resid) - uw(np.angle(Aap))))

print("(2) Aus dem Betrag rekonstruierte Phase == arg(H_min):")
print(f"    max-Fehler = {err_min:.2e}  -> der Betrag LEGT den Minimalphasen-Anteil FEST.")
print()
print("(3) Restphase arg(H) - rekonstruiert == arg(Allpass):")
print(f"    max-Fehler = {err_ap:.2e}  -> der Allpass ist der FREIE, betrags-blinde Teil.")
print()
print("Befund: der Betrag legt die Phase bis auf einen Allpass-Faktor fest. Frei")
print("        bleibt nur der Allpass -- und genau dort sitzt die theta-Holonomie")
print("        (das Offene). Die unqualifizierte Aussage 'Betrag legt Phase nicht")
print("        fest' gilt praezise nur fuer den Allpass-Anteil.")
