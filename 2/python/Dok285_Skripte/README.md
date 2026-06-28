# Dim-Bridge: rechnerischer Test der 3-vs-6-Frage (FFGFT vs HLV)

Frage (Johann): Beide Modelle reduzieren auf 3+1 — bilden die 3 (FFGFT) und die 6 (HLV)
dann nur dasselbe ab, also bloss eine mathematische Transformation? Und: Fuenfecke
brauchen die 6, Dreiecke sind fundamentaler, dafuer reichen die 3.

numpy only, feste Werte, kein Zufall.

| # | Skript | Aussage | Ergebnis |
|---|--------|---------|----------|
| 1 | dim_bridge_1_doubling.py | "6 ist die Verdopplung der 3" | 6 = 3 (+) 3' : die ikosaedrische 6D-Darstellung zerfaellt in zwei 3D-Irreps von A5, die sich exakt durch phi <-> 1-phi unterscheiden. 6D-Charakter INTEGER (1), jeder 3D-Block irrational (phi). |
| 2 | dim_bridge_2_crystallographic.py | Dreiecke fundamentaler, 3 genuegen; Fuenfecke brauchen 6 | Crystallographic restriction 2cos(2pi/n) in Z nur fuer n in {1,2,3,4,6}. 3-fold = -1 (kristallographisch, lebt in 3D). 5-fold = 1/phi (nicht-kristallographisch -> 6D-Einbettung noetig). |
| 3 | dim_bridge_3_same_ambient_fork.py | "nur mathematische Transformationen?" | Ambient 3+1 ist geteilt (transformierbar). Aber: cut-and-project r(tau)=2tau/(1+tau^2) <= 1; HLV-Wert 2/sqrt5 wird bei tau=phi erreicht, FFGFTs sqrt2 NIE -> die Strukturen sind NICHT ineinander transformierbar. |

## Gesamt-Verdikt

- Die 3 und die 6 bilden **dasselbe ambiente 3+1** ab (R^3 x R_t) — auf der Ebene der
  blossen Koordinaten-Mannigfaltigkeit ist es eine verlustfreie Transformation.
- Sie bilden **nicht dieselbe Struktur** ab: HLV traegt eine 5-zaehlige (ikosaedrische,
  2/sqrt5, bei tau=phi) Struktur, FFGFT eine 3-zaehlige (Z3, Koide 2/3, sqrt2). sqrt2 liegt
  ausserhalb des gesamten cut-and-project-Bereichs -> KEINE Transformation verbindet sie.
- Die 6 ist die Verdopplung der 3 (3 (+) 3'), und die Verdopplung wird **nur** gebraucht,
  weil die 5-Zaehlichkeit nicht-kristallographisch ist. Die 3-Zaehlichkeit (Dreieck) ist
  kristallographisch und damit der **minimale, fundamentalere** Traeger.

Kurz: "nur mathematische Transformationen" stimmt fuer die Einbettung, nicht fuer die
Physik. Der Fork (Dok 283) ist strukturell, kein Koordinaten-Artefakt.

Hinweis: das sqrt2 in Zeile n=8 der Tabelle (Skript 2) ist 2cos(45 Grad), die OKTAGONALE
Rotation — ein Zufall der Zahlenwerte, NICHT FFGFTs sqrt2. FFGFTs sqrt2 ist das
Koide-/Z3-Zirkulant-Verhaeltnis innerhalb der (kristallographischen) 3-Zaehligkeit, keine
Rotationsordnung.

## Korrektur (19. Juni 2026): Enthaltensein statt Gabelung

| 4 | recompute_reconcile.py | sind 4D und 7D vereinbar? | JA. A5 enthaelt C3 (3-fach und 5-fach permutieren denselben Ikosaeder); T^7=T^4 x T^3 (7=4+3). Also HLV ⊃ FFGFT: FFGFT = minimaler 3-zaehliger Kern, HLV = ikosaedrische Erweiterung. sqrt2 und 2/sqrt5 sind Invarianten koexistierender Untergruppen, kein Widerspruch. |

Damit ist die fruehere Formulierung in dim_bridge_3 ("inaequivalent / Fork strukturell")
korrigiert: das r(tau)<=1-Resultat zeigt nur, dass EINE cut-and-project-Abbildung sqrt2 und
2/sqrt5 nicht ineinander ueberfuehrt -- nicht Unvertraeglichkeit. Vereinbarkeit = gemeinsame
Einbettung, und die existiert (C3 < A5, T^4 < T^7). Der echte Unterschied ist, WELCHER
Symmetrie-Sektor physikalisch realisiert ist (FFGFT 3-fach/Koide, bestaetigt; HLV 5-fach/perp,
testbare Erweiterung).
