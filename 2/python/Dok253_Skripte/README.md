# Dok 253 (R63) — xi-Wirksamkeit bei der Faktorisierung: Skript

r63_xi_faktorisierung_wirkungslos.py
  Audit der xi-Resonanzheuristik aus rsa/factorization_benchmark_library.py
  (OptimizedUniversalT0Algorithm v2.1.0). Prueft: (1) ob der Schwellwert 1/1000
  im als "universell optimal" deklarierten Bereich xi >= 1/15 ueberhaupt je eine
  Periode verwirft (nein, 0 von 1999) -- der Filter ist dort inert; (2) ob das
  r=2-Maximum parameterabhaengig ist (nein, omega-pi = pi(2/r-1) verschwindet
  exakt bei r=2 fuer jedes xi); (3) ob das Gesamtergebnis von xi abhaengt
  (nein im Wirkbereich: identisch zum xi-freien Kontrollalgorithmus ueber 20
  Semiprime, 19/20 bei beiden, ebenso fuer die Kontrollwerte xi=1/2 und xi=1e6;
  mit xi_FFGFT=4/30000 dagegen 5/20, alle aus dem trivial_gcd-Zweig, keiner
  aus dem Periodenweg); (4) ob die Strategiewahl zirkulaer ist (ja,
  _simple_factorize loest n vollstaendig, bevor xi gewaehlt wird, 20/20);
  (5) ob die in Dok. 253 gedruckte Gauss-Form der implementierten Lorentz-Form
  entspricht (nein -- gleiches Maximum, unvereinbare Flanken).
  Ergebnis: die "xi-Optimierung" auf 1/10 hat nicht einen wirksamen Parameter
  gefunden, sondern den Bereich, in dem der Filter nicht mehr filtert.
  Entwertet keine Ableitung; xi als Fundamentalparameter (R57) unberuehrt.
  Bestaetigt und verschaerft die gesicherten Fakten von Dok. 253.
  Standardbibliothek only (math, fractions), keine externen Abhaengigkeiten,
  laeuft ohne die gepruefte Bibliothek (originalgetreue Nachbildung).
  Gehoert zum Registereintrag R63 in Dok 190.
  Aufruf:  python3 r63_xi_faktorisierung_wirkungslos.py
