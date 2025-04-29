from flask_restx import Namespace, Resource, fields
from alunos.alunos_model import Aluno  # Importando o modelo de aluno para integração com o banco
from config import db


alunos_ns = Namespace('alunos', description='Operações relacionadas aos alunos')


aluno_model = alunos_ns.model('Aluno', {
    'id': fields.Integer(description='ID do aluno', required=True),
    'nome': fields.String(description='Nome do aluno', required=True),
    'idade': fields.Integer(description='Idade do aluno', required=True),
    'data_nascimento': fields.String(description='Data de nascimento do aluno', required=True),
    'nota_primeiro_semestre': fields.Float(description='Nota do primeiro semestre', required=True),
    'nota_segundo_semestre': fields.Float(description='Nota do segundo semestre', required=True),
    'media_final': fields.Float(description='Média final do aluno', required=True)
})

@alunos_ns.route('/')
class AlunosList(Resource):
    @alunos_ns.marshal_list_with(aluno_model)
    def get(self):
        """
        Listar todos os alunos
        """
        alunos = Aluno.query.all()  
        return alunos  

@alunos_ns.route('/<int:id>')
class Aluno(Resource):
    @alunos_ns.marshal_with(aluno_model)
    def get(self, id):
        """
        Obter detalhes de um aluno específico
        """
        aluno = Aluno.query.get_or_404(id)  
        return aluno