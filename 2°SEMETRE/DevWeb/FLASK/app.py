from flask import Flask
from flask import render_template
from pessoa import Pessoa

app = Flask (
    __name__, 
    template_folder = "meu_modelo",
    static_folder = "static",   
)

@app.route('/')
def index():
    resposta = render_template('index.html')
    return resposta

@app.route('/alunos')
def aluno():
    # teste = Pessoa('RRS', 14122, 'ADS', 10)
    # pessoa = {'nome' : 'Rodrigo', 'matricula': 123456, 'curso' : 'ADS-2021'}
    nome_aluno = "Rodrigo"
    matricula_aluno = 123
    curso_aluno = "ADS"
    nota_curso = 2  
    
    return render_template (
        'aluno.html', 
        # objeto = teste
        # dados = pessoa
        nome = nome_aluno,
        matricula = matricula_aluno,
        curso = curso_aluno,
        nota = nota_curso
        
    )
    
    
    
@app.errorhandler(404)
def error404(e):
    return render_template('erro.html'), 404
    


app.run(debug=True)




























# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def ola():
#     hello = "Hello World"
    
#     return hello

# @app.route('/outra_rota')
# def outra_rota():
#     resposta = '<a href="/">Clique aqui para voltar</a>'
    
#     return resposta


# @app.route('/curso/<nome_curso>')
# def curso(nome_curso):
#     if nome_curso == 'devweb':
#         return "Pagina de DEVWEB"
    
#     elif nome_curso == 'POO':
#         return "Pagina d POO"
    
#     elif nome_curso == 'BD':
#         return "Pagiande de BD"
    
#     else:
#         return "Pagina inexistente"
    
    
# @app.route('/exemplo/<int:numero>')
# def numero(numero):
#     req = "O ano indicado é : " + str(numero)
    
#     return req
    
# @app.route('/curso/cursoBD')
# def curso2():
#     msg1 = "Pagina de curso de BD"
    
#     return msg1


# @app.route('/curso/cursoPOO')
# def curso3():
#     msg2 = "Pagina de curso POO"
    
#     return msg2
    

# app.run(debug=True, port=5000)