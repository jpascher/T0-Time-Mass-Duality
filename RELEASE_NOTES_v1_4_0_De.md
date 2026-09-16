# Release Notes — v1.4.0 (15. September 2026)

**DOI:** https://doi.org/10.5281/zenodo.22739112 — ersetzt v1.3.9
Laufende Korrekturen: **[2/pdf/190_T0_Korrekturen_De.pdf](2/pdf/190_T0_Korrekturen_De.pdf)**
Änderungsprotokoll: **[001_FFGFT_Changelog_De.md](001_FFGFT_Changelog_De.md)**

**FFGFT — Fundamentale Fraktale Geometrische Feldtheorie** zeigt: Alle Konstanten des
Standardmodells folgen aus einem einzigen dimensionslosen Parameter **ξ = 4/30000**
auf einem kompakten 4D-Torus T⁴/ℤ₃. Die Grundrelation lautet **T̃·m = 1** — intrinsische
Zeit und Masse sind invers gekoppelt.

**Autor:** Johann Pascher · ORCID 0009-0000-6518-4064

---

## Überblick

Diese Version bringt das neue Narrativ-Buch *Quantenmechanik ist deterministisch*
(De/En, 107/105 S.) mit vollständigen LaTeX-Quellen, 10 Python-Prüfskripten und
einer deterministischen PC-Implementierung aller Quanten-Logikbausteine. Das Buch
ist auf Amazon Kindle und als freies PDF auf Zenodo und GitHub verfügbar.
Keine algebraischen Ergebnisse aus v1.3.9 wurden geändert. Kein Registereintrag erforderlich.

---

## Neues Buch: Quantenmechanik ist deterministisch

### *Quantenmechanik ist deterministisch / Quantum Mechanics is Deterministic*
*(De/En, 107/105 S., 4 Teile, 15 Kapitel, 3 Anhänge)*

**DOI:** https://doi.org/10.5281/zenodo.22739112
**GitHub-Quellen:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/Sources/qmb-ch/
**Prüfskripte:** https://github.com/jpascher/T0-Time-Mass-Duality/tree/main/2/python/QMB_Skripte/

Ein Narrativ-Buch zur geometrischen Lesart der Quantenmechanik durch die FFGFT.
Geschrieben für Leserinnen und Leser mit Grundkenntnissen in linearer Algebra und
Quantenmechanik; kein Vorwissen in Differentialgeometrie erforderlich.

**Struktur:**

| Teil | Kapitel | Inhalt |
|------|---------|--------|
| I — Grundlagen | 1–3 | Träger T⁴/ℤ₃, Zustandsraum, Zeitoperator, Verschränkung als Torus-Eigenschaft |
| II — Bell | 4–7 | Bells Theorem, CHSH, No-Go-Theoreme (KS, PBR, Hardy, GHZ), CHSH-Auflösungsboden |
| III — Quantenrechner | 8–12 | Qubit-Formalismus, Algorithmen, Spin/QD, Hardware, Grenzen |
| IV — Zustandsraum | 13–15 | FFGFT↔Hilbertraum-Brücke, D₄-Gitter, Spektraltheorie, Zeit und Superposition |

**Anhänge:** Formelzeichenverzeichnis (5 Gruppen, alle Statusmarker) · Quellenverzeichnis
(Dok. 022–365 + 20 externe Referenzen mit Anmerkungen) · Hinweis zur KI-Assistenz.

---

## Wichtige neue Ergebnisse im Buch

### Deterministischer Einzeldurchlauf [K]
Die Zustandsbrücke (z,r,θ)↔(α,β) ist bijektiv. Alle Quanten-Logikbausteine —
Gatter, Deutsch, Grover, Bell-Zustände, Periodenfindung, Faktorextraktion — sind
auf einem normalen PC in einem einzigen deterministischen Durchlauf vollständig
realisierbar. Kein Quantensubstrat, keine Wiederholungen, keine Shot-Mittelung.

Verifiziert durch `pruef_logikbausteine.py`: H, X, Z, CNOT, X_frak (K_frak-Abweichung
1,333 %), Deutsch (konstant/balanciert, je ein Lauf), Grover (n=3..10, P>0,94),
Bell-Zustand (P(00)=P(11)=0,5 exakt), Periodenfindung N=15..323 — alle korrekt,
alle deterministisch.

IBM-Kingston-Vergleich (28. Mai 2026): Bell-Fidelität 0,9876±0,0028 über
50×2048 Shots. PC-Ergebnis: identisch in einem einzigen Lauf.

### PC schneller als QC — Ausnahme QFT in Superposition [K]
Modulare Exponentiation ist auf einem Quantenschaltkreis nachweislich teurer als
auf dem PC (Reversibilität, Uncomputation, Toffoli-Gatter). Der einzige echte
Quantenvorteil liegt in der QFT, die die Periode über alle x gleichzeitig in
Superposition ausliest: O((log N)³) statt O(N). Dieser Vorteil existiert
theoretisch — er ist Stand 2026 technisch nicht RSA-relevant (RSA-2048 erfordert
4,1×10⁶ physikalische Qubits, 8,6×10⁹ Gatter). Gottesman-Knill: Verschränkung
allein trägt den Vorteil nicht.

### Mathematik-Analogie für Instantanität [K]
In der Standardmathematik gilt 2+2=4 instantan für alle Stellen des Ausdrucks —
niemand leitet daraus eine physikalische Fernwirkung ab. Die Wellenfunktion ist eine
strukturelle Beschreibung, kein Ausbreitungsprozess. In der FFGFT gilt dasselbe:
T̃·m=1 ist eine lokale Zwangsbedingung am selben Raumpunkt, kein Signal zwischen
entfernten Punkten. Das ist der präzise Grund, warum die scheinbare Instantanität
in der QM kein Kausalitätsproblem ist.

### Bijektive Zustandsbrücke [K]
α = √((1+z)/2)·e^{iθ/2}, β = √((1-z)/2)·e^{-iθ/2}.
Invers: z = |α|²−|β|², r = 2|αβ|, θ = arg(α)−arg(β).
Verifiziert für 8 Testpunkte inkl. Pole, Äquatorzustände, allgemeine Punkte.
σ_z-Gatter: θ→θ−π (nicht +π). Hadamard: H²=I verifiziert. [K]

---

## Prüfskripte (neu): QMB_Skripte/

10 Python-Skripte, nur numpy, keine externen Abhängigkeiten:

| Skript | Kapitel | Tests | Status |
|--------|---------|-------|--------|
| pruef_hilbert_bridge.py | 13 | Bijektivität, Norm, σ_z, Hadamard | ✅ alle [K] |
| pruef_kfrak_gatter.py | 8 | K_frak=74/75, Δ=4/3%, Infidelität, NISQ-Band | ✅ alle [K] |
| pruef_qd_rbulk.py | 10 | N(22nm)=8,00, Stufenleiter, E/kBT-Tabelle | ✅ alle [K] |
| pruef_dekohaerenz_xi.py | 10 | 9 GO Spanne = 2·log₁₀(1/ξ_Higgs), T₂≤2T₁ | ✅ alle [K] |
| pruef_kausalitaet.py | 3 | Δt=r/c, t_P≪Attosekunde, retardierte Greensche Funktion | ✅ alle [K] |
| pruef_xi_hierarchie.py | 8 | Zeeman vs kBT, Photonenenergien, N_max=E/kBT | ✅ alle [K] |
| pruef_chsh_signal.py | 12 | Δ_CHSH=ξ/2π≈2×10⁻⁵, Tsirelson, NISQ-Verhältnis | ✅ alle [K/S] |
| pruef_xi_galois.py | 1 | ξ=(4/3)/10⁴, K_frak=74/75, Koide Q=3/2, Aut(D₄)=1152 | ✅ alle [K/E] |
| pruef_pbit_barrier.py | 11 | Arrhenius τ=τ₀·exp(U/kBT), p-Bit-Fenster bei 22 nm | ✅ alle [K] |
| pruef_logikbausteine.py | 8/9 | Gatter, Deutsch, Grover, Bell, Periodenfindung | ✅ alle [K] |

---

## Buchspezifische Klarstellungen (keine Korrekturen an bestehenden Dokumenten)

**CHSH-Auflösungsboden vs. kumulative Formel:**
Die elementare FFGFT-Abweichung Δ_CHSH = ξ/(2π) ≈ 2×10⁻⁵ pro Messung (Kap. 12)
und die kumulative Formel für N=73 Qubits (Dok. 022, Dok. 147) sind nicht direkt
vergleichbar und dürfen nicht gleichgesetzt werden (Kap. 7).

**Geltungsbereich der Weyl-Obstruktion:**
Die Weyl-Obstruktion (N(T)∼T ln T) gilt für unendliche arithmetische Spektren, nicht
für das Finden einer einzelnen Periode für ein konkretes N. Shors Algorithmus ist eine
endliche Aufgabe, die 2n+3 Qubits erfordert; die Obstruktion trifft ihn nicht
(Dok. 176, [K]).

**Einordnung des Heron-Tests:**
IBM-Kingston Bell-Fidelität 0,9876±0,0028 ist konsistent mit FFGFT und Standard-QM —
es ist eine Konsistenzprüfung, kein Nachweis. Die ξ-Abweichung liegt 10³–10⁴-fach
unter NISQ-Rauschen. Unterscheidbarkeit erfordert N∼10⁹ Messpaare. [K]

**Frühere 40×-Determinismus-Meldung zurückgezogen:**
Eine frühere Auswertung über 3 Läufe hatte fälschlicherweise 40×-Determinismus
gegenüber der QM gemeldet. Das war ein Stichproben-Artefakt. Die korrekte Aussage:
Ergebnisse sind identisch innerhalb der Messgenauigkeit. [K]

---

## Amazon Kindle

Das Buch ist als eBook, Taschenbuch und Hardcover in allen Märkten verfügbar:
- *Quantenmechanik ist deterministisch* (De, 107 S.)
- *Quantum Mechanics is Deterministic* (En, 105 S.)

---

## Korrekturen

Keine. Das neue Buch ist ein neues Dokument; kein bestehendes Dokument erforderte
eine Korrektur. Kein Registereintrag (R-Einträge gelten nur bei Korrekturen
an älteren Dokumenten).

---

## Offene Brücken (unverändert seit v1.3.9)

| Brücke | Status |
|--------|--------|
| CKM/PMNS-Winkelwerte (numerisch) | [S] (Dok. 348 Satz D) |
| HRV-Galois-Test: positives Ergebnis | [S] erfordert kontrollierte Atmung ≥13 min, n≥5 |
| Generationszuordnung (Reihenfolge) | [S] (Dok. 346) |
| m_Pl und α_em(M_Z) aus ξ | [S] |
| Quark-/Hadron-Sektor | offen (Dok. 318, R76) |
| CMB-Peaks {1,6,14,26}; \|n\|²=30 | offen (P29/P31) |
| Δm²₃₂ Mischterm F₅–F₇ | [S] |
| Torus T⁴/ℤ₃ als GALG-Polynom | offen |

## Einstieg für neue Leser
Dok. 205 „FFGFT in einfacher Sprache" (De/En, 13–14 S.) bleibt der empfohlene
Einstiegspunkt für die Physik. *Quantenmechanik ist deterministisch* ist der
empfohlene Einstiegspunkt für die Quantenmechanik- und Quantenrechner-Perspektive.

## Was sich nicht geändert hat
ξ, T̃·m=1 und alle algebraischen Ergebnisse aus v1.3.9 sind unverändert.
Alle Herleitungsketten aus v1.3.6 sind unverändert.
