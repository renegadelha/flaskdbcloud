import psycopg2

from decouple import config

con = psycopg2.connect(
    host=config("HOST_DATABASE"),
    database=config("DATABASE_NAME"),
    user=config("DATABASE_USER"),
    password=config("DATABASE_PASS")
)




def teste1(conexao):
    cur = conexao.cursor()
    try:
        cur.execute("INSERT INTO usuarios (nome, login, senha, id) VALUES ('tata', 'tata@gmail.com', 'tata123' )")
    except psycopg2.IntegrityError:
        print('erro integ')
        conexao.rollback()
    else:
        print('comitou')
        conexao.commit()

    conexao.close()

def teste2(conexao):
    cur = conexao.cursor()
    try:
        cur.execute("INSERT INTO noticias (titulo, texto, id_usuario) VALUES ('rene caiu de novo da escada', ' burro o cidadao rene se lascou ao cair', 1 )")
    except psycopg2.IntegrityError:
        print('erro integ')
        conexao.rollback()
    else:
        print('comitou')
        conexao.commit()

    conexao.close()

teste2(con)
