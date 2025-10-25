import gradio as gr
from transformers import pipeline
import torch
import os  # Für OAuth-Env-Vars

# Optional: Lade GPT-2 für smarte Generierung (erster Run lädt ~500 MB)
try:
    generator = pipeline('text-generation', model='gpt2', device=-1)  # CPU-only
except Exception as e:
    print(f"Modell-Load-Fehler: {e} – Fallback zu Rule-Based.")
    generator = None

# T0-Wissensbasis (aus deinen Docs – erweitere bei Bedarf)
t0_knowledge = {
    "dualität": "Zeit-Masse-Dualität: T · m = 1 (c=ℏ=1). Masse m = 1/T = ω. Hohe Masse → dilatierte Zeit (Krümmung als m-Variation).",
    "xi": "ξ ≈ 4/3 × 10^{-4}: Universeller Fraktionsfaktor für tetraedrische Packungen (D_f ≈ 2.94). Supprimiert Divergenzen.",
    "cutoff": "Λ = E_P / ξ ≈ 10^{23} GeV: Begrenzt Singularitäten, stabilisiert Exponentialwachstum (z. B. m_n = m_0 e^{ξ n}).",
    "vorhersagen": "99% Genauigkeit: α ≈ 1/(ξ E_0^2) ≈ 1/137; m_p ≈ 1836 m_e; H_0 ≈ 70 km/s/Mpc (brückt Hubble-Tension).",
    "testbar": "Testbar: 4MOST (ξ-Gradienten in Galaxien, ~ ξ^4-supprimiert); Euclid (Lensing-Anisotropien); Planck (CMB-Ratios).",
    "universum": "Statisches Universum: Kein Big Bang – illusorische Expansion durch ξ-Dilatation.