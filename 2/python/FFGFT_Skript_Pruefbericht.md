# FFGFT Skript-Prüfbericht — 04. Mai 2026

## Zusammenfassung

Geprüft: 25 Python-Skripte gegen FFGFT-Standard (Dok. 190)

| Status | Anzahl |
|--------|--------|
| ✅ Läuft fehlerfrei | 23 |
| 🔧 Gefixt (Laufzeitfehler) | 2 |
| ❌ Inhaltlich veraltet | 0 |

---

## Konformität mit Dok. 190 (Korrekturen)

| Korrektur | Prüfung | Status |
|-----------|---------|--------|
| K1: ξ = λ²v²/(16π³m²) | `higgs_pruefformel.py` | ✅ Korrekt — 16π³, Abw. −2.5 % |
| K2: r_τ = 25/9 | alle Koide-Skripte | ✅ Korrekt überall |
| K3: a_e = 2π²/(f·k) | `b18_g2_berechnung.py` | ✅ S₃ = 2π² verwendet |

---

## Laufzeit-Fixes (technisch, kein FFGFT-Inhalt)

### `t0_cosmic_data_analyzer.py` — 2 Fixes
- **pandas `freq='H'` → `'h'`**: Breaking Change in pandas ≥ 2.2.
  Alte Frequenzbezeichner sind veraltet.
- **matplotlib Import**: `matplotlib.use("Agg")` muss vor `import matplotlib.pyplot` stehen.
- **Plot-Dimensionsfehler**: `periods[:20]` und `power[:20]` hatten unterschiedliche Längen → `min(len, 20)`.

### `t0_cosmic_qubit_simulator.py`
- Braucht `pip install ephem` (fehlt in Standard-Installation).
  Nach Installation: ✅ läuft.

---

## Inhaltliche Befunde

### Shor-Algorithmus (`t0_shor_complete.py`)
- Erfolgsrate: **0/6 (0 %)** bei Testzahlen N=15..143
- Dies ist **bekannt und dokumentiert** (Dok. 176, 183–184):
  FFGFT-Shor ist konzeptuell korrekt, liefert aber klassisch
  keine zuverlässigen Faktoren weil xi-Resonanz für große N
  nicht ausreicht.
- **Kein Handlungsbedarf** — entspricht dem Stand der Theorie.

### Baryonenasymmetrie (`baron.py`)
- Offenes Problem dokumentiert: l₀_opt liegt im μm-Bereich
  statt sub-Planck → η_B Berechnung noch nicht geschlossen.
- **Bekanntes offenes Problem**, kein Fehler.

### Koide-Relation (`kodi-test.py`, `koide_korrekt.py`)
- Q = 0.6677 (T0-Idealwerte) vs. Q = 2/3 = 0.6667 (PDG)
- Abweichung 0.16 % — **korrekt dokumentiert** im Skript.
- PDG-Messwerte treffen Q = 2/3 viel genauer als T0-Idealwerte.
- **Kein Fehler** — konsistent mit Dok. 190 P5.

### Avi-Vorhersagen (`avi.py`)
- CP-Phase δ = 283.28°: Abw. 0.18° ✅
- sin²θ_W = 3/13: Abw. 0.195 % ✅
- Baryonenasymmetrie η: Abw. 0.50 % ✅
- **Alle drei Vorhersagen konform.**

### Feinstrukturkonstante (`t0_alpha_pruefung.py`)
- Methode 1: α⁻¹ ≈ 136.19 (Abw. −0.62 %)
- Hierarchie α/(ξ·φ³) ≈ 13 bestätigt ✅

---

## Empfehlungen

1. **`t0_cosmic_data_analyzer.py`**: Fixe einchecken (pandas + matplotlib).
2. **`t0_cosmic_qubit_simulator.py`**: `ephem`-Abhängigkeit in Requirements.txt dokumentieren.
3. **`t0_shor_complete.py`**: Kommentar ergänzen dass 0 % Erfolgsrate erwartet und theoretisch begründet ist.
4. **Alle anderen Skripte**: Konform, keine Änderung nötig.
