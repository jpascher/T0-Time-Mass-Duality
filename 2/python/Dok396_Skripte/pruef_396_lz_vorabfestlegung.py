#!/usr/bin/env python3
"""Prüfskript zu Dok. 396: Vorab-Festlegung zum LZ-Ereignis bei 248 keV.

Prüft die Zahlen, auf die sich die Festlegung stützt:
Signifikanzen und Zufallswahrscheinlichkeiten, Poisson-Erwartung des
Untergrunds, Phase der Jahresmodulation, Kinematik des Rückstoßes.

Aufruf aus der Repo-Wurzel:
    python3 2/python/Dok396_Skripte/pruef_396_lz_vorabfestlegung.py
"""
import math
from datetime import date

ok = n = 0


def check(name, cond, info=""):
    global ok, n
    n += 1
    ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FEHLER'}] {name}" + (f"  ({info})" if info else ""))


def p_einseitig(sigma):
    return 0.5 * math.erfc(sigma / math.sqrt(2))


print("1. Signifikanzen")
p26 = p_einseitig(2.6)
check("2,6 sigma (global): p = 4,7e-3, etwa 1 zu 200", abs(p26 - 4.66e-3) < 0.05e-3 and 180 < 1 / p26 < 230, f"1/{1/p26:.0f}")
p34 = p_einseitig(3.4)
check("3,4 sigma (lokal): p = 3,4e-4, etwa 1 zu 3000", abs(p34 - 3.37e-4) < 0.05e-4, f"1/{1/p34:.0f}")
p3 = p_einseitig(3.0)
check("3 sigma: etwa 1 zu 740", 700 < 1 / p3 < 780, f"1/{1/p3:.0f}")
p5 = p_einseitig(5.0)
check("5 sigma (Entdeckung): etwa 1 zu 3,5 Millionen", 3.4e6 < 1 / p5 < 3.6e6, f"1/{1/p5:.3g}")

print("\n2. Untergrund")
mu = 0.0106
P1 = 1 - math.exp(-mu)
check("Erwartung 0,0106 Ereignisse: P(>=1) = 1,05 %", abs(P1 - 0.01054) < 1e-4, f"{P1:.5f}")
check("lokaler Poisson-Wert vor Modell- und Versuchszahl-Korrektur liegt zwischen 2 und 2,6 sigma",
      p26 < P1 < p_einseitig(2.0))

print("\n3. Jahresmodulation")
t_max = date(2026, 6, 2).timetuple().tm_yday
t_ev = date(2023, 6, 16).timetuple().tm_yday
dt = t_ev - t_max
phase = math.cos(2 * math.pi * dt / 365.25)
check("Ereignis 16. Juni liegt 14 Tage nach dem erwarteten Maximum (2. Juni)", dt == 14, f"{dt} Tage")
check("Modulationsfaktor dort cos(2 pi 14/365) = 0,97", abs(phase - 0.971) < 0.002, f"{phase:.3f}")
v_sonne = 232.0; v_erde = 29.8; neigung = math.radians(60.0)
amp = v_erde * math.cos(neigung) / v_sonne
check("Geschwindigkeitsmodulation etwa +-6 % (Erdbahn 29,8 km/s, 60 Grad Neigung)", 0.06 < amp < 0.07, f"{amp*100:.1f} %")

print("\n4. Kinematik des Rückstoßes")
c = 299792.458
m_N = 130.0 * 0.9315          # GeV, Xe-Kern (A ~ 130)
v = 544.0 + 250.0             # km/s, Fluchtgeschwindigkeit + Erdbewegung (Obergrenze)
E_R = 248e-6                  # GeV
mu_min = math.sqrt(E_R * m_N / (2 * (v / c)**2))
m_min = mu_min * m_N / (m_N - mu_min)
check("elastisch: 248 keV verlangt eine Teilchenmasse von mindestens etwa 75 GeV", 60 < m_min < 90, f"{m_min:.0f} GeV")
E_max = 2 * m_N * (v / c)**2 * 1e6
check("Obergrenze des elastischen Rückstoßes für sehr schwere Teilchen > 1 MeV", E_max > 1000, f"{E_max:.0f} keV")

print(f"\nErgebnis: {ok}/{n} OK")
raise SystemExit(0 if ok == n else 1)
