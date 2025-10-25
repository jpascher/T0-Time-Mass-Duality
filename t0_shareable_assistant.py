import gradio as gr
from transformers import pipeline  # Optional für LLM-Erweiterung

# Optional: Lade GPT-2 für smarte Generierung (erster Run lädt Modell)
generator = pipeline('text-generation', model='gpt2', device=-1) if 'generator' not in globals() else generator

# T0-Wissensbasis (aus deinen Docs – erweitere hier)
t0_knowledge = {
    "dualität": "Zeit-Masse-Dualität: T · m = 1 (c=ℏ=1). Masse m = 1/T = ω. Hohe Masse → dilatierte Zeit (Krümmung als m-Variation).",
    "xi": "ξ ≈ 4/3 × 10^{-4}: Universeller Fraktionsfaktor für tetraedrische Packungen (D_f ≈ 2.94). Supprimiert Divergenzen.",
    "cutoff": "Λ = E_P / ξ ≈ 10^{23} GeV: Begrenzt Singularitäten, stabilisiert Exponentialwachstum (z. B. m_n = m_0 e^{ξ n}).",
    "vorhersagen": "99% Genauigkeit: α ≈ 1/(ξ E_0^2) ≈ 1/137; m_p ≈ 1836 m_e; H_0 ≈ 70 km/s/Mpc (brückt Hubble-Tension).",
    "testbar": "Testbar: 4MOST (ξ-Gradienten in Galaxien, ~ ξ^4-supprimiert); Euclid (Lensing-Anisotropien); Planck (CMB-Ratios).",
    "universum": "Statisches Universum: Kein Big Bang – illusorische Expansion durch ξ-Dilatation. Kein Dark Energy.",
    "präsentation": "Für Präsentationen: Schlage Slides vor (z. B. TikZ für Tetraeder). Hook: 'Physik als Geometrie – T0 vereinheitlicht alles.' Voll-Docs: https://github.com/jpascher/T0-Time-Mass-Duality."
}

def t0_response(message):
    message_lower = message.lower()
    found = False
    response = "T0-Helper: Basierend auf Johann Pascher's Theorie.\n"
    for key, value in t0_knowledge.items():
        if key in message_lower:
            response += value + "\n"
            found = True
    if not found:
        # Fallback: Generiere mit GPT-2 (smarter Touch)
        full_prompt = "T0-Theorie Erklärung: " + message + " (kurz, geometrisch)."
        gen = generator(full_prompt, max_new_tokens=50, temperature=0.5, do_sample=True, truncation=True)
        response += gen[0]['generated_text'].strip() + "\nVoll-Docs: https://github.com/jpascher/T0-Time-Mass-Duality."
    return response

# Web-App mit Gradio (öffentlich teilerbar)
demo = gr.Interface(
    fn=t0_response,
    inputs=gr.Textbox(label="Deine Frage zu T0-Theorie", placeholder="z. B. Was ist ξ?"),
    outputs=gr.Textbox(label="T0-Antwort"),
    title="T0-Assistent: Geometrischer Physik-Helper",
    description="Ein faktenbasierter Assistent für die T0-Theorie. Teile den Link mit anderen!",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(share=True)  # Erzeugt öffentlichen Link!