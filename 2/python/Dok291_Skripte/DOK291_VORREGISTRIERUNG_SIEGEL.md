# FFGFT Dok 291 — Vorregistrierungs-Siegel (2. Juli 2026)

Dieses Manifest friert die FFGFT-seitige Herleitung des dynamischen Ortes von
theta = 2/9 (Dok 291 samt Mechanismus-Skripten) VOR Marcels Stage-10-Lauf ein,
ohne den Inhalt offenzulegen. Zweck: symmetrische Vorregistrierung. Der Hash
belegt, dass die Herleitung in genau dieser Form vor dem Stage-10-Verdikt
existierte — er schliesst nachtraegliche Rueckkonstruktion auf ein bekanntes
Ergebnis aus. Der Inhalt bleibt versiegelt (nicht veroeffentlicht), bis das
Stage-10-Verdikt gebucht ist; damit bleibt zugleich Marcels Blindheit
gegenueber der Zielbegruendung gewahrt. Beide Bedingungen zusammen sichern die
UNABHAENGIGKEIT der Konvergenz — die einzige Quelle des wissenschaftlichen
Werts der Bruecke.

## Eingefrorene Objekte (Stand 2. Juli 2026)

Einzelhashes (SHA256):

    cfffb6f61fadd345b7af46c276e15e32cfa13330fc36ab4121105625d64c1314  291_Dynamischer_Ort_Theta_2_9_De_ch.tex
    9a1f1069375872e98208d0b95d891aae1e38cb89ad38d16cff57cf2baba91482  291_Dynamischer_Ort_Theta_2_9_En_ch.tex
    4ab49e1d4bb9223ef6f7e53e3392a2183d4155fc6f9f3c3b81db41827ba6934f  allpass_carrier_selection.py
    9ab6ed528ade512a8dbb9b9a18bc1e890099fc1c5dfc9746e4c21e2f452159aa  allpass_theta.py
    81d1b473cd61750b6e5b8c03e01986f3864049af10de63cf92a92307ba2c910d  delta_golden_daempfung.py
    4515231cb92bea86828852f21334ec84a2e1d0962f50ff7dc7bddef6be211577  forced_vs_contingent.py
    5d4fe2d7ae8c30506c61006f5998e7bb5114118c575d3d6832635cf83d77c2ec  holonomie_landschaft.py

## Master-Siegel (der zu kommunizierende Hash)

Deterministische Konkatenation in dieser exakten Reihenfolge:
  291_..._De_ch.tex, 291_..._En_ch.tex,
  allpass_carrier_selection.py, allpass_theta.py, delta_golden_daempfung.py,
  forced_vs_contingent.py, holonomie_landschaft.py

    MASTER-SIEGEL SHA256:
    858268627a0c7813a127628129b130815dc306b6c8033d7ab2fe3cbc14145276

Reproduktion (aus dem 291-Quell- und Skriptbaum):

    cat 291_Dynamischer_Ort_Theta_2_9_De_ch.tex \
        291_Dynamischer_Ort_Theta_2_9_En_ch.tex \
        allpass_carrier_selection.py allpass_theta.py \
        delta_golden_daempfung.py forced_vs_contingent.py \
        holonomie_landschaft.py | sha256sum

## Abgrenzung

- Dies ist NICHT das Stage-10-Verdikt-Harness. Jenes ist separat eingefroren
  (SHA256 99e11399f23377702c5878784d791f8fc90a350e7999f8c2906bf99221aab246,
  bereits im IPI-Verteiler) und kodiert nur die Auswertungsregel, nicht die
  2/9-Begruendung.
- Dieses Siegel deckt die BEGRUENDUNG (Mechanismus: chi=pi/2, delta*,
  Golden-Daempfung, Selektor). Sie bleibt versiegelt bis zum Verdikt.
- Nach dem gebuchten Stage-10-Verdikt werden Dok 291 und die fuenf Skripte
  freigegeben; der Master-Siegel-Hash erlaubt dann jedem Dritten den Nachweis,
  dass nichts nachtraeglich an das Ergebnis angepasst wurde.

Freigabe-Reihenfolge (bindend):
  1. Marcels Generator-Klasse eingefroren (Zenodo, gehasht) — erledigt.
  2. FFGFT-Verdikt-Harness eingefroren (99e1..) — erledigt, im Verteiler.
  3. FFGFT-Begruendung (Dok 291) eingefroren (dieses Siegel) — hiermit.
  4. Stage 10 laeuft blind.
  5. Verdikt gebucht.
  6. Erst dann: Dok 291 frei; alle drei Siegel oeffentlich pruefbar.

## Gegenseite: HLV Stage-9-Siegel (von Marcel, 2. Juli 2026, im Verteiler bestätigt)

Damit ist die Drei-Siegel-Struktur beidseitig geschlossen. Marcels
Bestaetigung im IPI-Thread nennt drei Hashes:

    HLV Stage-9 generator/source SHA256:
    8bd0f7ce1077c5ade851721089cee0ffbbf9f3ba4832b5526c9e07208d1b8fe0

    HLV Stage-9 CONFIG SHA256:
    45020f8232bc01045ec57754e9373ba824e3c5b80a32733b963babcf17c5f06c

    HLV OneClick-Notebook SHA256:
    7c295cb13ee69c2f3a28c8d6ca43c1b637983176c2495954657f86298772a240

## Vollstaendige Drei-Siegel-Struktur fuer Stage 10 (alle vor dem Verdikt)

    1. HLV Stage-9 frozen generator/source   8bd0f7ce...8d1b8fe0  (Marcel)
       (+ CONFIG 45020f82...c5f06c, OneClick 7c295cb1...772a240)
    2. FFGFT verdict harness                  99e11399...21aab246  (Johann)
    3. FFGFT reasoning master seal            85826862...14145276  (Johann)

Freigabe: nach gebuchtem Stage-10-Verdikt oeffnen sich alle Siegel
gemeinsam. Damit ist die Unabhaengigkeit der Konvergenz in BEIDE Richtungen
nachweisbar: Marcels Generator war vor jeder 2/9-Begruendung eingefroren
(Blindheit), und die FFGFT-Begruendung war vor jedem Stage-10-Ergebnis
eingefroren (keine Rueckkonstruktion). Bestaetigt im IPI-Verteiler
2. Juli 2026.
