import os
from google import genai
from dotenv import load_dotenv
import streamlit as st

# 1. Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# 2. Validamos que la clave exista antes de continuar
api_key_segura = os.getenv("GEMINI_API_KEY")

if not api_key_segura:
    print(" Error: No se encontró la variable GEMINI_API_KEY en el archivo .env")
else:
    # 3. Inicializamos el cliente moderno de Google GenAI pasándole la clave de forma explícita
    client = genai.Client(api_key=api_key_segura)

    # 4. Generamos el contenido usando el modelo recomendado actual
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Dame 3 ideas de títulos atractivos para un reel sobre programación en Python.',
    )

    print("--- Respuesta Segura de Google Gemini ---")
    print(response.text)

# --- Configuración de la Interfaz con Streamlit ---
st.set_page_config(page_title="Asistente Gemini", page_icon="🤖")

st.title("🚀 Generador de Ideas con Gemini")
st.markdown("Introduce un tema para obtener sugerencias creativas utilizando Inteligencia Artificial.")

# Campo de entrada de texto para el usuario
tema_usuario = st.text_input("¿Sobre qué quieres generar ideas?", "Programación en Python")

if st.button("Generar Ideas"):
    if not api_key_segura:
        st.error("Error: No se encontró la variable GEMINI_API_KEY en el archivo .env")
    else:
        with st.spinner("Consultando a Gemini..."):
            try:
                # 4. Generamos el contenido usando el input del usuario
                prompt_dinamico = f"Dame 3 ideas de títulos atractivos para un reel sobre {tema_usuario}."
                
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=prompt_dinamico,
                )

                st.subheader("--- Respuesta de Google Gemini ---")
                st.write(response.text)
                st.success("¡Contenido generado con éxito!")
                
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")

