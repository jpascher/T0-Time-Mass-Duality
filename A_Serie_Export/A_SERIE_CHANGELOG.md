# CHANGELOG — FFGFT A-Serie

Alle wesentlichen Änderungen dieser Serie. Format: Datum · Dokument · Inhalt.

---

## v1.1 — 2026-07-23

### Neu: Zwei Dokumente (45 De + 45 En)

**Block 1 — Sektoren**
- **A155 Meson-Massen und Baryon-Kandidat** (De+En, je 6 S.) — Eigenständiger
  additiver Ansatz m_M = Σm_q + Λ_QCD·K_frak^n_eff mit Geltungsbereichs-Beweis
  (Formeigenschaft: nur Bindung < Λ_QCD; Pionen drin, K/η/ρ/ω strukturell
  draußen). Pion-Anker: n_eff(π⁰)=37,79, n_eff(π±)=36,62 — verankert die
  Meson-Stufe 36+1 aus A270. GMOR-Prüfung: B_π≈B_K (chirale Konsistenz);
  [S]-Kandidat B ≈ 8·Λ·K_frak⁻³⁷ (zentral 0,02 %, P35: Quarkmassen-Schema
  trägt Präzision nicht). Baryon-Kandidat [S]: vollständig geometrische
  Proton-Formel m_p = (π³/12)·N_c(1+α_s)·e^(−3ξ/4)·Λ/2 (Δ=+0,21 %,
  absorbierbar in α_s/Λ); jeder Faktor gedeutet (Vol(B⁴)=π²/2,
  η_sc=π/6, Farbe, ξ-Dämpfung, Skala). Strukturfund:
  16π³/(π³/12) = 192 = D4-Weyl-Ordnung — Proton-Geometrie und
  Higgs-Formel (Dok. 190 K1) im exakten Weyl-Verhältnis. Alle externen
  Eingaben (Λ_QCD, Quarkmassen) explizit als [SETZUNG] deklariert;
  kein Bezug auf Altdokument 005.

**Block 3 — Erweiterungen**
- **A270 Z₃-Sektor-Struktur und Hadron-Massenkorrektur** (De+En, je 6 S.) —
  Bulk-Exponent 36: Schlüsselrelation K_frak⁻³⁶ ≈ 16/π² (Δ=0,010 %),
  unabhängig gestützt durch k*/100=36,09 (Dok. 275); Monte-Carlo-Statistik
  (Trefferrate 1,5 %; Spezifität: einziger Treffer unter 21 Konstanten).
  Orbifold-Struktur [B]: 3 Fixpunkte, Z₃-Eigenbasis (1, ω, ω²);
  Confinement topologisch erzwungen (Fixpunkt-Bedingung x=y=z),
  Leptonen frei. Sektor-Tabelle [H]: Lepton 36+0, Meson 36+1, Baryon
  36+2 — topologisch fixiert (|Z₃|−1=2). Meson-Stufe am Pion empirisch
  verankert (A155). Koide-Konsistenz: Zirkulant (A110) als Algebra des
  ungetwisteten Sektors liefert Kandidaten für den Grund des
  A150-Befunds („Zirkulant-Ebene hat kein Gegenstück"). Baryon-Stufe
  als Vorhersage (K_frak⁻³⁸ = 1,6654), Test wartet auf
  Vorwärts-Herleitung des Baryon-Kandidaten (A155).

### Register (Dok. 190, append-only)
- **R62** (Eintragstext in `Dok190_R62/ (De+En)`, zum
  Einfügen nach R60): Altkorpus-Dok. 005, Proton-Beispielrechnung —
  Anker der Formelzeile ist π²/2 (Vol B⁴), nicht m_μ; Fehlfaktor 46,672
  = (π²/2)/m_μ auf 0,07 %. Reparierte Zeile schließt mit unveränderten
  Druckwerten auf +0,05 % (PDG) bei geschlossener Dimensionsbilanz.
  Sekundärbefund: Druckwert K_corr=0,985 ≠ Formelwert 0,9605 (2,5 %).
  Aufspaltung QZ·K_corr unterbestimmt; geometrischer Kandidat π/6 in
  A155 §Baryon-Kandidat. Quelldokumente nicht revidiert (vgl. R50).

### Prüfskripte (alle Assertions bestanden)
- `python/A_Serie_Skripte/a155_meson.py` — Geltungsbereich, Pion-Anker,
  GMOR, 8Λ·K⁻³⁷-Kandidat, Proton-Kandidat, 192-Identität.
- `python/A_Serie_Skripte/a270_z3_sektoren.py` — Schlüsselrelation,
  k*/100, Fixpunkte (numerisch), Z₃-Eigenbasis (numerisch),
  Sektor-Tabelle, Monte-Carlo, Spezifität.
- `python/Dok190_Skripte/r62_baryon_anker.py` — Diagnose, Reparatur,
  Dimensionsbilanz, Sekundärbefund.

### Build
- LuaLaTeX je 3 Durchläufe; 4 neue PDFs (2 De + 2 En), 0 Fehler.

---

## v1.0 — 2026-07-22

### Neu: Vollständige A-Serie (43 Dokumente)

**Block 0 — Grundlage**
- A010 Zweck, Aufbau, Lesart der A-Serie (KI-Abschnitt vorne; neuer Abschnitt: eigenständige Altbestand-Dokumente)
- A015 Ursprung von ξ: 5 Plausibilitätsgründe; kein Beweis möglich/nötig (R-Entscheid diese Session)
- A020 Die drei Setzungen
- A030 Kompakte Geometrie T⁴/Z₃
- A040 Fraktale Korrektur K_frak = 74/75
- A050 Rekursion und Nichtschließung
- A060 Zeit: kompakte Richtung, native Reziprozität T·E = 1 (ersetzt Heisenberg-Begründung, R50)
- A070 Hilbertraum-Brücke H = L²(T⁴)⊗ℂ³
- A075 Feldtheorie: Modefunktionen, Lagrangian, Brückenformel
- A080 Einheiten und Buchhaltung
- A085 Natürliche Einheiten: der fundamentale Grund
- A090 Projektionskette T⁴→T⁰: drei Operationen (Typ I/II/III)
- A095 Torus-Chiralität (umbenannt aus A268)

**Block 1 — Sektoren**
- A100 Leptonleiter: ξ-Formel, Verhältnisse korrekturfrei
- A105 Leiter-Grundeinheit N₀
- A110 Zirkulant und Koide: Q = 2/3, θ = 2/9
- A120 θ = 2/9: Ort, Status, Grenze
- A130 Feinstrukturkonstante α = ξ·E₀² (Higgs-EFT 2.3%-Abweichung erklärt)
- A135 Was auf Eins gesetzt werden kann, ist nicht grundlegend
- A138 Anomale magnetische Momente: g−2 Verhältnisse exakt
- A140 Gravitation: G als Brücke, QG-Problem nicht gestellt
- A142 Gravitationsdynamik: Zeitfeld-Lagrange
- A145 Gravitationskonstante G = ξ²/(4m_char)
- A150 Quarks und Neutrinos: Stand und Spekulationsanteil
- A160 Quantenmechanik auf T⁴: Bell als Topologie (CHSH-Vorfaktor ξ/(2π) geometrisch begründet)
- A165 Bell-Tests und Hardware: IBM Heron r2 Mai 2026
- A180 Information: Windungsquant Δw = 1
- A190 Standardmodell als dekompaktifizierte Projektion (3 Eichsektor-Argumente)
- A192 Eichsektor: Torus-Topologie und kovariante Ableitungen (neu diese Session)

**Block 2 — Methodik**
- A200 Ordnung ohne Rangordnung: vier Schichten
- A210 Falsifizierbarkeit: vier Prognosegrößen
- A220 Toleranzmaßstab: vier Genauigkeitsklassen
- A230 Offene Punkte: Residuen der Serie
- A240 Abgrenzung: Standardmodell, Relativität, externe Rahmen
- A250 Verweistabelle: A-Serie und Altbestand

**Block 3 — Erweiterungen**
- A260 Casimir-Effekt: Vakuumstruktur, Bestätigung 4/3
- A261 Skalenhierarchie: ξ → Massen → α → E₀
- A262 c-Konvention: E = mc² = E = m
- A263 Dirac-Gleichung vollständig: Clifford-Algebra, Spin, Massenelimination
- A264 Strukturelle Asymmetrien: Chiralität, Gravitation, Monopole
- A265 Rotverschiebung: statisch, achromatisch, ohne Expansion
- A266 Einheitenprüfung und SI-Rückrechnung
- A267 Stipulation α = 1: Ladungsumdefinition, 137-Leiter

### Korrekturen und Entscheide (diese Session)

| Ref | Dok | Inhalt |
|-----|-----|--------|
| R-Entscheid | A015 | ξ-Beweis nicht möglich/nötig; 5 Plausibilitätsgründe statt Forderung geometrischer Ableitung |
| R-Entscheid | A142 | Gravitationsquantisierung nicht gefordert; G intrinsisch aus ξ |
| R50 | A060 | T·E = 1 nativ; Heisenberg-Begründung ersetzt (Konklusion unverändert) |
| R54 | A060 | Kein N₀ als Grundeinheit; Moden sind kommensurable Vielfache von d₁ = 1/75 |
| R52 | A210 | L₀-Zahlenwert am Standard-Anker korrigiert; 5.39×10⁻³⁹ m als Übertragungsfehler verworfen |
| neu | A190 | Higgs-EFT 2.3%-Abweichung strukturell erklärt (SI-Werte schemaabhängig + K_frak in v nicht trennbar) |
| neu | A192 | Eichsektor: U(1) aus Flussquantisierung, SU(3) aus Verschlingungszahl (beide [B]) |
| neu | A095 | g_R = 0 auf [B] angehoben: Kern-Argument Torus-Projektor P₊ |
| neu | A160 | CHSH-Vorfaktor ξ/(2π) geometrisch begründet: Kreisumfang als Konversionsfaktor |

### Technisch

- 43 × De-PDF, 43 × En-PDF (je 3 LaTeX-Läufe, TOC korrekt)
- 45+ Prüfskripte in python/A_Serie_Skripte/
- Alle En-Wrapper-Titel auf Englisch
- KI-Abschnitt in A010 vorne (alle anderen am Ende)
- A268 → A095 umbenannt; Altdateien entfernt

---

## Vorgeschichte (Altbestand, nicht A-Serie)

| Version | Datum | Inhalt |
|---------|-------|--------|
| v1.2.3 | 2026-07 | Korpus-Restrukturierung; Skripte in DokNNN_Skripte/; README DE+EN |
| v1.2.2 | 2026-06 | Korrekturregister R54–R56; Dok 306 (native Zeit-Energie-Reziprozität) |
| v1.1.0 | 2026-05 | Hilbertraum-Brücke (Dok 230/231/232); Zenodo-Release 10.5281/zenodo.20117635 |
| v1.0.x | 2025–2026 | Aufbau des Altbestands (300+ Dokumente) |

---

*Verantwortung für Inhalt und Fehler liegt vollständig beim Autor.*
