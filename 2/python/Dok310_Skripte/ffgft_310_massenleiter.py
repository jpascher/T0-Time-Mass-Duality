#!/usr/bin/env python3
"""
FFGFT Dok. 310 — Massenleiter: glatte Bausteine erzeugen krumme Verhaeltnisse
Prueft: m_l = r_l * xi^p_l * v reproduziert die NICHT-glatten Messwerte.
Eingaben deklariert: xi (harmonisch, P33), r_l und p_l (Dok 190).
"""
import math
from fractions import Fraction

xi = Fraction(1, 7500)

# Vorfaktoren (2-3-5-harmonisch) und Exponenten, Dok 190/258.
# Die Exponenten bilden eine GEOMETRISCHE Folge p_(n+1)=(2/3)p_n
# (Verhaeltnis q=2/3 = Koide-Wert), NICHT arithmetisch mit
# konstanter Schrittweite. Spruenge: 1/2 (e->mu), 1/3 (mu->tau).
r = {'e': Fraction(4,3),  'mu': Fraction(16,5), 'tau': Fraction(25,9)}
p = {'e': Fraction(3,2),  'mu': Fraction(1),    'tau': Fraction(2,3)}

# Messwerte (PDG)
meas = {'mu/e': 206.7683, 'tau/e': 3477.23}

def ratio(l):
    return float(r[l]/r['e']) * float(xi)**float(p[l]-p['e'])

print("="*60)
print(" MASSENLEITER: glatte Bausteine -> krumme Verhaeltnisse")
print("="*60)
print("  Bausteine (alle 2-3-5-glatt):")
for l in ['e','mu','tau']:
    print(f"    {l:>4}: r = {r[l]}, p = {p[l]}")
print(f"    xi = {xi} = {float(xi):.6e}")
print()

for key, l in [('mu/e','mu'), ('tau/e','tau')]:
    pred = ratio(l)
    m = meas[key]
    print(f"  m_{l}/m_e:  FFGFT = {pred:8.3f}  Messung = {m:8.3f}"
          f"  Abw = {(pred/m-1)*100:+.2f}%")
print()
print()
print("  Geometrische Folge p_(n+1) = (2/3) p_n (Dok 258):")
print(f"    p_e * 2/3  = {float(p['e']*Fraction(2,3)):.4f}  (p_mu = {float(p['mu']):.4f})")
print(f"    p_mu * 2/3 = {float(p['mu']*Fraction(2,3)):.4f}  (p_tau = {float(p['tau']):.4f})")
print("    Verhaeltnis q=2/3 = Koide-Wert Q. Spruenge 1/2, 1/3 folgen daraus.")
print()
print("  Die Messwerte 206.77 und 3477 sind NICHT glatt.")
print("  Glatte Bausteine erzeugen sie mit <2% Abweichung.")
print("  Ein perfekter Fit haette 0.00% -- die Restabweichung")
print("  zeigt: Struktur, keine Rueckwaerts-Anpassung.")
