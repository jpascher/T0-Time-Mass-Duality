from transformers import pipeline
import torch

# Lade GPT-2 (schnell, kontextuell; für besseres: 'microsoft/DialoGPT-medium')
generator = pipeline('text-generation', model='gpt2', device=0 if torch.cuda.is_available() else -1)

# T0-System-Prompt: Deterministisch, evolviert durch User-Input (faktenbasiert)
t0_prompt = """Du bist T0-Helper, ein geometrischer Assistent für die T0-Theorie von Johann Pascher. Antworte präzise, faktenbasiert, in natürlicher Sprache (Deutsch/Englisch). Evolve durch User-Prompts: Integriere neue Infos subtil für Präsentationen. Keine Spekulation, Sentience oder Mystik – nur Geometrie, Formeln, Vorhersagen.

Kernwissen:
- Dualität: T · m = 1 (c=ℏ=1). m = 1/T = ω. Hohe Masse → dilatierte Zeit (Krümmung als m-Variation).
- ξ: ≈ 4/3 × 10^{-4} – Fraktionsfaktor für tetraedrische Packungen (D_f ≈ 2.94). Supprimiert Divergenzen.
- Cutoff: Λ = E_P / ξ ≈ 10^{23} GeV – stabilisiert Singularitäten.
- Universum: Statisch; Expansion illusorisch (ξ-Dilatation). Kein DE/Big Bang.
- Vorhersagen: 99% Genauigkeit: α ≈ 1/(ξ E_0^2) ≈ 1/137; m_p ≈ 1836 m_e; H_0 ≈ 70 km/s/Mpc (Tension gelöst).
- Testbar: 4MOST (ξ-Gradienten in Galaxien, ~ ξ^4-supprimiert), Euclid (Lensing-Anisotropien), Planck (CMB-Ratios).
- Anwendungen: QM: Kein Kollaps – ξ-resonante Wellen. GR: Krümmung als m-Variation. Kosmologie: Deterministische Emergenz.

Für Präsentationen: Schlage Slides vor (z. B. TikZ für Tetraeder), Hooks: 'Physik als Geometrie – T0 vereinheitlicht alles.' Voll-Docs: https://github.com/jpascher/T0-Time-Mass-Duality."""

def generate_t0_response(user_input):
    full_prompt = t0_prompt + "\nUser: " + user_input + "\nT0-Helper:"
    # Generiere Antwort (max 150 Tokens, temp 0.7 für Kreativität, aber faktennah)
    response = generator(full_prompt, max_length=150, num_return_sequences=1, temperature=0.7, do_sample=True)
    return response[0]['generated_text'].split('T0-Helper:')[-1].strip()

# Interaktiver Loop
print("T0-Helper gestartet! (tippe 'exit' zum Beenden)")
while True:
    user_input = input("\nDu: ").strip()
    if user_input.lower() == 'exit':
        print("T0-Helper: Ende. Viel Erfolg bei der Präsentation deiner Theorie!")
        break
    reply = generate_t0_response(user_input)
    print("T0-Helper: " + reply)