from flask import Flask
from flask import render_template
from pessoa import Pessoa

app = Flask (
    __name__,
    static_folder = "static"
)

@app.route('/')
def index():
    PaginaInicial = render_template('index.html')
    return PaginaInicial


@app.route('/pagina1')
def pagina1():
    PaginaUm = render_template('pagina1.html')
    return PaginaUm


@app.route('/alunos')
def alunos():
    # nome_aluno = "Rodrigo"
    # curso_aluno = "ADS2C"
    # nota_aluno = 10
    # matricula_aluno = 2101648
    pessoa = Pessoa('Rodrigo', 2101648888, 'ADS2C', 10)
    
    return render_template (
        'aluno.html',
        obj = pessoa
        # nome = nome_aluno,
        # curso = curso_aluno,
        # nota = nota_aluno,
        # matricula = matricula_aluno
        
    )
    

app.run(debug=True)