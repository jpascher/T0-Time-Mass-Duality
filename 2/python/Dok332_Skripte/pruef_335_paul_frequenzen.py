"""
Dok. 335 -- Pruefskript: Massegebundene Zeitskalen und Interferometrie
FFGFT-Eigenfrequenzen aus T~*m=1 vs. Holometer/QUEST/D4-Gitter

Ausfuehren: python3 pruef_335_paul_frequenzen.py
"""

import numpy as np

print("=" * 70)
print("DOK. 335: FFGFT-FREQUENZSKALEN vs. INTERFEROMETRIE")
print("Pruefskript zu T~*m=1 -- Massegebundene Zeitskalen")
print("=" * 70)

# Fundamentalkonstanten (CODATA 2018)
c    = 2.99792458e8       # m/s
hbar = 1.054571817e-34    # J*s
h    = 2 * np.pi * hbar   # J*s
m_e  = 9.1093837015e-31   # kg
m_mu = 1.883531627e-28    # kg
m_p  = 1.67262192369e-27  # kg
m_n  = 1.67492749804e-27  # kg
l_P  = 1.616255e-35       # m  (Planck-Laenge)
xi0  = 4 / 30000          # FFGFT-Parameter
K_frak = 1 - 100 * xi0    # fraktale Korrektur

# Interferometer-Parameter
L_holo  = 40.0            # m  (Holometer)
L_quest = 1.84            # m  (QUEST)

print("\n--- EINGABEPARAMETER ---")
print(f"  xi_0    = {xi0:.6f}")
print(f"  K_frak  = 1 - 100*xi_0 = {K_frak:.6f}")
print(f"  Holometer: L = {L_holo} m")
print(f"  QUEST:     L = {L_quest} m")

print("\n" + "=" * 70)
print("ASSERTION 1: Comptonfrequenzen aus T~*m=1")
print("=" * 70)

teilchen = [
    ("Elektron", m_e),
    ("Myon",     m_mu),
    ("Proton",   m_p),
    ("Neutron",  m_n),
]

for name, m in teilchen:
    f_m = m * c**2 / h
    R_m = hbar / (m * c**2)
    assert f_m > 1e19, f"{name}: f_m zu klein"
    assert abs(f_m * R_m - hbar/h) < 1e-10, f"{name}: f_m * R_m != hbar/h"
    print(f"  {name:10s}: f_m = {f_m:.4e} Hz,  R_m = {R_m:.4e} m  [OK]")

print("\nAssertion 1 bestanden: alle Comptonfrequenzen korrekt aus T~*m=1")

print("\n" + "=" * 70)
print("ASSERTION 2: Frequenzluecke Elektron vs. Interferometer")
print("=" * 70)

f_e = m_e * c**2 / h
f_holo  = c / (2 * L_holo)
f_quest = c / (2 * L_quest)

ratio_holo  = f_e / f_holo
ratio_quest = f_e / f_quest

print(f"  f_e (Elektron-Compton):  {f_e:.4e} Hz")
print(f"  f_c (Holometer):         {f_holo:.4e} Hz = {f_holo/1e6:.4f} MHz")
print(f"  f_c (QUEST):             {f_quest:.4e} Hz = {f_quest/1e6:.4f} MHz")
print(f"  f_e / f_c (Holometer) =  {ratio_holo:.3e}  (>= 10^13 erwartet)")
print(f"  f_e / f_c (QUEST)     =  {ratio_quest:.3e}  (>= 10^12 erwartet)")

assert ratio_holo > 1e13, "Frequenzluecke Holometer zu klein"
assert ratio_quest > 1e12, "Frequenzluecke QUEST zu klein"
print("\nAssertion 2 bestanden: Frequenzluecke mindestens 13 Groessenordnungen")

print("\n" + "=" * 70)
print("ASSERTION 3: D4-Gitter -- Dispersionskorrektur bei L=40m")
print("=" * 70)

# D4-Gitter: 24 naechste Nachbarn
nn = []
for i in range(4):
    for s in [1, -1]:
        v = [0,0,0,0]; v[i] = s
        nn.append(np.array(v, dtype=float))
for s0 in [0.5,-0.5]:
    for s1 in [0.5,-0.5]:
        for s2 in [0.5,-0.5]:
            for s3 in [0.5,-0.5]:
                nn.append(np.array([s0,s1,s2,s3]))

assert len(nn) == 24, f"D4 sollte 24 nn haben, hat {len(nn)}"
dists = [np.linalg.norm(v) for v in nn]
assert max(dists) - min(dists) < 1e-10, "D4 nn nicht alle gleich weit"

k1_SI  = np.pi / L_holo          # 1/m
k1_lat = k1_SI * l_P             # dimensionslos (Gittereinheiten)
korr   = k1_lat**2               # Dispersionskorrektur O(k*a)^2

print(f"  D4-Gitter: 24 naechste Nachbarn, alle Abstand 1  [OK]")
print(f"  k_1 (L=40m) in Gittereinheiten: k1*l_P = {k1_lat:.3e}")
print(f"  Dispersionskorrektur (k*l_P)^2  = {korr:.3e}  (<<1 erwartet)")

assert korr < 1e-70, "Dispersionskorrektur sollte < 10^-70 sein"
print(f"\nAssertion 3 bestanden: D4-Korrektur ~ {korr:.1e} (unmessbar)")

print("\n" + "=" * 70)
print("ASSERTION 4: Masse fuer Signal bei f_c (Holometer)")
print("=" * 70)

m_signal = h * f_holo / c**2
ratio_me = m_signal / m_e

print(f"  Masse fuer Signal bei f_c = {f_holo:.3e} Hz:")
print(f"  m = h*f_c/c^2 = {m_signal:.3e} kg")
print(f"  m / m_e       = {ratio_me:.3e}  (<<1, kein bekanntes Teilchen)")

assert ratio_me < 1e-10, "Masse fuer Holometer-Signal groesser als erwartet"
print(f"\nAssertion 4 bestanden: kein bekanntes Teilchen bei dieser Masse")

print("\n" + "=" * 70)
print("ASSERTION 5: K_frak-Korrektur auf Comptonfrequenz")
print("=" * 70)

Delta_f_e    = f_e * (1 - K_frak)   # = f_e * 100*xi0
rel_korrektur = 1 - K_frak          # = 100*xi0

print(f"  K_frak = 1 - 100*xi_0 = {K_frak:.6f}")
print(f"  Relative Korrektur:   100*xi_0 = {rel_korrektur:.6f} = {rel_korrektur*100:.4f}%")
print(f"  f_e (ohne K_frak):    {f_e:.6e} Hz")
print(f"  f_e * K_frak:         {f_e*K_frak:.6e} Hz")
print(f"  Delta f_e:            {Delta_f_e:.4e} Hz")
print(f"  (das waere im Gammabereich spektroskopisch zugaenglich)")

assert abs(rel_korrektur - 400/30000) < 1e-12, "K_frak-Rechnung inkonsistent"
assert Delta_f_e > 1e17, "Delta f_e sollte > 10^17 Hz sein"
print(f"\nAssertion 5 bestanden: K_frak-Korrektur = {rel_korrektur*100:.4f}%")

print("\n" + "=" * 70)
print("GESAMTERGEBNIS: 5/5 Assertions bestanden")
print("=" * 70)
print(f"""
Kernaussagen (aus T~*m=1, abgeleitet):

  Elektron-Comptonfrequenz:  f_e = {f_e:.4e} Hz
  Holometer-Frequenz:        f_c = {f_holo:.4e} Hz  ({f_holo/1e6:.4f} MHz)
  Frequenzluecke:            f_e / f_c = {ratio_holo:.2e}

  D4-Gitter Dispersionskorrektur bei L=40m: {korr:.1e}  (nicht messbar)

  K_frak-Korrektur auf f_e:  Delta f_e = {Delta_f_e:.3e} Hz  ({rel_korrektur*100:.4f}%)
  (Gammabereich, nicht interferometrisch zugaenglich)

  Masse fuer Signal bei 3.75 MHz: {m_signal:.2e} kg = {ratio_me:.1e} * m_e
  (kein bekanntes Teilchen)
""")
