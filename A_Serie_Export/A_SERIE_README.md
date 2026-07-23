# FFGFT A-Serie — Fraktale Feldgeometrische Fundamentaltheorie / T0 Zeit-Masse-Dualität

**Autor:** Johann Pascher (ORCID: 0009-0000-6518-4064)  
**Version:** 1.1 (2026-07-23)  
**Zenodo DOI:** 10.5281/zenodo.21496379  
**Sprachen:** Deutsch (kanonisch) · Englisch (parallele Fassung)

---

## Was ist die A-Serie?

Die A-Serie ist die kanonische, sachgeordnete Fassung der FFGFT. Sie fasst mehr
als 300 Altdokumente in 43 thematisch geordneten Dokumenten zusammen — ein Thema
an einem Ort, jede Aussage mit Schichtstatus markiert, alle Korrekturen
eingearbeitet.

**Sie ersetzt den Altbestand nicht physisch.** Die alten Nummern bleiben bestehen
und sind zitierbar. Die A-Serie ist die Fassung, die man liest, wenn man wissen
will, was die Theorie heute behauptet.

---

## Verzeichnisstruktur

```
Sources/
  ch/                  86 Quelltexte (43 De + 43 En, *_ch.tex)
  pri-end/              3 Preamble-Dateien
  wr_standalone_A4/    86 Wrapper (43 De + 43 En, kompilierfertig)
pdf/                   86 PDFs (43 De + 43 En)
python/
  A_Serie_Skripte/     44 Prüfskripte (.py)
README.md
CHANGELOG.md
```

---

## Blockstruktur (43 Dokumente)

```
Block 0  A010–A095   Grundlage
         A010 Zweck, Aufbau, Lesart
         A015 Ursprung von ξ
         A020 Die drei Setzungen
         A030 Kompakte Geometrie T⁴/Z₃
         A040 Fraktale Korrektur K_frak
         A050 Rekursion und Nichtschließung
         A060 Zeit: kompakte Richtung, T·E = 1
         A070 Hilbertraum-Brücke H = L²(T⁴)⊗ℂ³
         A075 Feldtheorie: Modefunktionen, Lagrangian
         A080 Einheiten und Buchhaltung
         A085 Natürliche Einheiten
         A090 Projektionskette T⁴→T⁰
         A095 Torus-Chiralität, g_R = 0 [B]

Block 1  A100–A192   Sektoren
         A100 Leptonleiter: ξ-Formel
         A105 Leiter-Grundeinheit N₀
         A110 Zirkulant und Koide: Q = 2/3
         A120 θ = 2/9: Ort und Status
         A130 Feinstrukturkonstante α = ξ·E₀²
         A135 Was auf Eins gesetzt werden kann
         A138 Anomale magnetische Momente g−2
         A140 Gravitation: G als Brücke
         A142 Gravitationsdynamik: Zeitfeld-Lagrange
         A145 Gravitationskonstante G = ξ²/(4m_char)
         A150 Quarks und Neutrinos
         A160 Quantenmechanik auf T⁴: Bell als Topologie
         A165 Bell-Tests und Hardware (IBM Heron r2, Mai 2026)
         A180 Information: Windungsquant Δw = 1
         A190 Standardmodell als dekompaktifizierte Projektion
         A192 Eichsektor: U(1) und SU(3) aus Torus-Topologie [B]

Block 2  A200–A250   Methodik und Bilanz
         A200 Ordnung ohne Rangordnung: vier Schichten
         A210 Falsifizierbarkeit: vier Prüfgrößen
         A220 Toleranzmaßstab: vier Genauigkeitsklassen
         A230 Offene Punkte (Stand 2026-07, geschlossene Punkte verzeichnet)
         A240 Abgrenzung: SM, GR, externe Rahmen
         A250 Verweistabelle: A-Serie und Altbestand

Block 3  A260–A267   Erweiterungen
         A260 Casimir-Effekt
         A261 Skalenhierarchie: ξ → Massen → α → E₀
         A262 c-Konvention: E = mc² = E = m
         A263 Dirac-Gleichung vollständig
         A264 Strukturelle Asymmetrien: Chiralität, Gravitation, Monopole
         A265 Rotverschiebung: statisch, achromatisch
         A266 Einheitenprüfung und SI-Rückrechnung
         A267 Stipulation α = 1
```

---

## Schichtmarkierungen

| Marke | Bedeutung |
|-------|-----------|
| **[SETZUNG]** | Axiom, nicht hergeleitet |
| **[K]** | Kern — aus ξ hergeleitet, numerisch geprüft |
| **[B]** | Brücke — algebraisch bewiesen |
| **[S]** | Skizze — plausibel, nicht vollständig ausgeführt |

Die Marker [K] und [B] sind interne Zustandsangaben des Anspruchs, keine
externen Zertifizierungen. Keiner der beiden begründet für sich empirische
Wahrheit, externe physikalische Gültigkeit oder eine eindeutige Ontologie.

Der Anspruch der Serie lautet: **Jede berechenbare Aussage ist unabhängig
ausführbar und nachprüfbar, und jede substanzielle Aussage trägt einen
explizit deklarierten epistemischen Status.** *(Formulierung nach Stefaan
Vossen, 2026 — ersetzt die frühere Kurzform „Alles ist überprüfbar",
die mehr behauptete, als die Skripte leisten.)*

---

## Drei Setzungen (A020)

- **T̃·m = 1** — Zeit-Masse-Dualität
- **T⁴/Z₃** — kompakter 4-Torus mit Z₃-Orbifold
- **ξ = 4/30000** — geometrischer Grundparameter

---

## Aus ξ hergeleitet (Auswahl)

| Größe | Wert | Status | Dok |
|-------|------|--------|-----|
| Leptonmassen | ~1 % Übereinstimmung | [K] | A100 |
| Koide Q = 2/3 | exakt | [K] | A110 |
| α ≈ 1/137.036 | 0.0005 % | [K] | A130 |
| G = ξ²/(4m_char) | [K] | A145 |
| D_f = 3−ξ | 2.99987 | [K] | A040 |
| U(1)_EM aus Flussquantisierung | [B] | A192 |
| SU(3)_C aus Verschlingungszahl | [B] | A192 |
| g_R = 0 aus Torus-Projektor P₊ | [B] | A095 |
| CHSH-Vorfaktor ξ/(2π) | [B] | A160 |

---

## Vier Prüfgrößen (A210)

1. **τ-Masse:** 1776.968 MeV — echte Vorhersage, prüfbar
2. **CHSH-Abweichung:** Ordnung ξ ≈ 10⁻⁵ — heute unter NISQ-Rauschen
3. **Fraktale Dimension:** D_f = 3−ξ
4. **Grundlänge:** L₀ = ξ·ℓ_P = 2.155×10⁻³⁹ m

---

## Neu in dieser Fassung (2026-07)

- **A095** (neu): g_R = 0 auf [B] angehoben; Torus-Projektor P₊
- **A192** (neu): U(1) und SU(3) aus Torus-Topologie [B]
- **A060**: T·E = 1 nativ; Heisenberg-Begründung ersetzt
- **A130**: Higgs-EFT 2.3 %-Abweichung strukturell erklärt
- **A160**: CHSH-Vorfaktor ξ/(2π) geometrisch begründet
- **A230**: Geschlossene Punkte explizit verzeichnet
- **A240/A250**: Eichsektor-Status aktualisiert
- **A010**: Neuer Abschnitt eigenständige Altbestand-Dokumente
- Alle 43 En-Wrapper-Titel auf Englisch korrigiert
- KI-Abschnitt in A010 an den Anfang verschoben

---

## Eigenständige Altbestand-Dokumente (nicht in A-Serie)

Die A-Serie übernimmt 102 von ~320 Altdokumenten. Die übrigen:

| Gruppe | Dok. (Auswahl) | Bemerkung |
|--------|---------------|-----------|
| Kosmologie/Vakuum | 036, 063, 064, 140 | ausdrücklich ausgeschlossen (A010) |
| Operativer Eichsektor | 186, 281 | offener Punkt (A190, A192) |
| IPI-Vergleiche | 246, 251, 269, 271, 272, 283, 294 | extern, kein A-Bestandteil |
| Quanten-Hardware | 083–085, 161, 173–176, 183 | Anwendungen, eigenständig |
| Populär/Einführung | 002, 004, 185, 191 | Zugang ohne Formeln |
| KI/Bewusstsein | 100, 207 | philosophisch, eigenständig |
| Methodisch/Diagnose | 241–248, 262, 274, 277, 303–305 | Arbeitsmaterial |
| Physik-Erweiterungen | 021–081, 089, 095, 105, 114, 129, 137, 145–170, 182, 184, 187, 192, 206 | Zwischenstadien, Nebenlinien |

Vollständige Zuordnung: A250.

---

## Prüfskripte

```
python/A_Serie_Skripte/a???_*.py   (44 Skripte)
```

Ausführung mit Python 3.10+. Alle Kernaussagen liefern `BESTANDEN`.

---

## Kompilieren

```bash
cd Sources/wr_standalone_A4
lualatex A010_Zweck_Aufbau_De.tex   # 2–3× für TOC
```

Preambles werden aus `../pri-end/` geladen.

---

## Zitieren

```
Pascher, J. (2026). FFGFT A-Serie v1.1 (2026-07-23).
Zenodo. https://doi.org/10.5281/zenodo.21496379
```

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*  
*Dieses README wurde unter Verwendung KI-gestützter Werkzeuge erstellt.*
