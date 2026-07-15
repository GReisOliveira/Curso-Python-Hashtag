# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend
import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

load_dotenv() # carregar variaveis de ambiente do arquivo .env

api_key = os.getenv("api_key")

if not api_key:
    st.error("Defina api_key no arquivo .env.")
    st.stop()

cliente = genai.Client(api_key=api_key)
modelo = "gemini-flash-latest"

st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    historico_texto = []

    for mensagem_antiga in st.session_state["lista_mensagens"]:
        role = "Usuário" if mensagem_antiga["role"] == "user" else "Assistente"
        historico_texto.append(f"{role}: {mensagem_antiga['content']}")

    prompt = "\n".join(historico_texto) + "\nAssistente:"

    resposta_modelo = cliente.models.generate_content(
        model=modelo,
        contents=prompt,
    )

    resposta_ia = resposta_modelo.text

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)