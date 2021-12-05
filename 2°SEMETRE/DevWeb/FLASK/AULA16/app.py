from flask import render_template, request, Flask, session

app = Flask(__name__)
app.secret_key = 'CHAVE-MUITO-SECRETA'

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario == 'rodrigo' and senha == '1234':
            session['usuario'] == 'rodrigo'
        elif usuario == 'maria' and senha == '1111':
            session['usuario'] == 'maria'
        else:
            msg_erro = 'USUÁRIO OU SENHA INVALIDOS, TENTE NOVAMNETE'
        
    
    return render_template('index.html', erro = msg_erro)

app.run(debug=True)