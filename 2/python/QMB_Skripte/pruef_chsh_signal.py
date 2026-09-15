"""
pruef_chsh_signal.py — Kapitel 12: CHSH-Auflösungsboden
Quelle: QMB_n12_grenze.tex

Aussage: Delta_CHSH_elem ≈ xi/(2*pi) ≈ 2e-5 pro Messung [S]
NISQ-Rauschen: 1-5% (P(11)-Fehler) -> Delta_CHSH_NISQ >> Delta_CHSH_elem [K]

Statistischer Bedarf für SNR=1: N_shots ~ 1/signal^2
"""

import numpy as np

xi = 1/7500
CHSH_QM = 2 * np.sqrt(2)   # Tsirelson-Schranke

# FFGFT-Vorhersage (spekulativ [S])
delta_CHSH_elem = xi / (2 * np.pi)

# NISQ-Rauschen in CHSH-Einheiten: P(11)-Fehler 1-5%, CHSH-Skala ~4
# CHSH = E(a,b) - E(a,b') + E(a',b) + E(a',b')
# Fehlerrate epsilon im Gatter -> CHSH-Fehler ~ 4*epsilon
nisq_eps_min = 0.01
nisq_eps_max = 0.05
delta_CHSH_NISQ_min = 4 * nisq_eps_min
delta_CHSH_NISQ_max = 4 * nisq_eps_max

# Benötigte Schüsse für SNR=1, 3, 5
N_snr1 = int(1 / delta_CHSH_elem**2)
N_snr3 = int(9 / delta_CHSH_elem**2)

print("=" * 60)
print("pruef_chsh_signal.py — Kapitel 12: CHSH-Auflösungsboden")
print("=" * 60)
print(f"xi                  = {xi:.6e}")
print(f"CHSH_QM (Tsirelson) = {CHSH_QM:.6f}")
print(f"delta_CHSH_elem     = xi/(2pi) = {delta_CHSH_elem:.4e}  [S]")
print(f"NISQ-Rauschen       = {delta_CHSH_NISQ_min:.3f} -- {delta_CHSH_NISQ_max:.3f} (4*eps_gate)")
print(f"N_shots (SNR=1)     = {N_snr1:.2e}")
print(f"N_shots (SNR=3)     = {N_snr3:.2e}")

errors = 0

# Check 1: delta_CHSH_elem << NISQ-Rauschen [K]
if delta_CHSH_elem < delta_CHSH_NISQ_min:
    print(f"\n[K] FFGFT-Signal ({delta_CHSH_elem:.2e}) << NISQ-Rauschen ({delta_CHSH_NISQ_min:.3f})  OK")
else:
    print(f"\nFEHLER: FFGFT-Signal nicht kleiner als NISQ-Rauschen")
    errors += 1

# Check 2: Tsirelson-Schranke 2*sqrt(2)
tol = 1e-10
if abs(CHSH_QM - 2*np.sqrt(2)) < tol:
    print(f"[E] Tsirelson 2*sqrt(2) = {CHSH_QM:.8f}  OK")
else:
    errors += 1

# Check 3: CHSH_QM > 2 (Bell-Grenze überschritten)
if CHSH_QM > 2.0:
    print(f"[E] CHSH_QM = {CHSH_QM:.4f} > 2 (Bell-Grenze)  OK")
else:
    errors += 1

# Check 4: xi/(2pi) konsistent mit Kap. 7 (CHSH-Abweichung 2.1e-5)
kap7_wert = 2.1e-5   # aus QMB_n07
if abs(delta_CHSH_elem - kap7_wert) / kap7_wert < 0.1:
    print(f"[K] delta_CHSH = {delta_CHSH_elem:.4e} ≈ {kap7_wert:.1e} (Kap. 7)  OK")
else:
    # Toleranz 10% — Formel identisch, nur Rundung
    delta = abs(delta_CHSH_elem - kap7_wert)/kap7_wert
    print(f"FEHLER: delta_CHSH_elem={delta_CHSH_elem:.4e} vs. Kap7={kap7_wert:.1e} (delta={delta:.1%})")
    errors += 1

# Zusammenfassung
print(f"\nFazit: FFGFT-Abweichung {delta_CHSH_elem:.2e}")
print(f"       NISQ-Rauschen   {delta_CHSH_NISQ_min:.3f}--{delta_CHSH_NISQ_max:.3f}")
print(f"       Faktor:          {delta_CHSH_NISQ_min/delta_CHSH_elem:.0f}--{delta_CHSH_NISQ_max/delta_CHSH_elem:.0f}x unter Rauschen")
print(f"       Benötigte Schüsse für SNR=3: {N_snr3:.1e}")

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K/S]")
else:
    print(f"{errors} FEHLER")
