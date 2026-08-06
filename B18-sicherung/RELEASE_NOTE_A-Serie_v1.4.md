# FFGFT A-Serie v1.4 — Release Note

**Fraktale Feldgeometrische Fundamentaltheorie / T0 Zeit-Masse-Dualität**
Johann Pascher · ORCID 0009-0000-6518-4064 · 2026-07-27

Konzept-DOI (alle Versionen): 10.5281/zenodo.20117635
Repository: github.com/jpascher/T0-Time-Mass-Duality

---

## Deutsch

### Was ist die A-Serie?

Die A-Serie ist die kanonische, sachgeordnete Fassung der FFGFT: mehr als 300
Altdokumente, zusammengeführt in **48 thematisch geordneten Dokumenten** — ein
Thema an einem Ort, jede Aussage mit Schichtstatus markiert, alle Korrekturen
eingearbeitet. Sie ersetzt den Altbestand nicht physisch; die alten Nummern
bleiben zitierbar. Die A-Serie ist die Fassung, die man liest, wenn man wissen
will, was die Theorie heute behauptet.

### Was ist neu in v1.4

Dies ist ein **Konsolidierungs-Release ohne inhaltliche Änderung an den
Dokumenten**. Korrigiert wird eine Zählungs- und Listungslücke:

- **A155 (Meson-Sektor) nachgetragen.** A155 war in der Blockstruktur des README
  nicht gelistet, obwohl PDF, Quelltexte (De + En) und Prüfskript
  (`a155_meson.py`) vorhanden und vollwertiger Teil von Block 1 sind. A155 steht
  jetzt korrekt in der Blockstruktur (nach A150). Die kanonische Zählung geht
  damit von 47 auf **48 Dokumente** (96 PDFs De + En, 48 Prüfskripte).

- **Doppel-Nummerierung bereinigt.** A280 / A281 / A282 (Altstände der
  Thermodynamik-Trilogie Landauer / Träger und Information / Rechenkugel) sind
  aus dem kanonischen Objekt ausgeschlossen; die Trilogie wird unter
  A271 / A272 / A273 geführt. Das verirrte Skript `a282_rechenkugel.py` (Dublette
  von `a273_rechenkugel.py`) entfällt.

### Umfang des eingefrorenen Objekts

48 kanonische Dokumente A010–A273, je De + En (96 PDFs), 96 LaTeX-Quelltexte,
48 parameterfreie Prüfskripte, gemeinsame Preamble-Dateien sowie README,
CHANGELOG und WORKFLOW. Jedes Dokument ist ein eigenständiges PDF mit
Schichtstatus je Aussage; jede numerische Aussage ist mit dem beiliegenden
Skript nachrechenbar.

### Blockstruktur (48 Dokumente)

- **Block 0 — Grundlage (A010–A095):** Zweck, ξ-Ursprung, drei Setzungen,
  kompakte Geometrie T⁴/Z₃, fraktale Korrektur, Rekursion, Zeit (T·E = 1),
  Hilbertraum-Brücke, Feldtheorie, Einheiten, Projektionskette, Chiralität.
- **Block 1 — Sektoren (A100–A192):** Leptonleiter, Koide Q = 2/3, θ = 2/9,
  Feinstruktur α = ξ·E₀², g−2, Gravitation und G, Quarks/Neutrinos,
  **Meson-Sektor (A155)**, Quantenmechanik auf T⁴ (Bell als Topologie),
  Information (Windungsquant), Standardmodell als Projektion, Eichsektor.
- **Block 2 — Methodik und Bilanz (A200–A250):** Ordnung ohne Rangordnung,
  Falsifizierbarkeit, Toleranzmaßstab, offene Punkte, Abgrenzung, Verweistabelle.
- **Block 3 — Erweiterungen (A260–A273):** Casimir, Skalenhierarchie,
  c-Konvention, Dirac, strukturelle Asymmetrien, Rotverschiebung,
  Einheitenprüfung, Stipulation α = 1, Z₃-Sektor, Thermodynamik-Trilogie
  (Landauer, Träger und Information, Rechenkugel).

### Datei-Identität des Release-Archivs

```
Datei:      FFGFT_A-Serie_v1.4.zip
Byte-Größe: 11326512
SHA-256:    b82c1996a8ed86a98ee4380a06f5f27e9e73819a165144dd530896398db12190
MD5:        50f3f07902d437550733d442cf8dae1a
```

Ein Pro-Datei-SHA-256-Manifest (`MANIFEST_v1.4.txt`, 346 Zeilen) begleitet das
Archiv als eigene Datei — bewusst außerhalb des ZIP gehalten, damit der
Archiv-Hash nicht selbstbezüglich wird.

---

## English

### What is the A-Series?

The A-Series is the canonical, topic-ordered edition of FFGFT: more than 300
legacy documents consolidated into **48 thematically ordered documents** — one
topic in one place, every claim marked with its layer status, all corrections
incorporated. It does not physically replace the legacy corpus; the old numbers
remain citable. The A-Series is the version you read to learn what the theory
claims today.

### What is new in v1.4

This is a **consolidation release with no content change to the documents**. It
corrects a counting and listing gap:

- **A155 (meson sector) added to the listing.** A155 was absent from the README
  block structure although its PDF, sources (De + En) and verification script
  (`a155_meson.py`) exist and are a full part of Block 1. A155 is now correctly
  placed in the block structure (after A150). The canonical count therefore moves
  from 47 to **48 documents** (96 PDFs De + En, 48 verification scripts).

- **Duplicate numbering cleaned up.** A280 / A281 / A282 (legacy copies of the
  thermodynamics trilogy Landauer / Carrier and Information / Reckoning Bead) are
  excluded from the canonical object; the trilogy is carried under
  A271 / A272 / A273. The stray script `a282_rechenkugel.py` (duplicate of
  `a273_rechenkugel.py`) is removed.

### Scope of the frozen object

48 canonical documents A010–A273, each De + En (96 PDFs), 96 LaTeX sources,
48 parameter-free verification scripts, shared preamble files, plus README,
CHANGELOG and WORKFLOW. Each document is a self-contained PDF with a per-claim
layer status; every numerical claim is reproducible with the accompanying script.

### File identity of the release archive

```
File:      FFGFT_A-Serie_v1.4.zip
Byte size: 11326512
SHA-256:   b82c1996a8ed86a98ee4380a06f5f27e9e73819a165144dd530896398db12190
MD5:       50f3f07902d437550733d442cf8dae1a
```

A per-file SHA-256 manifest (`MANIFEST_v1.4.txt`, 346 lines) accompanies the
archive as a separate file — deliberately kept outside the ZIP so the archive
hash is non-circular.

---

## Verifikation / Verification

Nach dem Zenodo-Deposit die deponierte Datei erneut herunterladen und prüfen,
dass exakt der obige SHA-256 reproduziert wird. / After the Zenodo deposit,
re-download the deposited file and confirm it reproduces exactly the SHA-256
above.

```
sha256sum FFGFT_A-Serie_v1.4.zip
# erwartet / expected:
# b82c1996a8ed86a98ee4380a06f5f27e9e73819a165144dd530896398db12190
```

Windows:
```
certutil -hashfile FFGFT_A-Serie_v1.4.zip SHA256
```
