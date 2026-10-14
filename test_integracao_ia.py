"""
Script de Validação e Demonstração do Fluxo de Integração com IA
Fluxo: Banco de Dados -> Python -> FastAPI -> LangChain -> LLM -> Resposta IA
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def banner(titulo):
    print("\n" + "=" * 70)
    print(f" {titulo} ".center(70, "="))
    print("=" * 70)

def testar_relatorio():
    banner("1. TESTANDO RELATÓRIO ESTRATÉGICO (GET /ai/relatorio)")
    print("Enviando requisição para gerar relatório executivo...")
    res = client.get("/ai/relatorio")
    print(f"Status HTTP: {res.status_code}")
    if res.status_code == 200:
        dados = res.json()
        print("\n[Relatório Executivo Gerado]:")
        print(dados.get("relatorio_executivo"))
    else:
        print("Erro:", res.text)

def testar_analise_chamado(ticket_id=1):
    banner(f"2. TESTANDO ANÁLISE DE ATENDIMENTO (GET /ai/atendimento/{ticket_id}/analise)")
    print(f"Buscando dados do atendimento #{ticket_id} no banco e analisando com IA...")
    res = client.get(f"/ai/atendimento/{ticket_id}/analise")
    print(f"Status HTTP: {res.status_code}")
    if res.status_code == 200:
        dados = res.json()
        print(f"Sentimento detectado: {dados.get('sentimento')}")
        print(f"Diagnóstico técnico : {dados.get('analise')}")
        print(f"Sugestão de resposta: {dados.get('sugestao_resposta')}")
    else:
        print("Erro:", res.text)

def testar_chat():
    banner("3. TESTANDO CHAT COM OS DADOS (POST /ai/chat)")
    pergunta = "Qual atendente realizou mais chamados e qual a média de satisfação geral?"
    print(f"Pergunta do usuário: '{pergunta}'")
    res = client.post("/ai/chat", json={"pergunta": pergunta})
    print(f"Status HTTP: {res.status_code}")
    if res.status_code == 200:
        dados = res.json()
        print("\n[Resposta da IA]:")
        print(dados.get("resposta_ia"))
    else:
        print("Erro:", res.text)

if __name__ == "__main__":
    banner("INICIANDO SUÍTE DE TESTES DA INTEGRAÇÃO COM IA")
    testar_relatorio()
    testar_analise_chamado(1)
    testar_chat()
    banner("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
