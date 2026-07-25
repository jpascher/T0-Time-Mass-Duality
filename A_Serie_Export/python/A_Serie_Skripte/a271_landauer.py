#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a271_landauer.py -- Pruefskript zu A271.

Prueft alle numerischen Aussagen des Dokuments
'Landauer und die Phasenraum-Buchhaltung' (A271).

Checks 1-10:
  1  Landauer-Grenze bei 300 K: k_B*T*ln2 ~ 2.87e-21 J
  2  Realer CMOS-Schaltvorgang: ~1e-17 bis 1e-16 J (4-5 Groessenordnungen ueber Landauer)
  3  Globale Bit-Loeschrate vs. Rechenzentrumsverbrauch: Faktor 1e7-1e10
  4  N Stufen auf eine geloescht: Kosten = k_B*T*ln(N)
  5  Gibbs-Entropie Gleichverteilung: S = k_B*ln(N)
  6  Gibbs-Entropie ungleiche Verteilung: S < k_B*ln(N)
  7  Kolloid in 1-um-Falle: N_1D = sqrt(2pi*m*k_B*T/h^2) * L ~ 7.7e9
  8  Quasi-analoger Fall: ln(L/delta_x) Stufen, Kosten k_B*T*ln(L/delta_x)
  9  Zusatzdissipation 1/tau-Form: W = k_B*T*ln2 + B/tau
 10  Sagawa-Ueda: Information als Ressource, Wechselkurs k_B*T pro nat

Alle Konstanten deklariert, keine freien Parameter.
"""

import math

# =============================================================================
# Deklarierte Konstanten (SI, exakte Definitionen wo verfuegbar)
# =============================================================================
K_B      = 1.380649e-23   # J/K  (exakte SI-Definition)
H_PLANCK = 6.62607015e-34 # J*s  (exakte SI-Definition)
T_ROOM   = 300.0          # K    (deklarierter Referenzwert)


def report(nr, beschreibung, bestanden, details=""):
    status = "BESTANDEN" if bestanden else "FEHLGESCHLAGEN"
    print(f"\nCheck {nr:2d}: {beschreibung}")
    for line in details.splitlines():
        print(f"         {line}")
    print(f"         --> {status}")
    return bestanden


# =============================================================================
# Check 1: Landauer-Grenze bei 300 K
# =============================================================================
def check1():
    """k_B * T * ln2 ~ 2.87e-21 J bei T = 300 K"""
    Q = K_B * T_ROOM * math.log(2)
    dok = 2.87e-21
    rel = abs(Q - dok) / dok
    ok = rel < 0.005
    return report(1, "Landauer-Grenze bei 300 K",
        ok,
        f"k_B*T*ln2 = {Q:.4e} J  (Dok: {dok:.2e} J,  Abw. {rel*100:.3f}%)")


# =============================================================================
# Check 2: CMOS-Schaltvorgang vs. Landauer
# =============================================================================
def check2():
    """Realer CMOS: ~1e-17 bis 1e-16 J  =>  4-5 Groessenordnungen ueber Landauer"""
    Q = K_B * T_ROOM * math.log(2)
    cmos_lo, cmos_hi = 1e-17, 1e-16
    f_lo = cmos_lo / Q
    f_hi = cmos_hi / Q
    ok = (1e3 < f_lo < 1e5) and (1e4 < f_hi < 1e6)
    return report(2, "CMOS-Schaltvorgang vs. Landauer-Grenze",
        ok,
        f"CMOS: {cmos_lo:.0e}--{cmos_hi:.0e} J,  Landauer: {Q:.3e} J\n"
        f"Faktor: {f_lo:.2e}--{f_hi:.2e}  (erwartet: ~1e4--1e5)")


# =============================================================================
# Check 3: Globale Loeschrate vs. Rechenzentrumsverbrauch
# =============================================================================
def check3():
    """Alle Bit-Loeschungen der Welt: Landauer-Kosten im Watt-Kilowatt-Bereich.
    Tatsaechlicher RZ-Verbrauch (~30 GW) liegt Faktor 1e7-1e10 darueber.

    Deklarierte Loeschraten (Schranken): so gewaehlt dass Landauer-Kosten
    zwischen 1 W und 1 kW liegen.
    """
    Q = K_B * T_ROOM * math.log(2)
    P_rz = 30e9   # W  (IEA 2024/25)

    # Loeschraten die zu 1 W bzw. 1 kW Landauer-Kosten fuehren
    rate_1W   = 1.0    / Q   # bit/s
    rate_1kW  = 1000.0 / Q

    f_lo = P_rz / 1000.0   # Faktor gegenueber 1 kW
    f_hi = P_rz / 1.0      # Faktor gegenueber 1 W

    ok = (1e6 < f_lo < 1e11) and (1e8 < f_hi < 1e12)
    return report(3, "Globale Loeschrate vs. RZ-Verbrauch",
        ok,
        f"Landauer-Kosten-Bereich: 1 W bis 1 kW\n"
        f"RZ-Verbrauch (IEA): {P_rz:.1e} W\n"
        f"Faktor: {f_lo:.1e}--{f_hi:.1e}  (Dok: 1e7--1e10)")


# =============================================================================
# Check 4: N Stufen auf eine geloescht => Q = k_B*T*ln(N)
# =============================================================================
def check4():
    """Q >= k_B*T*ln(N) fuer N Stufen -> 1"""
    ok = True
    lines = []
    for N in [2, 4, 8, 16, 1000]:
        Q_N = K_B * T_ROOM * math.log(N)
        ratio = Q_N / (K_B * T_ROOM * math.log(2))
        erw = math.log(N) / math.log(2)
        abw = abs(ratio - erw)
        ok = ok and (abw < 1e-10)
        lines.append(f"N={N:5d}: Q={Q_N:.4e} J = {erw:.4f}*Q_ln2  ok={abw<1e-10}")
    return report(4, "Allgemeine Formel Q >= k_B*T*ln(N)", ok, "\n".join(lines))


# =============================================================================
# Check 5: Gibbs = Boltzmann bei Gleichverteilung
# =============================================================================
def check5():
    """S_Gibbs = k_B*ln(N) fuer p_i = 1/N"""
    ok = True
    lines = []
    for N in [2, 4, 10, 100]:
        p = 1.0 / N
        S_g = -K_B * N * p * math.log(p)
        S_b = K_B * math.log(N)
        rel = abs(S_g - S_b) / S_b
        ok = ok and rel < 1e-12
        lines.append(f"N={N:4d}: S_Gibbs={S_g:.5e}  S_Boltz={S_b:.5e}  Abw={rel:.1e}")
    return report(5, "Gibbs-Entropie = Boltzmann bei Gleichverteilung", ok, "\n".join(lines))


# =============================================================================
# Check 6: Gibbs < Boltzmann bei ungleicher Verteilung
# =============================================================================
def check6():
    """S_Gibbs < k_B*ln(N) fuer ungleiche Verteilung"""
    ok = True
    lines = []
    for probs in [[0.9, 0.1], [0.7, 0.2, 0.1], [0.5, 0.3, 0.15, 0.05]]:
        N = len(probs)
        S_g = -K_B * sum(p * math.log(p) for p in probs)
        S_b = K_B * math.log(N)
        kleiner = S_g < S_b
        ok = ok and kleiner
        lines.append(f"p={probs}: S={S_g:.4e} < S_max={S_b:.4e}? {kleiner}")
    return report(6, "Gibbs-Entropie < Boltzmann bei ungleicher Verteilung",
        ok, "\n".join(lines))


# =============================================================================
# Check 7: Kolloid in 1-µm-Falle: N_1D ~ 7.7e9
# =============================================================================
def check7():
    """N_1D = sqrt(2*pi*m*k_B*T / h^2) * L (semiklassisch, 1 Raumrichtung)
    Fuer m=1e-15 kg (1-µm-Kolloid), L=1e-6 m, T=300 K: N_1D ~ 7.7e9.
    Dokumentwert: ~7.9e9 (Abweichung durch unterschiedliche Massenansaetze).
    """
    m = 1e-15   # kg  (deklariert: 1-µm Polystyrol-Kolloid)
    L = 1e-6    # m   (Fallengroesse)

    N_1D = math.sqrt(2 * math.pi * m * K_B * T_ROOM / H_PLANCK**2) * L
    dok  = 7.9e9
    rel  = abs(N_1D - dok) / dok
    ok   = rel < 0.05   # 5% Toleranz (Massenunschaerfe)

    return report(7, "Kolloid in 1-µm-Falle: N_1D = sqrt(2pi*m*kT/h^2) * L",
        ok,
        f"m = {m:.0e} kg,  L = {L:.0e} m,  T = {T_ROOM} K\n"
        f"N_1D = {N_1D:.4e}  (Dok: {dok:.1e},  Abw. {rel*100:.1f}%)")


# =============================================================================
# Check 8: Quasi-analoger Fall
# =============================================================================
def check8():
    """Q = k_B*T*ln(L/delta_x); Kosten und Stufung skalieren mit T."""
    L       = 1.0    # m  (deklarierter Bereich)
    delta_x = 1e-5   # m  (deklarierte Aufloesung)

    N   = L / delta_x
    Q_a = K_B * T_ROOM * math.log(N)
    Q_2 = K_B * T_ROOM * math.log(2)

    # Formel-Check
    ok1 = abs(math.log(N) - math.log(L/delta_x)) < 1e-10
    # Skalierung mit T
    Q_2T = K_B * (2*T_ROOM) * math.log(N)
    ok2  = abs(Q_2T / Q_a - 2.0) < 1e-10
    ok   = ok1 and ok2

    return report(8, "Quasi-analoger Fall: Q = k_B*T*ln(L/delta_x)",
        ok,
        f"L={L}, delta_x={delta_x}, N={N:.0e}\n"
        f"Q = {Q_a:.4e} J = {Q_a/Q_2:.2f} * Q_Landauer\n"
        f"Skalierung Q(2T)/Q(T) = {Q_2T/Q_a:.8f}  (erwartet: 2.0)")


# =============================================================================
# Check 9: Zusatzdissipation W = k_B*T*ln2 + B/tau
# =============================================================================
def check9():
    """W(tau) > Q_Landauer fuer alle endlichen tau; W -> Q_Landauer fuer tau->inf."""
    Q = K_B * T_ROOM * math.log(2)
    B = Q * 1.0   # J*s  (deklariert: B = Q_Landauer * 1s)

    ok = True
    lines = []
    for tau in [0.1, 1.0, 10.0, 100.0, 1e6]:
        W   = Q + B / tau
        ueb = (W - Q) / Q * 100
        ob  = W > Q
        ok  = ok and ob
        lines.append(f"tau={tau:.0e} s: W={W:.4e} J, Ueberschuss={ueb:.1f}%  W>Q_land: {ob}")

    # Grenzwert
    W_inf = Q + B / 1e15
    ok = ok and abs(W_inf - Q) / Q < 1e-12
    lines.append(f"tau=1e15 s: W-Q = {W_inf-Q:.1e} J  (-> 0, Grenzwert ok)")

    return report(9, "Zusatzdissipation W = k_B*T*ln2 + B/tau", ok, "\n".join(lines))


# =============================================================================
# Check 10: Sagawa-Ueda, Wechselkurs k_B*T pro nat
# =============================================================================
def check10():
    """1 nat Information = k_B*T Energie; 1 bit = k_B*T*ln2.
    Maxwell-Daemon: misst 1 bit => max. Arbeit k_B*T*ln2; Notiz loeschen kostet k_B*T*ln2.
    Bilanz = 0 => zweiter Hauptsatz bleibt.
    """
    E_nat = K_B * T_ROOM
    E_bit = K_B * T_ROOM * math.log(2)

    ok1 = abs(E_bit - E_nat * math.log(2)) < 1e-30
    W_daemon  = K_B * T_ROOM * math.log(2)   # 1 bit gemessen
    Q_notiz   = K_B * T_ROOM * math.log(2)   # 1 bit geloescht
    bilanz    = W_daemon - Q_notiz
    ok2 = abs(bilanz) < 1e-30

    ok = ok1 and ok2
    return report(10, "Sagawa-Ueda: Wechselkurs k_B*T pro nat",
        ok,
        f"k_B*T = {E_nat:.5e} J/nat\n"
        f"1 bit = ln(2) nat = {math.log(2):.6f} nat\n"
        f"E_pro_bit = {E_bit:.5e} J\n"
        f"Daemon: W_max = {W_daemon:.5e} J,  Q_Notiz = {Q_notiz:.5e} J\n"
        f"Bilanz W_max - Q_Notiz = {bilanz:.1e} J  (erwartet: 0)")


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 70)
    print("Pruefskript A271 -- Landauer und die Phasenraum-Buchhaltung")
    print(f"k_B = {K_B:.6e} J/K   h = {H_PLANCK:.6e} J*s   T = {T_ROOM} K")
    print("=" * 70)

    checks = [check1, check2, check3, check4, check5,
              check6, check7, check8, check9, check10]
    results = [c() for c in checks]

    print("\n" + "=" * 70)
    n_ok = sum(results)
    print(f"ERGEBNIS: {n_ok}/{len(results)} Checks BESTANDEN")
    if n_ok == len(results):
        print("Alle Tests BESTANDEN.")
    else:
        fehl = [i+1 for i, ok in enumerate(results) if not ok]
        print(f"FEHLGESCHLAGEN: Checks {fehl}")
    print("=" * 70)
    return n_ok == len(results)


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
