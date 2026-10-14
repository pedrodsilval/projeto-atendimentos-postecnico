# Plano Técnico de Integração de IA (LangChain + Gemini)

## 1. Objetivo do Projeto
Evoluir o Sistema de Gestão e Análise de Atendimentos através da integração de Inteligência Artificial Generativa. O objetivo é transformar os dados transacionais e analíticos armazenados no banco de dados em insights acionáveis, resumos estratégicos e ferramentas interativas, utilizando processamento de linguagem natural (NLP).

## 2. Arquitetura e Fluxo de Dados Estruturado
O fluxo da informação seguirá rigorosamente a arquitetura proposta para garantir que a IA não sofra "alucinações" e atue unicamente sobre a base real de conhecimento da empresa:
**`Banco de Dados (SQLite) → Python (SQLAlchemy/Pandas) → FastAPI → LangChain → LLM (Google Gemini) → Resposta (JSON/Texto)`**

## 3. Stack Tecnológica
*   **FastAPI:** Exposição das rotas de IA e integração com o Swagger UI.
*   **LangChain:** Framework de orquestração da LLM, formatação de prompts e formatação das saídas (Parsers).
*   **Google Gemini Flash (API Gratuita):** Modelo fundacional de linguagem (LLM) selecionado pelo alto desempenho em análise de textos, velocidade e geração de relatórios.
*   **Python `python-dotenv`:** Gestão segura de variáveis de ambiente (Chave de API).

## 4. Funcionalidades e Endpoints Planejados

### 4.1. Visão Estratégica: Relatório Executivo (`GET /ai/relatorio`)
*   **Ação:** Extrai as métricas globais via Pandas (Tempo Médio, Satisfação, Ofensores) e envia como contexto para a LLM.
*   **Entrega:** A IA atua como consultora sênior e gera um texto executivo de 3 parágrafos destacando pontos positivos, gargalos operacionais e recomendações práticas para os gestores.

### 4.2. Visão Operacional: Análise de Sentimento (`GET /ai/atendimento/{id}/analise`)
*   **Ação:** Lê a descrição e os dados (status, duração) de um ticket específico no banco de dados.
*   **Entrega:** O LangChain força a LLM a devolver uma estrutura JSON rigorosa contendo:
    1.  `sentimento`: Positivo, Neutro, Negativo ou Furioso.
    2.  `analise`: Um diagnóstico técnico daquele atendimento.
    3.  `sugestao_resposta`: Um rascunho de e-mail/mensagem para tratar o problema com o cliente.

### 4.3. Visão Interativa: Chat com os Dados (`POST /ai/chat`)
*   **Ação:** Endpoint dinâmico onde o usuário envia perguntas livres no body da requisição HTTP.
*   **Entrega:** O sistema cruza a pergunta com a radiografia atual do banco de dados gerada pelo Pandas e responde de forma objetiva (ex: *"Qual setor teve pior desempenho hoje?"*).

## 5. Fases de Implementação

*   **Fase 1: Preparação da Infraestrutura**
    *   Criação da conta no Google AI Studio.
    *   Geração de API Key e isolamento via arquivo `.env`.
*   **Fase 2: Gestão de Dependências**
    *   Instalação das bibliotecas `langchain`, `langchain-google-genai` e `python-dotenv`.
*   **Fase 3: Desenvolvimento das Rotas**
    *   Criação do arquivo `routers/ai.py` isolado do resto da aplicação.
    *   Integração do roteador `ai.py` no `main.py`.
*   **Fase 4: Engenharia de Prompts**
    *   Criação dos *PromptTemplates* do LangChain.
    *   Injeção segura dos dados JSON do banco para a LLM.
*   **Fase 5: Testes e Validação**
    *   Testar limites de tempo de resposta.
    *   Validação no Swagger UI interagindo com os dados de mock gerados.

## 6. Governança e Segurança
*   **Privacidade:** Os dados trafegados na API do Gemini em contas de desenvolvedor não são utilizados para treinar modelos do Google.
*   **Limites de Custo:** A implementação utiliza o "Nível Gratuito" com bloqueio de cobranças (rate limit de 15 requisições/minuto), impossibilitando custos surpresas durante a homologação.
