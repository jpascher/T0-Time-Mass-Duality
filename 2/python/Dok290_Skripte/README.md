# Dok 290 — Skripte (Folgen für die Informationsfrage)

Reproduzierbare numpy-only-Skripte zu Dok. 290, Seed 20780458. `python3 <datei>.py`.

- `phase_traegt_struktur.py` — Oppenheim/Lim (1981): tauscht man Betrag und Phase
  zweier Muster über Kreuz, folgt die Rekonstruktion dem Phasen-Spender;
  Phase-only(A) korreliert mit A (+0,53), Magnitude-only(A) nicht (−0,24). Das
  Phasenspektrum trägt die Struktur → eine Masse-Energie-(Betrags-)Buchhaltung
  erfasst den strukturärmeren Kanal.
- `masse_information_phasenblind.py` — M = U·diag(m)·U†: jede Funktion der
  Eigenwerte (Σm, Koide Q) ist gegenüber der Mischung U invariant; bei festen
  Massen bleiben Σm=5 und Q=0,372 über drei Mischungen gleich, während
  ‖M_offdiag‖ (1,42…1,78) variiert → die Mischung/Phase ist ein zweiter Kanal,
  unsichtbar für die Masse-Information. Entarteter Grenzfall M=m·1 (Neutrino-
  Allpass): Mischung verschwindet aus M, Phase sitzt in der Propagations-/
  Holonomie-Phase.
- `photon_paket_count_energie.py` — ist ein Photon das kleinste Paket? Nur pro
  Mode; lokalisiertes Photon = Wellenpaket (Δx·Δk≥½). Trennt Informations-ZAHL
  (besetzt/leer = 1 Bit, frequenz-unabhängig), Bit-ENERGIE (E=ħc/L) und KAPAZITÄT
  (Shannon C=B·log₂(1+SNR), B∝f). Energie und Kapazität skalieren mit der Frequenz
  (Radio→Gamma ~15 Größenordnungen), die Zahl pro Quant bleibt 1. ξ-Decke:
  n_max~1/ξ≈7500 (243/009) deckelt |W| → Kapazität sättigt an der ξ-Skala.
  „Höhere Frequenz → mehr Information" = die Kapazitäts-(Modenzahl-)Achse, orthogonal
  zur Betrag/Phase-Spaltung innerhalb der Mode (I/Q bzw. QAM). Teil (5): absolute
  Informationsmenge I1 = log2(1/ξ) ≈ 12,87 Bit pro Freiheitsgrad (dimensionslos,
  ξ-verankert; nicht „magisch" — der Gehalt ist Endlichkeit + ξ-Verankerung).

- `fenster_zyklen_linienbreite.py` — Fensterwirkung: zeitbegrenztes Paket behält
  den definiten Träger f0; N=f·Δt. Festes Fenster → N∝f; feste Zyklenzahl →
  Δf/f=1/N frequenz-UNABHÄNGIG (Radio=optisch). Natürliche Linienbreite aus
  Lebensdauer τ: Q=ω0·τ=2πN (τ=10 ns, f0=5·10¹⁴ Hz → N=5·10⁶, Δf≈16 MHz). Der
  dimensionslose Zähl-/Zyklenwert ist absolut, dt/df/E sind dimensionales Beiwerk.

- `minimalphase_allpass.py` — Präzisierung von „Betrag legt Phase nicht fest": gilt
  nur BIS AUF einen Allpass-Faktor. H=H_min·H_ap; für den minimalphasigen Anteil legt
  der Betrag die Phase fest (Bode/Hilbert, arg=H{log|H|}), der Allpass (|H_ap|=1) ist
  frei. Verifiziert: aus dem Betrag rekonstruierte Phase == arg(H_min) (~1e-15),
  Restphase == arg(Allpass) (~1e-15). Dort sitzt die θ-Holonomie (Min-Phase×Allpass,
  Dok 288).

- `absolut_relational.py` — löst die Spannung absolut/relational: andere Achsen.
  Eine Windung ist relational (Schleifenintegral, halbe Schleife=1, lokal nicht
  ablesbar) UND absolut (eichinvariant unter einwertiger Umphasung, ganzzahlig).
  Die absolute Zahl log2(1/ξ) zählt genau diese relationalen Windungssektoren
  (~15000 bis n_max~1/ξ, log2≈13,9 Bit). Absolutheit im Boden (ξ), Relationalität
  in den Freiheitsgraden — kein Widerspruch.

- `quant_bit_modeninfo.py` — (1) weder Periodenzahl N noch Fensterlänge Δt ist
  intrinsisch: N=f·Δt vom Prozess gesetzt (monochromatisch=∞; spontan: f0 UND τ
  gekoppelt N=Q/2π; technisch: eine Größe fest); intrinsisch die dimensionslose N,
  Spannweite ~2 … 5e6. (2) „1 Quant = 1 Bit" ist KEINE Gleichung: ein Quant ist ein
  ZÄHLWERT (eine Anregung), sein Informationsgehalt ist log2(M) Bit (M unterscheidbare
  Moden), variabel, per dof gedeckelt bei I1=log2(1/ξ)≈12,87 Bit. „1 Quant = 1 Bit"
  gilt nur für M=2. Zählwert (Quant) und Bitgehalt sind verschiedene Achsen — gezeigt:
  1 Quant in 2^13 Moden = 13 Bit = 13 binäre Quanten (gleiche Bit, andere Quantenzahl).

- `bit_statisch_dynamisch.py` — statische vs. dynamische Definition des Bits.
  STATISCH: log2(M), E0=ħc/L (Struktur, Betragsseite). DYNAMISCH-KINEMATISCH
  (reversibel): T~=ħ/E0=1/m0, Rate 1/T~, E0·T~=ħ ⟺ T~·m=1; Margolus-Levitin
  τ≥πħ/2E — Energie SETZT die Uhr, kein Verlust, Kosten=Zeit; Rate=Kapazität
  (Bit/s, §5). DYNAMISCH-THERMODYNAMISCH (irreversibel, Landauer): Entropie kB·ln2,
  Löschwärme kB·T·ln2 — hängt an T nicht E0, Kosten=Wärme, in FFGFT emergent
  (T^4 unitär-reversibel). Brücke: dimensionsloser Bit gekleidet ×ħ,c→Energie/Zeit,
  ×kB→Entropie/Wärme; ħ,c,kB=SI-Buchhaltung. Energie 2 Rollen: Uhr vs. Wärme.

- `buchhaltung_si_natuerlich.py` — „Buchhaltung" heißt notwendig, nicht entbehrlich.
  Dimensionslos (log2 M, ln2) ist primär und einheitensystem-invariant; SI trennt K,J,s,
  also ist kB die unverzichtbare K→J-Umrechnung sobald thermodynamisch in SI gerechnet
  wird (sonst Löschwärme in Kelvin statt Joule), wie ħ,c für E0=ħc/L. Natürliche
  Einheiten: reine Zahlen; SI: Einheitenwände, kB,ħ,c der Mörtel. Ontologisch sekundär,
  operativ unverzichtbar.

- `bit_in_si.py` — das Bit konkret in SI-Zahlen, verankert an E0=√(me·mμ)=7,348 MeV
  (über α=ξ·E0² an Feinstruktur gekoppelt; √(α/ξ)=7,398 MeV, +0,68% — keine exakte
  Gleichheit). E0=1,177e-12 J, L0=ħc/E0=26,85 fm, m0=1,310e-29 kg, T~=ħ/E0=8,958e-23 s,
  Rate 1,116e22/s; E0·T~=ħ (T~·m=1). Landauer 300K=2,87e-21 J=17,9 meV, Q/E0=2,4e-9 -> E0/Q=4e8 = gut acht Groessenordnungen (NICHT neun).
  Zwei „Energien" eines Bits, ~9 Größenordnungen: was es IST (7,3 MeV) vs. was sein
  Löschen kostet (18 meV).

- `bit_temperatur.py` — die Temperaturskala des Bits. T0=E0/kB=8,53e10 K; vier
  Kleidungen derselben Energie m0·c²=E0=kB·T0=ħ/T~ (/c²→Masse, /ħ→Zeit, /kB→Temp).
  T0 = Temperatur-SKALA (kB·T=E0-Schwelle, darüber „schmilzt" das Bit), nicht was ein
  Bit „hat". Brücke: thermische Zeit ħ/(kB·T0) = Dual-Zeit T~ (KMS/Connes-Rovelli),
  Diff 1e-38 s. Kreisschluss Landauer: Q/E0=(T/T0)·ln2 — bei 300K =2,4e-9 (8,5 Dekaden
  unter T0), bei T=T0 =ln2=0,69. Statisch (E0,T0) und thermodyn. (kB·T·ln2) über T/T0
  verbunden, kein Sprung.

- `bit_temperatur_leiter.py` — die Leiter der Temperaturen. (1) E0 ist eine SPROSSE,
  nicht der Boden: der geometrische Boden ist die Sub-Planck-Länge L0=ξ·ℓ_P≈2,2·10⁻³⁹ m
  (Dok 163), in allen Kleidungen ausgedrückt (Länge/Zeit/Frequenz/Energie/Temperatur/
  Masse, alle 1/ξ=7500·Planck); „Boden\" = feinste Auflösung / UV-Maximum, nicht kleinste
  Energie. E0 (MeV) liegt ~25 Dekaden gröber; log₂(1/ξ)=log₂(7500)≈12,87 = I1 (die
  √2-Zwischenschritte pro Fraktal-Hauptstufe sind die Informationsdecke). (2) Landauer:
  Q=kB·T·ln2 hängt am BAD, nicht am Bit — drei Bäder (Raumtemp 18 meV / CMB 0,16 meV /
  T0→0,69 E0) mit Q, Q/E0, T/T0; invariant nur Q/E0=(T/T0)·ln2. Problematik: eine Leiter
  DEFINITER Temperaturen (Sprosse T0=8,5·10¹⁰ K, Boden T_max=1,1·10³⁶ K, 25 Dekaden),
  aber keine ist die Landauer-Temperatur; T_CMB eingesetzt ergibt den UIFT-Parameter
  ξ_UIFT≈3·10⁻¹⁰ — eine andere, kosmologische Größe (Kategorienunterschied).

## Befund
Die Magnitude/Phase-Zerlegung verschiebt die Informationsfrage von „ist
Information fundamental?" zu „welcher Kanal?": Vopson/Landauer = Betragskanal
(von FFGFT aus T⁴-Geometrie hergeleitet, Dok 255/257), die Phase = relationale
Information (Holonomie, θ), darstellungs-relativer Bit-Count (Dok 243/287), treue
Beschreibung quanten- statt bit-basiert. Ehrlich: strukturelle Schärfung, keine
neue Herleitung (P35); Neutrino-Grenze ruht auf spekulativer Entartung (Dok 007).

---
EN: numpy-only scripts for Doc. 290. The Oppenheim/Lim phase-carries-structure
result, and the demonstration that mass-information functionals (Σm, Koide Q) are
invariant under the mixing/phase channel — so Vopson/Landauer capture only the
magnitude channel, the phase is a second, independent (relational) channel.
Structural sharpening, not a new derivation (P35).
