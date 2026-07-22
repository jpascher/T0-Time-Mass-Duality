# Release Notes — v1.2.4 (Juli 2026)

**DOI:** (wird beim Zenodo-Upload vergeben — löst v1.2.3 · [10.5281/zenodo.21396624](https://doi.org/10.5281/zenodo.21396624) ab)

Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**  
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**  
A-Serien-Protokoll: **[A_Serie_Export/A_SERIE_CHANGELOG.md](A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fraktale Feldgeometrische Fundamentaltheorie** zeigt:
Alle Konstanten des Standardmodells folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Was ist neu in v1.2.4

v1.2.4 führt die **A-Serie** ein — die kanonische, sachgeordnete Fassung
der FFGFT. Alle 43 Dokumente tragen explizite Schichtmarkierungen
([SETZUNG] / [K] / [B] / [S]); jede berechenbare Aussage hat ein
Prüfskript. Drei theoretische Fortschritte bilden den inhaltlichen Kern
dieses Releases.

### Chiralität g_R = 0 algebraisch bewiesen — A095 (neu)

Die Linkshändigkeit der schwachen Wechselwirkung war bisher eine [S]-Skizze.
**A095** hebt sie auf [B] an: der Fourier-Projektor P₊ auf dem kompakten
Torus annihiliert den |1,−1⟩-Windungszustand. Sein Kern ist nicht-trivial
und g_R = ⟨0|H|0⟩ = 0 folgt direkt — kein freier Parameter, keine
zusätzliche Annahme jenseits der Torus-Geometrie.
Prüfskript: `a095_torus_chiralitaet.py`.

### Eichsektor aus Torus-Topologie — A192 (neu)

Zwei der drei Eichgruppen des Standardmodells sind jetzt auf [B]-Niveau
hergeleitet:

- **U(1)_EM:** Flussquantisierung Φ = n · h/e auf dem kompakten Torus
  erzwingt die Aharonov-Bohm-Phase und liefert die elektromagnetische
  Eichgruppe.
- **SU(3)_C:** drei Fäden mit Verschlingungszahl 3 erzeugen genau
  6 + 2 = 8 Gell-Mann-Generatoren; dim(su(3)) = 8 ist geometrisch
  aus der Windungsstruktur bewiesen, ohne Eingabe aus dem Standardmodell.
- **SU(2)_L:** aus der chiralen Projektion von A095.

Offene Kante: die kovarianten Ableitungen D_μ = ∂_μ + igA_μ^aT^a
sind noch nicht explizit ausgeschrieben.
Prüfskript: `a192_eichsektor.py`.

### Native Zeit-Energie-Reziprozität — A060, Registereintrag R50

Das frühere Argument gegen einen singulären Anfang (Dok. 025/063) war aus
der Heisenbergschen Energie-Zeit-Unschärfe geborgt. Drei Defekte wurden
identifiziert: invertierte Implikation (endliches Δt liefert eine
*endliche* Schranke, nicht ΔE → ∞); Anwendungsfehler (Pauli: kein
selbstadjungierter Zeitoperator; Mandelstam-Tamm-Δt ist eine
Änderungszeit, keine kosmische Dauer); Stilverstoß.
Die ersetzende Kette ist vollständig nativ:

T̃ · m = 1, also **T · E = 1** (eine Gleichung, keine Ungleichung).  
E → ∞ ⟺ T → 0; aber FFGFTs Zeit trägt ein minimales Inkrement
**d₁ = 100ξ₁ = 1/75**, allein von ξ fixiert. Daher ist E nach oben
beschränkt und eine unendliche Energiedichte strukturell ausgeschlossen —
die Konklusion von Dok. 025/063 ist unverändert, die Herleitung jetzt nativ.

Als **R50** in Dok. 190 eingetragen. Dok. 025/063 sind für diesen Punkt
nicht mehr maßgeblich; die native Kette in A060 ersetzt sie.

### CHSH-Vorfaktor ξ/(2π) geometrisch hergeleitet — A160

Der Faktor 2π ist der Kreisumfang des Einheitskreises — die natürliche
Umrechnung zwischen der Torus-Windungsphase und dem Messwinkel. Die
kumulative Formel CHSH(n) = 2√2 · exp(−ξ ln n / D_f) integriert über
D_f fraktale Dimensionen; ln(n) zählt die Verschränkungstiefe
logarithmisch; D_f im Nenner kodiert die fraktale Selbstkonsistenz.
Beide Faktoren sind jetzt [B].

Hardware-Stand: IBM Heron r2 (Mai 2026) bestätigt Bell-Verletzung
(S = 2,74, 96,9 % des Tsirelson-Werts). Der ξ-Effekt (~10⁻⁵) liegt unter
der Gerät-zu-Gerät-Variation (~1,4 %) um Faktor ~1400 — mit heutiger
NISQ-Hardware prinzipiell nicht auflösbar (A165).

### Higgs-EFT-Abweichung erklärt — A130

Die 2,3%-Lücke zwischen dem ξ-abgeleiteten α und dem elektroschwachen
Präzisionswert wird strukturell erklärt [S]: SI-Werte sind schemaabhängig
(1-Loop), und fraktale Korrekturen in v nicht sauber von der
Schleifenstruktur trennbar. ξ_EFT / K_frak^(3/2) ≈ 1,330 × 10⁻⁴; der
verbleibende Rest beträgt 0,3 %. Das ist eine strukturelle Erklärung,
kein Beweis.

---

## Die A-Serie im Überblick

| Block | Dokumente | Thema |
|-------|-----------|-------|
| 0 | A010–A095 (13) | Grundlage: Setzungen, Geometrie, Einheiten, Zeit |
| 1 | A100–A192 (16) | Sektoren: Leptonen, Konstanten, Gravitation, QM, SM |
| 2 | A200–A250 (6) | Methodik: Schichten, Falsifizierbarkeit, offene Punkte |
| 3 | A260–A267 (8) | Erweiterungen: Casimir, Skalenhierarchie, Dirac |

43 Dokumente × 2 Sprachen = 86 Quelltexte + 86 PDFs + 44 Prüfskripte.
Alle Dateien in **[A_Serie_Export/](A_Serie_Export/)**.

---

## Korrekturregister-Einträge (dieses Release)

| Eintrag | Betrifft | Beschreibung |
|---------|---------|--------------|
| R50 | Dok. 025/063/061/064/078 | Heisenberg-Singularitäts-Argument durch native T·E = 1-Kette ersetzt (A060) |

---

## Versionshistorie

| Version | DOI | Schwerpunkt |
|---------|-----|-------------|
| v1.2.4 | (ausstehend) | **A-Serie:** 43 kanonische Dokumente; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Informationsfrage (Dok. 301/302); natives T·E=1 (Dok. 306, R50–R53); Zeit im Zustandsraum (Dok. 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM als dekompaktifizierte Projektion (Dok. 298); K_frak = 74/75 (Dok. 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Zeit-Windung als Hilbertraum-Gedächtniskern (Dok. 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 als C₃-in-A₅-Geometrie-Invariant (Dok. 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Leptonsektor-Audit; α Zwei-Wege-Überbestimmung (Dok. 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbertraum-Bijektion (Dok. 230/231/232) |

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*
