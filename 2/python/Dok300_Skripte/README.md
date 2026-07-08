# Dok 300 -- Skripte: Spiral-Time als Auslesung und Comparator, K_frak = 1-100xi

Reproduzierbares numpy-/python-only-Prüfskript.

- `ffgft_300_kfrak_schliessungskomma_pruefung.py` -- prüft das Schließungs-Komma
  der aufgerollten Rekursion: xi = 4/30000, N = 1/(100 xi) = 75, eps = 100 xi = 1/75.
  Korpuswert K_frak = 1 - 100 xi = 74/75 = 0.9867 (subtraktiv). Das Komma
  re-exprimiert 100 xi; der Anker ist Dok. 133 (Faktor 100 aus RG-Lauf,
  K_frak durch m_e/m_mu-Konsistenz fixiert), nicht die 75. Das Skript rechnet
  die xi-Seite exakt, lässt K_frak als Eingabe und listet beide Vorzeichen als
  Kandidaten. Der Zeitsektor-Gegenlauf (BLP-Rückfluss 5,125) liegt bei Dok 299
  (`Dok299_Skripte/ffgft_299_iota_gegenlauf_winding_locked.py`).
