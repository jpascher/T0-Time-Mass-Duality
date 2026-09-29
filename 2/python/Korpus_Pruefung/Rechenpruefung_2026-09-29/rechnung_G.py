#!/usr/bin/env python3
"""G mit SI-Umrechnung: Dok. 081 (G = xi^2 c^3/hbar), Dok. 012/127/180 (G = xi^2/(4 m_e) * C_conv * K_frak)."""
import math

xi = 4 / 30000
hbar, c, eV = 1.054571817e-34, 299792458.0, 1.602176634e-19
MeV = 1e6 * eV
G_codata = 6.67430e-11
me = 0.51099895                       # MeV
K = 1 - 100 * xi                      # 0,98667
lP = math.sqrt(hbar * G_codata / c**3)
EP = math.sqrt(hbar * c**5 / G_codata) / MeV   # MeV

print("Reine SI-Umrechnung (nur hbar, c, MeV):")
U = hbar * c**5 / MeV**2              # m^3 kg^-1 s^-2 je MeV^-2
print(f"  1 MeV^-2 (hbar=c=1) entspricht {U:.4e} m^3 kg^-1 s^-2")
print(f"  G_nat = G/U = {G_codata/U:.4e} MeV^-2 = 1/E_P^2, E_P = {EP:.5e} MeV")

print("\nDok. 081: G = xi^2 c^3/hbar")
v = xi**2 * c**3 / hbar
print(f"  xi^2 c^3/hbar = {v:.3e}  [m kg^-1 s^-2]  (G hat m^3 kg^-1 s^-2; es fehlt Länge^2)")
L = math.sqrt(G_codata * hbar / (xi**2 * c**3))
print(f"  nötige Länge L mit G = (xi L)^2 c^3/hbar: L = {L:.4e} m = l_P/xi = {lP/xi:.4e} m")
print(f"  l_P^2 c^3/hbar = {lP**2*c**3/hbar:.5e} (prüft die Dimension; l_P ist über G definiert)")
print(f"  natürlich: G = xi^2 verlangt Energieskala E mit G = xi^2/E^2: E = xi*E_P = {xi*EP/1e3:.4e} GeV")
for name, m in (("Elektron", me), ("Proton", 938.272)):
    print(f"  alpha_G({name}) = G m^2/(hbar c) = {(m/EP)**2:.3e}   gegen xi^2 = {xi**2:.3e}")
print(f"  alpha_G = xi^2 gilt für m = xi*E_P = {xi*EP/1e3:.3e} GeV")

print("\nDok. 012/127/180: G = xi^2/(4 m_e) * C_conv * K_frak")
g0 = xi**2 / (4 * me)
print(f"  xi^2/(4 m_e) = {g0:.4e} MeV^-1  (Dimension E^-1, nicht E^-2)")
print(f"  nur SI-Umrechnung, als wäre es MeV^-2: {g0*U:.3e} m^3 kg^-1 s^-2 (Faktor {g0*U/G_codata:.2e} zu groß)")
Estar = g0 / (G_codata / U)
print(f"  fehlende Energieskala E* = (xi^2/4m_e)/G_nat = {Estar:.4e} MeV = xi^2 E_P^2/(4 m_e) = {xi**2*EP**2/(4*me):.4e} MeV")
Cconv_noetig = G_codata / (g0 * K)
print(f"  C_conv, damit G stimmt: {Cconv_noetig:.4e} (Dok. 012: 7,783e-3)")
print(f"  C_conv = U * 4 m_e/(xi^2 E_P^2 K) = {U*4*me/(xi**2*EP**2*K):.4e}  -> SI-Umrechnung von G (legt die SI-Zahl fest)")
print(f"  reine Einheitenumrechnung hbar c^5/MeV^2 = {U:.3e}; Verhältnis C_conv/U = {7.783e-3/U:.3e}")
print(f"  C_conv ~ c^3/hbar (Dok. 127): c^3/hbar = {c**3/hbar:.3e}")
Gf = g0 * 7.783e-3 * K
print(f"  G = xi^2/(4 m_e) * 7,783e-3 * K_frak = {Gf:.5e}  ({(Gf/G_codata-1)*100:+.3f} %)")
Gf2 = (1.778e-8 / (4 * 0.511)) * 7.783e-3 * 0.986
print(f"  mit gerundeten Werten (1,778e-8; 0,511; 0,986): {Gf2:.5e} ({(Gf2/G_codata-1)*100:+.3f} %)")

print("\nDok. 012 Z. 408-420 Schrittkette:")
s1 = 1.778e-8 / (4 * 0.511)
s2 = s1 * 3.521e-2
s3 = s2 * 7.783e-3
s4 = s3 * 0.986e1
print(f"  {s1:.4e} -> x3,521e-2 = {s2:.4e} -> x7,783e-3 = {s3:.4e} -> x0,986e1 = {s4:.4e}  (Text: 6,674e-11; Faktor {G_codata/s4:.3f})")
print(f"  C_dim * 10 = {3.521e-2*10:.4f}  (ohne diese beiden Faktoren stimmt die Kette)")
print("Dok. 127 Z. 176-180: 3,1e-10 x 7,8e-3 x 0,986e1 =", f"{3.1e-10*7.8e-3*9.86:.3e}", "(Text 6,67e-11)")
