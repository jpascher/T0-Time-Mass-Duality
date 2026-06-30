# Bell-Zustands-Wiederholbarkeit auf IBM Quantum Hardware

**Validierungsreport — 28. Mai 2026**
Johann Pascher · FFGFT (T0 / Zeit-Masse-Dualität)
ORCID 0009-0000-6518-4064

---

## Zusammenfassung

50 unabhängige Bell-Zustands-Messungen wurden auf IBM `ibm_kingston`
(Heron r2, 156 Qubit) durchgeführt, um die im Juni-2025-Report
aufgestellte Nebenvorhersage zu prüfen: dass die Lauf-zu-Lauf-Varianz
der Bell-Messung **unter** dem Niveau gewöhnlicher Quanten-Shot-Noise
liegt (Signatur einer deterministischen Evolution im T0-Bild).

**Ergebnis:** Die Wiederholbarkeits-Varianz ist statistisch **nicht
unterscheidbar** von gewöhnlicher Shot-Noise. Die Nebenvorhersage
„deterministisch reduzierte Varianz" wird durch diese Messung **nicht
gestützt**. Die Bell-Zustands-Erzeugung selbst gelingt mit hoher und
stabiler Fidelität (98,76 %).

Dieser Befund **überholt** die Wiederholbarkeits-Aussage des
Juni-2025-Reports (siehe Abschnitt 5). Die zentrale ξ-Vorhersage ist von
diesem Ergebnis **nicht betroffen** (siehe Abschnitt 6).

---

## 1. Aufbau

| Parameter | Wert |
|-----------|------|
| Backend | `ibm_kingston` (IBM Heron r2, 156 Qubit, heavy-hex) |
| Schaltkreis | Bell-Zustand \|Φ+⟩ = (\|00⟩+\|11⟩)/√2 (H, CNOT, measure_all) |
| Transpilation | optimization_level=3, seed_transpiler=42 (identisch über alle Läufe) |
| Transpilierte Tiefe | 7 (rz×5, sx×3, cz×1, measure×2) |
| Läufe | 50 unabhängig, sequentiell |
| Shots pro Lauf | 2048 |
| QPU-Zeit gesamt | ca. 200 s (Wallclock 743 s inkl. Warteschlange) |
| Datum | 28. Mai 2026, 14:15–14:28 UTC |
| Job-IDs | d8c4s047… (Lauf 1) bis d8c51o38… (Lauf 50), vollständig in CSV |

Identische Transpilation über alle Läufe ist methodisch entscheidend:
nur so misst die Lauf-zu-Lauf-Varianz die *Hardware-Wiederholbarkeit*
und nicht zufällige Transpilations-Unterschiede.

---

## 2. Ergebnisse

| Größe | Mittel | Varianz | Verhältnis zu Shot-Noise |
|-------|--------|---------|--------------------------|
| P(\|00⟩) | 0,509072 | 1,249·10⁻⁴ | **1,023** |
| P(\|11⟩) | 0,478535 | 1,184·10⁻⁴ | **0,970** |
| Bell-Fidelität | 0,987607 | — | sd = 0,002804 |

Shot-Noise-Referenz für Bin(N=2048, p=0,5)/N: 1,221·10⁻⁴.
Fehler-Outcomes (Leakage): P(\|01⟩)+P(\|10⟩) = 1,24 %.
Fidelitäts-Spanne über 50 Läufe: 0,9785 – 0,9927.

---

## 3. Statistische Prüfung der Kern-Hypothese

**Hypothese (Juni 2025):** Var(P) < Shot-Noise-Varianz (deterministische
Evolution reduziert die Lauf-zu-Lauf-Streuung).

**Test:** χ²-Test auf die Stichprobenvarianz. Unter der Nullhypothese
(reine Shot-Noise) ist (n−1)·s²/σ₀² ~ χ²(n−1).

| Größe | χ² (df=49) | Verhältnis s²/σ₀² | p (zweiseitig) |
|-------|-----------|-------------------|----------------|
| P(\|00⟩) | 50,14 | 1,023 | 0,856 |
| P(\|11⟩) | 47,52 | 0,970 | 0,933 |

Beide p-Werte sind groß (≫ 0,05). Die beobachtete Varianz ist mit reiner
Shot-Noise **vollständig verträglich**. Es gibt **keinen** statistisch
signifikanten Hinweis auf eine sub-Shot-Noise-Determiniertheit.

Die Verteilung der P(\|00⟩)-Werte ist normal (Shapiro-Wilk W=0,977,
p=0,42) — keine Ausreißer, kein Drift-Muster, ein sauberer Datensatz.

---

## 4. Warum der 10-Lauf-Vorbefund nicht hielt

Eine vorausgehende 10-Lauf-Messung (gleiche Hardware, gleicher Tag)
ergab ein Varianz-Verhältnis von **0,69** — scheinbar in T0-Richtung.
Schon damals war dieser Wert **nicht signifikant** (χ²-p = 0,57). Mit
50 Läufen ist das Verhältnis auf **1,02** zurückgewandert.

Das ist das erwartete Verhalten einer **Kleinstichproben-Fluktuation**:
aus 10 Punkten geschätzte Varianzen streuen breit; ein Verhältnis von
0,69 lag noch gut im Zufallsbereich. Die größere Stichprobe stabilisiert
die Schätzung und zeigt den wahren Wert ≈ 1,0. Dies unterstreicht, warum
die ursprünglichen **drei** Läufe (Juni 2025) für eine Varianz-Aussage
nicht ausreichten.

---

## 5. Verhältnis zum Juni-2025-Report

Der Juni-2025-Hardware-Validierungsreport nannte eine Lauf-zu-Lauf-
Varianz von 0,000248 (drei Läufe, `ibm_brisbane`, Eagle) und deutete
diese als „deterministisch reduziert" gegenüber der QM-Erwartung.

> ⚠️ **Überholt:** Diese Wiederholbarkeits-Aussage wird durch die
> vorliegende 50-Lauf-Messung nicht gestützt. Bei ausreichender
> Stichprobengröße und auf neuerer Hardware ist die Varianz mit
> gewöhnlicher Shot-Noise verträglich (Verhältnis 1,02; p = 0,86). Die
> drei Läufe von Juni 2025 waren statistisch zu wenig, um eine
> Varianz-Aussage zu tragen. Der Juni-Report bleibt als historischer
> Verlauf erhalten; für die Wiederholbarkeit gilt der hiesige Befund.

Was vom Juni-Report **bestätigt** wird: die hohe Bell-Fidelität und die
Lauffähigkeit von T0-Schaltkreisen auf Produktionshardware. Die Fidelität
ist hier sogar besser (98,76 % vs. 97,17 %), konsistent mit Heron r2 als
neuerer, fehlerärmerer Generation gegenüber der Eagle von 2025.

---

## 6. Was dieser Test über die zentrale ξ-Vorhersage NICHT aussagt

Die zentrale T0-Vorhersage ist eine Abweichung des CHSH-Wertes von der
Tsirelson-Schranke in der Größenordnung ξ ≈ 10⁻⁵ (≈ 10 ppm). Das aktuelle
NISQ-Rauschniveau (~2–3 %) liegt rund **280×** darüber. Dieser
Bell-Wiederholbarkeitstest war daher **nie** in der Lage, den ξ-Effekt
selbst zu messen — er prüfte ausschließlich die *Nebenvorhersage* zur
Wiederholbarkeit.

Der Negativbefund zur Wiederholbarkeit lässt die ξ-Vorhersage **unberührt**.
Diese bleibt mit aktueller Hardware nicht testbar und erfordert
fehlerkorrigierte Qubits (sub-ppm-Präzision) oder
Zero-Noise-Extrapolation.

---

## 7. Systematischer Nebenbefund: NISQ-Auslese-Asymmetrie

P(\|00⟩) = 0,509 liegt signifikant **über**, P(\|11⟩) = 0,479
signifikant **unter** dem Idealwert 0,5 (t = +5,7, p = 6·10⁻⁷ bzw.
t = −14,0, p = 1·10⁻¹⁸). Dies ist die bekannte NISQ-Auslese-Asymmetrie
(der Zustand \|0⟩ wird zuverlässiger gemessen als \|1⟩), ein
Hardware-Artefakt — **kein** T0-Effekt. Bemerkenswert: diese Asymmetrie
(~1–2 %) ist selbst um Größenordnungen größer als jeder vorhergesagte
ξ-Effekt, was die Notwendigkeit fehlerkorrigierter Hardware für den
eigentlichen Test unterstreicht.

---

## 8. Bewertung

- **Methodik:** sauber. 50/50 Läufe erfolgreich, identische
  Transpilation, vollständiges Job-ID-Logging, normalverteilte Daten,
  reproduzierbar über die in der CSV hinterlegten Job-IDs.
- **Kern-Hypothese (Wiederholbarkeit):** nicht gestützt. Varianz =
  Shot-Noise.
- **Bell-Fidelität:** 98,76 %, besser als Juni 2025.
- **ξ-Vorhersage:** unberührt, mit dieser Methode nicht testbar.

Ein Negativbefund für eine Nebenvorhersage, ehrlich dokumentiert, ist
ein Beitrag — er grenzt ab, was FFGFT auf heutiger Hardware behaupten
kann und was nicht.

---

## Anhang: Reproduktion

Skript: `t0_bell_repeatability_stage1.py` (50 Läufe, NUM_RUNS=50).
Rohdaten: `bell_repeatability_2026.csv` (50 Zeilen, alle Job-IDs).
Backend: `ibm_kingston`. Jeder Lauf ist über seine Job-ID im
IBM-Quantum-Dashboard nachprüfbar.

Unabhängige Reproduktion ausdrücklich erwünscht: gleiches Skript,
beliebiger IBM-Quantum-Account, ~3–4 min QPU-Zeit für 50 Läufe.

---

# Anhang B: CHSH-Parameter-Messung (Stufe 2)

**28. Mai 2026 · ibm_kingston (Heron r2, 156 Qubit)**

## B.1 Aufbau

Die erste echte CHSH-Parameter-Messung auf Hardware in diesem Korpus.
Im Gegensatz zur Bell-Wiederholbarkeit (eine Messbasis) verwendet CHSH
vier Winkel-Einstellungen und berechnet den S-Parameter aus Korrelatoren.

| Parameter | Wert |
|-----------|------|
| Winkel Alice | a = 0°, a' = 45° |
| Winkel Bob | b = 22,5°, b' = −22,5° |
| Messungen | 15 (je 4 Einstellungen × 2048 Shots) |
| Korrelator | E = [N₀₀ − N₀₁ − N₁₀ + N₁₁]/N |
| S-Kombination | S = E(a,b) + E(a,b') + E(a',b) − E(a',b') |
| Job-IDs | vollständig in chsh_stage2_2026.csv (60 Jobs) |

## B.2 Ergebnis

| Größe | Wert |
|-------|------|
| **Mittel S** | **2,7396 ± 0,0071** |
| Standardabweichung | 0,0274 |
| Spanne (min/max) | 2,6855 / 2,7891 |
| Tsirelson-Schranke 2√2 | 2,8284 |
| Klassische Schranke | 2,0000 |
| Erreichter Anteil von Tsirelson | **96,9 %** |
| Abweichung von 2√2 | −3,14 % |
| mittlere Korrelator-Stärke | 0,685 (ideal: 0,707) |

## B.3 Bewertung

**Bell-Verletzung zweifelsfrei.** S = 2,74 liegt **104 σ** über der
klassischen Schranke von 2. Lokaler Realismus ist ausgeschlossen; die auf
dem Gerät erzeugte Verschränkung ist genuin. Mit 96,9 % der
Tsirelson-Schranke ist dies ein für NISQ-Hardware ausgezeichnetes Resultat.

**Die −3,14 %-Lücke ist Dekohärenz, nicht ξ.** Die mittlere
Korrelator-Stärke 0,685 statt ideal 0,707 entspricht ~1,5 % Gate- und
Auslesefehler — die bekannte NISQ-Charakteristik. Der T0-ξ-Effekt liegt
bei ~10⁻⁵ (0,001 %), also rund **3000× kleiner** als die gemessene Lücke.
Diese Messung kann ξ daher **nicht** auflösen, in voller Übereinstimmung
mit der bekannten Rauschanalyse (NISQ ~280× über dem ξ-Signal).

**Was dieser Datensatz leistet:** Er ist der erste hardware-gemessene,
vollständig mit Job-IDs dokumentierte CHSH-Wert dieses Korpus. Er ersetzt
unbelegte CHSH-Behauptungen früherer interner Dokumente durch einen
reproduzierbaren Messwert: S = 2,74 auf Heron r2, ξ-Effekt darunter,
nicht auflösbar mit gegenwärtiger Hardware.

## B.4 Hinweis zur Auswertung

Der erste Auswertungslauf des Skripts verwendete eine zu den gewählten
Winkeln **nicht passende** Vorzeichenkombination der vier Korrelatoren und
ergab fälschlich S ≈ 0. Die Rohdaten (alle vier Korrelatoren pro Messung)
waren korrekt gemessen und gespeichert; die Korrektur der Kombination zu
S = E(a,b) + E(a,b') + E(a',b) − E(a',b') liefert aus **denselben
Hardware-Daten** den hier berichteten Wert S = 2,7396. Kein erneuter
Hardware-Lauf war nötig. Das korrigierte Skript ist t0_chsh_stage2.py.

## B.5 Budget

CHSH-Messung: 4 min QPU-Zeit (60 Jobs). Zusammen mit der 50-Lauf-
Bell-Messung (2 min) wurden 6 von 10 min des 28-Tage-Zyklus verbraucht.
