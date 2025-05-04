from flask import Flask, jsonify, request, Blueprint
from alunos import alunos_model as model


alunos_blueprint = Blueprint('alunos',__name__)

@alunos_blueprint.route("/alunos", methods=["GET"])
def exibir_alunos():
    print("LISTA DE TODOS ALUNOS:")
    alunos, status = model.getAlunos()
    return jsonify(alunos), status 

@alunos_blueprint.route("/alunos/<int:id>", methods=["GET"])
def exibir_alunos_por_id(id):
    aluno, status = model.obter_aluno_por_id(id)
    return jsonify(aluno), status
    
@alunos_blueprint.route("/alunos", methods=["POST"])
def criar_aluno():
    print("CRIANDO ALUNO!")
    dados = request.json
    aluno, status = model.criarAluno(dados)
    return jsonify(aluno), status

@alunos_blueprint.route("/alunos/<int:idAluno>", methods=["PUT"])
def atualizar_aluno(idAluno):
    dados = request.json
    aluno, status = model.updateAluno(idAluno, dados)
    return jsonify(aluno), status

@alunos_blueprint.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deletar_aluno(idAluno):
    resposta, status = model.deleteAluno(idAluno)
    return (jsonify(resposta), status) if resposta else ('', status)