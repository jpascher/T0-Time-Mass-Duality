#!/usr/bin/env python3
"""
Pruefung: Hat das LCDM-Modell einen inneren Spannungspunkt in der
zeitlichen Abfolge der Expansionsraten?

Behauptung: LCDM nimmt an
  1. Frühphase: extrem rasche Entwicklung (Inflation)
  2. dann: Verlangsamung (materie-/strahlungsdominiert, gebremste Expansion)
  3. heute: erneut beschleunigte Expansion (dunkle Energie)

Ist diese Abfolge korrekt wiedergegeben? Und ist sie intern konsistent
oder erfordert sie mehrere unabhaengige Mechanismen?
"""
import math

print("="*72)
print("Die LCDM-Expansionsgeschichte: drei Phasen, drei Mechanismen")
print("="*72)
print()
print("Phase 1 - INFLATION (t ~ 10^-36 bis 10^-32 s):")
print("  Expansion um Faktor ~10^26, exponentiell beschleunigt.")
print("  Mechanismus: Inflaton-Feld mit negativem Druck.")
print("  -> eigenes hypothetisches Feld, eigenes Potential.")
print()
print("Phase 2 - GEBREMSTE EXPANSION (nach Inflation bis ~9 Mrd. Jahre):")
print("  Strahlungs- dann materiedominiert. a(t) ~ t^(1/2) bzw. t^(2/3).")
print("  Expansion VERLANGSAMT sich (deceleration, q > 0).")
print("  Mechanismus: anziehende Gravitation von Strahlung + Materie.")
print()
print("Phase 3 - ERNEUTE BESCHLEUNIGUNG (ab z ~ 0.6, ~6 Mrd. Jahre):")
print("  a(t) waechst beschleunigt (q < 0).")
print("  Mechanismus: dunkle Energie / kosmologische Konstante Lambda.")
print("  -> zweites Feld/Konstante mit negativem Druck w ~ -1.")
print()
print("="*72)
print("Der Punkt: drei verschiedene Beschleunigungsregime")
print("="*72)
print("""
Die LCDM-Zeitachse verlangt:
  beschleunigt (Inflation) -> gebremst (Materie/Strahlung)
                           -> wieder beschleunigt (Lambda)

Das ist KEIN logischer Widerspruch im strengen Sinn (die Friedmann-
Gleichung erlaubt das mathematisch), ABER es erfordert:
  - ein Inflaton-Feld (Phase 1), das danach verschwindet/zerfaellt
  - normale Gravitation (Phase 2)
  - eine kosmologische Konstante Lambda (Phase 3),
    die zufaellig GERADE JETZT dominant wird ("Koinzidenzproblem")

Also: ZWEI separate Perioden beschleunigter Expansion, getrieben von
ZWEI verschiedenen, unabhaengig postulierten Mechanismen (Inflaton
und Lambda), getrennt durch eine gebremste Phase.

Das ist die strukturelle Schwaeche, auf die der Nutzer zeigt:
- Warum zwei Beschleunigungs-Epochen mit verschiedenen Ursachen?
- Das Koinzidenzproblem: warum wird Lambda gerade in unserer Epoche
  dominant? (Feinabstimmung)
- Das Inflaton wird postuliert, dann zum Verschwinden gebracht.
""")
print("="*72)
print("Im Vergleich: FFGFT")
print("="*72)
print("""
FFGFT hat EINEN Mechanismus: die fraktale Zeitentfaltung (Rekursion R).
Die scheinbare Beschleunigung waechst monoton mit der Rekursionstiefe.
Es gibt keine separate Inflations-Epoche und keine separate Lambda-
Epoche -- nur eine fortschreitende Entfaltung.

WICHTIG (ehrlich): Das ist KEINE empirische Ueberlegenheit. FFGFT hat
fuer die Fruehphase noch keine quantitativen Vorhersagen. Der Punkt ist
nur struktureller Art: LCDM braucht zwei unabhaengige Beschleunigungs-
mechanismen + eine Bremsphase dazwischen, FFGFT braucht einen.

Das ist genau die Art Aussage, die ins Dokument gehoert -- als
struktureller Vergleich, nicht als empirischer Sieg.
""")
