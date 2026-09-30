from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import AtendimentoCreate, AtendimentoUpdate, AtendimentoResponse
from app import crud

router = APIRouter(prefix="/atendimentos", tags=["Gerenciamento de Atendimentos (CRUD)"])

@router.post("/", response_model=AtendimentoResponse, status_code=status.HTTP_201_CREATED)
def criar(atendimento: AtendimentoCreate, db: Session = Depends(get_db)):
    return crud.criar_atendimento(db, atendimento)

@router.get("/", response_model=List[AtendimentoResponse])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.listar_atendimentos(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=AtendimentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    registro = crud.obter_atendimento_por_id(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado.")
    return registro

@router.put("/{id}", response_model=AtendimentoResponse)
def atualizar(id: int, dados: AtendimentoUpdate, db: Session = Depends(get_db)):
    registro = crud.atualizar_atendimento(db, id, dados)
    if not registro:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado.")
    return registro

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def remover(id: int, db: Session = Depends(get_db)):
    registro = crud.deletar_atendimento(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado.")
    return {"mensagem": f"Atendimento #{id} excluído com sucesso."}