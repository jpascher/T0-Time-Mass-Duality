#!/usr/bin/env python3
"""Rechenpruefung Gruppe A: Dok. 018 (Rev. 10/11/12), 020, 149, 155, 183."""
from math import pi, sqrt, log, log10

xi = 4/30000
f = 7500
phi = (1+sqrt(5))/2
E_P = 1.22089e19  # GeV
v = 246.22        # GeV

def h(t):
    print("\n=== " + t)

# ---------------- 018 ----------------
h("018-1 fraktale Dimensionen (Literaturwerte)")
print("Koch-Kurve log4/log3        =", log(4)/log(3))
print("Brownsche Bahn (d>=2)       = 2 ; Rand (Frontier) in 2D = 4/3 =", 4/3)
print("SAW 2D exakt 4/3 =", 4/3, "; SAW 3D Flory 5/3 =", 5/3, "(numerisch ~1,70)")
print("Mandelbrot-Rand (Shishikura) = 2")

h("018-2 a_tau-Werte und Anker")
S3 = 2*pi**2
kg = 2/sqrt(phi)*sqrt(2)
ae_T0 = S3/f/kg
dmu = 4*pi/f**(5/3); dtau = 4*pi/f**(4/3)
print("k_geom =", kg, " a_e(T0) =", ae_T0)
print("Delta mu =", dmu, " Delta tau =", dtau, " a_tau(geom) =", ae_T0+dtau)
r = f**(1/3)-1
print("f^(1/3)-1 =", r)
# Rev.10/11 gerundete Anker
ae_r, amu_r = 1.160e-3, 1.166e-3
d_r = amu_r-ae_r
print("gerundet: Delta(mu-e) =", d_r, " x18,57 =", d_r*18.57, " a_tau =", amu_r + d_r*18.57)
# praezise Anker
ae_x, amu_x = 1.15965218e-3, 1.16592059e-3
d_x = amu_x-ae_x
print("praezise: Delta(mu-e) =", d_x, " x r =", d_x*r, " a_tau =", amu_x+d_x*r)
print("Rev.11 Anker a_mu=1,1659: 1,1659e-3+1,114e-4 =", 1.1659e-3+1.114e-4)
# Rev.12 Bruecke
mt_mm = 1776.86/105.6583755
br = 144/125*mt_mm
print("m_tau/m_mu =", mt_mm, " 144/125*.. =", br, " Delta(tau-e) =", br*6.269e-6)
print("Rev.12 Z.493: 1,160e-3+1,214e-4 =", 1.160e-3+1.214e-4, "; mit a_e praezise:", ae_x+br*d_x)
print("Empfindlichkeit: Delta(mu-e) bei Rundung auf 3 Stellen +-", 1e-6, "->", 1e-6/d_x*100, "% ")

h("018-3 Massenabweichungen")
for n,t,e in [("e",0.505,0.511),("mu",105.0,105.7),("tau",1783,1777)]:
    print(n, abs(t-e)/e*100, "%")

h("018-4 5*phi")
print("5 phi =", 5*phi, " 5phi/7500 =", 5*phi/7500*100, "% ; f_ideal-5phi =", 7500-5*phi)

h("018-5 alpha als Einheit")
print("alpha = 1/137,036 =", 1/137.035999, "(dimensionslos, nicht per Einheitenwahl auf 1 setzbar)")

# ---------------- 020 ----------------
h("020-1 Lambda_T0")
print("E_P/xi =", E_P/xi, "GeV ; E_P*xi =", E_P*xi, "; 7500*1e19 =", 7500*1e19)
print("7,5e15/E_P =", 7.5e15/E_P)

h("020-2 M_Pl/M_EW")
print("1/sqrt(xi) =", 1/sqrt(xi), " ; E_P/v =", E_P/v, " ; E_P/(v/sqrt2) =", E_P/(v/sqrt(2)))
print("log_xi(E_P/v) =", log(E_P/v)/log(xi))

h("020-3 Shor")
n_int_log10 = 2048*log10(2)
print("RSA-2048: n ~ 10^%.1f, sqrt(n) ~ 10^%.1f, xi*sqrt(n) ~ 10^%.1f" % (n_int_log10, n_int_log10/2, n_int_log10/2+log10(xi)))
print("n = Bitlaenge 2048: xi*sqrt(2048) =", xi*sqrt(2048))

# ---------------- 149 ----------------
h("149-1 f = 1/(4 xi)")
print("1/(4xi) =", 1/(4*xi), " 30000/4 =", 30000/4, " 1/xi =", 1/xi)

h("149-2 Teiler von 7500")
div = [d for d in range(1,7501) if 7500 % d == 0]
print("Anzahl Teiler =", len(div), " (2+1)(1+1)(4+1) =", 3*2*5)

h("149-3 G Perspektive 2")
G = 6.67430e-11
Gp2 = xi/2*1e-6
print("xi/2*1e-6 =", Gp2, " Abw =", (Gp2-G)/G*100, "%")
tP = 5.391247e-44; hbar = 1.054571817e-34; c = 299792458
print("Persp.1: t0 =", tP/7500, " G =", tP**2*c**5/hbar)
print("Persp.3: k_G =", G*3.15576e15*pi)

h("149-4 Quarkformeln (f dimensionslos, Ergebnis wie hingeschrieben)")
pdg = dict(u=2.16, d=4.70, s=93.5, c=1273, b=4183, t=172570)
qu = {
 'u': f/(4*pi**3),
 'd': f/(2*pi**3*1.5),
 's': f/((2*pi**2)**2/(5*phi)),
 'c': f/(sqrt(2*pi**2)/phi),
 'b': f/(sqrt(2*pi**2)/phi**2),
}
for k,val in qu.items():
    print(k, "Formelwert =", val, " PDG [MeV] =", pdg[k], " Faktor PDG/Formel =", pdg[k]/val)
mt = 246.71/sqrt(2)
print("t: 246,71/sqrt2 =", mt, " mit v=246,22:", v/sqrt(2))
for ref in (172.69, 173.0, 172.57):
    print("  Abw gegen", ref, "=", (mt-ref)/ref*100, "%")
print("alpha^-1 = pi^4 sqrt2 =", pi**4*sqrt(2), " Abw", (pi**4*sqrt(2)-137.035999)/137.035999*100, "%")
print("E0 = sqrt(alpha/xi) =", sqrt((1/137.035999)/xi))

# ---------------- 155 ----------------
h("155-1 7500^60")
print("log10(7500) =", log10(7500), " 7500^60 = 10^", 60*log10(7500))
print("Ebenen fuer 61 Groessenordnungen:", 61/log10(7500), "; fuer 65 (1e-39..1e26):", 65/log10(7500))
print("Faktor je Ebene bei 60 Ebenen und 10^61:", 10**(61/60))
print("l_P/7500 =", 1.616255e-35/7500)

h("155-2 DNA-Kompression")
print("2 m / 6 um =", 2/6e-6, " ; Einzelchromosom ~5 cm / 5 um =", 0.05/5e-6)
print("Genom 6,4e9 bp * 0,34 nm =", 6.4e9*0.34e-9, "m")

h("183 xi")
print("4/30000 =", 4/30000, " = 1/", 1/(4/30000), " = 1/(3*2^2*5^4) =", 1/(3*4*625))
print("\nFertig ohne Fehler.")
