"""
pruef_dekohaerenz_xi.py — Kapitel 10: Dekohärenz-Skalierung über xi_Higgs
Quelle: QMB_n10_spin_qubit.tex

Aussage: T2(Exziton CdSe-QD) ~ 10 ps
         T2(Spin-Qubit Si)    ~ 10 ms
Differenz: 9 Größenordnungen.
FFGFT: xi_Higgs ≈ 1.038e-5; zwei Hierarchiestufen = xi_Higgs^2
log10(xi_Higgs^(-2)) = 2 * log10(1/xi_Higgs) = 2 * 4.984 = 9.97 GO
Übereinstimmung mit beobachteten 9 GO: [K]
"""

import numpy as np

xi_Higgs = 1.038e-5

T2_exziton = 10e-12   # 10 ps (CdSe-QD)
T2_spin_si = 10e-3    # 10 ms (Spin-Qubit Si)

GO_gemessen = np.log10(T2_spin_si / T2_exziton)
GO_ffgft    = 2 * np.log10(1 / xi_Higgs)

print("=" * 60)
print("pruef_dekohaerenz_xi.py — Kapitel 10: Dekohärenz-Skalierung")
print("=" * 60)
print(f"xi_Higgs          = {xi_Higgs:.3e}")
print(f"T2 Exziton        = {T2_exziton:.1e} s  (10 ps)")
print(f"T2 Spin-Si        = {T2_spin_si:.1e} s  (10 ms)")
print(f"Gemessene GO      = {GO_gemessen:.2f}")
print(f"FFGFT-Vorhersage  = {GO_ffgft:.4f}  (2 * log10(1/xi_Higgs))")

errors = 0
toleranz = 1.5   # ±1.5 Größenordnungen (Buch: "übereinstimmend")

delta = abs(GO_ffgft - GO_gemessen)
if delta < toleranz:
    print(f"\n[K] Abweichung = {delta:.3f} GO < {toleranz} GO  OK")
else:
    print(f"\nFEHLER: Abweichung = {delta:.3f} GO >= {toleranz} GO")
    errors += 1

# Zusatz: Einzelne log10-Werte
print(f"\nlog10(1/xi_Higgs) = {np.log10(1/xi_Higgs):.4f}")
print(f"Zwei Stufen       = {GO_ffgft:.4f} GO ≈ 9.97 GO (Buch)")

# Tabelle T1/T2 aus Buch
print("\n[E] Tabelle T1/T2 (Buch Kap. 10, etablierte Physik)")
systeme = [
    ("Elektron-Spin GaAs", 1e-3,   10e-9,   "Kernspin-Bad"),
    ("Exziton CdSe-QD",   1e-9,   10e-12,  "Phonon-Streuung"),
    ("Spin-Qubit Si",      1.0,    10e-3,   "isotrop. gereinigt"),
]
print(f"  {'System':22} {'T1':>10} {'T2':>10} {'T2<=2T1':>8}")
for name, T1, T2, mech in systeme:
    ok = T2 <= 2 * T1
    if not ok: errors += 1
    print(f"  {name:22} {T1:>10.1e} {T2:>10.1e} {'OK' if ok else 'FEHLER':>8}")

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K]")
else:
    print(f"{errors} FEHLER")
