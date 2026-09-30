from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.analytics import calcular_metricas_gerais, analises_adicionais

router = APIRouter(prefix="/relatorios", tags=["Análise de Dados (Pandas)"])

@router.get("/indicadores")
def obter_indicadores_obrigatorios(db: Session = Depends(get_db)):
    return calcular_metricas_gerais(db)

@router.get("/adicionais")
def obter_analises_adicionais(db: Session = Depends(get_db)):
    return analises_adicionais(db)