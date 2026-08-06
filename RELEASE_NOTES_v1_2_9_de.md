# Release Notes — v1.2.9 (August 2026)

**DOI:** *wird bei Zenodo-Veröffentlichung vergeben*

Dieses Release ersetzt inhaltlich **v1.2.8**
([21821995](https://doi.org/10.5281/zenodo.21821995)).

Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/190_T0_Korrekturen_De.pdf)**
Changelog: **[000_FFGFT_Changelog_De.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/000_FFGFT_Changelog_De.md)**
A-Serie-Log: **[A_Serie_Export/A_SERIE_CHANGELOG.md](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/A_Serie_Export/A_SERIE_CHANGELOG.md)**

---

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt:
alle Standardmodell-Konstanten folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Seit v1.2.8 ist **ein neues Korpus-Dokument** hinzugekommen:
**Dok. 315 „Die Form von K_frak: additiv oder multiplikativ?"**
(DE+EN, je 10 Seiten, vier Prüfskripte). Es prüft erstmals, ob der
Korpus die *Form* des fraktalen Korrekturfaktors diskriminiert —
additiv 1 − 100ξ = 74/75 gegen multiplikativ (1 − ξ)¹⁰⁰ — statt nur
seinen Wert.

Keine Änderung an ξ, an der Grundrelation oder an einer
Herleitungskette. Quelldokumente unverändert (append-only).

---

## Dok. 315 — Die Form von K_frak (neu)

**Die Frage.** Die beiden Formen unterscheiden sich um exakt den
zweiten Binomialterm, 4950ξ² ≈ 8,9×10⁻⁵. Eine Korpus-Stelle kann die
Form nur entscheiden, wenn ihre eigene Unsicherheit kleiner ist als
dieser Abstand (bei Potenz-Stellen entsprechend verstärkt).

**Kontrollfall.** Eulersche Musikspirale (5/7-Limit): exakter Schluss
per Primfaktorzerlegung unmöglich; beste Beinahe-Schlüsse sind das
Schisma (1,95 Cent) und im 7-Limit das Ragisma 4375/4374 (0,40 Cent).
Schließung entsteht nur durch Temperierung — Rationalisierung der
Schrittweite — genau die Rationalität, die der ξ-Zyklus (1/75,
ggT(74,75) = 1) per Setzung trägt.

**Drei Zeugen.**
- **A130-Zwei-Routen-Verhältnis:** m_μ kürzt sich vollständig; mit der
  nicht deklarierten Identität p = −(2−√3) diskriminiert die Stelle
  7,5:1 additiv. Neue offene Punkte P-315-1 (Herleitung der
  Identität) und P-315-2 (realer Rest von ≈ 7 eV in m_e, 45 000× über
  dem Messboden — derselbe Posten wie der in R72 gebuchte
  n = 101,3-Überschuss).
- **A270-Hochpotenz-Stelle:** K⁻³⁶ ≈ 16/π²; der ×36-Verstärker macht
  den Formabstand zu 0,32 %. Additiv trifft auf 1,0×10⁻⁴,
  multiplikativ verfehlt um 3,1×10⁻³ — **31:1 additiv**. Die Referenz
  ist per Dok. 314 aufgewertet: **16/π² = 1/Δ(D4)**, der Kehrwert der
  D4-Packungsdichte; **P35 verengt sich** von „woher die Konstante?"
  auf „warum koppelt der Bulk-Exponent 36 an Δ(D4)?".
- **A040-Potenzform:** tendiert additiv, kann aber nicht auflösen
  (D_eff nur vierstellig).

**Strukturargument.** Die additive Form ist die exakte
Windungsbuchhaltung der eingerollten Domäne (75(1−ε) = 74 als
Identität); die multiplikative die Stufenkomposition der ausgerollten
Skalendomäne. Angebunden an die Schließungsgabelung (Dok. 295/313,
per Dok. 314 Kap. D2): Fall B (ξ eingefroren) *ist* die additive
Buchhaltung, Fall C (ξ läuft, äquianguläre Spirale) *ist* die
multiplikativ-logarithmische; alle Korpus-Verwendungen buchen Fall B.

**Status.** Wert [K]; Form additiv [B], zweifach bedingt-bestätigt;
die multiplikative Alternative wird von beiden bedingten Zeugen
konsistent disfavorisiert, von keinem gestützt und bleibt nur
logisch möglich, solange beide Bedingungen offen sind. Unbedingte
Entscheidungslinie: die A270-Baryon-Stelle (K³⁸-Niveau, Formabstand
0,34 %) — zugleich Test der Gabelzuordnung und des Primats der
eingerollten Geometrie.

Verifikation: `2/python/315_Skripte/` — `euler_spirale_7limit.py`,
`pruefrechnung_kfrak_form.py`, `pruefrechnung_p_identitaet.py`,
`pruefrechnung_rest_0p1xi.py` (reine Standardbibliothek, exakte
Bruchrechnung, Sollwerte als Assertions).

Dokumente: [DE](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/315_Kfrak_Form_De.pdf) · [EN](https://github.com/jpascher/T0-Time-Mass-Duality/blob/main/2/pdf/315_Kfrak_Form_En.pdf)

---

## Neue und verengte offene Punkte

- **P-315-1:** Herleitung oder Deklaration von p = −(2−√3) in
  A130/Weg 2 (nach R72 der einzige Weg, Zeuge A auflösungsfähig zu
  machen).
- **P-315-2:** der reale ≈ 7-eV-Rest in m_e (kein einfacher
  Korrekturterm unter zehn F(ξ)-Familien; Größenordnung
  QED-Selbstenergie).
- **P-315-3:** n-Schärfe — Formdiskriminierung verlangt Δn ≤ 0,66;
  die Sektorleiter (n = 100,27) ist der aussichtsreichste Kandidat.
- **P35 (verengt):** Vorwärtsherleitung von K_frak⁻³⁶ = 1/Δ(D4),
  insbesondere die Rolle des Bulk-Exponenten 36.
