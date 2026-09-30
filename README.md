<h1 align="center">
  📊 Sistema de Gestão e Análise de Atendimentos
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

<p align="center">
  <strong>Projeto Final</strong> desenvolvido para o curso de Pós Técnico. Uma API REST completa para registro, gerenciamento e extração de insights (análise de dados) sobre atendimentos ao cliente.
</p>

---

## 🚀 O Projeto

O objetivo deste projeto é aplicar de maneira integrada os conhecimentos de **Desenvolvimento Back-end**, **Bancos de Dados Relacionais** e **Análise de Dados**. A aplicação simula o sistema interno de uma empresa para controlar os tickets de suporte, oferecendo desde operações de CRUD até relatórios analíticos complexos calculados em tempo real.

### ✨ Principais Funcionalidades

- **CRUD de Atendimentos**: Cadastro, leitura, atualização e exclusão de tickets com validação de dados via Pydantic.
- **Armazenamento Persistente**: Integração com banco de dados relacional via SQLAlchemy.
- **Análise de Dados (Data Science)**: Utilização do **Pandas** para cruzar métricas e identificar padrões:
  - Distribuição de atendimentos por categoria e status.
  - Avaliação de desempenho dos atendentes (quem atende mais, quem tem a melhor avaliação).
  - Cálculo de tempo médio de resolução e cruzamento por categoria.
  - Mapeamento de volume de chamados por dia da semana.
- **Documentação Automática**: Swagger UI nativo e interativo.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem principal.
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework moderno e de alta performance para a construção da API REST.
- **[Pandas](https://pandas.pydata.org/)** - Biblioteca poderosa para manipulação e análise exploratória de dados.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para comunicação segura e eficiente com o banco de dados.
- **[SQLite](https://www.sqlite.org/)** - Banco de dados relacional (escolhido para facilitar testes e portabilidade).
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

### 4. Popule o Banco de Dados (Opcional, mas recomendado)
Para não começar com a aplicação vazia, criamos um script de *seed* que gera automaticamente dezenas de atendimentos realistas.
```bash
python seed.py
```

### 5. Inicie o Servidor da API
```bash
uvicorn main:app --reload
```
A API estará rodando no endereço: `http://127.0.0.1:8000`

---

## 📖 Como Usar a API

A documentação interativa da API já vem embutida! Com o servidor rodando, basta acessar o link abaixo no seu navegador para testar todos os *endpoints* (rotas) visualmente:

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

---

## 👨‍💻 Autor

Criado para o trabalho de conclusão da disciplina do Pós Técnico.
Sinta-se livre para explorar o código, enviar feedbacks ou clonar para os seus estudos!
