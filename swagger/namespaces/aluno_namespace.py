from flask_restx import Namespace, Resource, fields
from alunos.alunos_model import Aluno, criarAluno, updateAluno, deleteAluno, AlunoNaoIdentificado
from config import db

alunos_ns = Namespace('alunos', description='Operações relacionadas aos alunos')

aluno_model = alunos_ns.model('Aluno', {
    'id': fields.Integer(readOnly=True, description='ID do aluno'),
    'nome': fields.String(required=True, description='Nome do aluno'),
    'idade': fields.Integer(description='Idade do aluno'),
    'data_nascimento': fields.String(required=True, description='Data de nascimento (YYYY-MM-DD)'),
    'nota_primeiro_semestre': fields.Float(required=True, description='Nota do 1º semestre'),
    'nota_segundo_semestre': fields.Float(required=True, description='Nota do 2º semestre'),
    'media_final': fields.Float(description='Média final do aluno')
})

@alunos_ns.route('/')
class AlunosList(Resource):
    @alunos_ns.marshal_list_with(aluno_model)
    def get(self):
        """Listar todos os alunos"""
        alunos = Aluno.query.all()
        return [aluno.to_dict() for aluno in alunos]

    @alunos_ns.expect(aluno_model)
    @alunos_ns.marshal_with(aluno_model, code=201)
    def post(self):
        """Criar um novo aluno"""
        dados = alunos_ns.payload
        aluno, status = criarAluno(dados)
        return aluno, status


@alunos_ns.route('/<int:id>')
class AlunoDetail(Resource):
    @alunos_ns.marshal_with(aluno_model)
    def get(self, id):
        """Obter detalhes de um aluno específico"""
        aluno = Aluno.query.get_or_404(id)
        return aluno.to_dict()

    @alunos_ns.expect(aluno_model)
    @alunos_ns.marshal_with(aluno_model)
    def put(self, id):
        """Atualizar um aluno existente"""
        dados = alunos_ns.payload
        aluno, status = updateAluno(id, dados)
        return aluno, status

    def delete(self, id):
        """Remover um aluno"""
        resposta, status = deleteAluno(id)
        return resposta, status