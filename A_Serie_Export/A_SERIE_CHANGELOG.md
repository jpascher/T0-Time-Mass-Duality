# CHANGELOG — FFGFT A-Serie

Alle wesentlichen Änderungen dieser Serie. Format: Datum · Dokument · Inhalt.

---

## v1.4 — 2026-07-27

### Dokumentenzählung korrigiert: 47 → 48

- **A155 (Meson-Sektor)** war in der Blockstruktur des README nicht gelistet,
  obwohl PDF, Quelltexte (De + En) und Prüfskript (`a155_meson.py`) vorhanden
  und vollwertiger Teil von Block 1 sind. A155 ist jetzt in der Blockstruktur
  (nach A150) ergänzt; die kanonische Zählung steht auf **48 Dokumenten**
  (96 PDFs De + En, 48 Prüfskripte).
- Keine inhaltliche Änderung an den Dokumenten selbst — reine Korrektur einer
  Zählungs- und Listungslücke im README.

### Ausgeschlossen aus dem kanonischen Stand

- **A280 / A281 / A282** (Doppel-Nummerierung der Thermodynamik-Trilogie
  Landauer / Träger und Information / Rechenkugel) sind Altstände der unter
  A271 / A272 / A273 kanonisch geführten Trilogie. Sie besitzen keine eigenen
  Quelltexte (nur PDFs) und sind nicht Teil des kanonischen Objekts. Ebenso
  entfällt das verirrte `a282_rechenkugel.py` (Dublette von `a273_rechenkugel.py`).

### Release

- v1.4 wird als eigenständiges Zenodo-Release deponiert (eigene Versions-DOI
  unter der Konzept-DOI 10.5281/zenodo.20117635). Das eingefrorene Objekt umfasst
  die 48 kanonischen Dokumente A010–A273, README, CHANGELOG, WORKFLOW und die
  48 Prüfskripte.

---

## v1.3 — 2026-07-25

### Neu: A272 Träger und Information (De + En, je 12/11 S.)

- **A272** Träger und Information / Carrier and Information — Textkritik zu A271.
  Was Landauer 1961 beweist, ist eine untere Schranke für Träger-Operationen an
  einem thermischen Gleichgewichts-Ensemble, keine universelle Aussage über
  abstrakte Information. Satz 1 (Mehrfachrealisierung): einem Informationsbit kann
  keine Energie zugeordnet werden, nur seinem Träger. Satz 2: eine rein
  interpretative Löschung verkleinert den Träger-Zustandsraum nicht. Ausdrücklich
  als Zuständigkeitsbefund gefasst, nicht als Widerlegung. Landauers eigener
  Ensemble-Vorbehalt dokumentiert; Rezeptionsgeschichte (Lairez, Norton,
  Earman/Norton, Hemmo/Shenker); Sprachkritik der Digitaltechnik; Hypostasierung
  als Deutungsrahmen [S]. Rückkopplungsschranke Q_min = kT(ln2 − I) mit I
  dimensionslos in nat. Verbindliches Wörterbuch A271 ↔ A272 (Gebiet = Träger,
  Beschreibung = Information). Kein eigenes Prüfskript.

### Neu: A273 Die Rechenkugel (De + En, je 10/9 S.)

- **A273** Die Rechenkugel / The Reckoning Bead — Token-Rechnen (Abakus, Muscheln,
  Münzen) als Grenzfall, an dem Landauers Argument in zwei unabhängige Hälften
  zerfällt. Die Buchhaltung gilt exakt und trägerunabhängig (ΔS/k_B = N·ln2); die
  thermische Umrechnung ΔS → Q = T·ΔS gilt dort nicht (Kugelverschiebung
  5,1·10¹⁵ × Landauer, Positions-Bit 3,8·10⁻²³ der Eigenentropie, Barriere
  3,6·10¹⁵ k_B·T). Der Token-Rechner fällt unter Landauers eigenen
  Ensemble-Vorbehalt. Zwei Böden: thermisch k_B·T und quantengeometrisch ħc/L,
  maßgeblich ist der größere (Schnitt bei 7,6 µm bei 300 K; Qubit hf/k_B·T = 24).
  Sichtbarkeit der Struktur und Bindekraft der Zahl laufen gegenläufig.
  Markenvorrat als eigene Kostenkategorie [S]. Prüfskript a273_rechenkugel.py
  (Checks 1–14, alle BESTANDEN).

### Geändert

- **A271** überarbeitet: hinreichend für die Wärmeproduktion ist die
  Nicht-Bijektivität der Gebietsabbildung, nicht die logische Irreversibilität
  (Realisierungsannahme ausgewiesen, Bennett-Bezug ergänzt); numerische Angaben
  vereinheitlicht; Quellenapparat vervollständigt; Prüfskript-Verweis auf
  a271_landauer.py korrigiert.
- Neuer Schichtmarker **[Q] — Quelle: korpusexterne Primärquelle oder Messwert**.
  [K] (Kern, aus ξ hergeleitet) kommt in A271–A273 nicht vor, da diese Dokumente
  FFGFT-Berührung: keine deklarieren.
- Blockstruktur: Block 3 jetzt A260–A273; Serie auf 47 Dokumente.

---

## v1.2 — 2026-07-25

### Neu: A271 Landauer und die Phasenraum-Buchhaltung (De + En, je 18 S.)

- **A271** Landauer und die Phasenraum-Buchhaltung / Landauer and the Phase-Space Accounting —
  Fehlinterpretation als Fragestellung, Landauers Originaltext als Antwort;
  Kernsatz §1: „circuit connections", nicht Daten, bestimmen Thermodynamik;
  Energie gehört dem Hardware-Element (nicht dem Bit); Dynamik als Vehikel;
  Realisierungsabhängigkeit (Spin / DRAM / Magnetdomäne) mit Landauer-Beleg;
  Qubit-Untergrenze als offene Frage [H]; drei wörtliche Zitate aus
  Landauer 1961 mit §-Nachweis. Prüfskript a271_landauer.py (Checks 1–10).

### Korrekturen

- Doppelnummerierung behoben: A270 = Z₃-Sektor (Altstand), A271 = Landauer (neu)

---

## v1.0 — 2026-07-22

### Neu: Vollständige A-Serie (43 Dokumente)

**Block 0 — Grundlage**
- A010 Zweck, Aufbau, Lesart der A-Serie (KI-Abschnitt vorne; neuer Abschnitt: eigenständige Altbestand-Dokumente)
- A015 Ursprung von ξ: 5 Plausibilitätsgründe; kein Beweis möglich/nötig (R-Entscheid diese Session)
- A020 Die drei Setzungen
- A030 Kompakte Geometrie T⁴/Z₃
- A040 Fraktale Korrektur K_frak = 74/75
- A050 Rekursion und Nichtschließung
- A060 Zeit: kompakte Richtung, native Reziprozität T·E = 1 (ersetzt Heisenberg-Begründung, R50)
- A070 Hilbertraum-Brücke H = L²(T⁴)⊗ℂ³
- A075 Feldtheorie: Modefunktionen, Lagrangian, Brückenformel
- A080 Einheiten und Buchhaltung
- A085 Natürliche Einheiten: der fundamentale Grund
- A090 Projektionskette T⁴→T⁰: drei Operationen (Typ I/II/III)
- A095 Torus-Chiralität (umbenannt aus A268)

**Block 1 — Sektoren**
- A100 Leptonleiter: ξ-Formel, Verhältnisse korrekturfrei
- A105 Leiter-Grundeinheit N₀
- A110 Zirkulant und Koide: Q = 2/3, θ = 2/9
- A120 θ = 2/9: Ort, Status, Grenze
- A130 Feinstrukturkonstante α = ξ·E₀² (Higgs-EFT 2.3%-Abweichung erklärt)
- A135 Was auf Eins gesetzt werden kann, ist nicht grundlegend
- A138 Anomale magnetische Momente: g−2 Verhältnisse exakt
- A140 Gravitation: G als Brücke, QG-Problem nicht gestellt
- A142 Gravitationsdynamik: Zeitfeld-Lagrange
- A145 Gravitationskonstante G = ξ²/(4m_char)
- A150 Quarks und Neutrinos: Stand und Spekulationsanteil
- A160 Quantenmechanik auf T⁴: Bell als Topologie (CHSH-Vorfaktor ξ/(2π) geometrisch begründet)
- A165 Bell-Tests und Hardware: IBM Heron r2 Mai 2026
- A180 Information: Windungsquant Δw = 1
- A190 Standardmodell als dekompaktifizierte Projektion (3 Eichsektor-Argumente)
- A192 Eichsektor: Torus-Topologie und kovariante Ableitungen (neu diese Session)

**Block 2 — Methodik**
- A200 Ordnung ohne Rangordnung: vier Schichten
- A210 Falsifizierbarkeit: vier Prognosegrößen
- A220 Toleranzmaßstab: vier Genauigkeitsklassen
- A230 Offene Punkte: Residuen der Serie
- A240 Abgrenzung: Standardmodell, Relativität, externe Rahmen
- A250 Verweistabelle: A-Serie und Altbestand

**Block 3 — Erweiterungen**
- A260 Casimir-Effekt: Vakuumstruktur, Bestätigung 4/3
- A261 Skalenhierarchie: ξ → Massen → α → E₀
- A262 c-Konvention: E = mc² = E = m
- A263 Dirac-Gleichung vollständig: Clifford-Algebra, Spin, Massenelimination
- A264 Strukturelle Asymmetrien: Chiralität, Gravitation, Monopole
- A265 Rotverschiebung: statisch, achromatisch, ohne Expansion
- A266 Einheitenprüfung und SI-Rückrechnung
- A267 Stipulation α = 1: Ladungsumdefinition, 137-Leiter

### Korrekturen und Entscheide (diese Session)

| Ref | Dok | Inhalt |
|-----|-----|--------|
| R-Entscheid | A015 | ξ-Beweis nicht möglich/nötig; 5 Plausibilitätsgründe statt Forderung geometrischer Ableitung |
| R-Entscheid | A142 | Gravitationsquantisierung nicht gefordert; G intrinsisch aus ξ |
| R50 | A060 | T·E = 1 nativ; Heisenberg-Begründung ersetzt (Konklusion unverändert) |
| R54 | A060 | Kein N₀ als Grundeinheit; Moden sind kommensurable Vielfache von d₁ = 1/75 |
| R52 | A210 | L₀-Zahlenwert am Standard-Anker korrigiert; 5.39×10⁻³⁹ m als Übertragungsfehler verworfen |
| neu | A190 | Higgs-EFT 2.3%-Abweichung strukturell erklärt (SI-Werte schemaabhängig + K_frak in v nicht trennbar) |
| neu | A192 | Eichsektor: U(1) aus Flussquantisierung, SU(3) aus Verschlingungszahl (beide [B]) |
| neu | A095 | g_R = 0 auf [B] angehoben: Kern-Argument Torus-Projektor P₊ |
| neu | A160 | CHSH-Vorfaktor ξ/(2π) geometrisch begründet: Kreisumfang als Konversionsfaktor |

### Technisch

- 43 × De-PDF, 43 × En-PDF (je 3 LaTeX-Läufe, TOC korrekt)
- 45+ Prüfskripte in python/A_Serie_Skripte/
- Alle En-Wrapper-Titel auf Englisch
- KI-Abschnitt in A010 vorne (alle anderen am Ende)
- A268 → A095 umbenannt; Altdateien entfernt

---

## Vorgeschichte (Altbestand, nicht A-Serie)

| Version | Datum | Inhalt |
|---------|-------|--------|
| v1.2.3 | 2026-07 | Korpus-Restrukturierung; Skripte in DokNNN_Skripte/; README DE+EN |
| v1.2.2 | 2026-06 | Korrekturregister R54–R56; Dok 306 (native Zeit-Energie-Reziprozität) |
| v1.1.0 | 2026-05 | Hilbertraum-Brücke (Dok 230/231/232); Zenodo-Release 10.5281/zenodo.20117635 |
| v1.0.x | 2025–2026 | Aufbau des Altbestands (300+ Dokumente) |

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*
