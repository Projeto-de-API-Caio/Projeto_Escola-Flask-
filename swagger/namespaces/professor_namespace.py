from flask_restx import Namespace, Resource, fields
from professores.professores_model import (
    getProfessores,
    obter_professor_por_id,
    criarProfessor,
    updateProfessor,
    deleteProfessor,
    ProfessorNaoIdentificado
)

professores_ns = Namespace('professores', description='Operações relacionadas aos professores')

professor_input = professores_ns.model('ProfessorInput', {
    'nome': fields.String(required=True, description='Nome do professor', example='Carlos'),
    'idade': fields.Integer(required=True, description='Idade do professor', example=40),
    'materia': fields.String(required=True, description='Matéria lecionada', example='Matemática'),
    'observacoes': fields.String(description='Observações adicionais', example='Especialista em álgebra')
})

professor_output = professores_ns.inherit('Professor', professor_input, {
    'id': fields.Integer(description='ID do professor', example=1)
})

@professores_ns.route('/')
class ProfessoresList(Resource):
    @professores_ns.marshal_list_with(professor_output)
    def get(self):
        """Listar todos os professores"""
        professores, _ = getProfessores()
        return professores

    @professores_ns.expect(professor_input, validate=True)
    @professores_ns.marshal_with(professor_output, code=201)
    def post(self):
        """Criar um novo professor"""
        professor, status_code = criarProfessor(professores_ns.payload)
        return professor, status_code

@professores_ns.route('/<int:id>')
@professores_ns.param('id', 'ID do professor')
class ProfessorResource(Resource):
    @professores_ns.marshal_with(professor_output)
    def get(self, id):
        """Obter um professor pelo ID"""
        try:
            professor, status = obter_professor_por_id(id)
            return professor, status
        except ProfessorNaoIdentificado as e:
            return {"erro": str(e)}, 404

    @professores_ns.expect(professor_input, validate=True)
    @professores_ns.marshal_with(professor_output)
    def put(self, id):
        """Atualizar os dados de um professor"""
        try:
            professor, status = updateProfessor(id, professores_ns.payload)
            return professor, status
        except ProfessorNaoIdentificado as e:
            return {"erro": str(e)}, 404

    def delete(self, id):
        """Excluir um professor"""
        try:
            _, status = deleteProfessor(id)
            return '', status
        except ProfessorNaoIdentificado as e:
            return {"erro": str(e)}, 404