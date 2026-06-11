# Dok 275 — Skripte: Von ξ zu φ

## Dateien
- `ffgft_hlv_gap_v2.py` — Erste korrigierte Version: ξ=4/30000 (statt Q_FFGFT),
  analytischer T⁴-Laplacian, ξ-Rekursion → 1/φ (Ebene 3), N=600.
- `ffgft_hlv_gap_v3.py` — Finale Version: N=2000, endlicher T⁴-Graph
  (kNN, gleiche Methode wie HLV), Mini-Ensemble (3 Seeds),
  Schalenstruktur-Diskriminierung 1/φ vs Q_FFGFT.
- `ffgft_hlv_gap_v2.png`, `ffgft_hlv_gap_v3.png` — Ausgabediagramme.

## Kernergebnisse (v3, N=2000)
- k* = log(φ)/ξ ≈ 3609; r(3609) = 0,6179940 (Fehler 4,0×10⁻⁵ zu 1/φ,
  relativ 6,5×10⁻⁵). Frühere Angabe <10⁻⁹ war falsch (zirkulär) —
  korrigiert per unabhängiger Nachrechnung am 10.6.2026.
- FFGFT-T⁴-Graph: gap_CV = 1,68 ± 0,09 → außerhalb Null-Band [0,31, 1,05].
- HLV: gap_CV = 0,755 ≈ jittered-kubisch 0,755 → im Band
  (unabhängige Bestätigung von Krüger Run E).
- Schalen-Diskriminierung bei N=2000: Q_FFGFT (0,804) passt besser
  zur HLV-Schalenstruktur als 1/φ (0,949), Δ=0,145 — vorläufig.

## Heuristiken / Einschränkungen
- Schalen-Erkennung: 5%-Schwellwert (heuristisch; g(r) wäre robuster).
- Ensemble: 3 Seeds, illustrativ, nicht statistisch abgesichert.
- T⁴-Graph und HLV-Graph sind verschiedene Objekte; Vergleich qualitativ.

## Reproduktion
python3 ffgft_hlv_gap_v3.py  (benötigt numpy, scipy, matplotlib; ~2 min)
