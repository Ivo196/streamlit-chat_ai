from dotenv import load_dotenv
from google import genai
import os
import streamlit as st

load_dotenv()

client = genai.Client(api_key = os.getenv('GEMINI_API'))

def chat_ai(message):
    instructions = "Responde como un asistente de chat sin incluir 'Assistant:' en la respuesta. "
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents= message + instructions
    )
    return response.text


st.title("Chat AI with GEMINI 1.5 🤖")
st.write("This is a chat using Gemini 1.5 flash model. ")


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


