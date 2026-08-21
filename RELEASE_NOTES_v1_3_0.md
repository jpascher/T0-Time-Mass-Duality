# Release Notes — v1.3.0 (August 2026)

**DOI:** Zenodo-Upload ausstehend — ersetzt v1.2.8

Laufendes Korrekturverzeichnis: **2/pdf/190_T0_Korrekturen_De.pdf**  
Changelog: **000_FFGFT_Changelog_De.md**

---

## Neue Dokumente

### Dok. 317 — Topologischer Ursprung der Leptonen-Generationen: KSAU und FFGFT (DE+EN, je 7 S.)

Vergleichs- und Synthesedokument zwischen der KSAU-Theorie (Knot-Synchronization-Adhesion Unified Theory, Zenodo 2026) und FFGFT. Enthält:

- **Vollständige Quantenzahltabellen** $(n_\theta, n_\phi, r_i, p_i)$ für alle sechs Leptonen (geladene + Neutrinos)
- **KSAU-Knotenstruktur:** $3_1$ (Trefoil/Elektron), $6_3$ (amphicheiral/Myon), $7_1$ (Torusknoten/Tau) mit Seifert-Genus, Alexander-Polynom-Span, Möbius-Energie-Status
- **Strukturelle Entsprechung** KSAU ↔ FFGFT: Generations-Skalierung, Symmetrie-Pivot, chirale Projektion
- **Torus-Knoten-Brückentheorem** [S]
- **Mathematische Präzisierungen:** Blatt et al. (2025, arXiv:2512.02998) beweisen kritische Punkte der Möbius-Energie in Torus-Knoten-Klassen; exakte analytische $E(K)$-Werte für $3_1$, $6_3$, $7_1$ nicht bekannt (nur numerisch, Kim & Kusner 1993)
- **Literatureinordnung:** Jeon et al. (2024, arXiv:2407.11731) behandelt Knotensolitonen für Baryon-Asymmetrie, kein Bezug zu Leptonenmassen; Avrin (2012, *Symmetry* MDPI, peer-reviewed) korrekt zitiert
- **Statusmarker** in Synthesetabelle und KSAU-Warnblock: FFGFT-Seite [K]/[B], KSAU-Knotenzuordnung [S]/[SETZUNG]

**Dok. 006 DE+EN** ergänzt: Unterabschnitt „Wicklungszahlen und topologische Zuordnung" mit vollständiger $(n_\theta, n_\phi)$-Tabelle und Verweis auf Dok. 317.

---

### Dok. 318 — Geltungsbereich der Masseableitungen in FFGFT (DE+EN, je 8 S.)

Explizite Grenzziehung des $\xi$-Ableitungsrahmens. Enthält:

- **Physikalische Begründung** aus der vollständigen Energierelation $E^2 = (m_0 c^2)^2 + (pc)^2$: masselose Gluonen tragen 99% der Protonmasse als Bewegungsenergie
- **Eingerollt vs. ausgerollt** (Dok. 311): Quark-Ruhemassen = eingerollte Moden (Yukawa, $\xi$-Ableitbar); Gluonenenergie = ausgerollte Moden (QCD-Dynamik, offene Brücke)
- **Geltungsbereichstabelle:** Leptonen [K], Neutrinos [S], Quark-Ruhemassen [S], Hadronen gesamt: offene Brücke, $m_p/m_e$: nicht beansprucht
- **$K_\text{frak}$ als Interface-Faktor:** tritt beim Übergang $m^\text{bare} \to m^\text{SI}$ auf, kürzt sich in Massenverhältnissen heraus (Dok. 012); kein QCD-Beitrag
- **Drei Szenarien für die QCD-Brücke** [S]: Orbifold-Geometrie ($\Lambda_\text{QCD} = v\cdot\xi^{1/3}$, Dok. 041 als erster Schritt), Spuranomalie auf Torus-QFT (Khanna et al. 2014), Hadronsektor mit SM-Inputs (Dok. 005, aktueller Stand)
- **$\alpha_s$ und laufende Kopplung:** Dok. 160 leitet $\alpha_s(m_\tau) = 3\xi^{1/4} \approx 0{,}322$ geometrisch ab [K]; Dok. 005 verwendet $\alpha_s(M_Z) = 0{,}118$ als SM-Input — konsistente verschiedene Skalen; RGE-Brücke innerhalb FFGFT offen [S]
- **Frühe Dokumente (Dok. 001–041):** Strukturskizzen in natürlichen Einheiten, keine SI-Präzisionsableitungen (R77)
- **Zeichenerklärung** ($M_Z$, $\Lambda_\text{QCD}$, $\alpha_s(\mu)$, $D$, $y_e$, RGE, $K_\text{frak}$, $m^\text{bare}$, $m^\text{SI}$)

---

## R75 — Neufassung der Shor-/Quantencomputing-Dokumente

Deklariert 17.–20. August 2026. Betrifft Dok. 024, 034, 075, 076, 147, 173, 176, 190, 006.

Kernkorrekturen: $\xi$/$\sigma$-Parametertrennung, Aufbereitung ≠ Transformation (95%/5% Gatterkosten), Weyl-Obstruktion als universelle Grenze (nicht FFGFT-spezifisch), Fouriertransformation als Projektion, Gottesman-Knill offen.

**Dok. 075 DE+EN** (je 10 S.): vereinigt — Teil I RSA-Grundlagen, Teil II Periodenfindung als Resonanzproblem.

Prüfskripte: `2/python/Shor_Skripte/s1_periodensuche.py`, `s2_grenzen.py`, `s3_thermik_zustandsraum.py`  
Abhängigkeiten: `2/python/requirements_147.txt` (numpy, scipy, matplotlib, pandas, ephem)

---

## Register-Einträge R76–R78 in Dok. 190

**R76** — Geltungsbereich der Masseableitungen: Leptonen [K], Hadronsektor offene Brücke, $m_p/m_e$ nicht beansprucht.

**R77** — Einordnung früher Kopplungskonstanten-Formeln (Dok. 041): Strukturskizzen in natürlichen Einheiten, keine SI-Präzisionsableitungen. $\xi^{-1/3} = 9{,}65$ (natürliche Einheiten) ≠ $\alpha_s(M_Z) = 0{,}118$ (SI). Status: [S].

**R78** — $\alpha_s$ und laufende Kopplung: $\alpha_s(m_\tau) \approx 0{,}33$ und $\alpha_s(M_Z) \approx 0{,}118$ sind verschiedene Werte derselben laufenden Kopplung. Dok. 160: $3\xi^{1/4}$ bei $m_\tau$ [K]. RGE-Brücke zu $M_Z$ offen [S].

---

## HTML-Simulator

`t0_Shore_simulator.html`: alle T0-Bezeichnungen durch FFGFT ersetzt; $\xi \to \sigma$ in Formeln und Anzeigetexten; Weyl-Obstruktion als universelle Grenze; $M_Z$-Erklärung.

---

## Dok. 319 — Das Proton als schwingender Torus (21. August 2026, DE+EN, je 6 S.)

Geometrische Beschreibung des Protons in der FFGFT. Vor Fertigstellung
systematische Diskussion aller Statusmarkierungen aus dem Korpus.

**Aus Korpus-Recherche neu als [K] belegt:**
- Fermion-Statistik aus D4-Trialität (halbzahlige Elemente, Dok. 314)
- Diskretes Spektrum auf $\mathbb{Z}_3$-Faser, nicht auf ausgerollter Achse (Dok. 285)
- Einschluss ist relational: wir beschreiben immer von innen (Dok. 248)
- Für $m=0$: $d\tau=0$ exakt, kein Ruhesystem; lokal immer $E=pc$ (Dok. 312)
- Photon und Gluon: beide masselose Feldmoden, keine Teilchen (Dok. 049)

**Gluon [S]:** $\mathbb{Z}_3/SU(3)$-Feldmode, stehende Welle im Proton-Torus,
nicht lokalisierbar, 8 Gluonmoden = 8 $SU(3)_c$-Generatoren (Dok. 145).

**Offene Fragen [S]:** $SU(3)_c$-Emergenz, Photon/Gluon-Sektortrennung,
$\Lambda_\text{QCD}$, RGE-Brücke, formale Randbedingungen auf $T^4/\mathbb{Z}_3$.
