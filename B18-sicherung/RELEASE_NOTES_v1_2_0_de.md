# Release Notes — v1.2.0 (Juli 2026)

**DOI:** wird beim Zenodo-Upload vergeben (löst v1.1.9 ab · [10.5281/zenodo.21193007](https://doi.org/10.5281/zenodo.21193007))

Laufende Korrekturen: **[2/PDFs/190_T0_Korrekturen_De.pdf](2/PDFs/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[000_FFGFT_Changelog_De.md](000_FFGFT_Changelog_De.md)**

---

**FFGFT — Fraktale Feldgeometrische Fundamentaltheorie** zeigt:
Alle Konstanten des Standardmodells folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Was ist neu in v1.2.0

v1.2.0 **schließt einen Faden ab**, den v1.1.9 geöffnet hatte. Der
FFGFT-interne Kern von [Dok. 295](2/PDFs/295_Zeit_Logspirale_De.pdf) —
die Zeit-Windung als **logarithmische Spirale mit Verhältnis e** — stand
bereits in v1.1.9. Dok. 295 stellte dort selbst die scharfe Testfrage,
ob die naheliegende Gleichsetzung mit HLVs \enquote{Spiral-Zeit} auf dem
**e-Kriterium** trägt. v1.2.0 führt diese Prüfung durch und beantwortet
sie — mit einem **klaren Negativ** — und ergänzt die zugehörige
Abgrenzung in [Dok. 294](2/PDFs/294_HLV_Pruefrichtung_De.pdf).

Der Befund ist ein **FFGFT-interner Abschluss**, kein neuer externer
Anspruch: die Zeit-Windung als log-Spirale mit e steht für sich; die
Gegenüberstellung zeigt nur, dass die Gleichsetzung mit dem externen
Rahmen nicht trägt. HLV bleibt für FFGFT nachrangig (vgl. das negative
BD17A-Verdikt in v1.1.7) — interessant wäre nur eine tragende Brücke
gewesen; hier ist das Ergebnis ein sauberes Negativ plus eine
Kategorien-Klärung.

### Zwei disjunkte „Spiral-Zeiten" — die Kategorien-Klärung

\enquote{Spiral-Zeit} bezeichnet in HLV nicht ein Objekt, sondern **zwei**,
die nur den Namen teilen:

- die **geometrische** Zeit aus der Faktorisierung T⁷ = T⁴ × T³
  (Dok. 285): ein A₅-Singlet auf dem S¹-Faktor, entkoppelt und separabel;
- die **temporal-dynamische** Spiral-Zeit — das Objekt, das HLV so *nennt*:
  ein Nicht-Markov-Operator Ψ(t) = (t, φ(t), χ(t)) mit Gedächtniskanal,
  **ohne** A₅, Singlet oder S¹-Faktor.

FFGFT faktorisiert im Gegensatz zu beiden nicht; seine Spirale ist die
Projektion eines untrennbaren Ganzen (T̃·m = 1). Die e-Testfrage zielt auf
ein **geometrisch selbstähnliches** Objekt — das benannte HLV-Objekt ist
von dieser Kategorie nicht.

### Das e-Kriterium: FFGFT trägt e, kein HLV-Strang tut es

Das e-Kriterium ist notwendig und hinreichend über den Ganghöhen-Zerfall:
eine Windung ist genau dann äquiangular (log-Spirale, Verhältnis e je 2π),
wenn der Defekt je Schritt wie **1/n** zerfällt und der kumulierte Defekt
logarithmisch wächst; konstanter Defekt ergibt eine **Archimedische**
Windung mit Verhältnis → 1.

- **FFGFT** trägt e: mit d_n = 100 ξ_n gilt d_n·(n+75) → 1 (der 1/n-Zerfall),
  der Spiral-Fit liefert e^{2πa} = 2,71947 ≈ e.
- **Marcels temporal-dynamische Spiral-Zeit** trägt es nicht: lineare
  phasonische Phase und beschränktes Fenster-Gedächtnis ergeben einen
  **konstanten** Defekt, D(k) wächst linear statt logarithmisch
  (D(10⁵) = 1333 gegen ln(1+k/75) = 7,2), gemessenes Verhältnis 1,0011 —
  auf eigenen Definitionen keine log-Spirale, sondern eine Windung
  konstanter Ganghöhe.
- Die **φ-Geometrie**, die HLV tatsächlich trägt, weist auf φ, nicht e:
  eine äquiangulare Spirale aus dem τ = φ-Cut-and-Project hätte den Faktor
  φ = 1,618 je Umlauf bzw. φ⁴ = 6,854 je 2π.

**Kein HLV-Strang trägt also e.** Als Brücken-Bedingung (P35) präzise: HLVs
Spiral-Zeit trüge e nur, wenn ihr Phasengesetz einen 1/n-Skalenlauf
enthielte; die vorliegenden Definitionen enthalten ihn nicht. Das ist ein
Kandidat, keine Ableitung — und **kein Verdikt über Marcels Rahmen**: das
temporal-dynamische Objekt ist (nach seinem Spiral-Time-Papier) ein sauber
definiertes Objekt offener Quantendynamik (unitäre Dilatation auf H_S ⊗ H_M,
geprüft über Prozesstensor, CP-Divisibilität, Hard-Reset, Finite-Bath),
also der **dynamischen**, nicht der geometrischen Kategorie zugehörig.

**FFGFTs Zeit ist nicht an ein Bild gebunden.** Die Nichtschließung liegt
gleichwertig in zwei Darstellungen vor: geometrisch als log-Spirale (Dok. 295)
und im Hilbertraum als **Gedächtniskern** — die Fourier-Transformierte der
diskreten Spektraldichte des T⁴-Connection-Laplace (Dok. 283), verlustfreie
Bijektion H = L²(T⁴)⊗ℂ³ (Dok. 230/282). Das ist Darstellungs-Robustheit, keine
zusätzliche Evidenz (*Übersetzung ist nicht Begründung*) — erlaubt aber, den
Abgleich in **Kern-Sprache** zu führen: FFGFTs Kern oszillierend/diskret-spektral
(Revivals, BLP-Rückfluss 5,125), Marcels abklingend — dieselbe Klasse, andere
Gestalt (Dok. 283); genau der 1/n-Skalenlauf, der e trägt, fehlt dem
abklingenden Kern.

### Basis und Dimensionen: gleiche Zahlen, verschiedene Bedeutung

Die Dimensionszahlen decken sich in der **Zahl**, nicht in der Bedeutung.
FFGFTs *Drei* ist das interne ℂ³ / die Z₃-Ordnung auf T⁴/Z₃ (Modenindex);
Marcels *Drei* ist die triadische Zeit (t, φ, χ). Geteilt ist allein die
**Z₃** (C₃ < A₅), kein gemeinsamer Koordinatenraum. FFGFTs *Sechs* ist nicht
nativ (erst über die Einbettung T⁷ = T⁴ × T³; FFGFT selbst ist 4D);
Marcels *Sechs* ist das Z⁶-Elterngitter des Cut-and-Project (3 + 3). Der
einzige konkret belegte Überlapp bleibt das φ-ikosaedrische geteilte Objekt
— einseitig verifiziert (FFGFT → HLV, Dok. 294) und filtrations-empfindlich.

### Status des Abgleichs

Auf dem e-Kriterium ist der Abgleich **negativ**: das temporal-dynamische
Objekt trägt kein Verhältnis e, sondern golden-ratio-/phasonische
Quasiperiodizität; die Basis-Frage reduziert sich auf die geteilte Z₃. Die
Kategorien-Trennung und der dimensionsweise Abgleich sind gesicherte
Feststellungen; die Gleichsetzung bleibt ein **Brücken-Kandidat**, auf dem
e-Kriterium derzeit **blockiert**. Die scharfe Restfrage verschiebt sich auf
das *geometrische* HLV-Objekt — ob die faktorisierte Schicht (A₅-Singlet auf
S¹) ein skaleninvariantes Objekt kennt, das gegen e prüfbar wäre; in den
vorliegenden Quellen ist ein solches nicht ausgewiesen.

---

## Kernableitungen (Stand v1.2.0)

| Ergebnis | Dokument |
|----------|----------|
| Ableitungskette ξ → G → ℓ_P → L₀ | [Dok. 180](2/pdf/180_T0_L0_Herleitung_De.pdf) |
| Leptonmassen aus rationalen Invarianten | [Dok. 006](2/pdf/006_T0_Teilchenmassen_De.pdf) / [046](2/pdf/046_Teilchenmassen_De.pdf) |
| Koide-Skalar Q = 2/3 (berechnet) | [Dok. 258](2/pdf/258_Koide_2-3_De.pdf) / [259](2/pdf/259_Koide_Kreuzterme_De.pdf) |
| θ = 2/9 als Z₃-Zirkulant-Phase | [Dok. 291](2/PDFs/291_Dynamischer_Ort_Theta_2_9_De.pdf) |
| θ = 2/9 als parameterfreier C₃-in-A₅-Geometrie-Invariant (zweiter Zeuge) | [Dok. 293](2/PDFs/293_Ikosaeder_Theta_2_9_De.pdf) |
| Zeit-Windung als log-Spirale mit Verhältnis e | [Dok. 295](2/PDFs/295_Zeit_Logspirale_De.pdf) |
| α⁻¹ = 137,036, zwei unabhängige E₀-Wege | [Dok. 011](2/pdf/011_T0_Feinstruktur_De.pdf) / [292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| SI-Brücke | [Dok. 013](2/pdf/013_T0_SI_De.pdf) |
| Hilbertraum-Bijektion FFGFT ↔ QM | [Dok. 230](2/pdf/230_Hilbertraum_Uebersetzung_De.pdf) |
| Leptonen-Empirie-Check, m_τ-Vorhersage, Toleranz-Bilanz | [Dok. 292](2/PDFs/292_Leptonen_Empirie_Check_De.pdf) |
| Falsifikation: Casimir / Rotverschiebung / Lithium | [Dok. 220](2/pdf/220_Casimir_De.pdf) / [221](2/pdf/221_Rotverschiebung_De.pdf) / [222](2/pdf/222_Lithium_De.pdf) |

---

## Reproduzierbarkeit

`2/Dok293_Skripte/` — ikosaedrische Umverteilung (p₀ = 2/9 exakt, Robustheit
über zufällige Achsen und die n-zählige Reihe), numpy-only.
`2/Dok294_Skripte/` — Winkelspektrum-Diskriminierung des geteilten Objekts
(RMS-Distanz-Metrik), numpy-only.
`2/Dok295_Skripte/` — Zeit-Windung: 75-Schließung, log-Spirale (Verhältnis e),
duale Zeit↔Masse-Projektion (Faktor 100 achsensymmetrisch); **neu in v1.2.0:**
`spiralzeit_verhaeltnis_probe.py` (e-Kriterium: FFGFT trägt e, Marcels
Spiral-Zeit trägt 1, φ-Geometrie trägt φ⁴) und `basis_6d_achsen_probe.py`
(die sechs projizierten Achsen äquiangular nur bei τ = φ), numpy-only.
`2/Dok292_Skripte/` — Leptonen-Empirie-Check (Teile A–L).
`2/Dok291_Skripte/` — θ = 2/9-Mechanismus-Skripte.

---

## Plattformen

| Ressource | Link |
|-----------|------|
| 🔬 Interaktives Portal | [huggingface.co/spaces/jpascher/T0-FFGFT-Portal](https://huggingface.co/spaces/jpascher/T0-FFGFT-Portal) |
| 📁 GitHub Pages | [jpascher.github.io/T0-Time-Mass-Duality](https://jpascher.github.io/T0-Time-Mass-Duality/) |
| 📺 YouTube | [@Time-MassDuality](https://www.youtube.com/@Time-MassDuality) |

---

© 2025–2026 Johann Pascher · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
