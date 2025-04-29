from config import db

class TurmaNaoIdentificada(Exception):
    pass

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    professor = db.relationship('Professor', back_populates='turmas')
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    aluno = db.relationship('Aluno', back_populates='turmas')

    def __init__(self, descricao, professor_id, ativo=True):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }

def getTurmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas], 200

def obter_turma_por_id(id):
    turma = Turma.query.get(id)
    if not turma:
        raise TurmaNaoIdentificada(f"Turma com ID {id} não encontrada.")
    return turma.to_dict(), 200

def criarTurma(dados):
    try:
        descricao = dados['descricao']
        professor_id = dados['professor_id']
        ativo = dados.get('ativo', True)

        turma = Turma(descricao=descricao, professor_id=professor_id, ativo=ativo)

        db.session.add(turma)
        db.session.commit()

        return turma.to_dict(), 201
    except KeyError as e:
        return {"erro": f"Campo obrigatório ausente: {str(e)}"}, 400

def updateTurma(idTurma, dados):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmaNaoIdentificada(f"Turma com ID {idTurma} não encontrada.")

    if 'descricao' in dados:
        turma.descricao = dados['descricao']
    if 'professor_id' in dados:
        turma.professor_id = dados['professor_id']
    if 'ativo' in dados:
        turma.ativo = dados['ativo']

    db.session.commit()
    return turma.to_dict(), 200

def deleteTurma(idTurma):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmaNaoIdentificada(f"Turma com ID {idTurma} não encontrada.")

    db.session.delete(turma)
    db.session.commit()
    return '', 204