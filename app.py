from flask import Flask, jsonify
from config import db, app
from alunos.alunos_controller import alunos_blueprint
from professores.professores_controller import professores_blueprint
from turmas.turmas_controller import turmas_blueprint
from swagger.swagger_config import create_swagger

db.init_app(app)  # <-- IMPORTANTE

create_swagger(app)

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

@app.route('/')  # Adicionando a rota '/'
def home():
    return jsonify({"message": "API rodando!"}), 200

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)