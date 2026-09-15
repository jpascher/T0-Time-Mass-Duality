"""
pruef_pbit_barrier.py — Kapitel 11: p-Bit Arrhenius-Gesetz
Quelle: QMB_n11_hardware.tex

p-Bit: tau = tau_0 * exp(U / kBT)
U = K_u * V  (Stoner-Wohlfarth Anisotropieenergie)
Bei 22 nm und weichmagnetischem Material sollte tau im ns-ms Bereich liegen.

FFGFT-Einordnung: 22nm = L_8 (xi-Stufe 8); dort ist tau ~ 1 ns bei K_u ~ 1e4 J/m^3
"""

import numpy as np

kB    = 1.381e-23  # J/K
T     = 300        # K (Raumtemperatur)
tau_0 = 1e-9       # s (attempt-time, typisch 1 ns)
xi    = 1/7500
ell_P = 1.616e-35
L_0   = xi * ell_P

def xi_stufe(r): return np.log(r/L_0) / np.log(1/xi)
def vol_sphere(d): return (4/3) * np.pi * (d/2)**3  # d = Durchmesser

print("=" * 60)
print("pruef_pbit_barrier.py — Kapitel 11: p-Bit Arrhenius")
print("=" * 60)
print(f"T = {T} K,  tau_0 = {tau_0:.1e} s\n")

errors = 0

# Gitter: (K_u, r_nm) -> tau
print("[A] tau = tau_0 * exp(K_u*V / kBT) bei verschiedenen K_u und r")
print(f"  {'K_u [J/m3]':>12} {'r [nm]':>8} {'N-Stufe':>8} {'U/kBT':>8} {'tau [s]':>12}")
print("  " + "-"*55)

K_u_liste = [1e3, 1e4, 5e4, 1e5]
r_liste   = [10e-9, 22e-9, 50e-9]

for r in r_liste:  # r ist Durchmesser
    N = xi_stufe(r)
    V = vol_sphere(r)  # r = Durchmesser
    for K_u in K_u_liste:
        U     = K_u * V
        UkBT  = U / (kB * T)
        if UkBT > 700:
            tau_s = ">>1e300"
            tau_ok = False
        else:
            tau   = tau_0 * np.exp(UkBT)
            tau_s = f"{tau:.3e}"
            tau_ok = True
        print(f"  {K_u:>12.1e} {r*1e9:>8.1f} {N:>8.3f} {UkBT:>8.2f} {tau_s:>12}")

# Kerncheck (B): 22nm, K_u=1e4 J/m^3 -> tau im ns-µs Bereich (p-Bit-Regime)
print("\n[B] Kerncheck: 22nm, K_u=1e4 J/m^3 -> p-Bit-Regime (tau ~ ns bis ms)")
d22 = 22e-9  # Durchmesser
V22 = vol_sphere(d22)
K_u_pbit = 1e4
U22  = K_u_pbit * V22
UkT22 = U22 / (kB * T)
tau22 = tau_0 * np.exp(UkT22)
N22   = xi_stufe(d22)
print(f"  d = 22 nm (Durchmesser) = L_8 (N = {N22:.3f})")
print(f"  K_u = {K_u_pbit:.0e} J/m^3  (weichmagnetisch)")
print(f"  V = {V22:.4e} m^3")
print(f"  U/kBT = {UkT22:.4f}")
print(f"  tau = {tau22:.3e} s")

# p-Bit-Fenster: tau zwischen 1ns und 1s
if 1e-9 <= tau22 <= 1.0:
    print(f"  [K] tau im p-Bit-Fenster [1ns, 1s]  OK")
else:
    print(f"  FEHLER: tau = {tau22:.3e} s ausserhalb p-Bit-Fenster")
    errors += 1

# Vergleich: K_u=4.5e5 J/m^3 (hartmagnetisch) -> Overflow
print("\n[C] Hartmagnetisch K_u=4.5e5 J/m^3 bei 22nm -> U/kBT >> 1 (klassisches Bit)")
K_u_hard = 4.5e5
U_hard = K_u_hard * vol_sphere(d22)
UkT_hard = U_hard / (kB * T)
print(f"  U/kBT = {UkT_hard:.1f}  -> tau = exp({UkT_hard:.0f}) = astronomisch gross")
if UkT_hard > 100:
    print("  [K] K_u=4.5e5 ergibt klassisches (stabiles) Bit, kein p-Bit  OK")
else:
    errors += 1; print("  FEHLER")

# Check N-Stufe 22nm = 8.00
print(f"\n[K] 22 nm = L_8: N = {N22:.4f}  {'OK' if abs(N22-8)<0.05 else 'FEHLER'}")
if abs(N22 - 8) >= 0.05:
    errors += 1

print("\n" + "=" * 60)
if errors == 0:
    print("Alle Checks bestanden [K]")
else:
    print(f"{errors} FEHLER")
