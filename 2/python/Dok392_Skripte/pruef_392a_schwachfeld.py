#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruef_392a_schwachfeld.py -- Dok. 392: Wo die Darstellungen der Gravitation sich trennen.
Teil A: statisches Schwachfeld (gamma, beta) -- welche Darstellungen die Messungen zulassen.

Rechnet nach (Bezug Dok. 389, 308):
  1. g00 = (m/m0)^2: exponentielle Massenform gibt beta = 1, lineare beta = 1/2.
  2. Lichtablenkung und Shapiro skalieren mit (1+gamma)/2; Cassini schließt gamma = 0, -1 aus.
  3. Perihel: Faktor (2+2gamma-beta)/3; Merkur schließt lineare Form und "nur Takt" aus.
  4. Geodätische Präzession (Gravity Probe B): Faktor (1+2gamma)/3 -- unabhängiger Test der
     räumlichen Hälfte, ohne Licht.
  5. Nordtvedt-Parameter eta = 4beta - gamma - 3 (ohne Vorzugssystem): Mondlaser.
Messwerte [Q]: Bertotti u.a. 2003 (Cassini); Clemence 1947/IAU (Merkur 42,98"/Jh.);
Everitt u.a. 2011, PRL 106, 221101 (GP-B); Williams, Turyshev, Boggs 2012, CQG 29, 184004 (LLR:
(m_G/m_I)_E - (m_G/m_I)_M = (-0,8 +- 1,3)e-13; Eigenenergie-Differenz Erde-Mond -4,45e-10).
sympy + Standardbibliothek.
"""
import math
import sympy as sp

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

c = 299792458.0
GMs = 1.32712440018e20; Rs = 6.957e8
GMe = 3.986004418e14
mas_per_yr = 180/math.pi*3600e3 * 365.25*86400      # rad/s -> mas/Jahr
rad2as = 180/math.pi*3600

# Darstellungen: (Name, gamma, beta)
DARST = [("Raumkrümmung (ART)", 1, 1),
         ("Takt (exp) + fraktale Wegverlängerung", 1, 1),
         ("Takt (linear) + Wegverlängerung", 1, sp.Rational(1, 2)),
         ("nur Takt (Massenänderung allein)", 0, 1),
         ("konform flach / Nordström (Dok. 143)", -1, sp.Rational(1, 2))]

print("1. beta aus der Form der Massenänderung (g00 = (m/m0)^2, Phi = -U)")
U = sp.symbols('U', positive=True)
g00_exp = sp.series(sp.exp(-2*U), U, 0, 3).removeO()
g00_lin = sp.expand((1 - U)**2)
beta_exp = sp.Rational(1, 2)*g00_exp.coeff(U, 2)
beta_lin = sp.Rational(1, 2)*g00_lin.coeff(U, 2)
check("m = m0 exp(Phi/c^2): g00 = 1 - 2U + 2U^2  ->  beta = 1", beta_exp == 1, f"g00 = {g00_exp}")
check("m = m0 (1 + Phi/c^2): g00 = 1 - 2U + U^2  ->  beta = 1/2", beta_lin == sp.Rational(1, 2), f"g00 = {g00_lin}")

print("2. Lichtablenkung am Sonnenrand (Cassini: gamma - 1 = (2,1 +- 2,3)e-5)")
defl_GR = 4*GMs/(c**2*Rs)*rad2as
gam_meas, gam_err = 2.1e-5, 2.3e-5
for name, g, b in DARST:
    d = defl_GR*(1+g)/2
    sig = abs((g-1) - gam_meas)/gam_err
    print(f"     {name:42s} gamma={g:>2}  Ablenkung {d:6.3f}\"  Abstand zu Cassini {sig:9.1e} sigma")
check("ART-Wert 1,751\"", abs(defl_GR - 1.7512) < 2e-3, f"{defl_GR:.4f}\"")
check("nur Takt (gamma = 0) liegt 4e4 sigma neben Cassini -> ausgeschlossen", abs(-1-gam_meas)/gam_err > 4e4)
check("konform flach (gamma = -1) liegt 8e4 sigma daneben -> ausgeschlossen", abs(-2-gam_meas)/gam_err > 8e4)

print("3. Merkur-Periheldrehung (ART 42,98\"/Jh., gemessen gleich innerhalb ~0,04 %)")
mer_GR = 42.98
peri = {}
for name, g, b in DARST:
    f = float((2+2*g-b)/3)
    peri[name] = f*mer_GR
    print(f"     {name:42s} Faktor {f:6.3f}  -> {f*mer_GR:7.2f}\"/Jh.")
check("lineare Massenform gibt 50,1\"/Jh. (+17 %) -> ausgeschlossen",
      abs(peri["Takt (linear) + Wegverlängerung"] - 50.14) < 0.05)
check("nur Takt gibt 14,3\"/Jh. -> ausgeschlossen", abs(peri["nur Takt (Massenänderung allein)"] - 14.33) < 0.05)
check("Nordström gibt -7,2\"/Jh. -> ausgeschlossen", abs(peri["konform flach / Nordström (Dok. 143)"] + 7.16) < 0.05)

print("4. Geodätische Präzession (Gravity Probe B, polar, a = 7027,4 km)")
a = 7027.4e3                                        # mittlerer Bahnradius GP-B (Everitt 2011)
geo_GR = 1.5*GMe**1.5/(c**2*a**2.5)*mas_per_yr
geo_meas, geo_err = 6601.8, 18.3
check("ART-Vorhersage 6606 mas/Jahr reproduziert (Everitt: 6606,1)", abs(geo_GR - 6606) < 15, f"{geo_GR:.0f} mas/Jahr")
for name, g, b in DARST:
    v = geo_GR*(1+2*g)/3
    print(f"     {name:42s} {v:8.0f} mas/Jahr  ({abs(v-geo_meas)/geo_err:6.0f} sigma)")
check("nur Takt: 1/3 des Werts (2202 mas/Jahr), 240 sigma neben GP-B -- unabhängig von Licht",
      abs(geo_GR/3 - geo_meas)/geo_err > 200)

print("5. Nordtvedt-Parameter eta = 4 beta - gamma - 3 (Mondlaser, ohne Zusammensetzungskorrektur)")
d_sep, d_err, dU = -0.8e-13, 1.3e-13, -4.45e-10
eta_meas, eta_err = d_sep/dU, d_err/abs(dU)
print(f"     eta = Delta(m_G/m_I)/Delta(U/Mc^2) = ({eta_meas*1e4:.1f} +- {eta_err*1e4:.1f})e-4")
for name, g, b in DARST:
    eta = 4*b - g - 3
    print(f"     {name:42s} eta = {float(eta):5.2f}  ({abs(float(eta)-eta_meas)/eta_err:7.0f} sigma)")
check("exp-Form + Wegverlängerung: eta = 0, verträglich", 4*1-1-3 == 0)
check("lineare Form: eta = -2, rund 7000 sigma ausgeschlossen -- unabhängige Bestätigung der beta-Aussage",
      abs(-2-eta_meas)/eta_err > 6000)

print("6. Bilanz")
allowed = [nm for nm, g, b in DARST if g == 1 and b == 1]
check("Zugelassen bleiben genau ART und Takt(exp) + Wegverlängerung (gamma = beta = 1)",
      allowed == ["Raumkrümmung (ART)", "Takt (exp) + fraktale Wegverlängerung"], str(allowed))
# Mischform: die räumliche Hälfte wird zu Anteil w als Krümmung, zu Anteil s als Wegverlängerung
# getragen; gamma = w + s. Cassini verlangt |w + s - 1| < 3*2,3e-5 + 2,1e-5.
lim = 3*gam_err + gam_meas
mixes = [(1, 0), (0, 1), (0.4, 0.6), (0.4, 0.5), (0.5, 0.5), (0, 0)]
zul = [(w, s) for w, s in mixes if abs(w + s - 1) < lim]
check("Mischform: zulässig genau dann, wenn Krümmungs- und Weganteil der räumlichen Hälfte "
      "zusammen 1 ergeben (w + s = 1)", zul == [(1, 0), (0, 1), (0.4, 0.6), (0.5, 0.5)], str(zul))

print(f"\n{ok}/{n} Prüfungen bestanden")
raise SystemExit(0 if ok == n else 1)
