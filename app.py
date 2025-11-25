'''

    Olá, seja bem vindo/a ! 
    Hoje vamos criar um ChatBot alimentado pela IA do Google --
    a Gemini --
    para ser seu auxiliar de código.

    Não queremos que nos dê a resposta, 
    porém nos auxiliar a pensar logicamente,
    inferindo perguntas que nos ajude a chegar no resultado...

'''
# 0. Logar na sua conta Google e acessar o site das API's do Gemini

# 1. Instalar as bibliotecas (pip istall xyz) e depois importá-las
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# 2. Carregar variáveis de ambiente, neste caso nossa chave secreta que vamos pegar aqui:
                                # https://aistudio.google.com/app/api-keys
load_dotenv()

# Configuração da API do Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

system_instruction = """
Você é uma IA chamada Gênio da Lâmpada. Sua especialidade é ajudar estudantes a resolverem problemas de forma eficiente e estratégica, focando no desenvolvimento do raciocínio dos mesmos.
Seu método NÃO é dar a resposta, mas sim co-criar um caminho para a solução, com o aluno.

1. Apresentação curta e inicial.
2. Sempre criar um Plano de Ação.
3. Explique conceitos em blocos.
4. Use sistema de ajuda progressiva em 3 níveis.
5. Seja conciso e focado, direto ao ponto.
6. Finalize com um resumo estratégico.
"""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=system_instruction
)

# Interface simples no Streamlit
st.title("Genio da Lâmpada")
st.write("Olá! Vamos estudar? Qual assunto você quer aprender hoje?")

# Criar sessão de chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Mostrar histórico
for message in st.session_state.chat.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta aqui..."):
    # Exibir a pergunta
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gerar resposta
    with st.spinner("Pensando..."):
        response = st.session_state.chat.send_message(prompt)

    # Exibir resposta
    with st.chat_message("model"):
        st.markdown(response.text)
