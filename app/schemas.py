from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AtendimentoBase(BaseModel):
    cliente_nome: str
    categoria: str
    atendente: str
    status: str = "aberto"
    descricao: Optional[str] = None
    duracao_minutos: float = Field(ge=0, description="Duração em minutos")
    avaliacao_satisfacao: Optional[int] = Field(None, ge=1, le=5)

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoUpdate(BaseModel):
    cliente_nome: Optional[str] = None
    categoria: Optional[str] = None
    atendente: Optional[str] = None
    status: Optional[str] = None
    descricao: Optional[str] = None
    duracao_minutos: Optional[float] = None
    avaliacao_satisfacao: Optional[int] = None

class AtendimentoResponse(AtendimentoBase):
    id: int
    data_atendimento: datetime

    class Config:
        from_attributes = True