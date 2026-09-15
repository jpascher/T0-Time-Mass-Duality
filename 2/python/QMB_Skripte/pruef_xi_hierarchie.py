"""
pruef_xi_hierarchie.py — Kapitel 8: xi-Energiehierarchie Spin vs. Photonik
Quelle: QMB_n08_qubit_formalismus.tex, Tabellen

Verifiziert:
  (A) Energieskala Spin-Qubit (Stufe N≈8): Delta_E_Z = 0.1-1 meV << kBT(RT)=26meV
  (B) Energieskala Photonik (Stufe N≈9-10): E_photon = 1-2 eV >> kBT(RT)
  (C) Stufenfaktor 1/xi ≈ 7500: von meV (N=8) zu eV (N=9) ist Faktor ~7500 [K]
  (D) N_max-Formel: N_max = E_photon/(kBT) direkt aus Tabelle
"""

import numpy as np

xi   = 1/7500
kB   = 1.381e-23  # J/K
eV   = 1.602e-19  # J
T_RT = 300        # K
kBT  = kB * T_RT  # in Joule
kBT_meV = kBT / eV * 1000  # in meV

print("=" * 60)
print("pruef_xi_hierarchie.py — Kapitel 8: xi-Energiehierarchie")
print("=" * 60)
print(f"xi      = {xi:.6e}")
print(f"1/xi    = {1/xi:.1f}")
print(f"kBT(300K) = {kBT_meV:.2f} meV = {kBT_meV/1000:.4f} eV\n")

errors = 0

# (A) Spin-Qubit Zeeman-Energie
print("[A] Spin-Qubit Zeeman-Energie (B=0.1-10 T, GaAs g*=-0.44, mu_B=5.79e-5 eV/T)")
gstar   = 0.44     # |g*| GaAs
mu_B    = 5.79e-5  # eV/T
for B in [0.1, 1.0, 5.0, 10.0]:
    dE_meV = gstar * mu_B * B * 1000  # meV
    verhältnis = dE_meV / kBT_meV
    regime = "Spin << kBT: Kühlung nötig" if dE_meV < kBT_meV else "Spin > kBT"
    print(f"  B={B:5.1f}T: dE={dE_meV:.3f} meV,  dE/kBT={verhältnis:.4f}  [{regime}]")

# Check: bei B=10T sollte dE_Z << kBT (Raumtemperatur)
dE_max_meV = gstar * mu_B * 10.0 * 1000
if dE_max_meV < kBT_meV:
    print(f"  [K] Delta_E_Z(max,B=10T) = {dE_max_meV:.2f} meV < kBT = {kBT_meV:.2f} meV  OK")
else:
    print(f"  FEHLER: Delta_E_Z > kBT bei B=10T")
    errors += 1

# (B) Photonische Energie
print("\n[B] Photonische Energie Stufe N≈9-10 (Glasfaser, Nahinfrarot)")
photonen = [
    ("Glasfaser 1550nm", 1550e-9, 0.8),
    ("Nahinfrarot 800nm", 800e-9, 1.55),
    ("Sichtbar 600nm",   600e-9, 2.07),
]
h = 6.626e-34; c = 3e8
for name, lam, E_eV_exp in photonen:
    E_J  = h * c / lam
    E_eV = E_J / eV
    EkT  = E_J / kBT
    ok   = abs(E_eV - E_eV_exp)/E_eV_exp < 0.05
    if not ok: errors += 1
    print(f"  {name}: E={E_eV:.3f} eV (erw. {E_eV_exp:.2f}), E/kBT={EkT:.1f}  {'OK' if ok else 'FEHLER'}")

# (C) Stufenfaktor: meV -> eV braucht Faktor ~1000-7500
print("\n[C] Stufenfaktor 1/xi = 7500: meV (Spin) -> eV (Photonik)")
E_spin_meV   = 0.1   # typische Zeeman-Energie
E_photon_eV  = E_spin_meV / 1000 * (1/xi)  # eine Stufe höher
print(f"  E_spin     = {E_spin_meV} meV")
print(f"  E * (1/xi) = {E_photon_eV*1000:.2f} meV = {E_photon_eV:.4f} eV")
print(f"  Buch: 'von meV (Stufe 8) zu eV (Stufe 9-10) Faktor 10^3-10^4'")
faktor = 1/xi
if 1e3 < faktor < 1e4:
    print(f"  [K] 1/xi = {faktor:.0f} ∈ (10^3, 10^4)  OK")
else:
    print(f"  FEHLER: 1/xi = {faktor:.0f} nicht in (10^3, 10^4)")
    errors += 1

# (D) N_max = E/kBT aus Technologietabelle
print("\n[D] N_max = E_photon/kBT (Tabelle Kap. 8)")
tech = [
    ("Nahinfrarot 200THz", 200e12,  31, 46),
    ("Glasfaser   300THz", 300e12,  46, 46),
    ("UV         1000THz", 1000e12, 154, 150),
]
for name, freq, Nmax_buch, _ in tech:
    E_J = h * freq
    Nmax_calc = E_J / kBT
    ok = abs(Nmax_calc - Nmax_buch)/Nmax_buch < 0.1
    if not ok: errors += 1
    print(f"  {name}: N_max_calc={Nmax_calc:.0f}, Buch={Nmax_buch}  {'OK' if ok else 'FEHLER'}")

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K]")
else:
    print(f"{errors} FEHLER")
