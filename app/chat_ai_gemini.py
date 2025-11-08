from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

# Cargar variables de entorno desde .env si existe
# En Docker, las variables ya estarán disponibles en el entorno
# si se usa --env-file al ejecutar el contenedor
load_dotenv(override=True)  # override=True da prioridad a las variables en .env sobre las del entorno

# Verificar si la API key está configurada
api_key = os.getenv('GEMINI_API')
if not api_key:
    st.error("⚠️ La API key de Gemini no está configurada. Por favor, configura la variable de entorno GEMINI_API.")
    st.info("Si estás ejecutando la aplicación con Docker, asegúrate de usar --env-file .env al ejecutar el contenedor.")
    st.stop()

# Inicializar el cliente de Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash')
except Exception as e:
    st.error(f"⚠️ Error al inicializar el cliente de Gemini: {str(e)}")
    st.stop()

def chat_ai(message):
    try:
        instructions = "Responds like a chat assistant without including 'Assistant:' in the response."
        response = model.generate_content(message + instructions)
        return response.text
    except Exception as e:
        return f"Lo siento, ocurrió un error al procesar tu mensaje: {str(e)}"


st.title("Chat AI with GEMINI-2.5-FLASH 🤖 Version 1.0.0")
st.write("This is a chat using Gemini 2.5 flash model.")


with st.chat_message('assistant'):
    st.markdown("Hello! I am Gemini AI. How can I help you today?")


user_input = st.chat_input("Write a message...")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

if user_input:

    st.session_state.messages.append({'role': 'user', 'content': user_input})

    with st.chat_message('user'):
        st.markdown(user_input)
    
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

    
    with st.chat_message('assistant'):
        thinking_message = st.empty()
        thinking_message.markdown("🤔 Thinking...")
    
    response = chat_ai(context)
    thinking_message.markdown(response)
    
    st.session_state.messages.append({'role': "assistant", 'content': response })


