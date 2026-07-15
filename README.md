# 🐍 Curso Python Hashtag - Automação, Análise de Dados e IA

Repositório com os projetos práticos desenvolvidos durante o curso **Python Impressionador (Hashtag Treinamentos)**, reunindo automação de processos, análise de dados, machine learning e desenvolvimento de aplicações com inteligência artificial.

## 📌 Sobre o projeto

Este repositório documenta minha jornada de aprendizado prático em Python aplicado a cenários reais de automação empresarial, ciência de dados e IA generativa. Cada pasta (`Auto`, `Auto2`, `Auto3`, `Auto4`) representa uma etapa do curso, evoluindo de automações simples até a construção de um chatbot com IA.

## 🚀 Tecnologias e bibliotecas utilizadas

- **Python 3**
- **PyAutoGUI** – automação de tarefas via interface gráfica (mouse e teclado)
- **Pandas** – manipulação e tratamento de dados
- **Plotly Express** – visualização de dados interativa
- **Scikit-Learn** – criação e treinamento de modelos preditivos
- **Streamlit** – criação de interfaces web interativas
- **Google Gen AI (Gemini)** – integração com modelo de linguagem para chatbot
- **python-dotenv** – gerenciamento de variáveis de ambiente e chaves de API

## 🧠 O que eu aprendi e estudei

### 1. Automação com PyAutoGUI
Aprendi a automatizar tarefas repetitivas que envolvem interação com a interface do sistema operacional, como abrir o navegador, acessar um sistema web, realizar login e preencher formulários automaticamente. O projeto simula o cadastro de produtos em massa a partir de uma planilha `.csv`, controlando cliques, digitação e navegação entre campos com `pyautogui`. Isso me mostrou como automatizar processos manuais e repetitivos do dia a dia usando controle programático de mouse e teclado.

**Principais conceitos:**
- Controle de mouse e teclado via código
- Leitura de dados de um `.csv` com Pandas e conversão para dicionário (`to_dict("records")`)
- Uso de `time.sleep()` para sincronizar a automação com o carregamento das páginas
- Estruturação de um loop para repetir o processo de cadastro para múltiplos registros

### 2. Análise de Dados com Jupyter e Plotly (Análise de Cancelamentos)
Trabalhei com uma base de dados real de clientes para entender os motivos de cancelamento de um serviço (churn). O foco foi transformar dados brutos em insights acionáveis para o negócio.

**Principais conceitos:**
- Importação e limpeza de dados com Pandas (remoção de colunas irrelevantes e valores nulos com `dropna()`)
- Análise exploratória inicial para entender a proporção de clientes que cancelaram
- Criação de gráficos de distribuição (histogramas) para cada coluna da base, cruzando com a variável de cancelamento, usando Plotly Express
- Identificação de padrões de causa e efeito, como:
  - Contratos mensais têm taxa de cancelamento muito maior que contratos anuais/trimestrais
  - Clientes que ligam mais de 4 vezes para o call center cancelam o serviço
  - Atrasos de pagamento acima de 20 dias estão fortemente ligados ao cancelamento
- Aplicação de filtros sucessivos na base para isolar os "clientes-problema" e medir o impacto de cada fator na taxa de cancelamento (de 56% para 18%)

### 3. Modelos Preditivos com Scikit-Learn
Dei os primeiros passos na criação de modelos de machine learning para prever comportamentos, como a probabilidade de um cliente cancelar o serviço, aplicando o fluxo de treinamento e avaliação de modelos preditivos.

### 4. Chatbot com IA e Streamlit
Desenvolvi uma aplicação web de chat integrando o modelo Gemini (Google Gen AI) com uma interface construída em Streamlit, incluindo sistema de memória de conversa.

**Principais conceitos:**
- Uso de variáveis de ambiente com `python-dotenv` para proteger chaves de API
- Uso do `st.session_state` como memória da aplicação, armazenando o histórico de mensagens durante a sessão
- Construção da interface de chat com `st.chat_input()` e `st.chat_message()`
- Montagem de um prompt com todo o histórico da conversa para manter o contexto nas respostas da IA
- Integração com a API do Google Gemini (`google.genai`) para gerar respostas dinâmicas

## 📂 Estrutura do repositório

Curso-Python-Hashtag/
├── Auto/       # Automação de cadastro com PyAutoGUI
├── Auto2/      # Análise de dados com plotly
├── Auto3/      # Análise de dados e modelos preditivos
├── Auto4/      # Chatbot com IA e Streamlit
├── .gitignore
└── README.md

## 🎯 Principais aprendizados gerais

- Como automatizar tarefas repetitivas e economizar tempo com PyAutoGUI
- Como limpar, tratar e explorar dados com Pandas
- Como transformar dados em visualizações que geram insights de negócio com Plotly
- Como aplicar machine learning para resolver problemas reais de previsão
- Como construir aplicações interativas e integrar IA generativa com Streamlit
- Boas práticas de segurança, como uso de variáveis de ambiente para chaves de API
