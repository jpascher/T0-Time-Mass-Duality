#!/usr/bin/env python3
"""Pruefung G-Rechnungen, Gruppe 3: Dok. 189, 285, 337, 351, 354, 374, A145, A210, A266."""
from math import sqrt, pi, log

# SI / CODATA-Anker
hbar = 1.054571817e-34      # J s
c = 299792458.0             # m/s
MeV = 1.602176634e-13       # J
m_e_kg = 9.1093837015e-31
G_cod = 6.67430e-11
xi = 4 / 30000
me = 0.511                  # MeV (Referenzanker)
me_p = 0.51099895
C_conv = 7.783e-3
K986 = 0.986
K100 = 1 - 100 * xi
K7475 = 74 / 75
hc = hbar * c
mP = sqrt(hbar * c / G_cod)
EP_MeV = sqrt(hbar * c**5 / G_cod) / MeV

def pct(x, ref=G_cod):
    return (x / ref - 1) * 100

def show(tag, val, note=""):
    print(f"  {tag:<48s} {val:.6g}  {note}")

print("Referenz: G_SI = xi^2/(4 m_e) C_conv K")
Gref = xi**2 / (4 * me) * C_conv * K986
show("G_ref (m_e=0,511, K=0,986)", Gref, f"{pct(Gref):+.3f} %")

# ---------------- Dok. 189 ----------------
print("\nDok. 189")
Deff = 2.973
Kf = (Deff / 3) ** (Deff / 2)
show("Z.220 (D_eff/3)^(D_eff/2), D_eff=2,973", Kf)
show("Z.212/1499 1-100 xi", K100)
show("Z.193 12/5 xi^-1/2 (m_mu/m_e)", 12 / 5 * xi**-0.5, "(Text 207,8)")
G189 = xi**2 / (4 * me)
show("Z.990 xi^2/(4 m_e) [MeV^-1]", G189)
show("  mit C_conv*K=0,986 -> SI", G189 * C_conv * K986, f"{pct(G189*C_conv*K986):+.3f} %")
show("Z.992 l_P = sqrt(G) vs xi/(2 sqrt m_e)", sqrt(G189) - xi / (2 * sqrt(me)), "(Differenz, soll 0)")
# Z.1124: G ~ xi * l_P^2 / hbar  mit l_P^2 = hbar G / c^3  -> xi * G / c^3
lP = sqrt(hbar * G_cod / c**3)
show("Z.1124 xi*l_P^2/hbar  (SI)", xi * lP**2 / hbar, "vs G=6,674e-11")
show("Z.1124 in Planck-Einh. (l_P^2=G): Faktor zu G", xi, "")

# ---------------- Dok. 285 ----------------
print("\nDok. 285")
M = 105.6583755 / 0.58021**2
show("Z.972 M = m_mu/mu^2 [MeV]", M, "(Text 313,86)")
show("Z.907 K_frak", Kf, "(Text 0,9867)")
fac = hc / MeV**2           # m/J  = s^2/(kg m)
show("hbar c/(1 MeV)^2 [m/J]", fac, "Einheit m J^-1 = s^2 kg^-1 m^-1")
G285 = xi**2 / (4 * M) * fac * K100
show("Z.1005 G mit M=313,86", G285, f"{pct(G285):+.1f} %")
G285e = xi**2 / (4 * me) * fac * K100
show("Z.1005 G mit m_e statt M", G285e, f"{pct(G285e):+.1f} %")
show("Z.1005 mit M, aber C_conv statt hbar c/MeV^2", xi**2 / (4 * M) * C_conv * K100, "")
# Einheitencheck: [MeV^-1 dimlos gezaehlt] * m/J  != m^3 kg^-1 s^-2
print("  Einheit rechte Seite: m J^-1 = m^-1 kg^-1 s^2 (Soll: m^3 kg^-1 s^-2) -> dimensional falsch")

# ---------------- Dok. 337 ----------------
print("\nDok. 337")
Mcoll = mP / sqrt(2)
Gd = hbar * c / (2 * Mcoll**2)
show("Z.264/271 hbar c/(2 M_coll^2), M_coll=m_P/sqrt2", Gd, f"{pct(Gd):+.4f} %")
show("Z.258 M_bit/m_P = ln2/(2pi)", log(2) / (2 * pi))
show("Z.288 M_bit/m_P = k_B T_P ln2/(c^2 m_P)", log(2), "(Widerspruch zu Z.258/327, Faktor 2pi)")
G337 = xi**2 * hbar * c / (4 * m_e_kg**2) * K7475
show("Z.312 xi^2 hbar c/(4 m_e^2) K (m_e in kg)", G337, "m^3 kg^-1 s^-2 (dimensional ok)")
print(f"  Faktor gegen CODATA: {G337/G_cod:.3e}")
G337n = xi**2 / (4 * me**2)          # MeV^-2
show("  gleiche Formel natuerlich [MeV^-2]", G337n, f"Soll 1/E_P^2 = {1/EP_MeV**2:.3e}")
show("  Referenz mit K=74/75", xi**2 / (4 * me) * C_conv * K7475, f"{pct(xi**2/(4*me)*C_conv*K7475):+.3f} %")

# ---------------- Dok. 351 ----------------
print("\nDok. 351")
show("Z.120 rel. Unsicherheit 0,00015/6,67430 [ppm]", 0.00015 / 6.67430 * 1e6, "(Text 22 ppm)")

# ---------------- Dok. 354 ----------------
print("\nDok. 354")
show("Z.316/329 xi^2/(4*0,511)", xi**2 / (4 * me), "MeV^-1")
for K, n in ((K986, "0,986"), (K100, "1-100xi"), (K7475, "74/75")):
    for m, mn in ((me, "0,511"), (me_p, "0,51099895")):
        g = xi**2 / (4 * m) * C_conv * K
        show(f"  G_SI m_e={mn}, K={n}", g, f"{pct(g):+.4f} %  (Text <0,01 %)")

# ---------------- Dok. 374 ----------------
print("\nDok. 374")
g374 = xi**2 / (4 * me_p) * C_conv * K986
show("Z.217 G (m_e=0,51099895, K=0,986)", g374, f"{pct(g374):+.4f} %")
show("Z.217 Textwert 6,6745e-11 vs CODATA", 6.6745e-11, f"{pct(6.6745e-11):+.4f} % (Text +0,003 %)")
G374 = 6.6745e-11
lP374 = sqrt(hbar * G374 / c**3)
show("Z.221 l_P", lP374, "(Text 1,6163e-35)")
show("Z.222 L_0 = xi l_P", xi * lP374, "(Text 2,155e-39)")
EP374 = sqrt(hbar * c**5 / G374) / MeV
show("Z.223 E_P [MeV]", EP374, "(Text 1,22087e22)")
show("Z.223 m_e/E_P", me_p / EP374, f"(Text 4,1855e-23), vs CODATA-E_P {((me_p/EP374)/(me_p/EP_MeV)-1)*100:+.4f} %")
show("Z.224 v/E_P, v=246,22 GeV", 246.22e3 / EP374, "(Text 2,01676e-17)")
show("Z.186 E_P [GeV] (CODATA G)", EP_MeV / 1e3, "(Text 1,2209e19)")
show("Z.187 E_P/sqrt(8pi) [GeV]", EP_MeV / 1e3 / sqrt(8 * pi), "(Text 2,435e18)")
show("Z.190 1,2189e19/E_P - 1 [%]", (1.2189e22 / EP_MeV - 1) * 100, "(Text -0,16 %)")
show("Z.191 1,2189e19/E_Pbar", 1.2189e22 / (EP_MeV / sqrt(8 * pi)), "(Text 5,0)")

# ---------------- A145 ----------------
print("\nA145")
show("Z.17 xi = 2 sqrt(G m) aus G=xi^2/(4m)", 2 * sqrt(xi**2 / (4 * me) * me), f"(= xi {xi:.6g})")
Ech = 7.40 * (4 / 3) ** 2 * (pi / sqrt(2)) * 0.986
show("Z.70 E_char = 7,40*(4/3)^2*pi/sqrt2*0,986", Ech, "(Text 28,8)")
show("Z.71 Abweichung gegen 28,4 [%]", (Ech / 28.4 - 1) * 100, "(Text +1,5 %)")
print("  Z.131/145/215 nennen dagegen ~0,5 % als Rest der E_char-Naeherung -> aus Dok.-Zahlen nicht reproduzierbar")
show("Z.63 G_nat = xi^2/(4 m_e)/28,4 [MeV^-2]", xi**2 / (4 * me) / 28.4)
show("  G_nat*E_char*C_conv*K (Dok.-012-Kette)", xi**2 / (4 * me) / 28.4 * 28.4 * C_conv * K986, "= Referenz")
show("Z.135 hbar c/m_P^2", hbar * c / mP**2, "(Definition, = G)")
show("Z.162 E_T0 = 1/xi", 1 / xi, "(Text 7500)")
show("Z.216 0,5 %/0,002 %", 0.5 / 0.002, "(Text rund 200)")
show("Z.218 0,5 %/0,05 %", 0.5 / 0.05, "(Text etwa 10)")

# ---------------- A210 ----------------
print("\nA210")
lP_ = 1.616e-35
show("Z.67 L_0 = xi*1,616e-35", xi * lP_, "(Text 2,155e-39)")
show("Z.72 5,39e-39/1,616e-35 (impliz. xi)", 5.39e-39 / lP_, "(Text 3,34e-4)")
show("  Faktor zu 4/30000", 5.39e-39 / lP_ / xi, "(Text 2,5)")

# ---------------- A266 ----------------
print("\nA266")
Gnat = 1 / (EP_MeV * MeV) ** 2          # J^-2
show("G_nat = 1/E_P^2 [J^-2]", Gnat)
show("Z.151 G_nat*hbar*c^3", Gnat * hbar * c**3, "Einheit m/kg (falsch)")
show("korrekt G_nat*hbar*c^5", Gnat * hbar * c**5, f"{pct(Gnat*hbar*c**5):+.4f} %")
show("Z.39 l_P^2 c^3/hbar", lP**2 * c**3 / hbar, "(= G, stimmt)")
print("  Z.153 Einheitenkette: J s * m^3 s^-3 / J^2 = m^3 s^-2 / J = m kg^-1, nicht m^3 kg^-1 s^-2")
