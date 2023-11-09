#https://freefrontend.com/assets/zip/css-login-forms/sign-up-login-form.zip
#local onde peguei o free html+css

from flask import *
from dao import *

app = Flask(__name__)
app.secret_key = 'ajshdgah123'
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))

    conexao = conectardb()
    tupla = listarUsuarios(conexao)


    for usuario in tupla:
        if(login == usuario[0] and senha == usuario[1]):
            session['usuario'] = login
            return render_template('menu.html', usuario=login)

    return render_template('errologin.html')


@app.route("/cadastrar", methods=["POST"])
def cadastrarusuario():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))
    nome = str(request.form.get('txt'))

    conexao = conectardb()
    if inserirDB(login, senha, nome, conexao):
        return render_template('index.html')
    else:
        return render_template('errocadastro.html')


if __name__ == "__main__":
    app.run(debug=True)