# Dok268_Skripte — Forward-Untersuchung des CMB-Peak-Sektors

Diese Skripte gehören zu Dok. 268, Schritt 17, und zu Dok. 190,
Präzisierung 14 (P29/P30/P31). Sie trennen, was **vorwärts** aus T⁴
folgt, von dem, was **rückwärts** (Retrodiktion) aus den Daten kam.

Benötigt: `numpy`, `scipy`. Aufruf: `python3 <skript>.py`.

| Skript | Zeigt |
|--------|-------|
| `forward_t4_spektrum.py` | T⁴ erzeugt forward ein **dichtes** Spektrum bzw. (symmetrische Resonanz) das **harmonische** 1:2:3:4:5 — nicht {3,18,42,78}. {1,6,14,26} ist keine Forward-Teilmenge. Inkl. \|n\|²=30. |
| `naive_bessel_projektion.py` | Die naive Cℓ-Bessel-Summe **wäscht aus** (Quasi-Kontinuum), reproduziert die Peaks **nicht**. P30 zurückgenommen. |
| `resonator_vergleich.py` | Anharmonizität ist **geometrisch**: flache Kreismembran (J₀) trifft den CMB forward auf ~5%; gekrümmte Sphäre liegt daneben. |
| `dimension_anharmonizitaet.py` | ν=D/2−1; Anharmonizität **maximal bei D=2**. Herleitung der flachen Scheibe: D_eff=D_f−1=2−ξ ⇒ ν≈0 ⇒ J₀. |
| `spektral_dimension.py` | Restabweichung (D=2→1.86) ist **nicht aus ξ** (Fraktal zu schwach) und größenordnungsmäßig Messrauschen. |

**Kernaussage:** harmonisches T⁴-Rückgrat (forward) + geometrische
Anharmonizität aus der Kodimension-1-Projektion (forward, ~5%, parameterfrei,
ohne Modenauswahl). Der Verhältnis-Match {3,18,42,78} ist Retrodiktion;
Einzel-Peak-Selektion und \|n\|²=30-Ausschluss bleiben offen.
