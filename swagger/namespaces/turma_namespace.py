from flask_restx import Namespace, Resource, fields
from turmas.turmas_model import (
    getTurmas,
    obter_turma_por_id,
    criarTurma,
    updateTurma,
    deleteTurma,
    TurmaNaoIdentificada
)

turmas_ns = Namespace('turmas', description='Operações relacionadas às turmas')

# Modelo para documentação Swagger
turma_model = turmas_ns.model('Turma', {
    'id': fields.Integer(description='ID da turma', example=1),
    'descricao': fields.String(required=True, description='Descrição da turma', example='Turma A'),
    'ativo': fields.Boolean(description='Status de ativação da turma', example=True),
    'professor_id': fields.Integer(required=True, description='ID do professor responsável', example=1)
})

@turmas_ns.route('/')
class TurmasList(Resource):
    @turmas_ns.marshal_list_with(turma_model)
    def get(self):
        """Listar todas as turmas"""
        return getTurmas()

    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model, code=201)
    def post(self):
        """Criar uma nova turma"""
        return criarTurma(turmas_ns.payload)

@turmas_ns.route('/<int:id>')
@turmas_ns.param('id', 'ID da turma')
class TurmaResource(Resource):
    @turmas_ns.marshal_with(turma_model)
    def get(self, id):
        """Obter uma turma pelo ID"""
        try:
            return obter_turma_por_id(id)
        except TurmaNaoIdentificada as e:
            return {"erro": str(e)}, 404

    @turmas_ns.expect(turma_model, validate=True)
    @turmas_ns.marshal_with(turma_model)
    def put(self, id):
        """Atualizar os dados de uma turma"""
        try:
            return updateTurma(id, turmas_ns.payload)
        except TurmaNaoIdentificada as e:
            return {"erro": str(e)}, 404

    def delete(self, id):
        """Excluir uma turma"""
        try:
            return deleteTurma(id)
        except TurmaNaoIdentificada as e:
            return {"erro": str(e)}, 404