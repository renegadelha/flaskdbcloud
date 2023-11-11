#https://freefrontend.com/assets/zip/css-login-forms/sign-up-login-form.zip
#local onde peguei o free html+css

from flask import *
from dao import *

from decouple import config

app = Flask(__name__)
app.secret_key = config("SECRET_KEY")
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cadastrarnoticia")
def cadastrarNoticia():
    return render_template('cadastrarnoticia.html')


@app.route("/listarnoticia")
def listarnoticia():

    id_usuario = session['id']
    conexao = conectardb()
    tupla = listarnoticiasUsuario(conexao, id_usuario)

    print(tupla)

    return render_template('listarnoticias.html', listanoticias=tupla, usuario=session['usuario'])



@app.route("/inserirnoticia", methods=['POST'])
def inserirnoticia():
    titulo = str(request.form.get('titulo'))
    texto = str(request.form.get('texto'))
    id_usuario = session['id']

    conexao = conectardb()
    if cadastrarNoticiaDB(titulo, texto, id_usuario, conexao):
        return render_template('menu.html')
    else:
        return 'deu tudo errado ao inserir noticia'

@app.route("/login", methods=["POST"])
def login():

    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))

    conexao = conectardb()
    tupla = listarUsuarios(conexao)

    for usuario in tupla:
        if(login == usuario[2] and senha == usuario[3]):
            session['id'] = usuario[0]
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