FFGFT — gebündelte Schriften (für LuaLaTeX-Build ohne Netz-Download)
====================================================================

Diese drei Schriftfamilien werden von den Präambeln verlangt
(Sources/pri-end/T0_preamble_*.tex):

  Inter            -> \setmainfont / \setsansfont   (4 Schnitte)
  JetBrains Mono   -> \setmonofont                  (4 Schnitte)
  Libertinus Math  -> \setmathfont (unicode-math)   1 OTF, MIT MATH-Tabelle
                      -> korrekte \underbrace-Klammern

Latin Modern (in einzelnen Sandbox-Präambeln) kommt aus texlive-fonts-recommended
und ist Teil der TeX-Basis -> muss nicht gebündelt werden.

Herkunft / Lizenz: alle SIL Open Font License 1.1 (siehe LICENSES/).
  - Inter            : aus Google-Fonts Variable-Font, statische Schnitte
                       (wght 400/700, opsz 14) erzeugt; Dateinamen Inter-Regular
                       .. Inter-BoldItalic passend zum *-Muster der Präambel.
  - JetBrains Mono   : Original-TTFs aus dem JetBrains-Repo.
  - Libertinus Math  : Original-OTF aus dem Ubuntu-Paket fonts-libertinus 7.051
                       (Google-Fonts-TTF hat KEINE MATH-Tabelle -> unbrauchbar).

Installation übernimmt setup_build_env.sh automatisch (kein Netz nötig).
