<h1 align="center">
  📊 Sistema de Gestão e Análise de Atendimentos
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

<p align="center">
  <strong>Projeto Final & Etapa de IA</strong> desenvolvidos para o curso de Pós Técnico. Uma API REST completa para registro, gerenciamento, análise estatística e extração de insights inteligentes via LLM sobre atendimentos ao cliente.
</p>

---

## 🚀 O Projeto

O objetivo deste projeto é aplicar de maneira integrada os conhecimentos de **Desenvolvimento Back-end**, **Bancos de Dados Relacionais**, **Análise de Dados** e **Inteligência Artificial Generativa**. A aplicação simula o sistema interno de uma empresa para controlar os tickets de suporte, oferecendo desde operações de CRUD até relatórios analíticos em tempo real e integração com LLM via LangChain.

### 🧠 Fluxo de Integração com IA
A solução atua exclusivamente com os dados reais armazenados, evitando alucinações e sem alterar valores da base:
$$\text{Banco de Dados (SQLite)} \rightarrow \text{Python (SQLAlchemy/Pandas)} \rightarrow \text{FastAPI} \rightarrow \text{LangChain} \rightarrow \text{LLM (Gemini)} \rightarrow \text{Resposta IA}$$

### ✨ Principais Funcionalidades

- **CRUD de Atendimentos**: Cadastro, leitura, atualização e exclusão de tickets com validação de dados via Pydantic.
- **Armazenamento Persistente**: Integração com banco de dados relacional via SQLAlchemy.
- **Análise de Dados (Data Science)**: Utilização do **Pandas** para cruzar métricas e identificar padrões:
  - Distribuição de atendimentos por categoria e status.
  - Avaliação de desempenho dos atendentes (volume e avaliação média).
  - Cálculo de tempo médio de resolução e cruzamento por categoria.
  - Mapeamento de volume de chamados por dia da semana.
- **Inteligência Artificial Generativa (LangChain + Google Gemini)**:
  - **Relatório Executivo**: Síntese gerencial de pontos fortes, ofensores e recomendações práticas.
  - **Classificação e Análise de Sentimento**: Diagnóstico do ticket, classificação do sentimento do cliente e geração de minuta de resposta.
  - **Chat com os Dados**: Assistente virtual para responder perguntas livres consultando a radiografia atual do banco de dados.
- **Documentação Automática**: Swagger UI nativo e interativo.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem principal.
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework moderno e de alta performance para a construção da API REST.
- **[LangChain](https://www.langchain.com/)** - Framework para orquestração da LLM e criação de prompts estruturados.
- **[Google Gemini](https://ai.google.dev/)** - Modelo fundacional de IA generativa (`gemini-1.5-flash`).
- **[Pandas](https://pandas.pydata.org/)** - Biblioteca para manipulação e análise de dados.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para comunicação com o banco de dados.
- **[SQLite](https://www.sqlite.org/)** - Banco de dados relacional.
- **[Faker](https://faker.readthedocs.io/)** - Geração de dados sintéticos para popular o banco em ambiente de testes.

---

## ⚙️ Como Executar na Sua Máquina

Siga os passos abaixo para testar a aplicação localmente:

### 1. Clone o repositório
```bash
git clone https://github.com/pedrodsilval/projeto-atendimentos-postecnico.git
cd projeto-atendimentos-postecnico
```

### 2. Crie e ative um Ambiente Virtual (Recomendado)
```bash
# No Windows:
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente
Copie o modelo de ambiente `.env.example` para `.env` e insira sua chave da API do Google Gemini (gratuita no [Google AI Studio](https://aistudio.google.com/)):
```bash
# No Windows (PowerShell):
cp .env.example .env

# No Linux/Mac:
cp .env.example .env
```
Edite o arquivo `.env`:
```env
GEMINI_API_KEY=sua_chave_aqui
```

### 5. Popule o Banco de Dados (Opcional, mas recomendado)
Para não começar com a aplicação vazia, utilize o script de *seed* que gera automaticamente dezenas de atendimentos realistas:
```bash
python seed.py
```

### 6. Inicie o Servidor da API
```bash
uvicorn main:app --reload
```
A API estará rodando no endereço: `http://127.0.0.1:8000`

### 7. Valide a Integração com IA (Opcional)
Execute o script automatizado para demonstrar o fluxo completo de IA em funcionamento:
```bash
python test_integracao_ia.py
```

---

## 📖 Como Usar a API

A documentação interativa da API já vem embutida! Com o servidor rodando, basta acessar o link abaixo no seu navegador para testar todos os *endpoints* visualmente:

🔗 **[Acessar Documentação Swagger UI](http://127.0.0.1:8000/docs)**

### Resumo dos Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/atendimentos/` | Lista todos os atendimentos cadastrados (suporta paginação). |
| `GET` | `/atendimentos/{id}` | Busca os detalhes de um atendimento específico. |
| `POST` | `/atendimentos/` | Cria um novo chamado de atendimento. |
| `PUT` | `/atendimentos/{id}` | Atualiza dados de um atendimento existente. |
| `DELETE`| `/atendimentos/{id}` | Remove um atendimento do banco de dados. |
| `GET` | `/relatorios/indicadores` | Retorna métricas gerenciais obrigatórias do projeto. |
| `GET` | `/relatorios/adicionais` | Retorna insights adicionais cruzando tempo, satisfação e volume. |
| `GET` | `/ai/relatorio` | **[IA]** Gera relatório executivo com recomendações a partir das métricas reais. |
| `GET` | `/ai/atendimento/{id}/analise` | **[IA]** Analisa ticket individual, gera diagnóstico, sentimento e minuta de resposta. |
| `POST` | `/ai/chat` | **[IA]** Chat interativo consultando os indicadores do banco de dados em tempo real. |

---

## 👨‍💻 Autor

Criado para o trabalho de conclusão da disciplina do Pós Técnico.
Sinta-se livre para explorar o código, enviar feedbacks ou clonar para os seus estudos!
