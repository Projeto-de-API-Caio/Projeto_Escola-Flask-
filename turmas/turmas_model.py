from config import db

escola = {
    "alunos": [],
    "professores": [],
    "turmas": []
}


class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    ativo = db.Column(db.Boolean, default=True, nullable=False)

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

class TurmaNaoIdentificada(Exception):
    print("Turma não identificada")

def getTurmas():
    return escola["turmas"]

def obter_turma_por_id(id):
    for turma in escola["turmas"]:
        if turma["id"] == id:
            return turma
    return {"erro": "turma nao encontrada"}, 404

def criarTurma(dados):
    if "id" not in dados or "nome" not in dados or "alunos" not in dados:
        return {"erro": "informacoes incompletas para criar turma"}, 400
    
    nova_turma = {
        "id": dados["id"],
        "nome": dados["nome"],
        "alunos": dados["alunos"]
    }
    escola["turmas"].append(nova_turma)
    return nova_turma, 201

def updateTurma(idTurma, dados):
    for turma in escola["turmas"]:
        if turma["id"] == idTurma:
            if "nome" in dados:
                turma["nome"] = dados["nome"]
            if "alunos" in dados:
                turma["alunos"] = dados["alunos"]
            return turma, 200
    return {"erro": "turma nao encontrada"}, 404

def deleteTurma(idTurma):
    turma_existe = any(turma["id"] == idTurma for turma in escola["turmas"])
    if not turma_existe:
        return {"erro": "turma nao encontrada"}, 404

    escola["turmas"] = [turma for turma in escola["turmas"] if turma["id"] != idTurma]
    return '', 204
