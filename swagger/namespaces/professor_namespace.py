from flask_restx import Namespace, Resource, fields

# Criando o namespace para professores
professores_ns = Namespace('professores', description='Operações relacionadas aos professores')

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos")

# Definindo os endpoints para o namespace 'professores'
@professores_ns.route('/')
class ProfessoresList(Resource):
    def get(self):
        """
        Listar todos os professores
        """
        return {"message": "Lista de todos os professores."}

@professores_ns.route('/<int:id>')
class Professor(Resource):
    def get(self, id):
        """
        Obter detalhes de um professor específico
        """
        return {"message": f"Detalhes do professor {id}."}