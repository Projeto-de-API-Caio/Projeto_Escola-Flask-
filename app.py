from flask import Flask, jsonify
from config import db
from alunos.alunos_controller import alunos_blueprint
from professores.professores_controller import professores_blueprint
from turmas.turmas_controller import turmas_blueprint
from swagger.swagger_config import create_swagger


app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])