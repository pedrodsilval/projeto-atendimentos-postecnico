import random
from datetime import datetime, timedelta
from faker import Faker
from app.database import SessionLocal, engine, Base
from app.models import Atendimento

fake = Faker("pt_BR")

CATEGORIAS = ["Suporte Técnico", "Financeiro", "Comercial", "Reclamação", "Cancelamento"]
ATENDENTES = ["Ana Beatriz", "Carlos Eduardo", "Mariana Silva", "Rodrigo Costa", "Juliana Lima"]
STATUS_LIST = ["concluido", "concluido", "concluido", "em_andamento", "aberto", "cancelado"]

def popular_banco(total_registros: int = 80):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print(f"Gerando {total_registros} atendimentos simulados...")
    for _ in range(total_registros):
        status_escolhido = random.choice(STATUS_LIST)
        duracao = round(random.uniform(3.5, 45.0), 1)
        avaliacao = random.randint(1, 5) if status_escolhido == "concluido" else (random.randint(1, 3) if status_escolhido == "cancelado" else None)
        
        data_aleatoria = datetime.utcnow() - timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 8),
            minutes=random.randint(0, 59)
        )

        novo = Atendimento(
            cliente_nome=fake.name(),
            categoria=random.choice(CATEGORIAS),
            atendente=random.choice(ATENDENTES),
            data_atendimento=data_aleatoria,
            status=status_escolhido,
            descricao=fake.sentence(nb_words=8),
            duracao_minutos=duracao,
            avaliacao_satisfacao=avaliacao
        )
        db.add(novo)

    db.commit()
    db.close()
    print("Base populada com sucesso!")

if __name__ == "__main__":
    popular_banco()