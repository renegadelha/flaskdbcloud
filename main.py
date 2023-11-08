#https://freefrontend.com/assets/zip/css-login-forms/sign-up-login-form.zip
#local onde peguei o free html+css

from flask import *
from dao import *

app = Flask(__name__)

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
        if(login == usuario[1] and senha == usuario[2]):
            return '<h1>LOGIN REALIZADO COM SUCESSO</h1>'

    return '<h1>LOGIN OU SENHA ERRADOS</h1>'


if __name__ == "__main__":
    app.run(debug=True)