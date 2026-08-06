# Release Notes — v1.2.5 (Juli 2026)

**DOI:** *(wird beim Zenodo-Upload vergeben)* (löst v1.2.4 · [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379) ab)

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

## Was ist neu in v1.2.5

v1.2.5 erweitert Block 3 der A-Serie um die **Thermodynamik der
Berechnung**: A271 überarbeitet, A272 und A273 neu. Alle drei
Dokumente deklarieren ausdrücklich **FFGFT-Berührung: keine** — sie
argumentieren auf der Ebene der statistischen Mechanik, das ξ-Schema
wird nicht berührt (eigene Ebene, eigene Buchhaltung, P20/P39-analog).
Dazu kommt ein neuer Schichtmarker für korpusexterne Belege.

### Die Schranke hängt am Gebiet, nicht an der Beschreibung — A271 (überarbeitet)

Landauers Prinzip wird als Aussage über **Gebiete im Phasenraum**
entwickelt, nicht über Information. Die Kette ist kurz:
Gebietsreduktion verkleinert das Volumen; Liouville verbietet
Volumenschrumpfung im abgeschlossenen System; also muss ein Bad das
Volumen übernehmen, und der Preis ist Wärme
Q ≥ k_B·T·ln(W_vorher/W_nachher) — das ln2 ist der Binär-Spezialfall,
nicht die Physik. Gezählt wird nach **Unterscheidbarkeit**
(Orthogonalität), nicht nach Energie; die absolute
Grund-Diskretisierung liefert h^f.

Daraus folgt unmittelbar die **Inhaltsneutralität**: Die Thermodynamik
zählt Gebiete und liest sie nicht. Ein Prozessor, der 2+2=4 rechnet,
und einer, der 2+2=5 rechnet, schalten dieselben Gebiete und zahlen
dieselbe Rechnung ans Bad. Es gibt keinen thermodynamischen
Wahrheitsdetektor.

Präzisiert gegenüber der Vorfassung: Hinreichend für die
Wärmeproduktion ist die **Nicht-Bijektivität der Gebietsabbildung** —
nicht die logische Irreversibilität. Mit der Gebietsabbildung fällt
diese nur unter einer ausdrücklich zu deklarierenden
Realisierungsannahme zusammen (disjunkte Gebiete, kein mitgeführtes
Gebiet); ohne sie trägt sie nichts, weil Bennett jede logisch
irreversible Funktion als Folge volumenerhaltender Abbildungen
ausführt.

Drei Ebenen werden strikt getrennt — Konstruktion (Ingenieur),
Zustandsübergang (Takt), Beschreibung (Programm). Daraus folgt, dass
ein realer Rechner nicht diskret Bits löscht, sondern einen
kontinuierlichen Entropiestrom trägt (DRAM-Refresh,
Qubit-Dekohärenz): der Rechner zahlt Entropie dafür, dass er
existiert, nicht nur dafür, dass er rechnet.

Der epistemische Vorbehalt ist ausdrücklich gebucht: nicht messbar
heißt nicht nicht vorhanden. Landauer gilt wegen der Mechanik
(Liouville), nicht wegen Unwissenheit; die Irreversibilität ist
statistisch, nicht ontologisch absolut (Maxwells Dämon, Bennetts
Auflösung).

Prüfskript `a271_landauer.py` (Checks 1–10).

### Träger und Information — A272 (neu)

Textkritik zu A271. Was Landauers Arbeit von 1961 beweist, ist eine
untere Schranke für **Träger-Operationen** an einem thermischen
Gleichgewichts-Ensemble — keine universelle Aussage über abstrakte
Information. Zwei Sätze tragen das:

- **Satz 1** (Mehrfachrealisierung): Einem Informationsbit kann keine
  Energie zugeordnet werden, nur seinem Träger. Derselbe
  Informationsgehalt lässt sich mit 5 V, mit 1 V, mit einem Spin oder
  mit einem Photon realisieren; die Energie variiert, der Gehalt
  nicht.
- **Satz 2**: Eine rein interpretative Löschung verkleinert den
  Träger-Zustandsraum nicht — sie kostet daher nichts.

Ausdrücklich als **Zuständigkeitsbefund** gefasst, nicht als
Widerlegung: Für die physikalische Operation, die Landauer betrachtet,
ist sein Ergebnis korrekt. Bestritten wird die Zuständigkeit dieses
Ergebnisses für einen Gegenstand, über den es keine Aussage macht.

Dazu: Landauers **eigener Ensemble-Vorbehalt** aus der Originalarbeit
dokumentiert und die Rezeptionsgeschichte der Verallgemeinerung
nachgezeichnet (Lairez, Norton, Earman/Norton, Hemmo/Shenker);
Sprachkritik der Digitaltechnik (Tabelle Träger vs. Information);
Hypostasierung als Deutungsrahmen [S]. Rückkopplungsschranke
Q_min = kT(ln2 − I) mit I dimensionslos in nat; das Wissen I ist
selbst trägergebunden, der Preis wird verschoben, nicht vermieden.

Enthält das verbindliche **Wörterbuch A271 ↔ A272** (Gebiet = Träger,
Beschreibung = Information), damit im Korpus keine zwei parallelen
Terminologien für einen Sachverhalt entstehen.

### Die Rechenkugel — A273 (neu)

Token-Rechnen (Abakus, Muscheln, Münzen) als Grenzfall, an dem
Landauers Argument in seine **zwei unabhängigen Hälften** zerfällt.

Die **Buchhaltung** gilt dort exakt und ist zum ersten Mal sichtbar:
Der Vorrat, aus dem die Marken kommen und in den sie zurückfließen,
ist ein Bad, auf das man zeigen kann; Marken bleiben erhalten
(Liouville-Analogon, abzählbar); ΔS/k_B = N·ln2 trägerunabhängig.

Die **thermische Umrechnung** ΔS → Q = T·ΔS gilt dort nicht: Eine
Abakuskugel kostet beim Verschieben rund 5,1·10¹⁵ mal die
Landauer-Grenze, ihr Positions-Bit trägt 3,8·10⁻²³ ihrer eigenen
thermischen Entropie, und ihre Positionsbarriere liegt bei
3,6·10¹⁵ k_B·T. Der Token-Rechner fällt damit unter genau den
Vorbehalt, den Landauer selbst formuliert hat.

Daraus die Ordnung, die der Intuition zuwiderläuft:
**Sichtbarkeit der Struktur und Bindekraft der Zahl laufen
gegenläufig.** Je primitiver der Träger, desto klarer die Buchhaltung
und desto irrelevanter die Schranke.

Zwei Böden werden getrennt: der thermische k_B·T und der
quantengeometrische ħc/L; maßgeblich ist der größere. Für massive
mechanische Träger ist ħ²/(2mL²) die einschlägige Quantenskala und
irrelevant (Kugel 2,7·10⁻⁴¹ k_B·T, Kolloid 1,6·10⁻²² k_B·T); bei
300 K schneiden sich beide Böden bei 7,6 µm; beim Qubit führt der
quantengeometrische (hf/k_B·T = 24 bei 5 GHz und 10 mK). Der
Grenzübergang ist stetig und ausrechenbar: kritische Markenmasse
k_B·T/(μ·g·d) = 1,4·10⁻¹⁹ kg.

Zusätzlich der **Markenvorrat als eigene Kostenkategorie**: eine
Materialschranke ohne Untergrenze in k_B·T, stehender Bestand statt
laufendem Strom. Beim Halbleiter fällt sie aus dem Blick, weil der
Vorrat in Silizium eingegossen ist [S].

Prüfskript `a273_rechenkugel.py` (Checks 1–14, alle BESTANDEN).

### Neuer Schichtmarker [Q]

Die A-Serie argumentiert sonst durchgehend ξ-intern und brauchte
deshalb keine Kategorie für korpusexterne Belege. A271–A273 sind die
ersten Dokumente, die Fremdliteratur und Messwerte zitieren. Neu daher:

| Marke | Bedeutung |
|-------|-----------|
| **[Q]** | Quelle — korpusexterne Primärquelle oder Messwert |

**[K]** (Kern — aus ξ hergeleitet, numerisch geprüft) behält
korpusweit seine Bedeutung und kommt in A271–A273 nicht vor.

---

## Die A-Serie im Überblick

| Block | Dokumente | Thema |
|-------|-----------|-------|
| 0 | A010–A095 (13) | Grundlage: Setzungen, Geometrie, Einheiten, Zeit |
| 1 | A100–A192 (16) | Sektoren: Leptonen, Konstanten, Gravitation, QM, SM |
| 2 | A200–A250 (6) | Methodik: Schichten, Falsifizierbarkeit, offene Punkte |
| 3 | A260–A273 (12) | Erweiterungen: Casimir, Skalenhierarchie, Dirac, Z₃-Sektor, Thermodynamik der Berechnung |

47 Dokumente × 2 Sprachen = 94 Quelltexte + 94 PDFs + 47 Prüfskripte.
Alle Dateien in **[A_Serie_Export/](A_Serie_Export/)**.

---

## Korrekturregister-Einträge (dieses Release)

Keine. Die Änderungen betreffen ausschließlich A-Serien-Dokumente ohne
ξ-Berührung; das Korrekturregister (Dok. 190) bleibt bei R60.

---

## Versionshistorie

| Version | DOI | Schwerpunkt |
|---------|-----|-------------|
| v1.2.5 | *(beim Upload)* | **Thermodynamik der Berechnung:** A271 (Schranke am Gebiet, nicht an der Beschreibung); A272 (Träger vs. Information); A273 (Token-Rechnen als Grenzfall); neuer Marker [Q] |
| v1.2.4 | [21496379](https://doi.org/10.5281/zenodo.21496379) | **A-Serie:** 43 kanonische Dokumente; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Informationsfrage (Dok. 301/302); natives T·E=1 (Dok. 306, R50–R53); Zeit im Zustandsraum (Dok. 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM als dekompaktifizierte Projektion (Dok. 298); K_frak = 74/75 (Dok. 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Zeit-Windung als Hilbertraum-Gedächtniskern (Dok. 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 als C₃-in-A₅-Geometrie-Invariant (Dok. 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Leptonsektor-Audit; α Zwei-Wege-Überbestimmung (Dok. 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbertraum-Bijektion (Dok. 230/231/232) |

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*
