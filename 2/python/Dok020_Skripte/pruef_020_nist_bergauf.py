#!/usr/bin/env python3
"""Prüfskript zu Dok. 020 (Abschnitt Atomuhren) und Dok. 078 (Messpräzision).

Anlass: NIST-Uhrenvergleich Boulder -- Mount Blue Sky (Yb-Gitteruhren,
~2,65 km Höhenunterschied, 80-km-Freistrahlstrecke, Ziel ~10 ppm der
Rotverschiebung).  Geprüft wird, was die FFGFT für diesen Versuch erwartet
und dass die aus Dok. 020 entfernte Korrektur  -xi * dE / E_P  für ihn
folgenlos ist.

Aufruf aus der Repo-Wurzel:
    python3 2/python/Dok020_Skripte/pruef_020_nist_bergauf.py
"""
import math
import sympy as sp

c = 299_792_458.0          # m/s
g = 9.796                  # m/s^2, Boulder
h_pl = 6.626_070_15e-34    # J s
eV = 1.602_176_634e-19     # J
E_P_eV = 1.220_890e28      # Planck-Energie in eV
xi = sp.Rational(4, 30000)
xif = float(xi)

ergebnisse = []


def pruefe(name, ok, info):
    ergebnisse.append(ok)
    print(f"[{'OK' if ok else 'FEHLER'}] {name}: {info}")


# 1  Rotverschiebung Boulder -> Gipfel (Schwachfeld, ART)
dz_ART = 2.885e-13                      # Vorhersage aus dem Video
dh = dz_ART * c**2 / g
ns_pro_tag = dz_ART * 86400 * 1e9
pruefe("1 ART-Rotverschiebung",
       2500 < dh < 2800 and 24 < ns_pro_tag < 26,
       f"dz = 2.885e-13 entspricht dh = {dh:.0f} m, {ns_pro_tag:.1f} ns/Tag")

# 2  Massenlesart m = m0 e^(Phi/c^2) gegen ART (isotrope Schwarzschild-Metrik)
U = sp.symbols('U', positive=True)
exp_lesart = sp.exp(-U)
art_iso = (1 - U/2) / (1 + U/2)           # sqrt(g00), isotrop
diff = sp.series(exp_lesart - art_iso, U, 0, 4).removeO()
gleich_bis_2 = sp.simplify(diff.coeff(U, 1)) == 0 and sp.simplify(diff.coeff(U, 2)) == 0
U_erde = 6.674e-11 * 5.972e24 / (6.371e6 * c**2)
rel = abs(float(diff.coeff(U, 3))) * 3 * U_erde**2   # d(U^3)/dU * U^2-Faktor relativ zu dU
pruefe("2 Massenlesart = ART bis 2. Ordnung (gamma = beta = 1)",
       gleich_bis_2,
       f"Differenz erst bei U^3 (Koeff. {diff.coeff(U, 3)}); relativ zur Rotverschiebung ~{rel:.0e}")

# 3  Hypothetische Korrekturen der Größe xi bzw. xi^2 gegen 10-ppm-Ziel
grenze = 1e-5
f1 = xif / grenze
f2 = grenze / xif**2
pruefe("3 Größenordnungen xi / xi^2 gegen 10 ppm",
       12 < f1 < 14 and 400 < f2 < 700,
       f"xi = {xif:.3e} liegt {f1:.1f}x über, xi^2 = {xif**2:.2e} {f2:.0f}x unter der Grenze")

# 4  Entfernte Formel aus Dok. 020: xi * dE / E_P für Yb (518,3 THz)
dE_Yb = h_pl * 518.295_836_590_863_6e12 / eV
korr = xif * dE_Yb / E_P_eV
pruefe("4 xi*dE/E_P für Yb",
       1e-32 < korr < 5e-32,
       f"dE = {dE_Yb:.3f} eV -> {korr:.1e} (unmessbar)")

# 5  Gleiche Atomsorte: Korrektur kürzt sich im Frequenzverhältnis exakt
f0, eps, z = sp.symbols('f0 epsilon z', positive=True)
f_unten = f0 * (1 - eps)
f_oben = f0 * (1 - eps) * (1 + z)
pruefe("5 Kürzung bei Yb/Yb-Vergleich",
       sp.simplify(f_oben / f_unten - (1 + z)) == 0,
       "f_oben/f_unten = 1 + z, unabhängig von epsilon")

# 6  Kosmische Wegverlängerung auf 80 km (H0 * L / c)
H0 = 67.4e3 / 3.0857e22
weg = H0 * 80e3 / c
pruefe("6 Wegverlängerung 80 km", weg < 1e-20, f"H0*L/c = {weg:.1e}")

# 7  Dok. 078: Chou et al. 2010, 33 cm
chou = g * 0.33 / c**2
pruefe("7 Chou 2010 (33 cm)", 3e-17 < chou < 4.5e-17,
       f"g*h/c^2 = {chou:.1e} -- ART-Rotverschiebung, keine xi-Signatur")

# 8  Dok. 020, GW-Term xi*(f/f_P)^2 im LIGO-Band 10..1000 Hz
f_P = 1.855e43
lo, hi = (10 / f_P)**2, (1000 / f_P)**2
pruefe("8 GW-Term (f/f_P)^2", 1e-86 < lo < 1e-84 and 1e-82 < hi < 1e-80,
       f"{lo:.0e} bis {hi:.0e} -- nicht messbar")

print(f"\nErgebnis: {sum(ergebnisse)}/{len(ergebnisse)} bestanden")
raise SystemExit(0 if all(ergebnisse) else 1)
