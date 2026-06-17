# Dok280_Skripte — Rotverschiebung, z→Zeit-Übertragung, SFRD

Begleitskripte zu **Dok. 280** (Rotverschiebung in FFGFT: statisch, achromatisch,
und die z→Zeit-Übertragung). Kernpunkt: modellunabhängig ist nur z; die Umrechnung
z→Zeit setzt a(t) voraus (ΛCDM-Konstrukt). Alle drei Skripte erzeugen Diagramme.

## z_time_ffgft.py
Erzeugt **`280_z_time_ffgft.png`** (die in Dok. 280 eingebettete Grafik):
ΛCDM-Lookback (Expansion+Λ, H₀=67,4) vs. FFGFT/T0 statisch (1+z=e^(ξx) ⇒
Lichtlaufzeit = ln(1+z)/H₀, H₀=66,2). Marker: cosmic noon z≈1,9, FFGFT z\*≈875
(Dok. 267), ΛCDM z\*≈1100. matplotlib(Agg)+numpy.

## z_time_mapping.py
Allgemeinere Fassung: ΛCDM-Lookback vs. generischer statischer Benchmark
τ=ln(1+z)/H₀ (tired-light, ausdrücklich „illustrativ, nicht FFGFT"). Zeigt, dass
die z→Zeit-Abbildung modellabhängig ist. Erzeugt `z_time_mapping.png`.

## lilly_madau_v4.py
Lilly–Madau kosmische Sternentstehungsgeschichte (SFRD) auf der ΛCDM-Zeitachse
(„Time (G-yr)"), Madau–Dickinson-2014-Fit + JWST-Hoch-z-Punkte; für J. Nicholson
(IPI). Demonstriert: die SFRD-Alters-Achse ist ein ΛCDM-Konstrukt. Erzeugt
`lilly_madau_v4_timeaxis.png`.

Lauf: `python3 <skript>.py` (numpy + matplotlib).
