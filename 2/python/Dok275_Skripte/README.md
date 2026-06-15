# Dok 275 — Skripte: Von ξ zu φ

## ⚠ Versionshinweis (11. Juni 2026)
`ffgft_hlv_gap_v4.py` ist die **gültige** Fassung. v2/v3 bleiben als
dokumentierte Fehlerstände im Archiv (Audit P. Stoychev, IPI, 11.6.2026):
v3 hatte (a) Punktduplikate im T⁴-Graphen (729/2000 unique,
λ_max=2,5×10¹²), (b) einen Seed-Bug in hlv_points (Ensemble war 3×
dieselbe Rechnung), (c) einen strukturell verzerrten Schalen-Detektor
für Ziele < 1. Die v3-Resultate gap_CV=1,68 (T⁴ außerhalb) und
Δ=0,145 (Schalen-Diskriminierung) sind **widerrufen**.

## v4-Endergebnisse (N=2000, 3 Seeds, dimensions-gematchte Nulls)
- 4D-Sektor: FFGFT T⁴ gap_CV = 1,329±0,025 — **im** Band [0,690, 2,406]
  (4D isotrop-kubisch 2,406 / jittered 0,690 / random 0,740)
- 3D-Sektor: HLV gap_CV = 0,710±0,008 — **im** Band [0,675, 0,978]
- Schalen: nur Ziele > 1 zulässig; err(φ)_HLV = 0,257
- k*(c)-Tabelle: k* existiert für jedes Ziel — P35 greift
- **Netto: keine Separation; verstärkt Krüger Run E.**

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
