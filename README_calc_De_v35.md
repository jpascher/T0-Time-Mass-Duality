# FFGFT / T0-Zeit-Masse-Dualität — Berechnungsskripte

**Johann Pascher** · Oberösterreich, Austria  
GitHub: [jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
Zenodo: [10.5281/zenodo.18834145](https://doi.org/10.5281/zenodo.18834145)

---

## Übersicht

Dieses Paket enthält vier Python-Skripte zur numerischen Validierung der
**FFGFT (Fundamentale Fraktale Geometrische Feldtheorie)**, auch bekannt als
**T0-Zeit-Masse-Dualität**.

Das zentrale Konzept der Theorie: Alle Naturkonstanten und Teilchenmassen
folgen aus einem einzigen dimensionslosen Parameter

$$\xi = \frac{4}{3} \times 10^{-4}$$

der seinerseits aus dem Higgs-Feld ableitbar ist (Dok. 049, 186).

---

## Skripte

### 1. `calc_De.py` — Hauptrechner v3.5

Berechnet **9 Teilchenmassen** und **47 physikalische Konstanten**
aus nur drei Eingabewerten: $\xi$, $\ell_P$, $E_0$.

**Ergebnisse:**
- Durchschnittlicher Massenfehler: **0,84 %**
- Durchschnittlicher Konstantenfehler: **0,0334 %**
- Beste Einzelvorhersage: $R_\text{gas}$ mit 0,0000 %

**Enthaltene Korrekturen (v3.5):**
- Tau-Vorfaktor korrigiert: $r_\tau = 8/3 \to 25/9$ (Dok. 186, Korrektur K2)
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
Da $\xi$ der einzige freie Parameter ist, aus dem alles folgt, ist
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

Berechnet drei Arten von Massuntergrenzen in FFGFT:

| Typ | Formel | Wert |
|-----|--------|------|
| Kosmologisches Minimum | $m_\text{min} = \hbar H_0 / c^2$ | $1{,}49 \times 10^{-33}$ eV |
| Leichtestes massives Teilchen | $m_{\nu_e} = \xi^2 \cdot m_e$ | $9{,}08$ meV |
| xi-Skalenleiter | $m_n = \xi^n \cdot m_e$ | diskret, $n = 0, 1, 2, 3, \ldots$ |

**Neutrino-Formel** ($r_i$ wie bei Leptonen, Dok. 006 / 186):
$$m_{\nu_i} = r_i \cdot \xi^2 \cdot m_e$$

| Neutrino | $r_i$ | $m_{\nu_i}$ | PDG-Limit |
|----------|--------|-------------|-----------|
| $\nu_e$  | $1$    | 9,08 meV    | < 45 meV (KATRIN) |
| $\nu_\mu$| $16/5$ | 29,07 meV   | < 190 keV |
| $\nu_\tau$| $25/9$ | 25,23 meV  | < 18,2 MeV |
| **Summe**|        | **63,4 meV**| **< 120 meV ✓** |

**Photon:** $m_\gamma = 0$ exakt — Torus-Geometrie erlaubt masselose Eichbosonen.

---

### 4. `calc-resonanz-leiter.py` — Vollständige Resonanz-Leiter

Berechnet alle 12 Fermionen (Leptonen + Quarks + Neutrinos) mit
exakter Bruch-Arithmetik (`fractions.Fraction`).

**Yukawa-Formel:**
$$m_i = r_i \cdot \xi^{p_i} \cdot v$$

**Exponent-Struktur** (Schrittweite $\Delta p = 1/3$, drei Raumdimensionen):

| $p$ | Teilchen |
|-----|----------|
| $-1/3$ | Top (einziges mit negativem $p$ — schwerste Quark) |
| $1/2$  | Bottom |
| $2/3$  | Tau, Charm |
| $1$    | Myon, Strange |
| $3/2$  | Elektron, Up, Down |
| $\xi^2 \cdot m_e$ | Neutrinos (eigene Klasse) |

Quarks passen **nicht** in die einfache Leiter $\xi^n \cdot m_e$,
da sie andere Exponenten $p$ tragen (andere topologische Windungszahl
im Torus-Modell).

---

## Voraussetzungen

```bash
python --version   # Python 3.8 oder neuer
# Nur Standardbibliothek: math, fractions, datetime, json
```

Keine externen Pakete erforderlich.

---

## Korrekturen gegenüber älteren Versionen

Dokumentiert in **Dok. 186** (Korrekturverzeichnis):

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
- **Dok. 182** — Maximale Univers-Skala und $t_0$  
- **Dok. 186** — Korrekturverzeichnis (verbindlich)  

Vollständige Dokumentation:  
[github.com/jpascher/T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)  
[zenodo.org/records/18834145](https://zenodo.org/records/18834145)
