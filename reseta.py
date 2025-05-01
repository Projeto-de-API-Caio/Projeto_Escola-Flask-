from config import db
from app import app


def reseta_banco():
    try:
        with app.app_context():
            db.session.query(db.Model).delete()
            db.session.commit()
        print("Dados resetados com sucesso!")
    except Exception as e:
        print(f"Não foi possível resetar o banco. Erro: {e}")

reseta_banco()
             
    