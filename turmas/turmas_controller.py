from flask import Flask, jsonify, request, Blueprint    
from turmas import turmas_model as model

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route("/turmas", methods=["GET"])
def exibir_turmas():
    print("LISTA DE TODAS TURMAS:")
    return jsonify(model.getTurmas())

@turmas_blueprint.route("/turma/<int:id>", methods=["GET"])
def exibir_turma_por_id(id):
    resultado = model.obter_turma_por_id(id)
    return jsonify(resultado)

@turmas_blueprint.route("/turmas", methods=["POST"])
def criar_turma():
    dados = request.get_json()
    resultado, status = model.criarTurma(dados)
    return jsonify(resultado), status

@turmas_blueprint.route("/turmas/<int:idTurma>", methods=["PUT"])
def atualizar_turma(idTurma):
    dados = request.get_json()
    resultado, status = model.updateTurma(idTurma, dados)
    return jsonify(resultado), status

@turmas_blueprint.route("/turmas/<int:idTurma>", methods=["DELETE"])
def deletar_turma(idTurma):
    resultado, status = model.deleteTurma(idTurma)
    if status == 204:
        return '', 204
    return jsonify(resultado), status