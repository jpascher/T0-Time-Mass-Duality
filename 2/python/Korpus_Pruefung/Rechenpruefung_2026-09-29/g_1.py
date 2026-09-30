#!/usr/bin/env python3
"""Nachrechnung aller G-Rechnungen, Gruppe 1: Dok. 004, 010, 013, 016, 028, 030, 041, 044, 053.
Zahlen jeweils aus dem Dokument selbst."""
from math import sqrt

G_CODATA = 6.67430e-11
hbar = 1.054571817e-34; c = 299792458.0
MeV_J = 1.602176634e-13
hbarc_MeV_m = 1.97326980e-13  # MeV*m

def rel(a, b): return (a - b) / b * 100

def show(dok, zeile, text, wert, soll=None):
    s = f"Dok {dok} Z.{zeile}: {text} = {wert:.6g}"
    if soll is not None:
        s += f"   (Dokument: {soll:.6g}, Abw. {rel(wert, soll):+.4f} %)"
    print(s)

xi = 4/30000
print("=== Referenz ===")
Gref = xi**2/(4*0.511)*7.783e-3*0.986
show("Ref", "-", "xi^2/(4 m_e)*C_conv*K_frak", Gref)
print(f"   vs CODATA {rel(Gref, G_CODATA):+.4f} %")

print("\n=== Dok 004 === Z.202 nur zitiert (6.67430e-11)")

print("\n=== Dok 010 ===")
print("Z.56/325/342/516: G = xi^2/(4 m_e)*C_dim*C_conv, ohne Zahlenwert")
EeJ = 0.511*1.6e-13
show("010", 621, "E_e = 0.511*1.6e-13 J", EeJ, 8.2e-14)
m_e_kg = EeJ/(3e8)**2
r0_SI_c4 = 2*6.674e-11*EeJ/(3e8)**4          # 2GE/c^4
r0_Planck = 2*(0.511/1.22089e22)*1.616255e-35  # 2 (E/E_P) l_P
show("010", 629, "r0 = 2GE/c^4 mit Dok-Zahlen [m]", r0_SI_c4, 1e-28)
show("010", 629, "r0 = 2 (E/E_P) l_P [m]", r0_Planck, 1e-28)
show("010", 634, "r0/l_P = 1e-28/1.6e-35", 1e-28/1.6e-35, 1e7)

print("\n=== Dok 013 ===")
xi0 = 1.333e-4
G13a = xi0**2/(4*0.511)*7.783e-3*0.986
G13b = xi**2/(4*0.511)*7.783e-3*0.986
show("013", "113-127", "G_SI mit xi0=1.333e-4", G13a, 6.674e-11)
show("013", "113-127", "G_SI mit xi=4/30000", G13b, 6.674e-11)
print(f"   Abw. zu CODATA-2018: {rel(G13a,G_CODATA):+.4f} % bzw. {rel(G13b,G_CODATA):+.4f} %  (Dokument: <0.0002 %)")
lPnat = 1.333e-4/(2*sqrt(0.511))
show("013", "172/296", "l_P^nat = xi/(2 sqrt(m_e))", lPnat, 9.33e-5)
show("013", "297-299", "l_P^SI = 9.33e-5 * 1.973e-13 m", 9.33e-5*1.973e-13, 1.616e-35)
print("   Dimension: G = xi^2/(4 m_e) hat [E^-1] (Dok. Z.101 selbst) -> sqrt(G) hat [E^-1/2], keine Länge")
show("013", 218, "l_P = sqrt(hbar G/c^3) mit G_gemessen", sqrt(hbar*6.674e-11/c**3), 1.616e-35)
E0 = sqrt(0.511*105.658)
show("013", 192, "hbar c/E0 (r0 = 1/E) [m]", hbarc_MeV_m/E0, 2.7e-14)
show("013", 192, "2 G E0/c^4 mit G_SI [m]", 2*6.674e-11*E0*MeV_J/c**4, 2.7e-14)
show("013", 198, "L0 = xi*l_P", xi*1.616e-35, 2.155e-39)

print("\n=== Dok 016 ===")
show("016", 162, "Schritt 1: xi/2", 1.333333e-4/2, 6.666667e-5)
Gnat = 6.666667e-5*3.521e-2
show("016", 163, "Schritt 3: G_T0*3.521e-2", Gnat, 2.347333e-6)
GSI16 = Gnat*2.843e-5
show("016", 164, "Schritt 4: G_nat*2.843e-5", GSI16, 6.673469e-11)
print(f"   rel. Abw. zu 6.6743e-11: {rel(GSI16,6.6743e-11):+.4f} % (Dokument 0.0125 %)")
show("016", "57-63", "1/28.4", 1/28.4, 3.521e-2)
show("016", 75, "3.521e-2 * xi", 3.521e-2*xi, 4.695e-6)
show("016", 76, "4.695e-6/xi^2", 4.695e-6/xi**2, 264)
show("016", 76, "xi^2", xi**2, 1.778e-8)
print("   Dimension Z.75/107: [E^-1]*[1] = [E^-1], nicht [E^-2]")
show("016", 117, "r0*E0 = 0.035211*28.4", 0.035211*28.4, 1.0)
print(f"Dok 016 Z.123: G_char = r0/(2E0) = {0.035211/(2*28.4):.4g}  vs  xi^2/(2 E_char) = {xi**2/(2*28.4):.4g}  -> ungleich")
f2 = 2*(28.4*1.333e-4)**2
show("016", "149-152", "2*(E_char*xi)^2", f2, 2.868e-5)
print(f"   vs verwendeter Faktor 2.843e-5: {rel(f2,2.843e-5):+.3f} %; G_SI mit 2.868e-5 wäre {Gnat*f2:.4g} ({rel(Gnat*f2,G_CODATA):+.2f} %)")
print(f"   Produkt der beiden Faktoren 3.521e-2*2.843e-5 = {3.521e-2*2.843e-5:.6g}")
# Tabelle Z.282ff: abgeleitete Planck-Größen mit G_T0 = 6.673469e-11
Gt = 6.673469e-11
ref = dict(mP=sqrt(hbar*c/G_CODATA), tP=sqrt(hbar*G_CODATA/c**5), FP=c**4/G_CODATA, PP=c**5/G_CODATA)
t0  = dict(mP=sqrt(hbar*c/Gt), tP=sqrt(hbar*Gt/c**5), FP=c**4/Gt, PP=c**5/Gt)
doc = dict(mP=0.0062, tP=0.0158, FP=0.0220, PP=0.0220)
for k in ref:
    print(f"Dok 016 Tab. Z.283ff {k}: T0 {t0[k]:.4e}, Ref {ref[k]:.4e}, Fehler {abs(rel(t0[k],ref[k])):.4f} % (Dokument {doc[k]} %)")

print("\n=== Dok 028 ===")
show("028", 97, "xi/2", xi/2, 6.666667e-5)
G28 = 6.666667e-5*1.00115e-6
show("028", 99, "6.666667e-5*1.00115e-6", G28, 6.674e-11)
print(f"   vs CODATA {rel(G28,G_CODATA):+.4f} %; K_SI aus 016-Faktoren: {3.521e-2*2.843e-5:.6g}")
print("   K_SI als 'dimensionslos' bezeichnet (Z.210), trägt aber die SI-Einheit von G")
show("028", 105, "M_P = sqrt(hbar c/G) mit G_CODATA", sqrt(hbar*c/G_CODATA), 2.176434e-8)
show("028", 106, "xi^-1/2", xi**-0.5, 86.6025)
show("028", 106, "86.6025*2.758e20", 86.6025*2.758e20, 2.389e22)
show("028", 106, "M_P/m_e (CODATA)", 2.176434e-8/9.1093837e-31, 2.389e22)

print("\n=== Dok 030 === Z.25 nur zitiert (6.674e-11)")

print("\n=== Dok 041 ===")
mmu = 105.66
E0sq = 4*sqrt(2)*mmu/xi**4
show("041", "171-182", "E0 = sqrt(4 sqrt2 m_mu/xi^4) [MeV]", sqrt(E0sq), 7.398)
print("   Algebra Z.172-179 ist korrekt umgeformt; Dimension: rechte Seite [E], linke Seite [E^2]")
show("041", 497, "alpha_G = xi^2", xi**2, 1.78e-8)
show("041", 1216, "nur zitiert", 6.674e-11)
print(f"   Nebenbefund Z.493: alpha_S = xi^(-1/3) = {xi**(-1/3):.4g} (Dokument 9.65)")

print("\n=== Dok 044 === Z.205/245: G_SI = xi^2/(4 m_e)*C_dim*C_conv ohne Zahlenwert; Z.238 G=1 (Konvention)")
print("\n=== Dok 053 === Z.21 nur zitiert (6.67e-11)")
