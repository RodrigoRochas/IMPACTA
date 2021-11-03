from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    

app.run(debug=True, port=5000)