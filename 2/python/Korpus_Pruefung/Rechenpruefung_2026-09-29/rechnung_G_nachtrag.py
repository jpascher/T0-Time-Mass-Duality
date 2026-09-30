#!/usr/bin/env python3
"""Zweite Nachrechnung aller G-Stellen (30. Sept. 2026): Werte zu den Korrekturen in
Dok. 010, 012, 033, 037, 044, 062, 127, 143, 164, 180, 182, 189 und A145."""
import math

xi = 4 / 30000
hbar, c = 1.054571817e-34, 299792458.0
G = 6.67430e-11
me = 0.51099895                     # MeV
alpha = 1 / 137.035999
K = 1 - 100 * xi
C_conv, C_dim, E_char = 7.783e-3, 3.521e-2, 28.4
EP = math.sqrt(hbar * c**5 / G) / 1.602176634e-10   # GeV
lP = math.sqrt(hbar * G / c**3)

g0 = xi**2 / (4 * me)
print("Kernformel xi^2/(4 m_e) C_conv K_frak:")
print(f"  mit K = 0,986: {g0*C_conv*0.986:.5e}  ({(g0*C_conv*0.986/G-1)*100:+.4f} %)")
print(f"  mit K = 1-100xi: {g0*C_conv*K:.5e}  ({(g0*C_conv*K/G-1)*100:+.3f} %)")
print("Vierfaktor-Form ohne E_char (Dok. 010/012/044/127/180/182):")
print(f"  xi^2/(4m_e) C_dim C_conv K = {g0*C_dim*C_conv*0.986:.3e};  ohne K: {g0*C_dim*C_conv:.3e}")
print(f"  C_dim * E_char = {C_dim*E_char:.4f}  (hebt sich in der Schrittkette von Dok. 012 auf)")

print("Dok. 143: G = 1/(xi E_P^2) gegen 1/E_P^2 -> Faktor 1/xi =", round(1/xi))
print(f"Dok. 164: xi^2 l_P^2 c^3/hbar = {xi**2*lP**2*c**3/hbar:.3e} = xi^2 G")
print(f"Dok. 182: xi/(2 sqrt(m_e)) = {xi/(2*math.sqrt(me)):.3e} (Dimension E^-1/2), l_P = {lP:.4e} m")

print("Dok. 033:")
v = xi**2 * alpha**5.5
print(f"  xi^2 alpha^(11/2) = {v:.2e};  G in GeV^-2 = {1/EP**2:.2e};  G m_e^2 = {(me*1e-3/EP)**2:.3e}")
print(f"  alpha xi^4 = {alpha*xi**4:.2e} (Faktor vor G)")
print(f"  G m_e^2/alpha = {(me*1e-3/EP)**2/alpha:.2e};  G m_p^2/alpha = {(0.938272/EP)**2/alpha:.2e}")
print(f"  6673e-11 * C_conv * C_1 = {6673e-11*C_conv*C_dim:.3e}")
print(f"  1/alpha^2 - 1 = {137**2-1};  /2.8125 = {(137**2-1)/2.8125:.1f}")

print("Dok. 062: xi(E) = 2 E / E_P")
for name, E in (("100 GeV", 100), ("1 GeV", 1), ("2,4 eV", 2.4e-9), ("1 eV", 1e-9)):
    print(f"  {name}: {2*E/EP:.3e}")
print(f"  hc/lambda(555 nm) = {1239.84198/555:.3f} eV; hbar c/lambda = {197.3269804*2*math.pi/555/(2*math.pi):.3f} eV")
print(f"  (hbar c/lambda = {197.3269804/555:.3f} eV)")

print(f"A145: sqrt(m_e m_mu) = {math.sqrt(me*105.6583755):.3f} MeV, /sqrt(K) = {math.sqrt(me*105.6583755/K):.3f} MeV")

print("\nE_char einheitlich 28,8 (Dok. 012, Herleitung):")
Ec = 7.40 * (4/3)**2 * math.pi / math.sqrt(2) * 0.986
print(f"  E_0 (4/3)^2 pi/sqrt2 K = {Ec:.3f}")
for E in (28.4, 28.8):
    kette = g0 / E * C_conv * 0.986 * E
    print(f"  Kette Dok. 012 mit E_char = {E}: {kette:.5e}  (E_char kuerzt sich)")
P = 3.521e-2 * 2.843e-5
print(f"  Weg xi/2 (Dok. 016): Produkt der Faktoren {P:.6e}; neu 1/28.8 = {1/28.8:.6e}, Faktor 2 = {P*28.8:.5e}")
print(f"  G = xi/2 * Produkt = {xi/2*P:.6e};  2(E_char xi)^2 mit 28.8: {2*(28.8*xi)**2:.4e} ({(2*(28.8*xi)**2/(P*28.8)-1)*100:+.1f} %)")
print(f"  r_0 = 1/28.8 = {1/28.8:.6f}; Faktor*xi = {xi/28.8:.4e} = {xi/28.8/xi**2:.0f} alpha_G; G_char = 1/(2*28.8^2) = {1/(2*28.8**2):.2e}")
