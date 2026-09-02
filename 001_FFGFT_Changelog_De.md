# FFGFT Changelog — laufend ab v1.3.4

**Grundlage:** Dok. 190 (Korrekturregister)  
**Archiv bis v1.3.3:** [`000_FFGFT_Changelog_De.md`](000_FFGFT_Changelog_De.md)

Neue Einträge werden hier oben eingefügt (neueste zuerst).

---

## 1. September 2026 — Dok. 341, R105, Galois-Bündel v2

### Dok. 341 — GF(27) in GALG: algebraische Brücke FFGFT↔GALG (DE+EN)

Ergebnis des algebraischen Vergleichs mit Doug Matzkes GALG-Framework
(Austausch IPI, August 2026). Drei algebraisch bewiesene Sätze [B]:

**Satz A:** G(3) enthält keine GF(27)-Struktur weil 13 ∤ |GF(81)*| = 80.
Dougs „Attempted 6561 with 0 found" ist strukturell erzwungen, kein Suchfehler.

**Satz B:** In G(6) existieren Elemente der Ordnung 26 = |GF(27)*|.
Konstruktion via Begleitmatrix des irreduziblen Polynoms f(x)=x³+2x+1 über GF(3).
Konkretes 5-Blade-Element in GALG-Notation für direkte Verifikation angegeben.
Ordnung-26-Elemente treten bei ≥5 Blades auf (~18–37% der invertierbaren Elemente
mit ≥6 Blades).

**Satz C:** GF(27) bettet als Teilkörper in M_n(GF(9)) genau dann ein wenn 3|n.
G(3)→n=2 und G(6)→n=8 tragen daher kein GF(27) als Teilkörper.

**Vakuumstruktur:** GALG-Witt-Paar-Vakua unter ℤ₃ stimmen exakt mit der
FFGFT-Frobenius-Trennung (Dok. 339) überein: gerade Vakua [0,2,4] = ℤ₃-Fixpunkte,
ungerade [1,3,5] = ℤ₃-Dreier-Orbit; Bilaterale = Gluon-Sektorwechsler [B].

Prüfskripte:
- `pruef_341_gf27_in_galg.py` (6/6 [B] Assertionen)
- `pruef_341_vakuum_witt_z3.py` (7/7 [B] Assertionen)
- `pruef_342_vakuum_witt_z3.py` (7/7 [B] Assertionen, unabhängige Verifikation)

### R105 — Nachträgliche Marker-Zertifizierung (1. Sept. 2026)

Neun Dokumente vor dem Marker-System (A010) als Kettenglieder des Galois-Programms
nachträglich zertifiziert:

- **Dok. 006** Teilchenmassen, Wicklungszahlen r_i, p_i → **[K]**
- **Dok. 011** Feinstruktur α, E₀, Grundrelationen → **[K]**
- **Dok. 070** K_frak kürzt sich in Verhältnissen, Absolutwerte tragen Korrektur → **[B]**
- **Dok. 182** Maximale Universum-Skala aus ξ (Schwarzschild + Hubble) → **[K]**
- **Dok. 231** Hilbertraum-Erweiterung, L²-Struktur → **[B]**
- **Dok. 257** Informationseinheit, Bit-Energie-Skala → **[K]**
- **Dok. 285** FFGFT-HLV-Dimensionsbrücke → **[K]**
- **Dok. 306** Native Zeit-Energie-Reziprozität aus T̃·m=1 → **[K]**
- **Dok. 307** Zeit im Zustandsraum → **[K]**

Anlass: Prüfung der Ableitungskette für Galois-Kern (Dok. 336, 338, 339, 340, 341)
gemäß R103-Kettenschlussbedingung. Prüfskripte aus Mail-Anhängen an Doug Matzke
(28. Aug. 2026) ins Repo nachgepusht:
`Dok320_321_322_Skripte/pruef_324–329.py` und `Dok338_Skripte/pruef_330–332.py`.

### Galois-Bündel v2

Vollständig verifiziertes Bündel aller Galois-Dokumente und Prüfskripte:
- 21 PDFs (Galois-Kern + Abhängigkeitskette, En)
- 23 Prüfskripte — alle bestanden
- Bundle-SHA-256: `a946e9871ea5a38808b54b83dfcc8b250a1f75a1aba2d393cdcfef0219af0354`

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

**R93 [B]:** S_BH(M_coll) = 2π nat = n_thresh(Matzke) in Bit  
**R94 [B]:** I_Sektor/I_thermisch = log₂3 für alle M  
**R95:** Vier Formulierungspräzisierungen nach externem Review (Krüger)

### Dok. 332 — Zwei Wege vom Diskreten zum Kontinuum (DE+EN, je ~16 S.)

Allgemeiner Vergleichsaufsatz (kein originärer FFGFT-Beweistext).
Referiert Krügers Preprint (Zenodo DOI 10.5281/zenodo.22105698).

**R96 [B]/[K]:** Per_{Rm}(ℝ_t) mit Pro-Periode-Norm ≅ L²(S¹_m) [B].

### Dok. 333 — K_frak, Ausrollen und die T̃·m-Dualität (DE+EN, je 5 S.)

**R98 [B]:** Zwei Ausroll-Bedeutungen + Rekursionsbindung

### Dok. 334 — Superposition ohne Zeit (DE+EN, 6/5 S.)

**R99 [B]/[K]:** Superposition ohne Zeit — Dok. 334

---

### R100 — ξ als Galois-Zahl [K] (28. August 2026)

**Kernidentität** (pruef_331):
$(r_\mu/r_e)^2/\xi = |\text{GF}(9)^*|^2\cdot5^2\cdot|\text{GF}(27)| = 43200$

### R101 — 1/α = 3700/27 aus Galois [K] (28. August 2026)

$1/\alpha = 3700/27 = 137{,}037$ (Abw. 7,6 ppm). Kein ξ, kein $v$, kein $m_e$.

### Dok. 339 — Frobenius-Trennung massiv/masselos in GF(27)* (DE+EN, 10 S.)

**R102 [B]:** Frobenius-Trennung massiv/masselos — Dok. 339

### Dok. 340 — Neutrino-Massenhierarchie aus GF(27)* (DE+EN, 9 S.)

**R103 [B]+[K]:** Neutrino-Massenhierarchie aus GF(27)* — Dok. 340

---
