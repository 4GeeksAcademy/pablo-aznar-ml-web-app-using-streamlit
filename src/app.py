import streamlit as st
from pickle import load
import base64
from utils1 import preprocess_text, lemmatize_text

# Cargamos modelo y vectorizador
model = load(open('src/12-opt-svm-model.pkl', 'rb'))
vectorizer = load(open('src/12-vectorizer.pkl', 'rb'))

# CSS personalizado
def load_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #0f2027);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .big-font {
        font-size: 26px !important;
        font-weight: bold;
    }

    .blinking {
        animation: blink 1s infinite;
        color: #ff4b4b;
    }

    @keyframes blink {
        0%, 50%, 100% { opacity: 1; }
        25%, 75% { opacity: 0; }
    }

    button[kind="primary"], button[kind="secondary"] {
        font-weight: bold;
        color: white !important;
        background-color: #1f6f8b !important;
        border-radius: 8px !important;
        padding: 0.6em 1.2em;
        border: none;
    }

    button[kind="primary"]:hover, button[kind="secondary"]:hover {
        background-color: #99c24d !important;
        color: black !important;
    }

    label, .stSlider label, .stTextInput label {
        color: white !important;
    }

    .custom-link a {
        color: #111 !important;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Función para reproducir sonido
def play_sound():
    with open("src/static/alarm.wav", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio autoplay loop id="alarm-audio">
                <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
        """, unsafe_allow_html=True)

# Función para limpiar
def limpiar():
    st.session_state.url_input = ""
    st.session_state.prediction_result = ""

# Cargar estilos
load_custom_css()

# Título
st.title("🚨 Clasificador de URLs SPAM")
st.markdown("Comprueba si una URL es potencialmente peligrosa o spam con nuestro modelo SVM.")

# Inicialización
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = ""

# Entrada del usuario
st.markdown('<label><strong style="color:white;">Introduce la URL a analizar:</strong></label>', unsafe_allow_html=True)
url_input = st.text_area(label="", key="url_input", placeholder="https://example.com/oferta-increible...")

# Clasificar
if st.button("🔍 Clasificar"):
    if st.session_state.url_input.strip() == "":
        st.warning("Por favor, introduce una URL.")
    else:
        clean_words = preprocess_text(st.session_state.url_input)
        lemmatized = lemmatize_text(clean_words)
        final_text = " ".join(lemmatized)
        vector = vectorizer.transform([final_text]).toarray()
        prediction = str(model.predict(vector)[0])

        if prediction == "1":
            st.session_state.prediction_result = '<p class="big-font blinking">⚠️ ¡¡¡SPAM DETECTADO!!! ⚠️</p>'
            play_sound()
        else:
            st.session_state.prediction_result = "✅ La URL parece legítima. No se detecta spam."
            with st.expander("🔗 ¿Deseas visitar la URL introducida?"):
                st.markdown(
                    f'<div class="custom-link"><a href="{st.session_state.url_input}" target="_blank">🌐 Abrir URL en nueva pestaña</a></div>',
                    unsafe_allow_html=True
                )

# Mostramos resultado si existe
if st.session_state.prediction_result:
    if "⚠️" in st.session_state.prediction_result:
        st.markdown(st.session_state.prediction_result, unsafe_allow_html=True)
    else:
        st.success(st.session_state.prediction_result)

# Encuesta
st.markdown("---")
st.markdown('<strong style="color:white;">🗳️ ¿Cómo valorarías tu experiencia usando esta aplicación?</strong>', unsafe_allow_html=True)
rating = st.slider("Califica esta app", 1, 5, 3)

if st.button("📩 Enviar valoración"):
    st.success(f"✅ ¡Gracias por tu valoración de {rating} estrella(s)!")

# Botón limpiar (con callback)
st.button("🧹 Limpiar", on_click=limpiar)