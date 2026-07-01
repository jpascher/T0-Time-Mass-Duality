#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dok 290 -- Hebel: die Phase traegt die Struktur (Oppenheim/Lim 1981).

Wenn man zwei Muster A, B Fourier-transformiert und Betrag und Phase ueber
Kreuz tauscht, traegt die Rekonstruktion die Struktur des PHASEN-Spenders,
nicht des Betrags-Spenders. D.h. das Phasenspektrum ist informationsdominant
gegenueber dem Betragsspektrum -- ein klassisches Resultat der
Signalverarbeitung.

Folge fuer die Informationsfrage: eine Masse-Energie-(Betrags-)Buchhaltung
erfasst gerade den strukturAERMEREN Kanal.

numpy-only, seed 20780458.
"""
import numpy as np
np.random.seed(20780458)

N = 64
yy, xx = np.mgrid[0:N, 0:N]
cy = cx = N/2

# zwei breitbandige, kantenreiche Muster (reicher Phaseninhalt)
r = np.sqrt((xx-cx)**2 + (yy-cy)**2)
A = (np.sin(r*1.1) > 0).astype(float)                          # konzentrische Ringe
B = ((np.sin(xx*0.9) > 0) ^ (np.sin(yy*0.9) > 0)).astype(float)  # Schachbrett-artig

def corr(u, v):
    u = (u - u.mean()).ravel(); v = (v - v.mean()).ravel()
    return float(u @ v / (np.linalg.norm(u)*np.linalg.norm(v) + 1e-12))

FA, FB = np.fft.fft2(A), np.fft.fft2(B)

# Hybrid: Betrag von B, Phase von A  -> sollte wie A aussehen
hyb_phaseA = np.real(np.fft.ifft2(np.abs(FB) * np.exp(1j*np.angle(FA))))
# Hybrid: Betrag von A, Phase von B  -> sollte wie B aussehen
hyb_phaseB = np.real(np.fft.ifft2(np.abs(FA) * np.exp(1j*np.angle(FB))))

print("Hybrid (Betrag B, Phase A):  corr mit A =", f"{corr(hyb_phaseA, A):+.3f}",
      " corr mit B =", f"{corr(hyb_phaseA, B):+.3f}")
print("Hybrid (Betrag A, Phase B):  corr mit A =", f"{corr(hyb_phaseB, A):+.3f}",
      " corr mit B =", f"{corr(hyb_phaseB, B):+.3f}")
print()

# Phase-only vs Magnitude-only Rekonstruktion von A
phase_only = np.real(np.fft.ifft2(np.exp(1j*np.angle(FA))))
mag_only   = np.real(np.fft.ifft2(np.abs(FA)))
print("Phase-only(A)  corr mit A =", f"{corr(phase_only, A):+.3f}")
print("Mag-only(A)    corr mit A =", f"{corr(mag_only, A):+.3f}")
print()
print("Befund: die Rekonstruktion folgt dem PHASEN-Spender. Das Phasenspektrum")
print("        traegt die Struktur; der Betrag allein nicht.")
