# FFGFT / T0-Zeit-Masse-Dualität — Berechnungsskripte

**Johann Pascher** · Oberösterreich, Austria  
GitHub: [jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
Zenodo: [10.5281/zenodo.18834145](https://doi.org/10.5281/zenodo.18834145)

---

## Übersicht

Dieses Paket enthält Python-Skripte zur numerischen Validierung der
**FFGFT (Fundamentale Fraktale Geometrische Feldtheorie)**, auch bekannt als
**T0-Zeit-Masse-Dualität**.

Das zentrale Konzept der Theorie: Alle Naturkonstanten und Teilchenmassen
folgen aus einem einzigen dimensionslosen Parameter

$$\xi = \frac{4}{3} \times 10^{-4}$$

der seinerseits aus dem Higgs-Feld ableitbar ist (Dok. 049, 190).

---

## Kern-Skripte (Hauptverzeichnis)

### 1. `calc_De.py` — Hauptrechner v3.5

Berechnet **9 Teilchenmassen** und **47 physikalische Konstanten**
aus nur drei Eingabewerten: $\xi$, $\ell_P$, $E_0$.

**Ergebnisse:**
- Durchschnittlicher Massenfehler: **0,84 %**
- Durchschnittlicher Konstantenfehler: **0,0334 %**
- Beste Einzelvorhersage: $R_\text{gas}$ mit 0,0000 %

**Enthaltene Korrekturen (v3.5):**
- Tau-Vorfaktor korrigiert: $r_\tau = 8/3 \to 25/9$ (Dok. 190, Korrektur K2)
- $n_0$ (Loschmidt): Einheitenfehler behoben (L → m³)
- $\Lambda$: kein Vergleich mit ΛCDM-Referenzwert (verschiedene Kosmologie-Modelle)
- $L_0 = \xi \cdot \ell_P$ und $t_0 = L_0/c$ als Ausgabewerte ergänzt

**Ausgabe:**
```
Berechnete Konstanten gesamt: 47
Durchschnittlicher Massenfehler:      0.84 %
Durchschnittlicher Konstantenfehler:  0.0334 %
```

**Verwendung:**
```bash
python calc_De.py
```
Erzeugt zusätzlich `T0_berechnungsdaten.txt` und `T0_berechnungen.json`.

---

### 2. `calc-h-berechnug.py` — Kalibrierungsprüfung $\hbar$

Leitet $\hbar$ aus dem Higgs-Feld über $\xi$ her und prüft die interne
Konsistenz der Theorie.

**Ableitungskette:**
$$\xi_\text{Higgs} = \frac{\lambda_h^2 \, v^2}{16\pi^3 \, m_h^2}
\;\longrightarrow\; L_0 = \xi \cdot \ell_P
\;\longrightarrow\; \hbar \sim \sqrt{\xi} \cdot \ell_P \cdot c$$

**Methodischer Hinweis:**  
Da $\xi$ der einzige freie Parameter ist, ist
diese Rechnung keine Zirkularität, sondern eine **Kalibrierungsprüfung**:
Stimmt $\xi_\text{Higgs}$ (aus Higgs-Parametern berechnet) mit
$\xi_\text{T0}$ (geometrischer Sollwert) überein?
Die $\hbar$-Abweichung entspricht stets der halben $\xi$-Abweichung
(wegen $\sqrt{\xi}$) — das ist der beabsichtigte Konsistenztest.

**Ergebnis:**
```
xi_Higgs   = 1.2994e-04  (Abw. -2.54 % vom T0-Sollwert)
hbar-Abw.  = -1.28 %     (= halbe xi-Abweichung — Konsistenz OK)
```

---

### 3. `calc-teilchen-untergrenze.py` — Untergrenzen der Teilchenmassen

Berechnet drei Arten von Massenuntergrenzen in FFGFT:

| Typ | Formel | Wert |
|-----|--------|------|
| Kosmologisches Minimum | $m_\text{min} = \hbar H_0 / c^2$ | $1{,}49 \times 10^{-33}$ eV |
| Leichtestes massives Teilchen | $m_{\nu_e} = \xi^2 \cdot m_e$ | $9{,}08$ meV |
| xi-Skalenleiter | $m_n = \xi^n \cdot m_e$ | diskret, $n = 0, 1, 2, 3, \ldots$ |

**Neutrino-Formel:**
$$m_{\nu_i} = r_i \cdot \xi^2 \cdot m_e$$

| Neutrino | $r_i$ | $m_{\nu_i}$ | PDG-Limit |
|----------|--------|-------------|-----------|
| $\nu_e$  | $1$    | 9,08 meV    | < 45 meV (KATRIN) |
| $\nu_\mu$| $16/5$ | 29,07 meV   | < 190 keV |
| $\nu_\tau$| $25/9$ | 25,23 meV  | < 18,2 MeV |
| **Summe**|        | **63,4 meV**| **< 120 meV ✓** |

---

### 4. `calc-resonanz-leiter.py` — Vollständige Resonanz-Leiter

Berechnet alle 12 Fermionen (Leptonen + Quarks + Neutrinos) mit
exakter Bruch-Arithmetik (`fractions.Fraction`).

**Yukawa-Formel:**
$$m_i = r_i \cdot \xi^{p_i} \cdot v$$

**Exponent-Struktur** (Schrittweite $\Delta p = 1/3$):

| $p$ | Teilchen |
|-----|----------|
| $-1/3$ | Top |
| $1/2$  | Bottom |
| $2/3$  | Tau, Charm |
| $1$    | Myon, Strange |
| $3/2$  | Elektron, Up, Down |
| $\xi^2 \cdot m_e$ | Neutrinos |

---

## Weitere Skripte (`2/python/`)

### Gravitationskonstante und Feldtheorie

#### `G_drei_formeln_bedeutung.py`
Vergleicht drei verschiedene FFGFT-Herleitungen der Gravitationskonstante $G$
und analysiert ihre geometrische Bedeutung im Torus-Modell.
Gibt an, welche Formel den kleinsten Fehler gegenüber CODATA liefert.

#### `c1_geometrisch.py`
Geometrische Ableitung der Kopplungskonstante $C_1$ aus der Torus-Topologie.
Verbindet $\xi$, $\ell_P$ und $c$ in der FFGFT-Grundformel.

#### `Yang-Mills.py`
Prüft die Konsistenz der FFGFT-Feldstruktur mit Yang-Mills-Eichtheorie.
Untersucht ob die Torsionsgeometrie die Yang-Mills-Gleichungen erfüllt.

---

### Kosmologie

#### `H0.py`
Leitet den Hubble-Parameter $H_0$ aus $\xi$ und der kosmologischen
Torus-Geometrie her. Vergleich mit Planck-CMB- und SH0ES-Messungen.
Adressiert die Hubble-Spannung im FFGFT-Rahmen.

#### `t0_cosmic_data_analyzer.py`
Analysiert kosmologische Beobachtungsdaten (CMB, BAO, Supernovae Ia)
auf Konsistenz mit dem FFGFT-Torus-Modell.
Vergleich: $\Lambda$CDM vs. FFGFT-Kosmologie.

#### `t0_cosmic_error_correction.py`
Korrigiert systematische Fehler in kosmologischen Datensätzen,
die durch das FFGFT-Projektionsprinzip entstehen:
Fraktale Lichtpfade werden auf Geraden projiziert —
dieser Fehler wird quantifiziert und korrigiert.

#### `t0_cosmic_qubit_simulator.py`
Simuliert Qubit-Operationen auf der kosmologischen $\xi$-Skalenstufe.
Verbindet Quanteninformation (Dok. 173–176) mit der kosmologischen
Torus-Struktur.

#### `max-mass.py`
Berechnet die maximale Masse/Energie die in FFGFT möglich ist,
bevor $t_0$ als Untergrenze erreicht wird.
Erzeugt `max_masse_pruefung.png`.

---

### Anomales magnetisches Moment ($g$-$2$)

#### `b18_g2_berechnung.py`
Vollständige Berechnung des anomalen magnetischen Moments für
Elektron, Myon und Tau im FFGFT-Rahmen.
Verwendet den korrigierten Vorfaktor $S_3 = 2\pi^2$ (Dok. 190, K3).

#### `b18_vollstaendige_herleitung.py`
Vollständige analytische Herleitung der $g$-$2$-Formel aus der
Torus-Geometrie. Zeigt alle Zwischenschritte von $\xi$ bis $a_e$.

---

### Koide-Formel und Leptonenmassen

#### `kodi.py` / `kodi-test.py`
Hauptimplementierung der Koide-Relation $Q = 2/3$ im FFGFT-Rahmen.
`kodi-test.py`: Automatisierte Assertions auf alle drei Leptonmassen.

#### `koide_korrekt.py`
Verifiziert die korrigierten Vorfaktoren ($r_\tau = 25/9$, Dok. 190 K2)
gegen PDG-Werte 2022. Gibt Abweichung für jede Leptongenerierung aus.

#### `koide_e0_test.py`
Testet die Abhängigkeit der Koide-Relation vom Vakuumerwartungswert $E_0 = v$.
Sensitivitätsanalyse: Wie ändert sich $Q$ bei kleiner $\xi$-Variation?

#### `koide_kfrak_test.py`
Untersucht den Einfluss des fraktalen Korrekturfaktors $K_\text{frak}$
auf die Koide-Relation. Verbindet $g$-$2$ und Koide in einem Test.
Erzeugt `koide_kfrak_test.png`.

#### `koide_test.py`
Schnelltest: Koide-Konsistenz für aktuelle PDG-Werte.
Gibt $Q$, Abweichung von $2/3$ und Signifikanz in $\sigma$ aus.

---

### Feinstrukturkonstante und $\alpha$-Herleitung

#### `t0_alpha_pruefung.py`
Prüft beide FFGFT-Methoden zur Herleitung von $\alpha$:
- Methode 1 (geometrisch): $\alpha = \xi \cdot \varphi^3 \cdot 13$, $\alpha^{-1} \approx 136{,}19$
- Methode 2 (T0-Quantenzahlen): $\alpha^{-1} \approx 141{,}44$

Enthält automatische `assert`-Prüfungen für beide Methoden.
Referenz: Dok. 133.

#### `higgs_pruefformel.py`
Prüft die Higgs-Ableitung von $\xi$ mit dem korrigierten Vorfaktor
$16\pi^3$ (Dok. 190, K1). Vergleicht $\xi_\text{Higgs}$ mit $\xi_\text{T0} = 4/30000$.

---

### Quanten-Computing und Shor-Algorithmus

#### `t0_shor_complete.py`
Vollständige FFGFT-Implementierung des Shor-Algorithmus.
Ersetzt die QFT durch $\xi$-Resonanzsuche (Dok. 176).
Unterstützt beliebige $N$, BigInt-exakt.

#### `t0_shor_production.py`
Produktionsversion des FFGFT-Shor-Algorithmus.
Optimiert für RSA-relevante $N$, mit Benchmarks gegenüber
klassischem Trial Division.

#### `bell_73qubit_FIXED.py`
Simulation von Bell-Zuständen auf 73-Qubit-Systemen mit
FFGFT-$\xi$-Dämpfung. Korrigierte Version (FIXED) mit
verbesserter Fehlerbehandlung bei großen Registern.
Erzeugt `bell_73qubit_fixed_analysis.png`.

---

### Geometrie und Topologie

#### `toroidal_vs_cylindrical_analysis.py`
Vergleicht toroidale Geometrie (FFGFT) mit zylindrischer Geometrie
(Standardmodell-Näherung) für Qubit-Zustandsräume (Dok. 175).
Erzeugt `toroidal_vs_cylindrical_analysis.png`.

#### `T3-experimet.py`
Numerisches Experiment zur T3-Symmetrie im FFGFT-Torus.
Prüft ob die dreifache Torus-Windungsstruktur die
Z3-Fixpunkte von Avi Rosenthals Geometrie reproduziert (Dok. 172).
Erzeugt `t3_experiment_pruefung.png`.

#### `fraktaler_wirkungsquerschnitt.py` *(Ausgabe: `fraktaler_wirkungsquerschnitt.png`)*
Berechnet den fraktalen Wirkungsquerschnitt für Streuexperimente
unter FFGFT-Korrekturen ($D_f = 3 - \xi$).

---

### Baryonenasymmetrie und Materie-Antimaterie

#### `baron.py`
Berechnet die Baryonenasymmetrie $\eta = n_B/n_\gamma$ im FFGFT-Rahmen.
Vergleich mit dem Planck-CMB-Wert $\eta \approx 6{,}10 \times 10^{-10}$.
Erzeugt `baryon_asymmetrie_pruefung.png`.

#### `baryon_asymmetrie_korrigiert.py` *(Ausgabe: `baryon_asymmetrie_korrigiert.png`)*
Korrigierte Version mit CP-Asymmetriephase $\delta$ aus
Avi Rosenthals Vorhersage (Dok. 172): $\delta = 283{,}28°$.

---

### Herleitung und Beziehungen

#### `t0_herleitung-beziehungen.py`
Dokumentiert alle Ableitungsbeziehungen zwischen den FFGFT-Größen:
$\xi \to L_0 \to \ell_P \to \hbar \to \alpha \to m_e \to \ldots$
Enthält automatische `assert`-Prüfungen für die gesamte Kette.

#### `messwert_analyse.py`
Statistische Analyse der Abweichungen zwischen FFGFT-Vorhersagen
und Messwerten. Berechnet mittlere Abweichung, Standardfehler
und Signifikanz für alle 47 Konstanten aus `calc_De.py`.

#### `offene-fragen.py`
Listet offene numerische Fragen der FFGFT und testet verschiedene
Ansätze: Quark-Massenvorfaktoren, höhere Ordnungen in $K_\text{frak}$,
Verbindung zur Zeta-Funktion (Dok. 176).

---

### Quantengravitation

#### `quantengravitation_pruefung.py` *(Ausgabe: `quantengravitation_pruefung.png`)*
Prüft FFGFT-Vorhersagen für Quantengravitations-Effekte
bei der Planck-Skala. Vergleich mit Loop-Quantengravitation
und Stringtheorie-Erwartungen.

---

### Kollaboration

#### `avi.py`
Numerische Verifikation der drei Vorhersagen aus dem Avi-Rosenthal-Dialog
(Dok. 172):
- CP-Phase: $\delta = 283{,}28°$ (Abw. $0{,}06°$ vom PDG-Wert)
- $\sin^2\theta_W = 3/13 \approx 0{,}23077$ (Abw. $0{,}19\,\%$)
- Baryonenasymmetrie: $\eta = 6{,}03 \times 10^{-10}$ (Abw. $0{,}5\,\%$)

---

## Voraussetzungen

```bash
python --version   # Python 3.8 oder neuer
# Nur Standardbibliothek: math, fractions, datetime, json
```

Keine externen Pakete erforderlich.
Ausnahme: `t0_cosmic_data_analyzer.py` und `t0_cosmic_qubit_simulator.py`
benötigen `numpy` und `matplotlib` für Diagramme.

---

## Erzeugte Ausgabedateien

| Skript | Ausgabe |
|--------|---------|
| `calc_De.py` | `T0_berechnungsdaten.txt`, `T0_berechnungen.json` |
| `T3-experimet.py` | `t3_experiment_pruefung.png` |
| `bell_73qubit_FIXED.py` | `bell_73qubit_fixed_analysis.png` |
| `baron.py` | `baryon_asymmetrie_pruefung.png` |
| `koide_kfrak_test.py` | `koide_kfrak_test.png` (nicht vorhanden, Ausgabe: `koide_kfrak_test.png`) |
| `max-mass.py` | `max_masse_pruefung.png` |
| `toroidal_vs_cylindrical_analysis.py` | `toroidal_vs_cylindrical_analysis.png` |
| `t0_cosmic_data_analyzer.py` | `T0_analyse.png` |
| `quantengravitation_pruefung.py` | `quantengravitation_pruefung.png` |

---

## Korrekturen gegenüber älteren Versionen

Dokumentiert in **Dok. 190** (Korrekturverzeichnis):

| Nr. | Betrifft | Fehlerhaft | Korrekt |
|-----|----------|------------|---------|
| K1 | Dok. 049 | $\xi = \lambda_h^2 v^2 / (64\pi^4 m_h^2)$ | $\xi = \lambda_h^2 v^2 / (16\pi^3 m_h^2)$ |
| K2 | Dok. 116 | $r_\tau = 8/3$ | $r_\tau = 25/9$ |
| K3 | Dok. 018 | $a_e = 4\pi/(f \cdot k)$ | $a_e = 2\pi^2/(f \cdot k)$ |

---

## Referenzen

- **Dok. 006** — Teilchenmassen: $r$- und $p$-Tabelle  
- **Dok. 018** — Anomales magnetisches Moment ($g$-$2$)  
- **Dok. 049** — Lagrangian und Higgs-Integration  
- **Dok. 133** — Feinstrukturkonstante: zwei Herleitungsmethoden  
- **Dok. 172** — Dialog mit Avi Rosenthal: CP-Phase, $\sin^2\theta_W$, Baryonenasymmetrie  
- **Dok. 173–176** — Quantenpunkte, Spin, Qubit-Zustandsräume, Shor-Algorithmus  
- **Dok. 182** — Maximale Univers-Skala und $t_0$  
- **Dok. 190** — Korrekturverzeichnis (verbindlich)  

Vollständige Dokumentation:  
[github.com/jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
[zenodo.org/records/18834145](https://zenodo.org/records/18834145)
