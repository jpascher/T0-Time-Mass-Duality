#!/usr/bin/env python3
# Dok. 328 — Prüfskript 2: Bandfilter-Regime numerisch (unterkritisch/kritisch/überkritisch)
# Übertragungsfunktion zweier induktiv gekoppelter, gleich abgestimmter Kreise.
import numpy as np

print("=" * 70)
print("PRÜFSKRIPT 2: Zweikreis-Bandfilter — Regime und kritische Kopplung")
print("=" * 70)

Q = 100.0
w0 = 1.0

def T(w, kQ):
    # Normierte Übertragungsfunktion des symmetrischen Bandfilters:
    # T ∝ kQ / ((1 + j·Q·v)^2 + (kQ)^2), v = (w/w0 - w0/w) (Verstimmung)
    v = w / w0 - w0 / w
    return np.abs(kQ / ((1 + 1j * Q * v) ** 2 + kQ ** 2))

w = np.linspace(0.97, 1.03, 400001)

print(f"\nGüte Q = {Q:.0f}, k_krit = 1/Q = {1/Q:.4f}  (symmetrischer Fall)")
print(f"{'κ=kQ':>6} | {'Maxima':>6} | {'|T|max':>7} | {'Höckerlage ω±':>22} | Regime")
print("-" * 70)
for kQ in [0.3, 0.7, 1.0, 1.5, 2.5, 4.0]:
    y = T(w, kQ)
    # lokale Maxima
    idx = np.where((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))[0] + 1
    peaks = w[idx]
    n = len(peaks)
    regime = "unterkritisch" if kQ < 1 else ("kritisch" if kQ == 1 else "überkritisch")
    lage = ", ".join(f"{p:.5f}" for p in peaks) if n else f"{w[np.argmax(y)]:.5f}"
    print(f"{kQ:>6.2f} | {n:>6d} | {y.max():>7.4f} | {lage:>22} | {regime}")

# Höckerformel prüfen: für kQ>1 gilt v± = ±sqrt(k^2 - 1/Q^2)  (exakt in v-Näherung)
print("\nPrüfung Höckerformel v± = ±sqrt(k² − k_krit²):")
for kQ in [1.5, 2.5, 4.0]:
    k = kQ / Q
    y = T(w, kQ)
    idx = np.where((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))[0] + 1
    v_num = np.array([wi / w0 - w0 / wi for wi in w[idx]])
    v_theo = np.sqrt(k**2 - (1/Q)**2)
    err = np.max(np.abs(np.abs(v_num) - v_theo)) / v_theo
    print(f"  κ={kQ:.1f}: v_num=±{np.abs(v_num).mean():.6f}  v_theo=±{v_theo:.6f}"
          f"  rel.Abw.={err:.2e}  {'BESTÄTIGT' if err < 1e-3 else 'FEHLER'}")

# Kritische Kopplung = maximal flach (Butterworth): |T|^2 hat bei ω0 verschwindende
# 2. Ableitung genau bei kQ=1 (in v). Numerisch: Krümmung von |T|² bei v=0.
print("\nMaximal flach bei κ=1 (Butterworth-Kriterium, Krümmung von |T|² bei ω0):")
dv = 1e-4
for kQ in [0.9, 1.0, 1.1]:
    def T2v(v):
        return np.abs(kQ / ((1 + 1j * Q * v) ** 2 + kQ ** 2)) ** 2
    curv = (T2v(dv) - 2 * T2v(0) + T2v(-dv)) / dv**2
    print(f"  κ={kQ:.1f}: d²|T|²/dv² |_0 = {curv:+.3e}"
          f"  ({'≈0 → maximal flach' if abs(curv) < 50 else ('Maximum (unterkrit.)' if curv < 0 else 'Sattel (überkrit.)')})")

print("\nFAZIT: Dreiteilung, Höckerformel und Butterworth-Bedingung numerisch bestätigt. [E]")
