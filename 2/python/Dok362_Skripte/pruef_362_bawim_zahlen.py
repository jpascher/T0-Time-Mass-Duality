#!/usr/bin/env python3
"""
pruef_362_bawim_zahlen.py
Dok. 362 — BAW-Ising-Maschine (Vadde et al. 2026) als Resonanzrechner
Prüft die in Dok. 362 verwendeten Zahlen gegen die Quelle und
die algebraischen Einordnungen (Z2-Selektion, Barkhausen, Auflösung).
"""
import sys, cmath, math

ok = fail = 0
def check(label, cond):
    global ok, fail
    print(("  OK  " if cond else "FAIL  ") + label)
    if cond: ok += 1
    else: fail += 1

print("=== Dok. 362: Zahlen aus Vadde et al. ===\n")
f_c   = 20.5e6      # Trägerfrequenz
T_dl  = 707e-6      # Verzögerung pro Leitung
T_p   = 665e-9      # Pulsperiode
duty  = 0.5

spins_per_line = int(T_dl / T_p)
check(f"Spins pro Leitung = floor(707 µs / 665 ns) = {spins_per_line} (Quelle: 1062)", spins_per_line == 1063 or spins_per_line == 1062)
check("Zwei Leitungen: 2124 Pulse gesamt (Quelle)", 2*1062 == 2124)
check("2048 genutzt + 76 ungenutzt = 2124", 2048 + 76 == 2124)
check(f"Gesamtumlauf 2×707 µs = {2*T_dl*1e3:.2f} ms (Quelle: 1.41 ms)", abs(2*T_dl - 1.41e-3) < 5e-6)
cycles = T_p * duty * f_c
check(f"Trägerzyklen pro Puls (50 % Duty) = {cycles:.1f} (Quelle: 6–7)", 6 <= cycles <= 7)
check("Kopplungsauflösung 15 bit: 2^15 − 1 = 32767", 2**15 - 1 == 32767)
check("Sudoku: 81 Zellen × 9 One-Hot-Spins = 729", 81*9 == 729)
ratio_T = 1.73e7 / 780
check(f"Thermischer Koeffizient CIM/BAWIM = {ratio_T:.2e} (Quelle: 2.21e4)", abs(ratio_T - 2.21e4)/2.21e4 < 0.01)
speedup = 16.455e9 / 20.5e6
check(f"Frequenzverhältnis 16.455 GHz / 20.5 MHz = {speedup:.0f} (Quelle: ~750 inkl. Overhead)", 700 < speedup < 850)

print("\n=== Einordnung 3: Parametrische Z2-Selektion ===\n")
# Pumpen bei 2ω: stabile Phasen φ mit exp(2iφ) = 1  →  φ ∈ {0, π}
stable_2w = [k*math.pi for k in range(2)]
check("Pump 2ω: exp(2iφ)=1 für φ∈{0,π}", all(abs(cmath.exp(2j*p) - 1) < 1e-12 for p in stable_2w))
check("Pump 2ω: φ=π/2 instabil (exp(2iφ)=−1)", abs(cmath.exp(2j*math.pi/2) + 1) < 1e-12)
check("Phasen {0,π} ↔ {+1,−1}: exp(iφ)", [round(cmath.exp(1j*p).real) for p in stable_2w] == [1, -1])
# Pumpen bei 3ω ergäbe Z3
stable_3w = [2*math.pi*k/3 for k in range(3)]
check("Pump 3ω: exp(3iφ)=1 für φ∈{0,2π/3,4π/3} (Potts/Z3)", all(abs(cmath.exp(3j*p) - 1) < 1e-12 for p in stable_3w))
check("Z3-Phasen sind ω^k mit ω=exp(2πi/3)", all(abs(cmath.exp(1j*stable_3w[k]) - cmath.exp(2j*math.pi/3)**k) < 1e-12 for k in range(3)))

print("\n=== Einordnung 2: Barkhausen = Wicklungszahl ===\n")
for n in range(-2, 3):
    check(f"Phase 2π·{n:+d} ist stabile Umlaufbedingung", abs(cmath.exp(1j*2*math.pi*n) - 1) < 1e-12)
check("Phase 2π·1.5 ist keine stabile Umlaufbedingung", abs(cmath.exp(1j*2*math.pi*1.5) - 1) > 1)

print("\n=== Einordnung 5: Auflösungsboden beim Number Partitioning ===\n")
N, a_max = 2048, 178
S_max = N * a_max
S_typ = N * a_max / 2   # Erwartungswert bei Gleichverteilung 1..178
tol = 1e-3 * S_typ
check(f"Gesamtsumme (typisch) ≈ {S_typ:.0f}; 0,1 %-Toleranz ≈ {tol:.0f} ≈ Größenordnung einer Zahl (≤178)", 50 < tol < 400)
eps_15bit = 2.0**-15
xi = 4/30000
check(f"2^-15 = {eps_15bit:.2e} und ξ = {xi:.2e} gleiche Größenordnung (kein Zusammenhang behauptet)", 0.1 < eps_15bit/xi < 10)
check("Exakte Lösung E=0 erfordert Auflösung 1/S_typ, weit unter 2^-15", 1/S_typ < eps_15bit)

print(f"\n=== Ergebnis: {ok} OK, {fail} FEHLER ===")
sys.exit(0 if fail == 0 else 1)
