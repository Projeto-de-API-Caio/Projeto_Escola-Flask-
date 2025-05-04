from flask import Flask, jsonify, request, Blueprint    
from professores import professores_model as model

professores_blueprint = Blueprint('professores',__name__)

@professores_blueprint.route("/professores", methods=["GET"])
def exibir_professores():
    print("LISTA DE TODOS PROFESSORES:")
    return jsonify(model.getProfessores())

@professores_blueprint.route("/professores/<int:id>", methods=["GET"])
def exibir_professor_por_id(id):
    professor , status = model.obter_professor_por_id(id)
    if status != 200:
        return jsonify({"error": "Professor não encontrado"}), 400
    return jsonify(professor)

@professores_blueprint.route("/professores", methods=["POST"])
def criar_professor():
    print("CRIANDO PROFESSOR!")
    dados = request.json
    professor , status = model.criarProfessor(dados)
    return jsonify(professor), status

@professores_blueprint.route("/professores/<int:idProfessor>", methods=["PUT"])
def atualizar_professor(idProfessor):
    dados = request.get_json()
    professor , status = model.updateProfessor(idProfessor, dados)
    return jsonify(professor), status

@professores_blueprint.route("/professores/<int:idProfessor>", methods=["DELETE"])
def deletar_professor(idProfessor):
    professor , status = model.deleteProfessor(idProfessor)
    return jsonify(professor), status

