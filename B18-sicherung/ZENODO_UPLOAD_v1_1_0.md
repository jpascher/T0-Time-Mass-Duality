# Zenodo-Upload-Checkliste für v1.1.0

Diese Datei dokumentiert alles, was für den Zenodo-Upload v1.1.0 vorbereitet werden muss, und listet exakt, welche Stellen nach DOI-Vergabe aktualisiert werden müssen.

**Status:** vorbereitet, nicht hochgeladen.
**Geplant für:** 2026-05-11.
**Vorgänger-DOI (v1.0.14):** 10.5281/zenodo.20041543.

---

## 1. Was hochzuladen ist

Der Zenodo-Upload v1.1.0 sollte enthalten:

- **`RELEASE_NOTES_v1_1_0.md`** — englische konsolidierte Release-Notes (274 Zeilen, 22 KB)
- **`RELEASE_NOTES_v1_1_0_de.md`** — deutsche konsolidierte Release-Notes (274 Zeilen, 23 KB)
- **Aktualisierte `README.md`** und **`README_de.md`** mit dem v1.1.0-Hinweis-Block nach dem DOI-Badge
- **Voller GitHub-Repository-Snapshot** zum Tag-Zeitpunkt (alle PDFs, LaTeX-Quellen, HTML-Tools, Python-Skripte, Audio-Dateien)

GitHub-Tag empfohlen: `v1.1.0` (parallel zu Zenodo-Release).

---

## 2. Zenodo-Metadaten (Vorschlag)

### 2.1 Pflichtfelder

**Title:**
```
T0-Time-Mass-Duality / FFGFT v1.1.0 — Hilbert-Space Bridge: A Consolidated Release
```

**Creators:**
- Name: Pascher, Johann
- Affiliation: Independent researcher, Austria
- ORCID: 0009-0000-6518-4064

**Publication date:** 2026-05-11

**Resource type:** Software / Other (Zenodo erlaubt beides für Mixed-Content-Repositories)

**Description / Abstract:**
```
T0/FFGFT (Fundamental Fractal-Geometric Field Theory) is a unified geometric framework
for quantum mechanics, relativity, and cosmology. The framework derives all Standard-Model
constants from a single dimensionless parameter ξ = 4/30000, anchored by the foundational
relation T̃ · m = 1.

v1.1.0 is a consolidated major release built on the four point releases v1.0.11–v1.0.14.
Its centrepiece is the Hilbert-Space Triptych (Docs 230, 231, 232):

— Doc 230 establishes a carried-out bijection between FFGFT mode formalism and standard
  Hilbert-space quantum mechanics on the qubit sector, with a testable Δ_CHSH ≈ 10⁻⁵
  deviation from the K_frak ≈ 0.9867 correction.

— Doc 231 identifies the four established mathematical structures (SU_q(2) with
  q = e^(iπ/75), Kac-Moody winding states, spinor bundles, Kaluza-Klein) needed
  to carry full FFGFT natively in Hilbert-space language.

— Doc 232 sketches Quantum Graphity (Konopka, Markopoulou, Severini 2008) as a
  hypothetical subset of FFGFT through five reduction steps, explicitly marked
  as plausibility sketch, not proved theorem.

The release further consolidates the Triangle-Matrix Reduction Theorem (Doc 206),
algebraic bridges to consciousness discussions (Doc 207), winding-structure
clarification (Doc 210), and the quantitative falsification trilogy for Casimir
(Doc 220), redshift (Doc 221), and lithium abundance (Doc 222).

The corpus is presented as three layers with distinct methodological status:
core derivations proved from ξ, external bridges algebraically or structurally
proved, and hypothetical reductions as plausibility sketches.
```

**Keywords (free-text):**
```
FFGFT, T0-Time-Mass-Duality, unified field theory, fine structure constant,
fractal spacetime, Hilbert-space bijection, Bloch sphere, Pauli matrices,
qubit, CHSH, quantum groups, SU_q(2), Kac-Moody, spinor bundles, Kaluza-Klein,
Quantum Graphity, triangulation, emergent geometry, ξ parameter, T̃·m=1,
muon g-2, Hubble tension, Casimir, redshift, lithium, falsification criteria
```

**Communities:** (optional)
- Keine spezifische Community-Zuordnung erforderlich; bestehende Releases
  v1.0.11–v1.0.14 sind ebenfalls standalone.

**License:** Same as previous releases. Empfehlung: Creative Commons Attribution
4.0 International (CC BY 4.0) für Texte und Dokumente, MIT für Python-Code.

**Related identifiers:**
- IsNewVersionOf: 10.5281/zenodo.20041543 (v1.0.14)
- IsSupplementTo: alle Vorgänger-DOIs als historische Kontextverweise
  - 10.5281/zenodo.20041529 (v1.0.13)
  - 10.5281/zenodo.20022166 (v1.0.12)
  - 10.5281/zenodo.18834145 (v1.0.11)

### 2.2 Optionale Felder

**Funding:** keine
**Conference / Journal / Book:** keine
**References:** in den Release-Notes selbst enthalten (Konopka-Markopoulou-Severini 2008
für Doc 232, Drinfeld-Jimbo 1985 für Doc 231, Adlam-McQueen-Waegell für Doc 207)

**Custom metadata für GitHub-Integration:**
Falls automatischer Upload via GitHub-Zenodo-Integration: `.zenodo.json` im
Repository-Root mit oben genannten Feldern, um manuelle Eingabe zu vermeiden.

---

## 3. DOI-Update-Stellen nach Vergabe

Sobald Zenodo eine DOI vergeben hat (Format: `10.5281/zenodo.XXXXXXXX`), müssen
folgende Stellen aktualisiert werden:

### 3.1 RELEASE_NOTES_v1_1_0.md (englisch)

| Zeile | Stelle | Vorher | Nachher |
|-------|--------|--------|---------|
| 5 | Header **DOI:** | `TBA — to be assigned upon Zenodo release` | `[10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX)` |
| 248 | Version history table, Zeile v1.1.0 | `**TBA**` | `**[10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX)**` |
| 256 | How to cite, erste Vorlage | `DOI: TBA upon Zenodo release.` | `DOI: [10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX).` |
| 274 | Letzter Vermerk | `To be updated upon Zenodo release with the v1.1.0 DOI.` | `Zenodo DOI assigned: 10.5281/zenodo.XXXXXXXX.` |

### 3.2 RELEASE_NOTES_v1_1_0_de.md (deutsch)

| Zeile | Stelle | Vorher | Nachher |
|-------|--------|--------|---------|
| 5 | Header **DOI:** | `TBA — wird bei Zenodo-Release vergeben` | `[10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX)` |
| 248 | Versionsgeschichte, Zeile v1.1.0 | `**TBA**` | `**[10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX)**` |
| 256 | Wie zu zitieren, erste Vorlage | `DOI: TBA bei Zenodo-Release.` | `DOI: [10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX).` |
| 274 | Letzter Vermerk | `Wird bei Zenodo-Release mit der v1.1.0-DOI aktualisiert.` | `Zenodo-DOI vergeben: 10.5281/zenodo.XXXXXXXX.` |

### 3.3 README.md und README_de.md

DOI-Badge in beiden Dateien (Zeile 3) auf neue v1.1.0-DOI aktualisieren:

**Vorher:**
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20041543.svg)](https://doi.org/10.5281/zenodo.20041543)
```

**Nachher:**
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)
```

Auch die Abstract-Zeile (englisch Z. 12 / deutsch Z. 11) am Ende: `DOI: 10.5281/zenodo.20041543.`
→ `DOI: 10.5281/zenodo.XXXXXXXX.`

### 3.4 Schnell-Befehl für die Aktualisierung

Sobald die neue DOI bekannt ist (z.B. `10.5281/zenodo.20050000`):

```bash
NEW_DOI=20050000

# Vier Dateien in einem Rutsch aktualisieren
for f in RELEASE_NOTES_v1_1_0.md RELEASE_NOTES_v1_1_0_de.md README.md README_de.md; do
  sed -i "s|10\.5281/zenodo\.20041543|10.5281/zenodo.$NEW_DOI|g" "$f"

  # In den Release-Notes: TBA-Platzhalter ersetzen
  if [[ "$f" == RELEASE_NOTES_v1_1_0* ]]; then
    sed -i \
      -e "s|TBA — to be assigned upon Zenodo release|[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)|" \
      -e "s|TBA — wird bei Zenodo-Release vergeben|[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)|" \
      -e "s|\\*\\*TBA\\*\\*|**[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)**|" \
      -e "s|DOI: TBA upon Zenodo release\\.|DOI: [10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI).|" \
      -e "s|DOI: TBA bei Zenodo-Release\\.|DOI: [10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI).|" \
      -e "s|To be updated upon Zenodo release with the v1\\.1\\.0 DOI\\.|Zenodo DOI assigned: 10.5281/zenodo.$NEW_DOI.|" \
      -e "s|Wird bei Zenodo-Release mit der v1\\.1\\.0-DOI aktualisiert\\.|Zenodo-DOI vergeben: 10.5281/zenodo.$NEW_DOI.|" \
      "$f"
  fi
done

# Kontrolle: sollte keine TBA-Stellen mehr finden
grep -n "TBA" RELEASE_NOTES_v1_1_0*.md
```

**Achtung:** Der README-DOI-Badge zeigt aktuell auf v1.0.14 (20041543). Nach v1.1.0-Upload muss er auf die neue v1.1.0-DOI aktualisiert werden. Die v1.0.14-DOI bleibt aber in den RELEASE_NOTES_v1_1_0.md als Predecessor-Referenz erhalten — der `sed`-Befehl oben würde das überschreiben. Daher entweder den `sed`-Befehl nur auf README* anwenden, oder die Predecessor-Zeile nach dem Befehl manuell wiederherstellen.

### 3.5 Sichere Version des Befehls

Damit die Predecessor-Referenz in den RELEASE_NOTES nicht zerstört wird:

```bash
NEW_DOI=20050000

# Nur READMEs: alle 20041543-Vorkommen ersetzen
for f in README.md README_de.md; do
  sed -i "s|10\.5281/zenodo\.20041543|10.5281/zenodo.$NEW_DOI|g" "$f"
done

# Release-Notes: nur TBA-Platzhalter ersetzen, Predecessor-Refs nicht anrühren
for f in RELEASE_NOTES_v1_1_0.md RELEASE_NOTES_v1_1_0_de.md; do
  sed -i \
    -e "s|TBA — to be assigned upon Zenodo release|[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)|" \
    -e "s|TBA — wird bei Zenodo-Release vergeben|[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)|" \
    -e "s|\\*\\*TBA\\*\\*|**[10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI)**|" \
    -e "s|DOI: TBA upon Zenodo release\\.|DOI: [10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI).|" \
    -e "s|DOI: TBA bei Zenodo-Release\\.|DOI: [10.5281/zenodo.$NEW_DOI](https://doi.org/10.5281/zenodo.$NEW_DOI).|" \
    -e "s|To be updated upon Zenodo release with the v1\\.1\\.0 DOI\\.|Zenodo DOI assigned: 10.5281/zenodo.$NEW_DOI.|" \
    -e "s|Wird bei Zenodo-Release mit der v1\\.1\\.0-DOI aktualisiert\\.|Zenodo-DOI vergeben: 10.5281/zenodo.$NEW_DOI.|" \
    "$f"
done

# Kontrolle: sollte leer sein
grep -nE "TBA" RELEASE_NOTES_v1_1_0*.md
```

---

## 4. Reihenfolge der Schritte

1. **GitHub-Commit** mit allen v1.1.0-Materialien (Release-Notes, README-Updates) auf `main`-Branch
2. **GitHub-Tag** `v1.1.0` setzen (löst bei aktiver GitHub-Zenodo-Integration den Zenodo-Upload automatisch aus)
3. **Auf Zenodo warten**, bis die DOI vergeben ist (typisch wenige Minuten)
4. **DOI-Update-Befehl** aus §3.5 ausführen
5. **Zweiten Commit** mit den DOI-Updates pushen
6. **Outreach-Mail** an IPI-Mailingliste mit der neuen DOI versenden

---

*Vorbereitet am 2026-05-11. Zu löschen oder zu archivieren, sobald v1.1.0 vollständig veröffentlicht ist.*
