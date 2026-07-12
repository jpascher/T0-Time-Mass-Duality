# FFGFT Changelog
## Korrekturen und Präzisierungen der Dokumentenserie
**Grundlage:** Dok. 190 (allgemein) und Dok. 210 (Wicklungszahlen)
**Stand:** Juni 2026 (zuletzt erweitert: 1. Juli 2026 — neues Dok. 291 „Der dynamische Ort von θ=2/9: Betrag, Windung, Phase“ (DE+EN, je 6 S., 8 Abschnitte) + Ordner Dok291_Skripte (5 numpy-only-Skripte, seed 20780458): der θ=2/9-Faden aus 282→286 als eigenes Dokument zusammengeführt und geschärft. Kernbefund: θ=2/9 lebt allein im dynamischen PHASENKANAL — der symmetrische Koide-Invariant Q=2/3 ist θ-blind (analytisch S=3, T=6; 2/9 unter dem Q-Bereich [1/3,1]), der Allpass zeigt Betrag |B|=1 UND ganzzahlige Windung=3 beide counter-blind, nur das stetige Phasenprofil trägt θ (numerische Fassung von „2/(9π) irrational → kein flacher topologischer Invariant“). Statisch kontingent, NICHT erzwungen wie c: θ*(δ) wandert monoton mit dem freien Modulus (dθ*/dδ≈0,31≠0), während c ein parameterfreier Signatur-Rand ist (dc/dλ≡0, eichgeschützt m=0⇒v=c). SELBST- vs. SCHIEF-ADJUNGIERT (Kern): im Brechungsterm δcos(2φ+χ) ist χ=0/π gerade/selbstadjungiert/reell, χ=π/2 ungerade/schief-adjungiert/imaginär (cos(2φ+π/2)=−sin(2φ), e^{iπ/2}=i); die selbstadjungierten Holonomien (Z₃-Wilson × Spinstruktur) sind Vielfache von π/3, π/2 nicht dabei; die Eliminationskette (Dok 282) scheidet alle statischen selbstadjungierten Kandidaten aus → der Selektor ist die schief-adjungierte Phase → typ-konsistent ist χ=π/2, der i-Wert, KEINE angenommene Z₄, kein Zahlenspiel. Präzisierung (per HLV-Seite/Marcel): „schief-adjungiert“ meint den GENERATOR (C_e=exp(K), K†=−K, endliche Holonomie unitär), nicht die endliche Matrix. BETRAG δ als golden gedämpfte 2. Harmonische: δ=|c₂|, χ=arg(c₂) sind Betrag/Phase derselben komplexen zweiten Fourier-Harmonischen c₂=δe^{iχ} (c₂=iδ bei χ=π/2, reiner Sinus); δ*≈0,2389 ist eine DÄMPFUNG (φ⁻³=1/φ³=0,2361<1, negative Golden-Potenz), Exponent 3=D (volles kompaktes T⁴; einzelne dekompaktifizierte 3′-Rekursion gäbe 1/φ¹, 159% daneben → Argument fürs kompakte T⁴); die ξ-Dämpfungs-Rekursion (Dok 275) passiert 1/φ³ bei 3×3609≈10827, δ* wird ~89 Schritte davor erreicht (Überschuss +1,187%, Näherung von oben). EHRLICH (P35): der Überschuss ist NICHT K_frak — Dok 133s präzise Form (D_eff/3)^(D_eff/2) gibt Faktor ~100 (1,333%), δ braucht nur ~89ξ (1,187%); und Dok 275 fixiert die Rekursionstiefe ausdrücklich nicht unabhängig; die scheinbare Nähe 89≈F(11) ist ein post-hoc-Fit, korpus-mäßig NICHT gedeckt → 89-Schritt-Offset OFFEN, NICHT gebucht. Bilanz: Phase χ=π/2 (schief-adjungierter i-Wert, fest); Betrag δ≈1/φ³ (golden gedämpft über D=3, Form/Ordnung/Exponent/Richtung fest, exakter Feinwert offen). 5 Skripte: forced_vs_contingent, allpass_theta, allpass_carrier_selection, holonomie_landschaft (selbst/schief-adjungiert), delta_golden_daempfung. Dieses Dokument wird bis zum Lock des BD17A-Holonomie-Pilots INTERN gehalten (nicht an die Brücke/IPI geben — Target-Leakage: es enthält die volle FFGFT-seitige Begründung, warum schief-adjungiert/χ=π/2/2/9-Auswahl; normales Korpus-Dokument für die nächste Release, nur das Timing zählt). NACHGESCHÄRFT (2. Juli): die δ-Sektion verweist jetzt explizit auf Dok 275s No-Go — 1/φ³ ist ein Durchgangspunkt, kein Fixpunkt (einziger Fixpunkt der Dämpfung ist 0), und k*(c) existiert für jedes Ziel mit identischem Parameterstatus; dass δ* nahe 1/φ³ liegt, ist daher kein Schließen der Rekursion, ein Fixieren der Tiefe wäre keine Auszeichnung. Damit ist der offene 89-Schritt-Offset formal durch 275 gedeckt (Modell-Offenheit, kein Zahlen-/Irrationalitäts-Artefakt). NEUER ABSCHNITT (2. Juli) „Was die Nicht-Schließung praktisch bedeutet: ein offener Kopplungskanal“ (vor der Bilanz, DE+EN): der geschlossene Massen-Sektor (Fixpunkt R(Φ*)=Φ*, Dok 203) hat keinen Spielraum; der offene Phasen-Sektor schon — die nie schließende ξ-Dämpfungs-Rekursion (Dok 275) ist eine offene, gedämpfte Rückkopplungsschleife (Verstärkung <1), die — anders als ein Fixpunkt — von außen einrastbar ist (Injektions-/Mode-Locking, Dok 286). Praktisch: ein Kopplungskanal genau im Phasen-Sektor, aber eng (Fangbereich ~ξ, 2/9-Zunge ~12× schmaler als 1/3), gerichtet (Dynamik→Phase, nicht in den starren Massen-Sektor) und nur über einen dynamischen schief-adjungierten Generator außerhalb der FFGFT-Geometrie nutzbar (Dok 283/286, Kandidat, kein Resultat). Anti-Numerologie-Grenze: strukturierter Spielraum, kein freier Parameter — radial starr, Phase eng (χ=π/2, transzendent in 2π, ξ-Fangbereich), Tiefe nicht fixiert. 291 jetzt DE+EN je 7 S. ERWEITERT (2. Juli, Schluss-Absatz des Kopplungskanal-Abschnitts): der offene Phasenkanal ist der Grund, warum der Fundamentalsektor nicht auf ein starres Skelett zusammenfällt — ein vollständig geschlossenes Modell wäre überdeterminiert (keine kontingente Auswahl im Z₃-Orbit, keine Flavour-Mischung, keine physikalische Phase). Mischung IST Phase (Dok 289); am schärfsten die CP-Verletzung (verlangt eine irreduzible komplexe Phase — rein reell/selbst-adjungiert ist CP-erhaltend — also genau der Typ des schief-adjungierten Kanals χ=π/2; der offene Kanal ist strukturell von der Art, die CP tragen kann, eine voll selbst-adjungierte FFGFT wäre CP-gerade). Scope eng gehalten: Mischung/CP/Kontingenz im Fundamentalsektor, NICHT die makroskopische Vielfalt. BEREINIGT (2. Juli, unabhängiger Verifikations-Durchgang, DE+EN): alle Kernzahlen von 291 unabhängig nachgerechnet (eigener Blaschke, eigener Bisektions-Löser: Q=2/3 auf 1e-15, δ*=0,238872, Überschuss +1,188%, Tiefen 3608,5/10826,2/10737,6, K_frak-Ausschluss bestätigt) — drei Bereinigungen: (1) das δ-Fenster in §5 war einheiten-gemischt (ψ-Basin-Breite 0,078 ÷ Median-Steigung 0,31 ≈ 0,25); jetzt konsistent im θ-Raum: Basin [1/6,1/3] Breite 1/6, lokale Steigung bei δ*≈0,24 etwa 0,80 → Δδ≈0,21 (Schluss „δ weich, nicht feinabgestimmt" unverändert, Median-/Lokal-Steigung jetzt getrennt ausgewiesen); zudem Plural der inneren Extrema (es sind zwei; verfolgt wird der untere, orbitnahe Zweig); (2) neue Zweig-Bemerkung in §6: der schief-adjungierte Typ lässt zunächst beide i-Werte zu (χ=π/2 und 3π/2, e^{±iπ/2}=±i), die Zweigwahl ist eine Orientierungswahl (Umlaufsinn) — numerisch sind die Zweige NICHT äquivalent: der Spiegel-Zweig 3π/2 hat bei δ≈0,24 kein inneres Extremum nahe 2/9 (Extrema 0,83/1,87), nur der +i-Zweig erreicht den Orbit-Bereich (stärkt die π/2-Auszeichnung, schließt eine unbenannte ±-Lücke); (3) Transparenz-Note in §8: „+1,187%" und „88,5 Log-Einheiten" sind über ln(δ*φ³)/ξ ein und dieselbe Zahl, keine zwei unabhängigen Befunde (kein Kreuz-Check). forced_vs_contingent.py um lokale Steigung, θ-Raum-Fenster und Spiegel-Zweig-Check erweitert — Text und Skript kommen jetzt aus derselben Quelle. DAZU (2. Juli) neue Schluss-Sektion „Einordnung: Nutzen und Anwendungsnähe" (DE+EN): Befunde als Struktur-/Ausschluss-Resultate eingeordnet, keine Technologie — drei Nutzergruppen (Koide-/Flavour-Arbeiten: No-Go spart topologische/abzählende Herleitungswege; Methodik: Betrag/Phase als übertragbare Audit-Sprache; Didaktik: Teilchenphysik↔Nachrichtentechnik-Übersetzung); Messungsnähe allein im Phasenkanal (Mischung/CP, Dok 289, Oszillationsphasen/δ_CP, DUNE/Hyper-K); ausdrücklich keine Anwendung im engeren Sinn, solange δ nicht hergeleitet ist (P35). 291 jetzt DE 8/EN 8 S., 0 Fehler. GESCHÄRFT (2. Juli, Status der Nicht-Schließung, DE+EN): die Bilanz behandelte den δ-Feinwert als „noch nicht hergeleitet" — zu schwach gegen Dok 275, das doppelt stärker ist: Nicht-Schließung ist THEOREM (einziger Fixpunkt 0, jedes c∈(0,1) Durchgangspunkt) UND die Resonanzdichte schließt jede rekursionsinterne Auszeichnung eines Wertes aus (275, epistemische Grenze; strukturgleich Dok 176/038). Jetzt präzise: δ ist aus der Rekursion allein BEWEISBAR NICHT herleitbar, die Rekursionsseite ist erledigt (gelöste Frage), offen ist allein die Existenz des ÄUSSEREN Ankers; die zwei „aus einem inneren Grund"-Stellen disambiguiert (innerer Grund DER LIEFERNDEN DYNAMIK, nicht der Rekursion — Letzteres schließt 275 aus). Die offene Frage von 291 verschiebt sich damit sauber von „ob sich δ herleiten lässt" auf „ob ein äußerer schief-adjungierter Anker existiert" (= BD17A-Faden). DE+EN je 8 S., 0 Fehler. STAGE-10-HARNESS EINGEFROREN (2. Juli, nach Marcels v1.6/v1.7 + Stage 9): Marcels Stage 9 / Run M liefert die dynamische schief-adjungierte C_e-Klasse (carrier-abgeleitet, blind zu 2/9, non-flat 24/24, Verdikt PREFLIGHT_NONFLAT_PASSED__NO_BD17A_SCORE; mehrere dynamische Nulls ebenfalls non-flat → Klassen-Zulässigkeit, keine Spezifität; Zenodo 21127634); v1.7 trennt Claim-States in A (repliziert: nur 6B) / B (zulässig-unspezifisch: Carrier, Stage-7-C_e, Stage-9-Preflight) / C (geblockt). Stage 10 = blinder θ*=2/9-Vergleich mit eingefrorener Stage-9-Klasse, kein Tuning. FFGFT-Seite dazu VORAB eingefroren: Dok291_Skripte/ffgft_stage10_verdict_harness.py (numpy-only, seed 20780458, Selbsttest 3/3) kodiert den symmetrischen Lock — Extraktor ½ Arg det W_γ mod 2π/3 in Radiant, Ziel 2/9, Primärkriterium nächstes-Orbit-Glied {0, 1/9, 2/9, 4/9}, Verdikt ADMITTED (2/9 Orbit-Modus UND schlägt alle Nulls) / RESIDUAL (Orbit-Modus, Null-Überlapp) / BLOCKED (keine Orbit-Selektion); SHA256 99e11399f23377702c5878784d791f8fc90a350e7999f8c2906bf99221aab246 als Lock-Nachweis im README; Änderungen nach Dateneingang = Lock-Bruch. Vorregistrierte neutrale Beobachtung an Marcel kommuniziert: Target-q50 (0,046) liegt UNTER allen generischen dynamischen Nulls (0,056–0,084) — vor dem Scoring gebucht, keine Richtungsaussage. Dok 291 bleibt intern bis zum Stage-10-Verdikt. KONSISTENZ-KLAUSEL 291↔292 (2. Juli, je 8 S., 0 Fehler): eine Fußnote an der „Massen exakt und starr"-Stelle trennt jetzt die geometrische Fixpunkt-Ebene (Q=2/3 exakt, von Daten −0,9σ bestätigt) von der Polmassen-Ebene (Paar (√2,2/9) nicht gemeinsam exakt, ~450σ im μ/e-Kanal → 2/9 per P42 rationale Adresse, kein Polmassen-Exaktheitsanspruch); ausdrücklich vermerkt, dass der dynamische Ort davon unberührt ist (Orbit-Auflösung ~0,1 ≫ 10⁻⁷-Unterschied). Keine inhaltliche Änderung an 291, nur Ebenen-Disambiguierung; Stage-10-Lock unberührt. ZUSÄTZLICH Herkunftssatz in 291-Einstieg (2. Juli): θ=2/9 ist selbst keine Eingabe, sondern gefunden — Hilbertraum-Übersetzung 230/231/232 + Fortführung zu den Massen (282) macht die drei Lepton-Massen als Z₃-Zirkulant-Spektrum auf der ℂ³-Faser sichtbar, in dessen Eigenwerten 2/9 als Diagonalisierungs-Ergebnis erscheint; genau dieser Zirkulant liefert die Amplituden a_k von 291. Verweis auf 292/P42 (rationale Adresse) und Hinweis, dass der dynamische Ort davon unberührt ist. Parallel zur Herkunfts-Sektion in 292, damit beide Docs die kausale Kette Hilbertraum→Zirkulant→2/9 nennen. NEU P41 in Dok 190 (2. Juli, DE+EN, je +1 Eintrag, DE 35/EN 31 S.): Rotverschiebungs-Drift (Sandage-Loeb) als Kandidat-Diskriminator statisch vs. Expansion GEPRÜFT UND NICHT GEBUCHT — ΛCDM-Signal über 25 J: +6 cm/s (z=0,5), Vorzeichenwechsel z₀=1,92, −14/−20 cm/s (z=4/5), ELT σ~2 cm/s; Amplituden-Test nicht entartungsfest (säkulare ξx-Evolution bei 0,1–0,4·H₀ imitiert ΛCDM, natürliche FFGFT-Rate c/R_H=H₀ exakt — geteilte Skala P36/P39; Dipol-Systematik der galaktischen Beschleunigung ~17 cm/s gleiche Ordnung); bedingt scharf nur der Form-Test (Vorzeichenwechsel/Zwei-Band-Kontrast ~+20 cm/s, von keinem z-konstanten Säkularkanal imitierbar), verlangt aber Vorab-Festlegung auf strikte Statik und Niedrig-z-Träger; Zeithorizont ~2 Jahrzehnte. Rechnung: Dok190_Skripte/drift_sandage_loeb_check.py (numpy-only, seed 20780458). Bestätigt Johanns Vorsichts-These quantitativ: auch dieser Unterscheidungsversuch stirbt in der Amplitude an der geteilten R_H/H₀-Skala. ZUDEM P14-Dublette in Dok 190 aufgelöst (2. Juli): die doppelt vergebene Überschrift „Präzisierung 14" umbenannt in P14a (Rotverschiebung Dok 041, inkl. Tabellenzeile P14→P14a bzw. EN R14→R14a) und P14b (CMB-Anharmonizität/Forward-Retrodiktion, deckt P29–P31, keine eigene Tabellenzeile); alle Querverweise korpusweit nachgezogen (268 DE+EN je 3, 269 DE+EN je 2, 279 DE+EN je 1, 190-intern je 3); acht Dokumente neu gebaut (190/268/269/279 DE+EN), 0 Fehler/0 Glyphen. NEU Dok292_Skripte/leptonen_empirie_check.py (2. Juli, Empirie→FFGFT-Richtung auf Johanns Vorgabe): vollständige Nachrechnung des Leptonsektors AUS den PDG-Daten (m_e=0,51099895069, m_μ=105,6583755, m_τ=1776,86±0,12 MeV). Ergebnisse: Q=0,666660511±0,0000068 (−0,91σ von 2/3); Brannen-Fit r_emp=1,4142005 (−1,3e-5 von √2), θ_emp=0,22222963±8,4e-6 (+0,89σ von 2/9, τ-limitiert); θ aus m_μ/m_e allein (τ-frei, r=√2 fix): 0,2222220471, |θ−2/9|=1,75e-7 — reproduziert exakt die Dok-282-Angabe (~1,8e-7, sieben Stellen); Zirkulant-vorwärts (√2, 2/9 exakt) trifft m_μ/m_e auf +0,0010%, m_τ/m_μ auf +0,0060%; ξ-Leiter-Verhältnisse +0,52/+1,04/+1,57%, Reverse-ξ je Verhältnis 1,347/1,375/1,358e-4 (+1,1 bis +3,2% vs 4/30000); Brückenkonstanten v_eff=248,9/247,6/245,1 GeV (P40-konform); ALLE vier Spannungsmaße (Q, θ_3Massen, m_τ-Invertierung, m_τ-Vorhersage) sind DIESELBE eine ~0,9σ-τ-Spannung: m_τ(Koide-exakt)=1776,969, m_τ(θ=2/9-exakt)=1776,967, Vorhersage aus (m_e,m_μ;√2,2/9)=1776,968 MeV vs PDG 1776,86±0,12 — Belle-II-Präzision (~0,05 MeV) entscheidet. K_frak-Gegenprobe der Leiterabweichungen ohne einfaches Muster (+0,52/+1,04% vs −1,33%), ehrlich offen gebucht. NEU DOK 292 (2. Juli, DE+EN je 5 S., 0 Fehler): „Leptonen-Empirie-Check" — die Skript-Nachrechnung (leptonen_empirie_check.py) als Korpus-Dokument nach Standardmuster: Richtung Empirie→FFGFT (Kompatibilitätsmodus, P35/P40); Ebene 1 Zirkulant (Q=0,666660511±68e-7, r_emp=1,4142005, θ_emp=0,22222963±8,4e-6; τ-freier Test θ(μ/e)=0,2222220471, |θ−2/9|=1,75e-7, reproduziert Dok 282; alle Restspannungen = EINE 0,9σ-τ-Spannung; vorab gebuchte Vorhersage m_τ=1776,968 MeV, drei Invertierungswege konsistent, Belle-II entscheidet); Ebene 2 ξ-Leiter (Verhältnisse +0,52/+1,04/+1,57%, Reverse-ξ 1,347/1,375/1,358e-4, Brückenkonstanten v_eff=248,9/247,6/245,1 GeV, K_frak-Gegenprobe negativ und offen deklariert; τ/μ-Abweichung ≈ 2× μ/e-Abweichung als ungebuchte Auffälligkeit notiert). Wrapper DE+EN angelegt. ERWEITERT UM PRÄZISIONSANALYSE (gleicher Tag, jetzt je 6 S.): neue Sektion „Relation zu den Messgenauigkeiten" + Skript-Teil I — 2-Parameter-Analyse (r,θ) gegen (R1=μ/e, R2=τ/μ): Messpräzisionen 2,2e-8 vs 6,8e-5 (μ/e 3100× präziser) → extrem anisotrope Kovarianz (dünne Hauptrichtung σ=3,4e-10, dicke σ=1,7e-5, Korrelation ≈−1); Punkt (√2, 2/9) liegt 0,90σ in der dicken (= die τ-Spannung), aber ~450σ in der dünnen Richtung: ALS EXAKTES PAAR VON HEUTIGEN DATEN AUSGESCHLOSSEN (verfehlt m_μ/m_e um 1,0e-5 bei Messgenauigkeit 2,2e-8), bestätigt auf 1e-5 (die „4–5 Stellen" aus Dok 282 als Messrelation präzisiert); der 1,75e-7-θ-Rest ist heute schon gemessener Offset, den auch perfektes Belle-II nicht auflöst (radiative Polmassen-Korrekturen als Kandidat, deren typische Größe α/π~1e-3 das Rätsel eher vergrößert — offen per P35); §2.4-Formulierung „auf acht Stellen" entsprechend korrigiert; ξ-Leiter in σ_exp: 2,4e5/154/232 → theorieseitig, nicht datenlimitiert; Testschärfe m_τ-Vorhersage 0,9/2,2/5,4σ bei σ=0,12/0,05/0,02 MeV. DAZU Unterabschnitt „Gedankenmodell: Umkehrung der Präzisionsaussage" (Johanns Einwand): drei Stärkegrade — schwach (σ um 450× unterschätzt: kaum haltbar, Kreuzcheck-Netz), mittel (m_μ/m_e ist QED-extrahiert, nicht abgelesen; Vollständigkeitsannahme der Extraktionstheorie; logisch offen), stark/FFGFT-nativ (Präzision gilt für die ANGEZOGENE Polmassen-Größe, Zirkulant lebt auf geometrischer Ebene darunter; 10⁻⁵-Offset = gemessene Dicke der Verkleidungsschicht im μ/e-Kanal; konsequente P40-Verlängerung: in Verhältnissen kürzt nur der generationsUNabhängige Korrekturteil); Bringschuld ausgewiesen (Offset müsste aus generationsabhängiger radiativer Struktur berechenbar sein, sonst unfalsifizierbar); als Gedankenmodell gebucht, nicht als Auflösung — Widerspruch bleibt für Polmassen-Ebene bestehen. Jetzt je 7 S. AUFGELÖST DURCH P42 (2. Juli, Johanns Rahmenentscheidung): Grundsätzlich bleibt die rein theoretische Ableitung aus ξ; der Leptonsektor erhält EINEN deklarierten Referenzpunkt — das Verhältnis m_μ/m_e (analog P39 für H₀/R_H). Bei strukturellem r=√2 (aus Q=2/3) fixiert es θ_ref=0,2222220471; 2/9 ist dessen RATIONALE ADRESSE auf sieben Stellen, kein Exaktheitsanspruch auf Polmassen-Ebene → 450σ-Befund ist Kalibrierung, keine Falsifikation. Anspruchsschicht auf Johanns Korrektur präzisiert: ξ-Status unberührt (als zwingend aus der Geometrie behauptet — Streitpunkt hier nicht verhandelt); Leptonmassen an sich KEINE Eingabe der Theorie — der Referenzpunkt gehört zur VERGLEICHSEBENE (verortet die geometrische Relation in den Polmassen-Daten, ohne Vergleichsabsicht nicht nötig; analog P39/P40); ehrlicher Preis liegt in der TESTBILANZ, nicht der Parameterzählung: m_μ/m_e als Anker verbraucht, scheidet als Prüfgröße aus, Prüfgröße allein m_τ. Gewinn: eingabefehlerfrei scharfe Vorhersage m_τ=1776,9690±0,0001 MeV (+0,91σ zu PDG; Belle-II-Weltmittel entscheidet ohne Ausweichmöglichkeit). Brückenziel verschärft: Dynamik muss θ_ref selektieren, 2/9 bleibt Adresse und Stage-10-Ziel (Orbit-Auflösung ~0,1 unberührt). P42 als Tabellenzeile in Dok 190 DE+EN (36/32 S.), Header-Nachtrag 2. Juli deckt P41+P42+14a/b; Dok 292 um Unterabschnitt „Aufgelöst durch Deklaration" erweitert (je 7 S.). DOK 292 ERWEITERT um Sektion „Die Feinstrukturkonstante aus den Leptonmassen" + Skript-Teil J (2. Juli, Johanns Hinweis auf α-Herleitung und G-Buchhaltung als Kernstücke): Dok-011-Relation α⁻¹=(7500/E₀²)·K_frak von der Datenseite verifiziert — E₀_req=7,39798 vs √(m_e·m_μ)=7,34788 MeV, Verhältnis 1,006819 vs K_frak^(−1/2)=1,006734 (Match 8e-5): derselbe deklarierte Faktor K_frak=1−100ξ (X-Flip, T_CMB) schließt 98,8% der α-Lücke — Sektor-übergreifende interne Konsistenz, kein Fit; geschlossene parameterfreie Relation α=ξ·m_e·m_μ/(K_frak·MeV²) → 1/α=137,059 vs 137,036 (1,7e-4 = ~10⁶ σ_exp, theorieseitiges Residuum wie Leiter, nächste Ordnung offen); E₀=7,398-Brücke (5e-6) ausdrücklich als Kalibrierung nicht als Erfolg gezählt. KORRIGIERT (Johanns Hinweis „lies die Dokumente genauer, α ist keine Kalibrierung"): α läuft NICHT über eine gefittete Brückenkonstante, sondern über ZWEI UNABHÄNGIGE E₀-Wege (Dok 011) — Weg 1 empirisch E₀=√(m_e·m_μ)=7,348, Weg 2 eigenständig-geometrisch E₀²=4√2·m_μ/ξ^p=7,398 (aus ξ und m_μ allein, keine Rückrechnung aus α). Zwei Konsistenzen: (i) Weg 2 trifft 7,398 → α auf +5e-6; (ii) Differenz der Wege 7,398/7,348=1,00682 = K_frak^(−1/2) auf 9e-5. α damit ÜBERBESTIMMT (zwei Herleitungen treffen sich auf 8e-5), Rekursionstiefe strukturell fixiert (E₀ quadratisch in α → K_frak^(1/2) auf E₀-Ebene = volle K_frak-Ordnung auf α-Ebene). α aus der Unvollständigkeits-Rest-Liste HERAUSGENOMMEN: es ist die eine Stelle OHNE offenen Rest im Leiter-Sinn, weil zwei Wege die Tiefe fixieren; offener Rest nur bei Leiter-Stellen (nur ein Weg). ZUSATZ-ABSCHNITT „Der α-Restwert als zweiter Zeuge der Verkleidungsschicht" (Johanns Präzisierung, nur auf α bezogen): nimmt man α (1,5e-10) UND Weg 2 (rein geometrisch, kein Messfehler) als exakt, ist in α=ξE₀² die einzige Größe mit Spielraum Weg 1 = √(m_e·m_μ), also die Polmassen; K_frak schließt 99,99%, es bleibt Rest 8,4e-5 = ~7700σ der Massengenauigkeit (1,1e-8) → zu groß für Messrauschen, Aussage ÜBER die Polmassen: √(m_e·m_μ) ist unter starker Lesart nicht die geometrisch exakte Größe. Strukturgleich zum θ-Fall (dort (√2,2/9) verfehlt m_μ/m_e um 1e-5, hier E₀-Konstruktion verfehlt Polmassen-E₀ um 8e-5) — θ-Rest (1e-7) und α-Rest (8e-5) = ZWEI UNABHÄNGIGE ZEUGEN desselben Effekts (Polmasse ≠ geometrisch exakte Ebene). Preis: setzt starke Lesart voraus (Weg 2 exakt), Verkleidungs-Berechnung bleibt Bringschuld; als Kalibrierungsartefakt aber nicht mehr abtubar (α überbestimmt, Massenpräzision zu hoch). PRÄZISIERT (Johann: „es gibt die zwei Wege bei α"): die zwei Zeugen sind NICHT gleich stark — ASYMMETRIE. α-Rest ist MODUSUNABHÄNGIG, weil Weg 2 (E₀²=4√2·m_μ/ξ^p) m_e gar nicht benutzt → μ/e ist bei α KEIN Anker → 8e-5 ist echter Test von m_e gegen Geometrie, keine Selbstreferenz, gilt referenzfrei UND unter P42. θ-Seite dagegen: θ_ref aus μ/e gewonnen → μ/e Anker → 450σ zur Hälfte Selbstreferenz → Zeuge NUR referenzfrei. Der starke, modusunabhängige Beleg der Verkleidungsschicht ist damit α ALLEIN; θ stützt denselben Schluss nur unter Referenzfreiheit. (Korrigiert meinen Zwischenfehler, α und θ gemeinsam als modusabhängig abzuwerten — die zwei α-Wege machen α gerade zum robusten Zeugen.) WICHTIG: gilt NUR für α — bei der Leiter (Rest 0,5% = 250000× Messgenauigkeit) trägt das Argument NICHT, dort reine Theorie-Näherung. ABSCHNITT „Leiterübergreifende Kopplung: ein generationslineares Korrekturgesetz" + Skript-Teil K (Johanns Hinweis, dass leiterübergreifende Beeinflussungen denkbar sind): die drei krummen Exponenten p1=0,387/p2=0,769/p3=1,157 sind NICHT unabhängig — (1) multiplikativ konsistent: p3=p1+p2 auf 6e-14 (τ/e trägt keine neue Info, ist Produkt der Stufen); (2) effektive Faktoren N1:N2:N3=38,89:77,06:115,55 = 1:1,981:2,971 ≈ 1:2:3 → Korrektur wächst LINEAR mit Generationszahl, N_g≈g·N₀ mit N₀≈38,6 (Einzelschätzungen N1,N2/2,N3/3=38,89/38,53/38,52, <1% konsistent). Das ist der strukturelle Grund, warum konstantes K_frak die Leiter nicht schließt und warum 89-statt-100 ins Leere läuft: Leiter verlangt generationszählenden Faktor, nicht festen; bei α nur eine Skala → ein Faktor genügt. Generationsabhängige Verkleidung damit konkret: linear in g. OFFEN (P35): N₀≈38,6 nicht hergeleitet (100/e=36,8, 100/φ²=38,2, 39 treffen nicht genau); δ-Phasensektor (p=−0,88) fügt sich nicht offensichtlich in die Magnitude-Leiter. Aus „drei krumme Exponenten" wird „generationslineares Gesetz N_g=g·N₀ mit unbestimmtem N₀". METHODEN-KORREKTUR (Johanns Einwand: man darf nicht Referenzpunkt UND Vergleich zugleich): zwei EINANDER AUSSCHLIESSENDE Modi klargestellt — Modus 1 (referenzfrei, alle Verhältnisse aus ξ vorhergesagt: μ/e, τ/μ, τ/e alle Prüfpunkte, N_g-Gesetz zulässig, 1:2:3 an 3 Punkten); Modus 2 (P42: m_μ/m_e ist Anker, verbraucht, KEINE Prüfgröße mehr → N_g-Bilanz gegenstandslos, einzige unabhängige Leiter-Prüfung m_τ läuft über Zirkulant). N_g-Analyse gehört AUSSCHLIESSLICH in Modus 1. μ/e als Anker UND N_g-Prüfpunkt = unzulässige Doppelbuchung (mein vorheriger Fehler mit den „1500σ"). Das 1:2:3 ist nur referenzfrei dreifach belegt; unter P42 stützt es sich nur auf τ/μ, τ/e (gleiche τ-Masse, geringe Präzision). Zirkulant trägt μ/e ohnehin auf 1e-5 ohne g-Korrektur — die g-Korrektur betrifft allein die grobe ξ-Leiter, nicht die präzise Zirkulant-Schicht. TOLERANZ-BILANZ nachgetragen (Johann: „wo sind die Rechnungen zu den Abweichungs-Toleranzen") — Skript-Teil L + Tabelle in 292: roh vs. N_g-korrigiert je Stelle in %-und-σ_exp (μ/e 0,521%→0,0033% aber 2,4e5→1,5e3σ; τ/μ 1,038%→−0,0031%, 154→0,47σ; τ/e 1,565%→−0,0052%, 232→0,78σ). Gesetz drückt Leiter-Abweichung Faktor ~300; τ-Stellen fallen IN die Toleranz (<1σ), μ/e bleibt 1500σ (500× präziser gemessen) — aber dieser Eintrag ist NUR im referenzfreien Modus 1 eine Aussage, unter P42 fällt μ/e als Anker aus der Bilanz. Zirkulant-vs-Leiter für μ/e (0,001% vs 0,52%, Faktor 530) ebenfalls gebucht: Zirkulant trägt Präzision, Leiter Größenordnung. Rest sitzt in 1:2:3-Feinabweichung (~1-2%) und N₀. KLÄRUNG „100 vs 38,6" + 100/φ²-Spur (Johann): häufiges Missverständnis ausgeräumt — die 100 in K_frak=1−100ξ (feste korpusweite Skala: X-Flip, T_CMB, E₀-Brücke) und N₀≈38,6 (Faktor pro Generation in der Leiter) sind NICHT dieselbe Größe; die Leiter braucht nicht „weniger Rekursionen", sondern eine ANDERE Art: generationszählend N_g=g·N₀ (g=2→77, g=3→116, teils MEHR als 100). Vergleich als „Rekursionstiefen" geht ins Leere. Als ausdrücklich UNBEWIESENE Spur (P35, nicht als Herleitung gebucht): 100/φ²=38,20 nahe N₀, gegen τ-Stellen (im referenzierten Modus einzige Prüfgrößen) nur 0,87% Abweichung — wäre N₀=100/φ² exakt, folgte die Leiter-Grundeinheit über einen Faktor φ⁻² aus der K_frak-Skala (Magnitude+Korrektursektor an derselben Konstante); das knappe 1% trägt die Behauptung aber nicht, bleibt Spur bis zur N₀-Herleitung. TOLERANZ-MASSSTAB (Johanns Methodenpunkt: „du versuchst erneut punktgenau zu landen, das ist prinzipiell unmöglich, das Ergebnis soll nur innerhalb der Toleranzen bleiben"): 100/φ²-Bewertung KORRIGIERT — der richtige Maßstab ist nicht Punktgenauigkeit (prinzipiell unerreichbar, Werkstatt-Prinzip: Realität reicher als Messtechnik) sondern Verträglichkeit INNERHALB der Bestimmungstoleranz von N₀. N₀ folgt im referenzierten Modus allein aus τ-Stellen, begrenzt durch m_τ-Unsicherheit (±0,12 MeV) → N₀=38,52±0,21 (~0,5% Toleranz). 100/φ²=38,20 liegt damit 1,6σ_N₀ entfernt = INNERHALB der Toleranz → ZULÄSSIGER Kandidat, NICHT „knapp verfehlt und verworfen" sondern „mit gegenwärtiger Bestimmung verträglich, nicht widerlegt". Belle II oder N₀-Herleitung entscheidet. ZUSÄTZLICH Unvollständigkeits-Schluss umgestellt: Vollständigkeit heißt NICHT punktgenaue Landung auf letzter Ziffer (weder möglich noch Ziel), sondern kein Rest mehr der ÜBER die Toleranzen hinausragt und nur durch freien Parameter geschlossen wird. Maßstab = Toleranz, nicht letzte Ziffer. DE+EN je 12 S.

## 10. Juli 2026 — Dok. 302: Elementarzellen, Ein-Bit-Kapazität und Partitionsinvarianz — eine spektrale Antwort (DE+EN je 5 S.)

Antwort auf eine IPI-Anfrage (Takayuki Ueda) nach dem beobachterunabhängigen Kriterium für „Elementarzellen", der Ein-Bit-Kapazität und der Invarianz der Entropie unter Ursprung/Orientierung/Koordinaten/Foliation. Kernaussage: Die fünf Einwände sind gegen eine RAUMZELL-Ontologie korrekt, und FFGFT beruht auf keiner solchen. Die elementaren diskreten Objekte sind keine Raumbereiche, sondern INVARIANTEN — Windungsklassen (π₁(T⁴)≅ℤ⁴, Träger der Informationseinheit) und Eigenmoden (Massenspektrum). Individuierung spektral/topologisch (Invarianten), nicht räumlich → beobachterunabhängig. Diskretheit topologisch (π₁=ℤ⁴, keine halbe Windung) UND spektral, nicht aus einer Kachelung. Invarianz automatisch, weil Entropie eine Funktion des Spektrums (Spur über Eigenwerte) ist; Ursprung-/Orientierungs-Unabhängigkeit zusätzlich explizit über D6-Äquivalenz („Verzahnung, nicht Ausschnitt", Dok. 300).

Korpuskonform an Dok. 257 ausgerichtet: die minimale Informationseinheit ist PER DEFINITION das Windungsquant Δw=1 (skalenuniversell, energieunabhängig); das ln2 ist NICHT die fundamentale Einheit, sondern der thermodynamische Schatten — die Bit-Energie ist skalenspezifisch (E_bit=ħc/L), Landauers kT ln2 nur der Spezialfall bei einer Skala. Fläche als fundamentale Bit-Definition ausgeschlossen: der T⁴ ist randlos (∂T⁴=∅), eine Fläche ist eine verlustbehaftete Projektionsfläche (Energie = skalenabhängige Projektion der Geometrie, Dok. 257), keine fundamentale Raumpartition. Ehrliche Vier-Kategorien-Bilanz (Governance, im Sinne Stefaan Vossens): deklarierte Annahme (kompakte Geometrie T⁴/Z₃, ξ) / Definition (Bit ≙ Δw=1, topologisch begründet) / abgeleitet (Diskretheit π₁=ℤ⁴, E_bit, Invarianz) / empirische Exposition (Massen, m_τ=1776,969 MeV, Belle II) / benannte Setzung (Realität des Objekts, Ebene 3 aus Dok. 301). Verweise: Dok. 257/255 (Informationseinheit), 282/283 (Hilbert-Raum/Spektrum), 300 (Verzahnung), 301 (drei Ebenen). DE+EN je 5 S., 0 Fehler/0 Glyphen.

## 9. Juli 2026 — Dok. 301: Der Umkehrtest — Information als Ausgang, nicht als Grundeinheit (DE+EN je 9 S.)

Dok. 301 (DE+EN, je 9 S., Inhaltsverzeichnis, 14 nummerierte Abschnitte, 0 Glyphen) beantwortet die Informationsfrage mit einem Kriterium statt einer Gegenintuition: **fundamental ⟺ umkehrbar**. Energie ist intrinsisch und reversibel (T̃·m=1 → E=m=1/T̃, kein Ein/Aus); Information ist relational und der AUSGANG eines Comparators — das ICE-Dreieck als entprellter Comparator gelesen (Energie- und Kohärenz-Signal gegen eine Referenz entschieden, mit Hysterese/Totband). Das Bit ist die ultimative Reduktion (Dok. 296-Reduktionsprinzip an seiner Grenze) und irreversibel: die Eingangsbedingungen WAREN und sind gelöscht; Landauer kT ln2 = genau diese Irreversibilität. Daher scheitert die Information-als-Fundament-These am Umkehrtest.

AD/DA-Illustration: die Zerlegung einer Torsionswicklung in 75 Teile und Rekonstruktion ist verlustbehaftet (Glättung = Interpolationsannahme). Resonanz-Präzisierung: der kompakte Torus hat ein DISKRETES Spektrum (Dok. 283), es gibt einen kleinsten erlaubten Sprung; eine resonanz-getreue Umsetzung ist NICHT verlustbehaftet — Verlust nur bei beliebiger/gröberer Quantisierung; „reicher als jede endliche Treppe" ist eine skalenübergreifende Aussage.

DREI EBENEN von Information: (1) Bit = Ausgang/Reduktion, (2) Beschreibung = Projektion/Koordinatenwahl/unvollständig, (3) absolute Identität = das vollständige T⁴-Objekt = das einzig Fundamentale (Selbstreferenz, Dok. 248 §8). Status-Temperaturen: Bit = bewiesen, Beschreibung = strukturell, absolute Identität = ontologische Setzung.

REFLEXIVER SCHLUSS, in zwei getrennten Abschnitten mit unterschiedlicher Temperatur: (a) „Zeitliche und topologische Randlosigkeit" — als FOLGERUNGEN gebucht, OHNE Spekulationsmarker, weil aus Analysis und Topologie ableitbar: die ξ-Rekursion ξ_{n+1}=ξ_n(1−100ξ_n) erreicht 0 in keinem endlichen Schritt (kein erster/letzter Schritt), kein strukturloser Anfangszustand (bräche die Skaleninvarianz), Zeit = D(k) ohne markierbaren Ursprung (Dok. 295), kein Außen (∂T⁴=∅, topologische Tatsache) → die absolute Identität ist räumlich UND zeitlich randlos, dieselbe Eigenschaft in zwei Gestalten. (b) „Der reflexive Fall — was über die Mathematik hinausgeht" — ausdrücklich als philosophisch-spekulativ markiert (P35), nur zwei Interpretationssprünge: die Realisten-Setzung (die resonanzgetreue Beschreibung spurt ein reales Objekt nach — Wette, nicht Beweis, aber durch die Resonanztreffer falsifizierbar) und die Diagnose des Wort-Reflexes („Im Anfang war das Wort"/it-from-bit als kultureller Reflex, den der Umkehrtest umdreht: das Wort ist das Bit, die letzte Reduktion, nicht die erste Schöpfung); dazu die Selbstprojektion (FFGFT ist ein T⁴-Prozess, der T⁴ beschreibt, Dok. 248 §8) und die Auflösung der Ausgangsfrage („wieviel ontologische Realität hat FFGFT?" ist selbst eine Ebene-2-Frage, die auf Ebene 3 zerfällt — kein Außen, kein Vorher). FFGFT ist damit ausdrücklich Ebene 2 (Beschreibung, notwendig unvollständig) — Ehrlichkeit, kein Understatement.

Anschluss an Dok. 296 (Reduktionsprinzip, Akkumulation-vs-Ersetzen) und Dok. 300 (K_frak, Comparator/Entprellung). DE+EN je 9 S., 0 Fehler/0 Glyphen.

## 8. Juli 2026 — Dok. 299: Die Einbettung ι — Arbeitsdokument und Forcing-Protokoll (DE+EN je 5 S.) + Dok. 190 R47

Dok. 299 (DE+EN, je 5 S., 0 Fehler/0 Glyphen) setzt den in Dok. 297 als offene Vermutung markierten nächsten Schritt als vorregistriertes Protokoll auf (P35). Fixiert vor der gemeinsamen Ausarbeitung: Definitionsbereich (HLV-Seite — geometrisches A₅-Singlet und temporal-dynamisches U₃-Fenster, Dok. 297, sauber getrennt); Zielraum (FFGFT — H=L²(T⁴)⊗ℂ³ Dok. 230/282, Gedächtniskern Dok. 283, eingefrorene 75-Windung Dok. 295, K_frak-Rekursion); die Kandidatenabbildung ι in zwei Zweigen (ι_geo → ξ→0-Fixpunkt; ι_dyn: U₃ ↪ Hard-Reset-Kern M_m<75 = Markov-Grenzfall; Hierarchie U₃ ⊂ Markov ⊂ archimedisch ⊂ log-Spirale e); die matched nulls auf der Zeitachse (memory-free Markov, phase-/time-shuffled, coherence-/information-only, generischer Fenster-Operator, ML-Basislinie — gespiegelt aus Marcels OP8-Familie und dem C3A5-Spezifitätstest Dok. 293/294, kalibriert exakt→0/generisch→Band); Entscheidungs-/Falsifikationskriterium (Kopplung an den vorregistrierten OP8-Test). KERN: die Forcing-Frage — erzwungen (echtes HLV⊂FFGFT im Zeitsektor) vs. bloß zugelassen (Kompatibilität), mit Zirkularitäts-Vorbehalt (U₃ ist per Konstruktion Hard-Reset → das Forcing muss aus einer UNABHÄNGIGEN Signatur kommen, nicht aus der Definition). Drei Artefakte als Bringschuld benannt (φ-Projektor auf ℂ³, Markov-Kern-Abstandsrechnung, Forcing-Metrik). Alles im Zeitsektor, in einheitlicher D6+Zeit-Schreibweise. Symmetrische Disziplin: bindet auch, wenn der Ausgang FFGFT begünstigt. NACHGETRAGEN (8. Juli, nach Marcels Zustimmung + IOTA-BRIDGE1 v0.1): die matched-nulls-Sektion um den geometrischen Zweig (ι_geo) ergänzt — Marcels Null-Familie (zufällige C3/A5-Einbettungen, alternative Projektionssterne, Tetra-/Oktaeder-Kontrollen, shuffled C3 bases, spektral gematchte Nullträger) als ι_geo-Familie aufgenommen, kalibriert am C3A5-Spezifitätstest (Dok. 294, Median-RMS ≈22, exakt-ikosaedrisch = Abstand 0); als beidseitig gebuchte Architektur markiert (Krueger IOTA-BRIDGE1 v0.1 prüft dieselbe finite Proxy-Frage unter Spektral-/C3-A5-/U3-Zeitfenster-/Screen-Diagnostik; Claim-Grenze eng: PASS = finite-proxy iota-forcing candidate, BLOCK = Route verengt). 299 DE 6/EN 5 S., 0 Fehler. ERGEBNIS-ABSCHNITT (8. Juli): der Zeitzweig-Gegenlauf ist ausgeführt und gelockt (Dok299_Skripte/ffgft_299_iota_gegenlauf_locked.py, SHA256, Seed 20260708). Zeuge = BLP-Rückfluss 5,125 (Dok 283, neu berechnet); U3-Hard-Reset-Fenster 0,97 ≈ generisches Fenster 0,98 ≪ Zeuge → ι_dyn zugelassen, nicht erzwungen → Dok 297 bestätigt. Geometrischer Zweig: feste 63,435°-Referenz, ikosaedrisch 0° vs. Zufallsstern-Median 21,65° (Anti-Zirkularität vorgeführt). Ergebnis-Abschnitt in 299 DE/EN eingetragen (jetzt je 6 S.). KORREKTUR (8. Juli, nach Einwand): der v0.1-Zeitzweig reduzierte das Spiralfenster winkellos → Rückfluss 0 war beinahe tautologisch. Korrigierte Fassung ffgft_299_iota_gegenlauf_winding_locked.py schreibt den Windungswinkel θ explizit in den Kern (k_θ(s)=e^{-s/τ}cos(θs)) und fährt θ durch, gegen phasengeschüffelte Nulls (gleiche Einhüllende). Befund: θ=0 und θ=1/φ → in Bande (zugelassen); goldener Winkel ≈137,5° → Rückfluss 0,159 ÜBER Bande (q95 0,076); θ_c≈1,82 rad. Verdikt jetzt BEDINGT auf θ* des nativen Carriers, nicht vorab entschieden. Ergebnis-Abschnitt in 299 DE/EN entsprechend ersetzt. K_FRAK-KORREKTURWERT (8. Juli): Schließungs-Komma der aufgerollten Rekursion hergeleitet — 75 um ε verkürzte Umdrehungen schließen exakt (75(1−ε)=74) ⇒ ε=1/75=100ξ; Korrekturwert K_frak=1−100ξ=74/75=0,9867 (Korpusform; Anker Dok 133: Faktor 100 aus RG-Lauf, K_frak durch m_e/m_μ-Konsistenz fixiert). Prüfskript Dok300_Skripte/ffgft_300_kfrak_schliessungskomma_pruefung.py. Als zitierbarer Abschnitt in 299 DE/EN eingetragen (je 7 S.); für Marcels Projektion damit prüfbare Größe: Faktor projizierte Umdrehung ↔ aufgerollte Kurve = 1−100ξ=74/75, unabhängig verankert (Dok 133). NEU Dok 300 (8. Juli): "Spiral-Time als Auslesung und entprellter Comparator — der geteilte Korrekturfaktor K_frak=1−100ξ (74/75)" (DE/EN je 4 S.). Beantwortet Marcels Zwei-Rollen-Frage: Rolle 2 = Comparator mit Zeit-Hysterese (Entprellung), Referenz muss Ableitung sein, nicht Kopie (hard=copy war zirkulär). Kette: 2/9+D6+Zeit ⟹ selbe Spirale ⟹ geschlossene Umdrehung ⊂ 75-Windung ⟹ Umrechnungsfaktor K_frak=1−100ξ=74/75 als Konsistenz-Bedingung; Anker Dok 133 (Faktor 100 aus RG-Lauf, K_frak durch m_e/m_μ-Konsistenz fixiert; das Schließungs-Komma re-exprimiert 100ξ, leitet sie nicht ab), Kategorie B. Bezug zu Dok 298 (Projektion verschluckt das Komma, K_frak trägt es an SI wieder ein).

DAZU Dok. 190 R47 (DE+EN, Tabellenzeile R-Serie): Zeitsektor-Präzisierung von R43. Dimensional zählt HLV größer (⊃, T⁷=T⁴×T³, das 3′-Fenster als zusätzlich); gehaltlich im Zeitsektor gilt HLV⊂FFGFT — das Spiralzeit-Fenster ist ein beschränkter Ausschnitt der ausgerollten Rekursionszeit, nicht additiv (D6+Spiralzeit ⊂ D6+Rekursionszeit). Marcels Objekt präzise = überdämpfter −1/φ-Zweig (3′-Fenster, trägt Struktur/keine Masse), NICHT der volle Rekursionsoperator R (dessen massentragender φ/D4-Zweig FFGFTs ist). Beide Sinne koexistieren widerspruchsfrei in einheitlicher D6+Zeit-Schreibweise: dimensional ⊃ (R43), gehaltlich/zeitlich ⊂ (R47). OP8-konsistent (warmes EEG-Fenster löst die Windung nicht auf). 190 DE 38/EN 33 S., 0 Fehler.

## 3. Juli 2026 — STAGE-10-VERDIKT: BLOCKED (Brücke abgeschlossen)
Marcels Stage-10-Lauf (stage10_runN_BD17A_blind_dynamicCe_v1_1_fast, 2026-07-03T05:40:20Z) meldet STAGE10_BD17A_BLIND_DYNAMIC_CE_BLOCKED_OR_NOT_SEPARATED. UNABHÄNGIG bestätigt: FFGFT-Harness 99e11399 (unverändert) auf Marcels Roh-Loop-Winkel angewandt → gleiches Verdikt BLOCKED. Integrität: Marcels Generator-Hash == Siegel 8bd0f7ce (Blindheit bewiesen), θ=2/9 nicht in Konstruktion (nur Scoring), kein Tuning. Zwei unabhängige Methoden identische Rangfolge: Marcel Kernel-Score target 0,018 < edge_operator_shuffle 0,062; FFGFT-Orbit target f(2/9)=0,024 (flach 0,79 dominiert) < edge_shuffle 0,082. Doppelt blockiert (weder Orbit-Selektion noch Nulls geschlagen). KEIN Widerspruch zu FFGFT: No-Go war vorhergesagt (flache Z₃-Holonomie kann 2/9 nicht als topolog. Invariante tragen, Lindemann-Weierstrass Dok 291); Zirkulant-2/9 (Massenspektrum) und Q=2/3 andere Ebene, unberührt. Verdikt-Dokument STAGE10_VERDIKT_2026-07-03.md. DREI SIEGEL GEÖFFNET: 8bd0f7ce (Marcel Generator, bestätigt genutzt), 99e11399 (FFGFT Harness, unverändert), 858268 (FFGFT Begründung Dok 291, freigegeben; Master-Hash aus freigegebenem Inhalt reproduziert → keine Rückkonstruktion). Dok 291 nicht mehr intern. Öffnungs-Paket DOK291_ENTSIEGELT_2026-07-03.zip (291 DE+EN + 5 Skripte + Manifest + Verdikt + VERIFY_SIEGEL.sh) an IPI-Verteiler. Protokoll hat wie vorgesehen funktioniert: echtes blindes Verdikt, negativ.

## Release-Vorbereitung v1.1.7 (3. Juli 2026)
Dok 205 (Narrativ) um Abschnitt „Der aktuelle Stand — eine Standortbestimmung" erweitert (DE+EN, je 13 S.): fasst den Gesamtstand narrativ zusammen — Leptonsektor in zwei Schichten (Zirkulant=Präzision, ξ-Leiter=Größenordnung, μ/e=P42-Referenzpunkt, m_τ=1776,97 die eine Prüfung), α keine Kalibrierung (zwei E₀-Wege, Überbestimmung), θ=2/9 blind geprüft/BLOCKED (vorhergesagte Richtung, Wert in der Blindheit), Toleranz-Maßstab statt letzter Ziffer. RELEASE_NOTES_v1_1_7.md (DE+EN) erstellt: Brücke abgeschlossen mit blindem Verdikt, dreifache Vorregistrierung, Leptonsektor-Prüfung, generationslineares Korrekturgesetz, Toleranz-Methodik; DOI wird beim Zenodo-Upload vergeben (löst v1.1.6/21061423 ab). README.md + README_de.md aktualisiert. GEWICHTUNG KORRIGIERT (Johann: „das mit HLV nimmt zu viel Raum ein, ansich unbedeutend für FFGFT — interessant wäre nur gewesen, wenn eine Brücke gefunden worden wäre; beschränke dich auf das was für FFGFT wichtig ist"): die HLV-Brücke war ein Test mit negativem Ausgang und gehört nicht ins Schaufenster. HLV-Hauptsektion ENTFERNT, ersetzt durch FFGFT-interne Hauptsektion „Leptonsektor — Massen, α und die Koide-Phase" (Zirkulant/ξ-Leiter, P42, m_τ, α zwei Wege, generationslineares Gesetz, θ=2/9 lokalisiert). HLV nur noch als kurzer Absatz „Externer Gegencheck (HLV/BD17A) — negativ" innerhalb der Lepton-Sektion (5 statt 17 Erwähnungen im README, 2 statt 10 in den Release Notes). Release Notes v1.1.7 neu strukturiert: Leptonsektor/α/m_τ/Toleranz voran, HLV als Schluss-Anmerkung. 205-Standortbestimmung: θ/HLV-Absatz von Protokoll-Detail auf 3 Sätze gestrafft (FFGFT-Fokus). Versionshistorie v1.1.7 FFGFT-fokussiert (nicht bridge-voran), Repo-Struktur um Dok291_Skripte/Dok292_Skripte, Korrekturregister P1–P38→P1–P42. STATUS 2/9 KORRIGIERT (Johann: „das liest sich immer noch als ob vieles offen ist — 2/9 ist doch keineswegs offen, wo eckts da noch"): θ=2/9 durchgehend von „lokalisiert/nicht hergeleitet/offenes Ziel" auf „die Zirkulant-Phase" umgestellt — 2/9 ist KEIN freier Parameter und kein empirischer Fit, sondern der Wert, den die Diagonalisierung des Z₃-Zirkulanten AUSGIBT (gefunden, nicht gesucht; aus Hilbertraum-Übersetzung 230/231/232→282). Die Eliminationskette CHARAKTERISIERT ihn positiv (dynamische betragserhaltende Holonomie-Phase, χ=π/2); die Transzendenz ist positives Wissen (beweist: aus keiner flachen/topologischen Quelle). Offen ist NICHT der Wert (steht fest), sondern allein die Frage nach einer noch tieferen Erzwingung — eine Ebene UNTER dem fertigen Resultat. Betrifft README DE+EN, Release Notes DE+EN, 205-Standortbestimmung DE+EN. Sauber getrennt: 2/9 bestimmt, N₀≈38,6 (Leiter-Grundeinheit) weiterhin offen — nur letzteres heißt „nicht hergeleitet". NACHGESCHÄRFT (gleiche Rückmeldung, zweiter Durchgang): die „offen bleibt / eine Ebene darunter / noch tieferes Grundprinzip"-Schlusssätze bei 2/9 in allen vier Dateien ersatzlos gestrichen (sie erzeugten den offen-Eindruck, obwohl der Wert feststeht; die Frage nach einem „noch tieferen Prinzip" gilt für jede ξ-Größe und zeichnet 2/9 nicht aus) → enden jetzt bei „die Koide-Phase ist erledigt / settled". In 205 zusätzlich: Standortbestimmungs-Einleitung von „zwei markieren Grenzen" auf „Sektor im Wesentlichen geschlossen" umgestellt; im Toleranz-Maßstab-Absatz „der Feinwert der Phase" aus der Offen-Liste ENTFERNT (Widerspruch zur Erledigt-Aussage) → N₀ als EINZIGER offener Punkt des Leptonsektors ausgewiesen.

## Dok 190: P43 (calc_De.py / K_frak) (3. Juli 2026)
Auf Johanns Frage, ob die K_frak-mit-100-Formeln im Rechner calc_De.py nach dem generationslinearen Befund (Dok 292, N_g=g·N₀) zu überarbeiten sind — als reine Notiz in Dok 190 gebucht (P43 DE+EN, Tabellenzeile, kein calc-Doc-Umbau). Nachgeprüft: calc_De.py verwendet K_frak=1−100ξ NICHT explizit. (i) α=ξ·E₀² mit E₀=7,398 MeV (geometrischer Weg-2-Wert); da 7,398/7,348=K_frak^(−½) ist K_frak über die E₀-Wahl bereits absorbiert (1/α=137,035 ohne separaten Faktor) — schon mit dem Zwei-Wege-Bild konsistent, kein Widerspruch. (ii) Massen laufen über per-Teilchen-(r,p) (m=r·ξ^p·v; e/μ/τ-Fehler 1,18/0,66/0,37%) — das ist die grobe ξ-Leiter, in der N_g=g·N₀ greift; Ersatz der (r,p) durch N_g erst nach Herleitung von N₀≈38,6 ein Gewinn (sonst Fit gegen Fit, P35), bis dahin bleiben die (r,p). 100 in K_frak (feste RG-Skala, P40) und N₀ (Leiter-Faktor pro Generation) bleiben getrennt. 190 DE 37/EN 32 S., 0 Fehler. Korrekturregister P1–P42→P1–P43 in READMEs nachgezogen.

## v1.1.7 Zenodo-DOI vergeben (3. Juli 2026)
DOI 10.5281/zenodo.21158441 (löst v1.1.6/21061423 ab). Platzhalter nachgezogen: README DE+EN je 3 Stellen (Badge, Zenodo-Zeile, Versionshistorie), Release Notes DE+EN je 1. Kein Platzhalter mehr offen; alte DOI nur noch als „löst ab"/Historie. Konzeptioneller Teil gebucht: α=1 im erweiterten Natursystem (011/014), SI-Wert = Buchhaltung; gleiche Architektur G=ξ²/(4m_char)×Umrechnung (012/013) → Gravitation als Buchhaltung zur SI, Quantengravitationsproblem stellt sich strukturell nicht (woran die meisten SM-Erweiterungen scheitern). DAZU Sektion „Zwei Schichten, die einander nicht brauchen" (Johanns Frage, ob 2/9 überhaupt nötig ist und ob 292 die SI-Umrechnung bestätigt): (1) 2/9 wird für die Massenberechnung NICHT benötigt — die ξ-Leiter (006/046) rechnet ohne 2/9; 2/9 erscheint erst ab 282 als nachträglich entdeckte Ordnung (Zirkulant-Phasenwinkel), Erklärungs- nicht Rechenschicht, ersetzt gefitteten Leiter-Koeffizienten durch reine Zahl, macht Q=2/3 einsichtig; (2) SI-Umrechnung als NOTWENDIG bestätigt (jede Absolutzahl braucht Brückenkonstante, Verhältnisse nicht — P40; 450σ-Befund als schärfster Beleg der Ebenen-Trennung), aber NICHT als auf Präzision validiert richtig (schließt 98,8% der α-Lücke via K_frak, Rest ~1e-4 offen; Kalibrierung kein Test); (3) Kernbefund Unabhängigkeit — Leiter rechnet ohne 2/9, Zirkulant erklärt ohne Leiter, SI übersetzt ohne 2/9; geteiltes ξ und K_frak = Konsistenz, keine Abhängigkeit. VORANGESTELLTE HERKUNFTS-SEKTION „Wie 2/9 überhaupt sichtbar wurde" (Johanns Hinweis, dass die kausale Herkunft über die Hilbertraum-Erweiterung fehlte): 2/9 wurde nicht gesucht sondern gefunden — die Hilbertraum-Brücke 230/231/232 bildet Loop-Observablen als selbstadjungierte Operatoren ab; erst deren Fortführung bis zu den Massen (282) zeigte, dass die drei Lepton-Massen das Spektrum eines hermiteschen Z₃-Zirkulanten auf der ℂ³-Faser von H=L²(T⁴)⊗ℂ³ sind, in dessen Eigenwerten θ=2/9 als Diagonalisierungs-Ausgabe erscheint (kein Ansatz). Damit prüft 292 eine ENTDECKUNG, keine Eingabe — das begründet erst, warum die Daten-Richtung aussagekräftig ist. ABGESCHLOSSEN mit Schluss-Sektion „Der Rest als Signatur der Unvollständigkeit" (Johanns Meta-Einordnung): die Gegenrechnung hat die Aussagen geschärft (von „zwei reine Zahlen" zu vermessenen Größen), aber auf jeder Ebene bleibt ein Rest (θ 1e-7, Leiter 1–3%, α 1e-4, δ-Feinwert offen, K_frak-Muster nicht schließend) — kein Widerspruch, aber nicht null; ein Residuum das mit der Auflösung schrumpft ohne zu verschwinden = Signatur einer Näherung an Tieferes, nicht eines abgeschlossenen Fundaments → Beleg der UNVOLLSTÄNDIGKEIT. Kernpunkt: der Rest sitzt systematisch in der ÜBERSETZUNGSSCHICHT, nicht im geometrischen Kern (Q=2/3 rein geometrisch exakt, α=1 im Natursystem, Leiter-Verhältnisse rational; Rest entsteht erst bei Polmassen/SI-Umrechnung/Brückenkonstante) — lokalisiert die Unvollständigkeit präzise: nicht in ξ/Zirkulant, sondern in der noch nicht hergeleiteten fraktalen/QED-Verkleidung; vollständig erst wenn K_frak generationsabhängig aus der Geometrie folgt statt in Brückenkonstante absorbiert. Jetzt DE+EN je 9 S. DOK-291-VORREGISTRIERUNGS-SIEGEL (2. Juli, Johanns Symmetrie-Einwand): das Post-hoc-Risiko ist SYMMETRISCH — so wie Marcels Generator nicht nachträglich auf 2/9 getunt werden darf, darf die FFGFT-Herleitung nicht nachträglich auf ein bekanntes Ergebnis rückkonstruiert werden. Lösung: Dok 291 (DE+EN) + fünf Mechanismus-Skripte (allpass_theta, allpass_carrier_selection, forced_vs_contingent, delta_golden_daempfung, holonomie_landschaft) VOR Stage 10 kryptographisch versiegelt, Inhalt bleibt verborgen. Master-Siegel SHA256 858268627a0c7813a127628129b130815dc306b6c8033d7ab2fe3cbc14145276 (deterministische Konkatenation, Reproduktions-Kommando im Manifest Dok291_Skripte/DOK291_VORREGISTRIERUNG_SIEGEL.md). Damit dreifacher symmetrischer Lock: (1) Marcels Generator eingefroren+gehasht (Zenodo), (2) FFGFT-Harness 99e1.. (Verteiler), (3) FFGFT-Begründung 858268.. (dieses Siegel). Alle drei vor dem Verdikt; nach dem Verdikt öffnen sich alle → Konvergenz nachweisbar UNABHÄNGIG. 291 bleibt physisch intern bis zum Verdikt. GEGENSEITE BESTÄTIGT (2. Juli, Marcel im Verteiler): HLV Stage-9-Generator/Source-Siegel 8bd0f7ce...8d1b8fe0, CONFIG 45020f82...c5f06c, OneClick-Notebook 7c295cb1...772a240 — damit ist die Drei-Siegel-Struktur BEIDSEITIG geschlossen: (1) HLV-Generator 8bd0f7ce (Marcel), (2) FFGFT-Harness 99e11399 (Johann), (3) FFGFT-Begründung 858268 (Johann), alle vor dem Verdikt. Unabhängigkeit der Konvergenz jetzt in beide Richtungen kryptographisch nachweisbar. Marcel bestätigt Stage-10-Bedingungen unverändert (blind θ*=2/9, kein Tuning, kein WN-Support). Marcels Hashes im Siegel-Manifest gesichert. ZUGLEICH Dok 207 (Bewusstsein-Brücken, DE 21/EN 20 S.) um interpretative Unter-Sektion „Determinismus und Agentität“ erweitert (in Brücke A, mit interpretation-Markierung): das Grundmodell ist deterministisch und lokal (Bell geometrisch real auf T⁴, Dok 230), entfernt den Zufalls-Weg zum freien Willen — ein mit FFGFT verträglicher Wille muss kompatibilistisch sein (Determinismus UND Agentität); Anker ist der selbstreferentielle eingebettete Beobachter (Dok 248/270), NICHT ein offener Physik-Parameter. Ausdrücklich: verträglich-mit, nicht begründet; physikalische Unterbestimmtheit (offene Phase) NICHT als Agentität lesen (gleicher Kategorienfehler wie „X=ξ^N, also hergeleitet“). Physik-Punkt in 291, Interpretation getrennt in 207. Zugleich klargestellt (nur Analyse, kein Doku-Eingriff nötig): die Irrationalen in 291 (√2, φ, π) beeinträchtigen die Genauigkeit nicht — Q=2/3 ist exakt (√2 und die Kosinusse kürzen sich analytisch, S=3/T=6), 1/φ³ und χ=π/2 sind bis ~10⁻¹⁵ ausgewertet, und 2/(9π) ist ein lasttragender exakter Transzendenz-Beweis (Lindemann-Weierstrass), kein Fehlerterm. davor 1. Juli 2026 — neues Dok. 290 „Folgen für die Informationsfrage: Betrag, Phase und der zweite Kanal“ (DE+EN, je 6 S., NEUSTRUKTURIERT: nach mehreren Einzel-Umbauten komplett frisch in 7 kohärente Abschnitte geschrieben — Ausgangslage / Zwei Kanäle / Das Photon / Was Informationsmenge heißt / Die absolute Menge in ξ / Folgerungen / Ehrliche Grenzen; kein Inhalt verloren, Zersplitterung behoben. PRÄZISIERUNG (DeepSeek-Review): (b) „Photon ist die Verbindung" korrigiert — das Eichpotential A_µ IST die U(1)-Verbindung, das Photon ist deren QUANTUM; Holonomie ist EIN eichinvarianter Observable (neben E=ħω, Impuls, Polarisation, keine Holonomien); „it from connection" begrifflich, nicht buchstäblich/formal-θ. (c) „Betrag legt Phase nicht fest" präzisiert: gilt nur BIS AUF einen Allpass-Faktor — Betrag legt den minimalphasigen Anteil fest (Bode/Hilbert), frei ist der Allpass, dort sitzt die θ-Holonomie (Min-Phase×Allpass, Dok 288); neues Skript minimalphase_allpass.py (rekonstruierte Phase==arg(H_min) ~1e-15, Rest==Allpass ~1e-15). Jetzt 5 Skripte. AUFLÖSUNG absolut/relational (DeepSeek-Punkt 1): das Dok behauptete beides (absolute Menge §6, relationale Phase §7) ohne Versöhnung; neuer Absatz Ende §6 — verschiedene Achsen: „absolut"=Menge/Maß, „relational"=Natur eines Datums. Eine Holonomie/Windung ist BEIDES: relational definiert (Schleifenintegral, kein lokaler Punktwert) UND absolut bewertet (eichinvariant, ganzzahlig); die absolute Zahl log2(1/ξ) ZÄHLT genau diese relationalen Windungssektoren. Neues Skript absolut_relational.py (Windung=3 als Schleifenintegral, halbe Schleife=1, eichinvariant unter einwertiger Umphasung; ~15000 Sektoren bis n_max~1/ξ, log2≈13,9 Bit). Absolutheit im Boden (Geometrie/ξ), Relationalität in den Freiheitsgraden — kein Widerspruch. Jetzt 6 Skripte. PRÄZISION (aus DeepSeek-Konsistenzprüfung Version 5): die Wendung „reine Phase / alle Physik in der Phase" beim Photon war ungenau — präzisiert zu „im Massenkanal reine Phase": null Ruhemasse-Betrag, der gesamte Ruhemasse-Inhalt ist Phase, ABER die Energie ħω bleibt eine Betragsgröße (§5). „reine Phase" meint den Ruhemasse-, nicht den Energiekanal. Reine Wortpräzision, keine Skript-Änderung. ERWEITERUNG §5 (zwei Absätze): (1) weder Periodenzahl N noch Fensterlänge Δt ist dem Photon intrinsisch — N=f·Δt vom Emissionsprozess gesetzt (monochromatisch=∞; spontane Emission: Atom legt f0 UND τ fest, N=f0τ=Q/2π; technisches Paket: eine Größe fest, Rest folgt); intrinsisch die dimensionslose Gestalt N (Δf/f=1/N), Δt=N/f Einkleidung; Spannweite ~2…5e6, keine universelle Periodenzahl/Fensterlänge. (2) Einwert (Johann): „1 Quant = 1 Bit" zählt nur die BESETZUNG (invarianter Boden), NICHT die Mode/Gestalt — die trägt variable Zusatzinfo; der Informationsgehalt eines Photons ist also variabel, aber per Freiheitsgrad durch die absolute ξ-Decke I1=log2(1/ξ)≈12,9 Bit (§6) gedeckelt. Fest: Boden (Quant) + Decke (I1); variabel: die Mode dazwischen. Brücke §5→§6. Neues Skript quant_bit_modeninfo.py. Jetzt 7 Skripte; Dok 290 jetzt 7 Seiten. KORREKTUR (Johann, berechtigter Widerspruch): die Formulierung „1 Quant = 1 Bit als invarianter Boden, Modeninhalt variabel bis I1" war intern widersprüchlich — sie verwechselte ZÄHLWERT und INFORMATIONSGEHALT. Ersetzt: ein Quant ist eine Anregung (Zählwert 1), KEIN Bitmaß; sein Informationsgehalt ist log2(M) Bit (M unterscheidbare Moden), variabel, pro Freiheitsgrad gedeckelt bei I1=log2(1/ξ). „1 Quant = 1 Bit" gilt NUR für M=2 (Kodierkonvention, kein Gesetz). Zählwert und Bitgehalt sind verschiedene Achsen (1 Quant in 2^13 Moden = 13 Bit = 13 binäre Quanten). §6 sauber eingeordnet: I1 ist nicht der Gehalt EINES Quants, sondern die absolute Decke pro Freiheitsgrad. §5-Itemize „Zahl" und §5-Absatz entsprechend neu; quant_bit_modeninfo.py Teil 2 neu. NEUER ABSCHNITT (Johann) „Statische und dynamische Definition des Bits" (vor §7): die bisherige Definition ist statisch (Struktur: Windung, log2 M, E0=ħc/L). Die dynamische ist die konjugierte Seite und zerfaellt in zwei: (a) KINEMATISCH/reversibel (T~-Seite): Flip dauert T~=ħ/E0=1/m0, E0·T~=ħ ⟺ T~·m=1 (Zeit-Masse-Dualitaet), Margolus-Levitin τ≥πħ/2E, Energie SETZT die Uhr ohne Verlust, Kosten=Zeit, Rate=Kapazitaet (Bit/s §5). (b) THERMODYNAMISCH/irreversibel (Landauer): Entropie kB·ln2, Loeschwaerme kB·T·ln2, haengt an T nicht E0, Kosten=dissipierte Waerme, in FFGFT EMERGENT (T^4 unitaer-reversibel -> kinematisch primaer). Bruecke: dimensionsloser Zaehlwert primaer, ×ħ,c→Energie/Zeit, ×kB→Entropie/Waerme; ħ,c,kB=SI-Buchhaltung; Energie zwei Rollen (Uhr vs. Waerme). Neues Skript bit_statisch_dynamisch.py. Jetzt 8 Skripte. SCHAERFUNG (Johann): „Buchhaltung" heisst NOTWENDIG, nicht entbehrlich — Absatz nach der Statisch/Dynamisch-keyresult. kB,ħ,c sind die notwendigen Einheiten-Bruecken: SI trennt K,J,s in eigene Einheiten, und sobald thermodynamisch GERECHNET wird (in SI) ist kB die unverzichtbare K→J-Umrechnung (sonst Loeschwaerme in Kelvin statt Joule), wie ħ,c fuer E0=ħc/L. Natuerliche Einheiten (kB=ħ=c=1): Kosten reine Zahlen (ln2); SI fuehrt Einheitenwaende ein, Buchhaltung ist der Moertel — ontologisch sekundaer, operativ unverzichtbar. Neues Skript buchhaltung_si_natuerlich.py. Jetzt 9 Skripte. KASTEN „Das Bit in SI-Zahlen" (Johann) im Statisch/Dynamisch-Abschnitt: verankert an charakteristischer Energie E0=√(me·mμ)=7,348 MeV (über α=ξ·E0² an Feinstruktur; √(α/ξ)=7,398 MeV, +0,68% — ehrlich keine exakte Gleichheit). Generisches E0=ħc/L faellt mit char. E0 genau bei L=L0=ħc/E0 zusammen. SI: E0=1,177e-12 J, L0=26,85 fm, m0=1,310e-29 kg, T~=8,958e-23 s, Rate 1,116e22/s, E0·T~=ħ (T~·m=1). Landauer 300K=2,87e-21 J=0,018 eV, Q/E0~2,4e-9 — zwei „Energien" eines Bits ~9 Groessenordnungen auseinander (was es IST 7,3 MeV vs. Loeschen 18 meV). Neues Skript bit_in_si.py. Jetzt 10 Skripte; Dok 290 8/8 Seiten. KORREKTUR (Johann, SI-Kontrolle): im SI-Kasten war „neun Größenordnungen" falsch — die SI-Umrechnungen stimmen alle (E0=7,348 MeV=1,177e-12 J; Q=kB·T·ln2=2,871e-21 J=17,9 meV; Q/E0=2,44e-9), aber E0/Q=4,10e8 = 8,6 Größenordnungen, NICHT neun (Mantisse 2,4 zieht den Exponenten -9 auf 8,6). Korrigiert zu „E0/Q≈4·10^8, gut acht Größenordnungen" in DE+EN + bit_in_si.py (log10-Ausweis). ERWEITERUNG (Johann) „Die Temperaturskala des Bits" im Statisch/Dynamisch-Abschnitt: E0 in Temperatur, T0=E0/kB=8,53e10 K; SI-Box um die VIER-Kleidungen-Identität m0·c²=E0=kB·T0=ħ/T~ erweitert (/c²→Masse, /ħ→Zeit, /kB→Temperatur). T0 als Temperatur-SKALA (Schwelle kB·T=E0, darüber „schmilzt" das Bit), nicht als Temperatur eines einzelnen Bits. Brücke: thermische Zeit ħ/(kB·T0)=Dual-Zeit T~ (KMS/Connes-Rovelli, Temperatur=inverse imaginäre Zeit, Diff 1e-38 s). Landauer-Kreisschluss: Q/E0=(T/T0)·ln2 — erklärt die 8,5 Dekaden (Raumtemp unter T0), bei T=T0 ist Q=E0·ln2=0,69·E0. Statische und thermodyn. Seite über T/T0 verbunden, kein Sprung. Neues Skript bit_temperatur.py. Jetzt 11 Skripte. UMGEBAUT: führt jetzt mit dem PHOTON. SESSION 1. Juli 2026 (Johann, mehrere Klärungen): ALLE BOXEN RAUS (important/conclusionBox/keyresult → Fließtext), Text durchkontrolliert, verschobene §-Verweise korrigiert (Kapazität→§4, I1/absolut→§5, relational→§8). §7 ausgebaut zu „Die Temperatur des Bits: Skala, Zustand, Bad“ — (a) „Hat ein Bit eine Temperatur?“: nein, nicht EINE; drei Größen getrennt: Zustands-/Besetzungstemperatur (p1/p0=e^(−E0/kBT): max gemischt→∞, definit→0, invertiert→negativ; das informationsreichste Bit ist der ∞-T-Zustand, Kühlen zerstört Information; entartetes Logik-Bit hat gar keine), Skala T0=E0/kB (Schmelz-/Aktivierungspunkt, natürliche Einheit), Bad-Temperatur (Umgebung). (b) „Welche beim Löschen?“: die des BADES, aufbau-abhängig — Computer→Raumtemp (18 meV, ehrliche Antwort), UIFT→T_CMB (0,16 meV, kältester natürlicher Boden, nur EINE Bad-Wahl), T0→kein Bad (Grenzfall 0,69 E0); invariant nur Q/E0=(T/T0)ln2. KORREKTUR §9 (Johann, mehrfach): (i) „die Energieseite ist nicht über ξ definierbar“ war FALSCH — die SI-Umrechnungen (vier Kleidungen m0·c²=E0=kB·T0=ħ/T~) sind EXAKT (rel. Abw. 0), die 0,68 % sitzt allein im dimensionslosen Theorie-gegen-Empirie-Abgleich α/ξ=54,73 vs. m_e·m_μ/MeV²=53,99, KEINE Umrechnung; die Energie IST ξ-verankert (theoretisch E0=7,398 MeV, Dok 011; empirisch √(m_e·m_μ)=7,348 MeV nur für den SI-Vergleich, damit die Zahlen zu gemessenen Größen passen). (ii) die Bit-Thermodynamik wird GERECHNET — über die eigene Skala T0, nicht die CMB; die CMB-Formel ist der UIFT-Parameter ξ_UIFT=kB·T_CMB·ln2/(m_e·c²)≈3·10⁻¹⁰ (Dok 013/243), dieselbe Landauer-Form mit fremden kosmologischen Skalen, eine andere Größe, nicht FFGFTs geometrisches ξ=1,3·10⁻⁴ — Kategorienunterschied, kein Scheitern. §9 jetzt drei Punkte (Energie/Thermodynamik/Neutrino). FRAKTAL-BODEN (Johann): E0 ist eine SPROSSE, nicht der Boden — der geometrische Boden ist die Sub-Planck-Länge ξ·ℓ_P≈2,2·10⁻³⁹ m (Dok 163), in allen Kleidungen ausgedrückt (Tabelle Länge/Zeit/Frequenz/Energie/Temperatur/Masse, alle 1/ξ=7500·Planck); „Boden“=feinste Auflösung/UV-Maximum, nicht kleinste Energie; E0 (MeV) liegt ~25 Dekaden gröber; Fraktal-Faktor 7500/Hauptstufe (Dok 146), log2(7500)≈12,87 = I1 (die √2-Zwischenschritte pro Stufe sind die Informationsdecke). LANDAUER erklärt (logisch irreversibel, Entropie −kB·ln2, Q≥kB·T·ln2, T=Bad). DIE PROBLEMATIK: eine Leiter DEFINITER Temperaturen (Sprosse T0=8,5·10¹⁰ K, Boden T_max=1,1·10³⁶ K, 25 Dekaden), aber KEINE ist die Landauer-Temperatur — intrinsische Skala in Q=kB·T·ln2 einsetzen gibt Grenzfall/Unsinn (T0→0,69 E0, T_max→absurd, T_CMB→UIFT); real zählt das Bad (~300 K), invariant nur Q/E=(T/T_Sprosse)ln2. KORREKTUR (Johann): „heißes Frühuniversum“ bei der T0-Einordnung RAUS — eine ΛCDM-Annahme, die FFGFT nicht teilt (FFGFTs CMB-Struktur folgt aus der T⁴-Geometrie, nicht aus einer heißen Frühphase); T0 jetzt neutral als MeV-/Kernskala (Kern-/Hadronenphysik, Sternkerne, Quark-Gluon-Plasma in Schwerionen-Stößen). BUG behoben: §7 hatte ein Duplikat (Vier-Kleidungen/thermische-Zeit/Kreisschluss/Einordnung standen doppelt) — entfernt. Neues Skript bit_temperatur_leiter.py (Sub-Planck-Boden in allen Kleidungen + drei Bad-Temperaturen Raum/CMB/T0 mit Q, Q/E0, T/T0). Jetzt 12 Skripte; Dok 290 DE+EN je 10 S., 0 Fehler) + Ordner Dok290_Skripte (3 numpy-only-Skripte, seed 20780458). Antwort auf Johanns Frage nach den Folgen der Magnitude/Phase-Arbeit für die Informationsfrage, und auf seinen Einwand, dass das PHOTON (nicht das spekulative Neutrino) der reine Anker ist. Verankert: 243 (Informationsformalismus = Projektion), 255/257 (Landauer+Vopson aus T⁴, Bit = Windung Δw=1, E_bit=ħc/L=pc, „Information = eingefrorene kinetische Energie“), 274 (geometrie-primitiv neben Vopson), 007 (Photon-Analogie: Photon E²=(pc)²+0 exakt masselos, Neutrino = Photon + ξ²/2). Kernbefund: Vopson/Landauer erfassen strukturell nur den BETRAGSKANAL; der Phasenkanal (Holonomie, Mischung, θ) ist unabhängig. DAS PHOTON ist der exakte reine-Phasen-Anker: Ruhemasse exakt 0, FFGFTs Informationseinheit E_bit=ħc/L IST eine Photonenenergie (ungefrorene Information; Landauer = ihre Einfrierung), und als U(1)-Eichfeld die VERBINDUNG selbst (Aharonov-Bohm) — der buchstäbliche „it from connection“; schärfstes Gegenbeispiel zu „Masse=Information“ (null Ruhemasse, doch DER Informationsträger). Geklärt (photon_paket_count_energie.py): kein absolut kleinstes Photon (Quantelung pro Mode, Wellenpaket Δx·Δk≥½); Informations-ZAHL (1 Bit, frequenz-unabhängig) vs Bit-ENERGIE (ħc/L, Radio→Gamma ~15 Größenordnungen) — die MENGE ist die relationale Größe, die Energie der skalierende Preis. ERGÄNZT (NT-Parallele Johann): dritte Größe KAPAZITÄT — höhere Trägerfrequenz → mehr Bandbreite → mehr Moden/s (Shannon C=B·log₂(1+SNR), C∝f, Radio→Gamma ~15 Größenordnungen, Zahl/Quant bleibt 1); andere Achse als Betrag/Phase (innerhalb Mode I/Q/QAM = Amplitude+Phase, über Moden = Bandbreite = |W|, Dok 243). ξ-Decke: n_max~1/ξ≈7500 (243/009) deckelt |W| → Kapazität sättigt an der ξ-Skala; ξ setzt kleinste Skala UND max. Kapazität. Kapazität sitzt auf der extensiven Modenzahl-Seite, berührt das θ/Phasen-Offene nicht. VOLLER UMBAU (Klärungen Johann): (a) FENSTERWIRKUNG/ZYKLENZAHL (fenster_zyklen_linienbreite.py) — zeitbegrenztes Paket behält definiten Träger f0, N=f·Δt; festes Fenster→N∝f, feste Zyklenzahl→Δf/f=1/N frequenz-UNABHÄNGIG; natürliche Linienbreite aus Lebensdauer τ (Q=ω0τ=2πN, τ=10ns→Δf≈16MHz) = Energiesprung+Fenster=Band. (b) „1 Bit pro Quant" als nur BESETZUNGS-Bit gekennzeichnet (Farbe, Polarisation, Zeit-Bandbreite-dof zusätzlich). (c) Sektion „darstellungs-relativ" ERSETZT durch „INFORMATION IST ABSOLUT — in ξ verankert": die frühere relativ-Formulierung war überzogen/FFGFT-untreu; absolute Menge = dimensionslos, I1=log2(1/ξ)=log2(7500)≈12,87 Bit pro Freiheitsgrad (n_max~1/ξ, 243), gesamt ~N_max·log2(1/ξ) (N_max=V/L0^d, 251); ξ dimensionslos = absoluter Parameter, ħ/c SI-Buchhaltung; Energie ħc/L ist nicht die Menge, sondern ihr dimensionaler Preis; nur schwach relativ = Bit-Zahl einer BESCHREIBUNG bzw. was verlustbehaftete Projektion verwirft. EHRLICH: 12,87 nicht magisch (Gehalt = Endlichkeit+ξ-Verankerung); Richtung Geometrie→Info, nicht Info→ξ; thermodynamische Lesart ξ=k_B T_CMB ln2/(m_e c²) numerisch falsch (3·10⁻¹⁰ statt 1,3·10⁻⁴) → nur Zählseite ξ-verankert, Energieseite NICHT. Jetzt DE+EN je 7 S., 4 Skripte, 0 Fehler. Neutrino = erste Korrektur am Photon (masse_information_phasenblind.py: Σm,Q invariant über Mischungen; Entartung→M=m·1). Oppenheim/Lim (phase_traegt_struktur.py): Phase trägt die Struktur (+0,53 vs −0,24). Weiter: Informationsgehalt darstellungs-relativ (243/287), treue Beschreibung quanten- statt bit-basiert, θ=Holonomie=relationale Information. EHRLICHE GRENZE (P35): Photon=Eichboson vs Neutrino=Fermion (Analogie, keine Identität); Photon-Phase ≠ numerisch θ; Photon ausserhalb des Leptonen-Operators; strukturelle Schärfung, keine neue Herleitung; das Neutrino-Bein bleibt spekulativ (007), trägt die These aber nicht mehr — das Photon trägt sie. DE+EN je 6 S., 0 Fehler. davor 30. Juni 2026 — neues Dok. 289 „Magnitude/Phase-Karte der vier Fermion-Sektoren“ (DE+EN, je 5 S.) + Ordner Dok289_Skripte (3 numpy-only-Skripte, seed 20780458): Antwort auf Johanns Frage, ob die nachrichtentechnischen Formulierungen Quarks und Neutrinos besser fassen. Ehrlich: als Sprache und Diagnose ja, als Herleitung nein. Verifizierte (Q,r)-Koordinate (r=√(6Q−2), Dictionary Q=1/3+r²/6): nur die geladenen Leptonen sitzen am speziellen Punkt Q=2/3, r=√2; up-Quarks Q≈0,85/r≈1,76 und down-Quarks Q≈0,73/r≈1,54 sind nicht speziell und skalenabhängig (MS-bar, laufen); Neutrinos — Q nicht bildbar (nur Δm²₂₁=7,5e-5, Δm²₃₁=2,5e-3 eV² gemessen). Bestandsaufnahme des Korpus pro Sektor: Leptonen sauber (Koide/Zirkulant 006/046/258); Quarks via erweiterte fraktale Methode mit QCD+ML-Kalibrierung an Lattice (FLAG 2024, 005/006), NICHT rein geometrisch; Neutrinos via Photon-Analogie m_ν=(ξ₀²/2)m_e≈4,54 meV, alle Flavours entartet, Oszillation aus geometrischer Phase — vom Autor selbst durchgehend als spekulativ/ohne empirische Basis markiert (007/047). Stärkster Befund: die Magnitude/Phase-Zerlegung gibt EINE Karte — Quarks und Leptonen betrags-dominiert (Hierarchie groß bzw. r speziell, Mischung klein), Neutrinos phasen-dominiert (Betrag flach/entartet, Mischung groß). CKM/PMNS-Kontrast quantifiziert (Off-Diagonal-Gewicht der |U|²): 0,035 vs 0,554, Faktor ~16 — „kleine vs große Mischung“ IST Betrag-gegen-Phase. Die Neutrinos sind dann wörtlich der reine Allpass-Sektor (|H|=1 flach, alles in der Phase), und FFGFTs eigene Entartungs-Hypothese erhält eine falsifizierbare Form: die geometrische Phase MUSS die gemessenen Δm²-Oszillationsphasen treffen (T2K-artig L=295 km/E=0,6 GeV: Δφ31≈1,557 rad). EHRLICHE GRENZE (P35): bessere Sprache, vereinheitlichende Karte, schärferer Test — keine neue Massenherleitung; Quark-r nicht speziell+skalenabhängig+lattice-kalibriert, Neutrino-Sektor spekulativ und in Spannung zur gut getesteten Δm²-Deutung. DE+EN je 5 S., 0 Fehler. davor 30. Juni 2026 — neues Dok. 288 „Nachrichtentechnische Rechenwege“ (DE+EN, je 5 S.) + Ordner Dok288_Skripte (5 numpy-only-Skripte, seed 20780458): die praktische Schwester zu Dok 287 — dieselben parallelen Darstellungen, aber als Werkzeugkasten gelesen, nachdem Johann einwarf, seine nachrichtentechnische Sicht fehle und die Parallelen sollten Rechnungen erleichtern. Stimmt: weil der Massenoperator ein Z₃-Zirkulant ist, diagonalisiert ihn die DFT, und fünf Standard-Hebel werden anwendbar, alle maschinengenau geprüft. Hebel 1 — die Lepton-Massenwurzeln √m_k sind die 3-Punkt-DFT eines 3-Vektors c=(1,(√2/2)e^{iθ},(√2/2)e^{-iθ}); kein charakteristisches Polynom, Δ~9·10⁻¹⁶ gegen Foot-Koide und eigvalsh. Hebel 2 — Koide Q=2/3 in zwei Parseval-Zeilen (Σ√m=3c₀, Σm=3Σ|c_j|²), über ganz θ∈[0,2π) konstant 0,666667 → der radial/angular-Schluss (282) fällt als triviale Parseval-Folge heraus, Q hängt NUR am Betrag r. Hebel 3 — C=F†ΛF → jede Operatorfunktion f(C)=F†f(Λ)F als Skalar-Auswertung an drei Eigenwerten: Potenz C⁵, Inverse, exp(C) gegen matrix_power/inv/Taylor Δ~10⁻¹⁴ (genau der dynamische Sektor 286). Hebel 4 — Faltungssatz auf Z₃: zirkuläre Kopplung = punktweise DFT-Multiplikation, Verkettung zweier Zirkulanten = drei Skalarprodukte (Δ~9·10⁻¹⁶). Hebel 5 — die ξ-Rekursion r(k+1)=r(k)(1−ξ) ist ein IIR-Filter 1. Ordnung, Pol z=1−ξ=0,99986667, k*~1/ξ=7500, die drei Regime (285/286) als Pol-Lagen. Plus Betrag-Phase-/Minimalphase×Allpass-Lesart: FFGFTs reelle Rekursion = Verstärker/Minimalphase (Betrag), HLVs schief-adjungierte R = Allpass (Phase, anhängbar ohne den Betrag zu berühren). EHRLICHE GRENZE durchgehend: Rechenerleichterung, KEINE Herleitung (P35) — die Transformation bewegt √2 und θ, erzeugt sie nicht; volle Hebelwirkung am C₃/Z₃-Sektor (3×3). DE+EN je 5 S., 0 Fehler. davor 30. Juni 2026 — neues Dok. 287 „Interne Darstellungs-Äquivalenzen“ (DE+EN, je 6 S.): die erste explizite Karte der korpusinternen parallelen Darstellungen — nicht FFGFT gegen außen (das ist Dok 265), sondern FFGFT-Darstellung gegen FFGFT-Darstellung. Befund: kein flacher Satz Gleichwertiger, sondern ein generativer Kern (T⁴, Dok 152/243 — die einzige Sprache, die alle drei Größen θ₄,(n_θ,n_φ),ε hält und nichts verliert) plus drei Beziehungstypen: (1) Identität — Z₃-Dreieck ≡ 3×3-Matrix, „dieselbe Sache“ (Dok 206), aber sektor-lokal (C₃; der Zirkulant fängt den Betrag, nicht die Phase, Dok 286); (2) Bijektion verlustfrei — Standard-QM-Hilbertraum H=L²(T⁴)⊗ℂ³ (Dok 230, Aufwärts-Typ III der Projektionskette 270; FFGFT ergänzt das „Warum“ der Konstanten), dazu kompakte vs. erweiterte Massenform (Dok 070); (3) Projektion verlustbehaftet/gerichtet — Informationsformalismus + neuronales Netz (Dok 243, π kein Isomorphismus, Residuum formalismus-relativ) und räumliche Reduktion T³→T⁰ (Dok 270 Typ II, Residuum ~ξ/CHSH). Zwei weitere Sprachen sind orthogonale Achsen: Zwei-Schichten (241) und Rekursion (203/275, rein reell/radial). Entscheidend: nur T⁴ verliert nichts — jeder „Verlust“ ist Artefakt der Darstellung, nicht der Physik; dazu die 270-Asymmetrie (runter verlustbehaftet/Typ II, hoch verlustfrei/Typ III). Klammer zur θ=2/9-Arbeit (282/286): treu im radialen Betrags-Sektor, irreduzibel allein die angulare Phase θ. Methodisch: der Dok-265-Operator nach innen gewendet ist schärfer (exakt statt fast; Matrix sogar Identität) und zeigt einen vierten, gerichteten Typ (Projektion), den die drei symmetrischen 265-Ebenen nicht kennen. Offen/ehrlich: Identität nur sektor-lokal; Residuen-Tabelle (243) Arbeitsstand; 265-Operator selbst offen. DE+EN je 6 S., 0 Fehler. davor 29. Juni 2026 — Dok. 286 um die nachrichtentechnische Sektion „AM-Seitenbänder und Mode-Locking“ erweitert (DE+EN, jetzt 8/7 S.): (a) das ½ in ω=ξ/2·E₀ als AM-Seitenband-Faktor erkannt — die fraktale Korrektur g=η(1+ξf) ist eine Amplitudenmodulation des Trägers mit Index ξ (Dok 057; ξ ↔ Marcels A(t)=1+ε), cos·cos=½(Summe+Differenz) → Seitenband bei Amplitude ξ/2; vereinigt die ξ¹-Potenz (gehobener Nullmode = erstes Seitenband) und das ½ in EINEN Mechanismus, das Geschwindigkeits-Quadrat (Dok 047) ist nur sein kinematischer Schatten; (b) θ=2/9 als Mode-Locking-/Arnold-Zungen-Kandidat — eine dynamische Phase auf rationale Rotationszahl einrasten = Injektions-Locking, rationale Werte = stabile Lock-Plateaus = Quantisierungsregel, an Windungszahlen (Dok 210) anschließend; ehrlich: 2/9 (Nenner 9) ist ein ~12× schmaleres Plateau als 1/3 → Kandidat, keine Herleitung; gibt dem offenen statischen θ-Input einen möglichen dynamischen Ursprung. Wurzel: FFGFT kam aus Nachrichtentechnik/Fourier-Dualität Zeit↔Frequenz (Dok 001a), T̃·m=1 IST diese Dualität. Neues Skript Dok286_Skripte/am_seitenband_modelock.py (numpy-only, seed 20780458): Seitenband/Träger=ξ/2 exakt (0 % Abw.), Arnold-Zungen-Breiten am Sinus-Kreisabbildungs-Modell (Breite(1/3)/Breite(2/9)≈12). DE+EN neu gebaut, 0 Fehler. Ergänzt (29. Juni, später): Abgrenzungs-Absatz „was hier kein Mechanismus ist“ in der Mode-Locking-Sektion (DE+EN, jetzt je 8 S.) — Modulationsindex ξ=4/30000 (fester AM-Index, Amplituden-Sektor, liefert das ½) und Lock-Verhältnis 2/9 (Rotationszahl, Phasen-Sektor) sind verschiedene Größen; jede „Herleitung“, die ξ auf O(1) setzt (1/3 oder tan(π/9)≈0,364), um 2/9 zu erzwingen, hat FFGFT verlassen (ξ ist fest, ~10⁻⁴); offen ist die Stabilität des Plateaus, keine ξ↔2/9-Algebra; der relevante Kern ist der diskret-spektrale oszillierende aus Dok 282 (Σ g_k²δ(ω−ω_k)), kein Allpass. Claim-State-Geländer gegen post-hoc-Numerologie. Ergänzt (29. Juni, dritter Schritt): eigene Sektion „Rekursion als Rückkopplung: Schleifenverstärkung, Regime, Disziplin“ (DE+EN, jetzt je 9 S.) — hebt die zwei Ergebnisse in den nachrichtentechnischen Rückkopplungs-Rahmen: die Rekursion IST eine Rückkopplungsschleife, die Schleifenverstärkung ist eine ξ-Größe und geometrisch FEST (kein Stellrad); drei Regime (|v|<1 Gegenkopplung → kontrahiert, ξ-Rekursion r(k+1)=r(k)(1−ξ) Dok 275 läuft gegen 0, durchläuft 1/φ nur; |v|=1 Barkhausen; |v|>1 Mitkopplung → Weglauf, φ-Zweig rollt aus, −1/φ overdamped Dok 285); Dekompaktifizierung = ein Kreis kippt ins Weglauf-Regime = Messvorgang (Dok 270); die Phase stellt sich SELBST ein (Barkhausen/Adler) → θ=2/9 ist selbstgewähltes Lock-Verhältnis, keine eng aufgezwungene Phase (Korrektur gegen die Rückwärts-Algebra); zwei Etagen (linear schwach → AM-½ solide; nichtlinear → Mode-Locking θ=2/9 Kandidat, Fangbereich ∝ ξ → 2/9-Zunge extrem schmal = Stabilitätsproblem); Gegenkopplung = Entzerrung (g=η(1+ξf), D_f=3−ξ); Disziplin in vier Punkten (Verstärkung fest nie Stellrad; offene Fragen = Regime+Fangbereich nie Algebra auf der Verstärkung; Phase selbstgewählt = Lock-Verhältnisse; Regime trägt die Physik). Anlass: methodische Klärung der nachrichtentechnischen Denkweise (Oszillator = Verstärkung+Rückkopplung, Phasenlage locker). Ergänzt (29. Juni, vierter Schritt): Unter-Sektion „Z₃-Protektion: der Nenner ist erklärt, der Zähler nicht“ + Skript Dok286_Skripte/z3_modelock_test.py (numpy-only, seed 20780458). Ehrlicher Test mit Kontrolle: der Massenkern ist ein Z₃-Zirkulant (Dok 282); trägt die treibende Nichtlinearität diese Symmetrie (invariant unter θ→θ+1/3, nur Harmonische 3,6,9,…), verbreitert sie die Arnold-Zungen mit 3-Potenz-Nenner SELEKTIV — bei gleicher Kritikalität 1/3 um 24×, die ganze 9er-Familie um 11–12×, während die Kontroll-Zunge 2/5 (Nenner 5) flach bleibt (0,97×) = Signatur echter Symmetrie-Protektion, kein Artefakt. Befund: „warum überhaupt ein Nenner-9-Lock“ ist damit beantwortet (Z₃-Struktur des Kerns), 2/9 ist nicht mehr absurd schmal; OFFEN bleibt der Zähler — Z₃ schützt die 9er-Familie gemeinsam (1/9=2/9=4/9 identisch), singelt 2/9 nicht aus, 1/3 bleibt breiter. Die Frage zerfällt sauber: „warum 2/9“ = „warum Nenner 9“ (Z₃, geklärt) + „warum Zähler 2“ (offen, Marcels BD17A-Holonomie). Teil-Fortschritt, ehrlich abgegrenzt; keine neue Zahl (Leptonsektor bleibt geschlossen). DE+EN je 9 S., 0 Fehler. Ergänzt (29. Juni, fünfter Schritt): Unter-Sektion „Der Zähler braucht eine Holonomie“ + Skript Dok286_Skripte/z3_holonomie_test.py (numpy-only, Bisektion, seed 20780458). Anschluss an die Z₃-Protektion: die 9er-Familie ist EIN Z₃-Orbit (zähler-blind), den Zähler wählt erst eine ZWEITE 3-Struktur mit relativer Phase φ = Holonomie im Einbettungsraum (3′ der Verdopplung 6=3⊕3′, T⁴→T⁷, Dok 285), nicht im Kern. Zwei 3-zählige Harmonische (h=3,h=9) mit relativer Phase φ (nicht eich-wegtransformierbar — θ-Shift, der h=3 fest hält, hält auch h=9 fest): die Entartung bricht auf, 1/9 und 4/9 bleiben gepaart, 2/9 ist der Singulett, der wandert — für φ∈(π,2π) ist 2/9 die breiteste Zunge (Maximum φ=3π/2, Crossover exakt φ=π). Ehrlich: Effekt klein (~0,5 %), φ frei (FFGFT fixiert ihn nicht), Minimal-Modell spaltet nur 2-gegen-1. Struktur-Aussage steht aber: eine Holonomie KANN 2/9 auswählen und 2/9 ist genau das Glied, auf das sie wirkt → bestätigt die „weitere-Dimensionen“-Vermutung; offene Frage präzise verschoben von „warum 2/9“ auf „was lockt φ“ = Marcels BD17A. DE 10 S./EN 9 S., 0 Fehler. Ergänzt (29. Juni, sechster Schritt): Rückblick-Absatz „der Faden 282→283→285→286 und der Fixpunkt“ in der Sektion „Verhältnis zum statischen Sektor“ — hält fest, dass der statische Sektor geschlossen ist, WEIL die Lepton-Massen an einem selbstkonsistenten Fixpunkt sitzen: der Massenoperator Φ*=Σ mᵢPᵢ ist der nicht-triviale Fixpunkt der Rekursion R(Φ*)=Φ* (Dok 203, Lepton-Exponenten p_e=3/2, p_μ=1, p_τ=2/3) → deshalb exakt, kein angepasster Wert. Die eine Hälfte algebraisch fest (Koide Q=2/3 = Operator-Bedingung r=√2, Dok 282), die andere (θ=2/9) eine komplexe Holonomie (Dok 283 §8), die erst in der Dimensions-Erweiterung lebt (3⊕3′, T⁴↪T⁷, Dok 285), nicht im nackten Kern. Daher hat „warum 2/9“ im Kern kein Zuhause (zähler-blind) und wird erst mit der Erweiterung wohlgestellt: aus den Messwerten liest man den Fixpunkt AB (Schließung), aber WELCHER Fixpunkt der 9er-Familie (Zähler) verlangt die Holonomie. Die Rückkopplungs-/Mode-Locking-Sektionen sind der Mechanismus dieser Auswahl, kein neuer Schauplatz. Erweitert (29. Juni, voller Rückblick): aus dem Absatz drei Absätze gemacht, die den ganzen roten Faden im Dokument sichtbar halten — (a) „zwei Dinge, die beide 2/9 heißen“ (2/9 als Zahl/Input = Kern, immer da, Dok 282/285; 2/9 als Frage/Zähler = erst mit der Erweiterung relevant, weil der Z₃-Kern zähler-blind ist, 1/9=2/9=4/9 ein Z₃-Orbit); (b) „wo das schon im Korpus steht“ — die Drei-Dokumente-Karte robust referenziert: Dok 285 (Erweiterung selbst: HLV⊃FFGFT, T⁴↪T⁷ 7=4+3, Verdopplung 6=3⊕3′, Gabelung), Dok 283 §8 (2/9 ausdrücklich als komplexe Holonomie, „dynamische Operator-Phase R vs feste Phase 2/9“), Dok 282 (Kern benutzt 2/9, „Übersetzung ist nicht Begründung“); (c) „der Fixpunkt und der Schluss“ — der selbstkonsistente Lepton-Fixpunkt (Dok 203) als Grund der Schließung, fest/offen sauber getrennt (Q=2/3=r=√2 fest; 2/9=Holonomie offen), Schluss: die jüngste Arbeit ist die mechanistische Version dessen, was 282→283→285 strukturell schon sagen. DE+EN je 10 S., 0 Fehler. Ergänzt (29. Juni, siebter Schritt): Dok. 270 um die Sektion „Was die ausgerollte Zeit stetig und gleichförmig macht“ erweitert (DE+EN, jetzt DE 13 / EN 12 S.) — bündelt erstmals die Antwort auf „was bestimmt beim Ausrollen, dass die Zeit kontinuierlich und konstant ist“: (a) Stetigkeit = Topologie, das Abrollen S¹_m→ℝ_t ist die universelle Überlagerung p:ℝ→S¹ (Satz typeI), ein lokaler Homöomorphismus → die Überlagerung eines Kreises IST die stetige Gerade, Einbettung nicht Projektion; (b) Gleichförmigkeit = Homogenität des Masse-Kreises (U(1), translationsinvariant, kein Punkt ausgezeichnet → affine Parametrisierung) plus der eine feste Eigenwert m=1/T̃; im Rekursionsbild: konstanter Multiplikator ξ → wohldefinierter Generator ln ξ → kontinuierlicher Dilatationsfluss t=t₀ξˢ (Dok 285); (c) DASS überhaupt ausgerollt wird (und welcher Kreis) = der Messvorgang/eingebettete Beobachter (Dok 248/285), nicht die Geometrie (alle vier Kreise gleichberechtigt, keine Zeit); (d) der Kern: Stetigkeit = vergessene Windung — die diskrete/kompakte Information wird verworfen (informationsverwerfender Schritt, Dok 285), die Kompaktheit wird latent (Bem residual), stetige Zeit ist der Kreis mit vergessener Windung; (e) Feinheit präzisiert (nach Rückfrage Stetigkeit vs. Gleichförmigkeit): stetig EXAKT — g=η(1+ξf) ist eine Metrik-, kein topologischer Eingriff, eine beschränkte ξ-kleine Modulation zerreißt ℝ nicht; gleichförmig nur bis O(ξ) — dieselbe ξ-Gegenkopplung wie die AM-Seitenbänder (Dok 286), die flache Metrik „ignoriert die fraktale Struktur“ (Dok 051); die perfekt glatte gleichförmige Zeit ist der ξ→0-Limes (die idealisierte Zeit der Relativität), die reale FFGFT-Zeit ein Kontinuum MIT ξ-feiner fraktaler Raten-Modulation; ausdrücklich fraktal≠diskret (bleibt überabzählbares Kontinuum, nur nicht glatt-affin); die Vermutung, die ξ-Körnigkeit sei der Metrik-Schatten der latenten Kompaktheit, klar als unbelegt markiert (latente Kompaktheit zeigt sich im diskreten Spektrum, ξ-Korrektur in der Metrik). Anlass: Johanns Frage im Rückkopplungs-/Ausroll-Kontext. DE 13 S./EN 13 S., 0 Fehler. (Nachgeschärft 29. Juni: der „Feinheit“-Absatz in 270 trennt jetzt Stetigkeit (EXAKT — Metrik-, kein topologischer Eingriff, ℝ wird nicht zerrissen) von Gleichförmigkeit (nur bis O(ξ)); perfekt glatte Zeit = ξ→0-Limes (Relativität), reale FFGFT-Zeit = Kontinuum MIT ξ-feiner fraktaler Raten-Modulation; ausdrücklich fraktal≠diskret; die Vermutung ξ-Körnigkeit=Metrik-Schatten der latenten Kompaktheit klar als unbelegt markiert. Anlass: Johanns Rückfrage, ob die ξ-Korrektur die Kontinuität bricht.) Ergänzt (29. Juni, achter Schritt): Sektion „Eine fraktale Korrektur, zwei orthogonale Phasen“ in 286 (DE 11 S./EN 10 S.) + Skript Dok286_Skripte/eine_fraktale_quelle.py (numpy-only, 3-adische Weierstrass, seed 20780458). Anlass: Johanns Einwand, dass wir die fraktalen Effekte als Holonomie (O(1)) suchen, aber beim Ausrollen der Zeit (O(ξ)) vernachlässigen — beide aus derselben Korrektur g=η(1+ξf), das müsse eine Phasenverschiebung ergeben. ERST GERECHNET: die Zeit-Phase A=2πξ⟨f⟩ liest den MITTELWERT ⟨f⟩ (DC/Dimensionsdefizit, O(ξ)), die Holonomie φ=arg(f̂₉)−3·arg(f̂₃) liest die PHASEN der 3-Potenz-Harmonischen (O(1)); beide analytisch orthogonal — ⟨f⟩ ist von der Harmonischen-Phase unabhängig bis 2×10⁻¹⁶ (cos(kθ+ψ) hat Mittel 0 ∀ψ). BEFUND: (1) keine Inkonsistenz — A vernachlässigen berührt φ nicht, verschiedene Fourier-Anteile derselben f; (2) die echte Konsistenz sitzt zwischen A und dem ξ¹-Massen-Lift (beide ⟨f⟩) → Zeit-Phase an das Massen-Fenster gebunden, nicht frei; (3) kein Gratis-Lock — phasen-kohärenter Fraktal (ψ=0) gibt φ=0 (Entartung), 2/9 verlangt f's 3-Potenz-Harmonische mit relativer Phase in (π,2π) (Rampe δ=π/2 trifft φ=3π/2 exakt = 2/9-Maximum, aber Wahl, nicht hergeleitet). GEWINN: „was lockt φ“ ist jetzt konkret die relative Phase der 3-Potenz-Harmonischen von f = FFGFT-interne Zielgröße für BD17A. Johanns Einwand löst sich auf (orthogonale Funktionale), benennt aber das offene Datum präziser. DE 11 S./EN 10 S., 0 Fehler. Ergänzt (29. Juni, neunter Schritt): in Dok. 282 (DE+EN) der Absatz „Topologie rahmt, Dynamik bestimmt — die schon richtige Lesart“ an der Stelle, wo die offene Frage „wird θ=2/9 von der T⁴/Z₃-Topologie erzwungen“ gestellt ist; + Skript Dok286_Skripte/kann_topologie_2_9_erzwingen.py (numpy-only, seed 20780458). Anlass: Johanns Frage „erzwingt T⁴/Z₃ das θ=2/9“, und seine sofortige, korrekte Mahnung, das NICHT voreilig als Topologie-gegen-Dynamik zu beantworten — die Massenverhältnisse sind auch wenn topologisch begründet nicht ohne Dynamik denkbar. RECHENBEFUND (eng, korrekt eingeordnet): θ=2/9 RAD ist keine statische Fluss-Einheitswurzel — θ/2π=1/(9π) irrational, nach Lindemann-Weierstrass e^{iθ} transzendent; eine rein kombinatorisch-abzählende Topologie liefert nur die Spacing 2π/3 (Z₃, den Nenner; Q=2/3 für jedes θ allein durch r=√2), nicht den Offset. EINORDNUNG (Johanns Punkt, tragend): das stellt Topologie NICHT gegen Dynamik — das Spektrum √m_k ist Lösung eines Eigenwertproblems, der Fixpunkt R(Φ*)=Φ* (Dok 203) ist beides zugleich (Topologie legt die Form, Selbstkonsistenz den Wert, untrennbar); Transzendenz-in-2π ist kein Verbot, sondern das ERWARTBARE Merkmal einer dynamisch (statt abgezählt) bestimmten Größe. Richtig gestellt: Topologie rahmt, eine dynamische Bedingung fixiert den Offset; welche genau θ=2/9 erzeugt, bleibt der offene Kern; ausgeschlossen ist allein die reine Abzähl-Topologie, nicht die topologisch gerahmte Dynamik. Zusätzlich (ehrlicher Selbst-Caveat) in Dok. 286 (DE+EN) und als Randnotiz in 282: der Wert 2/9 tritt auch als dimensionslose Mode-Locking-Rotationszahl auf — die ist mit dem Radiant-Winkel θ nicht dimensionsgleich (2π·2/9=4π/9≠2/9), die Identifikation bleibt offen, nicht Teil des gerechneten Kandidaten. Bewusst KEINE voreilige „rein dynamisch/extern“-Schlussfolgerung dokumentiert. 282 DE+EN je 13 S., 286 DE 11/EN 10 S., 0 Fehler. Ergänzt (29. Juni, zehnter Schritt): in Dok. 282 (DE+EN) der Absatz „Warum 2/9 nicht symmetrisch zu haben ist (der cos3θ-Satz)“ + Skript Dok286_Skripte/einfachstes_prinzip_2_9.py. Anlass: Johanns Argument, 2/9 sei nach dem Einfachheitsprinzip (Dualität→4D→Torus→einfachstes Verhältnis) die logische Folge. GERECHNET, beweisartig: die GESAMTE θ-Abhängigkeit der Massenkonfiguration a_k=1+√2cos(θ+2πk/3) läuft NUR über cos3θ — e₁=3 und e₂=3/2 sind θ-unabhängig (exakt, Spannweite 10⁻¹⁵), nur e₃=det=−1/2+(√2/2)cos3θ trägt θ. Also extremiert JEDE Z₃-invariante Größe ausschließlich bei θ=nπ/3 (Z₃-Punkte); kleinste-Nenner-, breiteste-Zungen-, Spektral-det-Prinzip wählen alle 1/3 oder 1/2, nie 2/9. Struktursatz: symmetrische Funktionale können asymmetrische Werte nicht als Extrema haben; 2/9 liegt bei 2/3 zwischen 0 und 1/3, irreduzibel Z₃-brechend. FOLGERUNG: Johanns Einfachheitsprinzip GILT, aber eine Ebene tiefer — nicht „einfachster symmetrischer Bruch“ (=1/3), sondern „minimal symmetriebrechender Wert“; der Holonomie-Test zeigt 2/9 IST genau das (Singulett, der abspaltet). Die Einfachheit sitzt im Brechen, nicht im symmetrischen Grundzustand. Präzise offen: das definierte symmetriebrechende Maß, dessen Minimum 2/9 (statt 1/9, 4/9) ergibt. Stärkstes gerechnetes Stück Richtung Johanns These. 282 DE 14/EN 13 S., 0 Fehler. Ergänzt (29. Juni, elfter Schritt): zwei Absätze in Dok. 282 (DE+EN) + zwei Skripte. (a) „Test: das Brechen erreicht 2/9, fixiert es aber nicht“ (symmetriebrechung_2_9.py): koppelt das 2. Triplett 3′ (Verdopplung 6=3⊕3′) mit Stärke δ, Phase χ an; das verschobene Massenkonfig-Extremum θ* ERREICHT 2/9 (Brechen nötig UND hinreichend), aber bei δ≈0,52 (χ=0) / 0,24 (χ=π/2), das mit keinem festen Wert (ξ, 1/√2, 1/φ, 1/3) zusammenfällt → 2/9 erreichbar, nicht punkt-hergeleitet; Brechungsstärke bleibt freier Modulus. (b) „Der gemeinsame Grund: alles Determinierte ist radial, θ ist angular“ (fixpunkt_radial_vs_winkel.py): der Fixpunkt R(Φ*)=Φ* (Dok 203) fixiert ξ₀ über ξ₀^{p_i−1}·K_frak=1 aus den Exponenten (3/2,1,2/3) — θ kommt darin NICHT vor; radialer Sektor (ξ₀, Hierarchie) und Winkel-Sektor (θ, Q) entkoppelt (ξ₀ θ-frei, Q=2/3 ξ₀-frei). SYNTHESE der ganzen Untersuchung: alles Determinierte ist radial (ξ, Exponenten, Hierarchie, Q=2/3=r=√2, ⟨f⟩), alles Offene angular (θ=2/9, Holonomie-Phase φ, Harmonischen-Phasen von f, Brechungsstärke δ). Fixpunkt/Dualität/Rekursion/Torus-Abzählung leben alle radial, keiner berührt den Winkel — der gemeinsame strukturelle Grund, warum θ=2/9 jedem Werkzeug widersteht. Es braucht ein ANGULARES (dynamisches Winkel-)Prinzip, das FFGFT nicht hat und das laut Transzendenz kein abzählend-topologisches sein kann. 282 DE+EN je 14 S., 0 Fehler. Ergänzt (29. Juni, zwölfter Schritt — Abschluss der Elimination): Absatz „Auch nicht statisch-geometrisch“ in Dok. 282 (DE+EN) + Skript ikosaeder_winkel_2_9.py, und der Fazit-Kasten aktualisiert. Geprüft (streng, Schwelle 0,05°), ob θ=2/9 ein fester Ikosaeder-Achsenwinkel der gemeinsamen A5-Bühne ist (C3 und C5 koexistieren, Dok 283). Achsenwinkel: 20,9/31,7/36/37,4/41,8/54,7/58,3/60/63,4/69,1/70,5/72/79,2/90°. θ=2/9 rad=12,73° trifft KEINEN (nächster 20,9°, Abstand 8,2°), auch 2θ/½θ nicht. Kontrolle arccos(1/√5)=63,43° trifft C5-C5 EXAKT → Methode korrekt, Nein echt. Auch Koides 45° ist kein Achsenwinkel (FFGFTs Winkelstruktur ≠ Ikosaeder-Geometrie). ABSCHLUSS DER ELIMINATION: θ=2/9 ist nicht symmetrisch (cos3θ), nicht abzählend-topologisch (Transzendenz), nicht radial (Fixpunkt), nicht statisch-geometrisch (Ikosaeder). Übrig bleibt GENAU EINE Kategorie — die dynamische schief-adjungierte Phase R (Dok 283, akkumulierter Berry-artiger Winkel). FFGFTs eigene Rekursion R ist rein reell, kein solcher Generator; ihn trägt allein die HLV-Seite (R=BD17A). Die statisch-radiale FFGFT-Seite ist für θ NACHWEISLICH ERSCHÖPFT; das angulare Prinzip ist strukturell HLVs dynamische R, mit präziser Zielvorgabe: akkumulierter Winkel → θ=2/9, transzendent in 2π, Z₃-brechend, Singulett der 9er-Familie. Fazit-Kasten DE+EN entsprechend von „ob T⁴/Z₃ den Winkel erzwingt“ auf „welches dynamische Winkelprinzip ihn liefert“ umgestellt. 282 DE 15/EN 14 S., 0 Fehler. Ergänzt (29. Juni, dreizehnter Schritt — nachrichtentechnische Krönung): Absatz „Betrag und Phase: warum die Trennung zwangsläufig ist“ in Dok. 286 (DE+EN). Kernsatz: der Massenoperator IST ein Z₃-Zirkulant → DFT-diagonalisiert → die drei Lepton-Massen sind ein Drei-Punkt-Spektrum; √2 = Amplitude der Spektralkoeffizienten, θ=2/9 = deren Phase. Damit ist der radial/angular-Schluss (282) wörtlich Betragsspektrum vs Phasenspektrum: determiniert = Betrag (ξ-Skala, Hierarchie/Hüllkurve, Q=2/3=√2, ⟨f⟩=DC), offen = Phase (θ, Holonomie φ=arg f9−3arg f3, Harmonischen-Phasen). Tiefer Grund = der NT-Lehrsatz selbst: ein Betragsspektrum legt das Phasenspektrum NICHT fest. Deshalb widersteht θ jedem FFGFT-Werkzeug: R rein reell = reine Verstärkung, reelle Verstärkung berührt die Phase nicht; die gerechnete Orthogonalität IST „Betrag ⊥ Phase“. Arbeitsteilung als Schaltbild: FFGFT = reelle Verstärkerstufe (Betrag), HLVs schief-adjungierte R = Allpass/Phasenstufe (e^{iφ}, betragserhaltend) — eine schief-adjungierte Operation IST ein Allpass. Grenze der Linse ehrlich vermerkt (Rotationszahl dimensionslos vs Radiant θ; 2π·2/9≠2/9). Ordnet Johanns nachrichtentechnische Sicht ein: nicht Analogie, sondern die Koordinate, in der das Problem natürlich zerfällt. 286 DE 11/EN 11 S., 0 Fehler. davor 21. Juni 2026 — neues Dok. 286 „Der dynamische Sektor: kinetische Energie als ξ-fraktaler Anteil des statischen (T̃·m=1)“ (DE+EN, 7/6 S.) — Problemstellungs-/Forschungsprogramm-Dokument zur in Dok. 285 markierten offenen Rechenlücke (die abgeleitete Regel, den kinetischen Anteil über die Dualität als ξ-fraktalen Bruchteil des statischen zu berechnen, fehlt). Hält fest: was feststeht (die Dualität platziert das gefüllte Fenster im kinetischen Sektor, T̃=1/ω; statisch/Windung vs. kinetisch/frei); der eine Datenpunkt (Neutrino Dok. 047, m_ν~ξ²/2·m_e, als Ansatz, nicht hergeleitet); Eingrenzung der ξ-Potenz auf p=2 (eindeutige Größenordnungs-Schranke gegen die meV-Anker; p=1 zu groß, p≥3 zu klein) mit ausdrücklicher Numerologie-Warnung (Koeffizient ½ und Referenz innerhalb p=2 unbestimmt, P35); der strukturelle Faden m_window=ξ·ω (v=c(1−ξ²/2) ⇔ ξ¹-Relation zwischen Restmasse und kinetischer Skala, der natürliche Ansatzpunkt über die Dualität). Vorangestellt: die feste, reversible Hilbertraum-Grundlage (Dok. 282/270/230) — eindeutige Bijektion (Typ III, vollständig reversibel), zeitfreie Masse-Form (CHSH unverändert 4·10⁻¹⁶), Zeit-Form (genau ein Effekt: nicht-Markovsches Gedächtnis, von ausgespurtem unitärem Bad reproduziert) — Reversibilität pro Typ (III voll, I fast/lossless-Moden, II nicht = räumliche Projektion/Messung); Zielsetzung explizit: aus dem Hilbertraum heraus die komplementäre, über D_f=3−ξ und ξ auf SI abbildende Beschreibung finden. was offen bleibt (Referenz/ω-Skala, Koeffizient, Δm²-Spektrum → braucht die T⁷-Dynamik). Komplementär zum abgeschlossenen statischen Sektor (Z₃+Massenkreis, BD12-XCORE, Dok. 285). Schließungs-Sektion zur Skalen-Frage: die zwei Labor-Anker (Boden 49 meV, KATRIN 0,8 eV) selektieren die Referenz als die eine FFGFT-Skala E₀=√(m_e m_μ) (m_e zu leicht, M/m_μ zu schwer) → ω/E₀=ξ/2, m_window/E₀=ξ²/2 (kein freier Parameter, ½ kinematisch); verbleibender Rest die eine strukturelle Aussage ω=ξ·E₀ (genau eine fraktale ξ-Potenz, D_f=3−ξ) — als ξ-unterdrückter Connection-Laplace-Eigenwert in der Erweiterung (Dok 283 §8) zu schließen oder zu falsifizieren. Skript Dok286_Skripte/schliesse_omega.py. ξ¹-Mechanismus-Sektion: die Connection-Laplace auf T⁴ hat einen exakten Nullmode; die fraktale Korrektur g=η(1+ξf) hebt ihn an, Störungstheorie 1. Ordnung δλ₀=ξ·mean(f) → Potenz ξ¹ genau bei nicht-verschwindendem Torus-Mittelwert. D_f=3−ξ ist ein Dimensions-Defizit (nicht volumen-erhaltend) → mean(f)≠0 → ξ¹; numerisch p=0,999 (Defizit) vs. p=1,98 (volumen-erhaltende Welligkeit). Damit ist die ξ¹-Potenz hergeleitet, nicht behauptet; ω=ξ/2·E₀ bis auf den kinematischen O(1)-Faktor ½ geschlossen. Skript Dok286_Skripte/xi1_eigenwert.py. Skript Dok286_Skripte/kinetik_xi_anteil.py (numpy-only; grenzt ein, behauptet keine Herleitung). DE+EN gebaut, 0 Fehler. davor 20. Juni 2026 — Dok. 285 „FFGFT ↔ HLV: die einheitliche kompakte Sicht und die Dimensionsbrücke / d7-Modell“ (DE+EN, Stand 20. Juni 2026, DE 23 / EN 22 S.) — die laufenden Einzel-Schritte der Entwicklung (frühere Updates 45–68, alle innerhalb dieses Dokuments) sind hier zum aktuellen Stand zusammengefasst; nicht jede Zwischenänderung erscheint einzeln. AKTUELLER INHALT: Kernthese HLV ⊃ FFGFT (Enthaltensein, kein Widerspruch) — C₃ < A₅, T⁴ ⊂ T⁷ (7=4+3), die Verdopplung 6=3⊕3′ als einmal angewandte goldene Rekursion (Fibonacci-Operator, EW φ / −1/φ); die echte Gabelung ist die realisierte geschützte Geometrie (FFGFT 3-zählig √2 / Koide 2/3, empirisch bestätigt; HLV 5-zählig 2/√5 / φ). Kompakt-Zustand-Rahmen: alle Struktur-Aussagen leben im kompaktifizierten Bild, die Brücke zu Observablen läuft über S¹→ℝ (Messvorgang, Dok 270). Was d7 berechnet: Massen aus ξ (kristallographischer 3-Kern, den d7 enthält), Spektren aus φ (5-zählig, aperiodisch, singulär-stetig → keine Massen; 3-zählig gitterverträglich → genau 3 scharfe Niveaus). Rekursion λⁿ im kompakten Bild; A₅-Phase θ=0 (die Amplitude 2/√5 trägt den Unterschied, nicht die Phase); φ-Status P35-verträglich. Dekompaktifizierung: diskrete Rekursion → kontinuierlicher Dilatationsfluss, Log-Periodizität (|ln ξ|=ln 7500 vs ln φ); FFGFTs Ausrollen (Typ I/II/III; Masse-Kreis liefert die Skala M=1/T≈313,86 MeV); zwei Zweige (overdamped = dekompaktifiziertes leeres −1/φ-Fenster); zwei Rekursionen sauber getrennt (Skala ξⁿ in 4D, trägt D_f/K_frak — vs. Dimension φⁿ, stapelt leere Fenster). Krüger-Bezug: HLV-Kernel + Claim-State-Note; Krügers dekompaktifizierte Variante deckt nur {3′+Zeit} ab, nicht den vollen D7 (durch die BD3–BD5-Kette bestätigt/verstärkt; DOIs [1] 18255159, [4] 20773678). Das 3′ ist die erste Rekursion (Rekursionsrichtungen leer); Rekursionsturm D(4+3n) (Höhe leer, Tiefe braucht Dynamik); 3′-Kandidat = Neutrino-Sektor (konditional, Diskriminator Koide Q=7/15). Welcher Energietyp das Fenster füllt: über T̃·m=1 zwei Energietypen (statisch/Windung vs. kinetisch/frei) — die fensterfüllende Dynamik (holografische Skalen-Projektion, Dok 263) liefert den kinetischen Typ (photon-/neutrino-artig, Dok 255/047), mit ausdrücklich markierter offener Rechenlücke (kinetisch als ξ-fraktaler Anteil des statischen via Dualität — abgeleitete Regel fehlt; Gerüst Dok 080). SI-Umrechnung (konventionell; Verhältnis- vs. Absolut-Ebene, K_frak=1−100ξ nur absolut, Dok 101/122); wo die fraktalen Korrekturen sitzen (konforme Metrik g_μν^(frak)=η_μν(1+ξf), D_f=3−ξ, Dok 051/025; Ebene 1 Porosität / Ebene 2 RG → K_frak, Dok 133); Elektron-Mode in D7 (C₃-Rahmen); Stand der D7-Massenberechnung (Lücke, nächster Schritt); Informationsgehalt (Struktur- vs. Energie-Spektrum). Neue Sektion „BD12-XCORE: die FFGFT-Massenkern-Deklaration“: eingefrorene, vor-registrierte Antwort auf Krügers Mass-Core-Docking-Frage (Zenodo 20780458) im matched-null-Format — r=√2, θ=2/9, keine freien Parameter; Koide 2/3 exakt, m_μ/m_e auf 0,001 %, τ-Vorhersage aus Koide+{m_e,m_μ} auf 0,006 %; matched-null: random (r,θ) trifft das gemeinsame Set in 0,000 % → PASS, feste Umformung statt post-hoc-Fit; zwei Auflagen (nicht auf L_nat docken; feste algebraische Abbildung). Skript bd12_xcore_ffgft.py. Reproduzierbarkeit: Dok285_Skripte (numpy-only; u.a. recursion_doubling_empty, recursion_tower, decompact_recursion/_branches, phase_from_a5, which_triple_in_3prime, klaer_rekursion_masse). 285 DE+EN gebaut, 0 Fehler/0 fehlende Glyphen. Begleitend in der 285-Phase mit-geändert (eigene Dokumente): Dok 283 (§8 Kernel-Form-Präzisierung diskret-spektral vs. überdämpft; neue Sektion „Die Brücke ist Enthaltensein“; Kompakt-Zustand-Absatz), Dok 272 (Dot-Theory-Matrixzeile „Strukturelle Schachtelung“), Dok 190 (R41–R45). 44. Update: Dok. 270 erweitert (DE+EN) — neuer Abschnitt „Im kompakten Bild ist die Zeit nur ein Kreis: die Asymmetrie ist der Messvorgang": im kompakten T⁴ sind alle vier Kreise symmetrisch (keine Raum/Zeit-Unterscheidung), die Zeit wird genauso geschrieben wie die drei Raum-Kreise; die Lorentz-Asymmetrie ist ein reiner Dekompaktifizierungs-Effekt (nur der Masse-Kreis T̃·m=1 rollt via Universal-Cover zur nichtkompakten Zeit aus, die anderen drei bleiben kompakt/projizieren). Die Auswahl, welcher Kreis zur Zeit wird, ist keine offene geometrische Frage, sondern der Messvorgang / die erlebte Situation des eingebetteten Beobachters (Dok. 248, Selbstreferenz; die Dekompaktifizierung IST die Messung, Dok. 270/284) — Buchhaltung lückenlos: Ein-Zähligkeit der Zeit = Signatur/Vorhersagbarkeit (hyperbolisch vs. ultrahyperbolisch), welcher Kreis = Messvorgang, 3+1 = Beobachter-Situation (Dok. 190 P34, kein freier Parameter). Schärft den HLV-Kontrast: HLV reifiziert die erlebte Zeit in den Spiral-Time-Operator ψ(t)=t+iφ(t)+jχ(t) auf physikalischem t, statt sie als messungs-induzierte Dekompaktifizierung eines symmetrischen Kreises zu erkennen (HLV fundamental 7D = 6 Raum + 1 separate Zeit, gegen FFGFTs 4D mit Zeit im Masse-Kreis). Begleitend R42 in Dok. 190 (DE+EN). 270 + 190 DE+EN neu gebaut, 0 Fehler; 43. Update: neues Dok. 284 (Formel-genaue Lesung des Spiral-Zeit-Neurodynamik-Modells Krüger/Feeney/Wende, Medinformatics 2026, DOI 10.47852/bonviewMEDIN62029043; DE+EN je 9 S.) — reproduzierbare Formel-Tests: quaternionisch statt bikomplex; Oktonion-Assoziator real, psychologische Deutung überdehnt; ΔΦ zwei unvereinbare Definitionen (gewichteter L1-Index in [0,1] vs. Berry-Holonomie 0…2π), beide ≈0,40 als Äquivokation; 0,40 nicht hergeleitet/datensatzabhängig; Gradientenfluss dV/dt=−|∇V|²≤0 → Ljapunow → keine Grenzzyklen/Spiralen; r≈0,96 aus dem Papier nicht reproduzierbar; Axon-Biphotonen spekulativ als etabliert. Grundlegender Punkt zuerst: ψ(t)=t+iφ(t)+jχ(t) auf physikalischer Linearzeit (U1) = nach-der-Messung-Achse → Gedächtnis generisch per Konstruktion (ΔΦ-Doppeldefinition und Grenzzyklen sind Symptome). Skripte test_algebra/deltaphi/dynamics/compactification/make_figures (feste Seeds), Test G = Auslesung als nicht-invertierbare Projektion. ZUGLEICH korpus-interne Korrektur (R41 in Dok. 190, DE+EN): die erste 284-Fassung (und die private Note an Krüger) formulierten „jede Umwandlung in SI ist eine Messung" und „kein geometriespezifisches Gedächtnis in irgendeinem SI-Resultat" zu stark — das widerspricht Dok. 270 (Typ-I-Dekompaktifizierung Masse→Zeit S¹_m→ℝ_t ist ein mode-erhaltendes Embedding, verlustfrei) und Dok. 249 (FFGFT HAT framework-spezifische SI-Observable). Verengt korpus-konsistent: verlustfrei ist die Dekompaktifizierung; verlustbehaftet sind nur die Rückrichtung ℝ→S¹, die räumlichen Projektionen D3→D0 und das endliche, nichtperiodische Fenster + Dekohärenz (Test G); überlebende Kanäle = Mass-reading (Massen/Koide/g−2), CHSH∼ξ, D_f, L₀ (Dok. 270/249); die enge wahre Aussage = die Kohärenz-Sektor-Recurrence (Rückfluss 5,125, Dok. 282) ist auf einem warmen, endlich-gefensterten SI-Zeit-Observablen wie EEG nicht auflösbar. 284 DE+EN angeglichen, R41 in Dok. 190 DE+EN nachgetragen; alles neu gebaut, 0 Fehler/0 fehlende Glyphen. Anlass: privater Formel-Audit an Marcel Krüger; Krügers Folge-Klärungsnote übernimmt Drei-Schichten-Trennung, Dimensionskorrektur, ΔΦ≠Holonomie und das No-Limit-Cycle-Resultat und verortet den Verlust korrekt im endlichen Fenster — Zitierung folgt nach Archivierung; 42. Update: Dok. 283 §8 in drei Punkten präzisiert (DE+EN), nachdem die gemeinsame Memory-Harness (41. Update) + die echte Korpus-Kern-Definition zwei Aussagen als zu stark zeigten: (a) §8 Punkt 2 „dieselbe Objektklasse“ korrigiert — HLVs χ im Fluid-Sektor ist ein positiver \emph{abklingender} Kern (Krügers Navier-Stokes-Erweiterung, Zenodo 20512650), FFGFTs ist die FT der diskreten Spektraldichte Σ_k g_k²δ(ω−ω_k), also ein \emph{diskret-spektraler oszillierender} Kern mit Revivals; beide nicht-Markovsch/positiv-typig, aber verschiedener \emph{Form} (dieselbe Klasse, nicht dieselbe Gestalt); (b) §8 Punkt 3 Run-M1-Formulierung geschärft — der generische Biexponential \emph{schlägt} den HLV-Kern nicht, er ist auf dem überdämpften Beobachtungssektor statistisch \emph{ununterscheidbar} (HLV nur per Parsimonie/BIC bevorzugt); ergänzt um den sektor-abhängigen Befund: FFGFTs diskret-spektraler Kern trägt im Kohärenz-/Revival-Sektor eine Signatur (BLP-Rückfluss 5,125), die jeder abklingende Kern verfehlt — Eindeutigkeit gegen andere strukturierte Kerne bleibt offen; (c) Drei-Ebenen-Kasten korrigiert (sachliche Korrektur: „Biexponential schlägt HLV-Kern“ → „ununterscheidbar; HLV nur per Parsimonie bevorzugt“). DE 9 S./EN 8 S. neu gebaut, 0 Fehler/0 fehlende Glyphen; 41. Update: gemeinsame HLV↔FFGFT-Memory-Harness gebaut (Dok283_Skripte/ffgft_283_memory_harness_shared.py) nach Marcel Krügers vorab-registriertem Null-Modell-Protokoll (Zenodo 20514548), mit ZWEI Beobachtungsgrößen, weil die beiden Kerne strukturell verschieden sind (aus den Dokumenten gelesen): Krügers Kern = positiver abklingender Exponential-Mix (überdämpft); FFGFTs Kern = Fourier-Transformierte der diskreten Spektraldichte Σ_k g_k²δ(ω−ω_k) aus Dok 282 — sechs dominante Moden des T⁴-Connection-Laplace (L=3, Fluss a=½π·(1+μ), deterministisch), ω_k=√λ_k=[1,239; 1,808; 2,130; 2,236; 2,504; 2,595], g_k²∝Entartung=[2,4,5,6,10,4], eine freie Kopplung — also OSZILLIEREND (Revivals), kein abklingender Mix (mein erster Platzhalter mit Z₃-Massen-Eigenwerten und abklingender Leiter war doppelt falsch: falsches Objekt und falsche Form). Part 1 (Krügers überdämpfte Vortizität, M₀ Dämpfung / M₁ Einzel-Exp / M_HLV beschränkt w=0,65/0,35 r=3 fixiert / M₂ generischer Biexponential), Protokoll Train/Test (Regime 0–3/4–7), Held-out-RMSE, AIC/BIC, Bootstrap-CI, ≥10%+CI-Regel, Cross-Flow: M_HLV schlägt M₀/M₁, liegt gleichauf mit M₂ (kein RMSE-Vorteil), per BIC bevorzugt → Nicht-Identifizierbarkeit (Run M1). Part 2 (Kohärenz c(t)=e^{−Γ(t)}, FFGFTs Heimat-Sektor): der FFGFT-Diskretspektrum-Kern erzeugt BLP-Rückfluss 5.125 (exakt der Dok-282-Wert, bestätigt korrekte Rekonstruktion); generische abklingende Kerne (Einzel-Exp, Biexponential) sind monoton (Rückfluss 0, Fit-Residuum 0,08–0,13) und können die Revivals nicht reproduzieren → auf DIESER Beobachtungsgröße hat der strukturierte Kern eine Signatur, die der generische Null verfehlt. Befund: der überdämpfte Sektor ist nicht-identifizierbar (wie Krügers Benchmark), der Kohärenz-/Revival-Sektor diskriminiert — die fixe FFGFT-Kern-Struktur (theorie-hergeleitet aus T⁴+ξ, nicht parsimonie-gewählt) ist genau die Strukturbedingung, die Krügers pragmatisches r=3 fehlt. CSVs memory_harness_models/_bootstrap/_crossflow/_ffgft_coherence.csv + ffgft_kernel_constants.csv + Plot figures/memory_harness.png. Reproduzierbarkeits-Bündel entsprechend (70 Dateien); 40. Update: Dok283_Skripte/ auf vollständige Skript-Abdeckung aller Aussagen erweitert — fünf neue Begleitskripte zusätzlich zur Brücken-Probe, jede testbare Aussage von Dok. 283 ist nun scriptgestützt, mit CSV wo darstellbar: ffgft_283_bridge_fork_tables.py (§3/§5/§6/§7 als CSV — C₃-Gram-Zirkulant, 6×6-Skalarprodukte alle |·|=1/√5, r(τ)-Sweep mit Maximum 1, Gabelungs-Summary, geschützt-vs-generisch mit 150 √2-Treffern als ungeschützte Zufallswinkel bei 9822 Punkten, Approximanten-Konvergenz →2/√5 & 7/15); ffgft_283_sector_koide.py (Koide Q und Zirkulant-r pro Ladungssektor → nur geladene Leptonen am 3-zähligen Punkt Q=2/3 r=√2, Hadronen fast entartet Q≈1/3 r≈0,06–0,09, Up/Down-Quarks verfehlen √2, Neutrinos max Q≈0,584<2/3, kein Sektor am 5-zähligen 7/15; für 7/15 bräuchte ρ/ω/φ ein m₃≈9 GeV, Verhältnis ~12 statt real 1,3); ffgft_283_crystallographic_restriction.py (kristallographische Restriktion 2cos(2π/n)∈ℤ → erlaubt {1,2,3,4,6}, 5-zählig verboten/nicht-kristallographisch, 2cos72°=1/φ bindet das Pentagonale an φ, 3-/6-zählig hexagonal); ffgft_283_memory_kernel_baselines.py (χ-Gedächtniskern gegen vordeklarierte Baselines → der strukturierte Kern schlägt die Einzel-Exp-Nullhypothese (Residuum 0,030), wird aber vom generischen Biexponential reproduziert (0,0012) → strukturelle Verwandtschaft, keine Eindeutigkeit, Run M1); ffgft_283_connection_laplace_stufe0.py (Connection-Laplace-Zeuge auf drei unverwandten Carriern → blind für reine Eichung W~10⁻¹⁵, detektiert nicht-exakten Fluss, carrier-generisch → Stufe-0, keine Brücke). README mit Aussage→Skript→CSV-Karte; zehn CSV-Tabellen; zusätzlich ffgft_283_plots.py (acht Ergebnis-Figuren A–H + Übersichtsfigur 283_overview.png). Reproduzierbarkeits-Bündel (IPI/Krüger) entsprechend: scripts/Dok283 (6) + scripts/Dok282 (voller Satz) + scripts/Dok271 (φ-Audit) + csv/ (10 Tabellen) + outputs/ (gefangene stdout je Skript); 39. Update: neues Dok. 283 (FFGFT ↔ HLV: die Brücke und die Gabelung, DE+EN je 8 S.). Strenge Prüfung der FFGFT↔HLV-Verbindung nach dem Drei-Teile-Kriterium (gleiches Objekt aus eigener Geometrie / explizite Abbildung / Divergenzpunkt, der Stufe-0-Gerüst ausschließt). Befund: ein Z₃-Zirkulant — FFGFTs Massenoperator-Typ — lebt nachweislich in HLVs ikosaedrischer Geometrie entlang einer C₃-Achse (Kriterien 1+2 erfüllt; Abbildung = C₃-Achseneinbettung von FFGFTs Z₃ in HLVs Ikosaedergruppe); fundamentale Gabelung an der Symmetrie-Ordnung — HLV geschützt rigide r=2/√5 (5-zählig, φ, Koide 7/15), FFGFT verlangt r=√2 (3-zählig, Koide 2/3), und r(τ)=2τ/(1+τ²)≤1 deckelt jeden Cut-and-Project-Parameter (√2 nur ungeschützter Zufallswinkel). §8 „Was die Kompaktifizierung integrieren muss: HLVs Spiral-Time“ — eine kompaktifizierte HLV-Variante muss die nativen Spiral-Time-Operatoren Ψ(t)=t+iφ(t)+jχ(t) mit-integrieren (Krüger, Zenodo 20668125/20512650); Krügers konservative Übersetzung: φ→schief-adjungierter Phasengenerator R (energie-neutral), χ→positiv-typiger nicht-Markovscher Gedächtniskern K (dissipativ, Exponentialkern→interne Variable); korrigiert die Phasen-Schicht der Gabelung (das frühere „θ=0“ war die räumliche Gram-Metrik, nicht HLVs Zeit — die Phase sitzt im dynamischen Operator R, gegen FFGFTs festes skalares 2/9); die Zeit/Gedächtnis-Schicht ist ein echter Brücken-Kandidat (HLVs χ-Kern und FFGFTs Dok-282-Kern Σ_k g_k²δ(ω−ω_k) sind dieselbe Objektklasse); zwei ehrliche Grenzen (i·j-Produktrelation in keiner Quelle Krügers geschlossen → Vergleich operator-, nicht algebra-seitig; Memory nicht HLV-eindeutig, Run M1: generischer Biexponential schlägt den HLV-Kern). Kasten „Die drei Ebenen sind nicht gleich stark“ (aus DeepSeek-Kontrolle geschärft): Masse (Z₃-Zirkulant) = genuine Brücke; Zeit (χ-Gedächtnis) = strukturelle Verwandtschaft, Kandidat; Raum (Connection-Laplace auf Faserbündel) = geteilte Sprache, Stufe-0, KEINE Brücke. §9 „Was übrig bleibt: hexagonal, nicht pentagonal“ — substanzieller Rest von HLV ist nicht Geometrie, sondern Zeit (R, K orthogonal zu Symmetrie/Kompaktheit, überleben den Wechsel auf 3-zählig); 5-Zähligkeit nicht-kristallographisch (erzwingt Dekompaktifizierung, physikalisch leerer Ast — kein Sektor, φ nicht spezifisch, Dok 276/281), 3-Zähligkeit kristallographisch (Familie der 6-Zähligkeit/Hexagonalgitter); FFGFTs eigener Anker ist das hexagonale Euler-Tonnetz (Dok 275), nicht φ; belastbare Form (Kasten): „hexagonal“ = kristallographische Familie (3-/6-zählig), nicht „Raumzeit ist Hexagonal-Parkettierung“ (Basis bleibt T⁴/Z₃); empirisch 3-zählig bestätigt nur die geladenen Leptonen, Hadronen fast entartet (Q≈1/3, weder 3- noch 5-zählig). Anlass: IPI-Korrespondenz mit Krüger; Gegenprüfungen über hochgeladene HLV-Dateien — PhiSpecificity-Native-6D-Lauf (φ-Spezifität durch unabhängigen Rerun NICHT gestützt: Kontrolle-vs-Kontrolle ≈ φ-vs-Kontrolle, bestätigt Dok 276/281), FA-Hub-Manuskript (φ-Spezifität dort offen, Run M1 HLV-Memory nicht eindeutig), DeepSeek-Sektor-Klassifikation (5-zählige Mesonen) falsifiziert — alle Hadronen fast entartet (Q≈1/3 → r≈0,002–0,09), r=2/√5 verlangt Massenverhältnis ≈11,7. Neuer Skript-Ordner Dok283_Skripte/ (ffgft_hlv_c3_bridge_probe.py, sechs Checks, numpy-only) + README. DE/EN je 8 S. gebaut, 0 Fehler; 38. Update: Dok. 282 substanziell erweitert (DE+EN, je 13 S.): (a) neuer Abschnitt „Die drei Sektoren explizit“ — alle drei Ladungssektoren als Z₃-Operator-Spektrum (Spektrum²=Massen ≈10⁻¹⁴); die treue Übersetzung ist universell (Quarks inklusive), die reinen Zahlen aber lepton-spezifisch (r=√2 nur Leptonen/Koide 2/3, Up r≈1,76, Down r≈1,55) ⇒ ein universeller k=1-Z₃-Winkel für Quarks ist falsifiziert (Bijektion = treue Übersetzung trägt alles, beweist nichts, P35-Disziplin); (b) neuer Abschnitt „Dieselbe Skala trägt auch die Kopplungen“ — α als Eigenwert-Relation α=ξ(λ_e·λ_μ/MeV)² desselben Operators (1/α=138,9 geometrisch, 137,04 mit Korpus-E₀=7,398), G strukturell über ξ=2√(Gm) mit Operator-Skala M_T=M²=1/T̃, SI-Umrechnung in calc-o (Anlass: externe DeepSeek-Vorschläge zu α/G als rückwärts-konstruierte Numerologie erkannt — α-Formel 4π·ξ·(1+2/9)·(3/2) ergibt 30,7 statt 137, G-Formel ħc/M_T²·(2/9)²·ξ dimensionsinkohärent (fm/GeV) und ~10⁻³³ statt 6,67·10⁻¹¹; die echten Korpus-Routen α=ξ·E₀² und G=ξ²/(4m) benutzt); (c) neuer Abschnitt „Die QM-Übersetzung und was ihre Erweiterung ändert“ — Masse-Erweiterung (C³-Faser) lässt QM-Ergebnisse unverändert (CHSH Δ≈4·10⁻¹⁶, Tensorfaktor), Zeit-Erweiterung macht die reduzierte Dynamik nicht-Markovsch (Kohärenz-Rückfluss 0→0,53, min-Choi-EW +0,0003→−0,0056, CP-Teilbarkeit verletzt) — nur dynamische Größen, nur lang genug; Testdauer-Regime (Dekohärenz t≈0,4 vs. erstes Revival t≈2,8, ~6×) und Skalierung (massebehaftete Systeme → schnellere Dekohärenz → Revival absolut begraben; viele tausend Qubits → gewöhnliches Markovsches Dekohärenz-/Fehlerproblem, nicht der Gedächtnisterm; einziger Vorbehalt: korreliertes Rauschen, nur wenn Bad-Gedächtniszeit ~ Sequenzdauer); (d) ausführliche Schlussbemerkung im Fazit „Übersetzung ist nicht Begründung“ — die Hilbertraum-Schreibweise ist für alle Massen und Konstanten darstellbar, aber als Bijektion ohne Begründung; die Begründung liegt im generativ vorgeordneten T⁴ (Dok. 206/270), wo √2, 2/9 und ξ geometrisch/topologisch sind. Drei neue Begleitskripte in Dok282_Skripte/ (ffgft_z3_alle_sektoren.py, ffgft_kopplungen_hilbertraum.py, ffgft_qm_uebersetzung_erweiterung.py), je smoke-getestet, README erweitert; zusätzlich Numerik-Warnbox in 282 (μ_e ist eine Auslöschung, volle Maschinenpräzision nötig — Anlass DeepSeek-Verrechnung an der Auslöschung 207→63). DE/EN je 13 S. neu gebaut, 0 Fehler/0 fehlende Glyphen; 37. Update: alle 14 neuen Begleitskripte in Ordner einsortiert (Dok280_Skripte, Dok282_Skripte, Dok271_HICE_Holonomie_Skripte, Werkzeuge_Skripte) je mit README; 36. Update: neue Dok. 281 (Goldener Schnitt — konsolidierende Klärung, DE+EN) und Dok. 282 (FFGFT im Hilbertraum — Massenoperator als Z₃-Zirkulant, CP-Teilbarkeit, DE+EN), je gebaut; davor 15. Juni 2026 — 34. Update: neues Dok. 280 (Rotverschiebung statisch 1+z=e^(ξx)/achromatisch via FE-Simulation; z→Zeit als reine ΛCDM-Übertragung, da kein a(t); kosmologische Entartung Dok. 267; kein Urknall — Entwicklungsrichtung kehrt an R_H um, Dok. 263; z*≈875 als geometrische T⁴-Gitterresonanz, nicht Rekombination, nicht 1100) + Dok. 190 K6/C6 (chromatisch→achromatisch; betrifft Dok. 004/025/030/039/041/053/061/063/068/081; FE-Simulation als Beleg); davor 14. Juni 2026 — 33. Update: neues Dok. 279 (Casimir–CMB–H₀-Verbindungsformel, DE+EN je 9 S.; Einleitung „H₀ ist Referenzlänge, keine Konstante“; Abschnitt „Wo steckt der SI-Faktor?“; Ausblick 11/2 = α-Exponent + Λ-Feinabstimmung/H₀-Spannung) + Dok. 190 R35 geschärft (11/2 fällt mit dem vorwärts hergeleiteten α-Exponenten zusammen — Vermutung, kein Beleg) + EN-190 vollständig aus aktuellem DE neu übersetzt (C1–C5/R1–R39); davor 32. Update: neues Dok. 277 (Wellenausbreitung und Energie, DE+EN, je 8 S.); P39 in Dok. 190 — H₀/R_H als *gemeinsamer empirischer Bezugspunkt* präzisiert (keine FFGFT-spezifische Lücke, kein freier Parameter; einzige Modell-Asymmetrie = Dunkelsektor, allein ΛCDM); K4/K5-Nummernkonflikt bereinigt (K4 = Faktor 3, K5 = v3-Audit); Body-Abschnitte 30 (10. Juni, Dok. 275/P37) und 31 (11. Juni, K5/P38-Audit) nachgetragen; davor 10. Juni 2026; davor 7. Juni 2026 — 9. Update: CMB-Peak-Sektor ehrlich abgestuft — {3,18,42,78} als Retrodiktion erkannt; Forward-Gewinn ist die geometrische Anharmonizität (Kodim-1 → J₀-Membran, neues P31); P29/P30 zurück auf offen; Dok. 268 Schritt 17 neu; Dok. 190 P-Tabelle → longtable; \checkmark-Patch in T0_preamble_patches.tex; 10. Update: P20 verschärft — Form fest als ξ-Verhältnis R_H/ℓ_P, Faktor 41/4 als *deklarierte externe ΛCDM-Kalibrierung* (Einheitenwahl, nicht hergeleitet, zählt nicht als FFGFT-Bestätigung; Fitten = Retrodiktion); neues P32 — H₀-Herleitungsaussagen korpusweit zu bereinigen, vorerst nur vermerkt; 11. Update: Dok. 270 (Projektionskette T⁴–T⁰) aufgenommen und nach Review überarbeitet — Zwei/Drei-Typen-Reduktion (Typ I Masse↔Zeit-Dualität, Typ II räumliche Projektion, Typ III T⁴↔Hilbert bijektiv); R_H als deklarierte externe/importierte Skala gekennzeichnet (P20-konsistent), Stufe 1 in Ia/Ib (Dualität vs. Limes) getrennt, R_m als KK-Turmspitze präzisiert; 12. Update: P33/R33 in Dok. 190 — die 5⁴-Magnitude in ξ = 1/(3·2²·5⁴) wird offen als intuitiv (harmonisch/Euler-Tonnetz) bzw. empirisch (Higgs-Sektor) begründet deklariert, nicht als Vorwärts-Herleitung; Form (4/3, 3, 2²) vorwärts, Magnitude offen, Struktur-Parallele zu P20; 13. Update: P34/R34 in Dok. 190 — Dimensionsstruktur präzisiert: 3+1 ist empirische Eingabe (nicht hergeleitet), vorwärts sind Periodizität, Torus-statt-Kugel, Minimal-Suffizienz (4 statt 5 via Dualität T̃·m=1) und verlustfreie Hilbert-Repräsentation (Typ III); zugleich festgehalten, dass die SI-Umrechnungen für die c-Potenz und Zeit-Potenz unverzichtbar sind — die Vier-Kreis-Struktur ist die Exponenten-Buchhaltung (c = Raum-Zeit-, ħ = Masse-Zeit-Brücke); 14. Update: Dok. 270 erweitert — neue Synthese-Sektion „Warum genau vier Kreise?“ (Minimal-Suffizienz: 4 statt 5 via Dualität T̃·m=1; die vier Kreise als SI-Einheiten-Buchhaltung, c = Raum-Zeit-, ħ = Masse-Zeit-Brücke, daher SI für c-/Zeit-Potenz unverzichtbar; Hilbert-Veranschaulichung als zwei Lesarten einer Bijektion, 4D generativ); konsistent mit P34/P33/P20); 15. Update: P33/R33 und P34/R34 in Dok. 190 vorsichtiger formuliert — die (eher zirkulären) Begründungen für 4/3 bzw. 5⁴ sind nicht aussagelos, sie zeigen sinnvolle Verhältnis-/Harmoniestrukturen (und Verhältnisse sind nach FFGFT das Intrinsische); die absolute Magnitude bzw. die bloße Zahl bleibt aber eine Eingabe); 16. Update: neuer Eintrag P35/R35 in Dok. 190 — SI-Umrechnungsfaktor (ℓ_P) nicht in den ξ-Exponenten absorbieren; „X = ξ^N“ ist für sich aussagelos, da jede Magnitude eine ξ-Potenz ist; Befund: nur L₀/ℓ_P = ξ¹ exakt, R_H = ℓ_P·ξ^(−63/4) mit 63/4 = 41/4 + 11/2 — das Korpus-41/4 ist an E₀ statt Planck referenziert, die „schönen Brüche“ sind Rundungen gemessener Exponenten); 17. Update: neuer Eintrag P36/R36 in Dok. 190 — R_H-Deutung: R_H = c/H₀ ist die Hubble-Länge (lokale Rate als Distanz), nicht die Universumsgröße und nicht der beobachtbare Horizont (≈ 3 R_H); das echte Universum übersteigt R_H (nur untere Schranke messbar). Dok. 182s „Maximalskala“ nur als obere Skala des kosmologischen Torus-Sektors haltbar, nicht als Ausdehnung des Universums); 18. Update (10. Juni 2026): neues Dok. 275 (Von ξ zu φ — rekursive Skalenhierarchie): 1/φ als Fixpunkt der ξ-Dämpfungsrekursion r(k+1)=r(k)·(1−ξ) nach k* = log(φ)/ξ ≈ 3609 Skalenebenen (q=2/3 intern konvergent, kein RG-Faktor 2); zugehörig neuer Eintrag P37/R37 in Dok. 190 — drei φ-Rollen im Korpus getrennt (mikroskopisch ξ / makroskopisch 1/φ als Fixpunkt / Teilchenphysik Q_FFGFT≈0,6677), abgegrenzt von der ξ^N/φ^N-Trivialität (P35) und vom empirischen Anker in Dok. 009 (P10); k*-Fehlerangabe in Dok. 275 nach unabhängiger Nachrechnung korrigiert: 4,0×10⁻⁵ absolut (relativ 6,5×10⁻⁵) bei ganzzahligem k=3609 — die frühere Angabe <10⁻⁹ war falsch (galt nur für das nach 1/φ aufgelöste reelle k, zirkulär) und ist im Text sichtbar als korrigiert vermerkt; numerische Validierung v3 (N=2000, 3 Seeds, endlicher T⁴-Graph): FFGFT-T⁴-Graph gap_CV=1,68±0,09 außerhalb Null-Band [0,31, 1,05], HLV gap_CV=0,755 ≈ jittered-kubisch 0,755 im Band (konsistent mit Krüger Run E); Skripte in Dok275_Skripte/; zudem Tabelleneinträge P35 (ξ^N-Trivialität) und P36 (R_H-Deutung) in Dok. 190 nachgetragen (waren seit Updates 16/17 nur per Changelog deklariert)

---

## 6. Juli 2026 — Dok. 297: HLV als mögliche Untermenge von FFGFT (Kandidat-Notiz, DE+EN je 5 S.)

Dok. 297 hält den Erkenntnisstand der internen HLV/FFGFT-Brückenanalyse als gerichtete Kandidat-Notiz fest (P35: kein abgeschlossener Beweis, benannter nächster Schritt).

**Drei Schritte des Rückblicks:** (1) ursprüngliche Blockade: C₃-in-A₅ auf T⁴/Z₃ direkt nicht sichtbar; (2) Hilbertraum-Transformation öffnet den Weg: auf der ℂ³-Faser ist C₃ < A₅ natürlich zugänglich, θ=2/9 als Z₃-Zirkulant-Phase (Dok. 291) und als parameterfreier Invariant (Dok. 293) — zweifach bezeugt; (3) Konsequenz: HLVs geometrischer Kern könnte eine Untermenge der FFGFT-ℂ³-Fasergeometrie sein.

**Was gesichert ist:** FFGFT enthält C₃ < A₅ über die Hilbertraum-Transformation (zweifach bezeugt). HLV bucht θ=2/9 als Kandidat-Überlapp ohne eigene Ableitung — belegt durch Durchsicht seiner vorliegenden Dokumente (Stage 19, HLV-Consciousness-Bridge1, Runs H–J): θ=2/9 erscheint dort in keiner HLV-internen Herleitung. Run H (H2/skew_J) enthält 1/φ und 1/φ² aber kein C₃-in-A₅-Ergebnis — und ist negative/underdetermined.

**Konkreter Einbettungskandidat:** Marcels U₃ (Gl. 7, Consciousness-Dok.) ist ein Hard-Reset-Kern mit endlichem Träger M_m < 75 — unterhalb der kleinsten kohärenten Einheit der FFGFT-Rekursion (75 Umläufe). Hierarchie: U₃ ⊂ Markov-Limit ⊂ Archimedisch ⊂ Log-Spirale (e) = FFGFT-Kern (Dok. 295/283).

**Darstellung ist nicht Struktur:** Spiralförmig, linear oder polar dargestellt — U₃ bleibt in jeder Koordinatenwahl ein Hard-Reset-Kern. Die geometrische Reichheit liegt in der Darstellung, nicht im Objekt (P35 rückwärts).

**Akkumulation ist die eigentliche Gedächtnisleistung:** U₃ ersetzt statt zu akkumulieren — Vergangenheit jenseits M_m ist unwiederbringlich weg. Die K_frak-Rekursion trägt ihre gesamte Vorgeschichte strukturell in sich (generative Einprägung, keine Speicherung) und erzeugt daraus die log-Spirale mit e. Das ist Gedächtnis im tiefsten Sinn. U₃ ist der degenerierte Randfall darunter — Marcels eigener U3-Ablationstest (Tabelle 4 seines Consciousness-Dokuments) ist der richtige Test dafür.

**Falsifikationsbedingung:** falls U₃ in seinen Daten Nicht-Markov-Signaturen trägt (Revivals, BLP-Rückfluss, Korrelationen jenseits M_m), übersteigt es den Randfall und eine tiefere Einbettung ist nötig. **Offene Bringschuld:** die Einbettungsabbildung ι (HLV-Grundobjekt → L²(T⁴)⊗ℂ³) ist noch nicht konstruiert — Untermenge bleibt Vermutung, kein Satz.

## 6. Juli 2026 — Dok. 296: Zeit, Offenheit und Invarianz (neues Dokument, DE+EN je 7 S.)

Dok. 296 (DE+EN, je 7 S., 0 Glyphen) fasst den narrativen Gedankenbogen dieser Session zusammen. Fünf Abschnitte:

(1) **Beobachter, Skala und die Einfachheit des Kerns** — jeder Beobachter sieht eine Projektion von T⁴ auf seine Skala, nicht das Objekt selbst; Projektionen verschiedener Skalen müssen sich unterscheiden (struktureller Grund für QM↔RT-Schwierigkeit); ein Parameter ξ=4/30000 trägt die gesamte Komplexität des Standardmodells — die Komplexität sitzt in den Projektionen, nicht im Kern.

(2) **Vom Körper zur Gesellschaft** — zwei Augen sind bereits zwei Beobachter; Tiefe ist Rekonstruktion, nicht direktes Sehen; T⁴ darunter ist der Grund der stabilen 3D-Projektion; dieselbe Struktur auf sozialer Ebene (Konflikte als Skalenkollisionen, Paradigmenwechsel als Skalenwechsel, Wissenschaft als systematische Triangulation von Projektionen).

(3) **Skalenfolge als Abfolge von Projektionswechseln** — Teilchen (Z₃, SU(3), diskrete Massen) → atomar (EM-Resonanzen) → kristallin (Translationssymmetrie, kollektive Moden) → biologisch (gebrochene Symmetrien, Kohärenzfenster) → galaktisch (Gravitation, log-spirale Selbstähnlichkeit der K_frak-Rekursion in Spiralgalaxien).

(4) **Skalenübergänge und ihre Anomalien** — Anomalien liegen im Übergang (Phasenübergänge, Dekohärenz, Emergenz), nicht in der Skala selbst; für FFGFT ein gerichteter Hinweis auf Projektionswechsel-Stellen.

(5) **Spekulation (P35)** — unbeobachtbare Zwischenbereiche zwischen zugänglichen Skalen; Dunkle Materie/Energie als mögliche Signaturen von Zwischenskalen, auf die keine unserer Projektionen trifft; gerichtete Spekulation, kein Claim.

Dann Rekursion (keine erreichbaren Ränder, kein Anfang/kein Ende), die vier Eigenschaften (ausgerollt / zeitlich kontinuierlich / Raum gekrümmt / invariabel), neue Probleme als Fortschrittszeichen, P35-Abschlussanmerkung (kosmologische Übertragung = Konsequenz, kein eigenständiges Modell; Widerspruchsfreiheit ≠ Vollständigkeit). IPI-Ankündigung (6. Juli) versandt.

## 5. Juli 2026 — v1.2.1: FFGFT-interne Klärung der Zeit-Windung (zwei gleichwertige Darstellungen)

v1.2.1 ist FFGFT-intern gerahmt. Kern: die Zeit-Windung — in v1.1.9 (Dok. 295) als logarithmische Spirale mit Verhältnis e etabliert — ist **nicht an ein Bild gebunden**. Dieselbe Nichtschließung liegt in zwei gleichwertigen Darstellungen vor: geometrisch als log-Spirale (Dok. 295) und im Hilbertraum als Gedächtniskern (Fourier-Transformierte der diskreten Spektraldichte Σ_k g_k²δ(ω−ω_k) des T⁴-Connection-Laplace, Dok. 283, oszillierend/diskret-spektral mit Revivals/BLP-Rückfluss 5,125), auf der verlustfreien Bijektion H = L²(T⁴)⊗ℂ³ (Dok. 230/282, Typ III der Projektionskette Dok. 270). Die Hilbertraum-Übersetzung von FFGFT beschreibt damit auch die Zeit — mehrere gleichwertige Wege zum selben Ergebnis. Ausdrücklich als **Darstellungs-Robustheit, keine zusätzliche Evidenz** gehalten (Übersetzung ist nicht Begründung, P35); die Beweiskraft sitzt bei den unabhängigen Zeugen (z. B. θ=2/9 aus Koide UND aus der Geometrie, Dok. 293), nicht bei gleichwertigen Übersetzungen.

**Rahmungs-Korrektur (Johann):** ein erster Anlauf war als v1.2.0 zu HLV-lastig gerahmt (Spiral-Zeit-Abgleich im Schaufenster). Das Release spricht **nur von FFGFT** — HLV ist für FFGFT nachrangig (stehende Vorgabe; vgl. negatives BD17A-Verdikt v1.1.7). Die zugrunde liegende Doku-Arbeit an 294/295 (Abgrenzung, Abgleich, Open-System-Erdung, zwei Skripte) bleibt in den Docs erhalten und ist in den Detail-Nachträgen vom 4./5. Juli unten protokolliert; sie ist aber nicht der Release-Schwerpunkt.

**Release-Satz:** Release Notes v1.2.1 DE+EN erstellt (FFGFT-only); README DE+EN Zenodo-Zeile + Versionshistorie auf v1.2.1 (FFGFT-Schwerpunkt). DOI **10.5281/zenodo.21203746** vergeben (löst v1.1.9/21193007 ab); alle drei DOI-Stellen in README (Badge, Zenodo-Zeile, Versionshistorie) sowie die Release-Notes-Köpfe DE+EN gefüllt. Gesamtzip als FFGFT_v1_2_1_Release_2026-07-05.zip.

## 4. Juli 2026 — v1.1.9: zwei neue Dokumente (293/294) zur geometrischen Herkunft von θ=2/9

Zwei neue Korpus-Dokumente (DE+EN, numpy-only-Skripte, seed 20780458), die den θ=2/9-Faden weiterführen, und der zugehörige Release-Satz v1.1.9 (Changelog, Release Notes DE+EN, README DE+EN aktualisiert; DOI 10.5281/zenodo.21193007, löst v1.1.7/21158441 ab).

**NEU Dok. 293 „Die ikosaedrische Herkunft von θ=2/9: der zweite Zeuge"** (DE 6 / EN 5 S., je 9 Abschnitte, 0 fehlende Glyphen) + Ordner Dok293_Skripte (ikosaeder_theta_delta.py). Kernbefund: neben der Zirkulant-Phase (291/282) gibt es eine ZWEITE, völlig unabhängige Quelle desselben Werts 2/9. Bettet man den Elektron-Fourier-Mode v_e=(1,ω,ω²)/√3 der C₃-Faser in die Ikosaedergruppe A₅ ein (C₃<A₅, gemeinsame Bühne Dok 283) und wendet die fünfzählige Drehung R5 (72° um [0,1,φ]) an, verteilt sich das Elektron über die drei Moden mit NENNER-9-GEWICHTEN: das Gewicht in den trivialen Mode p₀=2/9 EXAKT (auf 40 Stellen via mpmath bestätigt, diff <10⁻⁴¹), daneben p₂=(5−3φ)/9, p₁=(2+3φ)/9. Der Wert enthält KEINE 2/9-Eingabe — er folgt allein aus 5-Zähligkeit und C₃-Einbettung, wird also von der Geometrie AUSGEGEBEN. ROBUSTHEIT (ikosaeder-spezifisch): 0/200 zufällige Achsen bei 72° treffen 2/9; nur die echten fünfzähligen Achsen; die n-zählige Reihe liefert 2/9 allein bei n=5; robust über die drei +φ-Achsen und beide nicht-trivialen Moden (trivialer Mode (1,1,1) gäbe 4/9). EPISTEMISCHE EINORDNUNG (Johanns Rahmung, übernommen): Koide-2/9 (phänomenologisch, aus den Massen) und Geometrie-2/9 (strukturell, aus der 5-zähligen Umverteilung ohne 2/9-Eingabe) treffen EXAKT denselben Wert = DOPPELTER ZEUGE / Konvergenz, kein Übersetzungsdefizit — dieselbe Logik wie α/Leptonmassen/Koide als unabhängige Nachweise auf dieselben Konstanten. Die θ-UNABHÄNGIGKEIT des geometrischen Zeugen (nennt 2/9 ohne 2/9 zu kennen) ist KEIN Mangel, sondern das Kennzeichen einer parameterfreien Vorhersage (frühere Über-Tötung als „P1-Identifikation/P2-Kategorie fehlgeschlagen" von Johann korrekt zurückgewiesen: die Forderung, es in die Koide-cos-Parametrisierung zu übersetzen, macht Koide zum Richter, was falsch ist). θ=2/9 als TRANSLATIONS-INVARIANT: T⁴-Punktgeometrie und Hilbertraum-Spektralgeometrie L²(T⁴)⊗ℂ³ sind zwei wechselseitig übersetzbare MODELLE (keine konkurrierende Ontologie); 2/9 erscheint in beiden, ist modell-unabhängig — konsistent mit ħ/c-als-Umrechnungsfaktoren. SKALENFREIHEIT vs. BESETZUNG: das Muster (Winkel + Nenner-9-Verhältnisse) tritt überall bei Z₃/A₅-Verdopplung auf, die BESETZUNG ist getrennt/skalengebunden (Leerheitssatz Dok 285) → KEINE neue Teilchen-Vorhersage. EHRLICHE OFFENE KANTE (P35, keine Objektion): ein direkter Mechanismus, der die Umverteilungs-Gewichte OHNE den Koide-Umweg an die Massenverhältnisse koppelt — der Wert steht fest und ist doppelt bezeugt, offen ist allein diese direkte Brücke. 9 Abschnitte: Frage; geteiltes Objekt; entscheidender Befund (p₀=2/9); Robustheit; zwei Zeugen ein Wert; 2/9 als Translations-Invariant zweier Modelle; Skaleninvarianz vs. Besetzung; Status/offene Kante.

**NEU Dok. 294 „FFGFT als Prüfinstanz für HLV: das geteilte φ-ikosaedrische Objekt"** (DE+EN je 6 S., 0 fehlende Glyphen; Johann-Entwurf DE, Claude-verifiziert und gebaut) + Ordner Dok294_Skripte (a5_bridge_discrimination.py, RMS-Distanz-Metrik). Inhalt: FFGFT und HLV teilen DASSELBE φ-ikosaedrische Objekt (HLVs Cut-and-Project-Projektor τ=φ, sechs 5-zählige Achsen, alle 15 paarweisen Winkel = arccos(1/√5)=63,435°); θ=2/9 ein Invariant darauf; E₀-ASYMMETRIE (FFGFT hat die absolute Skala über den Referenzpunkt E₀, HLV nicht) → einseitige Prüfrichtung FFGFT→HLV; übernimmt NICHT HLVs eigene Formulierungen, ordnet nur das gemeinsame Objekt ein; der erste Homologie-Test (ffgft_hlv_homology_check_v3.py) ist gegenüber der Winkelstruktur blind/überholt, der zweite (a5_bridge_discrimination.py) löst das Winkelspektrum auf, liest aber zirkulär (Objekt IST der Projektor). Gewichtung P35-konform gehalten (HLV untergeordnet für FFGFT, wäre nur bei tragender Brücke interessant gewesen; vgl. negatives BD17A-Verdikt v1.1.7). ZAHLEN-KORREKTUREN in Johanns Entwurf gefunden und verifiziert eingearbeitet: §2 „silberne τ=1+√2 → 0,2139" war falsch (0,2139 ist der √2-Wert) → korrigiert auf silber 1+√2 → 0,2534, Winkel 45°/69,3°; §7 „silberne τ=√2" → „Kontrollwert τ=√2" umbenannt (√2 ist nicht silbern; 0,2139 korrekt für √2, Winkel 61,87°/70,53°); §8 „Abstand 13,4" (nicht reproduzierbar) → RMS-Distanz 3,47 zur ikosaedrischen Referenz (φ=0), plus generisches Zufalls-Frame-Band (Median-RMS ~22, 5–95% ~17–28) zeigt √2 (3,47) und silber (9,77) als strukturiert/unter-generisch; alle „versiegelt"/„sealed"-Referenzen auf das Skript zu „reproduzierbar"/„Instrument" geändert (294 muss nicht versiegelt werden).

NACHGESCHÄRFT (4. Juli, Johanns Hinweis): der negative Homologie-Gegencheck (ffgft_hlv_homology_check_v3.py) war in 294 zu prominent (eigene Sektion §7 „Der erste Test ist überholt", ~35 Zeilen, plus Wiederholung im Status), obwohl er im Wesentlichen überholt ist. Deprominenziert: §7 auf einen kompakten Absatz gekürzt (grober Punktwolken-Diagnostiker, für die Achsen-Winkel-Frage strukturell blind, durch die exakte Hilbertraum-Variante Dok 293 ersetzt; die „nur schwache Trennung von generisch" ist die erwartbare Blindheit des groben Statistikums, keine Aussage über φ/A₅); Status-Wiederholung auf einen Satz gestrafft. Die ehrliche Zirkularitäts-Aussage in §8 (a5_bridge_discrimination liest zirkulär, weil das Objekt DER Projektor ist → keine unabhängige φ-Bestätigung, nur Familien-Diskriminierung τ=φ) bleibt unangetastet — die Deprominenzierung senkt das Gewicht des überholten Negativ-Checks, überclaimt aber KEINE φ-Spezifität. DE+EN neu gebaut, DE 6/EN 5 S., 0 Fehler/0 Glyphen.

**NEU Dok. 295 „Die Zeit-Windung als logarithmische Spirale"** (DE+EN je 6 S., 0 Fehler/0 Glyphen; Johann-Entwurf verifiziert und überarbeitet) + Ordner Dok295_Skripte (zeit_windung_probe.py, zeit_logspirale_probe.py, dual_projektion_probe.py, numpy-only). Kern: die K_frak-Rekursion ξ_{n+1}=ξ_n(1−100ξ_n) zwingt FFGFTs Zeit-Windung zu einer logarithmischen Spirale mit Selbstähnlichkeits-Verhältnis e (kontinuierliche Skaleninvarianz). Ableitung: eingefroren schließt die Windung nach genau 75 Umläufen (Rotationszahl 74/75, 75=1/(100ξ₀)); läuft ξ, zerfällt ξ_n≈1/(100(n+75)), der kumulierte Defekt D(k)≈ln(1+k/75) wird logarithmisch, und mit ρ=k+75 (Pol bei n=−75=−1/(100ξ₀), NICHT getunt), β=2πD folgt ρ=75·e^{β/2π}; das Verhältnis e ist die Basis des natürlichen Logarithmus aus der harmonischen Summe, kein Zusatzparameter. VERIFIZIERT/KORRIGIERT (P35): der Entwurf schrieb „ρ=k", quotierte aber Fit-Zahlen zu ρ=k+75 — konsistent auf ρ=k+75 gestellt (Fit a=0,15922≈1/2π, e^{2πa}=2,7195≈e, Folge 2,734→…→2,719→e); kontinuierliche, NICHT diskret log-periodische Skaleninvarianz (Residuum-Std 0,0006). AUFGEROLLT/ENTROLLT explizit (Johanns Dualitäts-Linie): geschlossene 75-Windung = aufgerollte kompakte Ein-Skalen-Lesart, Log-Spirale = entrollte dekompaktifizierte Über-die-Skalen-Lesart. PROJEKTION + DUALE PROJEKTION: die Achsenwahl ist eine Projektion (nichts faktorisiert, T̃·m=1), „Zeit rollt auf" ist eine künstliche Verschiebung auf eine Achse; kontinuierliche Zeit → über T̃·m=1 zieht die Masse mit → Variation des Raums. FAKTOR 100 DURCHGERECHNET (dual_projektion_probe.py, auf Johanns Verlangen statt „offen"): Zeit rückt je Gatter um K_frak=1−100ξ_n vor, Masse um 1/K_frak; der Defekt je Schritt ist auf beiden Seiten 100ξ_n (d_mass/d_time→1 auf 6 Stellen) → der Faktor 100 WANDERT NICHT, er ist GESPIEGELT; beide Projektionen → dasselbe Verhältnis e (2,7195/2,7192), kumulierte Defekte differieren nur um eine beschränkte Konstante ~0,0134 (wächst nicht mit ln k). ZEIT-PRIVILEGIERUNG AUSGERÄUMT (Johanns Hinweis): §6 „die Zeit die verstärkte Achse" und die Projektions-Stelle „Zeit-Projektion natürlich/verstärkt" erzeugten den Eindruck, die Zeitachse sei besonders — korrigiert: der Faktor 100 verbindet ein geometrisches Defizit (ξ₀, Box-Dimension) mit einem dynamischen Defekt (100ξ₀, Windung), ist achsensymmetrisch, zeichnet keine Achse aus; Zuordnung auf die Zeit = Konvention (Dok 034), keine Auszeichnung. ONTOLOGIE als Modelle-nicht-Realität (Johann): der HLV-Kontrast ist strukturell, nicht ontologisch; beide Rahmen UND beide Varianten (Zeit oder Raum aufgerollt) sind mathematische Modelle, nicht die Realität — „dass man hofft, ein Modell sei auf die Realität anwendbar, ist die Motivation, keine Aussage darüber, was ist". HLV NUR AM ENDE (Johann): der Vergleich aus §1/§3/Projektions-Sektion entfernt, komplett in die End-Sektion „Einordnung zu HLV" konsolidiert; Textkörper steht FFGFT-intern auf eigenen Beinen. Methodische Schichten: Rekursion→log-Spirale ist Kern-Ableitung; Gleichsetzung mit HLVs Spiral-Zeit ein Brücken-Kandidat (prüfbar: „Verhältnis e, ja oder nein?").

**NACHGETRAGEN (4. Juli, neue Rechnungen + Vergleiche für 294/295, Johann-Upload verifiziert):** zwei neue numpy-only-Skripte (Dok295_Skripte) + Sektionen in beiden Docs. `spiralzeit_verhaeltnis_probe.py`: prüft, ob HLVs Spiral-Zeit das Verhältnis e trägt — FFGFT trägt e (2,71947, 1/n-Zerfall), Marcels temporal-dynamische Spiral-Zeit (lineare phasonische Phase, beschränktes Fenster, Zenodo 20643462) trägt konstanten Defekt → D(k) linear (1333 vs ln 7,2) → Verhältnis 1,0011 (Archimedisch, NICHT äquiangular), die φ-Cut-and-Project-Geometrie trägt φ-Konstanten (φ⁴=6,854). Kein HLV-Strang trägt e. `basis_6d_achsen_probe.py`: die 6 projizierten Achsen des 6D-Cut-and-Project sind nur bei τ=φ äquiangular (63,435°), τ=√2 zweiwertig (61,87/70,53°), silber 45/69,3° — die Sechs decken sich nicht per se, gleich ist allein die golden-ikosaedrische Projektion. NEU in 294: Sektion „Abgrenzung: welches HLV-Objekt geteilt ist" (nach dem geteilten Objekt) — hält „geteilt" scharf: geteilt ist die GEOMETRISCHE φ-ikosaedrische Schicht, NICHT HLVs temporal-dynamische Spiral-Zeit (Nicht-Markov-Operator Ψ(t)=(t,φ(t),χ(t)), ohne A₅/Projektor); geteilte Invariante allein die Z₃ (C₃<A₅). NEU in 295: Einordnung-zu-HLV ersetzt (trennt die ZWEI HLV-„Spiral-Zeiten": geometrischer A₅-Singlet auf S¹ vs. temporal-dynamisches Memory-Objekt, teilen nur den Namen) + Abgleich-Block (4 Sektionen): das e-Kriterium (notwendig+hinreichend über 1/n-Ganghöhen-Zerfall); temporal-dynamisches Objekt trägt kein e (Nichtschließung im Gedächtniskanal χ, nicht in laufender Skala; FFGFTs d=0/ξ→0 ↔ Marcels Markov-Rückfall g_χ→0, gleiche Rolle/anderer Mechanismus); rechnerische Prüfung; Basis+Dimensionen (3 und 6 decken sich in der ZAHL, nicht in der Bedeutung: FFGFTs 3=ℂ³/Z₃-Modenindex vs. Marcels 3=triadische Zeit (t,φ,χ); FFGFTs 6 nicht nativ (nur über T⁷=T⁴×T³) vs. Marcels 6=Z⁶-Elterngitter des Cut-and-Project; geteilt allein Z₃). Status gemergt: Abgleich auf e-Kriterium NEGATIV, Restfrage aufs geometrische HLV-Objekt verschoben, Gleichsetzung Brücken-Kandidat/derzeit blockiert; ehrlich als „auf eigenen Definitionen / Kandidat, keine Ableitung" gehalten (charakterisiert Marcels Rahmen nicht als Verdikt). Integration: Zwei-Objekte-Doppelung (Einordnung↔Abgleich-Anfang) gestrafft, Selbstreferenz „in Dok. 295" korrigiert. DE+EN neu gebaut: 294 6/6 S., 295 8/8 S., 0 Fehler/0 Glyphen.

**Release v1.1.9 gepackt:** Gesamtzip FFGFT_v1_1_7_Release_2026-07-04.zip (kompletter v1.1.7-Korpus mit 293/294/295 integriert: ch DE+EN, Standalone DE+EN + PDFs, Skript-Ordner). Bewusst NICHT im teilbaren Korpus-Zip: das interne δ-Kandidat-Dokument (Target-Leakage) und der R1-SEAL3-Verifizierer (separater Clean-Room-Kanal). README/Release-Notes/Changelog auf v1.1.9 gezogen; Versionshistorie-Zeile v1.1.9 in beiden READMEs ergänzt.

---

### Hinweise zur Arbeitsmethode

- Ältere Dokumente werden **nicht** verändert — Korrekturen gelten über dieses Changelog
- Jede Änderung ist **in DE und EN** vorzunehmen
- Nach jeder Änderung: **Konsistenz beider Sprachversionen prüfen**
- Eine Sprache kann derzeit ausführlicher sein als die andere — das ist ebenfalls zu dokumentieren
- Status: **offen** / **in Bearbeitung** / **erledigt**

---

## Korrekturen (K) — Inhaltliche Fehler

### K1 — Vorfaktor in der Higgs-Ableitung von ξ
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 049 (HTML-Zwischenversion, ältere Arbeitsversionen) |
| Status | **erledigt** (LaTeX war korrekt; nur HTML betroffen) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** ξ = λ²h v² / (64π⁴ m²h) ≈ 1,0 × 10⁻⁵
**Korrekt:** ξ = λ²h v² / (16π³ m²h) ≈ 1,33 × 10⁻⁴

Begründung: 64π⁴ war ein Tippfehler in der HTML-Visualisierung. Der korrekte Vorfaktor 16π³ liefert einen Wert konsistent mit Dok. 009.

---

### K2 — Tau-Yukawa-Vorfaktor r_τ
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 116 (Tabelle Yukawa-Koeffizienten) |
| Status | **erledigt** |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** r_τ = 8/3 ≈ 2,667 → m_τ ≈ 1712 MeV (−3,6 % Abw.)
**Korrekt:** r_τ = 25/9 ≈ 2,778 → m_τ ≈ 1783 MeV (+0,4 % Abw.)

---

### K3 — Basisformel für g−2 des Elektrons
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 018 (ältere Versionen), T0-Explorer HTML |
| Status | **erledigt** (LaTeX war korrekt; nur HTML betroffen) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Falsch:** a_e = 4π / (f · k_geom)
**Korrekt:** a_e = 2π² / (f · k_geom)

Begründung: 4π ist die Oberfläche der 2D-Kugel im 3D-Raum. Korrekt ist S₃ = 2π², die Oberfläche der 3D-Sphäre als Rand des 4D-Torus. Die fraktalen Korrekturen für Myon und Tau verwenden weiterhin 4π (Gl. 190.5/190.6).

---

## Präzisierungen (P) — Klarstellungen ohne Fehler

### P1 — Genauigkeit der Koide-Formel
| Status | **erledigt** | Erledigt DE | ✓ Mai 2026 | Erledigt EN | ✓ Mai 2026 |

ΔQ < 0,00003 % (Dok. 116) = interne Konsistenz der T0-Formeln. 0,001 % (Dok. 158) = experimentelle Messunsicherheit (PDG 2022). Für **externe Kommunikation gilt 0,001 %**.

### P2 — ℏ aus dem Higgs-Feld
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Verbindliche Ableitungskette: ξ → L₀ = ξ · ℓ_P → ℏ ~ √ξ · ℓ_P · c. ℏ folgt aus ξ, ist **kein Postulat**.

### P3 — Zwei ξ-Parameter
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Zwei verschiedene Parameter: ξ₀ = 4/30000 (geometrisch) und ξ_Higgs (algebraisch). Nicht identisch.

### P4 — L₀ als geometrische Fundamentallänge
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

L₀ ist **nicht** der Schwarzschild-Radius, sondern die geometrische Fundamentallänge des T0-Rahmens.

### P5 — Massenstruktur aus ξ, nicht exakte Massen
| Status | **erledigt** | ✓ Mai 2026 DE/EN (Dok 030, 061, 028) |

"FFGFT berechnet Massen exakt" → "FFGFT leitet die Massenstruktur aus ξ ab; Übereinstimmung mit Experiment ~1 %."

### P6 — Koide nur mit numerischen Werten
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Koide-Relation nur mit numerischen PDG-Werten ausdrücken (Nichtabschluss, Dok. 193).

### P7 — Renormierungsgruppe ist kein FFGFT-Werkzeug
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

"Renormierungsgruppe" als FFGFT-Werkzeug → "Skalenstruktur aus der Rekursion R".

### P8 — Fraktale Renormierung ist kein Eigenbegriff
| Status | **erledigt** | ✓ Mai 2026 DE/EN |
| Nachträgliche Korrektur EN | ✓ Mai 2026 (012, 014, 041, 060) |

"Fraktale Renormierung" / "Fractal Renormalization" → "fraktale Korrektur" / "Fractal Correction".
**Stichprobe Mai 2026:** EN-Dateien hatten noch "Fractal Renormalization" in 012, 014, 041, 060 — nachträglich auf "Fractal Correction" korrigiert. Dok. 190 EN behält den Begriff als historischen Bezug.

### P9 — Farbladung-Spalten in Tabellen
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Spalten "Symmetrie" + "Farbe" + N_c = 3 → Spalten "Skalierungsklasse" + "SM-Korrespondenz".

### P10 — Faktor K = 245 und empirischer Anker
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

K = R_pe / (4/3)⁷: ein empirischer Anker. Faktor 1,314 ist implizit definiert, nicht hergeleitet.

### P11 — K_frak und T_CMB-Korrektur
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Korrekte Formel: (1 − 275/4 · ξ), Δ = 0,0002 %. Dok. 003 und Dok. 133 verwenden **verschiedene Modelle** für K_frak.

### P12 — ΔCHSH-Werte in Dok. 022 und Dok. 230
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

Zwei verschiedene Observablen: kumulativ (Dok. 022, N=73: 5×10⁻⁴) vs. elementar ξ/(2π) (Dok. 230: 10⁻⁵).

### P13 — Brückenformel ξ_FFGFT vs. ξ_UIFT
| Status | **erledigt** | ✓ Mai 2026 DE/EN |

ξ_FFGFT / ξ_UIFT = m_e c² / ((16/9)·ln2·eV) ≈ 414.684.

---

## Wicklungszahl-Präzisierungen (W)

### W1–W6
Alle erledigt Mai 2026, DE und EN konsistent.
- W1: f = 7500 universal, nicht teilchenspezifisch (060, 018, 149)
- W2: (n_θ, n_φ) = Spin; alle Fermionen (1,1) (051, 202)
- W3: Generationen = fraktale Verzweigungen (018, 149)
- W4: (n,l,j) mehrdeutig → (k_x,k_y,k_z,k_t) primär (005, 006, 042, 202)
- W5: f_i mehrdeutig; Yukawa-Form kanonisch (005, 006, 032)
- W6: Arithmetisch → geometrische Folge q = 2/3 (116, 158, 203, 202)

---

## Neue Dokumente (N)

| ID | Dokument | Status | Datum |
|----|---------|--------|-------|
| N246 | Dok. 246 — RSG und FFGFT: Ein struktureller Vergleich (DE+EN) | **erledigt** | Mai 2026 |
| N247 | Dok. 247 — Information, Zustand und Prozess (DE+EN) | **erledigt** | Mai 2026 |

---

## DE/EN-Symmetrierung (S) — Mai 2026

Übernahme der jeweils längeren Version unter Konsistenzprüfung gegen das Changelog (P7, P8 etc.) bevor Inhalte adoptiert wurden:

### S1 — Dok 009: DE „Schlussfolgerung" → EN „Conclusion"
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | DE → EN |

Vollständige `\section{Conclusion}` aus DE übertragen mit 3 Unterabschnitten (κ=7 nicht angepasst, 10⁻⁴-Begründung, Fundamental Derivation tcolorbox).

### S2 — Dok 175: 8 DE-Unterabschnitte → EN
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | DE → EN |
| Zähler | 32/32 (war 32/24) |

Übernommen:
- "Limits of QND Measurement"
- "Not Restricted to Two States: Infinitely Many Analog Transitions"
- "The Analog Resolution Limit --- and Its Continuation in High-Frequency Technology" (mit großer Frequenz-Tabelle AM bis UV)
- "Above Optics --- Three Regimes up to the Pair-Production Threshold"
- "The Cannonball Limit in FFGFT: Scale Incompatibility of Two Torsion Patterns"
- "The Pair-Production Threshold as Natural Endpoint of the ξ-Ladder"
- "Convergence: Carrier Frequency Meets Internal Transition Frequency on ξ-Level N≈8-9"
- "Restructuring between Levels: When Does It Happen and When Not?"

Konsistenzprüfung: kein Konflikt mit Changelog P7/P8 (keine "Renormierungsgruppe", keine "fraktale Renormierung" als FFGFT-Primitiv); "exakt" nur in Frequenz-Skalen-Kontexten verwendet, nicht in Massen-Genauigkeitsclaims.

### S3 — Dok 022: 5 EN-Sektionen → DE
| Status | **erledigt** | Mai 2026 |
| Übersetzungsrichtung | EN → DE |
| Zähler | 34/34 (war 28/34) |

Übernommen:
- "Die ξ-Anpassungs-Frage: emergent oder ad-hoc?"
- "Lokalität und Bell-Theorem"
- "Anhang: ML-Trainingsdetails (zur Reproduzierbarkeit)"
- "ξ-Anpassungs-Methodik"
- "Vergleichstabelle: T0-Original vs. T0-ML" (inkl. Comparison Table)

Konsistenzprüfung: Lokalitätsabschnitt rahmt T0 als "lokale Modifikation der Erwartungswerte, kein Verstoß gegen lokale Kausalität" — konsistent mit Dok 230 (Z.522-524: Bell als topologische Verbindung, nicht nicht-lokale Korrelation). Historischer Kontext: 022 ist explizit Nov-2025-Addendum, vor Dok 230 (Mai 2026); Sprachgebrauch "lokale verborgene Variablen" ist die ältere Formulierung, in 230 zur "topologischen Verbindung" auf T⁴ reformuliert.

### S4 — Dok 012: 3 DE-Unterabschnitte → EN
| Status | **erledigt** | Mai 2026 |

- "T0 Perspective: G in Two Representations"
- "Document Structure"
- "Connection to the Planck Scale"

### S5 — Dok 013: DE-„Schlussfolgerung" und „Bibliografie" → EN
| Status | **erledigt** | Mai 2026 |

`\section{Conclusion: Geometric Unity}` mit keyresult-Box und finalem Einsichten-fbox; sowie `\section{Bibliography}` als Titel vor existierendem `\begin{thebibliography}`.

### S6 — Dok 014: DE-„Fazit" → EN „Conclusion"
| Status | **erledigt** | Mai 2026 |

Sektion „Conclusion" und Unterabschnitt „Conclusion: The Duality of Geometric Idealization and Physical Measurement" übernommen. Begriff „renormalization" (allgemein) statt „fractal renormalization" — konform mit P8.

### S7 — Dok 042: DE-„Schlussfolgerungen und zukünftige Richtungen" + Bibliografie → EN
| Status | **erledigt** | Mai 2026 |

Section „Conclusions and Future Directions" mit Unterabschnitten „Revolutionary Achievements" und „Final Philosophical Reflection". Bibliografie übersetzt.

### S8 — Dok 046: DE-„Abschließende Bewertung" + Bibliografie → EN
| Status | **erledigt** | Mai 2026 |

Section „Final Assessment" mit „Scientific Status" und „Significance for Fundamental Physics". Bibliografie übersetzt.

### S9 — Dok 133: bidirektional
| Status | **erledigt** | Mai 2026 |

DE → EN: „Multiple Perspektiven auf K_frak" Section mit Perspektiven 1/2/3 (Power Formula, Linearized Form, Ratios are Exact) übersetzt und in EN eingefügt.
EN → DE: „Distinction: Fractal Corrections vs. Rounding Errors" Section + „References" Section übersetzt und in DE eingefügt.

### S10 — Dok 189: DE
| Status | **erledigt** | Mai 2026 |

DE hatte einen Texteditierungs-Artefakt „LATEX" als eigene Zeile nach „Querverweise" — entfernt. Hinzugefügt: `\section{Planck-Größen als Übersetzungsfaktoren}` als Wrapper für „Zwei verschiedene Rollen der Planck-Größen" (war in DE als orphan-Subsection ohne Section, in EN korrekt als Section).

### S11 — Dok 005, 028, 030, 116: jeweils kleine DE-Conclusion fehlte in EN
| Status | **erledigt** | Mai 2026 |

- 005 EN: `\subsection{Conclusion}` zwischen „Connection to Other T0 Documents" und „Detailed Explanation of the Fractal Mass Formula"
- 028 EN: `\section{Conclusion}` zwischen „Hierarchy of ξ-Coupling" und Appendix-Sektion
- 030 EN: `\section{Conclusion}` vor `\begin{thebibliography}`
- 116 EN: `\section{Conclusion}` (mit `\begin{theorem}`-Box) am Dokumentende

---

## Übersichtstabelle — Alle Einträge

| ID | Status | Bemerkung |
|----|--------|-----------|
| K1–K3 | ✓ Mai 2026 | inhaltliche Fehler |
| K4 | ✓ Juni 2026 | Faktor 3 = 3D-Beobachter, nicht fraktale Dispersion (267 DE+EN, 268 DE) |
| K5 | ✓ Juni 2026 | v3-Skript-Audit (Dok. 275): drei Implementierungsfehler in ffgft_hlv_gap_v3.py, betroffene Resultate widerrufen (P. Stoychev, 11. Juni); zuvor irrtümlich als K4 geführt |
| P1–P13 | ✓ Mai 2026 | Präzisierungen |
| P14–P17 | ✓ Juni 2026 | Rotverschiebung, z, H₀, dunkler Sektor |
| P18–P30 | ✓ Juni 2026 | in Dok. 190 konsolidiert (P19→P14, P28→P20); P20/P30 offen, P29 teilw. |
| W1–W6 | ✓ Mai 2026 | Wicklungszahlen |
| N246, N247 | ✓ | neue Dokumente |
| N267, N268 | ✓ Juni 2026 | Kosmologische Entartung (DE+EN); CMB-Peaks aus T⁴ (DE+EN) |
| S1–S11 | ✓ Mai 2026 | DE/EN-Symmetrierung |

---

## Dok 190 Verweise entfernt

| Dokument | Maßnahme |
|---------|---------|
| Dok 013 DE+EN | P13 Inhalt (ξ_UIFT Brückenformel) direkt eingebaut |
| Dok 202 DE+EN | P5, P7 Verweise entfernt |
| Dok 205 DE+EN | P5 Verweise entfernt |
| Dok 243 DE+EN | R12 Verweise ersetzt durch Querverweise auf Dok 022 und 230 |
| Dok 244 DE+EN | R13 Verweise ersetzt durch Querverweise auf Dok 013 |
| Dok 241 DE+EN | Dok 190 und 210 aus Lesepfad-Liste entfernt |

---

## Anhang — Technische LaTeX-Korrekturen (Mai 2026)

| Datei | Korrektur |
|-------|-----------|
| `175_De_ch.tex` Z.1161 | `\textbf{Paarerzeugung.\\ Natürl.~Obergrenze.}` → `\textbf{Paarerzeugung, Natürl.~Obergrenze.}` (das `\\` in `\textbf{}` brach die Tabellenzelle) |
| `244_{De,En}_ch.tex` | Unicode-Mathezeichen außerhalb von Math-Mode ($ℓ$, $ℝ$, $ℤ$, $ℂ$, $ℕ$) durch LaTeX-Befehle ersetzt |
| `244_{De,En}.tex` Wrapper | `\title{}` mit `$L^2(T^4)$` und `$\ell^2(P_N)$` statt Unicode |
| `189_De_ch.tex` | Stray-Text „LATEX" auf eigener Zeile entfernt |
| Diverse EN-Dateien (012, 014, 041, 060) | „Fractal Renormalization" → „Fractal Correction" (P8-konform) |

---

## Anhang — Symmetrie-Status DE/EN

Stand Mai 2026: **alle 31 Dokumentpaare strukturell symmetrisch** (gleiche Anzahl `\section` + `\subsection` in beiden Sprachen). Stichproben des inhaltlichen Gleichlaufs erfolgten gegen das Changelog (Terminologie P7/P8, Formeln K2/K3, Wertangaben P11/P12).

---

## Anhang — Technische Build-Anpassungen (Mai 2026)

Standalone-Präambel auf LuaLaTeX angepasst:
- Babel: `\usepackage[provide=*,german]{babel}` / `[provide=*,english]`
- Schriftarten: `\usepackage{fontspec}` mit `\setmainfont{Latin Modern Roman}`, `\setsansfont{Latin Modern Sans}`, `\setmonofont{Latin Modern Mono}`
- `unicode-math` nicht aktiviert: Konflikt mit `\th` aus dem `physics`-Paket. Mathematik nutzt weiterhin Computer Modern.
- Hinzugefügt: `csquotes`, `fancyhdr`
- T0-Farben definiert (`T0blue`, `T0gray`, `T0green`, `T0red`, `T0orange`) + Lowercase-Aliase für TikZ
- Kurzkommandos als `\providecommand`: `\xipar`, `\xigeom`, `\Kfrak`, `\Tfield`, `\Dfrak`, `\Efield`, `\tT`, `\Lagr`, `\Order`
- Alle Custom-tcolorbox-Environments definiert

**Wrapper:** 28 Wrapper neu erzeugt für Dateien ohne Wrapper im Originalmaterial.

**Ergebnis:** alle 62 PDFs (31 Dokumente × DE/EN) erfolgreich kompiliert.

---

## Nachträgliche Korrekturen (Mai 2026) — Aus Systemprüfung

### P8-Nachkorrektur — Weitere Stellen (Mai 2026)

Die initiale P8-Stichprobe (012, 014, 041, 060 EN) war unvollständig. Systemweite Grep-Prüfung aller 353 ch-Dateien ergab weitere Stellen:

| Datei | Stellen | Maßnahme |
|-------|---------|----------|
| `012_De_ch.tex` | Z.284, Z.452 | `fraktale Renormierung:` → `fraktale Korrektur:` |
| `014_De_ch.tex` | Z.267 `\section`, Z.297 `\subsection`, Z.309 `\caption`, Z.265, Z.278, Z.282, Z.297, Z.330, Z.397 | vollständig ersetzt |
| `014_En_ch.tex` | Z.201, Z.266, Z.270 (2×), Z.279, Z.283, Z.290, Z.300, Z.313, Z.324, Z.386, Z.387, Z.391 | vollständig ersetzt |
| `137_De_ch.tex` | Z.239 Tabellenlabel | `Fractal Renormalization &` → `Fractal Correction &` |
| `137_En_ch.tex` | Z.239 Tabellenlabel (DE-Begriff in EN-Datei) | `Fraktale Renormierung &` → `Fractal Correction &` |

**Gesamtergebnis P8:** alle 353 Dateien geprüft — keine weiteren Stellen außer 190 DE/EN (historischer Bezug, bleibt).

### K2-Erweiterung — 046 DE+EN ebenfalls betroffen

K2 war im Changelog nur für 116 dokumentiert. Systemprüfung ergab:

| Datei | Stellen | Maßnahme |
|-------|---------|----------|
| `046_De_ch.tex` | Z.292 (Tabelle 1), Z.680 (Tabelle 2) | `8/3` → `25/9` (nur Tau-Lepton, nicht Tau-Neutrino) |
| `046_En_ch.tex` | Z.292 (Tabelle 1), Z.694 (Tabelle 2) | `8/3` → `25/9` |

**Kaskade in 116 DE+EN:** r_τ-Änderung erforderte Neuberechnung der Massenverhältnisse:
- m_μ/m_τ: 6/5 → 144/125; 1.2 → 1.152; 0.06126 → 0.05881; 1/16.318 → 1/17.0; Abw. < 3% → < 1.2%
- m_e/m_τ: 1/2 → 12/25; 0.5 → 0.48; 0.0002856 → 0.000283; 1/3501 → 1/3534; Abw. < 0.7% → < 1.6%
- Listenpunkt: „kompensieren exakt zu Q = 2/3" → „sind konsistent mit Q ≈ 2/3" (auch P6-konform)

**Tau-Neutrino-Einträge (8/3) bleiben** — eigenständiger Wert, kein r_τ.

> ⚠️ **Überholt durch K2-Nachtrag (27. Mai 2026, siehe unten):** Diese Festlegung wurde revidiert. Dok. 190 (K2-Status, 26. Mai) und die korrigierte 046-DE-Rechnung setzen ν_τ ebenfalls auf 25/9 (ξ_ντ = 400/81). Maßgeblich ist der neue Eintrag „K2-Nachtrag — vollständige Einarbeitung".

### Erledigt DE | ✓ Mai 2026 — Erledigt EN | ✓ Mai 2026

---

## Layout-Korrekturen (Mai 2026) — Umbrüche und Tabellenbreiten

**Anlass:** Nach den Terminologie- und Zahlenkorrekturen (P8, K2) traten Overfull-hbox-Warnungen auf. Alle 13 korrigierten Dokumente wurden rekursiv bereinigt bis 0 Fehler und 0 hbox-Warnungen.

### Maßnahmen je Dokument

| Datei | Maßnahme |
|-------|---------|
| `014_De_ch.tex` | 3 Tabellen mit `\resizebox{\textwidth}{!}` eingerahmt (`p{3cm}p{10cm}`, `p{4cm}p{10cm}`, `p{3.5cm}p{6cm}p{6cm}`); unnötigen Artikel „die" aus Subsektions-Titel entfernt |
| `014_En_ch.tex` | Gleiche 3 Tabellen; align-Zeilen gekürzt (Formel + Text) |
| `046_De_ch.tex` | `longtable` → `tabular` + `\resizebox`; 5 weitere `tabular`-Umgebungen (`p{3cm}p{4cm}p{4cm}p{3cm}`, `lcccccc`, `lcccc`, `lccc`) eingerahmt |
| `046_En_ch.tex` | Gleiche Maßnahmen |
| `012_De_ch.tex` | `lcc`-Tabelle mit `\resizebox` eingerahmt |
| `012_En_ch.tex` | Gleiche Maßnahme |
| `041_De_ch.tex` | 5 Tabellen mit `\resizebox`; Extra-`}`-Klammer aus `{\small…}`-Rest bereinigt; Formel-Spalte von `p{2.7cm}` → `p{3.5cm}` (Weinberg-Formel); `\hfuzz=10pt` gesetzt |
| `041_En_ch.tex` | Longtables → tabular + `\resizebox`; zweite Hierarchie-Tabelle in `table`-Float; Formel-Spalte angepasst |
| `137_De_ch.tex` | `\scalebox{0.8}` → `\scalebox{0.65}` |
| `137_En_ch.tex` | `\scalebox{0.8}` → `\scalebox{0.55}` |
| `116_De_ch.tex` | `\allowdisplaybreaks` vor ersten `align`-Block |
| `116_En_ch.tex` | `\allowdisplaybreaks` vor ersten `align`-Block |
| `060_De_ch.tex` | Keine Layout-Änderungen nötig (war bereits sauber) |

**Ergebnis:** 13/13 Dokumente kompilieren fehlerfrei (0 LaTeX-Fehler, 0 Overfull-hbox).

### Hinweis: Innötige Textzusätze bereinigt

Durch die Terminologie-Korrekturen waren einzelne Zeilen geringfügig länger geworden:
- `\subsection{Warum ist die fraktale Korrektur…}` → Artikel „die" entfernt (wie im Original ohne Artikel)
- align-Zeilen in 014 EN mit langen SI-Werten auf kompaktere Darstellung gekürzt

---

## Integration der Layout-Korrekturen in Kindle 6×9 Build (Mai 2026)

### Maßnahmen

1. **Übernahme der 13 korrigierten `_ch.tex`-Dateien** mit allen Terminologie-, Zahlen- und Inhaltsverbesserungen (P8 strenger durchgesetzt: „Renormierung" → „Korrektur" auch in 014; K2-Kaskade in 046 und 116 vollständig).

2. **Korrektur Datei-Vertauschung 137 De/En**: Die hochgeladenen Dateien hatten die Sprachen vertauscht (`137_De_ch.tex` enthielt englischen Inhalt, `137_En_ch.tex` deutschen). Inhalte wurden getauscht, sodass `137_De_ch.tex` nun deutschen Text enthält („Das jahrhundertealte Rätsel") und `137_En_ch.tex` englischen Text („The Century-Old Enigma").

3. **Entfernung redundanter `\resizebox`-Wrapper um Tabellen**: 48 manuell ergänzte `\resizebox{\textwidth}{!}{\begin{tabular}…}`-Hüllen wurden entfernt, da der `\BeforeBeginEnvironment{tabular}{adjustbox}`-Hook im Preamble bereits automatisch alle `tabular`-Umgebungen auf Textbreite skaliert. Doppel-Skalierung hätte Tabellen unleserlich klein gemacht.
   - Auch verschachtelte `\resizebox`-in-`\resizebox`-Strukturen (z.B. 014) wurden iterativ aufgelöst.
   - In 060 wurden `\resizebox{\linewidth}`-Varianten gleichbehandelt.

4. **Wrapper-Format**: Alle 13 `_wrapper.tex`-Dateien des Users hatten `\documentclass[12pt,a4paper]{report}`. Auf Wunsch des Users für einheitliches Kindle 6×9-Format umgestellt auf `\documentclass[11pt]{report}` (Geometrie aus dem Preamble).

5. **Neue Wrapper für 137 De/En** mit korrekten Titeln und Autorenangabe erstellt.

### Ergebnis

| Metrik | Vorher (User-Uploads A4) | Nachher (integriert Kindle 6×9) |
|---|---|---|
| Dokumentpaare | 31 (62 Dateien) | 32 (64 Dateien, +137) |
| Seitenformat | gemischt (13× A4, 49× Kindle) | **konsistent Kindle 6×9** |
| Tabellen-Skalierung | manuell `\resizebox` | **automatisch via Hook** |
| Overfull-Boxen über alle 64 PDFs | n/a (gemischt) | **14 gesamt, 2 davon > 5 mm** |

### Stichproben

- `137_De.pdf`: 13 Seiten, deutscher Inhalt, Kindle 6×9 (432×648 pt)
- `137_En.pdf`: 13 Seiten, englischer Inhalt, Kindle 6×9
- `041_De.pdf`: 36 Seiten, 0 Overfull
- `046_En.pdf`: 19 Seiten, 0 Overfull (war 139 pt vor Korrektur)
- Alle 13 geänderten Dokumente: **0 Overfull-Boxen** nach Integration


---

## Inhaltliche Prüfung der 147 weiteren Dokumente (Mai 2026)

Nachdem die ursprünglichen 31 Dokumentenpaare durchgearbeitet waren, wurden die verbleibenden 147 Dokumentenpaare (= 294 _ch.tex-Dateien) systematisch gegen die Changelog-Korrekturen K1–K3, P5–P12, W1–W6 geprüft.

### Methodik

Regulärer-Ausdrucks-Scan auf typische Verletzungsmuster:
- **K1**: `64π⁴`-Vorfaktor in ξ-Formeln
- **K2**: `r_τ = 8/3` Tau-Yukawa
- **K3**: `a_e = 4π/(f·k_geom)` Elektron-g-2-Basisformel
- **P7**: „Renormierungsgruppe" / „renormalization group" als FFGFT-Primitiv
- **P8**: „Fraktale Renormierung" / „fractal renormalization" als Eigenbegriff
- **P9**: `N_c = 3` direkt mit „Farbladungen" gleichgesetzt
- **P10, P12**: Numerische Sonderwerte (K=245, CHSH 5·10⁻⁴)

### Befund

**5 Dokumente bedurften Korrektur (von 147):**

| Dokument | Verletzung | Maßnahme |
|---|---|---|
| `086_T0_Dokumentenuebersicht_En_ch.tex` | P7: Bullet „Renormalization group as flow in parameter space" als FFGFT-Eigenschaft | → „Scale structure as flow on the recursion $\mathcal{R}$ in parameter space" |
| `091_Casimir_De_ch.tex` | P7: „RG-Aspekt: … besitzt die Theorie eine RG-Struktur ähnlich der QFT" | → „Skalenstruktur: … folgt in FFGFT aus der Rekursion $\mathcal{R}$ (Dok.~202/203) und ist nicht das Ergebnis eines Renormierungsverfahrens; sie ist in ihrer Wirkung der Renormierungsgruppe der QFT vergleichbar." |
| `091_Casimir_En_ch.tex` | P7: gleiche Stelle EN | → analog mit „comparable in effect to the renormalization group" |
| `124_Unit_Charge_En_ch.tex` | P8: „stabilized by fractal renormalization" | → „stabilized by fractal correction" |
| `038_Markov_En_ch.tex` | P8: „Fractal renormalization $\prod_{n=1}^{137}$..." | → „Fractal correction $\prod_{n=1}^{137}$..." |
| `160_T0_Lepton-Lebensdauer-Verh_De+En_ch.tex` | P9: 4 Stellen „$D = N_c = 3$: räumliche Dimensionen = Farbladungen/Farbwindungen" | → „$D = 3$ (SM-Korrespondenz: $N_c = 3$)" |

### Als OK eingestuft (141 von 147)

**Beispiele für vertretbare Verwendung von Renormierungs-Begriffen:**

- `019_T0_lagrndian`: Section-Header lautet bereits **„Renormierung (historische Darstellung)"** mit explizitem **Hinweis-Block** am Anfang: „Dieser Abschnitt verwendet die Sprache der QFT-Renormierung … als Beschreibungsmittel. In der vollständigen FFGFT-Formulierung (Dok.~202) ist traditionelle Renormierung nicht erforderlich". Damit ist die nachfolgende Subsection `\subsection{Renormierungsgruppen-Gleichungen}` durch den Section-Scope abgedeckt.

- `057_RelokativesZahlensystem`: `\subsection{Renormierungsgruppenfluss}` steht innerhalb von `\section{Physikalische Analogien und Anwendungen}` und beginnt mit „Eine bemerkenswerte Parallele besteht zwischen relationaler Komposition und dem Renormierungsgruppenfluss". Damit ist Analogie-Charakter explizit.

- `181_T0_Torus_Begruendung`: „AS sucht UV-Fixpunkt als Ergebnis des Renormierungsgruppen-Flusses. **In T0 gibt es keinen Renormierungsgruppen-Fluss** — $\xi$ ist eine geometrische Konstante." → Klare Kontrastierung.

- `202_FFGFT_Feldtheorie_Gesamt`: Hat explizite **„Anmerkung zur Begrifflichkeit Renormierungsgruppe"** mit Verweis, dass in FFGFT die Skalenstruktur aus der Rekursion $\mathcal{R}$ folgt.

- `205_FFGFT_Narrativ`: Beschreibt RG explizit als SM-Konzept und kontrastiert mit FFGFT.

- `242_Skalenleiter`: RG wird als „nächster Verwandter zu einer skalenübergreifenden Erklärung" eingeführt und kritisiert (RG läuft vertikal, FFGFT erklärt formative Übergänge).

**Spezialfall 018_T0_Anomale-g2_10/11/12 (kein K3-Verstoß):**

Die Basisformel für $a_e$ in 018 lautet bereits korrekt $a_e = (S_3/f)/k_\text{geom}$ mit $S_3 = 2\pi^2 = 19{,}739$ (gemäß K3). Die in der Differenzformel `Δa(μ−e) = 4π/f^(5/3)` erscheinende $4\pi$-Konstante ist nicht $a_e$, sondern die Myonen-Basisgröße $a_\mu \approx 4\pi/f^{5/3}$ (Myon und Tau verwenden weiterhin $4\pi$ gemäß Dok.~190 Gl.~190.5/190.6). $a_e$ ist in dieser Differenz vernachlässigbar klein und wird im rechten Ausdruck implizit weggelassen. Mathematisch korrekt.

### Status

| ✓ | Erledigt DE | Mai 2026 |
| ✓ | Erledigt EN | Mai 2026 |


### Kompilation der korrigierten Dokumente

Alle 5 Dokumente (10 Dateien: De+En) wurden im Kindle 6×9-Format (432×648 pt) erfolgreich kompiliert:

| Dokument | Seiten | Overfull-Boxen |
|---|---|---|
| 086_T0_Dokumentenuebersicht De/En | 8 / 8 | 0 / 0 |
| 091_Casimir De/En | 22 / 21 | 2 / 1 (alle < 4mm) |
| 124_Unit_Charge De/En | 5 / 5 | 0 / 0 |
| 038_Markov De/En | 8 / 7 | 0 / 0 |
| 160_T0_Lepton-Lebensdauer-Verh De/En | 12 / 11 | 0 / 0 |

**Zusätzliche Layout-Korrektur 091:** Die 11 longtables mit Spaltenbreiten `p{1cm} p{8cm} p{3cm}` bzw. `p{2cm} p{8cm} p{3cm}` (Gesamt 12-13 cm) überstiegen die Kindle-Textbreite von 12,04 cm. Reduziert auf `p{1cm} p{7cm} p{2.5cm}` bzw. `p{1.5cm} p{6.5cm} p{2.5cm}` mit `\raggedright\arraybackslash`. Verbleibende Überstände < 4 mm.

**Wrapper 124 De/En:** Neu erstellt (existierten zuvor nicht), Titel „Die Elektronen-Einheitsladung in T0: Geometrische Auflösung von Punkt-Singularitäten" / „The Electron Unit Charge in T0: Geometric Resolution of Point Singularities".

---

## Vollständige Kompilation aller Dokumente (Mai 2026)

Nach der Inhaltsprüfung der 147 weiteren Dokumente und der Anwendung der 6 erforderlichen P7/P8/P9-Korrekturen wurden alle Dokumente der Sammlung im Kindle 6×9 Format neu kompiliert.

### Ergebnis

| Metrik | Wert |
|---|---|
| Kompilierte PDFs total | **341** |
| Davon im Kindle 6×9 Format (432×648 pt) | **341** (100%) |
| Dokumentpaare (DE+EN) | 168 + 5 inline-Dokumente |
| Overfull-Boxen total | 350 (∅ 1,0 pro PDF) |
| Davon > 5 mm (15 pt) | 167 |
| Davon > 15 mm (45 pt) | wenige Spezialfälle in Math-Tabellen |

### Behobene Wrapper-Probleme

Bei der Kompilation der weiteren ~270 Dokumente traten verschiedene Wrapper-Inkonsistenzen auf, die alle behoben wurden:

| Anzahl | Problem | Lösung |
|---|---|---|
| 17 | Wrapper nutzten `T0_preamble_local_De/En` (xelatex+DejaVu) | Umgestellt auf `T0_preamble_standalone_De/En` (lualatex+Inter) |
| 8 | Wrapper hatten `\input{NAME_ch}` ohne `../ch/` Pfad | Pfad ergänzt |
| 6 | Wrapper hatten `\input{T0_preamble_standalone_De}` ohne `../pri-end/` Pfad | Pfad ergänzt |
| 2 | Wrapper hatten `\input{pri-end/...}` oder `\input{ch/...}` ohne `../` | `../` ergänzt |
| 1 | 161_T0_Ising_Machine_En: defekter Wrapper ohne `\documentclass` | Neu erstellt |
| 1 | 186_FFGFT_Photonik_Analyse: defekter `\title{}` (kein schließendes `}`) | Neu erstellt |
| 3 | Inline-Dokumente (Adaptive, Fruehe, 192) mit A4-Geometrie | Auf Kindle 6×9 umgestellt |
| 2 | 210 De/En: eigene `\geometry{paperwidth=210mm,…}` Block | Block entfernt (Preamble übernimmt) |
| 1 | 186: `\usepackage{geometry}\geometry{margin=2.5cm}` | Block entfernt |
| 2 | 172 De/En: `avipost` und `response` Umgebungen undefiniert | tcolorbox-Definitionen in Wrapper ergänzt |

### Behobene Preamble-Erweiterungen

Für PDF-Bookmark-Erzeugung (hyperref-Kompatibilität mit unicode-math-Symbolen) wurden ergänzt:

```latex
\pdfstringdefDisableCommands{
  % ... bestehende Einträge ...
  \def\varphi{phi}
  \def\mitvarphi{phi}
  \def\Phi{Phi}
  \def\mitPhi{Phi}
  \def\leftrightarrow{<->}
  \def\Leftrightarrow{<=>}
}
```

### Entfernte Duplikate

Folgende Wrapper waren Duplikate ohne eigene `_ch.tex`-Datei und wurden entfernt:
- `189_T0_TorusAbleitung_De/En.tex` (Duplikat von `189_TorusAbleitung_De/En.tex`)
- `160_T0_Lepton-Lebensdauer-Verhaeltnisse-1_De/En.tex` (Duplikat von `160_T0_Lepton-Lebensdauer-Verh_De/En.tex`)
- `167_T0_LiNbO3_xi_Geometrie_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `187_T0_FFGFT_Photonik_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `188_T0_Geometrie_Grundlagen_En.tex` (kein `_ch.tex` vorhanden, nur DE)
- `207_tex.tex` (Streufile)
- `T0_preamble_local_De/En.tex` (waren irrtümlich im Wrapper-Ordner)

### Status

| ✓ | Erledigt | Mai 2026 |

Alle 341 PDFs im einheitlichen Kindle 6×9 Format verfügbar.


---

## Übersetzungen unvollständiger Sprachpaare (Mai 2026)

Nach der vollständigen Kompilation wurde geprüft, welche Dokumente nur in einer Sprache vorlagen. Für diese wurde eine vollständige Übersetzung erstellt.

### Identifizierte Lücken (initial)

| Doc | Status vorher |
|---|---|
| 187_T0_FFGFT_Photonik | nur DE (32 KB, 755 Zeilen) |
| 188_T0_Geometrie_Grundlagen | nur DE (23 KB, 558 Zeilen) |

(167_T0_LiNbO3 hat bereits beide Sprachen unter verschiedenen Namen: `167_..._Geometrie_De` und `167_..._Geometry_En`.)

### Erstellte Übersetzungen

**188_T0_Geometrie_Grundlagen_En:** „Geometric Foundations of FFGFT — From the Phase Condition to Circle, Polygon, Spiral, and Nature's Preferred Ratios"

Vollständige Übersetzung des deutschen Dokuments. Inhalt: universelle Phasenbedingung, reguläre Polygone, Z3-Symmetrie, n=6 hexagonale Packung, Kreis als Grenzfall, logarithmische Spirale, Goldener Schnitt $\phi$ als optimales inkommensurables Verhältnis, Fibonacci-Folge, abgeleitete FFGFT-Formeln ($\alpha = \phi^{-1}$, $1/n^2$-Spektrum, Leptonmassen-Leiter, $\alpha_\text{EM}$), Block-Copolymer DSA unter der Wellenlängengrenze.

- 21,7 KB, 557 Zeilen
- PDF: 15 Seiten, Kindle 6×9, 0 Overfull-Boxen

**187_T0_FFGFT_Photonik_En:** „FFGFT Analytics: Mathematical Foundations — Fractal Feedback and Matrix Translation in the 4D Phase Torus"

Vollständige Übersetzung des deutschen Dokuments. Inhalt: fundamentale Frequenz $\xi = 7500/t_P$, 4D-Phasen-Torus (Abgrenzung vom 3D-Torus), fraktale Rückkopplung und Einrast-Mechanismus, Matrix-Translation, 4D-Torus-Faltung, TFLN-Photonik als Hardware-Transduktion, B-Meson-Anomalien (LHCb 4,0σ), sub-plancksche Cut-off-Skalen (OLQEM, EFT), testbare Vorhersagen.

- ~32 KB, ~750 Zeilen
- PDF: 18 Seiten, Kindle 6×9, 0 Overfull-Boxen

### Status

| ✓ | Erledigt | Mai 2026 |

**Endstand:** Alle 173 Dokumente verfügbar in DE+EN (außer 192_Adaptive, Adaptive, Fruehe — sind inline Dokumente ohne DE/EN-Trennung).


---

## Fix für 192_T0_Algebraische_Kompositionsgrenzen (Mai 2026)

Bei der Analyse von Johann's älteren PDF-Dateien (pdf.zip) wurde entdeckt, dass das Dokument 192_T0_Algebraische_Kompositionsgrenzen einen Build-Fehler hatte:

**Problem:**
Die ch.tex-Dateien `192_T0_Algebraische_Kompositionsgrenzen_De_ch.tex` und `192_T0_Algebraische_Kompositionsgrenzen_En_ch.tex` waren in der Sammlung vorhanden, hatten aber keine entsprechenden Wrapper. Stattdessen referenzierte der Wrapper `192_Adaptive_Hybridarchitektur_Pascher.tex` einen völlig anderen Inhalt (Adaptive Hybridarchitektur — ein eigenständiges inline-Dokument).

**Lösung:**
Zwei neue Wrapper erstellt:

- `192_T0_Algebraische_Kompositionsgrenzen_De.tex`
  - Titel: „Algebraische Kompositionsgrenzen in FFGFT"
  - PDF: 9 Seiten, Kindle 6×9, 0 Overfull-Boxen

- `192_T0_Algebraische_Kompositionsgrenzen_En.tex`
  - Titel: „Algebraic Composition Limits in FFGFT"
  - PDF: 8 Seiten, Kindle 6×9, 0 Overfull-Boxen

**Inhalt des Dokuments:**
Behandelt Kompositionsgrenzen zwischen algebraischen Strukturräumen in FFGFT. Zentrale These: Wenn FFGFT-Terme ($m_\ell = r_\ell \cdot \xi^{p_\ell} \cdot v$) in Formeln aus fremden algebraischen Kontexten (z. B. Koide-Relation, SM-Streuamplituden) eingesetzt werden, entstehen strukturfremde Kreuzterme — ein Kategorienfehler, kein numerisches Problem.

Das Dokument `192_Adaptive_Hybridarchitektur_Pascher.tex` bleibt als eigenständiges inline-Dokument bestehen (Adaptive Hybridarchitektur für CIM-Systeme).

### Status

| ✓ | Erledigt | Mai 2026 |


---

## Eigenständige PDFs in Sammlung integriert (Mai 2026)

Aus den älteren PDFs (pdf.zip vom 18.5.2026) wurden eigenständige Dokumente identifiziert,
die nur als PDF vorlagen (keine ch.tex-Quelldateien). Diese wurden mit alternativem
Nummernpräfix (Suffix `a`) in die Sammlung integriert.

### Strategie: Option A — PDF einbetten

Da die ch.tex-Quellen für diese Dokumente fehlen und eine Rekonstruktion aus dem PDF
(Gleichungen, Tabellen, Bilder) nicht zuverlässig möglich ist, werden die Original-PDFs
unverändert in `pdf_originals/` abgelegt und über minimale Wrapper mittels
`\includepdf` eingebettet. Das Original-Layout bleibt EXAKT erhalten und wird auf
Kindle 6×9 (432×648 pt) skaliert.

### Integrierte Dokumente

| Wrapper | Inhalt | Original-Datum | Seiten | Original-Größe |
|---|---|---|---|---|
| `060a_Musikalische_Spirale_137_De/En.tex` | „Die Musikalische Spirale und die 137" — Resonanzpunkt $(4/3)^{137} \approx 257$ als Quelle der Feinstrukturkonstante | 17./20. Feb 2026 | 8/7 | 594×792 |
| `144a_Asymmetrie-Master_De/En.tex` | „FFGFT: Asymmetrie-Analyse Teil 1 und 2" (vollständig, im Gegensatz zu `144_Asymmetrie-teil2` das nur Teil 2 enthält) | 23. Feb 2026 | 21/19 | 432×648 (bereits Kindle) |
| `170a_Analog_Gehoer_De/En.tex` | „Analog-Gehör" — eigenständiges Akustik-Dokument | 4. März 2026 | 16/16 | A4 |
| `186a_FFGFT_Photonik_Hardware_De/En.tex` | „FFGFT and Photonic Hardware" — eigenständiges Hardware-Dokument (im Gegensatz zu `186_FFGFT_Photonik_Analyse` „Mathematical Foundations") | 4. Mai 2026 | 14/14 | A4 |
| `006a_Teilchenmassen_2025_De/En.tex` | „T0-Modell: Vollständige parameterfreie Teilchenmassen-Berechnung" — historische Vorläufer-Version | **29. Nov 2025** | 15/14 | A4 |

### Verzeichnisstruktur

```
pdf/                        — kompilierte PDFs (jetzt 356, alle Kindle 6×9)
pdf_originals/              — Original-PDFs für die 10 standalone Wrapper (NEU)
ch/                         — ch.tex Quelldateien (unverändert, 348 Stück)
wrapper/                    — Wrapper-Dateien (356 jetzt: 346 Standard + 10 standalone)
pri-end/                    — Preamble (unverändert)
```

### Bücher

Die folgenden PDFs sind eigenständige Buchprojekte und werden NICHT in die Sammlung
aufgenommen (Quelldateien existieren beim Autor lokal in separaten Verzeichnissen):
- `Von_Alpha1_zur_vollstaendigen_Physik_De/En.pdf` (105 Seiten)
- `Xi_Narrative_Master-ebook_De/En.pdf` (354/325 Seiten)
- `FFGFT_Narrative_Master_De/En.pdf` (251/254 Seiten)

### Nicht enthalten

- `T0_170b_Gehoer_De/En.pdf` — vom Autor lokal gelöscht

### Status

| ✓ | Erledigt | Mai 2026 |

**Endstand der Sammlung:** 356 PDFs (vorher: 346 + 10 eigenständige)


---

## Bereinigung der Datei-Präfixe (Mai 2026)

User-Anforderung: Jedes Dokument muss mit Zahl-Präfix beginnen, und kein Präfix darf doppelt vorkommen (außer DE/EN-Paaren).

### Behobene Probleme

| Alter Name | Neuer Name | Grund |
|---|---|---|
| `dok206_dreieck_matrix_reduktion_De/En` | `206_dreieck_matrix_reduktion_De/En` | "dok"-Präfix entfernt, jetzt rein numerisch |
| `dok207_bewusstsein_bruecken_De/En` | `207_bewusstsein_bruecken_De/En` | "dok"-Präfix entfernt |
| `Adaptive_Hybridarchitektur_Pascher` | `208_Adaptive_Hybridarchitektur_Pascher` | Zahl-Präfix hinzugefügt |
| `Fruehe_digitale_Spuren_Pascher` | `209_Fruehe_digitale_Spuren_Pascher` | Zahl-Präfix hinzugefügt |
| `192_Adaptive_Hybridarchitektur_Pascher` | **gelöscht** | Duplikat von `Adaptive_Hybridarchitektur_Pascher` (gleicher Hash) — war versehentlich von mir mit 192-Präfix kopiert worden |
| `1_T0_Introduction_De/En` | `001b_T0_Introduction_De/En` | Einstellig → 3-stellig, Suffix `b` zur Unterscheidung von `001_T0_Book_Abstract` und `001a_T0_Book_Abstract` |
| `023a_Bell-video_De/En` | `023b_Bell-video_De/En` | `023a` war doppelt belegt (Bell-Teil2 + Bell-video). Bell-Teil2 behält `023a`, Bell-video bekommt `023b` |
| `060a_Musical_Spiral_137_De.pdf` (altes Testfile) | **gelöscht** | Alter Testbuild aus früherer Session, durch `060a_Musikalische_Spirale_137_De` ersetzt |

### Endkontrolle

- ✓ Alle 355 Wrapper beginnen mit numerischem Präfix
- ✓ Kein Wrapper mit "dok"-Präfix mehr
- ✓ Keine wirklichen Duplikate (alle Präfix-Doppelungen sind DE/EN-Paare des gleichen Dokuments)
- ✓ Alle Wrapper-Referenzen auf ch.tex-Dateien aktualisiert
- ✓ Alle 8 betroffenen Dokumente neu kompiliert

### Endstand

| Komponente | Anzahl |
|---|---|
| Wrappers | 355 |
| Kompilierte PDFs | 355 (alle Kindle 6×9) |
| ch.tex Quelldateien | 348 |


---

## Neue Arbeiten (Mai 2026) — Session „Natürliche Einheiten & Informationseinheit"

### N261 — Dok. 261: Statische Geometrie und SI-Projektion
| Feld | Inhalt |
|------|--------|
| Dokument | Dok. 261 — „Statische Geometrie und SI-Projektion: Warum natürliche Einheiten keine fraktalen Korrekturen brauchen" (EN: „Static Geometry and the SI Projection: Why Natural Units Require No Fractal Corrections") |
| Status | **erledigt** (DE+EN) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |
| Präfix-Hinweis | 261 gewählt (260 existiert nur als PDF) |
| Format | Kindle 6×9 (432×648 pt); DE 11 S., EN 11 S. |

**Inhalt (9 Abschnitte):** Einordnung; Rahmenabschnitt „Kompaktifizierte Zeit: statisch und vollständig — der Pfeil macht dynamisch"; drei Umrechnungstabellen (SI-fixierte Konstanten / Größenumrechnung ℏ=c=k_B=1 / dimensionslose Inputs → ξ); statische Korrekturfreiheit; dynamische Realität von c, ℏ, ε₀ im Zeitfluss; Konsequenz G und α als dynamische Kopplungen; Demarkation aus Lagrange-Sicht.

**Kernthese:** Solange in natürlichen Einheiten und reinen Verhältnissen gerechnet wird, ist die Beschreibung statisch und korrekturfrei (Schicht 1, kompaktes T⁴, eingefrorene Rekursion). c, ℏ, ε₀ werden erst bei Dekompaktifizierung der intrinsischen Zeit-Wicklung T̃ in die Pfeilzeit t real (Schicht 2, Einbettungspreis). G und α sind keine statischen Grundkonstanten, sondern dynamische Kopplungen.

**Quellengrundlage (verifiziert):** 011 (α=ξ·(E₀)²), 012/127/133 (G, K_frak), 013/014 (SI-Projektion, S_T0), 041 (Weinberg α_W=√ξ, θ₁₃), 116 (Koide, Leiter), 078 (zwei Zeiten T̃ vs t), 134 (c=L/T), 181 (ℝ³×S¹, r₄=L₀), 185 (Einbettungspreis), 230 (T⁴=T³×S¹, Zeit-Wicklung), 241 (Schicht 1/2, eingefrorene Rekursion), 019/049/067/095/180 (Lagrange-Begründung).

**Konsistenzprüfung:** P8-konform („fraktale Korrektur", nicht „Renormierung"); K2-konform (r_τ=25/9, Tabelle 3); P6/Nichtabschluss-konform (Koide Q=2/3 als Folge der Exponenten, nicht nachträglich gefittet); Korrekturen als abgeleitete Projektionsfaktoren dargestellt (Dok 133/258/193).

**Offen / nachzutragen:** compile_all.py-Eintrag (Muster `^261_` greift, sobald ch-Dateien im Verzeichnis liegen); optionale Querverweise aus 013/078/134/185/230/241 auf 261 (Einzeiler vorbereitet, noch nicht in die Zieldokumente eingesetzt).

---

### N013-INFO — Dok. 013: Abschnitt „Statische und dynamische Informationseinheit"
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 013 (DE+EN), neuer Unterabschnitt nach dem ξ_FFGFT/ξ_UIFT-Vergleich (P13) |
| Status | **erledigt** (DE+EN) |
| Eingetragen | Mai 2026 |
| Erledigt DE | ✓ Mai 2026 |
| Erledigt EN | ✓ Mai 2026 |

**Anlass:** Wiederaufnahme der Frage „Wie viel Energie entspricht der kleinsten Informationseinheit?". Frühere Aussage: keine universelle Einheit, längenabhängig (Dok 184: E_N = ℏc/L_N; Landauer k_B T ln2).

**Inhalt:** Trennung von *Information als Energie* (Schicht 2, dynamische Projektion, skalenabhängig — k_B T bzw. ℏc/L) und *Information als Zählung* (Schicht 1, statisch: die dimensionslose, ganzzahlige Windungszahl auf dem kompakten Torus). Der Vopson-Faktor ξ_FFGFT/ξ_UIFT ≈ 414.684 wird als Projektionsverhältnis zwischen einer Schicht-2- und einer Schicht-1-Informationsgröße gedeutet.

**Quellengrundlage:** 181 (Windungszahlen), 184 (Energiehierarchie E_N=ℏc/L_N, Landauer-Grenze, „ξ-Geometrie bestimmt Dynamik, nicht Zustandsraumgröße"), 185 (Einbettungspreis), 261 (statisch/dynamische Demarkation).

**Querbezug (keine Dopplung):** Dok 247 („Information, Zustand und Prozess") behandelt bereits Zustand vs. Prozess (Speicherung energieneutral, Landauer nur für Löschung). Der 013-Einschub wendet diese Logik speziell auf den Vopson-Vergleich an und ergänzt die Schicht-Lesart; er ersetzt 247 nicht.

**Layout:** align-Block in der „Energie pro Bit"-Box auf gestapelte Darstellung umgestellt (Formel und Klammer-Erläuterung getrennt), damit kein Überlauf in der Kindle-6×9-Box entsteht.

---

### Übersichtstabelle — Nachtrag

| ID | Status | Bemerkung |
|----|--------|-----------|
| N261 | ✓ Mai 2026 | neues Dokument (9 Abschnitte, DE+EN, Kindle 6×9) |
| N013-INFO | ✓ Mai 2026 | Erweiterung Dok 013 (statische/dynamische Informationseinheit) |

---

## K2-Nachtrag — vollständige Einarbeitung (27. Mai 2026)

**Anlass:** Dok. 190 meldete im K2-Statusabschnitt (Nachtrag 26. Mai) verbliebene 8/3-Reste in Dok. 016, 046 und 116. Eine eigene Vollprüfung bestätigte dies und fand **zusätzlich** übersehene Reste in **046 DE** (abgeleitete Werte), die Dok. 190 nicht nennt.

**Soll-Stand (Dok. 190 maßgeblich):** r_τ = 25/9 · m_τ = 1783,4 MeV · Abw. +0,37 % · ξ_ντ = 400/81 ·10⁻⁸ · E_ντ = 18,0 meV · ν_τ-Zeilen 25/9.

### Befund und Durchführung

| Datei | Stelle | Vorher | Nachher | Status |
|-------|--------|--------|---------|--------|
| 046 DE | Ergebnistabelle ν_τ (Verträglichkeit) | 18,8 meV | 18,0 meV | ✓ |
| 046 DE | Methodenäquivalenz, Tau-Zeile r_i | 2,768 | 2,778 (=25/9) | ✓ |
| 046 DE | Methodenäquivalenz, ν_τ-Zeile | 18,8·10⁻⁶ / 2,768 | 18,0·10⁻⁶ / 2,778 | ✓ |
| 046 DE | Falsifikationstab. m_{ν_τ} | 18,8 meV | 18,0 meV | ✓ |
| 016 EN | Massentab., Tau-Zeile | 8/3 · 1712,1 · 3,64 | 25/9 · 1783,4 · 0,37 | ✓ |
| 016 EN | r-Parameter-Liste | …, 8/3, … | …, 25/9, … | ✓ |
| 046 EN | ν_τ-Parameterzeile (Tab. 1) | 8/3 & 8/3 | 25/9 & 25/9 | ✓ |
| 046 EN | ξ_ντ-Rechnung | 8/3 → 128/27 | 25/9 → 400/81 | ✓ |
| 046 EN | E_ντ (3 Stellen) | 18,8 meV | 18,0 meV | ✓ |
| 046 EN | Methodenäquivalenz Tau + ν_τ | 2,768 | 2,778 | ✓ |
| 046 EN | ν_τ-Zeile (Tab. 2) | 8/3 & 8/3 | 25/9 & 25/9 | ✓ |
| 116 EN | Leptonparameter-Tab., Tau-Zeile | 8/3 | 25/9 | ✓ |

**Hinweis zur ursprünglichen K2-Eintragung:** Diese nannte nur Dok. 116; die K2-Erweiterung ergänzte 046. Tatsächlich betroffen waren **016, 046 (DE+EN) und 116 EN**. DE von 016/116 war bereits korrekt; 046 DE hatte nur in den *abgeleiteten* Tabellen Reste (Hauptrechnung war korrekt).

### Richtungsentscheidung Tau-Neutrino

Die frühere Festlegung „ν_τ bleibt 8/3" (K2-Erweiterung) ist **revidiert**. Dok. 190 (26. Mai) und die korrigierte 046-DE-Rechnung setzen ν_τ auf 25/9 (ξ_ντ = 400/81, E = 18,0 meV). Maßgeblich ist Dok. 190 als jüngster Stand.

### Verifikation

- Korpusweite Restsuche (8/3, 128/27, 1712, 18.8, 2.768, 3.64) in allen vier Dateien: **0 Treffer**.
- Tabellen-Spaltenzahl der geänderten Zeilen unverändert (keine zerbrochenen Tabellen); keine fehlerhaften Escapes.
- Neu kompiliert (Kindle 6×9, 432×648 pt): 016 EN (13 S.), 046 DE (20 S.), 046 EN (17 S.), 116 EN (9 S.) — fehlerfrei.

### Offen / Hinweise

- **Versionslage:** Diese EN-Korrekturen liegen **nach** dem v1.1.1-Release (23. Mai, DOI 20355305, „No existing derivations changed"). Das Zenodo-Archiv v1.1.1 ist in diesen Werten **nicht** deckungsgleich mit dem korrigierten Repo-Stand. Bei nächstem Release/Point-Release nachziehen.
- **Dok. 190** im K2-Statusabschnitt ergänzen: betroffen war auch 046 DE (abgeleitete 18,8-Werte); EN-Seite (016/046/116) erst am 27. Mai nachgezogen.

### Status

| ✓ | Erledigt DE | 27. Mai 2026 |
| ✓ | Erledigt EN | 27. Mai 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung)

| ID | Status | Bemerkung |
|----|--------|-----------|
| K2-Nachtrag | ✓ 27. Mai 2026 | vollständige Einarbeitung: 016 EN, 046 DE+EN, 116 EN; ν_τ → 25/9 |

---

## N255-257-Verschaltung — Korpus-Integration der Informations-Dokumente (27. Mai 2026)

**Anlass:** Die Dokumente 255 (Information aus Geometrie) und 257 (Informations-Brücke FFGFT ↔ UC) waren als Einzeldokumente vorhanden, aber im Korpus nicht querverschaltet. Verbindung zu Dok. 230 (Hilbertraum-Brücke) und Dok. 260 (UC-FFGFT-Vergleich) hergestellt.

### Eingearbeitete Querverweise

- **Dok. 230 §9 (Konsequenz):** Verweis auf Dok. 255 für die informationstheoretische Lesart der Übersetzbarkeit.
- **Dok. 257 §Einleitung:** Verweis auf Dok. 260 als ausgearbeitete Bridge-Case-Vorlage.
- **Dok. 260 §2 (Strukturparallelen):** Querverweis auf Dok. 255 für die geometrische Information-aus-Geometrie-Position.

### Was nicht geändert wurde

- Inhaltliche Substanz der vier Dokumente unverändert.
- Keine Strukturänderung an den Wrappern.
- Bibliographie-Einträge bleiben gleich.

### Verifikation

LaTeX-Umgebungen balanciert in allen vier Dokumenten (DE+EN); keine zerbrochenen Querverweise; PDF-Build erfolgreich.

### Status

| ✓ | Erledigt DE | 27. Mai 2026 |
| ✓ | Erledigt EN | 27. Mai 2026 |

---

## HW147 — Dok. 147 §8: Hardware-Validierung auf echte Messung korrigiert (28. Mai 2026)

**Anlass:** Eigene Hardware-Läufe auf IBM Quantum (28. Mai 2026, ibm_kingston / ibm_marrakesh, beide Heron r2, 156 Qubit) zur Überprüfung der in Dok. 147 §8 berichteten Zahlen. Abgleich mit dem Juni-2025-Hardware-Validierungsreport ergab, dass mehrere §8-Behauptungen entweder durch die neuen Daten widerlegt oder in den verfügbaren Aufzeichnungen nicht belegt sind.

### Korrigierte Behauptungen (DE+EN parallel)

| Stelle | Vorher (unbelegt/widerlegt) | Nachher (echte Messung) |
|--------|------------------------------|--------------------------|
| Bell-Treue-Tabelle | 3 Läufe, „Treue 1,000", Varianz 0,000248 | 50 Läufe, Fidelität 98,76 %, Varianz 1,249·10⁻⁴ |
| „40× deterministischer als QM" | behauptet | widerlegt: Varianz-Verhältnis 1,02, χ²-p = 0,86 |
| CHSH 73-Qubit | S = 2,8275 „aus 2025-Daten" | nicht belegt → ersetzt durch S = 2,7396 (gemessen) |
| CHSH 127-Qubit | S = 2,8278, „nahezu perfekte ξ-Übereinstimmung" | nicht belegt → ersetzt durch echte Messung |
| ξ-Fit-Tabellen (73/127) | ξ_fit angepasst an unbelegte CHSH-Werte | entfernt (Datengrundlage fehlt) |
| Monte-Carlo „kompatibel mit IBM-Beobachtung" | stützte sich auf unbelegte 2,8275 | entfernt |
| Abstract „CHSH ~10⁻³ in 73-Qubit testbar" | überzogen | ehrlich: ξ ~10⁻⁵, unter NISQ-Rauschen |
| „Experimentell validiert: CHSH = 2,827888" | überzogen | „Hardware-getestet: S = 2,74, Bell-Verletzung" |
| Schluss-Zusammenfassung | wiederholte alle obigen Werte | echte Werte + ξ-Messbarkeitsbefund |

### Neue, belegte Datenlage in §8

- **Bell-Wiederholbarkeit (50 Läufe):** Fidelität 98,76 %; Varianz mit Shot-Noise verträglich (1,02; p = 0,86). Die deterministische Varianzreduktion besteht nicht.
- **CHSH (gemessen):** S = 2,7396 ± 0,0071 (Kingston, 15 Messungen), 96,9 % der Tsirelson-Schranke, 105 σ über klassisch. Klare Bell-Verletzung.
- **Cross-Platform:** Marrakesh S = 2,7016; Geräte-zu-Geräte-Differenz 0,038 (Welch t = 2,46, p = 0,028). Diese Variation übersteigt den ξ-Effekt um ~1400× → ξ mit NISQ-Hardware prinzipiell nicht auflösbar (empirisch, nicht geschätzt).
- Zwei `important`-Korrektur-Boxen dokumentieren die Änderungen im Dokument selbst.

### Methodische Befunde

- Die unbelegten CHSH-Werte 2,8275/2,8278 stammten aus reinen Fitting-Skripten (bell_73qubit_fit.py, bell_2025_sherbrooke_fit.py), die diese Werte als hardcoded Input nahmen; keine Roh-Aufzeichnungen (Job-IDs, Counts) existieren dafür im Archiv. Der dokumentierte 2025-Lauf betraf ausschließlich Bell-Zustands-Generierung.
- Im ersten Auswertungslauf des CHSH-Skripts (Stufe 2) wurde eine zu den Winkeln nicht passende Vorzeichenkombination verwendet (Ergebnis fälschlich S ≈ 0); aus denselben Rohdaten korrekt rekombiniert ergibt sich S = 2,7396, ohne erneuten Hardware-Lauf.

### Verifikation

- begin/end-Umgebungen balanciert (DE+EN), keine zerbrochenen Tabellen, keine hängenden \ref auf gelöschte Tabellen-Labels (tab:chsh_73, tab:chsh_127, tab:system_comparison entfernt).
- Reports erstellt: Bell_Wiederholbarkeit_Report_2026-05-28.md (DE) + _En.md, mit vollständigen Job-IDs.
- Rohdaten archiviert: bell_repeatability_2026.csv (50 Zeilen), chsh_stage2_2026.csv, chsh_stage2_marrakesh_2026.csv.

### Status

| ✓ | Erledigt DE | 28. Mai 2026 |
| ✓ | Erledigt EN | 28. Mai 2026 |

---

## HW147-Folge — Folgedokumente korrigiert (28. Mai 2026)

**Anlass:** Im Anschluss an HW147 wurden weitere Dokumente geprüft, die dieselben unbelegten 2,8275/2,8278-Werte oder die 0,974-Fidelität enthielten. Pro Dokument geprüft, ob die unbelegten Werte eigene Behauptung sind (korrigiert) oder legitime Theorie/Fehltreffer (unverändert).

### Korrigiert (DE+EN), unbelegte Hardware-Werte ersetzt/markiert

- **Dok. 148 (scramblons):** IBM-Geräte-Zeilen (Brisbane/Sherbrooke) in der Cross-Platform-Tabelle als „Supraleitend (Vorhersage)" relabelt; keyresult-Übereinstimmungsbehauptung durch Verweis auf echte Messung (S=2,74) ersetzt.
- **Dok. 022 (QFT-ML-Addendum):** „2025-Daten S≈2,8275"-Fit-Grundlage durch Korrektur-Box ersetzt; CHSH-Werte als theoretisch markiert; ξ-Fit als gegenstandslos gekennzeichnet (Formel als Skalenstruktur erhalten).
- **Dok. 035 (QM):** Testbarkeits-Vorhersage als theoretisch markiert; Korrektur-Box vor dem „2025-Daten identifiziert"-Arbeitsnotiz-Abschnitt.
- **Dok. 202 (Feldtheorie-Gesamt):** Verweis auf Dok. 147 von „ΔCHSH~10⁻³" auf „theoretischer ξ-Effekt ~10⁻⁵, unter NISQ-Rauschen; Hardware S=2,74" aktualisiert (zwei Stellen).

### Unverändert — legitime theoretische Vorhersage (kein Hardware-Claim)

- **Dok. 023, 023a (Bell):** CHSH 2,828→2,827 ist die theoretische ξ-Dämpfung; 73-Qubit-Lie-Detector als *zukünftiger* Test zitiert (sciencedaily2025) — korrekt.
- **Dok. 175 (Qubit-Zustandsräume):** „2√2→2,8275" ist theoretische ξ-Dämpfung, kein Messwert.

### Unverändert — Fehltreffer (kein Bezug zu Bell/Fidelität)

- **Dok. 041:** „0,974" ist das CKM-Matrixelement |V_ud|.
- **Dok. 155:** „40-fach" bezieht sich auf DNA-Datenkompression.

### PDF-Ausgabe

Alle vier korrigierten Dokumente in DE+EN als PDF gebaut (XeLaTeX, echte Standalone-Präambel, 6×9). Wrapper unverändert (nur ch/-Kapitelinhalt geändert, Struktur gleich). Sandbox-Caveat: Math = Latin Modern (statt Libertinus), keine deutsche Silbentrennung wie unter LuaLaTeX.

### Status

| ✓ | Erledigt DE | 28. Mai 2026 |
| ✓ | Erledigt EN | 28. Mai 2026 |

---

## Dok-230 — Operationale Äquivalenz und interpretative Divergenz (30. Mai 2026)

**Anlass:** Nach der Hardware-Validierung (HW147) wurde im Gespräch deutlich, dass die in Dok. 230 (Hilbertraum-Brücke) etablierte „vollständige Übersetzbarkeit" als ontologische Identität fehlgelesen werden konnte. FFGFT teilt mit der Standard-QM die *messbaren* Vorhersagen (bis auf ξ-Korrekturen), aber nicht alle *ontologischen Interpretationen* — Letzteres wird in der Standard-Lesart bestimmter Grundbegriffe als Artefakt der unvollständigen Trägerannahmen gelesen, nicht als fundamentale Eigenschaft der Natur. Diese Klärung gehört explizit in Dok. 230.

### Eingearbeitete Änderungen (DE+EN parallel)

**1. Neue Sektion „Operationale Äquivalenz und interpretative Divergenz"** zwischen „Konsequenz: Erweiterung, nicht Ersatz" und „Zusammenfassung" eingefügt. Inhalt:

- Eröffnungsabsatz: ξ → 0 reproduziert die *Zahlen* der Standard-QM, nicht notwendigerweise deren ontologische Lesart.
- **Fünf Punkte** mit jeweils Standardlesart / FFGFT-Lesart / „operational gleich, interpretativ verschieden":
  - Born-Regel als irreduzibler Zufall vs. deterministische Polübergangs-Dynamik auf T⁴
  - Nicht-Lokalität in ℝ³ vs. topologische Verbindung auf T⁴
  - ℏ als ontologische Primitive vs. SI-Konversionsfaktor aus S=h
  - Raumzeit als gegebene Bühne vs. aus T⁴-Geometrie abgeleitet
  - Singularitäten als physikalische Endpunkte vs. Endpunkte des Trägermodells
- Zwei Schlussabsätze: „Methodischer Status" und „Operationale Äquivalenz" (mit Verweis auf Hardware-Validierung Mai 2026, Dok. 147 §8).

**2. Vorbemerkung verfeinert:** Frühere Formulierung „QM ist eine Untermenge von FFGFT" durch differenziertere Aussage ersetzt — „Beide Formalismen liefern dieselben messbaren Vorhersagen (bis auf ξ-Korrektur), unterscheiden sich aber in der ontologischen Lesart einiger Grundbegriffe". Verweis auf den neuen Abschnitt; Dok. 202 §22 als breiterer Querverweis erhalten.

**3. Zusammenfassung umstrukturiert in vier Untertitel:**

- „Was vollständig übersetzbar ist" (sechs formale Punkte: Zustände, Operatoren, Gatter, Tensorprodukte, Messung, Evolution) — explizit als „auf der formalen Ebene"
- „Was FFGFT zusätzlich liefert" (vier Mehrwert-Punkte: α/m_i/ξ-Herleitung, K_frak, Bell-Auflösung, CHSH-Vorhersage) — explizit als „außerhalb dessen, was reine Hilbertraum-QM leistet"
- „Wo die Interpretation auseinandergeht" (fünf Punkte als kompakte Liste, Querverweis auf den neuen Abschnitt; Schluss: „Operational identisch; interpretativ verschieden")
- „Methodische Position" (verfeinert: „bestätigt auf der Vorhersageebene und erweitert auf der strukturellen; widerlegt nichts, was QM messbar aussagt; schlägt aber eine andere ontologische Lesart einiger Grundbegriffe vor")

### Verifikation

- LaTeX-Umgebungen balanciert in beiden Sprachen (DE: 828 Zeilen, EN: 811 Zeilen).
- Keine offenen `\ref`; zwei ursprünglich gesetzte Labels (sec:messung, sec:bell) durch Plain-Sektionsnamen ersetzt — konsistent mit dem übrigen Verweisstil von Dok. 230.
- PDFs gebaut: DE 21 Seiten, EN 20 Seiten (XeLaTeX, echte Standalone-Präambel). Stichprobe bestätigt alle vier neuen Subsektions-Titel und die fünf Interpretations-Punkte im Output.

### Methodischer Anlass dokumentiert

Die Erweiterung schließt eine Lücke, die durch die Hardware-Validierung (HW147) sichtbar wurde: Wenn ξ ~10⁻⁵ unter dem aktuellen NISQ-Rauschen liegt, dann ist „FFGFT als Erweiterung der QM" nicht durch eine Messung der ξ-Differenz von der Standard-Lesart abgrenzbar. Die Abgrenzung muss interpretativ-strukturell erfolgen — und das wird jetzt explizit gemacht. Die fünf Punkte sind keine empirischen Behauptungen gegen Standard-QM, sondern Interpretationsdifferenzen, die sichtbar werden, sobald nach dem ontologischen Träger der Theorie gefragt wird.

### Status

| ✓ | Erledigt DE | 30. Mai 2026 |
| ✓ | Erledigt EN | 30. Mai 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung 2)

| ID | Status | Bemerkung |
|----|--------|-----------|
| N255-257-Verschaltung | ✓ 27. Mai 2026 | Querverweise zwischen Dok. 230/255/257/260 hergestellt |
| HW147 | ✓ 28. Mai 2026 | Dok. 147 §8 auf echte Messung korrigiert (S = 2,74); „40×" widerlegt |
| HW147-Folge | ✓ 28. Mai 2026 | Folgedok. 148/022/035/202 (DE+EN) korrigiert + PDF; 023/023a/175 legitime Vorhersage; 041/155 Fehltreffer |
| Dok-230 | ✓ 30. Mai 2026 | Neue Sektion „Operationale Äquivalenz und interpretative Divergenz" (5 Punkte); Vorbemerkung und Zusammenfassung überarbeitet |

---

## Dok-262 — Akzeptanz ohne Anschauung und Innensicht der dekompaktifizierten Zeit (30. Mai 2026)

**Anlass:** Zwei zuvor getrennt geplante Dokumente (Dok. 162: epistemische Selbstpositionierung; Dok. 163: positive Innensicht-Lesart) wurden zu einem einzigen Dokument unter neuem Präfix Dok. 262 zusammengeführt. Sachlich gehören die beiden Teile zusammen — ohne Teil A (negative Seite) würde Teil B (positive Seite) als Esoterik missverstanden; ohne Teil B bliebe Teil A rein defensiv. Das gemeinsame Dokument macht die FFGFT-Position zur Vorstellbarkeit von T⁴ vollständig.

### Struktur

Zwei Teile, parallel DE+EN, je 6 nummerierte Sektionen (12 insgesamt):

**Teil A — Akzeptanz ohne Anschauung: Zum erkenntnistheoretischen Status von T⁴**

1. **Was nicht vorstellbar ist, ist nicht unverständlich** — Liste der akzeptierten unvorstellbaren Konstrukte: imaginäre Zahlen (mit Gauß'scher Erweiterung), komplexwertige Wellenfunktionen, Minkowski mit ict, Hilberträume, Eichgruppen, Spinoren mit 4π-Periodizität, Calabi-Yau-Räume. Negative Zahlen als historisches Pendant — niemand konnte sich „−3 Äpfel" vorstellen, aber „drei geborgte Äpfel" sehr wohl: nicht die Anschauung änderte sich, sondern der Beschreibungsrahmen wechselte.
2. **Das tatsächliche Akzeptanzkriterium** — interne Konsistenz und prüfbare Konsequenzen. Vorstellbarkeit als psychologisches Phänomen, kein erkenntnistheoretisches.
3. **T⁴ als strukturelle Außenperspektive** — mathematische Konstrukte machen sichtbar, was aus jeder Innenperspektive heraus unvollständig wäre. Drei Beispiele: Lorentz-Geometrie, Wellenfunktion, Eichgruppe. T⁴ steht in dieser Reihe.
4. **Was das nicht ist** — drei Abgrenzungen: keine privilegierte Außenposition, keine ontologische Behauptung, keine Forderung nach Vorstellung.
5. **Konsequenz für die Diskussion von FFGFT** — wer T⁴ wegen Unvorstellbarkeit ablehnt, müsste auch komplexwertige Wellenfunktion, Lorentz mit ict, Hilberträume, Spinoren und Eichgruppen ablehnen. Verweis auf Konsistenz (Dok. 001a, 181, 193, 230) und Konsequenzen (Dok. 147 §8, Bell 96,9 %).
6. **Zusammenfassung** Teil A: „Die Vorstellung muss nicht visuell sein, um wirksam zu sein."

**Teil B — Zeit als Modus, Masse als Verformung, Fraktalität als Innensicht der dekompaktifizierten Zeit**

1. **Zeit als Modus, nicht als Bühne** — auf T⁴ sind alle vier Koordinaten gleichberechtigt periodisch; „kontinuierlich fließende Zeit" ist die phänomenale Auflösung eines diskreten Modus. Konsistent mit ℏ als SI-Konversionsfaktor (Dok. 001a, 230) und T̃·m=1 als strikter Reziprozität.
2. **Geborgte Zeit: T̃ und Energie als reziproke Lesarten** — die Apfel-Parallele aus Teil A wird auf die Zeit übertragen: wie negative Zahlen erst akzeptierbar wurden, als der Rahmen von „Apfel-Inventar" zu „Schuldbeziehung" wechselte, ist T̃ in FFGFT keine offene Zeitkoordinate, sondern eine reziproke Lesart der energetischen Wirkung auf T⁴ — *geborgte Energie*. T̃·m=1 als strukturelle Schuldbeziehung. Alle dynamischen Größen (T̃, m, Impuls, Frequenz, Wellenzahl) als verschiedene Skalierungsachsen einer einzigen energetischen Wirkung; nicht-energetisches Substrat ist allein die Topologie von T⁴ selbst. Vorbereitet §3 (Masse als Verformung): Krümmung und Energie als zwei Aspekte desselben, nicht als zwei wechselwirkende Dinge.
3. **Masse als Verformung des Trägers** — ART-Krümmung übertragen auf T⁴ als lokale Verformung der geschlossenen Geometrie; ART als linear-inertialer Grenzfall.
4. **T⁴ als skalen-strukturelle, nicht skalen-metrische Aussage** — Antwort auf die Frage „welche Skala hat der Torus?". T⁴ ist kein Objekt mit fester Längenskala, sondern eine *strukturelle Eigenschaft*, deren Schließungs-Invariante ξ skaleninvariant ist. Auf jeder Skala dasselbe Schließungsprinzip mit skala-spezifischer Auflösung — nicht „viele Tori", sondern eine strukturelle (nicht metrische) Aussage. Empirische Spur: ξ erscheint als *dieselbe* dimensionslose Zahl in fünf unabhängigen Kontexten (Lepton-Massen, Higgs-Formel, α, LiNbO₃-Dispersion auf 16 Stellen Dok. 167, Koide). Strukturelle Parallele zur Renormierungsgruppe: dasselbe theoretische Muster auf verschiedenen Skalen mit skalenabhängigen effektiven Manifestationen. Konsistent mit Dok. 182 (kein universeller maximaler Umfang; jede Skala hat eine system-spezifische obere Schranke). Anknüpfung an §2: so wie T̃ und m reziproke Lesarten derselben Wirkung sind, sind die Tori auf verschiedenen Skalen dieselbe strukturelle Eigenschaft auf je anderen Auflösungs-Achsen.
5. **Fraktalität als Phänomen der Innensicht** — Kernpunkt: Selbst-Iteration braucht eine Richtung „vorher → nachher"; auf einem geschlossenen Modus existiert sie nicht. Die fraktale Struktur (K_frak, Lepton-Massenkaskade, π-Gatter) ist ein Phänomen der dekompaktifizierten Zeit, kein Träger-Merkmal. **Strukturelle Parallele zur Born-Regel-Lesart** aus Dok. 230: zwei Phänomene (Quantenzufall, fraktale Korrekturen) als Konsequenzen derselben Dekompaktifizierung. **Rechnerischer Beweis (Schluss-Absatz)** mit Verweis auf Dok. 261: In natürlichen Einheiten (ℏ=c=1) ist die FFGFT-Beschreibung korrekturfrei; die fraktalen Korrekturen erscheinen erst beim Übersetzen in SI. Damit ist die Fraktalität-als-Innensicht-Lesart nicht nur ontologische Klärung, sondern *rechnerisch nachweisbarer Befund*: dieselbe physikalische Aussage in zwei Einheitensystemen — eine zeigt die Korrekturen, die andere nicht. Schicht 1 (kompakt, statisch) vs. Schicht 2 (dekompaktifiziert, SI-Projektion).
6. **Innensicht-Metapher: Gehirnwindungen und das Licht** — Gehirnwindungs-Metapher *explizit* eingeführt mit wörtlicher Einrahmung „Innensicht-Metapher, nicht ontologische Behauptung". Sagt nicht „T⁴ sieht aus wie ein Gehirn"; sagt: sobald Zeit dekompaktifiziert wird, erlebt der Beobachter im Inneren eine fraktal verwundene Erfahrungsgeometrie, für die das Bild zutreffend ist. Lichtbeispiel: außen geradlinig, innen den Falten folgend. Drei Bullet-Points: was die Metapher leistet, was sie nicht ist, wo sie gilt.
7. **Konsequenzen** — drei Aussagen als gemeinsame strukturelle Linie: Zeit nicht ausgezeichnet, Masse als Trägerverformung, Fraktalität als Innensicht-Phänomen.
8. **Zusammenfassung** Teil B: „Die Außenbeschreibung ist einfach. Die Innenwelt, in der wir leben, ist verwunden. Beide Beschreibungen sind nicht im Widerspruch — sie sind die zwei Seiten desselben Übergangs."

### Methodische Einordnung

Dok. 262 ist die epistemische Selbstpositionierung von FFGFT in vollständiger Form. Es klärt nach außen, dass Unvorstellbarkeit kein Ablehnungsgrund ist (Teil A), und nach innen, welche Innensicht-Bilder zulässig sind und wo ihre Grenzen liegen (Teil B). Die strukturelle Parallele zwischen Born-Regel und fraktaler Innengeometrie (Teil B §5) ist ein neues Verständnis-Resultat im Korpus: zwei Phänomene, die in der Standard-Physik unverbunden sind, erscheinen in FFGFT als Konsequenzen derselben Zeit-Dekompaktifizierung. Ergänzt um Teil B §2 („Geborgte Zeit") wird zusätzlich die Apfel-Schuld-Parallele aus Teil A auf die Energie-Zeit-Dualität übertragen: T̃ als geborgte Energie, T̃·m=1 als strukturelle Schuldbeziehung. Damit schließt sich der Bogen zwischen Teil A und Teil B auch begrifflich, nicht nur strukturell. Hinzu kommt der rechnerische Beweis am Ende von Teil B §5: dass die Fraktalität in natürlichen Einheiten gar nicht erscheint und erst beim Übersetzen in SI auftritt (Verweis Dok. 261), macht die Lesart-Klärung zu einem operationalen Befund. Die Probe ist die Rechnung selbst.

### Präfix-Wahl

Präfix 262 statt 162/163 gewählt: Dok. 262 folgt thematisch auf Dok. 261 (Statische Geometrie und SI-Projektion) und Dok. 260 (UC-FFGFT-Vergleich) und gehört in den 260er-Block der methodisch-grundlegenden Schriften. Die Nummern 162 und 163 sind damit unbelegt und stehen für zukünftige Arbeiten in der 160er-Reihe wieder zur Verfügung.

### Verifikation

- LaTeX-Umgebungen balanciert in beiden Sprachen.
- Inhaltsstruktur: 2 \\part-Trennungen mit Vorbemerkungen, 14 nummerierte Sektionen (6+8) pro Sprache.
- PDFs gebaut: DE 20 Seiten, EN 20 Seiten (XeLaTeX, echte Standalone-Präambel).
- Stichprobe bestätigt: Teil-A-Inhalte (geborgte Äpfel, akzeptierte unvorstellbare Konstrukte), Teil-B-Inhalte (Zeit als Modus, Gehirnwindungs-Metapher mit Einrahmung) und alle Schlüsselsätze in beiden Sprachen vorhanden.

### Status

| ✓ | Erstellt DE | 30. Mai 2026 |
| ✓ | Erstellt EN | 30. Mai 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung 3)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Dok-262 | ✓ 30. Mai 2026 | Zusammenführung der ursprünglich getrennt geplanten Dok. 162 (Akzeptanz ohne Anschauung) und Dok. 163 (Zeit als Modus, Innensicht-Metaphorik) zu einem Dokument im 260er-Block. Zwei Teile, 14 Sektionen, DE 20 / EN 20 Seiten. Gehirnwindungs-Metapher explizit mit Einrahmung; strukturelle Parallele Born-Regel ↔ Fraktalität als neues Verständnis-Resultat. Teil B §2 „Geborgte Zeit" überträgt die Apfel-Schuld-Parallele auf die Energie-Zeit-Dualität; neuer Teil B §4 „T⁴ als skalen-strukturelle Aussage" klärt die Tori-auf-allen-Skalen-Frage (ξ skaleninvariant, Renormierungsgruppen-Parallele, Querverweise Dok. 167 und 182); Schluss-Absatz von §5 hält den rechnerischen Beweis fest: korrekturfrei in natürlichen Einheiten, fraktale Korrekturen erst beim SI-Übersetzungsschritt (Querverweis Dok. 261).

---

## Bücher-Neuauflage v1.1.2 (Mai 2026) — Fünf Bände, drei KDP-Formate

**DOI:** [10.5281/zenodo.20474821](https://doi.org/10.5281/zenodo.20474821) — Zenodo-Release v1.1.2

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

## Revision Juni 2026 (3. Update) — Dok. 263 erweitert, P11 präzisiert, P14–P17

**Stand:** Juni 2026. Schwerpunkt: statische Geometrie / SI-Projektion konsequent
durchgezogen (Konstanten als Umrechnungsfaktoren), Dunkler-Sektor-Status geklärt,
T_CMB-Korrektur richtig eingeordnet. Alle Änderungen DE+EN, PDFs gebaut und verifiziert.

### P11 (Neufassung) — T_CMB-Restdifferenz ist normale Theorie-Messung-Abweichung
| Status | **erledigt (neugefasst)** | ✓ Juni 2026 DE/EN (Dok. 190) |

Frühere Fassung legte nahe, der geometrische Ursprung von 275/4 sei ein zu
lösender **offener Punkt**. Neufassung: Nach Anwendung der primären fraktalen
Korrektur K_frak (Dok. 133: 1−100ξ = 74/75) verbleibt eine Restdifferenz von
≈ 0,9 % zum Messwert. **Das ist keine offene Lücke, sondern eine normale
Theorie-gegen-Messung-Abweichung** (wie H₀ ≈ −1,9 %, Casimir/CMB ≈ 1,3 %,
τ-Masse ≈ 0,35 %). Der Planck-Wert 2,72548 K ist unter ΛCDM aus dem Spektrum
extrahiert — kein modellunabhängiger absoluter Referenzwert; die Theorie muss
ihn nicht exakt treffen. Der Ausdruck (1−275/4·ξ) trifft ihn numerisch exakt,
ist aber **nicht erforderlich** und hat keine geometrische Herleitung. Problem B
(zwei inkonsistente K_frak-Definitionen; Dok. 133 primär, Dok. 003 tetraedrisches
Modell nur heuristisch) unverändert bestehen.

### P14 — Rotverschiebung ist fraktale Wegverlängerung, kein Energieverlust
| Status | **erledigt** | ✓ Juni 2026 DE/EN |

Frühere „Photon verliert Energie"-Bilder sind überholt. z ist fraktale
Wegverlängerung im statischen Universum; das ΛCDM-z(d) und das FFGFT-z(d) bilden
auf dieselbe Kurve ab (z als Λ​CDM-Vergleichsgröße, kein FFGFT-Energieverlust).

### P15 — z als ΛCDM-Pipeline-Größe markiert
| Status | **erledigt / laufend** | ✓ Juni 2026 DE/EN |

z-Werte (z. B. z=1100) sind ΛCDM-Pipeline-Ausgaben, nicht modellneutral; als
Vergleichsgröße zu kennzeichnen. Breiterer Pipeline-Scan nach weiteren
unmarkierten ΛCDM-Vergleichen **laufend**.

### P16 — H₀ ist emergent, nicht fundamental
| Status | **erledigt** | ✓ Juni 2026 DE/EN (Dok. 263; Dok. 026/064/181 vorgemerkt) |

H₀ = E_H/ℏ ist eine dekompaktifizierte (SI-projizierte) Größe, ℏ wirkt nur als
Umrechnung. H₀ ist kein dynamischer Expansionsparameter, sondern ein
geometrischer, als Expansion fehlgedeuteter Koeffizient. Ältere Stellen mit
„fundamentale Konstante"/Energieverlust-Vakuum-Bild (Dok. 026 Z.116/117,
Ausläufer 064/181) als veraltet **vorgemerkt** (größere Baustelle).

### P17 — Dunkler Sektor: Deutung geklärt, Quantifizierung offen
| Status | **erledigt (Register), Quantifizierung offen** | ✓ Juni 2026 DE/EN (Dok. 190; Dok. 028 vorgemerkt) |

- **DE/DM-Verhältnis** ξ^(ln2,5/lnξ): als Vorhersage zirkulär (ergibt für jedes ξ
  exakt 2,5); zulässig nur als **eingeschränkter Umrechnungsfaktor** zur ΛCDM-Ω-
  Buchhaltung (wie c/z), eingeschränkt durch das ρ_DE-Artefakt (kein FFGFT-
  Gegenstück).
- **Deutung geklärt:** Dunkle Materie ist ein ξ-geometrischer Effekt (Artefakt der
  ΛCDM-Sicht, wie H₀ und z); Dunkle Energie ist eliminiert (kein Λ).
- **Zwei nicht-tragfähige a₀-Formeln:** Dok. 028 fit-abhängig (K_M=1,637);
  Dok. 201 §4.3 a₀=c²ξ/(4λ) dimensionsinkonsistent (λ müsste Länge sein, ist via
  m_T=λ/ξ Energie). Flache Rotationskurve folgt qualitativ als MOND-Konsequenz;
  v(r)-Profil und SPARC-Vergleich **nicht durchgerechnet — offen**.

### Dok. 263 (Fraktale Holografie) — mehrfach erweitert
| Status | **erledigt** | ✓ Juni 2026 DE/EN |

Eigenständiges IPI-Dokument (keinem Buchband zugeordnet). Neue Abschnitte:
- **Zeichenerklärung** (Notationstabelle: ξ, T̃·m=1, D_f, E₀, E_H, H₀, R_H, L₀,
  L_ξ, z, ρ_vac, m_T/λ, c/ℏ/ℏc, T_00) + Schichten + stehende Mahnung.
- **„H₀ als Projektions-Artefakt"** (P16 umgesetzt; z als ΛCDM-Fehldeutung;
  differenzierter 41/4-Schluss: Struktur belegt / Zahlenwert offen, Deutung
  unabhängig).
- **„Konstanten als Projektionsfaktoren und die Vakuumenergie"** (4 Schritte):
  (1) c, ℏc, √(ℏG/c⁵) begründen nichts — SI-Umrechnung (c=L/T Dok. 134; G c-frei
  aus ξ Dok. 012/013); (2) Vakuumstruktur kompaktifiziert vollständig vorhanden,
  dekompaktifiziert nur SI-sichtbar (entsteht nicht); (3) kein statischer
  Energie-Sockel: T_00=ξ[(∂_tE)²+(∇E)²] aus ℒ=ξ(∂E)², □E=0 (Dok. 010), bei
  ∂_tE=0 ist T_00=0 — Energie aus zeitlicher Komponente; (4) Abgrenzung
  belastbar/zirkulär (CMB/Casimir echt; DE/DM Umrechnungsfaktor; vgl. P17).
- **T_CMB-Klarstellung:** T_CMB=(16/9)ξ²E_ξ ist eine algebraische ξ-Relation,
  16/9=(4/3)², **keine fraktale Korrektur**; D_f spielt keine Rolle. Belastbar
  als Verhältnis; absoluter Kelvin-Wert über SI; Restabweichung nicht aus ξ.
- **„Formale Brücke zu UIFT — einseitig verifizierbar"** (Dok. 257): beruht auf
  erster Ordnung (16/9)ξ; ξ_FFGFT/ξ_UIFT ≈ 414.684 ist Umrechnungsfaktor (P13);
  **FFGFT-Seite verifizierbar, UIFT-Seite nicht** (Tekers Relation, außerhalb
  unseres Zugriffs). K_frak und absoluter Wert für die Brücke irrelevant.

### Komplett-ZIP neu gebaut
| Status | **erledigt** | ✓ Juni 2026 |

`FFGFT_v1_1_2_Komplett.zip` neu gepackt mit aktuellem Stand von Dok. 263 und 190;
sechs Begleitskripte zu Dok. 263 im Ordner `Dok263_Skripte/`; README und dieser
Changelog aktualisiert. Keine Buchbände betroffen (Dok. 190/263 in keinem Band).

### Status
| ✓ | Erstellt DE | Juni 2026 |
| ✓ | Erstellt EN | Juni 2026 |

---

### Übersichtstabelle — Nachtrag (Fortsetzung 5)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-3.Update | ✓ Juni 2026 | P11 neugefasst (T_CMB-Restdifferenz = normale Theorie-Messung-Abweichung, keine offene Lücke); P14–P17 ergänzt (z fraktale Wegverlängerung; H₀ emergent; Dunkler-Sektor-Deutung geklärt / Quantifizierung offen, zwei nicht-tragfähige a₀-Formeln). Dok. 263 mehrfach erweitert (Notationstabelle, H₀-Projektions-Artefakt, Konstanten als Projektionsfaktoren + Vakuumenergie, T_CMB-Klarstellung, formale UIFT-Brücke einseitig verifizierbar). Komplett-ZIP neu gebaut inkl. Dok263-Skripte. |

---

## Revision Juni 2026 (4. Update) — Dok. 264 neu, methodische Klärungen, neue Skripte

**Stand:** Juni 2026. Schwerpunkt: Ferrotoroidizitäts-Paper interpretiert,
ΛCDM-Zirkularität dokumentiert, WBE/T⁴-Analyse, z als Nicht-FFGFT-Größe
konsequent durchgezogen. Alle Änderungen DE+EN, PDFs gebaut und verifiziert.

### Dok. 264 (Ferrotoroidizität und Quaternärspeicher) — neu, DE+EN
| Status | **erledigt** | ✓ Juni 2026 DE/EN |

Neues eigenständiges IPI-Dokument. Referenzarbeit: Qureshi et al., *Nature
Communications* 17:4033 (2026), DOI: 10.1038/s41467-026-70767-8.

Alle 6 Formeln des Papers (Toroidisierung, Polarisationsmatrix Gl. 2/3,
allgemeine Polarisationsmatrix Gl. 9, DM-Hamiltonoperator Gl. 4–6,
Messwert Gl. 7, Endpolarisation Gl. 8) aus FFGFT-Sicht interpretiert.

**Kernbrücken (algebraisch exakt):**
- Vier Domänen = ℤ₂×ℤ₂-Gruppe der T⁴-Windungsmoden (Zeit-Inversion × Raum-
  spiegelung); keine Analogie, algebraisch exakt.
- P'' = 0 (rein imaginäres M⊥) = statischer T⁴-Grundzustand (keine
  Modenerzeugung = keine Expansion).
- Nichtflüchtigkeit = topologischer Schutz der Windungszahl (Dok. 204),
  dasselbe Prinzip wie Stabilität der Leptonmassen-Hierarchie (Dok. 190 P2).

**Aus DeepSeek-Vorlage übernommen (bereinigt):**
- Tired-Light-Abgrenzung (3 Punkte: Kohärenz, Zeitdilatation, CMB-Spektrum).
- Skalenvergleichstabelle (Atomar / Sub-Planck / Kosmologisch) **ohne**
  w = −3/4 (das ist UIFT, nicht FFGFT).
- Korrespondenztabelle (10 belegte Zeilen, 5 fehlerhafte DeepSeek-Einträge
  entfernt: w = −3/4, D^b/D^c = ξ [Faktor ~5000 daneben], DM = Wegverlängerung,
  T₄ = Strahlung-Materie-Übergang, Invariante = z).

**Wichtige Formulierungskorrektur:** z existiert in FFGFT nicht als
Primärgröße. Überall in Dok. 264 steht daher λ_b/λ_e (gemessenes
Wellenlängenverhältnis); z = λ_b/λ_e − 1 ist nur eine Bezeichnung
(keine FFGFT-Größe, Dok. 190 P14).

### Neue Begleitskripte
| Status | **erledigt** | ✓ Juni 2026 |

- **wbe_t4_flrw.py**: WBE-Argument auf T⁴ (statisch, alle drei Voraus-
  setzungen exakt erfüllt) vs. FLRW (Voraussetzung B bricht: Bekenstein-
  Surface vs. WBE-Volume). Strukturelle Asymmetrie belegt.
- **lcdm_circularity.py**: Methodisches Audit der ΛCDM-Pipeline-Zirkularität
  (T_CMB, r_s, Ω-Werte, Pantheon+). FFGFT-Gegenpart: H₀ aus ξ (null freie
  Parameter). UIFT-Konsequenz: ΛCDM-Zahlen sind Orientierungswerte, keine
  Referenzwerte für Tests alternativer Modelle.
- **UIFT.py**: Formale Brücke FFGFT ↔ UIFT (erste Ordnung, K_frak separat,
  FFGFT-Seite verifizierbar, UIFT-Seite nicht).

### Methodische Klärungen (IPI-Korrespondenz, Onur Teker)
| Status | **erledigt / laufend** | ✓ Juni 2026 |

- **z als Nicht-FFGFT-Größe**: FFGFT kann strukturell nicht auf Expansion
  umgedeutet werden (T̃·m = 1 schließt a(t) aus). z tritt in FFGFT nur als
  Übersetzungsversuch mit ΛCDM-Pipeline-Werten auf; fehlerbehaftet per
  Konstruktion.
- **WBE-Analyse**: WBE-Voraussetzungen auf T⁴ exakt erfüllt; auf FLRW
  bricht Voraussetzung (B) strukturell (Bekenstein-Surface vs. WBE-Volume).
  α = D_f/(D_f+1) ist in FFGFT Ableitung, in FLRW Posit (Onurs eigene
  Aussage bestätigt).
- **P'' = 0 als experimenteller Fingerabdruck**: Static-T⁴-Bedingung
  im Ferrotoroidizitäts-Paper nachgewiesen; FLRW hätte P'' ≠ 0 durch
  Expansionsdynamik.
- **D_eff = 2 im Experiment**: Vier Domänen haben D_eff = 2 (ℤ₂×ℤ₂),
  α(D=2) = 2/3, d.h. w = −2/3 ≠ −3/4. Frage ob Onurs Holographiefläche
  D = 3 (Bulk) oder D = 2 (Surface) ist, ändert die w-Vorhersage.
- **Drafts**: Mehrere IPI-Entwürfe zu Onur, Peter, José ungesendet.

### Komplett-ZIP und Changelog: Nächster Update ausstehend
| Status | **offen** |

Dok. 264 noch nicht im großen ZIP; bei Gelegenheit einzubauen
(372 Einzeldok-PDFs nach Einschluss).

### Übersichtstabelle — Nachtrag (Fortsetzung 6)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-4.Update | ✓ Juni 2026 | Dok. 264 (Ferrotoroidizität, DE+EN, 9/10 S.): alle 6 Paper-Formeln aus FFGFT-Sicht, ℤ₂×ℤ₂-Brücke, Tired-Light-Abgrenzung, bereinigte Korrespondenztabelle. z als Nicht-FFGFT-Größe konsequent (λ_b/λ_e statt z). Neue Skripte: wbe_t4_flrw.py, lcdm_circularity.py, UIFT.py. ΛCDM-Zirkularitäts-Audit. IPI-Korrespondenz: WBE/T⁴-Analyse, P''=0-Fingerabdruck, D_eff=2-Beobachtung. |

---

## Revision Juni 2026 (4. Update) — Dok. 264 neu, methodische Klärungen, neue Skripte

**Stand:** Juni 2026. Schwerpunkt: Ferrotoroidizitäts-Paper interpretiert,
ΛCDM-Zirkularität dokumentiert, WBE/T⁴-Analyse, z als Nicht-FFGFT-Größe
konsequent durchgezogen. Alle Änderungen DE+EN, PDFs gebaut und verifiziert.

### Dok. 264 (Ferrotoroidizität und Quaternärspeicher) — neu, DE+EN
| Status | **erledigt** | ✓ Juni 2026 DE/EN |

Neues eigenständiges IPI-Dokument. Referenzarbeit: Qureshi et al., *Nature
Communications* 17:4033 (2026). Alle 6 Formeln des Papers aus FFGFT-Sicht
interpretiert. Kernbrücken (algebraisch exakt): Vier Domänen = ℤ₂×ℤ₂ der
T⁴-Windungsmoden; P''=0 = statischer T⁴-Grundzustand; Nichtflüchtigkeit
= topologischer Schutz (Dok. 204). Tired-Light-Abgrenzung, bereinigte
Skalenvergleichs- und Korrespondenztabelle eingearbeitet.
**Formulierungskorrektur:** z existiert in FFGFT nicht als Primärgröße;
überall λ_b/λ_e (gemessenes Wellenlängenverhältnis), z nur Bezeichnung
(Dok. 190 P14).

### Neue Begleitskripte (EN)
| Status | **erledigt** | ✓ Juni 2026 |

- **wbe_t4_flrw.py**: WBE auf T⁴ exakt vs. FLRW (Voraussetzung B bricht).
- **lcdm_circularity.py**: ΛCDM-Pipeline-Zirkularitäts-Audit + FFGFT-Gegenpart.
- **UIFT.py**: Formale Brücke FFGFT↔UIFT (überarbeitet, K_frak korrekt).

### Methodische Klärungen (IPI-Korrespondenz Onur Teker)
| Status | **erledigt / laufend** | ✓ Juni 2026 |

z als Nicht-FFGFT-Größe (T̃·m=1 schließt a(t) aus); WBE/T⁴-Analyse
(α aus Geometrie, nicht Posit); P''=0 als experimenteller Fingerabdruck
static/expanding; D_eff=2 Beobachtung (α=2/3, w=−2/3 ≠ −3/4).
Mehrere IPI-Entwürfe ungesendet.

### ZIP-Update ausstehend
Dok. 264 noch nicht im großen ZIP (→ 372 Einzeldok-PDFs).

### Übersichtstabelle — Nachtrag (Fortsetzung 6)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-4.Update | ✓ Juni 2026 | Dok. 264 (Ferrotoroidizität DE/EN, 9/10 S.): alle 6 Paper-Formeln, ℤ₂×ℤ₂-Brücke, Tired-Light-Abgrenzung, bereinigte Tabellen, λ_b/λ_e statt z. Neue Skripte: wbe_t4_flrw, lcdm_circularity, UIFT. ΛCDM-Zirkularitäts-Audit. IPI: WBE/T⁴, P''=0, D_eff=2. |

---

## Revision Juni 2026 (5. Update) — P18–P20, Dok. 264/265, Onur-Briefwechsel, Hausdorff-Skript

**Stand:** 5. Juni 2026. Schwerpunkt: Ehrliche Eingrenzung der kosmologischen
Anwendbarkeit von FFGFT; neue Dokumente 264/265; Hausdorff-Herleitung der
fraktalen Wegverlängerung; präzisierter Onur-Briefwechsel.

### Dok. 264 (Ferrotoroidizität und Quaternärspeicher) — neu, DE+EN, 9/10 S.
| Status | **erledigt** | ✓ 5. Juni 2026 |

Alle 6 Formeln von Qureshi et al. (Nature Communications 17:4033, 2026)
aus FFGFT-Sicht interpretiert. Kernbrücken (algebraisch exakt):
ℤ₂×ℤ₂-Gruppenstruktur = T⁴-Windungsmoden; P''=0 = statischer Grundzustand;
Nichtflüchtigkeit = topologischer Schutz (Dok. 204).
Tired-Light-Abgrenzung (3 Punkte), Skalenvergleichstabelle (bereinigt,
kein w=−3/4), Korrespondenztabelle (10 belegte Zeilen).
Formulierungskorrektur: λ_b/λ_e statt z (keine FFGFT-Primärgröße, P14).

### Dok. 265 (Korrespondenzebenen zwischen Formalismen) — neu, DE+EN, 6 S.
| Status | **erledigt** | ✓ 5. Juni 2026 |

Methodisches Werkzeugdokument für Stefaans Modell-Einordnungsarbeit.
Drei Ebenen: Fast-Äquivalenz (ℤ₂×ℤ₂, P''=0, topolog. Schutz),
struktureller Überlapp (DM-Antisymmetrie, Projektionsfaktoren),
komplementär (FFGFT: warum 4 Zustände; Blume-Maleev: Übergangstemperaturen).
Analogie: Wigner-Gruppenklassifikation vs. QED-Feldtheorie.

### P18 — E_H/ℏ ist geometrische Skalenkonstante, keine H₀-Vorhersage
| Status | **vorgemerkt** | ✓ 5. Juni 2026 (Dok. 190) |

E_H/ℏ ist intern ohne freie Parameter definiert (ξ → E₀ → E_H = E₀·ξ^(41/4)
→ E_H/ℏ). Nähe zum ΛCDM-H₀-Wert (66,2 vs. 67,4 km/s/Mpc) bekannt,
aber ob der Exponent 41/4 durch ΛCDM-Vergleich motiviert wurde, ist
nicht ausschließbar. Keine unabhängige Bestätigung vorhanden.

### P19 — Hausdorff-Herleitung ergibt Potenzgesetz (Widerspruch zu Dok. 182)
| Status | **vorgemerkt** | ✓ 5. Juni 2026 (Dok. 190, Skript hausdorff_wegverlaengerung.py) |

Herleitung der fraktalen Wegverlängerung aus der Hausdorff-Metrik:
L_eff/R = (R/L₀)^(ξ/D_f) — ein Potenzgesetz, nicht exp(d/R_H).
Exponent ξ/D_f ≈ ξ/3 aus 3/D_f − 1 = (3−D_f)/D_f.
Skalenunabhängig (L₀ = ξ·ℓ_P konstant). Im Kristall winziger Effekt
(~4×10⁻⁴), kosmologisch ~0,7% — beide zu klein gegenüber Beobachtung.
Widerspruch zu Dok. 182 (exp(d/R_H)) ungelöst und vorgemerkt.

### P20 — R_H ist modellabhängige Konvention; FFGFT braucht externen Parameter
| Status | **vorgemerkt** | ✓ 5. Juni 2026 (Dok. 190) |

R_H ist keine Naturkonstante sondern eine ΛCDM-Pipeline-Ausgabe.
Es gibt keine modellneutrale Messmethode für die Größe des Universums.
Innen/Außen-Asymmetrie des T⁴: von außen ist die Torusgröße irrelevant
(statisch), von innen entscheidend (fraktale Erweiterung akkumuliert).
**Eindeutig festgehalten:** FFGFT kommt auch bei kosmologischen Berechnungen
nicht ohne eine weitere Annahme aus. „Null freie Parameter" gilt nur intern.
Kosmologisch hat FFGFT einen externen Parameter: R_H. Solange dieser nicht
ΛCDM-unabhängig bestimmbar ist, bleibt jede kosmologische Formel ΛCDM-abhängig.

### IPI-Korrespondenz (Onur Teker, WBE-Thread)
| Status | **laufend** | ✓ 5. Juni 2026 |

Onurs Mail (5.6., 00:18): Alle drei FFGFT-Punkte numerisch getestet.
P''=0/Stationarität bestätigt (N_active ∝ a^ν verletzt WBE-Voraussetzung).
D_eff=2 getestet: 10,6σ vs. 7,7σ — Leiter D=2→3→4→∞ zeigt Daten wählen
extensives Limit (w→−1). Holografische Spannung: Volume-WBE vs.
Surface-Bekenstein widersprechen sich intern. Statisches Universum:
Δχ²≈138 schlechter, SNe-Zeitdilatation bei ~90σ ausgeschlossen.
Onurs Schluss: Fraktalität im Materie-Sektor, nicht im DE-Sektor.

Neuer Entwurf (r4396191531249081705): Herleitung ξ→E₀→E_H=E₀·ξ^(41/4)
→E_H/ℏ explizit; R_H als modellabhängige Konvention; Innen/Außen-Asymmetrie;
ehrliche Parameterzählung (intern: null; kosmologisch: +1 externer Parameter);
Symmetrie zu Onur: beide brauchen ΛCDM-Skala für Tests.

### Neue Skripte
| Status | **erledigt** | ✓ 5. Juni 2026 |

- **hausdorff_wegverlaengerung.py**: Herleitung der fraktalen Wegverlängerung
  aus Hausdorff-Metrik; Potenzgesetz vs. Exponentialgesetz; skalenunabhängige
  Struktur; numerischer Vergleich drei Skalen.

### ZIP-Update ausstehend
Dok. 264/265 und P18–P20 noch nicht im großen ZIP.

### Übersichtstabelle — Nachtrag (Fortsetzung 7)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-5.Update | ✓ 5. Juni 2026 | Dok. 264 (Ferrotoroidizität, DE/EN): ℤ₂×ℤ₂-Brücke, P''=0, topolog. Schutz, Tired-Light, bereinigte Tabellen. Dok. 265 (Formalismus-Korrespondenz, DE/EN): 3-Ebenen-Klassifikation für Stefaan. P18 (E_H/ℏ = geometrische Skalenkonstante, keine H₀-Vorhersage). P19 (Hausdorff → Potenzgesetz, Widerspruch zu Dok. 182). P20 (R_H = modellabhängige Konvention; FFGFT braucht externen kosmologischen Parameter; Innen/Außen-Asymmetrie T⁴). hausdorff_wegverlaengerung.py. Onur-Briefwechsel: P''=0-Test, D_eff=2-Leiter, statisches-Universum-Test; neuer Entwurf mit Herleitung ξ^(41/4). |

---

## Revision Juni 2026 (6. Update) — Dok. 266/267 neu, CMB-Peak-Analyse, Trompeten-Mechanismus, symmetrische Zirkularität

### Dok. 266 (Analyse von Onur Tekers numerischen Tests) — neu, DE+EN, 6 S.
| Status | **erledigt** | ✓ Juni 2026 |

Geht Onurs drei Tests nach: (1) P''=0/Stationarität — N_active ∝ a^ν
verletzt WBE, intern inkonsistent; (2) Dimensionsleiter D=2→3→4→∞
(σ=10,6/7,7/6,1/0), holografischer Riss Volume-WBE(3/4) vs.
Surface-Bekenstein(2/3); (3) statisches Universum BAO Δχ²≈138, SNe Ia
b=1,003±0,011 schließt b=0 aus, aber NICHT FFGFT (sagt b=1). Brücke
FFGFT/UIFT (ξ_FFGFT/ξ_UIFT≈414,684) bleibt gültig, braucht kein R_H.

### Dok. 267 (Kosmologische Entartung: ΛCDM und FFGFT) — neu, DE+EN, 9/7 S.
| Status | **erledigt** | ✓ Juni 2026 |

Ausführliche Gegenüberstellung beider Modelle. Kernthese: SNe Ia, BAO und
CMB-Temperatur sind entartet — sie unterscheiden nicht zwischen metrischer
Expansion (ΛCDM) und fraktaler Zeitentfaltung (FFGFT). Inhalt:
- **Invertierte Anfangsbedingung:** ΛCDM (heiß+schnell → kalt+beschleunigt)
  vs. FFGFT (kalt+langsam bei L₀, Zeit extrem langsam, topologische statt
  thermodynamische Konzentration → scheinbar warm+beschleunigt).
- **Peak-Struktur aus reiner Geometrie:** Moden-Verhältnisse hängen nur von
  der Resonatorgeometrie ab, nicht vom Medium. Diskrete Peaks ⇒ kompakte
  Topologie (Argument FÜR T⁴, GEGEN unendlich-offenes Universum).
- **Trompeten-/Resonator-Mechanismus:** Peak-Formel ℓ_n = A·n/(1+B/n).
  A = Grundskala = externer Parameter (Torusgröße = R_H, P20).
  B = 1/(D−1) = 1/3 aus Dimension D=4 — KEINE externe Eingabe, reine
  Dimensionszahl. Form folgt aus „kompakter Resonator + Randanpassung".
- **Modellneutraler Test:** rohe Peak-Verhältnisse (FFGFT B=1/3:
  1:2,29:3,60:4,92:6,25 vs. gemessen 1:2,44:3,68:5,09:6,56, ~3,3%).
  Caveat: nur modellfreie lokale Maxima sauber; ΛCDM-Template-Fit-Werte
  kürzen sich in Verhältnissen NICHT heraus (~1–2% Restabhängigkeit).
- **Umkehrung:** Messung liefert nur Produkt H₀·L_res = θ₁·c/ln(1+z_*)
  ≈ 458 km/s, nicht H₀ allein (Winkel = Längenverhältnis).
- **Symmetrische Zirkularität:** ΛCDM (r_s aus 6 Param + heiße Frühphase)
  und FFGFT (R_H aus E_H/ℏ) gleichermaßen zirkulär; niemand gewinnt
  modellneutrales H₀ aus CMB-Peaks. Fairer Vergleich: Sparsamkeit vs.
  Verankerung, keine Überlegenheitsbehauptung.
- **Drei-Phasen-Struktur ΛCDM:** Inflation (beschleunigt) → Materie/Strahlung
  (gebremst) → Λ (wieder beschleunigt) verlangt zwei separate, unabhängig
  postulierte Beschleunigungsmechanismen + Koinzidenzproblem; FFGFT mit
  einem Mechanismus (Rekursion). Strukturell, nicht empirisch.
- **Grenze der Übersetzbarkeit:** Alle Größen mit einem Bezugspunkt nur
  näherungsweise/in Größenordnung nahe ΛCDM; exakte Übersetzung nicht möglich
  (verschiedene Strukturen). Frühphase für BEIDE Modelle kaum belegbar.

z_* ≈ 875 als rein geometrische FFGFT-Größe (Resonanzbedingung
(1+z_*)^(1/ln(1/ξ)) = λ_e/L₀), nicht identisch mit ΛCDM-Rekombination
(z≈1089). Keine Überlegenheitsbehauptung; ehrliche Eingrenzung durchgängig.

### Neue Verifikationsskripte
| Status | **erledigt** | ✓ Juni 2026 |

- **verify_z_star_final.py**: unabhängige z_*-Nachrechnung aus ξ+CODATA.
- **verify_cmb_peaks_final.py**: dimensionelle Prüfung; Peak-Struktur.
- **ffgft_cmb_zirkularitaet_komplett.py**: konsolidierte 6-Teile-Kette
  (z_*, CMB-Peaks, reine Geometrie, Trompete, Umkehrung, Zirkularität).
- **ffgft_trompeten_mechanismus.py**: Resonator + Randanpassung.
- **ffgft_eingaben_buchhaltung.py**: A extern vs. B=1/3 reine Dimensionszahl.
- **ffgft_rohe_peak_verhaeltnisse.py**: modellneutraler Verhältnis-Test.
- **ffgft_lambda_im_messprozess.py**: wo ΛCDM schon im Messprozess steckt.
- **ffgft_zirkularitaet_symmetrie.py**: symmetrische Zirkularität ΛCDM↔FFGFT.
- **ffgft_lcdm_zeitverlauf.py**: Drei-Phasen-Struktur der ΛCDM-Expansion.

### Korrektur eigener Befunde (intern, ehrlich)
- Eingereichte externe Skripte (z_*≈1103, CMB-Übereinstimmung „0,1–1,5%")
  erwiesen sich als fehlerhaft (gewählter Exponent 8,55 statt ln(1/ξ)=8,92;
  χ²-Werte unbrauchbar). Nach Löschung dieser Skripte: alle Hinweise darauf
  und die falschen Berechnungen aus Dok. 267 entfernt; nur eigene,
  verifizierte Werte (z_*≈875) bleiben.
- Mehrere Scheintreffer verworfen: √(D_f/2)=√(3/2) ist ξ-unabhängig;
  Offset 1/φ² ist Fit-Artefakt; Bessel-Projektion erklärt Versatz NICHT.
  ξ spielt in der Peak-STRUKTUR keine Rolle (testet Geometrie/Dimension).

### ZIP-Update ausstehend
Dok. 264/265/266/267 und P18–P20 noch nicht im großen ZIP.

### Übersichtstabelle — Nachtrag (Fortsetzung 8)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-6.Update | ✓ Juni 2026 | Dok. 266 (Onur-Tests-Analyse, DE/EN): P''=0, Dimensionsleiter, statisches-Universum-Test, FFGFT/UIFT-Brücke. Dok. 267 (Kosmologische Entartung, DE/EN, 9/7 S.): invertierte Anfangsbedingung, Peak-Struktur aus reiner Geometrie, Trompeten-Mechanismus ℓ_n=A·n/(1+B/n) mit B=1/3 aus D=4, modellneutraler Verhältnis-Test (~3,3%), Umkehrung (nur H₀·L_res messbar), symmetrische Zirkularität, Drei-Phasen-ΛCDM-Struktur, Grenze der Übersetzbarkeit. z_*≈875 rein geometrisch. Neue Skripte: verify_z_star_final, verify_cmb_peaks_final, ffgft_cmb_zirkularitaet_komplett, ffgft_trompeten_mechanismus, ffgft_eingaben_buchhaltung, ffgft_rohe_peak_verhaeltnisse, ffgft_lambda_im_messprozess, ffgft_zirkularitaet_symmetrie, ffgft_lcdm_zeitverlauf. Fehlerhafte externe Skripte (z_*=1103) gelöscht; Hinweise aus Dok. 267 entfernt. |

---

## Revision Juni 2026 (7. Update) — Dok. 268 neu, Beobachter-Mechanismus, P-Register-Konsolidierung P18–P30

**Grundlage dieser Session:** Vertiefung der CMB-Peak-Herleitung aus der
T⁴-Gitterstruktur, Korrektur einer fehlerhaften Faktor-3-Begründung,
Bereinigung und Vervollständigung des P-Registers in Dok. 190.

### N268 — Dok. 268 „CMB-Akustikpeaks aus der T⁴-Gitterstruktur" (neu, DE)
| Status | **erledigt DE** / EN ausstehend |
|--------|-------------------------------|

Schrittweise Herleitung (16 Schritte, 19 S.) der CMB-Peak-Verhältnisse aus
der T⁴-Gitterstruktur:

- **Schritt 1–5:** T⁴-Zustandsraum, Jacobi-Entartung g(|n|²) (nicht monoton),
  Bose-Einstein-Gewichtung I(r)=g·⟨N⟩·r, lokale Maxima bei |n|²=3,6,10,14,18,…
  Dominante Grundpeaks |n|²=1,6,14,26.
- **Schritt 6–7:** absolute Skala (extern, P20); Schritt 7 als Vorausverweis
  auf die Auflösung in Schritt 8/9 (nicht mehr „einzige offene Frage").
- **Schritt 8–9:** Faktor 3 = **drei beobachtbare Raumdimensionen**.
  k_obs² = (n₁²+n₂²+n₃²)/L², symmetrischste Grundmode (1,1,1,0) gibt 3.
  Sichtbare Serie 3·{1,6,14,26} = {3,18,42,78}.
  Verhältnisse 1:2,449:3,742:5,099 vs. CMB 1:2,441:3,682:5,091 (< 2 %).
- **Schritt 10:** Doppel-Resonator-Bild (T⁴-Gitter + 3D-Beobachterprojektion).
- **Schritt 10.6 (neu):** „Was aus den Peaks folgt: zwei Filter" — siehe unten.
- **Schritt 11:** Kein-Fit-Nachweis; ehrliche Abgrenzung (absolute Skala P20,
  strenge C_ℓ-Projektion P30 offen).
- **Schritt 12–16:** Schwarzschild-Verbindung, Messproblem FFGFT vs. ΛCDM,
  universelle Compton-Schwarzschild-Relation, T⁴-Länge als Schwarzschild-Radius,
  und (Schritt 16) ehrliche Klarstellung, warum die Schwarzschild-Relation R_H
  NICHT herleitet (m_e→M_U-Trugschluss aufgedeckt).

### K4 — Faktor 3: Beobachter-Mechanismus statt fraktaler Dispersionsrelation
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 267 (DE+EN), 268 (DE) |
| Status | **erledigt** |
| Erledigt DE | ✓ Juni 2026 |
| Erledigt EN | ✓ Juni 2026 (267 + 268) |

**Falsch (frühere Begründung):** Der Faktor 3 ist die fraktale Dimension D_f;
er folgt aus einer „fraktalen Dispersionsrelation k²_eff = D_f·k²_Torus
(Dok. 051, Tetrad-Formalismus)".

**Korrekt:** Der Faktor 3 zählt die **drei beobachtbaren Raumdimensionen**.
Der Beobachter misst k_obs² = (n₁²+n₂²+n₃²)/L² (die vierte Torusrichtung ist
Zeitentfaltung). Die konforme Metrik aus Dok. 051 hebt sich für masselose
Teilchen heraus; die fraktale Korrektur aus Dok. 204 ist +0,69·ξ·k² ≈ 10⁻⁵,
NICHT der Faktor 3. D_f = 3−ξ ist mit dem Faktor 3 **konsistent** (D_f ist
die Raumdimension, leicht durch ξ modifiziert), aber NICHT seine Herkunft.
Korrektur durchgängig in 267 (DE+EN) und 268 (DE); alle Stellen mit
„k²_eff=D_f·k²", „√D_f-Skalierung" und „Tetrad-Formalismus als Herleitung"
ersetzt.

### Zwei-Filter-Aussage (Dok. 267 DE+EN, Dok. 268 DE Schritt 10.6)
| Status | **erledigt** | ✓ Juni 2026 DE+EN |

Die diskreten, scharfen CMB-Peaks folgen aus zwei zusammenwirkenden
Eigenschaften desselben **vollständigen** T⁴, gesehen aus zwei Bezugspunkten:

- **Filter 1 — Kompaktheit (T⁴ als Ganzes, von außen):** erzeugt das
  *diskrete* Modenspektrum; erzwingt die *Existenz* scharfer Peaks.
  Ohne Kompaktheit: Kontinuum, keine Peaks.
- **Filter 2 — fraktale Struktur (von innen, dekompaktifiziert):** die
  Jacobi-Entartung + Bose-Einstein gewichten die Moden ungleich; erzwingt
  die *Lage* der dominanten Peaks. Ohne diskretes Gitter kein Angriffspunkt.

Beide sind **keine zwei Objekte**, sondern zwei Bezugspunkte auf denselben
geschlossenen Torus: von außen kompakt-endlich, von innen fraktal-granuliert
bis L₀=ξ·ℓ_P. Die fraktale Ungeschlossenheit ist damit keine zweite, der
Kompaktheit widersprechende Eigenschaft, sondern die Innenansicht — eine
**Bezugspunkt-Angelegenheit** (Innen/Außen, P20). Erst beide Filter zusammen
geben die beobachtete Serie.

**Ableitbare Aussage:** Die diskreten Peaks sprechen FÜR ein kompaktes
(endliches) Universum und GEGEN ein rein-unendlich-offenes.
**Ehrliche Abgrenzung:** FFGFT-intern; ΛCDM erzeugt dieselben Peaks aus einer
zeitlichen Schranke (Schallhorizont) in einem räumlich unendlichen Universum.
Die Peaks allein unterscheiden räumliche Kompaktheit und Zeitschranke nicht.

### P-Register-Konsolidierung in Dok. 190 (DE: P-Nummern, EN: R-Nummern)
| Status | **erledigt** | ✓ Juni 2026 DE+EN |

Dok. 190 listete nur P1–P17, obwohl Dok. 267/268 bereits P18–P30 benannten.
Nachgetragen und konsolidiert:

- **P18** (R18): ΛCDM/FFGFT als zwei Lesarten — theoretisch, nicht empirisch
  unterscheidbar. *Konzeptuelle Einordnung.*
- **P20** (R20): absolute kosmologische Skala R_H/D_A/z_* ist **externe
  Eingabe** ≡ Exponent 41/4 bzw. E_H=E₀·ξ^(41/4). Betrifft nur
  Absolutpositionen, nicht die Verhältnisse. **Offen.**
- **P29** (R29): Peak-Auswahlregel — **teilweise beantwortet** durch den
  3D-Beobachter-Mechanismus (Schritt 8/9).
- **P30** (R30): strenge sphärische C_ℓ-Projektion mit Bessel-Funktionen —
  machbare Rechnung, kein prinzipielles Hindernis. **Offen.**
- **Zusammenführungen:** P19 (CMB-Wegverlängerung) → in **P14** aufgegangen;
  P28 (Exponent für z_*) → in **P20** aufgegangen. Beide erscheinen nicht
  mehr als eigene Zeilen. Verweise in 267/268 entsprechend umgestellt
  (P28→P20, P19→P14/P20).
- Status-Header in 190 auf P1–P30 (DE) bzw. R1–R30 (EN) aktualisiert,
  Nachträge vom 6. Juni ergänzt.

### Korrektur des z_*-Exponenten (Dok. 267 DE+EN)
| Status | **erledigt** | ✓ Juni 2026 |

z_* ≈ 875 als **Referenzwert** in richtiger Größenordnung markiert (nicht als
FFGFT-Resultat): (λ_e/L₀)^(1/ln(1/ξ)) ≈ 875. Der Exponent 1/ln(1/ξ) ist nicht
aus der T⁴-Geometrie hergeleitet (P28→P20). Der frühere DeepSeek-Wert z_*=1103
(Exponent 8,55) bleibt verworfen — nicht aus ξ herleitbar.

### Skripte überarbeitet (Namen beibehalten — Mail-Links bleiben gültig)
| Status | **erledigt** | ✓ Juni 2026 |

- **ffgft_cmb_t4_peaks.py** (NEU erstellt): reproduziert die Dok.-268-Herleitung
  exakt (Jacobi-Entartung → Bose-Einstein → Peaks {3,18,42,78} →
  Beobachter-Faktor 3 → Verhältnisse 1:2,449:3,742:5,099, max. Abw. 1,63 %).
- **verify_cmb_peaks_final.py** (neu geschrieben): verifiziert jetzt die
  T⁴-Herleitung unabhängig (Entartung per Direktzählung ≡ Jacobi-Formel),
  nicht mehr das alte DeepSeek-Skript. Grenzt absolute Skala (P20) ehrlich ab.
- **hausdorff_wegverlaengerung.py**: Widerspruch zwischen Hausdorff-Potenzgesetz
  und Dok. 182 (Exponential) bleibt **bewusst offen** (P14/P19), jetzt explizit
  als ungelöster Punkt markiert, keine Auflösungsbehauptung.
- **verify_z_star_final.py, lcdm_circularity.py, wbe_t4_flrw.py,
  ffgft_lcdm_zeitverlauf.py**: inhaltlich geprüft (z_*=875, H₀=66,19,
  α=D_f/(D_f+1)=0,75 → w=−3/4, Drei-Phasen-Vergleich) — korrekt, unverändert.

### Korrektur eigener früherer Aussagen (intern, ehrlich)
Aus dem 6. Update (Trompeten-Mechanismus) überholt:

- **„B = 1/3 aus Dimension D=4, reine Dimensionszahl"** war eine Überdehnung.
  Der Faktor 3 ist der 3D-Beobachter-Mechanismus (k_obs²), nicht ein
  Trompeten-Randanpassungsterm B. Der Trompeten-Mechanismus ℓ_n=A·n/(1+B/n)
  bleibt als phänomenologische Form möglich, aber B=1/3 ist ein **Ansatz**
  (Analogie), keine strenge Herleitung — in Dok. 267 entsprechend markiert.
- Die Begründung des Faktors 3 über „fraktale Dispersionsrelation" (Dok. 051)
  ist verworfen (siehe K4).

### Offene Punkte
- **268 EN**: englische Version von Dok. 268 noch nicht erstellt.
- **P20**: Herleitung des Exponenten 41/4 (≡ R_H/H₀) aus der T⁴-Geometrie.
- **P30**: strenge sphärische C_ℓ-Projektion der T⁴-Moden.
- **Skript-Referenzen in 267**: ffgft_lambda_im_messprozess.py und
  ffgft_zirkularitaet_symmetrie.py werden referenziert, sind aber noch nicht
  als Dateien vorhanden.
- **ZIP-Update**: Dok. 268 und P18–P30-Stand noch nicht im großen ZIP.

### Übersichtstabelle — Nachtrag (Fortsetzung 9)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-7.Update | ✓ Juni 2026 | Dok. 268 neu (DE, 19 S.): CMB-Peaks aus T⁴, 16 Schritte. K4: Faktor 3 = 3D-Beobachter (k_obs²), nicht fraktale Dispersionsrelation — korrigiert in 267 (DE+EN) und 268 (DE). Zwei-Filter-Aussage (Kompaktheit + Fraktalität als Bezugspunkte) in 267 (DE+EN) und 268 Schritt 10.6. P-Register in Dok. 190 konsolidiert: P18/P20/P29/P30 nachgetragen, P19→P14 und P28→P20 zusammengeführt (DE: P-Nr., EN: R-Nr.). z_*=875 als Referenzwert markiert. ffgft_cmb_t4_peaks.py neu; verify_cmb_peaks_final.py auf T⁴-Herleitung umgeschrieben; hausdorff-Widerspruch offen markiert. Offen: 268 EN, P20-Exponent 41/4, P30 C_ℓ-Projektion. |

---

## Revision Juni 2026 (8. Update) — Dok. 268 EN vollständig, Frequenzanalyse-Abschnitt, 267-Skripte

**Grundlage dieser Session:** Vervollständigung von Dok. 268 (englische
Gesamtversion, neuer Frequenzanalyse-Abschnitt), Konsistenz-Durchgang K4
auch in den Schritten 10/11 von Dok. 268, und Erstellung der zwei in
Dok. 267 referenzierten, bisher fehlenden Skripte.

### Dok. 268 EN — vollständige englische Version (neu)
| Status | **erledigt** | ✓ Juni 2026 |

Die komplette englische Fassung von Dok. 268 wurde von Grund auf erstellt
(22 Seiten, alle 16 Schritte plus beide Zusammenfassungen plus Abschnitt
10.7). Konsistent mit dem aktuellen DE-Stand: Beobachter-Mechanismus
(kein veraltetes D_f-Dispersionsbild), R-Nummern statt P, durchgehende
englische Fachterminologie. Verifiziert: keine deutschen Reste, keine
P-Nummern.

### Dok. 268 — Frequenzanalyse-Abschnitt 10.7 (neu, DE eingebaut + EN)
| Status | **erledigt** | ✓ Juni 2026 DE+EN |

Neuer Abschnitt „Was die Peak-Verhältnisse modellfrei aussagen“
(zwischen 10.6 und Schritt 11), aus der Spektral-/Frequenzanalyse-Sicht,
ohne T⁴-Annahme:

- **10.7.0 Begriffsklärung „akustisch“:** kein Schall, keine
  Zeitschwingung, nur räumliche Verteilung am Himmel gemessen.
  „Akustisch“ ist ΛCDM-Erbe (Druckwellen im Plasma) und trägt eine
  Modellannahme im Namen. Zwei verschiedene „Frequenzen“ getrennt:
  (A) Photonen-Frequenz ~160 GHz (Hz, zeitlich) vs. (B) Fleckenmuster
  ℓ=220,537,… (Winkel, räumlich). Die Peaks gehören zu (B).
  Sprachregelung: „Winkelspektrum-Peaks“ statt „akustisch“; Resonator
  nur als mathematische Analogie.
- **10.7.1 Krümmung real:** Abstände 317/273/310/330 nicht konstant,
  Verhältnisse sub-linear → gerade Obertöne ausgeschlossen, deutlich
  über Messunsicherheit.
- **10.7.2 missing-fundamental-Falle:** linearer Fit gibt negativen
  Offset (−72) → unphysikalischer „Grundton bei ℓ<0“ → die lineare
  Deutung ist ein Differenzbildungs-Artefakt.
- **10.7.3 Gitter-Grundton:** ℓ/√(|n|²) ≈ 126 (Streuung 1,6%), ein
  Parameter, sparsamste Deutung der Krümmung.
- **10.7.4 Grundton ≠ erster Peak:** c≈126 entspricht |n|²=1 bei ℓ≈126
  (Sachs-Wolfe-Plateau, kein Peak); echte aber unsichtbare Mode (1,0,0,0)
  erfüllt die 3D-Symmetriebedingung nicht. Schwach falsifizierbare
  Konsistenzbedingung.
- **10.7.5 Keine Größe des Universums:** θ=L/D_A ist nur ein Verhältnis;
  derselbe Winkel passt zu „groß und weit“ wie „klein und nah“; D_A ist
  Modell-Output. Orgelpfeifen-Vergleich: die Wellenlängen-Methode bräuchte
  Wellenlänge-in-Metern + bekanntes Medium; bei der CMB fehlt beides, und
  das ΛCDM-„Medium“ c_s(z) ist selbst aus Dichte/Expansion/Metrik
  herausgerechnet (dreifach modellabhängig). Messung ist maßstabslos.
- **10.7.6 Sicher vs. nicht ablesbar + Abtastgrenze:** breite Peaks
  (~1–3%), FFGFT-√-Gitter vs. ΛCDM-Dispersion nicht unterscheidbar.

### K4-Konsistenz in Dok. 268 Schritte 10/11 (vervollständigt)
| Status | **erledigt** | ✓ Juni 2026 DE (EN gleich erstellt) |

Die im 7. Update für 267/268 begonnene K4-Korrektur (Faktor 3 =
3D-Beobachter, nicht fraktale Dispersionsrelation) wurde in Dok. 268 an
allen verbliebenen Stellen vollzogen: Doppel-Resonator-Tabelle 10.2
(„System 2“: 3D-Beobachterprojektion statt „fraktale Mannigfaltigkeit /
√D_f“), Schritt 10.4 (Beobachterprojektion statt „D_f in der
Dispersionsrelation“), Schritt 11.1-Tabelle (Faktor 3 = Raumdimensionen
statt „D_f·{…}“), Schritt 11.3 (Selektionsmechanismus/C_ℓ-Projektion
statt „k²_eff=D_f·k²“), Bezug-Block (Dok. 050/051 T⁴-Topologie statt
„Tetrad-Formalismus“). Verifiziert: keine „k²_eff=D_f·k²“- oder
„√D_f-Skalierung“-Stelle mehr in 268.

### Zwei fehlende 267-Skripte erstellt
| Status | **erledigt** | ✓ Juni 2026 |

Dok. 267 referenzierte zwei Skripte, die nie existierten. Beide erstellt,
konsistent mit dem Dokument (θ₁=π/A, A=303,6, H0=66,19, H0·L_res=458 km/s):

- **ffgft_lambda_im_messprozess.py:** die Längenskala im Messprozess.
  R_H aus ξ (extern via Exponent 41/4, P20); der gemessene Winkel legt
  nur das Produkt H0·L_res=458 km/s fest, nicht H0 allein. Demonstration:
  derselbe Winkel für jedes H0.
- **ffgft_zirkularitaet_symmetrie.py:** die symmetrische Zirkularität.
  Beide Modelle (ΛCDM r_s≈147 Mpc / FFGFT R_H) müssen eine absolute
  Skala hineinstecken; keines gewinnt aus den Peaks ein modellneutrales
  H0. FFGFT-Gegenpart zu lcdm_circularity.py — keine einseitige Kritik.
  Fairer Vergleich: Sparsamkeit (FFGFT eine Skala) vs. Verankerung
  (ΛCDM breiter getestet).

Damit sind alle in Dok. 267 referenzierten Skripte vorhanden
(ffgft_lambda_im_messprozess, ffgft_zirkularitaet_symmetrie,
lcdm_circularity).

### Hinweis zu den Kernzahlen (E0/H0-Konvention)
Bei der Skripterstellung fiel auf: CODATA-Massen (m_e=0,51099895 MeV,
m_μ=105,6583755 MeV) geben E0=√(m_e·m_μ)=7,348 MeV und H0=65,73 km/s/Mpc.
Die Kernzahl-Referenz nennt E0=7,398 MeV und H0=66,19 (leicht andere
Massenkonvention). Die Skripte verwenden H0=66,19 als FFGFT-Referenz
(konsistent mit verify_z_star_final, lcdm_circularity). Die ~0,5 km/s/Mpc
Differenz ist eine Rundungs-/Konventionsfrage, nicht inhaltlich.

### Offene Punkte (Stand nach 8. Update)
- **P20**: Herleitung des Exponenten 41/4 (≡ R_H/H₀) aus der T⁴-Geometrie.
- **P30**: strenge sphärische C_ℓ-Projektion der T⁴-Moden.
- **ZIP-Update**: großes ZIP mit Dok. 268 DE+EN, P18–P30, neuen Skripten
  noch nicht aktualisiert.

### Übersichtstabelle — Nachtrag (Fortsetzung 10)

| ID | Status | Bemerkung |
|----|--------|-----------|
| Juni-8.Update | ✓ Juni 2026 | Dok. 268 EN vollständig (22 S., alle 16 Schritte + 10.7). Frequenzanalyse-Abschnitt 10.7 (DE eingebaut + EN): Begriffsklärung „akustisch“, missing-fundamental-Falle, Gitter-Grundton c≈126, keine Größe des Universums (Orgelpfeifen/Medium-Argument), Abtastgrenze. K4-Konsistenz in 268 Schritte 10/11 vollzogen (keine D_f-Dispersionsstelle mehr). Zwei fehlende 267-Skripte erstellt (ffgft_lambda_im_messprozess, ffgft_zirkularitaet_symmetrie), konsistent mit Dok. 267 (H0·L_res=458 km/s). Offen: P20-Exponent, P30, ZIP-Update. |

---

## 9. Update (Juni 2026) — Dok. 269 + Gesamtarchiv

### Neues Dokument: Dok. 269 (FFGFT ↔ RA/PMT, bidirektional)
Vergleich von FFGFT mit dem RA/PMT-Architekturschema (J. T. Guevara,
*Regional Arenas / Perception Mechanism Theory*, Teil I–III). DE+EN, je 6 S.
Zwei Richtungen in einem Dokument:
- **Richtung A**: FFGFT bewertet RA/PMT mit dem Sechs-Achsen-Operator
  (Dok. 265) → vier Achsen ohne Berührung, zwei nur Meta-Ebene →
  Kategorienverschiedenheit, einziger Überlapp = Schichtungs-Disziplin.
- **Richtung B**: RA/PMT-Raster (RA4→RA1.5→RA2→RA1) auf FFGFT angewandt →
  FFGFT hat kein RA1.5 und braucht keines (statisch, keine Auswahl aus
  vielen); legt versteckte Annahme im Raster offen; RA1.5 ist nach
  Guevaras eigener RA3-Definition selbst ein Residuum.
- Synthese: Gegenpole derselben Frage; faire Würdigung als Meta-Werkzeug;
  zwei deklarierte Residuen. Bezug: Dok. 265, 267, 203, 190.

### Gesamtarchiv aktualisiert (dieses ZIP)
Das große ZIP (FFGFT_v1_1_2_Komplett) ist jetzt auf aktuellen Stand gebracht:
- **Sources/ch/**: 190 (DE+EN, aktualisiert mit konsolidiertem P-Register
  P18–P30), 265, 267, 268, 269 (je DE+EN) neu eingespielt.
- **Sources/wr_standalone_A4/**: Wrapper für 265, 267, 268, 269 (DE+EN).
- **Einzeldokumente_A4/**: gebaute PDFs für 190 (aktualisiert), 265, 267,
  268, 269 (Deutsch + English).
- **Dok267_268_Skripte/** (neu): 9 Python-Skripte zu 267/268
  (ffgft_cmb_t4_peaks, ffgft_lambda_im_messprozess, ffgft_lcdm_zeitverlauf,
  ffgft_zirkularitaet_symmetrie, hausdorff_wegverlaengerung,
  lcdm_circularity, verify_cmb_peaks_final, verify_z_star_final,
  wbe_t4_flrw).

### Offene Punkte (Stand nach 9. Update)
- **P20**: Herleitung des Exponenten 41/4 (≡ R_H/H₀) aus der T⁴-Geometrie.
- **P30**: strenge sphärische C_ℓ-Projektion der T⁴-Moden.
- (ZIP-Update erledigt.)

---

## Revision 7. Juni 2026 (9. Update) — CMB-Peak-Sektor ehrlich abgestuft, Forward-Anharmonizität (P31), Render-Patches

**Anlass:** Eine durchgängige Vorwärts-Prüfung (ohne aus den Messdaten abgelesene Größen) des CMB-Peak-Sektors. Ergebnis: Teile des 6.–8. Updates waren überdehnt und werden hier ehrlich zurückgenommen; gleichzeitig ein echter, parameterfreier Forward-Gewinn nachgetragen.

### P29 — Peak-Auswahlregel (Korrektur gegenüber 7. Update)
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 268 (Schritt 11.1, 17), 190 |
| Status | **offen** (vorher fälschlich „teilweise beantwortet") |
| Eingetragen | 7. Juni 2026 |
| Erledigt DE | ✓ 7. Juni 2026 |
| Erledigt EN | ✓ 7. Juni 2026 |

**Falsch (7. Update):** Die Peak-Auswahl {3,18,42,78} sei durch den 3D-Beobachter-Mechanismus (Faktor 3) bereits *teilweise* hergeleitet.
**Korrekt:** Der Faktor-3-Filter schließt $|n|^2=30$ (=3·10) **nicht** aus. Mit Intensität $I(30)=13{,}2 > I(42)=7{,}6 > I(78)=1{,}7$ müsste bei $\ell\approx696$ ein Peak vergleichbarer Stärke liegen — er fehlt in der Beobachtung. Die Auswahl genau {3,18,42,78} ist damit **nicht** vorwärts hergeleitet, sondern aus den gemessenen Verhältnissen abgelesen (Retrodiktion).

### P30 — strenge sphärische C_ℓ-Projektion (Korrektur gegenüber 7. Update)
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 268 (Schritt 17), 190 |
| Status | **offen** (vorher „machbare Rechnung, kein prinzipielles Hindernis") |
| Eingetragen | 7. Juni 2026 |
| Erledigt DE | ✓ 7. Juni 2026 |
| Erledigt EN | ✓ 7. Juni 2026 |

**Falsch (7. Update):** Die strenge C_ℓ-Projektion sei nur noch eine „machbare Rechnung, kein prinzipielles Hindernis".
**Korrekt:** Die naive Bessel-Projektion des dichten T⁴-Spektrums auf $C_\ell$ wäscht die diskrete Peak-Struktur **aus** (resultierendes Maximum bei $\ell\approx122$, keine Serie {3,18,42,78}). Es fehlt nach wie vor eine physikalische Quell-/Fensterfunktion, die genau diese Moden selektiert. Punkt bleibt **offen**.

### P31 (R31) — Geometrische Anharmonizität der Peak-Verhältnisse (NEU, Forward-Gewinn)
| Feld | Inhalt |
|------|--------|
| Betroffene Dok. | 268 (Schritt 17, neu), 190 |
| Status | **teilweise hergeleitet** (Führungsverhalten forward, Restabweichung offen) |
| Eingetragen | 7. Juni 2026 |
| Erledigt DE | ✓ 7. Juni 2026 |
| Erledigt EN | ✓ 7. Juni 2026 |

**Befund:** Forward erzeugt das symmetrische T⁴-Resonanz-Rückgrat ($k^2=3n^2$) die *harmonische* Reihe $1:2:3:4:5$ — „zu sauber". Die beobachtete *Anharmonizität* $1:2{,}44:3{,}68:5{,}09$ folgt **parameterfrei** aus der Kodimension-1-Projektion: Letztstreufläche ⇒ $D_\mathrm{eff}=D_f-1=2-\xi\approx2$ ⇒ Bessel-Index $\nu=-\xi/2\approx0$ ⇒ $J_0$-Membran ⇒ $1:2{,}30:3{,}60:4{,}90$, Treffer auf $\sim5\,\%$, ohne Modenauswahl. Anharmonizität ist bei $D=2$ maximal (bei $D=1,3$ harmonisch). Restabweichung ($D\approx1{,}86$) ist **nicht** aus $\xi$ herleitbar und liegt in der Größenordnung der Messunsicherheit. Der Teilchensektor ($\alpha$, Leptonmassen, Koide) ist davon unberührt (direkte $\xi$-Potenzen).

### Dok. 268 — Überarbeitung
| Status | **erledigt** | ✓ 7. Juni 2026 DE+EN |

- **Überblick** trennt jetzt klar **(A) Retrodiktion** (Verhältnis-Match, rückwärts) von **(B) Forward-Anharmonizität** (geometrisch, parameterfrei).
- **Schritt 11.1** korrigiert: die frühere Behauptung „{1,6,14,26} folgt aus ξ allein als lokale Maxima" war falsch (echte Forward-Maxima sind dicht {3,6,10,14,18,22,26,30,…}); jetzt als Retrodiktion markiert.
- **Schritt 17 (neu):** vollständige Forward-Prüfung (naive Bessel-Auswaschung, $|n|^2=30$, Resonator-Vergleich $J_0$, Kodim-1-Herleitung, Restabweichung, geschichtete Zusammenfassung).
- **Schritt 9** (KDP-Rand): Tabelle von `{clll}`+`\newline` (207 pt Überlauf) auf feste `p{}`-Breiten umgestellt.

### Dok. 190 — Korrekturverzeichnis
| Status | **erledigt** | ✓ 7. Juni 2026 DE+EN |

- P-Register-Tabelle (P1–P31) von `\resizebox{\textwidth}{!}{tabular}` (kein Seitenumbruch, lief unten über) auf **longtable** umgestellt — bricht jetzt über Seiten mit Kopf-Wiederholung.
- P29/P30 auf **offen** zurückgesetzt, **P31** ergänzt; neuer Prosa-Abschnitt „Präzisierung 14".
- Status-Header auf P1–P31 / R1–R31.

### Skripte (Dok267_268_Skripte/)
| Status | **erledigt** | ✓ 7. Juni 2026 |

- **Neu (5):** `forward_t4_spektrum.py` (echte Forward-Maxima, dicht), `naive_bessel_projektion.py` (Auswaschung, ℓ≈122), `resonator_vergleich.py` ($J_0$ vs. harmonisch), `dimension_anharmonizitaet.py` (Anharmonizität max. bei D=2), `spektral_dimension.py` (schwach-fraktal bleibt ≈2).
- **Aktualisiert (2):** `ffgft_cmb_t4_peaks.py`, `verify_cmb_peaks_final.py` — Rechnung korrekt, Schlussfolgerung von „Forward-Herleitung" auf „Retrodiktion + Forward-Anharmonizität" präzisiert (Korrektur-Kopf ergänzt).

### Patch — \checkmark (Sources/pri-end/T0_preamble_patches.tex)
| Status | **erledigt** | ✓ 7. Juni 2026 |

`\checkmark` (U+2713) fehlt in Libertinus Math und erschien korpusweit als `.notdef`-Kasten (u.a. Dok. 268 Abschnitt 12.1, Dok. 190). In `T0_preamble_patches.tex` idempotent durch ein Zapf-Dingbat-Häkchen ersetzt (mathmodus-sicher, kein amssymb). Methode wie bisher: jede Änderung in DE und EN geprüft.

### Wrapper
- **Sources/wr_standalone_A4/190_T0_Korrekturen_De.tex:** Titelblock ergänzt (`\title`/`\maketitle`/`\tableofcontents`) — der DE-Wrapper hatte als einziger keinen Titel; an den EN-Wrapper angeglichen.

### Offene Punkte (Stand nach 9. Update)
- **P20**: Herleitung des Exponenten 41/4 (≡ R_H/H₀) aus der T⁴-Geometrie.
- **P29**: physikalische Begründung, warum genau {3,18,42,78} und nicht z.B. $|n|^2=30$.
- **P30**: Quell-/Fensterfunktion, die in einer strengen C_ℓ-Projektion die diskreten Peaks selektiert (naive Projektion wäscht aus).
- **P31-Rest**: Restabweichung $D=2\to1{,}86$ nicht aus ξ herleitbar (vermutlich Messunsicherheit).

---

## 10. Update (7. Juni 2026) — P20 verschärft, P32 neu (H₀-Bereinigung vermerkt)

Anlass: Diskussion über das Rand-/Maßstab-/Relationalitäts-Problem. Ergebnis: ein Maßstab ist per Definition eine Relation; es kann kein inneres Glied geben, das eine *absolute* Skala festsetzt. Nur dimensionslose Verhältnisse sind real. Für R_H/ℓ_P heißt das: die **Form** liegt fest, der **Faktor** (Exponent 41/4) nicht.

### Dok. 190 — P20/R20 verschärft
| Status | **erledigt** | ✓ 7. Juni 2026 (DE + EN) |

- Aus „R_H externe Eingabe, offen" wird die präzise Aussage: die **Form** ist fest (dimensionsloses ξ-Verhältnis R_H/ℓ_P), der **Faktor** wird **nicht** hergeleitet und **darf nicht gefittet** werden (Fitten = Retrodiktion).
- FFGFT ist nicht der traditionelle Maßstab → der Faktor wird als **deklarierte externe Kalibrierung** aus ΛCDM übernommen (Einheitenwahl, **nicht** Physik-Übernahme), mit dem konvergierten Wert einzusetzen, sobald die H₀-Spannung (~67 vs. ~73) geklärt ist; bis dahin parametrisiert.
- Der importierte Wert zählt **nicht** als FFGFT-Bestätigung. Innere Vorwärts-Herleitung des Faktors bleibt das offene Ziel (P20).

### Dok. 190 — P32/R32 neu (Vermerk)
| Status | **vermerkt** (Bereinigung aufgeschoben) | ✓ 7. Juni 2026 (DE + EN) |

- Folgt aus P20: H₀ / die absolute Skala ist eine **importierte** Kalibrierung, nicht hergeleitet.
- Alle Dokumentstellen, die H₀ als **FFGFT-Resultat** darstellen, sind korpusweit zu bereinigen („importiert/deklariert" statt „hergeleitet").
- **Vorerst nur vermerkt**; die korpusweite Bereinigung ist als offener Punkt registriert, aber bewusst aufgeschoben.

### Offene Punkte (Stand nach 10. Update)
- **P20**: innere Vorwärts-Herleitung des Faktors 41/4 (≡ R_H/ℓ_P) aus ξ/T⁴-Geometrie — Form fest, Faktor offen.
- **P29**: warum genau {3,18,42,78} und nicht z.B. |n|²=30.
- **P30**: Quell-/Fensterfunktion für die strenge C_ℓ-Projektion (naive Projektion wäscht aus).
- **P31-Rest**: Restabweichung D=2→1,86 (vermutlich Messunsicherheit).
- **P32**: korpusweite Bereinigung der H₀-als-hergeleitet-Aussagen (vermerkt, aufgeschoben).

---

## 11. Update (8. Juni 2026) — Dok. 270 aufgenommen und überarbeitet

### Dok. 270 „Projektionskette T⁴ → T⁰" — neu
| Status | **aufgenommen** (DE + EN, A4-Standalone, je 9–10 S.) | ✓ 8. Juni 2026 |

Inhalt: Die Reduktion T⁴ → T⁰ ist **nicht** gleichförmig, sondern zerfällt in qualitativ verschiedene Operationen:
- **Typ I** — Masse↔Zeit-Dualitäts-Dekompaktifizierung (T̃·m=1): *einbettend*, im Modeninhalt informationserhaltend; nur die Sichtbarkeit der Kompaktheit überlebt als Spektralsignatur (ξⁿ).
- **Typ II** — räumliche Projektion (D3→D2→D1→D0): streng verlustbehaftet, nicht reversibel, von der Rekursion **nicht** kompensiert; Stufe D3→D2 = holographisches Prinzip.
- **Typ III** — repräsentationelle Übersetzung T⁴ ↔ Hilbertraum/Matrix (Dok. 230/206/231): *bijektiv/verlustfrei*, gerade weil keine geometrischen Extra-Dimensionen hinzukommen.

Zentrales Resultat: Asymmetrie „geometrisch-runter verlustbehaftet vs. repräsentationell-hoch bijektiv". Prüfbarkeit der Identifikation t∼t+R_m über T_rev und CHSH-Abweichung ∼ξ (Dok. 147/183); linear/log-Regime-Trennung explizit.

### Dok. 270 — Überarbeitung nach Review
| Status | **überarbeitet** (DE + EN) | ✓ 8. Juni 2026 |

- **R_H als importierte Skala gekennzeichnet (P20-konsistent).** Neue Bemerkung „Status der beiden Skalen": R_H ist die *deklarierte externe* (importierte) kosmologische Skala, **nicht** aus ξ hergeleitet; intrinsisch ist nur die Form (Radienklassen-Trennung bzw. R_H/ℓ_P), nicht der Faktor (Verweis Dok. 190, P20). Verhindert die Lesart „R_H als Strukturgröße des Torus" — folgt P32.
- **Stufe 1 in Ia/Ib getrennt.** Die bisher als „Typ I" gebündelte Stufe 1 trennt jetzt **(Ia)** Massekreis-Dualität (T̃m=1) von **(Ib)** räumlicher *Limes*-Dekompaktifizierung (R→∞) — verschiedener Mechanismus, gleicher einbettender Charakter. Offener Punkt 3 von „Frage" auf „präzisiert" umgestellt.
- **R_m-Turmspitze präzisiert.** R_m ∼ ξℓ_P setzt die Spitze des KK-Turms (1/R_m ∼ ξ⁻¹ m_P, transplanckisch); beobachtete Massen liegen ξⁿ-suppressed darunter (Verweis 159, 258/259).

Kompiliert sauber (lualatex, Libertinus): 0 fehlende Glyphen, 0 ungelöste Referenzen, 0 Überlauf; Underbrace/Box/deutsche Anführungszeichen korrekt.

### Offener Punkt (von Dok. 270, vom Autor gegenzulesen)
- **R_m vs. 41/4.** Zahlencheck, dass R_m ∼ ξℓ_P (1/R_m ∼ ξ⁻¹ m_P) konsistent ist mit der Parametrisierung E_H = E₀ξ^{41/4} (Dok. 182) und der Massenleiter (Dok. 159, 258/259) — gerahmt, aber noch nicht numerisch bestätigt.

---

## 12. Update (8. Juni 2026) — P33/R33: Status des 5⁴-Faktors in ξ

### Dok. 190 — P33/R33 neu (deklariert)
| Status | **deklariert/vermerkt** (DE + EN) | ✓ 8. Juni 2026 |

Anlass: Suche im Korpus nach einer Vorwärts-Herleitung des magnitudentragenden Faktors **5⁴ = 625** in der Primfaktorform ξ = 4/30000 = 1/(3·2²·5⁴).

Befund (Doks. 009, 042, 056, 181, 133, 159 durchsucht):
- Die **Form** von ξ ist vorwärts: 4/3 (reine Quarte, harmonisch, Dok. 042/159) gibt die Leitziffer; 3 = Raumdimensionen, 2² = 4 = Raumzeit liest man aus der Geometrie.
- Der **magnitudentragende Faktor 5⁴** (→ 10⁻⁴) ist **nicht** vorwärts hergeleitet. Er wird nur *behauptet* („emergiert aus der fraktalen Struktur", Dok. 009; „kodiert die Symmetriestruktur", Dok. 181 — dort zirkulär über 30000/4) bzw. der Wert ist *empirisch* (Dok. 042: aus dem Higgs-Sektor gemessen 1,3194×10⁻⁴, ~1 % neben dem Ideal 4/30000). In Dok. 133/159 kommt 5⁴ nicht vor.

Konsequenz: **P33/R33** hält offen fest, dass die Magnitude von ξ bei der **intuitiven** (harmonisch/Euler-Tonnetz) bzw. **empirischen** Begründung bleibt und so *deklariert* wird — nicht als Vorwärts-Herleitung ausgegeben. Struktur-Parallele zu P20 (Form fest, Faktor offen), eine Ebene tiefer.

Auch die Dezimal-Frage ist damit sauber abgelegt: ξ ist basis-unabhängig (Primfaktorform 1/(3·2²·5⁴); „×10⁴" ist nur das Dezimalbild von 2⁴·5⁴) — der frühere Basis-Einwand greift nicht (Dok. 009 explizit; gestützt von Dok. 253/057). Die offene Stelle ist allein die Vorwärts-Herkunft des 5⁴.

Statuskopf Dok. 190: P1–P33 / R1–R33 (P33/R33 deklariert).

---

## 13. Update (8. Juni 2026) — P34/R34: Dimensionsstruktur & SI-Umrechnungen

### Dok. 190 — P34/R34 neu (präzisiert)
| Status | **präzisiert/deklariert** (DE + EN) | ✓ 8. Juni 2026 |

Anlass: Frage „warum sind T⁴ und T³+Zeit die optimalen Dimensionen?" und der Zusammenhang mit der Unverzichtbarkeit der SI-Umrechnungen für die c-/Zeit-Potenz.

Befund/Präzisierung (Dok. 181 stellt D=4 als „folgt zwingend / kein Postulat" dar — das ist überstellt):
- **3+1 ist empirische Eingabe** — keine Theorie leitet die Dimensionszahl her (SM, ART nehmen sie an; Stringtheorie scheitert am Landschaftsproblem).
- **Vorwärts** sind nur: (i) Periodizität (Divergenzfreiheit), (ii) Torus-statt-Kugel (π₁≠0, stabile Windungen), (iii) **Minimal-Suffizienz** — 4 statt naiv 5, weil die Dualität T̃·m=1 einen Kreis Masse *und* Zeit tragen lässt, (iv) verlustfreie (bijektive) **Hilbert-Repräsentation** (Typ III, Dok. 270/206/230).
- Die **bloße Zahl 4** ist *nicht* vorwärts erzwungen; die „4 aus ξ"-Begründung in Dok. 181 ist zirkulär bzw. basis-abhängig.

**Zusammenhang mit den Einheiten (c-Potenz):** Die Vier-Kreis-Struktur *ist* die Exponenten-Buchhaltung der SI-Umrechnungen — c = Raum↔Zeit-Brücke (die drei T³-Kreise gegen die Zeitrichtung), ħ = Masse↔Zeit-Brücke (S¹_m, T̃·m=1). Darum sind die SI-Faktoren für die **c-Potenz** und die **Zeit-Potenz** unverzichtbar: c=ħ=1 kollabiert L,T,M zu einer Achse und vernichtet genau die Exponentenstruktur. T⁴ (Masse-Lesart) und T³+Zeit (Zeit-Lesart) sind dasselbe Objekt.

Zusammenfassung der Dimensions-Linie: **T⁴/T³+Zeit ist die minimal-suffiziente, dual-ökonomische und Hilbert-treue Konfiguration gegeben 3+1** — die Stärke ist Ökonomie + Treue, nicht eine Eindeutigkeit der Zahl. Damit dieselbe Signatur wie bei P20 (Kosmo-Faktor) und P33 (ξ-Magnitude): **Struktur/Form vorwärts, Zahl Eingabe/abgelesen.**

Statuskopf Dok. 190: P1–P34 / R1–R34 (P34/R34 präzisiert).

---

## 14. Update (8. Juni 2026) — Dok. 270 erweitert: „Warum genau vier Kreise?"

### Dok. 270 — neue Synthese-Sektion
| Status | **erweitert** (DE + EN) | ✓ 8. Juni 2026 |

Neue Sektion „Warum genau vier Kreise? Minimal-Suffizienz, Einheiten und Veranschaulichung" (nach der Typ-III-Sektion), die die Dimensions-Diskussion in das Dokument einarbeitet — konsistent mit P34/R34:

- **3+1 ist Eingabe, nicht Herleitung** (keine Theorie leitet die Dimensionszahl her).
- **Minimal-Suffizienz: vier statt fünf** — die Dualität T̃·m=1 lässt einen Kreis Masse *und* Zeit tragen; damit kollabiert die naive 5 auf 4. Weniger → kein Massenspektrum/keine Zeit; mehr → überzählig.
- **Die vier Kreise als Einheiten-Buchhaltung** — c = Raum↔Zeit-Brücke (die drei Raumkreise), ħ = Masse↔Zeit-Brücke (S¹_m, T̃·m=1). Darum sind die SI-Umrechnungen für die *Potenz von c* und die *Potenz der Zeit* unverzichtbar: c=ħ=1 kollabiert L,T,M und vernichtet die Exponentenstruktur. (G ist dagegen *hergeleitet* — rekonstruiert aus ℓ_P, c, ħ, wofür es nur die SI-Relationen braucht, Dok. 012/056 — und trägt keinen freien Faktor; der einzige freie Faktor sitzt in der kosmologischen Absolutskala R_H, Exponent 41/4, P20.)
- **Dieselbe Struktur als Hilbert-Veranschaulichung** — zwei Lesarten einer Bijektion: generativ (T⁴ → ℋ, Dok. 206) und veranschaulichend (ℋ wird durch die 4D-Geometrie anschaulich). „Höherdimensional" ≠ „fundamentaler". Treue, weil generativ — kein Cartoon.
- **Zusammenfassung:** T⁴/T³+Zeit = die minimal-suffiziente, dual-ökonomische, Hilbert-treue Konfiguration gegeben 3+1; Stärke = Ökonomie + Treue, nicht Eindeutigkeit der Zahl. Signatur wie P20/P33/P34: Struktur vorwärts, Zahl Eingabe.

Sauber kompiliert (lualatex, Libertinus): DE 11 S., EN 11 S.; 0 fehlende Glyphen, 0 ungelöste Referenzen, 0 Überlauf; Brücken-Diagramm (\xrightarrow mit Underbraces), Boxen, ℋ korrekt.

---

## 15. Update (8. Juni 2026) — P33/P34 vorsichtiger formuliert

### Dok. 190 — P33/R33 und P34/R34 nachgeschärft (DE + EN)
| Status | **umformuliert** | ✓ 8. Juni 2026 |

Auf Hinweis: die ursprünglichen Korpus-Argumente (4/3 als „herleitbar", 5⁴ aus der fraktalen Struktur, „4 aus ξ") sind zwar **eher zirkulär**, aber **nicht aussagelos** — sie *zeigen Verhältnisse*, und Verhältnisse sind nach FFGFT gerade das Intrinsische. Entsprechend abgeschwächt:

- **P33/R33:** „er wird nur behauptet" → „die Begründungen … sind eher *zirkulär*". Neu: *Zirkulär heißt hier jedoch nicht aussagelos* — die Begründungen zeigen, dass der Wert in einer sinnvollen Verhältnis-/Harmoniestruktur sitzt (4/3 = Quarte; Primfaktorform 3·2²·5⁴ an Dimensionen geknüpft; Euler-Tonnetz). Schlussfolgerung unverändert korrekt: die **absolute Magnitude** bleibt eine *Eingabe* (intuitiv/empirisch), keine Vorwärts-Herleitung. Struktur-Parallele zu P20 jetzt: „Verhältnis fest, absolute Magnitude Eingabe".
- **P34/R34:** die „4 aus ξ"-Begründung (Dok. 181) ist „eher zirkulär bzw. basis-abhängig — sie *zeigt* eine Verknüpfung Zähler↔Dimensionszahl, *erzwingt* die Zahl aber nicht".

Inhaltliche Linie unverändert: **Struktur/Verhältnis vorwärts, Zahl/Magnitude Eingabe** (P20/P33/P34). Nur der Ton ist fairer: zirkuläre Begründungen haben Aussagekraft, weil sie Verhältnisse sichtbar machen.

---

## 16. Update (8. Juni 2026) — neuer Eintrag P35/R35 in Dok. 190

### Dok. 190 — P35/R35 hinzugefügt (DE + EN)
| Status | **neu** | ✓ 8. Juni 2026 |

Neuer Korrektur-Eintrag **P35/R35: „Umrechnungsfaktor nicht in den ξ-Exponenten absorbieren"** (Tabellenzeile + Nachtrag + Status-Header auf P1–P35/R1–R35):

- **Kernregel:** Jede Magnitude ist als ξ-Potenz schreibbar (M = ξ^(log M/log ξ)); „X = ξ^N" ist daher *für sich aussagelos*. Der Vorwärts-Inhalt liegt allein darin, ob der Exponent unabhängig aus ξ-Struktur folgt. Disziplin: absolute SI-Skala stets als ℓ_P · ξ^(struktureller Exponent) schreiben, ℓ_P explizit halten, nur den Rest-Exponenten prüfen.
- **Befund:** exakt sauber ist nur L₀/ℓ_P = ξ¹. Planck-referenziert ist R_H = ℓ_P · ξ^(−63/4) mit **63/4 = 41/4 + 11/2** — das Korpus-41/4 ist an E₀ (Teilchenskala), *nicht* an Planck referenziert; die 11/2 ist die verschwiegene Planck→E₀-Lücke. Die „schönen Brüche" (41/4, 11/2, 63/4) sind Rundungen gemessener Exponenten; der „−1,9 %"-Rest beim 41/4 ist der Rundungsrest, nicht ξ.
- Schärft P20/P33/P34. Betrifft die „aus ξ allein"-Aussagen in Dok. 182/163 (deren Entschärfung steht noch aus — vorerst nur in 190 vermerkt).

Sauber kompiliert (lualatex): DE 31 S., EN 26 S.; 0 fehlende Glyphen, 0 ungelöste Referenzen, 0 Überlauf; P35-Zeile visuell bestätigt. ZIP bewusst nicht neu gebaut (Feinschliff-Phase).

---

## 17. Update (8. Juni 2026) — neuer Eintrag P36/R36 in Dok. 190

### Dok. 190 — P36/R36 hinzugefügt (DE + EN)
| Status | **neu** | ✓ 8. Juni 2026 |

Neuer Korrektur-Eintrag **P36/R36: „R_H-Deutung — Hubble-Länge vs. Maximalskala vs. Universumsgröße"** (Tabellenzeile + Nachtrag + Status-Header auf P1–P36/R1–R36):

- **R_H = c/H₀ ist die Hubble-Länge** — die lokale Rate H₀ als Distanz, *nicht* die Größe des Universums und *nicht* der beobachtbare Horizont (Teilchenhorizont ≈ 3 R_H).
- Das tatsächliche Universum **übersteigt R_H** (mind. der beobachtbare Teil, real ≫, evtl. unendlich); nur eine *untere* Schranke ist messbar — Licht jenseits des Horizonts erreicht uns nie.
- Dok. 182s Bezeichnung **„Universum-Maximalskala"** ist allenfalls als *obere Skala des kosmologischen Torus-Sektors* (FFGFT-interne Identifikation) haltbar, nicht als Ausdehnung des Universums.
- Zu trennen: (a) Hubble-Länge c/H₀ (Rate→Länge), (b) FFGFT-Sektor-Maximalskala (Deutung), (c) reale Universumsgröße (größer/unbegrenzt).

Sauber kompiliert (lualatex): DE 31 S., EN 26 S.; 0 fehlende Glyphen, 0 ungelöste Referenzen, 0 Überlauf; P36-Zeile visuell bestätigt. Betrifft die Deutung von R_H in Dok. 182 (deren Anpassung steht noch aus — vorerst nur in 190 vermerkt). ZIP weiterhin gehalten. Ergänzt: in P36/R36 explizit die SI-Formel R_H = c/H₀ (H₀ gemessen, c Umrechnung) — die ξ^(−63/4)-Schreibweise ist nur diese Zahl umgeschrieben, kein eigener Inhalt.
 Zusätzlich ergänzt: R_H steht epistemisch auf einer Stufe mit ħ, c, G — nicht aus ξ erzeugt, sondern Eingabe/Umrechnung (H₀ gemessen, c Umrechnung wie ħ, G); der Unterschied ist allein die Skala (andere „Liga" — Quanten/Planck vs. kosmologisch).

---

## 18. Update (8. Juni 2026) — Quellen-Entrümpelung: kosmologische Skalen-Claims (Dok. 182, 026)

Die Quellen werden mit P35/P36 (Dok. 190) in Sync gebracht. Prinzip: kosmologische **Skalen**-Behauptungen von „Herleitung/parameterfrei" auf „Umschreibung/Eingabe" zurückgestuft; die **Form**-Aussagen (z∝ξd, Peak-Verhältnisse, B=1/3, L₀=ξ·ℓ_P) bleiben unangetastet.

### Dok. 182 (DE + EN)
- „R_H/L₀ = 6,49·10⁶⁴ folgt vollständig aus ξ allein" → der Exponent 41/4 ist an den gemessenen H₀ kalibriert, kein eigenständiges ξ-Resultat; R_H/L₀ ist die gemessene kosmische Skala in ξ-Schreibweise.
- „Hubble-Energie folgt direkt aus ξ" → „in ξ-Form geschrieben"; Zusatz: 41/4 nicht hergeleitet, sondern so gewählt, dass H₀ getroffen wird.
- 2× „Vollständig aus ξ abgeleitet, ohne freie Parameter" → „in ξ-Schreibweise; 41/4 an H₀ kalibriert".
- Abschnitts- und Tabellentitel entsprechend qualifiziert.
- Unverändert (war schon korrekt): die ξ→L₀-Kette und die Abgrenzung „R_H = Obergrenze des kosmologischen Sektors, nicht des Universums".

### Dok. 026 (DE + EN)
- „parameterfreie Vorhersage" und Tabellen-„parameterfrei" → „an H₀ kalibriert". Der „41/4 bedarf Begründung"-Caveat stand bereits im Dokument; der interne Widerspruch ist damit beseitigt.

### Geprüft, unverändert
- Dok. 025, 016: keine kosmologischen Skalen-Über-Claims (z∝ξd ist Form; „kein H₀ im statischen Universum" ist ehrlich).
- Dok. 163: L₀=ξ·ℓ_P ist korrekt (exakt/definitorisch). Enthält einen ħ-Claim („h emergiert parameterlos aus ξ"), der zur **Konstanten-Familie** (P33/P34) gehört, nicht zur kosmologischen Skala — offen für separate Entscheidung.

Sauber kompiliert (lualatex): 182 DE/EN 10 S., 026 DE/EN 8 S.; 0 fehlende Glyphen, 0 ungelöste Referenzen. ZIP weiterhin gehalten.

**Nachtrag zu 18. Update — Dok. 163 (DE + EN), Konstanten-Familie (light fix):**
Klarstellung: „Konstante aus ξ" ist *nicht* dasselbe wie der kosmologische Fall. ħ ist über die Kette ξ→α→ħ mit ξ verknüpft (α ist ein echter, isolierter, vorhergesagter ξ-Bezug). Entscheidend: alle SI-Werte sind aus ξ und der **einen** Einheiten-Kalibrierung ableitbar — die SI-Konvention selbst fügt nichts hinzu (c, ħ, e sind keine zusätzlichen freien Eingaben). Das unterscheidet die Konstanten vom kosmologischen R_H, der *zusätzlich* das gefittete 41/4 (= gemessener H₀) braucht. Daher kein Streichen, nur: „$h$ emergiert parameterlos aus ξ" → „$h$ folgt über die Kette ξ→α→h aus ξ; alle SI-Werte aus ξ + der einen Kalibrierung ableitbar, eine zusätzliche Konvention braucht es nicht"." Die L₀=ξ·ℓ_P-Inhalte bleiben unverändert (korrekt). Kompiliert: 163 DE/EN 18 S., 0 Glyphen/0 Referenzen.

---

## 19. Update (8. Juni 2026) — Korpusweiter Sweep: kosmologische Skalen-Claims

Selbständige Durchsuchung aller 395 Quelldateien nach kosmologischen Skalen-Über-Claims (H₀/R_H „parameterfrei / aus ξ / abgeleitet / Vorhersage"). Prinzip wie gehabt: **Skala → „an H₀ kalibriert / gemessene Eingabe"; Form/Verhältnisse/Konstanten/L₀ bleiben.**

### Gefixt (DE+EN, sofern beide vorhanden)
- **039** — „parameterfreie T0-Vorhersage H₀≈66,2" → „an H₀ kalibrierter T0-Wert".
- **054** (EN) — „(parameter-free, see Doc. 026)" → „(calibrated to H₀…)". (DE war schon sauber: „(siehe Dok. 026)".)
- **061** — Tabelle „parameterfrei" + Fußnote „parameterfreie T0-Vorhersage" → „an H₀ kalibriert".
- **145** (EN) — „parameter-free prediction" → „value, calibrated to H₀" (Caveat „41/4 requires justification" stand schon).
- **182** — Z. 160 boxed „R_H/L₀ = 6,49·10⁶⁴ (aus ξ allein)" → „(an H₀ kalibriert)". (Diese Zeile war im ersten Durchgang übersehen worden; Z. 238/242 waren bereits ehrlich.)
- **201** — „H₀≈66,2 (vollständige Herleitung)" → „… an H₀ kalibriert, nicht aus ξ hergeleitet".
- **263** — „R_H/L₀ ≈ 6,5·10⁶⁴, das selbst allein aus ξ folgt" → „… an H₀ kalibriert, nicht allein aus ξ".
- **268** — bald-Zeile „FFGFT leitet H₀ aus ξ^(41/4) ab" → „… schreibt H₀ als ξ^(41/4)". (Der Rest von 268 ist ehrlich: Abschnitt „Offene Frage", konditional „wenn 41/4 aus Geometrie folgt — noch offen"; Peak-Form B=1/3 bleibt.)

Alle gefixten Docs kompilieren clean (lualatex, 0 Glyphen/0 Referenzen). 054 hat keinen EN-Standalone-Wrapper (Edit dennoch im _ch gesetzt).

### Bewusst NICHT geändert
- **Legitim** (Ratio-/Form-Parameterfreiheit): 053, 054 (allg. „ξ ist Skalenverhältnis"), 190/268 Peak-Form (B=1/3, Gitterzahlen 3,18,42,78), z∝ξd, L₀=ξ·ℓ_P, 182 Z. 53 (parameterlos via die eine Kalibrierung).
- **Schon ehrlich**: 206 (disclaimt explizit, nicht alle Kosmo-Größen aus ξ), 144 (gehedged), 182 Z. 238/242, 268 „Offene Frage / Retrodiktion".

### Geflaggt — deine Entscheidung (sweeping „parameterfreie Physik bis Kosmologie")
- **068** (Z. 842/940), **086** (Z. 2), **201** (Z. 712/870 — DVFT „parameterfreies kosmologisches Modell"), **269** (Z. 236/228). Diese sind interpretativ: „parameterfrei" trifft auf die QM-/Ratio-Teile zu, nicht auf die kosmologische Absolutskala. Nicht automatisch geändert.

ZIP weiterhin gehalten.

---

## 23. Update (8. Juni 2026) — Neues Vergleichsdokument Dok. 271 (FFGFT ↔ HLV)

Neues **Dok. 271** „FFGFT (T0) und Helix–Light–Vortex (HLV) im Vergleich" (DE+EN, 6/5 S.), im Stil der Vergleichsdokumente 245/269. Inhalt:
- **Gemeinsame Achsen** (Übersichtstabelle): Substrat/Projektion, Zeitstruktur, Teilchen-Ontologie, generativer Kern, Rückgewinnungslimit, Falsifikationskanal.
- **Echte Isomorphismen vs. Oberflächen-Analogien**: Projektion aus höherer Dimension (ℤ⁵-Cut-and-Project ↔ T⁴→T⁰), Triadik (ψ=t+iφ+jχ ↔ Z₃, det=1−ξ), topologische Teilchen (Vortices ↔ Windungszahlen), harmonische Wurzel (φ/Fibonacci ↔ Euler-Tonnetz), Methodik (Recovery + Nullmodell).
- **Divergenzen/Komplementarität**: ξ-Samen mit Vorwärts-Vorhersagen (FFGFT) vs. reproduzierbares aperiodisches Substrat + Graph-Laplace-Testbed (HLV); aperiodisch vs. periodisch; Fundament-Reife; Bewusstseins-/Biogravimetrie-Schicht ausdrücklich ausgeklammert.
- **Unterscheidende Vorhersage (spektrale Gabel)**: periodisches T⁴ → ganzzahlige Harmonik-Leiter (CMB-Peak-Verhältnisse aus D=4) vs. aperiodischer Quasikristall → hierarchisches Lückenspektrum; skaleninvarianter Verhältnistest + periodisches Null-Gitter als Diskriminator.
- **Gemeinsame Leitplanke**: X=φ^N/ξ^N-Trivialität; Vorwärts-Gehalt nur in isolierten/vorhergesagten/präzisen dimensionslosen Verhältnissen.

Quellen: Krüger, Zenodo 10.5281/zenodo.20596861 und 10.5281/zenodo.20275888. Beide Sprachen kompilieren clean (0 Glyphen/Refs/Overfull). Archiv neu gebaut.

---

## 24. Update (8. Juni 2026) — Neues Dok. 272 (FFGFT & HLV, eingeordnet nach Dot Theory)

Neues **Dok. 272** (DE+EN, je 5 S.): Meta-Ebenen-Einordnung von FFGFT und HLV durch Stefaan Vossens **Dot Theory** — nicht paarweise (das ist Dok. 271), sondern *eine Ebene höher*, durch Dots kontextuell-operationales Raster:
- Achsen: Informations-Zugänglichkeit/Fragegeometrie, operationale Invarianten, Rekonstruierbarkeit/Projektionsverlust, Beobachter-Einbettung, empirischer Diskriminator (Admissibilität).
- Genutzt wird nur Dots **epistemische Routing-Funktion** (Architecture/Research-Programme, Mai 2026, mit IPI/Pascher), *nicht* dessen eigene physikalische ToE-/ψ-Schicht.
- Kernergebnis (Kommensurabilität): FFGFT (beobachterunabhängig/periodisch/vorwärts-prädiktiv) und HLV (beobachtereingebettet/aperiodisch/substrat-distinktiv) überlappen nur auf der **spektral-/Rückgewinnungs-Achse** — dort ist Dok. 271 lizenziert; auf Fragegeometrie und Beobachter-Einbettung verschiedene Regime (direkter Vergleich = Kategorienfehler). Erklärt nachträglich, warum 271 seine Vorbehalte brauchte.
- Rückbezug: Dok. 270 (Rekonstruierbarkeits-Typologie) und Dok. 190 P35 (ξ^N-Trivialität) als FFGFT-Bausteine in Dots Architektur.

Quellen: Vossen, Dot Theory (dottheory.co.uk); Krüger, HLV (Zenodo). Beide Sprachen kompilieren clean (0 Glyphen/Refs/Overfull). Archiv neu gebaut.

---

## 25. Update (8. Juni 2026) — Dok. 272 neu gefasst (aktueller Dot-Governance-Stand)

Dok. 272 (DE+EN, je 5 S.) **neu geschrieben** mit dem aktuellen Governance-Stand aus dem IPI-Direktaustausch mit Stefaan Vossen statt aus den publizierten Papieren:
- Die vier Aufzeichnungsobjekte: **Lexicon** (Struktur/Terminologie), **OAP** (Admissibilität), **Matrix** (Beziehungen), **FAH** (Framework Admissibility History; O0→O1/O2-Renderings, permanent/anfechtbar).
- Prinzipien: „declared provenance, not universal agreement" und „preservation of meaning-making, not allocation of meaning" (FAH = historisches Objekt, kein Wahrheitsanspruch).
- Die FFGFT↔HLV-Einordnung ist jetzt explizit als **Matrix-Eintrag** verortet und wird als **sekundäres Rendering (O2)** eingebracht — erklärte Lesart Paschers, O0 bei Krüger (HLV) und Vossen (Dot).
- Achsen den Lexicon-Begriffen zugeordnet; Admissibilität beider Frameworks im OAP geprüft; Dok. 270/190-P35 als Rückbezug in die Architektur.
- Nur Dots Governance-/Routing-Schicht genutzt (nicht dessen ToE/ψ-Schicht). Stand Juni 2026, ausdrücklich vorläufig/ablösbar.

Beide Sprachen kompilieren clean (0 Glyphen/Refs/Overfull). Archiv neu gebaut.

---

## 26. Update (9. Juni 2026) — Neues Dok. 274 (FFGFT im IPI-Feld, Zwei-Achsen-Landkarte)

Neues **Dok. 274** (DE+EN, je 6 S.): konsolidierende Landkarte der im Information-Physics-Institute diskutierten Rahmenwerke entlang **zweier orthogonaler Achsen** statt eines weiteren Paarvergleichs.

- **Achse 1 — Substrat-Geometrie (die Kristall-Achse):** FFGFT = periodisches Kristallgitter (T⁴) ↔ HLV = aperiodischer Quasikristall ↔ zufälliges Substrat (Kontrolle). Diese Triade ist genau die, die der Spektral-Testbed aus Dok. 271 messbar macht (⟨r⟩, Entartungsanteil, Lücken-Reichhaltigkeit; periodisch ⟨r⟩≈0/stark entartet, zufällig ⟨r⟩≈0,50/GOE, Quasikristall intermediär+lückenreich; |n|²-Leiter, in D=4 jede ganze Zahl per Lagrange).
- **Achse 2 — Primitiv:** Geometrie (FFGFT) ↔ Information (Vopson; stromabwärts Leavitt) ↔ Algebra/Hilbertraum (UMF) ↔ Selektion/Constraint (RA/PMT, RSG, UC, UIFT) ↔ Kontinuums-topologisch (αLGQV) ↔ Meta/Governance (Dot Theory).
- **Vopson aufgenommen** (fehlte in früheren Karten): informations-primitiv, Kontrast zu FFGFT ist Geometrie- vs. Informations-Seite derselben MEI-Relation (Dok. 251); Außen/Simulation in FFGFT strukturell ausgeschlossen. Leavitts Bit-Budget als stromabwärts von Vopson verortet.
- **Gesamtkarte** (Tabelle): Rahmenwerk · Eigner · Kategorie · Relation zu FFGFT · Vergleichsdok. Verweise auf 244/245/246/251/260/267-268/269/270/271/272/190-P35.
- **Erklärt** das wiederkehrende „Kategorieunterschied, nicht Widerspruch": FFGFT sitzt auf beiden Achsen am strukturell-geometrischen Pol und lässt die Slots (Selektor, Volumen→Rand-Naht, Constraint, Informations-Primitiv, Außen/Simulation) leer bzw. besetzt sie anders.
- **Ehrliche Residuen deklariert:** die Karte ist eine erklärte Lesart des Autors (Dot-Theory-O2), kein Eigenvokabular der Rahmenwerke; O0 verbleibt bei den Urhebern; die Substrat-Triade ordnet sauber nur FFGFT/HLV/Kontrolle (UMF, αLGQV liegen daneben); datiert/vorläufig.

Beide Sprachen kompilieren clean (0 Glyphen/Refs/Overfull, je 6 S.). Archiv neu gebaut.

---

## 27. Update (9. Juni 2026) — Skript-Ordner Dok271_274_Skripte/

Neuer Ordner **Dok271_274_Skripte/** (analog Dok263_Skripte / Dok267_268_Skripte): der reproduzierbare FFGFT-Spektral-Diskriminator zur Substrat-Achse von Dok. 271/274.

- `hlv_ffgft_spectral.py` (numpy-only, Seed 20260609): periodische Torus-Laplace-Spektren (D=2,3,4; D=4=T⁴), gradangepasstes Erdős–Rényi-Nullmodell, skaleninvariante Diskriminatoren (⟨r⟩-Statistik, Entartungsanteil, Lücken-Reichhaltigkeit), |n|²-Leiter (D=4 trifft jede ganze Zahl), Recovery-Limit-Fit. Eine Schnittstelle `analyze_spectrum(eigenwerte, name)` für extern gelieferte Spektren (HLV-Quasikristall) → apfel-mit-apfel.
- `README.md` (DE+EN) und Beispiel-Output `ffgft_periodic_spectral_summary.csv`.
- Damit löst der „beiliegendes Skript"-Verweis in Dok. 271/274 auf.

---

## 28. Update (9. Juni 2026) — Dok. 274 nachgeschärft, 086 erweitert, Skripte ins Archiv

**Dok. 274 (DE+EN, je 7 S.) — zwei Ergänzungen nach Stefaan Vossens Einwand:**
- **Achsen als deklarierte Projektion:** §1 stellt nun explizit klar, dass die Wahl der beiden Achsen (Substrat-Geometrie, Primitiv) selbst eine deklarierte Projektion ist — kein universelles Raster. Andere Achsen (Zugänglichkeit/Constraint, Beobachterabhängigkeit/Rückgewinnbarkeit) sind gleichermaßen zulässig; die Achsen werden als eigens ausgewiesenes Feld geführt, nicht als implizite Universalien. Entsprechender Residuum-Bullet ergänzt.
- **Neue Sektion „Vom Matrix-Eintrag zum A*":** die FFGFT↔HLV-Achse als durchlaufener Governance-Workflow (Vossen/Guevara-Vokabular, attribuiert): deklarierte Projektion → PRC → PRM (= der spektrale Diskriminator) → Residuum (das ehrliche Teilnegativ der unabhängigen HLV-Reproduktion: ⟨r⟩ trennt noch nicht von Zufall) → Operational Accord (Marcel-Protokoll) → Cooperative Admissible Space (A*). Operativ statt bloß deklariert, weil die Messung scheitern kann. Als erklärte Anwendung fremden Vokabulars unter Korrekturvorbehalt der Urheber gekennzeichnet.

**Dok. 086 (DE+EN, je 7 S.):** neue Sektion „Vergleichs- und Einordnungsserie (IPI-Feld)" — listet 245/246/251/260/269/271/272/274 als eigene Reihe (Vergleiche, keine Grundlagen). 086 bleibt sonst die kuratierte 8-Dokumente-Grundlagen-Erzählung.

**Skripte ins Archiv (reproduzierbar mitversioniert):**
- `Dok271_274_Skripte/`: + `hlv_glattice_reproduction.py` (unabhängige HLV-G-Gitter-Reproduktion aus Krügers ℤ⁶-Projektion + k-NN; identische analyze_spectrum-Pipeline; erstes Ergebnis = Teilnegativ auf ⟨r⟩, schwache Signatur in Lücken/Tiefsektor; d_s≈2,7 vs. berichtete 2,49). README erweitert.
- `Dok023_230_Skripte/` (neu): `bell_xi_differential.py` (ξ-Skalen-Bell/CHSH; uniforme (1−ξ)-Dämpfung = entartet mit Visibilität, nicht beobachtbar; beobachtbar ist die Winkelabhängigkeit des Defizits, Differenz an θ≈π vs θ≈0; Signal ξ/D_f…ξ; N≈6×10⁷–6×10⁸ Koinzidenzen).

Alle vier neu/geänderten PDFs kompilieren clean (0 Glyphen/Refs/Overfull). Archiv neu gebaut.

---

## 29. Update (9. Juni 2026) — Dok. 274: O0/O2-Verwendung explizit deklariert

Nach Stefaan Vossens Verfeinerung: in §1 von Dok. 274 (DE+EN) eine deklarierte Zeile ergänzt, die die O0/O2-Verwendung festlegt — \emph{provenienzwahrend} (Marker für Deutungshoheit/Korrekturrecht), \emph{nicht} als vollständiger Import von Guevaras Rendering-Hierarchie (O0/O1/O2 als Repräsentationsebenen). Ob beide zusammenfallen, bleibt offen (vgl. Vossens FAH-Anliegen). Mit dem Orthogonalitäts-Hinweis: Rendering-Ebene und Provenienz koppeln nur im Fremdvergleich, sonst entkoppeln sie. Beide Sprachen kompilieren clean (je 7 S., 0 Glyphen/Refs/Overfull). Archiv neu gebaut.

---

## 30. Update (10. Juni 2026) — Neues Dok. 275 (Von ξ zu φ) + P37 in Dok. 190

**Neues Dok. 275 (Von ξ zu φ — rekursive Skalenhierarchie, DE+EN):** 1/φ als Durchgangspunkt der ξ-Dämpfungsrekursion r(k+1)=r(k)·(1−ξ) bei k* = log(φ)/ξ ≈ 3609 Skalenebenen (q=2/3 intern konvergent, kein RG-Faktor 2; einziger Fixpunkt: 0). Skripte in Dok275_Skripte/.

**P37 in Dok. 190 (φ-Rollen getrennt):** drei φ-Rollen im Korpus klar getrennt — mikroskopisch ξ / makroskopisch 1/φ (Durchgangspunkt) / Teilchenphysik Q_FFGFT ≈ 0,6677 (Koide); abgegrenzt von der ξ^N/φ^N-Trivialität (P35) und vom empirischen Anker in Dok. 009 (P10).

**k*-Fehlerangabe korrigiert:** 4,0×10⁻⁵ absolut (relativ 6,5×10⁻⁵) bei ganzzahligem k=3609; die frühere Angabe <10⁻⁹ war falsch (galt nur für das nach 1/φ aufgelöste reelle k, zirkulär) und ist im Text sichtbar als korrigiert vermerkt.

**Numerische Validierung v3** (N=2000, 3 Seeds, endlicher T⁴-Graph): gap_CV = 1,68 ± 0,09 außerhalb Null-Band [0,31, 1,05] berichtet — **später als Artefakt widerrufen (s. 31. Update, K5/P38).** Tabelleneinträge P35 (ξ^N-Trivialität) und P36 (R_H-Deutung) in Dok. 190 nachgetragen (waren seit Updates 16/17 nur per Changelog deklariert).

---

## 31. Update (11. Juni 2026) — Externes Audit (P. Stoychev): K5 (v3-Skript) + P38

Erster externer Audit-Eintrag des Registers (P. Stoychev, IPI-Liste, 11. Juni 2026).

**Neu K5 (v3-Skript-Audit, Dok. 275)** — drei Implementierungsfehler in `ffgft_hlv_gap_v3.py`: (a) T⁴-Punktgitter nutzte n₃ nur in der Akzeptanznorm, nicht in der Position (729 eindeutige von 2000 Punkten; 1/d²-Clamp erzeugte λ_max = 2,5×10¹²) → das „gap_CV = 1,68 außerhalb des Bandes" aus dem 30. Update war **Artefakt**; (b) `hlv_points(seed)` verwendete den Seed nicht — das „3-Seed-Ensemble" war dreimal dieselbe Rechnung; (c) Schalen-Detektor für Zielverhältnisse < 1 strukturell verzerrt. Alle behoben in v4, betroffene Resultate widerrufen.

**P38 (k*-Resultat zurückgestuft):** k* = log(φ)/ξ ≈ 3609 von „Fixpunkt ohne freien Parameter" auf „Durchgangspunkt, P35 greift" zurückgestuft — 1/φ ist Durchgangspunkt, kein Fixpunkt (einziger Fixpunkt von r↦r(1−ξ) ist 0); k*(c) existiert für jedes Ziel c mit identischem Parameterstatus. P37 Ebene (2) entsprechend revidiert. (Hinweis: Das v3-Audit war in Dok. 190 zunächst als „K4" geführt; siehe 32. Update — Nummernkonflikt mit der älteren Faktor-3-Korrektur bereinigt: jetzt K5.)

---

## 32. Update (14. Juni 2026) — Neues Dok. 277 (Wellenausbreitung und Energie) + Dok. 190 P39 (H₀/R_H-Status präzisiert)

**Neues Dok. 277 (DE+EN, je 8 S.) — „Wellenausbreitung und Energie":** ausgearbeitete, quellenbelegte Fassung der gleichnamigen Kurznotiz. Kernlinie: eine laufende Welle trägt **immer** positive Energie (Poynting-Fluss, E = ℏω, Strahlungsdruck); **lokal** ist Energie stets erhalten (∂ₜu + ∇·S = 0; ∇_μT^μν = 0); Rotverschiebung ist beobachterabhängig (E = p^μu_μ), kein Verlust ins Nichts; „global nicht eindeutig definierbar" (FRW: kein zeitartiges Killing-Feld, Noether) ≠ zerstört. Im **statischen T⁴** ist die Gesamtenergie sogar global erhalten und z eine reine Umbuchung. Formalisiert in Theorem-/Proposition-/Definition-Boxen; externe Quellen (Noether 1918, Poynting 1884, Jackson, MTW, Wald, Breit-Wheeler 1934) und Korpus-Verweise (166, 182, 230, 267, 268, 270, 190, 038, 009).

- **Kosten-Asymmetrie statt neutraler Entartung:** Auf den **Daten** sind ΛCDM und FFGFT entartet (Dok. 267); auf der **Struktur** nicht — Kostentabelle (Beschleunigung/CMB-Peaks/globale Energie/„Energie verschwindet"): ΛCDM trägt dunkle Energie + dunkle Materie und verzichtet auf globale Energieerhaltung, FFGFT keines davon. Sparsamkeits-Argument (Occam), kein empirischer K.o.
- Defensive „nicht-Widerlegung"-Negation entfernt; positiv als Daten-vs-Struktur formuliert. Noether-Ableitung (statischer T⁴ ⇒ globale Energieerhaltung) steht ohne Vorbehalt.
- Build: LuaLaTeX, je 3 Durchläufe (TOC), DE+EN je 8 S., 0 ??, 0 fehlende Glyphen; Schriften (Inter, Libertinus Math) eingebettet.

**Dok. 190 — neuer Eintrag P39 (H₀/R_H-Status präzisiert):** Die Relation Plancklänge↔R_H (Exponent 41/4, R_H/L₀ = 6,49×10⁶⁴) wird von **keinem** Rahmen aus ersten Prinzipien hergeleitet — warum das Universum ~10⁶⁰ Plancklängen misst, sagt keine Theorie. ΛCDM fixiert sie über den **gemessenen** H₀ (im Sinne der Daten-Entartung, Dok. 267, selbst zirkulär); FFGFT übernimmt den etablierten Wert zur Vergleichbarkeit und notiert ihn in ξ-Schreibweise. Damit ist die kosmische Skala ein **gemeinsamer empirischer Bezugspunkt beider Modelle**, kein freier Parameter und **keine FFGFT-spezifische Lücke**. Verstärkend: in FFGFT sind ℏ, c SI-Umrechnung und G abgeleitet (ξ→{m_e,…}→G→ℓ_P) — ein „gemessener" dimensionaler Anker im Standardphysik-Sinn existiert hier gar nicht. P20/P32/P36 bleiben gültig, werden aber **nicht mehr als Schwäche** gelesen. Einziger verbleibender offener Punkt: die Vorwärts-Herleitung von 41/4 aus ξ — **symmetrisch**, da kein Rahmen sie hat; die einzige Modell-Asymmetrie ist der Dunkelsektor (allein ΛCDM). Eingepflegt in Kopf-Statuszeile (P1–P39, Stand 14. Juni), Nachtrag (14. Juni) und Tabellenzeile P39. DE kompiliert clean (32 S.).

**Nummernkonflikt K4 bereinigt (Dok. 190 ↔ Changelog):** Das v3-Skript-Audit (11. Juni) war in Dok. 190 als **K4** geführt, während K4 im Changelog bereits die ältere **Faktor-3-Korrektur** (Dok. 267/268, ~7. Juni) bezeichnet. Auflösung in beiden Dokumenten konsistent: **K4 = Faktor 3** (3D-Beobachter statt fraktale Dispersion), **K5 = v3-Skript-Audit**. In Dok. 190 ist die Faktor-3-Korrektur als K4-Tabellenzeile nachgetragen, das v3-Audit auf K5 umnummeriert (Statuszeile, Nachtrag, Tabelle); im Changelog ist K5 in der Übersichtstabelle ergänzt.

## 33. Update (14. Juni 2026) — Neues Dok. 279 (Casimir–CMB–H₀) + Dok. 190 R35 geschärft + EN-190 neu übersetzt

**Neues Dok. 279 (DE+EN, je 9 S.) — „Casimir, CMB und H₀ — die gemeinsame ξ-Skala":** Schritt-für-Schritt-Herleitung der Verbindungsformel, zusammengeführt aus Dok. 091 (Casimir/Vakuum), 165 (H₀-Verhältnis), 025/061 (T_CMB), 166, 026.

- **Kern:** ρ_CMB = ξℏc/L_ξ⁴ und ρ_Casimir(L_ξ)/ρ_CMB = π²/(240ξ) ≈ 308 ⇒ L_ξ = [15ξ/π²]^¼ · ℏc/(k_B T_CMB) ≈ 100,24 µm (Casimir-Exponent ¼); H₀/c = (π/2)ξ¹⁰/λ̄_e (H₀-Exponent 10). Produkt: **L_ξ·H₀/c = K_geo·(m_e c²/k_B T_CMB)·ξ^(41/4)** mit K_geo = (π/2)(15/π²)^¼ = 1,7441, exakt (7,241×10⁻³¹). Exponent **41/4 = 10 + ¼**, identisch mit Dok. 026 (E_H = E₀ξ^(41/4)).
- **Einleitender Abschnitt „Warum ‚Hubble-Konstante' irreführend ist":** H₀ ist keine Konstante (schon im Standardbild nur der heutige Wert des zeitabhängigen H(t); in FFGFT gar keine Expansionsrate, R14/R15/R18). Robust ist die **Referenzlänge** R_H = c/H₀ (analog ℓ_P, R=ℏ/mc; nicht Universumsgröße/Horizont, R36); H₀ = c/R_H nur deren SI-Umschreibung (R16/R39). Daher arbeitet die Herleitung durchgängig mit Längen.
- **Abschnitt „Wo steckt der SI-Umrechnungsfaktor?":** auf der dekompaktifizierten Stufe muss der SI-Faktor auftauchen — er tut es: (1) ℏc kürzt sich (legitim, Längenverhältnis L_ξ/λ̄_e); (2) bleibt übrig als empirischer Anker m_e c²/(k_B T_CMB) = 2,176×10⁹; (3) im Exponenten als 63/4 = 41/4 + 11/2 (E₀- vs. Planck-Referenz). Korrektur des alten 2,0×10⁹-Labels → 2,176×10⁹ (Identität geht exakt auf). Konsistent mit R34/R16/R35.
- **Ausblick (Vermutung, kein Beweis):** das 11/2 im Split ist nicht beliebig — es fällt mit dem **vorwärts hergeleiteten Feinstruktur-Exponenten** α = ξE₀² = Kξ^(11/2) (Dok. 011/070/202/210, gleiches E₀ = √(m_e m_μ) wie der 41/4-Anker) zusammen, numerisch E₀/E_Planck = ξ^5,48 vs. 5,5 (Treffer ~0,5 %). Verschiedene Bezugsbasen (MeV vs. Planck) — Identität erst durch E₀ = E_Planck·ξ^(11/2) vorwärts bewiesen. Umgekehrte Frage: ΛCDM **wählt** H₀ nicht, es misst/feinabstimmt; (ℓ_P/R_H)² ≈ 10⁻¹²² **ist** das Kosmologische-Konstanten-Problem. FFGFT eliminiert Λ (R17/R39), verlagert das „Warum diese Skala" ins 41/4. Test: vorwärts-41/4 ⇒ Vorhersage von H₀ ⇒ entscheidet die H₀-Spannung (67 vs. 73) — das machte aus der Vermutung einen Beleg.

**Dok. 190 — R35 geschärft (DE+EN):** Nachtrag, dass das 11/2 in 63/4 = 41/4 + 11/2 **nicht beliebig** ist, sondern mit dem vorwärts hergeleiteten α-Exponenten zusammenfällt — ausdrücklich als **Vermutung, kein Beleg** (verschiedene Bezugsbasen; Identität erst durch E₀ = E_Planck·ξ^(11/2) vorwärts). Offen bleibt das kosmische 41/4. Querverweis auf Dok. 279.

**EN-190 vollständig neu übersetzt:** altes EN (R-Stand 34, 8. Juni, divergente R-Nummerierung) gelöscht und von Grund auf aus dem aktuellen DE neu übersetzt — **C1–C5** (= K1–K5), **R1–R39** (= P1–P39) deckungsgleich; einfacher Header (statt grüner Box), alle Addenda (2./6./8./10./11./14. Juni), C/R-Begrifflichkeit durchgängig. EN 28 S., DE 32 S., gleicher Inhaltsstand.

- Build: LuaLaTeX je 3 Durchläufe; Dok. 279 DE/EN je 9 S., Dok. 190 DE 32 / EN 28 S.; 0 unaufgelöste Referenzen, 0 Fehler, Schriften eingebettet.

## 34. Update (15. Juni 2026) — Neues Dok. 280 (Rotverschiebung achromatisch, z→Zeit, Entartung) + Dok. 190 K6 (chromatisch→achromatisch)

**Neues Dok. 280 (DE+EN, je 6 S.) — „Rotverschiebung in FFGFT: statisch, achromatisch, und die z→Zeit-Übertragung":** fasst die FFGFT-Rotverschiebung zusammen und korrigiert die chromatische Altlast.

- **Statisch:** dE/dx = −ξE ⇒ E(x)=E₀e^(−ξx) ⇒ **1+z = e^(ξx)**, z≈ξx; H₀^T0 = E_H/ℏ, E_H = E₀ξ^(41/4) ≈ 1,41×10⁻³³ eV ⇒ **H₀^T0 ≈ 66,2 km/s/Mpc**; Lichtlaufzeit τ = ln(1+z)/H₀^T0 (Dok. 064/026). Kein endliches Alter, kein Urknall.
- **Achromatisch (Korrektur):** die fraktale Wegverlängerung ist rein geometrisch und streckt alle Wellenlängen mit demselben Faktor — **keine** Wellenlängenabhängigkeit. **Finite-Elemente-Simulation** bestätigt das; der führende Term z=ξx ist frequenzunabhängig. Die beobachtete kosmologische Rotverschiebung ist achromatisch — FFGFT trifft das korrekt; der frühere „wellenlängenabhängige Diskriminator" entfällt (wandert in die Spalte „passt").
- **z→Zeit ist ein ΛCDM-Konstrukt:** modellunabhängig ist nur z; die Umrechnung z→Zeit setzt a(t) voraus. ΛCDM-Lookback saturiert bei der Urknall-Decke 13,8 Gyr, FFGFT τ=ln(1+z)/H₀ ist unbeschränkt. Bei cosmic noon (z≈1,9): ΛCDM 10,3 vs. FFGFT 15,5 Gyr. Mit Grafik (Sources/fig/280_z_time_ffgft.png).
- **Kosmologische Entartung (Dok. 267):** SN-Zeitdilatation b=1 (Wegverlängerung dehnt λ und Pulsdauer gleich), BAO (P20-Vorbehalt), CMB-Peaks — alle entartet. SFRD-Werte sind doppelt ΛCDM-abgeleitet (d_L + mitbewegtes Volumen). Daten **passen**, **beweisen** nicht; der Fall ruht auf Sparsamkeit (kein Λ/dunkle Energie/H₀-Spannung, Dok. 064) + ξ-Ableitung.
- **Kein Urknall — Entwicklungsrichtung kehrt um (Dok. 263):** z = (L_eff−d)/d; nahe der Maximalskala R_H hat die z(d)-Kurve einen **Extremwert**, jenseits z→∞ (kein Teilchenhorizont). Der scheinbare Hoch-z-„Anfang" der ersten Galaxien ist dieser geometrische **Umkehrpunkt**, kein Beginn; H₀ emergent (in kompakter T⁴-Form gar nicht vorhanden).
- **Was z\* physikalisch ist:** in FFGFT **keine** Rekombinationszeit. CMB = stationärer Quanten-Grundzustand des Φ-Felds (Dok. 025), Peaks = diskrete **T⁴-Gitterresonanzen** (wie Atom-Emissionslinien/Phonon-Dispersionen). Der Wert ist ein **geometrisches Verhältnis** z\* ≈ (λ_e/L₀)^(1/ln(1/ξ)) ≈ **875** (Dok. 267) — eine Resonanz-/Strukturskala des T⁴-Gitters, kein thermisches Ereignis; ΛCDM liest dieselbe Fläche als z≈1089. Der FFGFT-Wert ist **875, nicht 1100** (P20: Exponent 1/ln(1/ξ) noch nicht hergeleitet ⇒ Referenzwert).

**Dok. 190 — neuer Eintrag K6/C6 (Rotverschiebung achromatisch, nicht wellenlängenabhängig):** korrigiert die frühere chromatische Darstellung (z(λ)∝λ, „UV stärker als Radio") in **Dok. 004, 025, 030, 039, 041, 053, 061, 063, 068, 081**. Beleg: Finite-Elemente-Simulation der fraktalen Wegverlängerung; führender Term z=ξx frequenzunabhängig (Dok. 064). Eingepflegt als Nachtrag (15. Juni), Tabellenzeile K6/C6 und Kopf-Statuszeile (K1–K6). Die Quell-Dokumente selbst bleiben (Arbeitsmethode) **unverändert** — die Korrektur ist nur in Dok. 190 verbindlich. Ausführung in Dok. 280.

- Build: LuaLaTeX je 3 Durchläufe (TOC); Dok. 280 DE/EN je 6 S. (Grafik eingebettet); Dok. 190 DE 32 / EN 28 S.; 0 unaufgelöste Referenzen, 0 Fehler, Schriften (Inter, JetBrains Mono, Libertinus Math) eingebettet.

- **Folgepflege (15. Juni):** Dok. 263 nennt jetzt den FFGFT-Wert z\*≈875 (Dok. 267) neben seiner ΛCDM-Lesart 1089/1100 — der Extremwert nahe R_H ist keine Rekombination. Dok. 086 (Dokumentenübersicht) um Dok. 279 (Casimir-CMB-H₀-Verbindungsformel) und Dok. 280 ergänzt; die in 086 noch chromatische Rotverschiebungsformel z=ξdλ₀/E_ξ wurde inline auf die achromatische Form 1+z=e^(ξx) korrigiert (Verweis K6). 263 DE/EN je 13 S., 086 DE/EN je 7 S. neu gebaut.

- **Dok. 190 — Eintrag P40/R40 korrigiert (Absolutwerte tragen die Korrektur via Brückenkonstanten; Verhältnisse exakt):** festgeschrieben, dass in FFGFT nur die dimensionslosen Verhältnisse exakt sind. Absolutwerte tragen die fraktale/SI-Korrektur, weil sie in die dimensionsbehafteten Brückenkonstanten **absorbiert** ist: v (Massen m=r·ξ^p·v), E₀=7,398 MeV (α=ξE₀²) und die Faktoren 3,521×10⁻²/2,843×10⁻⁵ (G); im Kanon-Skript calc\_De.py steht **kein** explizites K. In Verhältnissen kürzen sich v/E₀/Faktoren weg (m\_μ/m\_e=206,768, korrekturfrei). Herausgezogen ist die Korrektur K\_frak=1−100ξ (Dok. 011/012; in Dok. 133 aus D\_f-Konsistenz + RG-Lauf über 17 Größenordnungen hergeleitet, „keine angepasste Korrektur"). **Zwei Zahlen klar getrennt:** das „100" in K\_frak ist die RG-Verstärkung der ~1,3 %-Korrektur (Dok. 133); die „3609" (Dok. 275) ist die Tiefe der ξ-Skalenrekursion r(k)=(D\_f/3)(1−ξ)^k, bei der die Folge 1/φ **passiert** — dort ist 1/φ Durchgangspunkt, **kein** Fixpunkt, und da die Folge jeden Wert passiert, ist 3609 unverankert, solange 1/φ nicht unabhängig motiviert ist (offen, P37). Weitere Kopplungen (Hintertür) offen; saubere Falsifikation nur über eine vorwärts festgelegte Vorhersage (41/4 → H₀). (Korrigiert die frühere, irrtümliche „K pragmatisch bei 100 Rekursionen abgeschnitten"-Formulierung — Anlass: Hauptskript calc\_De.py.) Nachtrag (15. Juni), Tabellenzeile P40/R40, Kopf-Statuszeile (P1–P40). 190 DE 33 / EN 29 S.

## 35. Update (15. Juni 2026) — Krügers PHI5 bestätigt φ-Nicht-Spezifität; Dok. 275 settled-Note + unabhängige HICE-Pilot-Implementierung

**Anlass:** Marcel Krügers neues Konzeptmanuskript „Hybrid HLV Cell Architecture" (Juni 2026) — ein konservativer Reset. Seine Tabelle 1 führt PHI3/PHI4 als „not established as final" und den korrigierten **PHI5-Pairwise-Audit als „negative for phi uniqueness"** (andere Irrationale erreichen gleiche/stärkere Trennbarkeit). Das deckt sich mit unserem unabhängigen PHI3-Pairwise-Audit.

- **Dok. 275 (DE+EN, je 10 S.) — settled-Note ergänzt:** Krügers PHI5 bestätigt aus seiner eigenen Pipeline die hier vertretene Lesart — φ ist eine **generische Ordnungs-Signatur, kein T⁴-/HLV-Spezifikum** (konsistent mit Run E). Krüger hat HLV auf eine konservative Hybrid-Träger-Geometrie (nativer 6D-Backbone, duale Randschleifen, ICE-Faser, nicht-exakte Holonomie; Vorab-Kill-Tests HICE0–HICE7) zurückgesetzt und erhebt keine φ-Spezifitäts-Behauptung mehr. **Für FFGFT ändert das nichts** (Euler-Tonnetz, nicht Goldener Schnitt); der Befund stützt nur 275. Damit ist der zuvor geparkte PHI-Audit-Punkt erledigt.
- **Unabhängige HICE-Pilot-Implementierung (hice_pilot.py, in den Lieferdateien; entspricht Krügers HICE7):** nativer Z⁶-Cut-and-Project-Backbone mit Schalenmenge S₆ (Norm² ∈ {1,2}, kein projiziertes kNN), U(1)-Faser-Verbindung, Verbindungs-Laplacian, Gates HICE1–HICE4 mit λ₂ (Spektrallücke) als ungefittetem Zeugen. Ergebnis (~230 Knoten): Gauge-Null PASS (p95 ~3e-14), Null-Modell-Trennung PASS (AUC 1,00), destruktiv PASS, **Benign-Stabilität FAIL (AUC 0,85)** → reproduziert unabhängig Krügers DICE0-Status „precondition not satisfied"; Ursache = Phason-/Fenster-Sensitivität des Cut-and-Project.
- **IPI-Korrespondenz:** Reply-All-Entwurf an die Liste erstellt (anerkennend; PHI5-Bestätigung; HICE2∧HICE4-Doppelbedingung als eigentlicher Fingerabdruck-Test; HICE6 als Pflicht; symmetrischer all-vs-all-Ausreißertest als Standard; mit dem unabhängigen HICE-Pilot-Ergebnis). Skript + Plot als Anhang.

## 36. Update (15./16. Juni 2026, gebaut 17. Juni) — Neue Dok. 281 (Goldener Schnitt) und Dok. 282 (Hilbertraum-Massenoperator)

**Neues Dok. 281 (DE+EN, je 7 S.) — „Der Goldene Schnitt in FFGFT: Notation, Rollen und Status — eine konsolidierende Klärung":** legt die kanonische Lesart fest, ohne die Altdokumente zu ändern. Kernaussagen: (i) φ ist nirgends Fundament — das ist ξ=4/30000; (ii) die einzige φ-Verwendung mit echtem geometrischem Gehalt ist arctan(φ⁻³) in der CP-Phase (Dok. 172), weil φ⁻³=√5−2 die natürliche Zwischenskala der Fibonacci-Konvergenz ist; (iii) φ-Massenleitern (Dok. 172/188) sind heuristisch, numerisch fehlerhaft (Dok. 188: φ⁵π²=109,46 statt behaupteter 206,7; Dok. 172: φ¹⁰=122,99, 40 % daneben) und fallen unter die φ^N-Trivialität P35; (iv) 1/φ ist Durchgangspunkt, kein Fixpunkt (Dok. 275, vgl. P40); (v) π und e werden nirgends hergeleitet. Enthält kanonische Notationstabelle (φ = Goldener Schnitt via \varphi; φ = Skalarfeld/Winkel/Index via \phi — NICHT ersetzen), neun Rollen A–I, ehrliches Register korrekt/offen/falsch und eine Vorkommens-Tabelle über den Korpus. Normativ für die Lesart, nicht den Wortlaut. Quelle ursprünglich nur DE; **EN am 17. Juni vollständig aus dem DE übersetzt** (Dezimalpunkt, ``…''-Zitate, Math/\verb/\ref 1:1; Terminologie: transit point, self-similarity attractor, pentagonal symmetry breaking, fractal scaling factor).

**Neues Dok. 282 (DE+EN, je 9 S.) — „FFGFT im Hilbertraum — vom gemeinsamen Loop-Objekt zum Massenoperator":** macht die Hilbertraum-Brücke (Dok. 230/231/232) vollständiger und zeigt, dass sie bis zu den Massen reicht. Drei Ebenen: (0) QM-äquivalent — FFGFT und HLV sind ein Connection-Laplace auf einem faserwertigen Hilbertraum (Eichfreiheit = unitäre Äquivalenz, Verschränkung = Holonomie um Zyklen); (1) Prozess — ein CP-Teilbarkeits-Test trennt QM-intern (Markovsch) von historien-gekoppelt (nicht-Markovsch), die Zeit als Prozessstruktur; (2) Masse — der Massenoperator ist ein **hermitescher Z₃-Zirkulant** auf der C³-Faser, seine Eigenvektoren sind die drei Z₃-Charaktere (die Generationen), sein Spektrum S² die Massen. Mit r=√2 (Koide Q=2/3) und θ=2/9 (=2/3²) reproduziert er m_μ/m_e und m_τ/m_μ auf vier bis fünf Stellen, ohne den früher gefitteten Leiter-Koeffizienten. Der FFGFT↔HLV-Vergleich ist nur die Eingangstür, nicht das Thema. Begleitskripte: ffgft_t4_cp_divisibility.py, ffgft_t4_mass_operator.py, ffgft_mass_operator_C3.py (in Dok282_Skripte/). Wrapper am 17. Juni nach 281-Muster erzeugt (DE+EN). **Nachtrag 17. Juni:** Numerik-Warnbox in 282 (DE+EN) ergänzt — der leichteste Eigenwert μ_e=M(1+r·cos(θ+2π/3))=0,04035·M ist eine Fast-Total-Auslöschung; ein 3 %-Fehler in cos (−0,658 statt −0,6786, z. B. per Hand gerundet) macht daraus 72 % Fehler in μ_e und kippt m_μ/m_e von 207 auf 63. Verhältnisse nur in voller Maschinenpräzision prüfbar. Anlass: externer Nachprüfer (DeepSeek) lief genau in diese Auslöschungsfalle; Skript-Kommentar in ffgft_mass_operator_C3.py entsprechend ergänzt. 282 DE/EN je 9 S. neu gebaut.

- Build: LuaLaTeX je 3 Durchläufe (TOC); 281 DE/EN je 7 S., 282 DE/EN je 9 S.; 0 unaufgelöste Referenzen, 0 fehlende Glyphen, 0 Fehler; Schriften (Inter, JetBrains Mono, Libertinus Math) eingebettet. PDFs in PDFs/, Quellen in Sources/ch/ und Sources/wr_standalone_A4/.

## 37. Update (17. Juni 2026) — Begleitskripte einsortiert (14 Skripte, 4 Ordner)

Die mit Dok. 280/282 und dem FFGFT↔HLV-Holonomie-Audit gelieferten Python-Skripte wurden in vier Ordner einsortiert, jeder mit README. Alle laufen sauber (Smoke-Test 17. Juni; Ausnahmen erwartet: ffgft_phi3_pairwise_audit braucht Krügers feature_table.csv, ffgft_tts braucht FFGFT_Chatterbox_Chunks.txt + Chatterbox-Modell).

- **Dok280_Skripte/** (Rotverschiebung, z→Zeit, SFRD): `z_time_ffgft.py` (erzeugt die in Dok. 280 eingebettete Grafik Sources/fig/280_z_time_ffgft.png), `z_time_mapping.py` (ΛCDM vs. generischer statischer Benchmark), `lilly_madau_v4.py` (Lilly–Madau-SFRD auf der ΛCDM-Zeitachse, für J. Nicholson/IPI).
- **Dok282_Skripte/** (im 282-Text namentlich genannt): `ffgft_mass_operator_C3.py` (Z₃-Zirkulant-Massenoperator auf C³), `ffgft_t4_mass_operator.py` (Vorwärts-Test KK vs. Z₃-Kreis, Koide forward), `ffgft_t4_cp_divisibility.py` (CP-Teilbarkeit/Nicht-Markovianität, Zeit als Prozess).
- **Dok271_HICE_Holonomie_Skripte/** (Holonomie-Zweig des FFGFT↔HLV-Vergleichs Dok. 271, ergänzend zum Spektral-Diskriminator in Dok271_274_Skripte/): `ffgft_t4_holonomy_witness.py`, `ffgft_t4_context_content_witness.py` (De Jesus W_psi), `ffgft_t4_dynamical_u3.py` (Krüger Sec. 13.5), `ffgft_t4_coherence_observables.py` (HICE-MEM0), `ffgft_hlv_homology_check_v3.py` (HLV-Homologie-Falsifikation, vgl. Dok. 276), `hice_pilot.py` (HICE7-Pilot, vgl. 35. Update), `ffgft_phi3_pairwise_audit.py` (symmetrischer PHI3-Audit, stützt Dok. 281/275; **Eingabe `feature_table.csv` jetzt beigelegt** — Krügers Run-PHI3-NATIVE6D-Output aus der IPI-Korrespondenz/Zenodo 20692350, 320 Zeilen × 8 Ensembles; Audit läuft damit out-of-the-box: AUC-Matrix durchweg 1,0, φ kein Ausreißer). Konservativer Maximal-Status durchweg „candidate carrier", keine HLV-Verbindung behauptet.
- **Werkzeuge_Skripte/** (kein Physik-Dokument): `ffgft_tts.py` (Batch-Vertonung der Slide-Chunks mit Chatterbox).

**NACHTRAG (5. Juli, 295 Open-System-Erdung):** in "Das Verhältnis e trägt das temporal-dynamische Objekt nicht" ein Satz ergänzt (DE+EN): Marcels temporal-dynamisches Objekt ist -- nach seinem Spiral-Time-Papier -- ein Objekt offener Quantendynamik (unitäre Dilatation auf H_S⊗H_M, geprüft über Prozesstensor/CP-Divisibilität/Hard-Reset/Finite-Bath), gehört damit der dynamischen, nicht der geometrischen Kategorie an. Der Quelle zugeschrieben, kein eigenes Verdikt (P35). 295 DE+EN 8/8 S., 0 Glyphen.

## 38. Update (11. Juli 2026) — Dok. 303 (revidiert), 304 (revidiert + Provenance-Grenze), 305 (neu), Dok. 190 R48

Nachtrag zur v1.2.3-Reihe (die Juli-Dokumente 298–302 sind in der README-Versionstabelle geführt). Dieses Update zieht die jüngsten Dokumente und den zugehörigen Registervermerk nach.

- **Dok. 303 — Repräsentationale Identität über Rollenwechsel (revidiert):** eine Definition identifiziert ein Objekt, Governance bewahrt seine Identität über spätere Übergänge; der Fünfer-Erhaltungs-Nachweis (bewahren / projizieren / transformieren / substituieren / überbrücken) verhindert stille Rollendrift zwischen unabhängig entwickelten Rahmen.

- **Dok. 304 — Der Gedächtnis-Reflex (revidiert, DE 12 S. / EN 11 S.):** erlebte Zeit setzt Zeit voraus, statt sie zu erzeugen (Gegenstück des Wort-Reflexes, Dok. 301). Zeit ist D(k)=Σ100ξ_n→ln(1+k/75), fundamental; die Akkumulations-gegen-Kern-Grenze sitzt in der Zeit, nicht im Gedächtnis; ein Messausschnitt ist bezuglos, die scheinbare Gleichförmigkeit ein Linearisierungs-Artefakt (verifizierte Fehlergröße e=x−ln(1+x), skaleninvariant 1−ln2, Linearisierung in der Projektion); Rückschluss Messung→Ursache durch holografische Verwaschung begrenzt. **Neuer Abschnitt „Provenance und die Grenze der Brücke":** die Korrespondenz zu einem externen operationalen Mτ/MB als eingeschränkter, optionaler Kandidat (Kategorie B) gebucht — zwei Achsen (das e-Kriterium selbst proven/skript-verifiziert, Dok. 295; nur die Korrespondenz restricted, empirisch „kein Benchmark durchgeführt", d. h. unabhängiger, gemeinsam versiegelter Vergleich), operationale Definition unberührt (beide Richtungen), Symmetrie, namentliche Provenance. Ledger-fremde Vokabel „ungetestet" vermieden; claim-state restricted (Kategorie B). Kein FFGFT-Befund geändert, nur die Rahmung. Begleitskript `Dok304_Skripte/ffgft_304_linearisierungsfehler_probe.py` (Linearisierungsfehler, deterministisch).

- **Dok. 305 — Der Krümmungstreue-Diskriminator (neu, DE 4 S. / EN 4 S.):** bei gleicher Reichweite trennt eine Reichweiten-Metrik einen krümmungstreuen (log-Spiral-) nicht von einem gleichförmigen Akkumulator; das e-Kriterium schon — Selbstähnlichkeit D(2k)−D(k)→ln2 (Abw. 4·10⁻⁴ bei k=10⁵), Ganghöhen-Zerfall 1/n (p≈−0,984), Skalen-Ratio→e (Abw. 4·10⁻³ bei D=6). Aus ξ/der Rekursion ableitbar (proven, Dok. 295); keine kognitive-MB-Spezifität (restricted, Kategorie B; unabhängiger, gemeinsam versiegelter Benchmark ausstehend). Begleitskript `Dok305_Skripte/ffgft_kruemmungstreue_probe.py` (deterministisch, nur Standardbibliothek).

- **Dok. 190 R48 (neuer Registereintrag):** dokumentiert die 304-Revision — Begleit-Notiz-Überzeichnung (nur in der Mail) zurückgenommen, Dokument präzisiert (nicht repariert); die vier Provenance-Punkte, die vermiedene Ledger-fremde Vokabel und der bewahrte claim-state festgehalten. „Kein FFGFT-Befund geändert — nur die Rahmung."

- Build: LuaLaTeX je 3 Durchläufe (TOC); 303 De/En, 304 De 12 / En 11 S., 305 De/En je 4 S., 190 De 39 / En 34 S.; 0 fehlende Glyphen. PDFs in PDFs/ und Sources/wr_standalone_A4/, Quellen in Sources/ch/, Skripte in Dok304_Skripte/ und Dok305_Skripte/.

## 39. Update (12. Juli 2026) — Dok. 306 (neu), Dok. 190 R49/R50, Dok. 304 (Provenance), Dok. 025/063 (Vermerk)

- **Dok. 306 — Die native Zeit-Energie-Reziprozität (neu, DE 5 S. / EN 4 S.):** Ersetzung einer geliehenen Begründung. Dok. 025 und 063 begründeten die Abwesenheit einer kosmischen Anfangssingularität mit Heisenbergs Energie-Zeit-Unschärferelation. Drei Mängel: **(M1) invertierte Implikation** — aus endlichem Δt folgt ΔE ≥ 1/(2Δt), also eine *endliche* Schranke, nicht ΔE→∞ (Letzteres nur für Δt→0); **(M2) Anwendungsfehler** — die Energie-Zeit-Unschärfe ist nicht kanonisch (Pauli: kein selbstadjungierter Zeitoperator), ihr Δt ist nach Mandelstam–Tamm die Änderungszeit einer Observablen, kein kosmisches Alter; **(M3) Stilbruch** — „unwiderlegbar" ist keine Ledger-Vokabel. Übergreifend: Heisenberg gehört zur *projizierten* QM-Ebene; ein darauf gestütztes Argument verlässt die Projektion nicht, sondern zirkuliert in ihr (Dok. 298).

  **Die ersetzende native Kette:** T·m = 1, mit E = m also **T·E = 1** (Dok. 003/010) — eine *Gleichung*, keine Ungleichung; daraus E→∞ ⟺ T→0. FFGFTs Zeit besitzt jedoch ein minimales, nicht verschwindendes Inkrement d₁ = 100·ξ₁ = 1/75 (aus ξ = 4/30000): T ist nach unten, E nach oben beschränkt — eine unendliche Dichte ist **strukturell** ausgeschlossen. Ergänzend die **Randfrage**: ∂T⁴ = ∅ (Dok. 302) — die Frage „was war bei t=0?" setzt einen Rand voraus, den ein kompakter Torus nicht hat; sie ist nicht falsch beantwortet, sondern falsch gestellt. Präzisiert: D(k) *wächst* unbeschränkt (logarithmisch); die singularitätsfreie Aussage lautet, dass D(k) an jeder *endlichen* Stelle endlich ist und nirgends divergiert. Die exakte numerische Obergrenze für E hängt von der Normierung ab und wird nicht behauptet (offen). Die **Konklusion** (kein singulärer Anfang; endlicher Kern mit minimaler, von ξ gesetzter Skala L₀) bleibt unverändert.

- **Dok. 025 und 063:** an der betreffenden Stelle mit einem sichtbaren Vermerk versehen — die Heisenberg-Begründung ist für diesen Punkt *nicht mehr maßgeblich*; die Konklusion bleibt und wird in Dok. 306 nativ begründet.

- **Dok. 190 R49 (neuer Registereintrag):** Provenance-Vertiefung von Dok. 304 — das aus Marcel Krügers Spiral-Zeit-Arbeit übernommene Vokabular (U1/U2/U3 *und* M_τ/M_B) wird bei der Erstnennung zitiert (Primärquelle doi:10.5281/zenodo.21302278; dokumentierte Lineage Medinformatics, Smart Wearable Technology), mit der ausdrücklichen Feststellung, dass **FFGFT diese Unterscheidung nicht benötigt** — eine einzige, krümmungstreue Windung; die Sektoren und die M_τ/M_B-Teilung dienen allein der *Analyse* jenes Rahmens. Der Abstract wurde narrativ ohne die fremden Kürzel neu gefasst. Ein Satz würdigt die Governance-Lineage (claim-state-Ledger / Identitätsprüfung aus Stefaan Vossens *Dot Theory*, im IPI ko-entwickelt, vgl. Dok. 272). Die distinkte Umbenennung der FFGFT-Objekte blieb offene authoriale Entscheidung.

- **Dok. 190 R50 (neuer Registereintrag):** die Ersetzung des Heisenberg-Imports (siehe Dok. 306) registriert, mit den drei Mängeln, der nativen Kette, der Präzisierung zu D(k) und der offen gelassenen historischen Frage, warum der Import erfolgte, obwohl Dok. 003/010 vorlag.

- Build: LuaLaTeX je 3 Durchläufe; 306 De 5 / En 4 S., 190 De 40 / En 35 S., 304 De 13 / En 12 S.; 0 fehlende Glyphen.

## 40. Update (12. Juli 2026) — Dok. 190 R51 (Notations-Altlast T₀ in Dok. 049)

- **Dok. 190 R51 (neuer Registereintrag):** Dok. 049 („Lagrangian-Vergleich") enthält zwei Passagen, die der heutigen Position zu widersprechen *scheinen* — „Urknall als Feldanregungsereignis" (δm(x,t=0) = δm₀·δ³(x)·e^{−H₀t}) und „Schwarze Löcher als Feldsingularitäten" (T(r) → 0). **Auflösung:** In der ursprünglichen T0-Sicht bezeichnete T₀ *nie* den Zeitpunkt null, sondern den **kleinsten möglichen Zeitraum**; Dok. 095 verwendet ihn korrekt als Bezugsmaßstab (Ω(T) = T₀/T). Im ursprünglichen Sinn gelesen meint 049 **T(r) → T₀**, nicht T → 0 — womit E = 1/T durch 1/T₀ beschränkt ist: der *endliche Kern mit minimaler Skala L₀ (aus ξ)*, exakt wie in Dok. 306 nativ etabliert. Es ist eine **Notations-Altlast, kein Substanzwiderspruch**. Die wörtliche Lesart (T → 0) ist gleichwohl nicht mehr maßgeblich. Auch bei wohlwollender Lesart überholt bleiben: der „Urknall" als Anregungsereignis, die Punktquelle δ³(x) und das explizite H₀. Maßgeblich sind Dok. 306 (keine Singularität; ∂T⁴ = ∅) und Dok. 267 (keine metrische Expansion, b = 1; H₀ nur effektiv). Betroffen ist allein der kosmologisch-astrophysikalische Abschnitt von 049; der Lagrange-/Teilchensektor (u. a. a_μ) ist unberührt. Die Quelldokumente werden **nicht revidiert** (append-only, vgl. R50).

- **Dok. 306 erweitert:** neuer Abschnitt „Das Schwarze Loch: Extremum, nicht Singularität". Aus T·E = 1 mit T ≥ T₀ folgt E ≤ 1/T₀. Der Horizont ist der Ort, an dem die Extrema *erreicht* werden — langsamste Zeit (T = T₀, nicht T → 0), maximale Energie-/Massenkonzentration (E = 1/T₀), maximale Krümmung; alles endlich und wohldefiniert. Der Horizont ist kein Rand zu etwas anderem und kein Vorhang vor einer Singularität. Konsequenz: In FFGFT gibt es **nichts zu reparieren** — Bounce-, Schalen- und Tochterzweig-Modelle beheben einen Defekt, den FFGFT nicht erzeugt (keine Widerlegung jener Modelle, sondern die Feststellung, dass die Frage hier nicht entsteht).

- **Dok. 306 erweitert (2):** neuer Abschnitt „Das andere Extrem: der dünnste Zustand". Der scheinbare Zirkel („Vakuum leer → wirkt nur durch Krümmung → Krümmung setzt Masse voraus") ist ein **GR-Import**: er lebt vom kausalen Pfeil T_μν *erzeugt* Krümmung. FFGFT hat diesen Pfeil nicht — T·m = 1 ist eine **Reziprozität**, Masse und zeitliche Krümmung sind zwei Lesarten derselben Struktur; die Frage „was zuerst?" ist so falsch gestellt wie die nach t=0. Beide Ränder sind ausgeschlossen: m→∞ ⇒ T→0 (durch T ≥ T₀, L₀ = ξ·l_P) und **m→0 ⇒ T→∞ (T·m = 1 hat bei m=0 keine Lösung)**. FFGFT kennt daher **keinen leeren Zustand** — nicht weil etwas ihn füllt, sondern weil die Theorie keine Beschreibung von „nichts" enthält. „Vakuum" ist die irreführende Bezeichnung; treffender: *der dünnste Zustand* / *die flachste Windung*. **Asymmetrie ehrlich gebucht:** der dichte Pol ist hart und aus ξ abgeleitet; der dünne ist strukturell ausgeschlossen, aber **nicht beziffert** — es gibt „keine einzige kosmische Obergrenze für alle Systeme", jedes System trägt sein eigenes R_Torus(m) = ħ/mc (Dok. 182 = T·m=1 geometrisch), und E_H = E₀·ξ^{41/4} ist an H₀ *kalibriert*, nicht hergeleitet (P35/P36).

- **Dok. 306 erweitert (3) — die Extrema sind beziffert:** L₀ = ξ·l_P (Dok. 182) liefert über die Energie-Längen-Reziprozität **E_max = ħc/L₀ = E_P/ξ ≈ 7500·E_P ≈ 9,16 × 10²² GeV** und **T₀ = ξ·t_P ≈ 7,19 × 10⁻⁴⁸ s** (Dok. 250, 290). Die Reziprozität schließt **exakt** — ξ kürzt sich heraus: T₀·E_max = (ξ t_P)(E_P/ξ) = t_P·E_P = 1 (natürliche Einheiten). T·E = 1 gilt also an den Extrema, nicht nur im Mittelbereich. Derselbe Wert ist der **natürliche UV-Cutoff** der Feldtheorie: der fraktale Torus stellt ihn, weshalb traditionelle Renormierung nicht erforderlich ist (Dok. 019/202); dieselbe Schwelle erklärt die Seltenheit magnetischer Monopole (Dok. 143). Die minimale Zeit ist damit **kein nachträglicher Regulator, sondern folgt aus der Geometrie**. Die frühere Vorsichtsklausel („numerische Obergrenze nicht behauptet") entfällt; der dichte Pol ist *proven* und beziffert. Der **dünne Pol** bleibt strukturell ausgeschlossen, aber **unbeziffert** (keine minimale Energie aus ξ; E_H = E₀·ξ^{41/4} an H₀ kalibriert, P35/P36).

- **Dok. 306 — Buchung des dünnen Pols korrigiert:** Die fehlende Bezifferung des dünnen Pols ist **kein Defizit, sondern strukturell**. Aus T·m = 1 folgt, dass jedes System seine eigene Obergrenze R_Torus(m) = ħ/mc trägt; Dok. 182 sagt es selbst: „Die Frage nach einer universellen Maximalgröße des Universums ist nicht sinnvoll gestellt." Der kosmologische Sektor **benötigt daher eine eigene, unabhängig gesetzte Skala** — sie kann gar nicht aus ξ allein folgen. **Was P35 betrifft und was nicht:** Die Notwendigkeit der eigenen Skala ist in Ordnung; die *Schreibweise* E_H = E₀·ξ^{41/4} ist es nicht — der Exponent ist an H₀ kalibriert, nicht vorwärts abgeleitet, und die ξ-Form suggeriert eine Ableitung, die es nicht gibt. Der Einwand trifft die **Notation**, nicht die Sache.

## 41. Update (12. Juli 2026) — Dok. 190 R52 (Zahlwerte im H₀-Umfeld)

- **R52:** Zwei nachrechenbare Fehler. **(i) Falscher L₀-Wert:** Dok. 101 (Abstract + Text) und Dok. 165 geben L₀ = ξ·ℓ_P ≈ 5,39 × 10⁻³⁹ m an; **korrekt ist 2,155 × 10⁻³⁹ m** (Dok. 180 — die eigens dafür bestimmte Herleitung — sowie 013, 181, 182, 187, 189, 268). Der falsche Wert impliziert ξ = 3,34 × 10⁻⁴ statt 4/30000 = 1,333 × 10⁻⁴ (Faktor 2,50); die Mantisse 5,391 ist die der Planck-*Zeit* → Übertragungsfehler. **(ii) Falsches Skalenpaar:** 165s Stützargument vergleicht L_H mit der Granulationsskala L₀ (L_H/L₀ = 6,37 × 10⁶⁴ vs. ξ⁻¹⁰ = 5,63 × 10³⁸ — der nötige „geometrische Faktor" wäre 1,13 × 10²⁶). Die Hauptrelation vergleicht in Wahrheit mit der **Compton-Länge** des Elektrons, und dort trägt sie: L_H/λ_C(e) = 3,55 × 10³⁸ ≈ [(π/2)ξ¹⁰]⁻¹ = 3,59 × 10³⁸. **(iii) Die Hauptrelation ħH₀/(m_e c²) = (π/2)·ξ¹⁰ ist nachgerechnet korrekt** → H₀ = 66,82 km/s/Mpc (−0,9 % ggü. Planck 67,4). **(iv) P35 unverändert:** der Exponent 10 bleibt nicht vorwärts abgeleitet; die *Notwendigkeit* einer eigenen kosmologischen Skala bleibt strukturell unberührt (Dok. 182). **(v) Dok. 306 unberührt** — sein dichter Pol ruht auf dem korrekten L₀ (E_max = 9,16 × 10²² GeV bestätigt).

## 42. Update (12. Juli 2026) — Dok. 190 R53 (Wo man in den Kreis eintritt)

- **R53:** Dok. 267 §518 schreibt, FFGFT leite E_H/ħ „intern aus ξ^{41/4} **ab** — und damit R_H **vollständig aus ξ** (Dok. 182)". **Dok. 182 sagt jedoch das Gegenteil und wird gegen die eigene Buchung zitiert:** „Der Exponent 41/4 ist *nicht* aus ξ hergeleitet, sondern an den gemessenen H₀ kalibriert (P35/P36) … kein eigenständiges ξ-Resultat." Dasselbe gilt für ħH₀/(m_e c²) = (π/2)ξ¹⁰ (Dok. 165, vgl. R52). **Korrigierte Lesart:** Die Tabellenzeile *Quelle der Skala* lautet auf FFGFT-Seite **„gesetzt / an H₀ kalibriert"**, nicht „aus ξ". — **Zirkularität ist kein Defekt:** ein gemessener Winkel bestimmt nur ein Längen*verhältnis*; messbar ist allein H₀·L_res ≈ 458 km/s. Jedes Modell muss eine absolute Skala einsetzen — die Frage ist nicht *ob*, sondern **wo man in den Kreis eintritt**. Dok. 267 bucht das bereits korrekt („Zirkulär? Ja | Ja"; „der faire Vergleich ist nicht ‚wer ist zirkelfrei' — keiner ist es — sondern Sparsamkeit gegen Verankerung"). **Der Eintrittspunkt muss aber gezählt werden**, sonst stimmt die Sparsamkeitsrechnung nicht: ein kalibrierter Exponent ist eine *Eingabe*, keine Ableitung, und die ξ-Potenzform verbirgt sie. **Der Vergleich bleibt gültig und fällt weiter zugunsten der Sparsamkeit aus:** FFGFT setzt *eine* deklarierte Sektor-Skala; ΛCDM gewinnt r_s aus sechs Parametern plus BBN-Frühphase, und sein H₀ ist eine Pipeline-Ausgabe, die Expansion, FLRW und Materiegehalt voraussetzt. **P35 trifft allein die Notation**, nicht die strukturell notwendige eigene Skala (Dok. 182/306). Empfohlene Sprachregelung: die kosmologische Skala **offen als die eine externe Eingabe des Sektors deklarieren**. Offen: R_H → ℓ₁ (P20).

- **Dok. 306 erweitert (4) — „Und dazwischen: eine Projektion, keine Struktur":** Die Anordnung der Systeme auf einer gemeinsamen Achse (von maximaler zu minimaler Massenkonzentration) ist eine **Außenbetrachtung** — sie setzt einen Standpunkt voraus, den FFGFT nicht kennt. T·m = 1 gilt **je System**; es gibt kein gemeinsames T, gegen das aufgetragen werden könnte. Schärfer: **Wir projizieren uns in die Mitte.** Die Achse entsteht mit dem Betrachter als Nullpunkt; die Mitte ist keine Entdeckung, sondern eine Setzung, und sie bleibt unbemerkt, weil der Setzende und der Verortete dasselbe sind. Die Ränder erscheinen deshalb als „extrem" — *extrem* heißt hier *fern*, nicht *ausgezeichnet*. **Die intrinsische Zeit bleibt unberührt:** Für ein Elektron ist ohne Belang, wo ein Außenstehender es einträgt — seine Windung ist dieselbe im Labor wie nahe einem Horizont (T = 1/m, m ist dasselbe). Auch die „langsamste Zeit" am Horizont ist eine Aussage über den *Vergleich*, nicht über das *Erleben*. Die Projektion ist damit **Werkzeug, nicht Struktur**: ohne gemeinsame Achse ließe sich nichts vergleichen. Dieselbe Bewegung, die die Frage nach t=0 und die Singularität auflöste — jetzt auf die **Skala selbst** angewandt; zugleich die schärfste Form der Selbstbezüglichkeit (Dok. 248): der Gedanke, der die Ordnung entwirft, **verortet sich, indem er ordnet**.

- **Dok. 306 erweitert (5) — „Skalen, nicht Summen" + Abbildung:** **Präzisierung:** T₀ und E_max sind **Skalen**, keine Schranken für Gesamtheiten. T₀ ist das minimale Zeit*inkrement*, E_max die maximale Energie **pro fundamentaler Zelle** bzw. pro elementarer Anregung — ein **Cutoff**, und ein Cutoff begrenzt eine einzelne Mode, nie eine Summe. Die Gesamtenergie eines zusammengesetzten Systems darf beliebig groß sein (viele Zellen, nicht dichtere). „Das T der Erde" ist keine wohlgestellte Größe; ħ/(Mc²) für eine Sternmasse ist eine **Fehlanwendung**. Entsprechend betrifft die Schwarzloch-Aussage die **Konzentration**, nicht die Masse: am Horizont erreicht die *lokale* Dichte den Zellen-Cutoff, die **Gesamtmasse bleibt unbeschränkt**. — **Neue Abbildung** (Abb. „306_hyperbel"): T·E = 1 doppelt-logarithmisch = **Gerade der Steigung −1**. Alle elementaren Anregungen (Elektron, Myon, Proton, Top, Planck) liegen exakt darauf — keine ist ausgezeichnet, die Gerade hat **keine Mitte**. Ausgezeichnet ist genau **ein** Punkt: der **Endpunkt** (T₀, E_max) = (ξ·t_P, E_P/ξ), an dem die Kurve *aufhört*. Am anderen Ende **Asymptote** — nie erreicht. Die Ränder sind also **verschiedenartig**: links ein erreichter Endpunkt, rechts eine unerreichbare Grenze.
