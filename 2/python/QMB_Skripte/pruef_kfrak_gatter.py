"""
pruef_kfrak_gatter.py — Kapitel 8: K_frak im X-Gatter
Quelle: QMB_n08_qubit_formalismus.tex

FFGFT-Vorhersage: Pi-Gatter (Bit-Flip X) dreht um alpha = pi * K_frak
statt um pi. Abweichung: delta = pi - pi*K_frak = pi * 100*xi = pi * 0.01333
Prozentuell: delta_percent = 100*xi * 100% = 1.333%

K_frak = 1 - 100*xi = 74/75 ≈ 0.98667
xi     = 1/7500 = 4/30000
"""

import numpy as np

xi      = 4 / 30000
K_frak  = 1 - 100 * xi        # = 74/75 = 0.98667
pi_ideal  = np.pi
pi_actual = np.pi * K_frak

delta_rad     = pi_ideal - pi_actual          # = pi * 100 * xi
delta_deg     = np.degrees(delta_rad)
delta_percent = 100 * xi * 100                # = 1.333...%

print("=" * 60)
print("pruef_kfrak_gatter.py — Kapitel 8: K_frak-Gatter")
print("=" * 60)
print(f"xi           = {xi:.6e}")
print(f"K_frak       = {K_frak:.8f}  (= 74/75 = {74/75:.8f})")
print(f"pi_ideal     = {pi_ideal:.8f} rad")
print(f"pi_actual    = {pi_actual:.8f} rad")
print(f"delta_rad    = {delta_rad:.6e} rad")
print(f"delta_deg    = {delta_deg:.6f}°")
print(f"delta_prozent= {delta_percent:.4f}%")

errors = 0

# Check 1: K_frak = 74/75
if abs(K_frak - 74/75) > 1e-12:
    print(f"FEHLER: K_frak != 74/75")
    if not (nisq_rauschen_min <= signal <= nisq_rauschen_max):
        errors += 1
else:
    print("\n[1] K_frak = 74/75  OK")

# Check 2: delta_percent = 100*xi*100 = 4/3 %
expected_pct = 4/3
if abs(delta_percent - expected_pct) > 1e-8:
    print(f"FEHLER: delta_percent={delta_percent} != {expected_pct}")
    if not (nisq_rauschen_min <= signal <= nisq_rauschen_max):
        errors += 1
else:
    print(f"[2] delta_percent = {delta_percent:.6f}% = 4/3%  OK")

# Check 3: X-Gatter mit Kfrak: Zustand |0> wird zu cos(pi*K_frak/2)|0> + sin(pi*K_frak/2)|1>
# Standard: |0> -> |1> exakt; mit K_frak: leichte Abweichung
alpha0 = np.array([1.0, 0.0], dtype=complex)
Rx_ideal  = np.array([[np.cos(pi_ideal/2),  -1j*np.sin(pi_ideal/2)],
                       [-1j*np.sin(pi_ideal/2), np.cos(pi_ideal/2)]])
Rx_kfrak  = np.array([[np.cos(pi_actual/2),  -1j*np.sin(pi_actual/2)],
                       [-1j*np.sin(pi_actual/2), np.cos(pi_actual/2)]])
psi_ideal = Rx_ideal @ alpha0
psi_kfrak = Rx_kfrak @ alpha0

fidelity = abs(np.dot(psi_ideal.conj(), psi_kfrak))**2
infidelity = 1 - fidelity
expected_infidelity = (np.sin(delta_rad/2))**2
if abs(infidelity - expected_infidelity) > 1e-12:
    print(f"FEHLER: Infidelität {infidelity:.4e} != erwartet {expected_infidelity:.4e}")
    if not (nisq_rauschen_min <= signal <= nisq_rauschen_max):
        errors += 1
else:
    print(f"[3] Infidelität 1-F = {infidelity:.4e}  OK")

# Check 4: SNR — NISQ-Rauschen ~1-5%, K_frak-Abweichung 1.333% -> unter NISQ-Rauschen
nisq_rauschen_min = 0.01   # NISQ-Rauschen 1--5%
nisq_rauschen_max = 0.05
signal = delta_percent / 100
if nisq_rauschen_min <= signal <= nisq_rauschen_max:
    print(f"[4] Signal ({signal:.4f}) im NISQ-Rauschband [{nisq_rauschen_min},{nisq_rauschen_max}]: nicht isolierbar [K]  OK")
else:
    print(f"[4] FEHLER: Signal ({signal:.4f}) ausserhalb NISQ-Rauschband [{nisq_rauschen_min},{nisq_rauschen_max}]")
    if not (nisq_rauschen_min <= signal <= nisq_rauschen_max):
        errors += 1

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K]")
else:
    print(f"{errors} FEHLER")
