from fastapi import FastAPI
from app.database import engine, Base
from app.routers import atendimentos, relatorios

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestão e Análise de Atendimentos",
    description="API REST desenvolvida com FastAPI, SQLAlchemy e Pandas.",
    version="1.0.0"
)

app.include_router(atendimentos.router)
app.include_router(relatorios.router)

@app.get("/", tags=["Health Check"])
def raiz():
    return {
        "status": "Online",
        "docs": "Acesse http://127.0.0.1:8000/docs para explorar os endpoints interativos."
    }