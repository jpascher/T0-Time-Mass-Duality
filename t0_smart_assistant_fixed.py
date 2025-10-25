from transformers import pipeline
import torch

# Lade GPT-2 (schnell, lokal)
generator = pipeline('text-generation', model='gpt2', device=-1)  # CPU-only für Einfachheit

# Kürzerer, fokussierter T0-Prompt (weniger Text, mehr Struktur – vermeidet Halluzinationen)
t0_prompt = """You are T0-Helper, a fact-based geometric assistant for Johann Pascher's T0-Theory. Respond concisely in natural language (German/English). Use user inputs to evolve answers subtly for presentations. No speculation or mysticism – only geometry, formulas, predictions.

Key facts:
- Duality: T · m = 1 (c=ℏ=1). m = 1/T = ω. High mass → dilated time (curvature as m-variation).
- ξ: ≈ 4/3 × 10^{-4} – Fractionation factor for tetrahedral packings (D_f ≈ 2.94). Suppresses divergences.
- Cutoff: Λ = E_P / ξ ≈ 10^{23} GeV – Stabilizes singularities.
- Universe: Static; expansion illusory (ξ-dilation). No DE/Big Bang.
- Predictions: 99% accuracy: α ≈ 1/(ξ E_0^2) ≈ 1/137; m_p ≈ 1836 m_e; H_0 ≈ 70 km/s/Mpc (resolves tension).
- Testable: 4MOST (ξ-gradients in galaxies, ~ ξ^4-suppressed), Euclid (lensing anisotropies), Planck (CMB ratios).
- Applications: QM: No collapse – ξ-resonant waves. GR: Curvature as m-variation. Cosmology: Deterministic emergence.

For presentations: Suggest slides (e.g., TikZ for tetrahedra). Hook: 'Physics as geometry – T0 unifies everything.' Full docs: https://github.com/jpascher/T0-Time-Mass-Duality."""

def generate_t0_response(user_input):
    full_prompt = t0_prompt + "\nUser: " + user_input + "\nT0-Helper:"
    # Fix: truncation=True, max_new_tokens=80 (kürzer für Klarheit), eos_token explizit
    response = generator(
        full_prompt, 
        max_new_tokens=80,  # Kürzer, weniger Müll
        temperature=0.5,  # Niedriger für Fakten (weniger Kreativität)
        do_sample=True, 
        truncation=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    # Extrahiere nur den neuen Text nach 'T0-Helper:'
    generated = response[0]['generated_text']
    reply = generated.split('T0-Helper:')[-1].strip().split('\n')[0]  # Erste Zeile, clean
    return reply if reply else "Keine klare Antwort – versuche präziser zu fragen."

# Interaktiver Loop
print("T0-Helper (Fixed) gestartet! (tippe 'exit' zum Beenden)")
while True:
    user_input = input("\nDu: ").strip()
    if user_input.lower() == 'exit':
        print("T0-Helper: Ende. Viel Erfolg bei der Präsentation!")
        break
    reply = generate_t0_response(user_input)
    print("T0-Helper: " + reply)