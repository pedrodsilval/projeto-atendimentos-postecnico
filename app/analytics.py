import pandas as pd
from sqlalchemy.orm import Session
from app.models import Atendimento

def get_dataframe(db: Session) -> pd.DataFrame:
    query = db.query(Atendimento).statement
    df = pd.read_sql(query, con=db.bind)
    return df

def calcular_metricas_gerais(db: Session) -> dict:
    df = get_dataframe(db)
    if df.empty:
        return {"mensagem": "Sem registros para análise."}

    atendentes_contagem = df["atendente"].value_counts()
    melhor_atendente = atendentes_contagem.index[0] if not atendentes_contagem.empty else None

    df_avaliados = df.dropna(subset=["avaliacao_satisfacao"])
    maiores_avaliacoes = (
        df_avaliados[df_avaliados["avaliacao_satisfacao"] == df_avaliados["avaliacao_satisfacao"].max()][["id", "cliente_nome", "avaliacao_satisfacao"]].to_dict(orient="records")
        if not df_avaliados.empty else []
    )
    menores_avaliacoes = (
        df_avaliados[df_avaliados["avaliacao_satisfacao"] == df_avaliados["avaliacao_satisfacao"].min()][["id", "cliente_nome", "avaliacao_satisfacao"]].to_dict(orient="records")
        if not df_avaliados.empty else []
    )

    return {
        "total_atendimentos": int(len(df)),
        "por_categoria": df["categoria"].value_counts().to_dict(),
        "por_status": df["status"].value_counts().to_dict(),
        "por_atendente": df["atendente"].value_counts().to_dict(),
        "atendente_lider": melhor_atendente,
        "tempo_medio_minutos": round(float(df["duracao_minutos"].mean()), 2),
        "media_satisfacao": round(float(df["avaliacao_satisfacao"].mean()), 2) if not df_avaliados.empty else None,
        "maiores_avaliacoes": maiores_avaliacoes,
        "menores_avaliacoes": menores_avaliacoes,
    }

def analises_adicionais(db: Session) -> dict:
    df = get_dataframe(db)
    if df.empty:
        return {"mensagem": "Sem registros para análise."}

    df["data_atendimento"] = pd.to_datetime(df["data_atendimento"])
    
    tempo_por_cat = df.groupby("categoria")["duracao_minutos"].mean().round(2).to_dict()
    satisfacao_por_atendente = df.groupby("atendente")["avaliacao_satisfacao"].mean().round(2).dropna().to_dict()
    df["dia_semana"] = df["data_atendimento"].dt.day_name()
    volume_por_dia = df["dia_semana"].value_counts().to_dict()

    return {
        "tempo_medio_por_categoria": tempo_por_cat,
        "satisfacao_media_por_atendente": satisfacao_por_atendente,
        "volume_por_dia_semana": volume_por_dia
    }