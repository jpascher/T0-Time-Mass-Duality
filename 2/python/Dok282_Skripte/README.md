# Dok282_Skripte — Hilbertraum-Massenoperator und CP-Teilbarkeit

Die Begleitskripte zu **Dok. 282** (FFGFT im Hilbertraum — vom gemeinsamen
Loop-Objekt zum Massenoperator). Vier Ebenen: QM-Operationen, Prozess/Zeit, Masse,
Kopplungen. numpy-only.

## ffgft_mass_operator_C3.py
Der eigentliche Massenoperator auf der C³-Faser: ein **hermitescher
Z₃-Zirkulant** S = circ(t0,t1,t2). Eigenvektoren = die drei Z₃-Charaktere (die
Generationen), Spektrum von S² = die Massen. Aus zwei reinen Zahlen — r=√2
(Koide Q=2/3) und θ=2/9 (= 2/3², Kandidat-Grundbedingung, kein Fit) — reproduziert
er m_μ/m_e und m_τ/m_μ auf vier bis fünf Stellen.

## ffgft_t4_mass_operator.py
Vorwärts-Test: kann die Hilbert/Operator-Abbildung Massen *berechnen*? Vergleicht
(A) naive Kaluza-Klein-T⁴-Laplace (scheitert: O(1)-Verhältnisse, Koide≠2/3) gegen
(B) Z₃-Kanal-Kreis (Doc. 206): Q=(1+r²/2)/3 ⇒ Q=2/3 für r=√2, exakt, ohne Fit.
Ehrliches Fazit: der Winkel θ ist der einzige verbleibende Rest.

## ffgft_t4_cp_divisibility.py
CP-Teilbarkeit / Nicht-Markovianität: trennt QM-intern (Markovsch, CP-teilbar) von
historien-gekoppelt (nicht-Markovsch) über einen T⁴-Loop-Operator-Bad. BLP- und
RHP-Zeugen (für Dephasierung deckungsgleich). Das ist „die Zeit als Prozessstruktur".

## ffgft_z3_alle_sektoren.py
Alle drei Ladungssektoren als Operator-Spektrum: baut den Z₃-Zirkulanten aus den
Massen jedes Sektors und prüft Spektrum²=Massen (≈10⁻¹⁴). Zeigt, dass die treue
Übersetzung universell ist (Quarks inklusive), die reinen Zahlen aber
lepton-spezifisch sind: r=√2 nur bei Leptonen (Koide 2/3), Up r≈1,76, Down r≈1,55.

## ffgft_kopplungen_hilbertraum.py
Die Kopplungen α und G über die Hilbertraum-Abbildung. α als Eigenwert-Relation
desselben Operators: α=ξ(λ_e·λ_μ/MeV)² mit λ_e·λ_μ=√(m_e m_μ)=E₀ → 1/α=138,9
(geom.), 137,04 mit Korpus-E₀. G strukturell über ξ=2√(Gm), Skala M_T=M²=1/T̃;
SI-Umrechnung in calc-o.

## ffgft_qm_uebersetzung_erweiterung.py
Was die Masse-/Zeit-Erweiterung an den QM-Übersetzungsergebnissen (Dok. 230/231/232)
ändert. Teil A (Masse): CHSH auf der Basis mit/ohne C³-Massefaser identisch
(Δ≈4·10⁻¹⁶, Tensorfaktor). Teil B (Zeit): Kohärenz Markovsch vs. historien-gekoppelt
— Rückfluss 0→0,53, min-Choi-EW kippt negativ (CP-Teilbarkeit verletzt). Befund:
statische QM-Ergebnisse unverändert, nur dynamische bekommen die nicht-Markovsche
Korrektur.

Lauf: `python3 <skript>.py` (numpy).
