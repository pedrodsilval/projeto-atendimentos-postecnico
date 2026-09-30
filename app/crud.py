from sqlalchemy.orm import Session
from app.models import Atendimento
from app.schemas import AtendimentoCreate, AtendimentoUpdate

def criar_atendimento(db: Session, atendimento: AtendimentoCreate):
    db_atendimento = Atendimento(**atendimento.model_dump())
    db.add(db_atendimento)
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento

def listar_atendimentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Atendimento).offset(skip).limit(limit).all()

def obter_atendimento_por_id(db: Session, atendimento_id: int):
    return db.query(Atendimento).filter(Atendimento.id == atendimento_id).first()

def atualizar_atendimento(db: Session, atendimento_id: int, dados_atualizacao: AtendimentoUpdate):
    db_atendimento = obter_atendimento_por_id(db, atendimento_id)
    if not db_atendimento:
        return None
    
    dados_dict = dados_atualizacao.model_dump(exclude_unset=True)
    for chave, valor in dados_dict.items():
        setattr(db_atendimento, chave, valor)
        
    db.commit()
    db.refresh(db_atendimento)
    return db_atendimento

def deletar_atendimento(db: Session, atendimento_id: int):
    db_atendimento = obter_atendimento_por_id(db, atendimento_id)
    if not db_atendimento:
        return None
    db.delete(db_atendimento)
    db.commit()
    return db_atendimento