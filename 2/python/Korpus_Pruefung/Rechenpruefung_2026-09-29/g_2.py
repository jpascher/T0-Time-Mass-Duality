#!/usr/bin/env python3
"""Pruefung G-Rechnungen, Gruppe 2: Dok. 054, 063, 066, 068, 086, 091, 116, 122, 137.
Zahlen jeweils aus dem Dokument selbst; nur G bzw. Rechnungen, in die G eingeht."""
from math import sqrt, pi

G_CODATA = 6.67430e-11
hbar, c, kB, eps0 = 1.054571817e-34, 2.99792458e8, 1.380649e-23, 8.8541878128e-12

def rel(a, b):
    return (a / b - 1) * 100

print("=== Dok. 054 (G nur Eingabe, 6,67e-11 'zugewiesen', Z. 15) ===")
G = 6.674e-11
tP = sqrt(hbar * G / c**5); lP = sqrt(hbar * G / c**3); mP = sqrt(hbar * c / G)
TP = sqrt(hbar * c**5 / (G * kB**2)); IP = sqrt(4 * pi * eps0 * c**6 / G)
IPstd = sqrt(eps0 * c**6 / G)
for name, v, doc in [("t_P Z.129", tP, 5.392e-44), ("l_P Z.130", lP, 1.617e-35),
                     ("m_P Z.131", mP, 2.177e-8), ("T_P Z.132", TP, 1.417e32),
                     ("I_P Z.105/133", IP, 3.479e25), ("I_P(Std) Z.104", IPstd, 9.81e24)]:
    print(f"  {name}: gerechnet {v:.4e}, Dok {doc:.4e}, Abw {rel(doc, v):+.3f} %")
print(f"  I_P(Std)/I_P = {IPstd/IP:.4f} (Dok: 28,2 %)")
# Z.102/103: E_P = c^4/(4 pi eps0 G), B_P = c^3/(4 pi eps0 G)
EP_doc = c**4 / (4 * pi * eps0 * G); BP_doc = c**3 / (4 * pi * eps0 * G)
EP_std = (c**4 / G) / sqrt(4 * pi * eps0 * hbar * c); BP_std = EP_std / c
print(f"  E_P nach Dok-Formel: {EP_doc:.3e} (Einheit N^2 m^2/C^2, nicht V/m); Dok-Zahl 1,04e61")
print(f"  E_P Standard c^4/(G sqrt(4 pi eps0 hbar c)) = {EP_std:.3e} V/m")
print(f"  B_P nach Dok-Formel: {BP_doc:.3e}; Standard E_P/c = {BP_std:.3e} T; Dok-Zahl 3,48e52")

print("\n=== Dok. 066, Tab. Z. 92-104: xi_SI = 2 G m / l_P (G=6.674e-11, l_P=1.616e-35) ===")
lP = 1.616e-35
rows = [("Elektron", 9.109e-31, 7.52e-7), ("Proton", 1.673e-27, 1.38e-3),
        ("Mensch", 70.0, 6.4e6), ("Erde", 5.972e24, 4.1e28),
        ("Sonne", 1.989e30, 1.8e38), ("Planck-Masse", 2.176e-8, 2.0)]
for n, m, doc in rows:
    a = 2 * G * m / lP              # Formel wie geschrieben (Einheit m^2/s^2)
    b = 2 * G * m / (c**2 * lP)     # dimensionslos (r_s / l_P)
    print(f"  {n:13s} Dok {doc:.2e} | 2Gm/l_P = {a:.3e} | 2Gm/(c^2 l_P) = {b:.3e}")
print("  Dimension 2Gm/l_P: m^3 kg^-1 s^-2 * kg / m = m^2 s^-2 -> nicht dimensionslos ohne c^2")

print("\n=== Dok. 086, Z. 96-110: G_SI = xi^2/(4 m_e) * C_conv * K_frak ===")
xi, me, Cconv, K = 4 / 3 * 1e-4, 0.511, 7.783e-3, 0.986
G086 = xi**2 / (4 * me) * Cconv * K
print(f"  xi^2 = {xi**2:.6e}; /(4 m_e) = {xi**2/(4*me):.6e} MeV^-1")
print(f"  * C_conv = {xi**2/(4*me)*Cconv:.6e}; * K_frak = {G086:.6e}")
print(f"  Dok: 6.67429e-11, 'Abweichung < 0.0002 %'; gerechnet {G086:.5e}, "
      f"Abw. zu CODATA {rel(G086, G_CODATA):+.4f} %")
print(f"  C_1 = 3.521e-2 -> 1/C_1 = {1/3.521e-2:.2f} (= E_char 28,4; kommt in der Boxformel nicht vor)")
print(f"  Doc-Wert 6.67429 vs CODATA 6.67430: {rel(6.67429e-11, G_CODATA):+.5f} %")

print("\n=== Dok. 116, Z. 259-262 und Z. 327 ===")
m = xi / 2
Gnat = xi**2 / (4 * m)
print(f"  xi^2/(4 * xi/2) = {Gnat:.6e}; xi = {xi:.6e}; Verhaeltnis = {Gnat/xi:.3f} (also xi/2, nicht xi)")
for lab, g in [("G_nat = xi (Dok)", xi), ("G_nat = xi/2 (korrekt ausgerechnet)", Gnat)]:
    print(f"  {lab} * 2.843e-5 = {g*2.843e-5:.4e} (Ziel 6.674e-11, Faktor {g*2.843e-5/6.674e-11:.0f})")
print(f"  benoetigter Faktor fuer G_nat = xi: {6.674e-11/xi:.4e}; fuer xi/2: {6.674e-11/(xi/2):.4e}")
print(f"  Z. 326 (nicht G): alpha = xi*E0^2 = {xi*7.398**2:.6e} -> 1/alpha = {1/(xi*7.398**2):.3f}")

print("\n=== Dok. 091, Z. 19: L_P = sqrt(hbar G/c^3) mit G=6.674e-11 (Tab. Z. 453) ===")
print(f"  L_P = {sqrt(hbar*6.674e-11/c**3):.4e} m (Dok 1.616e-35)")
print(f"  Z. 141: L_0 = xi L_P = {xi*1.616e-35:.4e} m (Dok 2.155e-39)")

print("\n=== Dok. 122 (keine G-Zahl; Nebenrechnung alpha Z. 103-104) ===")
print(f"  138.9 * 0.9862 = {138.9*0.9862:.3f} (Dok: 137.036)")
print(f"  benoetigt: 137.036/0.9862 = {137.036/0.9862:.2f}")

print("\n=== Dok. 063 Z. 261, 137 Z. 219: G = 6.67430e-11 ohne Rechnung; 068/066: G=1 bzw. zitiert ===")
