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

## Revision August 2026 — Dok. 339 und Dok. 340 (Galois-Neutrino-Sektor)

**Datum:** 30. August 2026

### Dok. 339 — Frobenius-Trennung massiv/masselos in GF(27)*

Neue Ableitung der massiv/masselosen Trennung aus der Frobenius-Struktur:

- GF(27)* ≅ Z₂₆ ≅ Z₂ × Z₁₃ (chinesischer Restsatz) [B]
- Fixpunkte {+1,−1} unter φ:x↦x³ = massiver Z₂-Sektor (Teilchen/Antiteilchen) [B]
- 8 Dreier-Orbits = 8 Gluonen (adjungierte SU(3)-Darstellung) [K]
- Fixkörper GF(3)* = Photon (U(1)) [K]
- Orbit₄ = 2⁻¹·Orbit₁ in Z₁₃ [B]
- Konforme Skalierung k↦3k im Typ-III-Pullback [K]
- Prüfskript: pruef_339_frobenius.py (6/6 Assertions)

### Dok. 340 — Neutrino-Massenhierarchie aus GF(27)*

Ableitung beider gemessener Δm²-Werte aus dem 4. Frobenius-Orbit:

**Algebraisch bewiesen [B]:**
- Orbit₄ = 2⁻¹·Orbit₁: {7,8,11} = 7·{1,3,9} (mod 13)
- Δm²_sol = (|Z₁₃|−2)/3 · m_ν² = 11/3 · m_ν² (Abw. 0.46 %)
- Orbit₃ selbstinvers → Majorana-Charakter; Σ(Orbit₃) = 26 = |GF(27)*|
- Branching-Rule ρ₄↓_A₄ = ρ₃^A₄ ⊕ ρ₁^A₄ → W-Richtung A₄-invariant
- p_vent = |A₅:A₄| / Kissing(D₄) = 5/24

**Konsistent [K]:**
- Δm²_atm = 120·m_ν² = (11²−1)·m_ν² (Abw. 1.0 %)
- Neutrinomassen (normale Hierarchie): m₁=4.54, m₃=9.81, m₂=49.96 meV
- Σm_i = 64.3 meV < 120 meV (Planck 2018) ✓
- cos²(2π·2/13) ≈ sin²θ₁₂ (Abw. 5.1 %), cos²(2π·5/13) ≈ sin²θ₂₃ (Abw. 2.8 %)
- m_ee ≈ 7.1 meV < 36 meV (KamLAND-Zen) ✓
- SICC-Venting-Formel (p=5/24, κ=12·m_ν) ≡ Standard-Oszillationsformel

**Falsifizierbare Vorhersagen:**
1. Neutrinomassen m₁=4.54, m₃=9.81, m₂=49.96 meV (CMB-S4, Euclid)
2. Ratio Δm²_atm/Δm²_sol = 32.73 (gemessen: 33.20)
3. Sterile Neutrinos (Majorana): m_min = 4·m_ν = 18.2 meV (IceCube, SBN, BEST)

**Prüfskript:** pruef_340_neutrino_galois.py (10/10 Assertions)

### Neue Dateien (Dok. 339 + 340)
```
Sources/ch/339_Frobenius_Trennung_{De,En}_ch.tex
Sources/ch/340_Neutrino_Galois_{De,En}_ch.tex
Sources/wr_standalone_A4/339_Frobenius_Trennung_{De,En}.tex
Sources/wr_standalone_A4/340_Neutrino_Galois_{De,En}.tex
pdf/339_Frobenius_Trennung_{De,En}.pdf
pdf/340_Neutrino_Galois_{De,En}.pdf
python/Dok332_Skripte/pruef_339_frobenius.py
python/Dok332_Skripte/pruef_340_neutrino_galois.py
python/Dok332_Skripte/sicc_kappa_analysis.py
```
