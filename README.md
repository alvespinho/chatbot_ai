# ChatBot "Gênio da Lâmpada" – Assistente Inteligente de Código

Este projeto é um **ChatBot educacional** construído com **Streamlit** e a API **Google Gemini**, criado para ajudar estudantes a desenvolver **raciocínio lógico**, entender conceitos e resolver problemas de forma guiada — sem entregar respostas prontas.

O foco é estimular o aluno a pensar, formular caminhos, compreender conceitos e aplicar estratégias inteligentes.

---

## ✨ Funcionalidades

* Chat interativo usando **Google Gemini 2.5 Flash**.
* Estilo de ensino baseado em:

  1. **Apresentação curta**.
  2. **Plano de Ação** para cada problema.
  3. **Explicações em blocos**.
  4. **Ajuda progressiva em 3 níveis**.
  5. **Clareza e foco**, sem enrolação.
  6. **Resumo estratégico** final.
* Histórico da conversa mantido automaticamente.
* Interface leve e simples feita em **Streamlit**.
* Uso seguro da API via **dotenv** e variáveis de ambiente.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit** (interface web)
* **Google Generative AI (Gemini)**
* **python-dotenv** (carregar variáveis de ambiente)

---

## 📦 Instalação

### 1. Clone o repositório

```
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. Crie e ative um ambiente virtual

Linux/macOS:

```
python3 -m venv .chatbot_ai
source .chatbot_ai/bin/activate
```

Windows:

```
python -m venv .chatbot_ai
.chatbot_ai\Scripts\activate
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

---

## 🔑 Configure sua chave da API Gemini

1. Acesse:
   [https://aistudio.google.com/app/api-keys](https://aistudio.google.com/app/api-keys)
2. Crie uma key
3. No projeto, crie um arquivo `.env`:

```
GOOGLE_API_KEY="sua_chave_aqui"
```

Certifique-se de que **.env está no .gitignore**.

---

## ▶️ Como rodar o projeto

Com o ambiente virtual ativado, execute:

```
streamlit run app.py
```

O navegador abrirá automaticamente.

---

## 📁 Estrutura do Projeto

```
📂 seu_projeto
│── app.py
│── .env                # NÃO subir para o GitHub
│── .gitignore
│── requirements.txt
└── README.md
```

---

## 🧠 Lógica do ChatBot

O Gênio da Lâmpada segue um fluxo inteligente:

1. Saúda rapidamente.
2. Pede o assunto.
3. Gera um **Plano de Ação** numerado.
4. Explica em blocos.
5. Se o aluno travar, usa **Ajuda Progressiva**:

   * Nível 1: dica conceitual
   * Nível 2: exemplo análogo
   * Nível 3: passo guiado
6. Ao final, gera um **Resumo Estratégico** da solução.

Esse padrão garante aprendizado profundo e não dependência da IA.

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## 💬 Contato

Caso precise de ajuda ou queira evoluir o projeto, envie uma issue no GitHub ou entre em contato.

---

Bom estudo e bons códigos!
