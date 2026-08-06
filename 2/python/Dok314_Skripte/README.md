# Dok 314 — Gitter im Hilbertraum: Pruefskripte

Alle Skripte sind deterministisch (keine Zufallszahlen ausser mit
festen Seeds), tragen die Sollwerte als Assertions und brechen bei
jeder Abweichung mit Fehlerort ab. Ein Durchlauf ohne Ausgabe
"FEHLER" ist die Verifikation der im Dokument gebuchten Zahlen.

d4_skript_1_spektrum_deformation.py
  Thetareihen D4 gegen Z4 mit k4-Aufspaltung (24 = 12+12), Spektrum
  des anisotropen Torus E(k) = k1^2+k2^2+k3^2 + (k4/r)^2 mit der
  Wicklungsformel E = 1 + 1/r^2, und die exakte Kreuzungskarte:
  im Bereich 1 < r <= 2.5 gibt es genau zwei Kreuzungsradien,
  r = sqrt(2) und r = sqrt(3). Nur Standardbibliothek.
  Gehoert zu Kap. B/C und 9.1.
  Aufruf:  python3 d4_skript_1_spektrum_deformation.py

d4_skript_2_trialitaet_orbifold_phasen.py
  Automorphismenzaehlung |Aut(D4)| = 1152 = |W(F4)| und
  |Aut(Z4)| = 384 per Gram-Tupel-Enumeration; Ordnungsverteilung
  {1,2,3,4,6,8,12} mit NULL Elementen der Ordnung 5 (5 teilt
  1152 = 2^7*3^2 nicht); Dreiklassen-Struktur der 80 Ordnung-3-
  Elemente; |det(1-A)| = 9 fuer die Trialitaetsklasse (T^4/Z3 mit
  9 Fixpunkten); Zirkulant {1, w, w^2} auf jedem Dreierorbit;
  Phasen-Test: alle Invarianten haben Nennerspektrum {1,2,3,6},
  2/9 kommt NICHT vor; -1-Paarung 24 = 4 x 6.
  WICHTIG: Trialitaetselemente sind halbzahlig — es wird exakt mit
  2A (ganzzahlig) gerechnet; Rundung auf ganze Zahlen zerstoert
  genau diese Elemente. numpy.
  Gehoert zu Kap. E/F/G und Abschnitt 6/7.
  Aufruf:  python3 d4_skript_2_trialitaet_orbifold_phasen.py

d4_skript_3_schalen_casimir.py
  Schalensaetze bis Norm 20 (jede Schale zerfaellt frei in
  Dreierorbits, Charaktergehalt N/3 je, N/6 Sechserbloecke — die
  Struktur ist generisch, nicht auf die erste Schale beschraenkt);
  Epstein-Zeta bei s = -1/2 fuer den Casimir-Vergleich bei
  Kovolumen 1, mit doppelter Verifikation (Direktsumme bei
  s = 4, 5; Z4 exakt gegen 8(1-4^(1-s)) zeta(s) zeta(s-1) auf
  25+ Stellen, auch bei s = -1/2). Ergebnis: der Z4-Torus liegt
  tiefer (-0.932 gegen -0.869) — das dichteste Gitter verliert,
  weil es die groesste Spektralluecke hat. Waermekern: Weyl-Term
  identisch, Gitterunterschied 4e-27 bei t = 0.05. numpy, mpmath.
  Gehoert zu Kap. H und Abschnitt 9.2-9.4.
  Aufruf:  python3 d4_skript_3_schalen_casimir.py

d4_skript_4_stoerung_reziprozitaet.py
  Teil A: Stoerungstheorie 1. Ordnung auf der 24er-Schale.
  Multiplettgroessen folgen den IRREP-DIMENSIONEN der respektierten
  Symmetrie, nicht den Orbits: 9+8+4+2+1 bei voller Aut(D4)-
  Symmetrie, 8x1 + 8x2 bei Z3 (abelsch, Dubletts durch antiunitaere
  chi1/chi2-Paarung), 24x1 generisch. Je drei unabhaengige Seeds
  pro Symmetrieklasse, Ergebnis seedunabhaengig.
  Teil B: Reziprozitaet auf dem Massenkreis. lambda_4 * m = 2 pi
  modenweise exakt (de Broglie, Ort-Relation); im Gemisch
  <k><1/k> >= 1 nach Jensen, Gleichheit genau bei scharfer Schale
  (2000 Zufallsverteilungen, Minimum 1.077). numpy, mpmath.
  Gehoert zu Kap. D1 und J.3.
  Aufruf:  python3 d4_skript_4_stoerung_reziprozitaet.py
