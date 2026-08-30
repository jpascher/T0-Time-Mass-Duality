# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---

## 27. August 2026 — Dok. 324 Korrektur · Register R97

### Dok. 324 — Vakuumoperator-Korrektur (De+En)

Nach Doug Matzkes Einwand (IPI-Mail 26. Aug. 2026) und numerischer Prüfung
durch `pruef_324_vakuum_involution.py` (22 Assertions):

Matzkes Vakuumoperator ist **R97 [B]:**

    V = N₁⁺N₂⁺N₃⁺N₁⁻N₂⁻N₃⁻ = −64 · (Pn1·Pn2·Pn3)

In ℤ₃ℂ-Arithmetik: −64 ≡ −1 (mod 3), also V² ≡ −V (Involution).

Dok. 324 hatte irrtümlich das Pp-Produkt Pp1·Pp2·Pp3 (komplementärer
Teilchen-Sektor, anderer Strahl: |⟨vac_V|vac_Pp⟩| = 0) als Matzkes V
behandelt. Korrekturen in De+En: Symboltabelle, Konstruktionsabschnitt,
Spektrumssektion, Vergleichstabelle, Gesamtstatus-Box.

Unverändert korrekt [B]: Trine-Theorem T_k³ = I · ξ kein Spektralwert.

---

## 26. August 2026 — v1.3.4: Dok. 328, 330, 332 · Register R93–R96

### Dok. 328 — Kopplungsregime, Resonanz und Synchronisation (DE+EN, je ~12 S.)

Nachrichtentechnische Dreiteilung (unterkritisch / kritisch / überkritisch,
relativ zu Systemdämpfungen) als strukturelles Ordnungsprinzip. Dieselbe
Struktur kehrt in Quantenoptik (strong coupling), Teilchenphysik (Mischung,
avoided crossing) und Synchronisationstheorie (Kuramoto-Schwelle, Arnold-Zungen)
wieder. Für FFGFT: natürliche Sprache für Teilchen als Resonanzzustände.

- **[B]** Wörterbuch Zweikreis ↔ 2×2-Mischung; Ausnahmepunkt g_EP = |γ₁−γ₂|/4
- **[B]** Dualität D²+V²=1 für alle reinen Zeiger; Messübergang κ = d/(2σ)
- **[K]** κ_mix(θ_W) ξ-abgeleitet über Komposition mit Dok. 323; Screening negativ
- **[B]** GST-Textur H₁₂=√(m₁m₂) symbolisch bewiesen (Dok.-041-Formeln)
- **[K]** K_eff = 2πξ ≈ 8,4×10⁻⁴; φ außerhalb aller Arnold-Zungen
- Vier Prüfpunkte in Dok. 041 identifiziert (Autorenentscheidung erforderlich)

**Neu:** Marker **[E]** eingeführt für etablierte externe Formalismen
(Zweikreis, Kuramoto) ohne Korpus-Freigabe als [K]/[B].  
Zehn Prüfskripte.

### Dok. 330 — Drei Operationen von T⁴ zum Beobachtraum (DE+EN, je ~14 S.)

Konsolidiert Typ-I/II/III-Klassifikation (Dok. 270); grenzt FFGFT von diskreten
Emergenzmodellen ab. HLV (Krüger, August 2026) als Fallstudie.

- **Typ I [B]:** S¹_m → ℝ_t via T̃·m=1; informationserhaltend (Pullback p*)
- **Typ II:** D3→D2→D1 geometrische Projektion; verlustbehaftet
- **Typ III [K]/[B]:** T⁴ ↔ H bijektiv, verlustfrei
- **T⁴ flach [K]:** K=0 punktweise via Metrik-Abstieg (R95)
- **D₄-Spezifitätstest [S]:** adversariell gegen angepasste Träger — offen

**R93 [B]:** S_BH(M_coll) = 2π nat = n_thresh(Matzke) in Bit;
Restentropie des Endpunkts (Dok. 325, 329)  
**R94 [B]:** I_Sektor/I_thermisch = log₂3 für alle M;
Strukturkonstante der ℤ₃-Geometrie (Dok. 325)  
**R95:** Zwei Formulierungspräzisierungen nach externem Review (Krüger):
(i) Flachheit K=0 punktweise [B]; (ii) „selbstadjungiert" = beschränkt + symmetrisch;
(iii) Typ-I-Pullback p* [B]; (iv) D₄-Spezifitätstest [S] offen

### Dok. 332 — Zwei Wege vom Diskreten zum Kontinuum (DE+EN, je ~16 S.)

Allgemeiner Vergleichsaufsatz (kein originärer FFGFT-Beweistext).
Referiert Krügers Preprint (Zenodo DOI 10.5281/zenodo.22105698).

Zwei Strategien: (1) Regge/Kettenkomplex — Kategorienfehler blockiert,
Kontinuumslimes via Mosco-Konvergenz *postuliert*. (2) Kanonischer
Funktions-Pullback (FFGFT) — Per_{Rm}(ℝ_t) ≅ L²(S¹_m) [B] (R96).

**R96 [B]/[K]** (zweite Krüger-Rückmeldung, 26. Aug. 2026):
Per_{Rm}(ℝ_t) mit Pro-Periode-Norm ≅ L²(S¹_m), NICHT L²(ℝ_t) —
Pullback ist Darstellungswechsel, kein neuer Sektor [B].
Nash–Kuiper-Zuschreibung in Dok. 330/R95(i) korrigiert:
Existenzsatz für C¹, keine C²-Nichteinbettbarkeitsaussage [K].  
Prüfskript: `pruef_332_krueger_periodizitaet.py`

---

### Dok. 333 — K_frak, Ausrollen und die T̃·m-Dualität (DE+EN, je 5 S.)

Eigenständiges FFGFT-Dokument (27. Aug. 2026). Klärt zwei im Korpus
bisher vermischte Bedeutungen von „Ausrollen" und bindet die Rekursion
zwingend an die T̃·m-Dualität.

**Typ I (Messakt, verlustbehaftet):** bisheriger Korpus-Sprachgebrauch
(Dok. 285): S¹_m → ℝ_t, Windungszahl verworfen — Brücke zur Beobachtung.

**Typ III (Pullback, verlustfrei):** kanonischer Funktionen-Pullback
L²(S¹_m) ≅ Per_{Rm}(ℝ_t) (Dok. 332/R96) — reiner Koordinatenwechsel,
m und t rollen gemeinsam, kein Informationsverlust [B].

**K_frak am Pullback:** nicht beteiligt. Sitzt in der Wahl von
R_m = ℏ/(m·c²) über die Massenformel; sichtbar erst beim SI-Übergang
über Brückenkonstanten E₀, v (Dok. 314/R72) [B].

**Rekursion zwingend aus T̃·m=1:** Jede Massenänderung erzwingt
Zeitänderung → ξ_{n+1} = ξ_n(1−100·ξ_n) (Dok. 295/146).
Fall B (stabil, K_frak=74/75) = Projektion von Fall C
(laufende Rekursion, Log-Spirale) auf statische Näherung [B].
Fall A (K_frak=1) strukturell ausgeschlossen [B].

Dok. 332 auf kurzen Querverweis zurückgebaut.

**R97 [B]:** Vakuumoperator-Korrektur Matzke/Dok. 324 (26. Aug. 2026)
(bereits in Dok. 190 eingetragen)

**R98 [B]:** Zwei Ausroll-Bedeutungen + Rekursionsbindung (Dok. 333)

---

### Dok. 334 — Superposition ohne Zeit (DE+EN, 6/5 S.)

Eigenständiges FFGFT-Dokument (27. Aug. 2026). Fokus: was bedeutet
die Abwesenheit des Zeitoperators in der QM konkret für
Superposition, Verschränkung und Kollaps?

**§1 Klassische Vorgeschichte:**
Newton, Coulomb, Hamilton — alle instantan, $t$ externer Parameter.
Pauli hat nur explizit gemacht was klassisch stillschweigend war.

**Verborgene Inkonsistenz:** Zustand $\psi(t)$ ist instantan,
aber probabilistische Auswertung $|\psi(t)|^2$ braucht echte
Zeit. Der Formalismus ist instantan, seine Verifikation zeitlich
ausgedehnt — diese Spannung fehlt im Formalismus.

**Superposition doppelt zeitlos:** kein intrinsisches „Wann",
keine Verifikation ohne Zeitaufwand; jede Messung kollabiert
die Superposition.

**Kollaps ohne Dauer** im QM-Formalismus.

**Pauli-Theorem** greift nicht für kompaktes $\tilde{T}$.

**FFGFT-Auflösung:** $\tilde{T}_i=1/m_i$ gibt jeder Mode
intrinsische Zeitskala; modenübergreifend inkompatible
$\tilde{T}_i\neq\tilde{T}_j$.

Verweise: Dok. 174, 285, 306, 307, 333.

**R99 [B]/[K]:** Superposition ohne Zeit — Dok. 334

---

### R100 — ξ als Galois-Zahl [K] (28. August 2026)

**Kernidentität** (pruef_331):
$(r_\mu/r_e)^2/\xi = |\text{GF}(9)^*|^2\cdot5^2\cdot|\text{GF}(27)| = 43200$

Wicklungszahlen vollständig aus GF$(3^n)$: $n_{\theta,1}=3=\text{char}$, $n_{\phi,1}=2=|\text{GF}(3)^*|$, $n_{\theta,2}=5=\text{min.Prim}(|\text{GF}(81)^*|)$, $n_{\phi,2}=4=\varphi(5)$, $n_{\theta,3}=9$, $n_{\phi,3}=5$. Rekursion: $n_{\theta,g}=n_{\theta,g-1}+n_{\phi,g-1}$. ξ = 4/30000 folgt algebraisch. Dok. 317 (§xi-Galois), 336 (§6), 338.

---

### R101 — 1/α = 3700/27 aus Galois [K] (28. August 2026)

**Neue Beobachtung** (pruef_332): $m_e\cdot m_\mu = 54 = |\text{GF}(3)^*|\cdot|\text{GF}(27)|$ MeV² (0,016\%; nicht empirisch — Dok. 011 leitet $E_0=\sqrt{m_e m_\mu}$ geometrisch her).

Einsetzen in $\alpha=\xi E_0^2/K_\text{frak}$: $|\text{GF}(27)|=27$ kürzt sich heraus.

$$1/\alpha = 3700/27 = 137{,}037\quad(\text{Abw. 7,6 ppm})$$

Kein ξ, kein $v$, kein $m_e$ als expliziter Eingang. Einzige SI-Brücke: MeV. Dok. 338.

---

### Dok. 339 — Frobenius-Trennung massiv/masselos in GF(27)* (DE+EN, 10 S.)

Eigenständiges FFGFT-Dokument (29. Aug. 2026). Frobenius-Zerlegung
$GF(27)^*\cong\mathbb{Z}_{26}\cong\mathbb{Z}_2\times\mathbb{Z}_{13}$:

**§1 Ausgangspunkt:** GF(27)* = Z₂₆ unter φ: x ↦ x³. Zwei Fixpunkte
{+1,−1} = massiver ℤ₂-Sektor. Acht Dreier-Orbits = 8 Gluonen.

**Kernresultat [B]:** Orbit₄ = 2⁻¹·Orbit₁ in ℤ₁₃:
{7,8,11} = 7·{1,3,9} (mod 13). Orbits 2 und 4 algebraisch invers
(2⁻¹=7, 7⁻¹=2). Fixkörper GF(3)* = Photon (U(1)).

**Konforme Skalierung [K]:** k↦3k im Typ-III-Pullback-Bild.
Skalen: E_max = E_P/ξ (dichter Pol), E_H ≈ 1.4×10⁻³³ eV (dünner Pol).

Prüfskript: pruef_339_frobenius.py (6/6 Assertions).

**R102 [B]:** Frobenius-Trennung massiv/masselos — Dok. 339

---

### Dok. 340 — Neutrino-Massenhierarchie aus GF(27)* (DE+EN, 9 S.)

Eigenständiges FFGFT-Dokument (30. Aug. 2026). Beide gemessenen
Δm²-Werte aus der Zahl 11 = max({7,8,11}) = 4. Frobenius-Orbit in ℤ₁₃:

**Algebraisch bewiesen [B]:**
- Orbit₄ = 2⁻¹·Orbit₁: {7,8,11} = 7·{1,3,9} (mod 13)
- Orbit₂ ↔ Orbit₄ invers: 2⁻¹=7, 7⁻¹=2
- Δm²_sol = (|ℤ₁₃|−2)/3 · m_ν² = 11/3 · m_ν² (Abw. 0.46 %)
- Orbit₃ = {4,10,12} selbstinvers → Majorana; Σ(Orbit₃) = 26 = |GF(27)*|
- Branching-Rule ρ₄↓_A₄ = ρ₃^A₄ ⊕ ρ₁^A₄ → W-Richtung A₄-invariant
- p_vent = |A₅:A₄| / Kissing(D₄) = 5/24

**Konsistent [K]:**
- Δm²_atm = (11²−1)·m_ν² = 120·m_ν² (Abw. 1.0 %)
- Dreigeneration-Schema (normale Hierarchie):
  m₁ = 4.54 meV (D4, 4D), m₃ = 9.81 meV (E6, 6D), m₂ = 49.96 meV (E8, 8D)
- Σmᵢ = 64.3 meV < 120 meV (Planck 2018)
- cos²(2π·2/13) ≈ sin²θ₁₂ (5.1 %), cos²(2π·5/13) ≈ sin²θ₂₃ (2.8 %)
- δ_CP ≈ −π/2 mit k=10 aus Orbit₃ (Abw. 6.9°)
- m_ee = 7.1 meV < 36 meV (KamLAND-Zen)
- SICC-Venting-Formel (p=5/24, κ=12·m_ν) ≡ Standard-Oszillationsformel

**Falsifizierbare Vorhersagen:**
1. Neutrinomassen 4.54, 9.81, 49.96 meV (CMB-S4, Euclid)
2. Ratio Δm²_atm/Δm²_sol = 32.73 (gemessen: 33.20)
3. Sterile Neutrinos (Majorana): m_min = 4·m_ν = 18.2 meV (IceCube, SBN, BEST)

Prüfskript: pruef_340_neutrino_galois.py (10/10 Assertions).

**R103 [B]+[K]:** Neutrino-Massenhierarchie aus GF(27)* — Dok. 340

---

