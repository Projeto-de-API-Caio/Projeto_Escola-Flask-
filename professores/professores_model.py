from config import db
from datetime import datetime, date

class ProfessorNaoIdentificado(Exception):
    pass

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.String(100))

    turmas = db.relationship('Turma', back_populates='professor')

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

def getProfessores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores], 200
    
def obter_professor_por_id(id):
    professor = Professor.query.get(id)
    if not professor:
        raise ProfessorNaoIdentificado(f"Professor com ID {id} não encontrado.")
    return professor.to_dict(), 200

def criarProfessor(dados):
    try:
        nome = dados['nome']
        idade = dados['idade']
        materia = dados['materia']
        observacoes = dados.get('observacoes')

        professor = Professor(nome=nome, idade=idade, materia=materia, observacoes=observacoes)

        db.session.add(professor)
        db.session.commit()

        return professor.to_dict(), 201
    except KeyError as e:
        return {"erro": f"Campo obrigatório ausente: {str(e)}"}, 400

def updateProfessor(idProfessor, dados):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoIdentificado(f"Professor com ID {idProfessor} não encontrado.")

    if 'nome' in dados:
        professor.nome = dados['nome']
    if 'idade' in dados:
        professor.idade = dados['idade']
    if 'materia' in dados:
        professor.materia = dados['materia']
    if 'observacoes' in dados:
        professor.observacoes = dados['observacoes']

    db.session.commit()
    return professor.to_dict(), 200

def deleteProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoIdentificado(f"Professor com ID {idProfessor} não encontrado.")

    db.session.delete(professor)
    db.session.commit()
    return '', 204