#!/usr/bin/env python3
"""
pruef_382_myon_g2_stand.py  -- Dok. 382: Myon g-2, Stand 2025, Einordnung der FFGFT-Aussagen

Quellen der Eingabewerte (alle in Einheiten 1e-11):
  Fermilab-Endergebnis (Juni 2025):      a_mu(FNAL)  = 116 592 070.5 (14.8)   [127 ppb]
  Weltmittel (E821 + E989, WP25 Gl. 9.5): a_mu(exp)   = 116 592 071.5 (14.5)
  Theory Initiative White Paper 2025:    a_mu(SM,25) = 116 592 033 (62)       [HVP aus Gitter-QCD]
  Differenz WP25 Gl. 9.6:                Delta_25    = 38 (63)
  Stand 2021 (WP20 gegen FNAL+BNL 2021): Delta_21    = 251 (59)
FFGFT-Werte: Dok. 018 (Rev. 12) -- a_mu^(korr) = a_e^(korr) + 4 pi / f^(5/3), f = 7500.
Frühe Dokumente (019, 033, 070): Delta a_mu^(T0) = 251e-11 als T0-Beitrag.
Jede Prüfung kann fehlschlagen.
"""
import math

ok = n = 0
def check(name, cond, info=""):
    global ok, n
    n += 1; ok += bool(cond)
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}" + (f"  ({info})" if info else ""))

E11 = 1e-11
exp_c, exp_s = 116592071.5, 14.5
sm25_c, sm25_s = 116592033.0, 62.0
d25_c, d25_s = 38.0, 63.0
d21_c, d21_s = 251.0, 59.0

print("1. Stand der Abweichung exp - SM")
d = exp_c - sm25_c
s = math.hypot(exp_s, sm25_s)
check("Differenz Weltmittel - WP25 = 38(63)e-11 (Rundung)", abs(d - d25_c) < 1 and abs(s - d25_s) < 1.5,
      f"{d:.1f} ± {s:.1f}")
sig25 = d25_c / d25_s
sig21 = d21_c / d21_s
check("2021: Abweichung 251(59) entspricht etwa 4,2 sigma", 4.1 < sig21 < 4.4, f"{sig21:.2f} sigma")
check("2025: Abweichung 38(63) entspricht etwa 0,6 sigma (nicht signifikant)", 0.5 < sig25 < 0.7, f"{sig25:.2f} sigma")

print("\n2. Früherer T0-Beitrag Delta a_mu = 251e-11 gegen den Stand 2025")
t0_old = 251.0
z = (t0_old - d25_c) / d25_s
check("Ein fester Zusatzbeitrag von 251e-11 liegt 2025 rund 3,4 sigma über der Differenz",
      3.2 < z < 3.6, f"{z:.2f} sigma")
check("Spielraum (95 %) für einen Zusatzbeitrag: 38 ± 2*63 -> etwa -88 ... +164 (e-11)",
      d25_c - 2*d25_s < 0 < d25_c + 2*d25_s, f"{d25_c-2*d25_s:.0f} ... {d25_c+2*d25_s:.0f}")

print("\n3. Absolutwert nach Dok. 018 (Rev. 12) gegen das Weltmittel")
f = 7500.0
S3 = 19.739
k_geom = 2.2236
Kfrak = 1 - 100 * 4 / 30000
k_eff = k_geom / Kfrak**1.5
a_e = S3 / f / k_eff
da_mu = 4 * math.pi / f**(5/3)
a_mu = a_e + da_mu
check("Delta a_fraktal = 4 pi / 7500^(5/3) = 4,373e-6", abs(da_mu - 4.373e-6) < 5e-9, f"{da_mu:.4e}")
check("a_e(korr) = 1,1600e-3 (Dok. 018)", abs(a_e - 1.1600e-3) < 2e-7, f"{a_e:.5e}")
check("a_mu(korr) = 1,1644e-3 (Dok. 018)", abs(a_mu - 1.1644e-3) < 2e-7, f"{a_mu:.5e}")
rel = (a_mu - exp_c*E11) / (exp_c*E11)
check("Abweichung vom Weltmittel etwa -0,13 %", -0.0014 < rel < -0.0012, f"{100*rel:.3f} %")
absdiff = abs(a_mu - exp_c*E11) / E11
check("Absolut etwa 150 000e-11 -- rund 600-mal größer als die frühere Anomalie von 251e-11",
      500 < absdiff / d21_c < 900, f"{absdiff:.0f}e-11, Faktor {absdiff/d21_c:.0f}")
check("in Einheiten der Messunsicherheit (14,5e-11) weit über 1000 sigma: kein Präzisionsvergleich",
      absdiff / exp_s > 1000, f"{absdiff/exp_s:.0f}")

print("\n4. Verhältnis-Linie (Dok. 018, Rev. 12) -- unabhängig von der Anomalie")
r1 = f**(1/3) - 1
check("Delta a(tau-mu)/Delta a(mu-e) = f^(1/3) - 1 = 18,57 (exakt aus den Exponenten)",
      abs(r1 - 18.57) < 0.005 and abs((4*math.pi/f**(4/3) - 4*math.pi/f**(5/3))/(4*math.pi/f**(5/3)) - r1) < 1e-12, f"{r1:.4f}")
a_e_exp = 1.15965218059e-3          # CODATA/Fan et al. 2023
a_mu_exp = exp_c * E11
d_mue = a_mu_exp - a_e_exp
check("gemessenes Delta a(mu-e) = a_mu - a_e = 6,2685e-6 (2025)", abs(d_mue - 6.2685e-6) < 2e-10, f"{d_mue:.5e}")
d_mue_21 = 116592061e-11 - a_e_exp   # Weltmittel 2021
check("gegenüber 2021 praktisch unverändert (relative Änderung < 2e-5)",
      abs(d_mue - d_mue_21) / d_mue < 2e-5, f"Delta = {abs(d_mue-d_mue_21):.1e}")
mt_mm = 1776.93 / 105.6583755
bridge = 144/125 * mt_mm
check("Brücke (144/125)*m_tau/m_mu = 19,37, nahe f^(1/3) = 19,57 (Massenformel-Verhältnis)", abs(bridge - 19.37) < 0.01, f"{bridge:.4f}")
a_tau = a_e_exp + bridge * d_mue
check("a_tau-Vorhersage mit Stand 2025: 1,2811e-3 (Dok. 018: 1,282e-3 mit gerundetem a_e)",
      abs(a_tau - 1.2811e-3) < 5e-7, f"{a_tau:.5e}")
a_tau_direct = a_e + 4*math.pi/f**(4/3)
check("direkte Absolutformel a_tau(korr) = a_e(korr) + 4 pi/f^(4/3) = 1,2456e-3 (Dok. 018 Tabelle)",
      abs(a_tau_direct - 1.2456e-3) < 2e-7, f"{a_tau_direct:.5e}")
check("verankerter Wert (Brücke + Messwerte) liegt 2,8 % über dem direkten -- der Korpus verwendet den verankerten",
      0.025 < a_tau/a_tau_direct - 1 < 0.032, f"{100*(a_tau/a_tau_direct-1):.2f} %")
a_tau_sm = 1.17721e-3
check("Unterschied zum SM-Wert a_tau = 1,1772e-3 etwa 1,04e-4", abs((a_tau - a_tau_sm) - 1.04e-4) < 3e-6,
      f"{a_tau - a_tau_sm:.3e}")
# Beste Schranke: CMS 2024 (Photon-Photon-Erzeugung von Tau-Paaren in pp-Kollisionen), -0,0042 < a_tau < 0,0046 bei 95 % CL;
# die ältere DELPHI-Schranke (-0,052 ... 0,013) ist rund siebenmal weiter.
cms_lo, cms_hi = -0.0042, 0.0046
check("heutige Schranke (CMS 2024: -0,0042 ... 0,0046, 95 % CL) ist rund 85-mal weiter als dieser Unterschied; beide Werte liegen darin",
      84 < (cms_hi - cms_lo) / (a_tau - a_tau_sm) < 86 and cms_lo < a_tau_sm < a_tau < cms_hi,
      f"Faktor {(cms_hi-cms_lo)/(a_tau-a_tau_sm):.1f}")
check("Modellwert Delta a(mu-e) = 4,373e-6 liegt 30 % unter dem gemessenen; die Brücke nutzt den gemessenen",
      0.28 < 1 - da_mu / d_mue < 0.32, f"{100*(1-da_mu/d_mue):.1f} %")

print(f"\nERGEBNIS: {ok}/{n} Prüfungen bestanden")
assert ok == n
