from flask_restx import Namespace, Resource

# Criando o namespace para turmas
turmas_ns = Namespace('turmas', description='Operações relacionadas às turmas')

# Definindo os endpoints para o namespace 'turmas'
@turmas_ns.route('/')
class TurmasList(Resource):
    def get(self):
        """
        Listar todas as turmas
        """
        return {"message": "Lista de todas as turmas."}

@turmas_ns.route('/<int:id>')
class Turma(Resource):
    def get(self, id):
        """
        Obter detalhes de uma turma específica
        """
        return {"message": f"Detalhes da turma {id}."}