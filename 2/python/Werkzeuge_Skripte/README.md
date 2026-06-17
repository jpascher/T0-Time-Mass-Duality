# Werkzeuge_Skripte — Hilfswerkzeuge (kein Physik-Dokument)

Tooling, das zu **keinem** FFGFT-Dokument gehört, aber zum Korpus-Workflow.

## ffgft_tts.py
Batch-Vertonung der FFGFT-Slide-Chunks mit Chatterbox-TTS. Liest
`FFGFT_Chatterbox_Chunks.txt`, erzeugt pro Häppchen ein WAV, kann pro Slide und/oder
zu einem durchgehenden Avatar-Ton zusammenhängen. Resume-fähig, feste Sprecherstimme
via `--voice`, `--dry-run` zum Parsen-Prüfen.

Setup: `pip install chatterbox-tts torchaudio`
Lauf:  `python3 ffgft_tts.py --merge-slides --merge-full`
(Externe Eingabe `FFGFT_Chatterbox_Chunks.txt` und das Chatterbox-Modell nötig;
nicht numpy-only.)
