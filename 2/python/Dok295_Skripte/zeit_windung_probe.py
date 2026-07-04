"""Dok 295 -- Zeit-Windung: Nichtschliessung und 75-Schliessung (eingefrorenes xi).
numpy-only. Deterministisch.

Prueft die algebraischen Tatsachen und den eingefrorenen Fall:
- 100 xi0 = 1/75, K_frak = 74/75, 1/(100 xi0) = 75
- eingefroren: Rotationszahl 74/75 rational -> Schliessung nach genau 75 Umlaeufen
"""
import numpy as np

xi0 = 1.0/7500.0
Kfrak = 1 - 100*xi0

print("exakte Tatsachen")
print("  100*xi0        =", 100*xi0, "  1/75 =", 1/75)
print("  K_frak         =", Kfrak,   "  74/75 =", 74/75)
print("  1/(100*xi0)    =", 1/(100*xi0))

# Eingefroren: pro Umlauf Vorschub K_frak (in Umlauf-Einheiten), Defekt d=1/75.
# Schliessung, wenn kumulierter Vorschub ganzzahlig -> m*K_frak in Z.
d = 100*xi0                       # Defekt je Umlauf
# kleinste Umlaufzahl P mit P*d in Z:  P*(1/75) in Z  -> P=75
P = 75
cum = (np.arange(1, P+1)*Kfrak) % 1.0
closes = np.argmin(np.abs(((np.arange(1,P+1)*Kfrak+0.5)%1.0)-0.5))  # naehe an ganzzahlig
print("\neingefrorener Fall")
print("  Defekt je Umlauf d =", d, " (=1/75)")
print("  Rotationszahl K_frak = 74/75 rational -> Periode P =", P)
print("  Vorschub nach 75 Umlaeufen (soll ganzzahlig=74):", round(75*Kfrak, 10))
assert abs(75*Kfrak - 74) < 1e-9
print("  -> schliesst nach genau 75 Umlaeufen, 75-zaehlige Struktur  [OK]")
