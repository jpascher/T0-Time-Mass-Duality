# Dok283_Skripte — FFGFT ↔ HLV: die Brücke und die Gabelung

Begleitskripte zu **Dok. 283**. Jede testbare Aussage des Dokuments ist durch ein
Skript abgedeckt; wo eine Aussage als Tabelle darstellbar ist, schreibt das Skript
eine CSV. numpy-only (Skript für den χ-Kern nutzt scipy, wenn vorhanden).

## Aussage → Skript-Karte

| Dokument-Aussage | Skript | CSV |
|---|---|---|
| §3 Z₃-Zirkulant auf der C₃-Achse (Brücke) | ffgft_hlv_c3_bridge_probe.py (Check 1); ffgft_283_bridge_fork_tables.py | bridge_gram_c3.csv |
| §5 nur 1/√5, kein τ erreicht √2, √2 nur 3-zählig | Probe (Checks 2–4); bridge_fork_tables | inner_products_6x6.csv, r_tau_sweep.csv, fork_summary.csv |
| §6 geschützt vs. generisch (√2 nur unprotected) | Probe (Check 5); bridge_fork_tables | protected_vs_generic.csv |
| §7 rationaler Approximant → 2/√5, 7/15 (fairer Vergleich) | Probe (Check 6); bridge_fork_tables | approximant_convergence.csv |
| §8/Kasten χ-Gedächtnis = nicht eindeutig (Run M1, generischer Biexponential) | ffgft_283_memory_kernel_baselines.py | memory_kernel_baselines.csv |
| Kasten Raum-Ebene = Stufe-0 (Connection-Laplace generisch) | ffgft_283_connection_laplace_stufe0.py | connection_laplace_carriers.csv |
| §9 nur Leptonen 3-zählig, Hadronen entartet, kein 5-Zähligkeits-Sektor, ν < 2/3, Verhältnis ~12 | ffgft_283_sector_koide.py | sector_koide.csv |
| §9 5-zählig nicht-kristallographisch, 3-/6-zählig hexagonal, 2cos72°=1/φ | ffgft_283_crystallographic_restriction.py | crystallographic_restriction.csv |

(Die Masse-/Zeit-Seite der χ-Brücke selbst — FFGFTs nicht-Markovscher Kern — liegt in
Dok282_Skripte: ffgft_t4_cp_divisibility.py, ffgft_qm_uebersetzung_erweiterung.py.)

## Skripte

**ffgft_hlv_c3_bridge_probe.py** — der Kern-Beweis (sechs Checks, deterministisch).
HLV = ikosaedrischer 6D→3D-Cut-and-Project (τ=φ parallel, −1/φ senkrecht); die
C₃-Achse (x,y,z)→(z,x,y) zerlegt die sechs Spalten in zwei 3-Zyklen. Befund:
genuine Z₃-Zirkulant-Brücke (Check 1) + fundamentale 5-gegen-3-Gabelung
(Checks 2–6); übersteht die Rekompaktifizierung (rationaler Approximant).

**ffgft_283_bridge_fork_tables.py** — schreibt §3/§5/§6/§7 als CSV-Tabellen
(C₃-Gram, 6×6-Skalarprodukte, r(τ)-Sweep, Gabelungs-Summary, geschützt-vs-generisch
mit den 150 Generik-Treffern, Approximanten-Konvergenz).

**ffgft_283_sector_koide.py** — Koide Q und Zirkulant-r pro Ladungssektor.
Belegt §9: nur geladene Leptonen am 3-zähligen Punkt (Q=2/3, r=√2); Hadronen fast
entartet (Q≈1/3); Up/Down-Quarks verfehlen √2; Neutrinos max. Q≈0.584 < 2/3; kein
Sektor am 5-zähligen Punkt 7/15; für 7/15 bräuchte ρ/ω/φ ein m₃≈9 GeV (Verhältnis ~12).

**ffgft_283_crystallographic_restriction.py** — die kristallographische Restriktion
(n-zählig periodisch ⇔ 2cos(2π/n) ∈ ℤ). Belegt §9: 5-zählig nicht-kristallographisch
(erzwingt Dekompaktifizierung), 3-/6-zählig kristallographisch (Hexagonalgitter);
2cos72°=(√5−1)/2=1/φ bindet das Pentagonale an den Goldenen Schnitt.

**ffgft_283_memory_kernel_baselines.py** — der χ-Gedächtniskern gegen vordeklarierte
Baselines (Einzel-Exp = schwache Null, Biexponential = generisch, Power-Law,
Stretched). Belegt §8/Kasten: der strukturierte Kern schlägt die schwache Null, wird
aber vom generischen Biexponential reproduziert (Residuum ~1e-3) → strukturelle
Verwandtschaft, keine Eindeutigkeit (Run M1).

**ffgft_283_connection_laplace_stufe0.py** — der Connection-Laplace-Zeuge auf drei
unverwandten Carriern (kubisch, zufällig-regulär, Ring). Belegt den Kasten: blind für
reine Eichung (W~1e-15), detektiert nicht-exakten Fluss (W>0), auf jedem Carrier
gleich → generisch → Stufe-0, keine Brücke.

**ffgft_283_plots.py** — erzeugt aus denselben Zahlen acht Ergebnis-Figuren
(A r(τ)-Deckel, B Sektor-Koide, C kristallographische Restriktion, D χ-Kern gegen
Baselines, E Connection-Laplace Stufe-0, F 6×6-Skalarprodukte, G geschützt-vs-generisch,
H Approximanten-Konvergenz) plus eine Übersichtsfigur 283_overview.png in figures/.

**ffgft_283_memory_harness_shared.py** — die gemeinsame HLV↔FFGFT-Memory-Harness nach
Krügers vorab-registriertem Null-Modell-Protokoll (Zenodo 20514548), mit ZWEI
Beobachtungsgrößen, weil die beiden Kerne strukturell verschieden sind (aus den Dokumenten
gelesen, nicht erfunden): Krügers Kern ist ein positiver abklingender Exponential-Mix
(überdämpft); FFGFTs Kern ist die FT der diskreten Spektraldichte Σ_k g_k²δ(ω−ω_k) — sechs
dominante Moden des T⁴-Connection-Laplace (L=3, Fluss a=½π·(1+μ)), ω_k=√λ_k, g_k²∝Entartung,
eine freie Kopplung — also OSZILLIEREND (Revivals), kein abklingender Mix.
Part 1 (Krügers überdämpfte Vortizität, M₀/M₁/M_HLV/M₂): M_HLV schlägt M₀/M₁, liegt
gleichauf mit M₂, per BIC bevorzugt → Nicht-Identifizierbarkeit (Run M1). Part 2
(Kohärenz c(t)=e^{−Γ(t)}, FFGFTs Heimat-Sektor): der FFGFT-Diskretspektrum-Kern erzeugt
BLP-Rückfluss 5.125 (exakt Dok-282-Wert); generische abklingende Kerne sind monoton
(Rückfluss 0) und können die Revivals nicht reproduzieren → hier hat der strukturierte
Kern eine Signatur, die der generische Null verfehlt. Der überdämpfte Sektor ist
nicht-identifizierbar, der Kohärenz-Sektor diskriminiert. CSVs: memory_harness_models/
_bootstrap/_crossflow/_ffgft_coherence.csv, ffgft_kernel_constants.csv; Plot
figures/memory_harness.png. (Part-1-Daten sind modellgeneriert: reproduziert Protokoll +
qualitatives Tabelle-1-Ergebnis, nicht Krügers exakte Zahlen.)
