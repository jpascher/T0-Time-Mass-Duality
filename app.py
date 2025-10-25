# app.py - Speichere diesen Code in der Datei
import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from t0_assistant import T0ResearchAssistant

def main():
    st.set_page_config(
        page_title="T0 Research Assistant",
        page_icon="🔬",
        layout="wide"
    )
    
    st.title("🔬 T0 Theory Research Assistant")
    st.markdown("**Personal AI für die T0-Time-Mass-Duality Forschung**")
    
    if 'assistant' not in st.session_state:
        st.session_state.assistant = T0ResearchAssistant()
        st.session_state.conversation = []
    
    with st.sidebar:
        st.header("T0 Theory Basics")
        st.markdown("""
        - **ξ-Parameter**: 4/3 × 10⁻⁴
        - **Massenhierarchie**: m_i ∝ e^(ξ·n_i)
        - **Fraktale Dimension**: D_f = 2.94
        - **Zeit-Masse-Dualität**: T·m = 1
        """)
        
        if st.button("GitHub Repository"):
            st.markdown("[T0-Time-Mass-Duality](https://github.com/jpascher/T0-Time-Mass-Duality)")
    
    st.header("Forschungs-Dialog")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("ξ-Parameter"):
            st.session_state.user_input = "Erkläre den ξ-Parameter"
    with col2:
        if st.button("Massenhierarchie"):
            st.session_state.user_input = "Wie beschreibt T0 die Leptonenmassen?"
    with col3:
        if st.button("Fraktale Raumzeit"):
            st.session_state.user_input = "Was bedeutet D_f = 2.94?"
    with col4:
        if st.button("Experimentelle Tests"):
            st.session_state.user_input = "Welche experimentellen Tests gibt es?"
    
    user_input = st.text_input(
        "Stellen Sie eine Frage zur T0-Theorie:",
        key="user_input",
        placeholder="z.B. 'Erkläre die Beziehung zwischen ξ und e'"
    )
    
    if user_input:
        with st.spinner("Analysiere Frage..."):
            response = st.session_state.assistant.generate_response(user_input)
            
            st.session_state.conversation.append({
                "question": user_input,
                "response": response
            })
    
    st.header("Konversationsverlauf")
    for i, exchange in enumerate(reversed(st.session_state.conversation[-5:])):
        with st.expander(f"Frage {len(st.session_state.conversation)-i}: {exchange['question'][:50]}..."):
            st.markdown(f"**Frage:** {exchange['question']}")
            st.markdown(f"**Antwort:** {exchange['response']}")

if __name__ == "__main__":
    main()