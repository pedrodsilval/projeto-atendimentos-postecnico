import os
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from app.database import get_db
from app.models import Atendimento
from app.analytics import calcular_metricas_gerais, analises_adicionais
from app.schemas import (
    ChatRequest,
    RelatorioExecutivoResponse,
    AnaliseSentimentoResponse,
    ChatResponse
)

load_dotenv()

router = APIRouter(prefix="/ai", tags=["Inteligência Artificial Integrada"])

def extrair_texto(conteudo):
    """Extrai texto seguro da resposta da LLM, tratando retornos em string ou blocos de dicionário."""
    if isinstance(conteudo, list):
        partes = []
        for item in conteudo:
            if isinstance(item, dict) and "text" in item:
                partes.append(item["text"])
            elif isinstance(item, str):
                partes.append(item)
            elif hasattr(item, "text"):
                partes.append(getattr(item, "text"))
        return "".join(partes)
    return str(conteudo)

def get_llm():
    load_dotenv(override=True)
    chave = os.getenv("GEMINI_API_KEY")
    if not chave or chave in ["cole_sua_chave_aqui", "sua_chave_aqui"]:
        raise HTTPException(
            status_code=500, 
            detail="Chave da API do Gemini não configurada. Defina GEMINI_API_KEY no arquivo .env."
        )
    
    # Sobrescreve para garantir sincronia com a chave informada no .env
    os.environ["GOOGLE_API_KEY"] = chave
    
    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=chave,
        temperature=0.5
    )

@router.get("/relatorio", response_model=RelatorioExecutivoResponse, summary="Gera relatório executivo via IA")
def gerar_relatorio_estrategico(db: Session = Depends(get_db)):
    """Gera um relatório executivo com recomendações gerenciais baseadas nos dados reais"""
    llm = get_llm()
    metricas = calcular_metricas_gerais(db)
    adicionais = analises_adicionais(db)
    
    dados = {
        "metricas_gerais": metricas,
        "analises_estrategicas": adicionais
    }
    
    prompt = PromptTemplate.from_template(
        "Você é um consultor sênior de atendimento ao cliente. Analise os seguintes dados operacionais de um sistema de gestão:\n\n{dados}\n\n"
        "Com base unicamente nesses dados, crie um relatório executivo curto (máximo de 3 parágrafos) destacando:\n"
        "1. O que está indo bem (ex: atendente líder, categorias com bom desempenho).\n"
        "2. Os principais problemas, gargalos ou ofensores.\n"
        "3. Uma recomendação prática para os gestores."
    )
    
    chain = prompt | llm
    try:
        resposta = chain.invoke({"dados": json.dumps(dados, ensure_ascii=False)})
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Erro ao comunicar com a LLM: {str(e)}")
    
    texto = extrair_texto(resposta.content)
    return RelatorioExecutivoResponse(relatorio_executivo=texto)

@router.get("/atendimento/{id}/analise", response_model=AnaliseSentimentoResponse, summary="Análise de sentimento e diagnóstico de chamado")
def analisar_chamado(id: int, db: Session = Depends(get_db)):
    """Lê um chamado específico e gera análise de sentimento e sugestão de resposta"""
    llm = get_llm()
    atendimento = db.query(Atendimento).filter(Atendimento.id == id).first()
    
    if not atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
        
    dados_chamado = {
        "cliente": atendimento.cliente_nome,
        "categoria": atendimento.categoria,
        "descricao": atendimento.descricao,
        "status": atendimento.status,
        "duracao_minutos": atendimento.duracao_minutos,
        "satisfacao": atendimento.avaliacao_satisfacao
    }
    
    prompt = PromptTemplate.from_template(
        "Analise o seguinte chamado de atendimento:\n{dados}\n\n"
        "Responda DEVOLVENDO APENAS UM JSON VÁLIDO com as seguintes chaves:\n"
        "- \"sentimento\": O sentimento provável do cliente (Positivo, Neutro, Negativo ou Furioso).\n"
        "- \"analise\": Uma frase curta diagnosticando a situação.\n"
        "- \"sugestao_resposta\": Um rascunho educado do que o atendente deveria dizer ao cliente."
    )
    
    chain = prompt | llm
    try:
        resposta = chain.invoke({"dados": json.dumps(dados_chamado, ensure_ascii=False)})
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Erro ao comunicar com a LLM: {str(e)}")
    
    texto = extrair_texto(resposta.content).replace("```json", "").replace("```", "").strip()
    try:
        dados_json = json.loads(texto)
        return AnaliseSentimentoResponse(
            sentimento=dados_json.get("sentimento", "Neutro"),
            analise=dados_json.get("analise", "Diagnóstico concluído."),
            sugestao_resposta=dados_json.get("sugestao_resposta", "Olá! Como podemos ajudar?")
        )
    except Exception:
        return AnaliseSentimentoResponse(
            sentimento="Neutro",
            analise=texto,
            sugestao_resposta="Olá! Agradecemos pelo contato e estamos à disposição para sanar quaisquer dúvidas."
        )

@router.post("/chat", response_model=ChatResponse, summary="Chat interativo com os dados operacionais")
def chat_com_dados(req: ChatRequest, db: Session = Depends(get_db)):
    """Permite fazer perguntas livres e a IA responde consultando as métricas atuais"""
    llm = get_llm()
    metricas = calcular_metricas_gerais(db)
    adicionais = analises_adicionais(db)
    contexto = {
        "metricas_gerais": metricas,
        "analises_detalhadas": adicionais
    }
    
    prompt = PromptTemplate.from_template(
        "Você é o assistente virtual inteligente do nosso sistema de gestão de chamados. O usuário fará uma pergunta e você deve responder "
        "baseado estritamente no seguinte contexto de dados reais atualizados:\n"
        "Contexto atual dos dados: {dados}\n\n"
        "Pergunta do usuário: {pergunta}\n\n"
        "Responda de forma clara, prestativa e direta ao ponto."
    )
    
    chain = prompt | llm
    try:
        resposta = chain.invoke({
            "dados": json.dumps(contexto, ensure_ascii=False),
            "pergunta": req.pergunta
        })
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Erro ao comunicar com a LLM: {str(e)}")
    
    texto = extrair_texto(resposta.content)
    return ChatResponse(resposta_ia=texto)




