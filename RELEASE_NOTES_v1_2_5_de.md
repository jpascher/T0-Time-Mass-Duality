# Release Notes — v1.2.5 (Juli 2026)

**DOI:** [10.5281/zenodo.XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX) (löst v1.2.4 · [10.5281/zenodo.21496379](https://doi.org/10.5281/zenodo.21496379) ab)
<!-- XXXXXXXX vor Veröffentlichung durch den neuen Versions-DOI ersetzen -->

Laufende Korrekturen: `2/pdf/190_T0_Korrekturen_De.pdf`  
Änderungsprotokoll: `000_FFGFT_Changelog_De.md`  
A-Serien-Protokoll: `A_Serie_Export/A_SERIE_CHANGELOG.md`

---

**FFGFT — Fraktale Feldgeometrische Fundamentaltheorie** zeigt:
Alle Konstanten des Standardmodells folgen aus einem einzigen
dimensionslosen Parameter **ξ = 4/30000** auf einem kompakten
4D-Torus T⁴. Die Grundrelation ist **T̃ · m = 1** — intrinsische Zeit
und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Was ist neu in v1.2.5

v1.2.5 ist ein Korrektur- und Präzisierungsrelease. Es enthält keine
neuen theoretischen Ergebnisse. Sein Inhalt ist die Einarbeitung zweier
externer Korrekturen (S. Vossen, 2026-07-23) in die A-Serie und der
Rückzug eines Altbestand-Parameters nach Konsistenzprüfung gegen die
kanonische A-Serie (R61). Beides ist der Supersessions-Mechanismus der
A-Serie im Vollzug: Korrekturen werden benannt, gebucht und bleiben
nachvollziehbar — sie verschwinden nicht.

### A-Serie v1.1 — externe Korrekturen eingearbeitet (CL-01 bis CL-03)

Beide Punkte wurden von S. Vossen als Rückmeldung zur A-Serie benannt
und als Korrekturen — nicht als Vorschläge — angenommen.

**CL-01 — Verifizierbarkeitsanspruch präzisiert.** Die Kurzform
„Alles ist überprüfbar" behauptete mehr, als die Prüfskripte leisten:
Skripte verifizieren Berechenbarkeit — nicht die Setzungen, nicht die
physikalische Lesart einer Brücke, nicht die empirische Adäquatheit.
Der Anspruch der Serie lautet jetzt:

> Jede berechenbare Aussage ist unabhängig ausführbar und nachprüfbar,
> und jede substanzielle Aussage trägt einen explizit deklarierten
> epistemischen Status. *(Formulierung nach Stefaan Vossen, 2026)*

**CL-02 — [K] und [B] sind keine externen Zertifizierungen.** A010 §6
ergänzt (De + En), gebucht als [SETZUNG]: Die Marker [K] und [B] sind
interne Zustandsangaben des Anspruchs. [K] besagt, dass eine Aussage
innerhalb des deklarierten Kerns folgt; [B], dass eine Brücke unter
ihren genannten Bedingungen algebraisch etabliert ist. Keiner der
beiden Marker begründet für sich empirische Wahrheit, externe
physikalische Gültigkeit oder eine eindeutige Ontologie.

**CL-03 — DOI-Angleichung.** A_SERIE_README.md (Header und
Zitierempfehlung) trug den v1.1.0-Altbestand-DOI (20117635) statt des
kanonischen Records (21496379); die Zenodo-Beschreibung führte den DOI
noch als ausstehend. Beides korrigiert. Für eine Serie, deren Gegenstand
dokumentarische Nachfolge ist, war das kein kleiner Makel.

### R61 — Zweitparameter ξ_Higgs zurückgezogen (Dok. 174/175)

Dok. 174/175 führten einen zweiten Parameter ein,
ξ_Higgs = λ_h²v²/(16π³m_h²) ≈ 1,038 × 10⁻⁵, und stützten darauf eine
Dekohärenzraten-Skalierung samt T₂-Verhältnis-Befund. Die
Konsistenzprüfung gegen die kanonische A-Serie ergab: **Dieselbe Formel
ist das Higgs-Matching von ξ selbst.** Mit Standardeingaben
(v = 246,22 GeV, m_h = 125,25 GeV) liefert sie 1,304 × 10⁻⁴ ≈ ξ = 4/30000
(Abweichung 2,2 %; vgl. R59 zur Schemaabhängigkeit) — so kanonisch
gebucht in A142 [K]. Der Wert 1,038 × 10⁻⁵ folgt aus keiner im Korpus
deklarierten Eingabekonvention und erscheint in der A-Serie nicht.

Konsequenz: Der T₂-Befund aus Dok. 174 verliert seine numerische Basis
(mit dem einen ξ trifft das gemessene Fenster von 9–11 Dekaden keine
ganzzahlige Stufenzahl) und war zudem nach Kenntnis der Daten gebildet,
nach P35 ohnehin ungebucht — er ist damit doppelt hinfällig. Unberührt
bleibt das Stufenkopplungsgesetz C ∝ ξ^|ΔN| mit dem einen
Fundamentalparameter (R57). Maßgebliche Form für künftige Verwendung:
Γ ∝ ξ^(2ΔN)·ω — deklariert und versiegelt in der
SDCR-Stage-2-Vorregistrierungsnotiz v1.1 (SHA-256 c47d73ce…3992,
23. Juli 2026), vor Vorliegen jeglicher Stage-2-Daten. Als **R61** in
Dok. 190 eingetragen; die Quelldokumente werden nicht revidiert
(append-only). Prüfskript: `python/Dok190_Skripte/r61_xi_higgs_matching.py`.

---

## Änderungen im Dateibestand

| Datei | Änderung |
|-------|----------|
| A_Serie_Export/Sources/ch/A010_Zweck_Aufbau_De_ch.tex | CL-02: [SETZUNG]-Absatz zu [K]/[B] |
| A_Serie_Export/Sources/ch/A010_Zweck_Aufbau_En_ch.tex | CL-02: [STIPULATION]-Absatz zu [K]/[B] |
| A_Serie_Export/pdf/A010_Zweck_Aufbau_{De,En}.pdf | neu gebaut |
| A_Serie_Export/A_SERIE_README.md | CL-01, CL-03; Version 1.1 |
| A_Serie_Export/A_SERIE_CHANGELOG.md | v1.1-Abschnitt (append-only) |
| 2/pdf/190_T0_Korrekturen_{De,En}.pdf | R61 |
| python/Dok190_Skripte/r61_xi_higgs_matching.py | neu (Prüfskript R61) |

Alle übrigen Dokumente, Skripte und Ergebnisse sind gegenüber v1.2.4
unverändert.

---

## Korrekturregister-Einträge (dieses Release)

| Eintrag | Betrifft | Beschreibung |
|---------|---------|--------------|
| R61 | Dok. 174/175 (vgl. A142, 147, 162; R57, P35) | Zweitparameter ξ_Higgs zurückgezogen — dieselbe Formel ist das Higgs-Matching von ξ selbst (A142 [K]); T₂-Befund doppelt hinfällig (Basis + P35); maßgeblich: Γ ∝ ξ^(2ΔN)·ω |

---

## Versionshistorie

| Version | DOI | Schwerpunkt |
|---------|-----|-------------|
| v1.2.5 | [XXXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXXX) | **Korrekturrelease:** A-Serie v1.1 (CL-01–03, Vossen-Korrekturen); R61 (ξ_Higgs zurückgezogen) |
| v1.2.4 | [21496379](https://doi.org/10.5281/zenodo.21496379) | **A-Serie:** 43 kanonische Dokumente; A095 (g_R=0 [B]); A192 (U(1), SU(3) [B]); A060 R50; CHSH ξ/(2π) [B] |
| v1.2.3 | [21396624](https://doi.org/10.5281/zenodo.21396624) | Informationsfrage (Dok. 301/302); natives T·E=1 (Dok. 306, R50–R53); Zeit im Zustandsraum (Dok. 307) |
| v1.2.2 | [21266963](https://doi.org/10.5281/zenodo.21266963) | SM als dekompaktifizierte Projektion (Dok. 298); K_frak = 74/75 (Dok. 300) |
| v1.2.1 | [21203746](https://doi.org/10.5281/zenodo.21203746) | Zeit-Windung als Hilbertraum-Gedächtniskern (Dok. 283/295/296/297) |
| v1.1.9 | [21193007](https://doi.org/10.5281/zenodo.21193007) | θ=2/9 als C₃-in-A₅-Geometrie-Invariant (Dok. 293/294/295) |
| v1.1.7 | [21158441](https://doi.org/10.5281/zenodo.21158441) | Leptonsektor-Audit; α Zwei-Wege-Überbestimmung (Dok. 291/292) |
| v1.1.0 | [20117635](https://doi.org/10.5281/zenodo.20117635) | Hilbertraum-Bijektion (Dok. 230/231/232) |

---

## Hinweis zum eingefrorenen Korpus

Diese Version ist als eingefrorener Quellkorpus für eine externe
Methodenstudie (KI-gestützte wissenschaftliche Synthese, S. Vossen)
vorgesehen. Maßgeblich sind der Versions-DOI dieses Releases und der
SHA-256-Hash des Release-Archivs; beide werden nach Veröffentlichung
im Begleitschreiben festgehalten. Der eingefrorene Korpus umfasst
ausdrücklich das Korrekturregister und die Changelogs.

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*  
*Diese Release Notes wurden unter Verwendung KI-gestützter Werkzeuge erstellt.*
