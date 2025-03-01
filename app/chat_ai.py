import ollama
import streamlit as st


st.title("Chat AI with DeepSeek 🤖✨")
st.write("This is a simple web app to chat with Deepseek AI.")

user_input = st.chat_input("Write a message...")

with st.chat_message("assistant"):
    st.markdown("Hello! I am Deepseek AI. How can I help you today?")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message('assistant'):
        thinking_message = st.empty()
        thinking_message.markdown("🤔 Thinking...")


    response = ollama.chat(model="deepseek-r1:1.5b", messages=st.session_state.messages)

    bot_response = response['message']['content']

    thinking_message.markdown(bot_response)

 
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
