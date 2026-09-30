from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from app.database import Base

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente_nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    atendente = Column(String(100), nullable=False)
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    status = Column(String(30), default="aberto")
    descricao = Column(String(255), nullable=True)
    duracao_minutos = Column(Float, nullable=False, default=0.0)
    avaliacao_satisfacao = Column(Integer, nullable=True)