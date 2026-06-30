# Release Notes — v1.1.2 (Mai 2026)

> **Schwerpunkt:** Komplette Neuauflage der Kindle-Buchserie als
> Fünf-Band-Sammlung in drei KDP-Formaten — Erweiterung um alle nach
> v1.1.0 hinzugekommenen Dokumente.

**DOI:** [10.5281/zenodo.20474821](https://doi.org/10.5281/zenodo.20474821)

---

## Was sich gegenüber v1.1.1 ändert

v1.1.1 hatte 11 neue Dokumente im Korpus ergänzt (Dok. 240, 245–254).
Diese fanden sich noch *nicht* in den damals veröffentlichten drei
Kindle-Bänden wieder. v1.1.2 schließt diese Lücke:

- Die bisherigen drei Bände (Grundlagen, Lagrangian/QFT,
  Kosmologie/Bewusstsein) werden **mit allen Korrekturen seit
  Februar 2026 neu gebaut** (HW147-Korrektur in Dok. 147 §8,
  Folgedokument-Updates Dok. 022/035/148/202, Dok. 230 erweitert).
- **Zwei neue Bände (Bd. 4 und Bd. 5)** ergänzen die Sammlung um
  74 weitere Dokumente, die seit der ursprünglichen Drei-Band-Konzeption
  entstanden oder ergänzt wurden — darunter die gesamte
  Hilbertraum-Bijektion (Dok. 230–232), die Falsifikationstrilogie
  (Dok. 220–222), die FFGFT-vs.-RA/RSG-Vergleiche (Dok. 245–247), die
  Schwarzloch-Information (Dok. 250), die dualen Ordnungsprinzipien
  (Dok. 254) und die epistemische Selbstpositionierung (Dok. 262).
- Jeder der fünf Bände wird in **drei KDP-Formaten** ausgeliefert:
  eBook 6×9 Zoll (Kindle), Taschenbuch 8.5×11 Zoll (Paperback) und
  Hardcover 8.25×11 Zoll — jeweils auf Deutsch und Englisch.
- **30 PDFs** insgesamt: 5 Bände × 2 Sprachen × 3 Formate.

---

## Die fünf Bände

| Band | Inhalt | Dok.-Anzahl | eBook DE | Paperback DE | Hardcover DE |
|------|--------|-------------|----------|--------------|--------------|
| Teil 1 | Grundlagen, ξ-Parameter, Konstanten, Einheiten | 40 | 533 | 452 | 459 |
| Teil 2 | Lagrangian-Formalismus, QFT, QM-Tests, Photonenchip | 36 | 505 | 423 | 427 |
| Teil 3 | Kosmologie, CMB, Bewusstsein, FFGFT-Narrativ | 35 | 487 | 412 | 415 |
| Teil 4 | Frühe Erweiterungen (bis Dok. 184 p-bit) | 37 | 473 | 407 | 414 |
| Teil 5 | Schichten, Hilbertraum-Brücke, jüngste Klärungen | 37 | 506 | 436 | 438 |

Englische Versionen vergleichbar kürzer (1-2 Seiten weniger pro Kapitel).

**Alle Bände eingehalten:**
- eBook ≤ 550 Seiten (Kindle eBook-Limit)
- Paperback ≤ 828 Seiten (KDP Paperback 8.5×11-Limit)
- Hardcover ≤ 550 Seiten (KDP Hardcover 8.25×11-Limit)

---

## Aufteilung Buch 4 / Buch 5

Schnittstelle bei **Dok. 184 → Dok. 185**. Thematisch sauber:

- Bis Dok. 184 (p-bit): Theorie wird auf Schicht 1 (kompaktes T⁴,
  korrekturfreie Beschreibung in natürlichen Einheiten) erarbeitet.
- Ab Dok. 185 (Einbettungspreis): die Schicht-1/Schicht-2-Sprache
  wird als ausdrückliches Beschreibungsraster verwendet und bis zur
  epistemischen Selbstpositionierung in Dok. 262 durchgeführt.

---

## Drei KDP-Formate

Beide Print-Formate (Paperback und Hardcover) verwenden identische
Geometrie-Parameter, nur die Papierbreite unterscheidet sich:

```latex
\documentclass[11pt,openright,twoside]{book}
\usepackage[
  paperwidth=8.50in,   % oder 8.25in für Hardcover
  paperheight=11.0in,
  top=1.0in,
  bottom=1.2in,
  inner=0.75in,
  outer=1.25in,
  bindingoffset=5mm,
  twoside
]{geometry}
```

Das eBook verwendet symmetrische Ränder (oneside, je 0.5 in) für die
digitale Anzeige.

---

## Technische Verbesserungen

### Tabellen-Wrap für Kindle 6×9

650 Tabellen in 206 ch-Dateien wurden automatisch in
`\adjustbox{max width=\textwidth}{...}` eingewickelt. `max width`
skaliert nur HERUNTER, wenn die Tabelle zu breit ist; kleinere
Tabellen behalten ihre natürliche Größe. Effekt im Kindle 6×9-Format:

- Teil 1 DE: 185 → 43 Overfull-hboxes (−77%)
- Teil 5 DE: 363 → 22 Overfull-hboxes (−94%)
- Teil 1 EN: 201 → 1 LaTeX-Errors (kaskadierende Tabellen-Fehler
  in der Dokumentenübersicht Dok. 086 aufgelöst)

In den Print-Formaten ist der Textbereich breiter, sodass die meisten
Tabellen ohnehin nicht skaliert werden müssen. Dieselbe ch-Datei
funktioniert für alle drei Formate ohne separate Pflege.

### Patches-Datei `T0_preamble_patches.tex`

Ergänzt fehlende Environments und Farbnamen, die in einzelnen
ch-Dateien verwendet wurden, aber in `T0_preamble_De.tex` /
`T0_preamble_En.tex` nicht definiert waren:

- Environments: `avipost`, `response` (Dok. 172 Avi-Dialog);
  `geminibox`, `userbox`, `videobox` (Dok. 191 Gemini-Dialog);
  `infobox`, `keybox`, `predbox`, `warnbox` (Dok. 187, 188, 189).
- Farb-Aliase: `T0red`, `T0gray`, `T0blue`, `T0green`, `T0orange`,
  `T0purple`, `T0yellow` (Großbuchstaben-Varianten zu den bereits
  definierten Kleinbuchstaben).

Lädt nach der Hauptpräambel, ändert nichts an bestehenden Definitionen.

### Korrektur Teil2-end-Typo

Die alten Wrapper enthielten in `pri-end/Teil2-end_De.tex` und `_En.tex`
einen Tippfehler: `\input{../ch/023a_Bell-video_De_ch}` (Datei existiert
nicht) — korrigiert zu `023b_Bell-video_De_ch`. Ohne diesen Fix konnte
Band 2 in dieser Form nie gebaut werden.

### Neue Einleitungen für Teil 4 und Teil 5

`000_Einleitung_Teil4_{De,En}_ch.tex` und `000_Einleitung_Teil5_{De,En}_ch.tex`
mit ausdrücklicher Beschreibung der Bd.-4/Bd.-5-Aufteilung und
Schicht-1/2-Vokabular-Übergang.

---

## Was inhaltlich neu ist

**Im Korpus seit v1.1.0 hinzugekommen** (jetzt erstmals in Bd. 4+5
zusammengefasst):

- **Hilbertraum-Brücke** (Dok. 230–232): konkrete Bijektion FFGFT
  ↔ Standard-QM auf dem Qubit-Sektor; ΔCHSH ~ 10⁻⁵ testbar.
- **Falsifikationstrilogie** (Dok. 220–222): Casimir, Rotverschiebung,
  Lithium — drei explizite Falsifikationskriterien.
- **Schichten- und Skalenleiter** (Dok. 241–253): systematische
  Durcharbeitung von Schicht 1 (statisch, kompakt) vs. Schicht 2
  (dynamisch, SI-projiziert).
- **IPI-Brücken** (Dok. 245–247): FFGFT vs. RA 2.1 (Guevara),
  FFGFT vs. RSG (Austin), Kategorienfehler überarbeitet.
- **Schwarzloch-Information** (Dok. 250): Hawking-Paradoxon
  via Ontologie/Epistemologie-Unterscheidung; Gitterdispersions-
  korrektur ΔE/E = −(E/E_max)²/24.
- **Duale Ordnungsprinzipien** (Dok. 254): Resonanz und Entropie
  kausal verbunden; Vopsons zweites Infodynamik-Gesetz geometrisch
  reproduziert.
- **Akzeptanz ohne Anschauung** (Dok. 262): epistemische
  Selbstpositionierung; "drei geborgte Äpfel" als Modell für
  T̃·m=1; Schicht-1/2-Sprache abgeschlossen.
- Plus die HW147-Korrektur in Dok. 147 §8 (echte IBM-Messung
  S = 2,74; "40×"-Behauptung widerlegt) mit Folgekorrekturen in
  Dok. 022, 035, 148, 202.

---

## Build-Umgebung

- **LuaLaTeX** (TeX Live 2023+)
- **Inter** (Variable Font, Hauptschrift)
- **JetBrains Mono** (Code-Listings)
- **Libertinus Math** (mathematische Notation)
- **babel-ngerman** für deutsche Silbentrennung
- **adjustbox**, **tcolorbox**, **microtype**, **fontspec**

---

## Repository-Änderungen

### Neue Dateien

```
2/tex-n/wr/
├── Teil1_ebook_De.tex                  (NEU mit Patch-Zeile)
├── Teil1_paperback_De.tex              (NEU)
├── Teil1_hardcover_De.tex              (NEU)
├── … analog für Teil 2, 3, 4, 5 in DE und EN  (30 Wrapper insgesamt)

2/tex-n/pri-end/
├── Teil2-end_De.tex                    (Typo-Fix)
├── Teil2-end_En.tex                    (Typo-Fix)
├── Teil4-end_De.tex                    (NEU)
├── Teil4-end_En.tex                    (NEU)
├── Teil5-end_De.tex                    (NEU)
├── Teil5-end_En.tex                    (NEU)
└── T0_preamble_patches.tex             (NEU)

2/fixed/ch/
├── 000_Einleitung_Teil4_De_ch.tex      (NEU)
├── 000_Einleitung_Teil4_En_ch.tex      (NEU)
├── 000_Einleitung_Teil5_De_ch.tex      (NEU)
├── 000_Einleitung_Teil5_En_ch.tex      (NEU)
└── (206 weitere ch-Dateien mit \adjustbox-Wrapper um Tabellen)

scripts/
└── wrap_tables_for_kindle.py           (NEU)

books/                                  (NEU — alle Print-PDFs)
├── eBook_6x9/Deutsch/Teil1-5_ebook_De.pdf
├── eBook_6x9/English/Teil1-5_ebook_En.pdf
├── Paperback_8.5x11/Deutsch/Teil1-5_paperback_De.pdf
├── Paperback_8.5x11/English/Teil1-5_paperback_En.pdf
├── Hardcover_8.25x11/Deutsch/Teil1-5_hardcover_De.pdf
└── Hardcover_8.25x11/English/Teil1-5_hardcover_En.pdf
```

### DOI-Hinweis

Die Bücher selbst enthalten an mehreren Stellen Verweise auf frühere
Zenodo-DOIs (16142455, 17390358, 18834145, 20041529, 20117635). Diese
Verweise sind versionspezifisch — Verweise auf "die aktuelle
Veröffentlichung" werden mit dem v1.1.2-Release auf den neuen DOI
aktualisiert. Verweise auf historische Versionen bleiben unverändert.

(Die DOI-Aktualisierung in den ch-Dateien erfolgt im Anschluss an den
Zenodo-Upload.)
