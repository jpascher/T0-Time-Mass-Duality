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

---

## Doc. 319 — The Proton as a Vibrating Torus (21 August 2026, DE+EN, 6 pp. each)

*(Already listed above — updated 22 August 2026)*  
[S] markers for SU(3)_c and fixed-point conditions updated to [B]/[K]
following Docs. 321 and 322.

---

## Doc. 320 — Detailed Field-Geometric Spectral Theory (22 August 2026, DE+EN, 12/8 pp.)

Step-by-step derivation of all lepton masses and neutrino spectra from ξ = 4/30000
and T⁴/ℤ₃ topology, numerically verified by `320_verify.py`.

**Charged leptons [K]:** m_e = 0.511 MeV (<0.1 %), m_μ = 104.96 MeV (−0.66 %),
m_τ = 1783.5 MeV (+0.38 %). Parameter-free ratios derived.

**Neutrinos:** m_ν1 = 0.976 meV, m_ν2 = 9.084 meV, m_ν3 = 44.51 meV.
Δm²₂₁ = 8.16×10⁻⁵ eV² (+8.3 %) [K]. Δm²₃₂ = 1.90×10⁻³ eV² (−22 %) [S open].
Σm_ν = 54.57 meV < 0.12 eV ✓  
→ [DE](2/pdf/320_Spektraltheorie_De.pdf) · [EN](2/pdf/320_Spektraltheorie_En.pdf)

---

## Doc. 321 — Algebraic Derivation of the SU(3)_c Gauge Structure (22 August 2026, DE+EN, 11/8 pp.)

Closes the bridge marked [S] in Docs. 319, 320, 322.

**Key results [B]:** Three ℤ₃ projectors P_k on L²(T⁴) constructed and proved.
Eight Gell-Mann operators from eigensectors H_0, H_1, H_2: su(3) commutation
relations verified with canonical structure constants. N_c = 3 algebraically necessary.
Confinement = triality selection T_R = 0 (Doc. 049 algebraically). U(1)_Y from T¹
direction. SU(2)_L from ℤ₂ pairing H_1↔H_2. sin²θ_W|_GUT = 3/8 from trace formula.
Verification: `321_verify.py` (50+ assertions).  
→ [DE](2/pdf/321_SU3_Z3_Emergenz_De.pdf) · [EN](2/pdf/321_SU3_Z3_Emergenz_En.pdf)

---

## Doc. 322 — Spectral Theory and Hilbert-Space Embedding (22 August 2026, DE+EN, 12/8 pp.)

**Key results [K]:** ξ = λ_min(F̂_D4) as spectral eigenvalue. State space
H_FFGFT = H_geom ⊗ H_spin ⊗ H_flavor. Fractal measure with 100-fold recursion;
D_f = 3 − ξ emergent. Fixed-point boundary conditions ψ_χ(x₀+y) = χ·ψ_χ(x₀+g*(y))
ground neutrino localisation. GFT, MASA basis. Gell-Mann matrices from orbifold modes [B].
Open [S]: full self-adjointness proof for F̂.  
→ [DE](2/pdf/322_Spektraltheorie_Hilbert_De.pdf) · [EN](2/pdf/322_Spektraltheorie_Hilbert_En.pdf)

---

## Doc. 323 — Derivation of the Weinberg Angle at M_Z (22 August 2026, DE+EN, 8/5 pp.)

Closes the RGE bridge declared [S] in R78 and Doc. 321.

**Main result [K]:**
sin²θ_W(M_Z) = 3/8 − (55 α_em(M_Z))/(24π) [ln(m_Pl/M_Z) + (19/12) ln ξ] = **0.2308**
(PDG: 0.2312, deviation **−0.19 %**).

M_GUT = m_Pl · ξ^(19/12) = 8.94×10¹² GeV. Exponent p = 19/12 = p_e + 1/(4N_c) = 3/2 + 1/12.
Verification: `323_verify.py`.  
→ [DE](2/pdf/323_Weinberg_Winkel_RGE_De.pdf) · [EN](2/pdf/323_Weinberg_Winkel_RGE_En.pdf)

---

## Corrections Register — R79–R83 (22 August 2026)

**R79** — SU(3)_c emergence from ℤ₃ triality [B] (Doc. 321). Closes [S] from Docs. 319/320/322.

**R80** — SU(2)_L, U(1)_Y, sin²θ_W|_GUT = 3/8 [B] (Doc. 321).

**R81** — Weinberg angle sin²θ_W(M_Z) = 0.2308 [K], −0.19 % (Doc. 323). Closes R78.

**R82** — Hilbert-space embedding, fixed-point boundary conditions [K] (Doc. 322).

**R83** — Status update: 8 bridges closed; remaining open: Δm²₃₂ (−22 %, Doc. 320),
self-adjointness of F̂ (Doc. 322), 2-loop α_s corrections, m_Pl and α_em from ξ,
quark/hadron sector (Doc. 318).

## Verification Scripts

`python/Dok320_321_322_Skripte/`:
- `320_verify.py` — lepton masses, neutrino spectrum, mass-squared differences
- `321_verify.py` — SU(3) algebra, Gell-Mann matrices, Weinberg trace formula (50+ assertions)
- `320_322_verify.py` — combined check for Docs. 320 + 322
- `323_verify.py` — Weinberg angle RGE derivation
