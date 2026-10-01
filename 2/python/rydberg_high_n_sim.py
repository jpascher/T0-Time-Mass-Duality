"""rydberg_high_n_sim.py -- Wasserstoffniveaus mit fraktaler Daempfung, n = 7-20 (Dok. 022/035).

STATUS: Vorhersage ausgeschlossen (Dok. 035, R142). Die Energieformel
E_n*exp(-xi*n^2/D_f) ist durch die 1S-2S-Spektroskopie
ausgeschlossen: die relative Verschiebung waere von der Ordnung xi ~ 1e-4,
gemessen ist die 1S-2S-Frequenz auf ~1e-15 genau (bereits die 2. Ordnung
waere beobachtbar). Die Tabelle zeigt nur, was die Formel ergaebe, nicht
gueltige FFGFT-Werte.

Aktualisiert am 1.10.2026: xi = 1.340e-4 (an unbelegte CHSH-Daten angepasst,
entfernt) durch den Korpuswert xi = 4/30000 ersetzt; Kopfvermerk und Ausgabe
"Vorhersage ausgeschlossen" ergaenzt (vgl. Dok. 035 bzw. Dok. 190, R142, R143).
"""
import numpy as np

xi = 4/30000   # Korpuswert (vorher Fit-Wert 1.340e-4, entfernt)
D_f = 3 - xi
phi = (1 + np.sqrt(5)) / 2

def E_standard(n):
  return -13.6 / n**2

def E_ext(n, gen=0):
  return E_standard(n) * phi**gen * np.exp(-xi * n**2 / D_f)

ns = np.arange(7,21)
E_std = E_standard(ns)
E_ext_vals = E_ext(ns)

delta_ext = np.abs((E_ext_vals - E_std) / E_std * 100)

print('HINWEIS: Formel durch Wasserstoffspektroskopie (1S-2S) ausgeschlossen (Dok. 035, R142) -- keine gueltigen FFGFT-Werte')
print(f'xi = {xi:.6e} (4/30000)')
print('n | E_std (eV) | E_ext (eV) | Δ_ext (%)')
for i in range(len(ns)):
  print(f'{ns[i]} | {E_std[i]:.4f} | {E_ext_vals[i]:.4f} | {delta_ext[i]:.4f}')
