#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392c_gravitationswellen.py -- Dok. 392, Teil C: Gravitationswellen und die flache Darstellung.

Drei Anforderungen, die jede Darstellung erfüllen muss:
  1. Geschwindigkeit: GW170817/GRB 170817A, Delta t = 1,74 s nach ~40 Mpc
     -> |c_gw/c - 1| <~ 1e-15 [Q] Abbott u.a. 2017, ApJL 848, L13.
  2. Gleiche Shapiro-Verzögerung für Licht und Gravitationswellen im Potential der Milchstraße
     (~ Hunderte Tage): eine Wegverlängerung, die nur Licht streckt, ist ausgeschlossen.
     [Q] dieselbe Arbeit: -2,6e-7 <= gamma_GW - gamma_EM <= 1,2e-6.
  3. Abstrahlung: Bahnzerfall des Hulse-Taylor-Pulsars entspricht der Quadrupolformel
     (Peters-Mathews); [Q] Weisberg & Huang 2016, ApJ 829, 55: Pdot_obs/Pdot_GR = 0,9983 +- 0,0016.
     Ein Skalarfeld mit eigener Wellenmode strahlt zusätzlich Dipolanteile ab (Monopol entfällt
     bei Massenerhaltung); Polarisation: GW170814 bevorzugt reine Tensormoden gegenüber reinen
     Skalarmoden mit Bayes-Faktor > 1000 [Q] Abbott u.a. 2017, PRL 119, 141101.
Standardbibliothek.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

c = 299792458.0; G = 6.67430e-11
Msun = 1.98847e30; GMsun = 1.32712440018e20
Mpc = 3.0857e22; kpc = 3.0857e19; day = 86400.0

print("1. Geschwindigkeit der Gravitationswellen")
d = 40*Mpc; dt = 1.74
frac = dt*c/d
check("Delta t / Laufzeit = 4e-16: |c_gw/c - 1| < 1e-15", frac < 1e-15, f"{frac:.1e}")
check("Eine Darstellung, in der Gravitationswellen nicht mit c laufen, ist ausgeschlossen "
      "(Zeitdifferenz bei 1 % Abweichung: 4e5 Jahre statt 1,7 s)", 0.01*d/c/(365.25*day) > 4e5)

print("2. Shapiro-Verzögerung im Potential der Milchstraße")
M_MW = 2.5e11*Msun; b = 8*kpc
dt_shap = 2*G*M_MW/c**3*math.log(d/b)     # (1+gamma) GM/c^3 ln(d/b), gamma = 1
print(f"     Shapiro-Verzögerung (gamma = 1): {dt_shap/day:.0f} Tage")
check("Shapiro-Verzögerung ~ 100 bis 400 Tage", 100 < dt_shap/day < 400)
bound = dt/dt_shap*2
check("gleiches gamma für Licht und Gravitationswellen auf < 1e-6 (eigene Abschätzung)", bound < 1e-6, f"{bound:.1e}")
check("Folgerung: wirkt die fraktale Wegverlängerung nur auf Licht (gamma_GW = 0), käme das Licht "
      "rund 120 Tage nach den Wellen an statt 1,7 s danach -> ausgeschlossen", 0.5*dt_shap > 1e6*dt)

print("3. Hulse-Taylor: Quadrupolstrahlung (Peters-Mathews)")
Pb = 0.322997448918*day; e = 0.6171340; mp = 1.438*Msun; mc = 1.390*Msun
fe = (1 + 73/24*e**2 + 37/96*e**4)/(1 - e**2)**3.5
Tsun = GMsun/c**3
Pdot = -192*math.pi/5*(2*math.pi*Tsun/Pb)**(5/3)*fe*(mp/Msun)*(mc/Msun)/((mp+mc)/Msun)**(1/3)
check("Pdot_GR = -2,4026e-12 (Weisberg & Huang: -2,40263e-12)", abs(Pdot + 2.40263e-12) < 2e-15, f"{Pdot:.5e}")
ratio, rerr = 0.9983, 0.0016
check("Messung/ART = 0,9983 +- 0,0016: Quadrupolstrahlung auf 0,2 % bestätigt", abs(ratio-1) < 2*rerr)
check("Zusätzliche Abstrahlung (z. B. skalarer Dipol) höchstens ~0,3 % des Quadrupols (2 sigma)",
      (1 - ratio) + 2*rerr < 0.005)

print("4. Polarisation und Bilanz (Literaturangaben, nicht gezählt)")
print("     GW170814: reine Tensormoden gegenüber reinen Skalarmoden bevorzugt, Bayes-Faktor > 1000 [Q].")
print("     Anforderung an jede Darstellung: Wellen mit c, gleiche Wirkung der räumlichen Hälfte auf")
print("     Licht und Wellen, Quadrupolabstrahlung mit zwei Tensorpolarisationen. Ein skalares m(x)")
print("     kann mit c laufen, liefert aber keine Tensorpolarisation; nötig ist ein Tensoranteil.")

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
