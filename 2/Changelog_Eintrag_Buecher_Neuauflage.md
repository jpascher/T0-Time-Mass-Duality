## Bücher-Neuauflage v1.1.2 (Mai 2026) — Fünf Bände, drei KDP-Formate

**Anlass:** Die bisherige Drei-Band-Sammlung (Teil 1–3) war im Februar
2026 zuletzt veröffentlicht worden und enthielt weder die Korrekturen
seit dieser Zeit noch die seither hinzugekommenen Dokumente (Dok. 220–222
Falsifikationstrilogie, Dok. 230–232 Hilbertraum-Bijektion, Dok. 240
KI-Detektoren, Dok. 241–253 Schichten-Reihe, Dok. 245–247 IPI-Brücken,
Dok. 250 Schwarzloch-Information, Dok. 254 Duale Ordnungsprinzipien,
Dok. 262 Akzeptanz ohne Anschauung).

**Vorgehen:**

1. **Bände 1–3 neu gebaut** mit der aktuellen ch-Sammlung — sämtliche
   Korrekturen seit Februar 2026 sind damit automatisch integriert
   (HW147-Korrektur in Dok. 147 §8, Folgedokument-Updates Dok. 022,
   035, 148, 202, Dok. 230 erweitert). Keine Wrapper-Änderung nötig.

2. **Bände 4 und 5 neu erstellt** für 74 Dokumente, die in der
   ursprünglichen Drei-Band-Sammlung nicht enthalten waren:
   - **Band 4 (37 Dok.):** ergänzende Einzeldokumente (001, 001b, 002,
     018-11, 018-12, 129, 137, 143, 144, 148), Zeit/Kosmologie/numerische
     Vorhersagen (157–169), Bewusstsein/Photonik/Qubits (170–179),
     frühe Torus- und L₀-Begründungen (180–184 bis p-bit).
   - **Band 5 (37 Dok.):** späte Geometrie ab Dok. 185 (Einbettungspreis,
     187–193), FFGFT-Feldtheorie und Operatoren (202–210),
     Hilbertraum-Brücke (230–232), Schichten und Informationsformalismus
     (241–253), jüngste Klärungen einschließlich Dok. 262 (255–262).
   - **Schnittstelle bei Dok. 184 → Dok. 185** thematisch sauber:
     Schicht 1 vs. Schicht 1/2-Sprache.

3. **Drei KDP-Formate** pro Band:
   - **eBook 6×9 Zoll** (Kindle eBook, oneside, Margins 0,5 in)
   - **Taschenbuch 8,5×11 Zoll** (twoside, openright, bindingoffset 5 mm)
   - **Hardcover 8,25×11 Zoll** (twoside, openright, bindingoffset 5 mm)
   - 5 × 2 × 3 = **30 PDFs** insgesamt.

4. **Build-System:** LuaLaTeX + Inter + JetBrains Mono + Libertinus Math,
   plus die Patches-Datei `T0_preamble_patches.tex` für fehlende
   Environments (`avipost`, `response`, `geminibox`, `userbox`,
   `videobox`, `infobox`, `keybox`, `predbox`, `warnbox`) und
   Farb-Aliase (`T0red`, `T0gray`, …).

### Technische Korrekturen am Bestand

- **Typo-Fix in `Teil2-end_De.tex` und `_En.tex`:** `\input{../ch/023a_Bell-video}`
  (Datei existiert nicht) korrigiert zu `023b_Bell-video`. Band 2 in
  dieser Form vorher nicht baubar.
- **Tabellen-Wrap** in 206 ch-Dateien: 650 Tabellen automatisch in
  `\adjustbox{max width=\textwidth}{...}` eingewickelt für Kindle-Breite.
  Skaliert nur HERUNTER, wenn Tabelle breiter als textwidth — in
  Print-Formaten unverändert. Effekt im eBook DE 6×9:
  - Teil 1: 185 → 43 Overfull-hboxes (−77 %)
  - Teil 5: 363 → 22 Overfull-hboxes (−94 %)
  - Teil 1 EN-Errors: 201 → 1 (kaskadierende Tabellen-Fehler in
    Dok. 086 Dokumentenübersicht aufgelöst).
- **Patch-Datei** `T0_preamble_patches.tex` von allen 30 Wrappern nach
  der Hauptpräambel geladen.

### Endgültige Seitenzahlen

| Band | eBook DE | Paperback DE | Hardcover DE | eBook EN | Paperback EN | Hardcover EN |
|------|----------|--------------|--------------|----------|--------------|--------------|
| Teil 1 | 533 | 452 | 459 | 487 | 419 | 424 |
| Teil 2 | 505 | 423 | 427 | 454 | 388 | 393 |
| Teil 3 | 487 | 412 | 415 | 461 | 386 | 392 |
| Teil 4 | 473 | 407 | 414 | 406 | 357 | 362 |
| Teil 5 | 506 | 436 | 438 | 480 | 414 | 419 |

**Alle Bände unter den jeweiligen KDP-Seitenlimits.**

### DOI-Aktualisierung in den Büchern (nach Zenodo-Upload)

Die ch-Dateien enthalten an 137 Stellen Verweise auf frühere
Zenodo-DOIs (16142455, 17390358, 18834145, 20041529, 20117635 —
nicht 20355305 v1.1.1). Nach dem Zenodo-Upload von v1.1.2 werden
Verweise auf „die aktuelle Veröffentlichung" auf die neue DOI
aktualisiert; Verweise auf historische Versionen bleiben unverändert.
Dies erfolgt im Anschluss als separater Schritt.

### Status

| ✓ | Erstellt DE | 31. Mai 2026 |
| ✓ | Erstellt EN | 31. Mai 2026 |
| ☐ | DOI-Migration nach Zenodo-Upload | offen |

---

### Übersichtstabelle — Nachtrag (Fortsetzung 4)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Bücher-v1.1.2 | ✓ 31. Mai 2026 | Komplette Fünf-Band-Neuauflage in drei KDP-Formaten (30 PDFs); Bd. 1–3 mit aktuellen ch-Dateien neu gebaut, Bd. 4+5 für 74 neue Dokumente erstellt; Tabellen-Wrap für Kindle, Patches-Datei für fehlende Environments, Typo-Fix in Teil2-end. DOI-Aktualisierung in Buchinhalten erfolgt nach Zenodo-Upload. |

---

## Bücher-Neuauflage Oktober 2026 — Acht Bände, Taschenbuch und Hardcover

**Anlass:** Seit der Fünf-Band-Ausgabe (Mai 2026, bis Dok. 262) sind die
Dokumente 263 bis 389 hinzugekommen. Sie werden in drei neuen Bänden
aufgenommen; die Bände 1 bis 5 werden mit den aktuellen ch-Fassungen neu
gebaut. Gesetzt werden die beiden Druckformate Taschenbuch (8,5 × 11 Zoll)
und Hardcover (8,25 × 11 Zoll), jeweils De und En — 8 × 2 × 2 = 32 PDFs.

**Neue Bände.** Band 6 (Dok. 263–310, 44 Dokumente) „Holografie, HLV-Brücke
und die Struktur der Zeit“; Band 7 (Dok. 311–343, 33 Dokumente) „Gitter im
Hilbertraum, Spektraltheorie und Galois-Struktur“; Band 8 (Dok. 344–389,
46 Dokumente) „Standardmodell aus GF(27), Leptonmassen und Schnittstellen“.
Die Bandgrenzen fallen auf inhaltliche Schnitte und halten jeden Band
deutlich unter dem Hardcover-Limit von 550 Seiten. Einleitungen De/En für
die Bände 6–8 neu (`ch/000_Einleitung_Teil6–8_*_ch.tex`); in den
Einleitungen der Bände 3, 4 und 5 ist die Aussage „letzter Band“ bzw.
„schließt die Sammlung ab“ auf die Acht-Band-Gliederung umgestellt.

**Buchsatz der neueren Dokumente.** Die Dokumente ab 263 sind für die
A4-Standalone-Preamble geschrieben und bringen eigene `\chapter*`,
`\addcontentsline`, `\maketitle`, `\tableofcontents`, Theorem-Definitionen
und teils `\end{document}` mit. `pri-end/T0_preamble_book_plus.tex` stellt
die Standalone-Ergänzungen bereit (Farb-Aliase, Bildpfade, Tabellenbreite,
PDF-Lesezeichen) und kapselt jedes Dokument über `\FFGFTdoc` bzw.
`\FFGFTdocDemote` (Dok. 308–314 und 335, die `\chapter` als oberste
Gliederung nutzen), sodass jedes Dokument genau ein Buchkapitel mit genau
einem Inhaltsverzeichniseintrag ergibt. Die Bände 6–8 werden aus
`pri-end/Teil6–8-end_*.tex` gebaut.

**Korrekturen am Bestand.** `\appendix` in einem Einzeldokument schaltete
bisher die Kapitelzählung aller folgenden Dokumente auf „Anhang n“ um;
`pri-end/T0_preamble_book_appendixfix.tex` (in allen 32 Wrappern geladen)
begrenzt die Wirkung auf die Abschnitte des laufenden Dokuments. Band 1
verweist auf die nicht mehr vorhandene g-2-Fassung 018-10; ersetzt durch
die aktuelle Fassung 018-12, die in Band 4 entfallenen Kapitel 018-11/018-12
stehen damit nicht doppelt. In Band 4 unterdrückt ein Gruppenrahmen das
`\maketitle` von Dok. 184; englische Kapiteltitel mit `H_0`, `L_0`,
`LiNbO_3` in Band 4/5 in Mathematikmodus gesetzt. Die sechs Abbildungen von
Dok. 164 fehlten im Repo (`2/Sources/fig/fig1–fig6_*_de/en.pdf`); sie sind aus
den Standalone-PDFs vektoriell herausgelöst. Dok. 265 En: Verweis
`tab:ebenen` → `tab:levels`. Dok. 365/366: Markerlegende als eigener Absatz
(Tabelle lief in den Rand).

### Seitenzahlen

| Band | Paperback DE | Hardcover DE | Paperback EN | Hardcover EN |
|------|--------------|--------------|--------------|--------------|
| Teil 1 | 450 | 456 | 424 | 432 |
| Teil 2 | 415 | 419 | 383 | 386 |
| Teil 3 | 422 | 428 | 395 | 405 |
| Teil 4 | 364 | 368 | 347 | 350 |
| Teil 5 | 458 | 462 | 439 | 444 |
| Teil 6 | 361 | 372 | 346 | 355 |
| Teil 7 | 339 | 343 | 317 | 321 |
| Teil 8 | 340 | 346 | 322 | 329 |

Alle 32 PDFs kompilieren ohne LaTeX-Fehler und ohne unaufgelöste Verweise.

