# Dok 190 (P41) — Rotverschiebungs-Drift: Skript

drift_sandage_loeb_check.py
  Sandage-Loeb-Drift-Test (P41): diskriminiert die Rotverschiebungs-Drift
  FFGFT von LCDM, oder verlaeuft auch das in der geteilten-Skala-Entartung?
  numpy-only, seed 20780458. Gehoert zur Praezisierung P41 in Dok 190.
  Aufruf:  python3 drift_sandage_loeb_check.py

r55_leiterkopplung_evidenzbreite.py
  Evidenzbreite des generationslinearen Korrekturgesetzes N_g = g*N_0
  (Dok. 292, Abschnitt "Leiteruebergreifende Kopplung"). Prueft: (1) N_g aus
  den angegebenen p_g; (2) ob p_3 = p_1 + p_2 eine Identitaet ist (symbolisch);
  (3) ob daraus N_3 ~ N_1 + N_2 folgt und in welcher Ordnung in xi; (4) welchen
  Restfaktor ein gemeinsames N_0 prinzipiell uebriglassen muss. Ergebnis: das
  Gesetz bleibt bestehen, seine Evidenz ist eine gemessene Zahl (N_2/N_1 =
  1,9815), nicht drei Stellen. Widerlegt nichts, leitet N_0 nicht her (offen,
  R54/P35), beruehrt die Modus-Trennung (P42) nicht. sympy-only.
  Gehoert zum Registereintrag R55 in Dok 190.
  Aufruf:  python3 r55_leiterkopplung_evidenzbreite.py
