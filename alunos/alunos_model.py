from config import db
from datetime import datetime, date
from turmas.turmas_model import Turma


class AlunoNaoIdentificado(Exception):
    pass

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Numeric(5, 2), nullable=False)

    turma = db.relationship("Turma", back_populates="aluno")
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.nome = nome
        self.idade = self.calcular_idade() 
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = round((nota_primeiro_semestre + nota_segundo_semestre) / 2, 2)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento.isoformat(),
            'nota_primeiro_semestre': float(self.nota_primeiro_semestre),
            'nota_segundo_semestre': float(self.nota_segundo_semestre),
            'media_final': float(self.media_final)
        }

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

def getAlunos():
        alunos = Aluno.query.all()
        return [aluno.to_dict() for aluno in alunos], 200
        
def obter_aluno_por_id(id):
    try:
        aluno = Aluno.query.get(id)
        if not aluno:
            raise AlunoNaoIdentificado(f"Aluno com ID {id} não encontrado.")
        return aluno.to_dict(), 200
    except AlunoNaoIdentificado as e:
        return {"erro": str(e)}, 404
        
def criarAluno(dados):
    
    try:
        nome = dados['nome']
        idade = dados.get('idade')
        turma_id = dados.get('turma_id')
        data_nascimento = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()
        nota1 = float(dados['nota_primeiro_semestre'])
        nota2 = float(dados['nota_segundo_semestre'])


        turma = Turma.query.get(dados['turma_id'])
        if turma is None:
            return {"messege": "Turma não existe"}

        aluno = Aluno(nome, idade, turma_id, data_nascimento, nota1, nota2)

        db.session.add(aluno)
        db.session.commit()

        return aluno.to_dict(), 201
    except KeyError as e:
        return {"erro": f"Campo obrigatório ausente: {str(e)}"}, 400
        
def updateAluno(idAluno, dados):
    try:
        aluno = Aluno.query.get(idAluno)
        if not aluno:
            raise AlunoNaoIdentificado(f"Aluno com ID {idAluno} não encontrado.")

        if 'nome' in dados:
            aluno.nome = dados['nome']
        if 'idade' in dados:
            aluno.idade = dados['idade']
        if 'turma_id' in dados:
            aluno.turma_id = dados['turma_id']
        if 'data_nascimento' in dados:
            aluno.data_nascimento = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()
        if 'nota_primeiro_semestre' in dados:
            aluno.nota_primeiro_semestre = float(dados['nota_primeiro_semestre'])
        if 'nota_segundo_semestre' in dados:
            aluno.nota_segundo_semestre = float(dados['nota_segundo_semestre'])

        aluno.media_final = round((aluno.nota_primeiro_semestre + aluno.nota_segundo_semestre) / 2, 2)

        db.session.commit()
        return aluno.to_dict(), 200
    except AlunoNaoIdentificado as e:
        return {"erro": str(e)}, 404
        
def deleteAluno(idAluno):
    try:
        aluno = Aluno.query.get(idAluno)
        if not aluno:
            raise AlunoNaoIdentificado(f"Aluno com ID {idAluno} não encontrado.")

        db.session.delete(aluno)
        db.session.commit()
        return '', 204
    except AlunoNaoIdentificado as e:
        return {"erro": str(e)}, 404