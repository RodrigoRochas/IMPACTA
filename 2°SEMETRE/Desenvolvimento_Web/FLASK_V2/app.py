from flask import Flask
from flask import render_template, request
from pessoa import Pessoa

app = Flask (
    __name__,
    static_folder = "static"
)

@app.route('/index/<int:matricula>')
def index(matricula):
    return f'O valor recevido e {matricula}'

@app.route('/pagina')
def recebe_params():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    if nome is None or idade is None:
        return render_template('form.html')
    else:
        return f'O nome é {nome} e a idade é {idade}'

@app.route('/form')
def formulario():
    return render_template('form.html')
    
    
    
# @app.route('/pagina1')
# def pagina1():
#     PaginaUm = render_template('pagina1.html')
#     return PaginaUm


# @app.route('/alunos')
# def alunos():
#     # nome_aluno = "Rodrigo"
#     # curso_aluno = "ADS2C"
#     # nota_aluno = 10
#     # matricula_aluno = 2101648
#     pessoa = Pessoa('Rodrigo', 2101648888, 'ADS2C', 10)
    
#     return render_template (
#         'aluno.html',
#         obj = pessoa
#         # nome = nome_aluno,
#         # curso = curso_aluno,
#         # nota = nota_aluno,
#         # matricula = matricula_aluno
        
#     )
    

app.run(debug=True)