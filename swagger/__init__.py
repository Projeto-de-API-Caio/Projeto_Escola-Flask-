from flask_restx import Api

api = Api(
    version='1.0',
    title='API Escola',
    description='Uma API para gestão de alunos, professores e turmas',
    doc='/swagger', 
    mask_swagger=False, #desativa o x-field no swagger,
)