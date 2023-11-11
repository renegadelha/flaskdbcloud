import psycopg2

from decouple import config

def conectardb():
    con = psycopg2.connect(
        host=config("HOST_DATABASE"),
        database=config("DATABASE_NAME"),
        user=config("DATABASE_USER"),
        password=config("DATABASE_PASS")
    )

    return con


def inserirDB(login, senha, nome, conexao):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (nome, login, senha) VALUES ('{nome}', '{login}', '{senha}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito


def cadastrarNoticiaDB(titulo, texto, id_usuario, conexao):

    cur = conexao.cursor()
    try:
        sql = f"INSERT INTO noticias (titulo, texto, id_usuario) VALUES ('{titulo}', '{texto}', {id_usuario} )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito


def listarnoticiasUsuario(conexao, id_usuario):

    cur = conexao.cursor()
    cur.execute(f'select * from noticias where id_usuario = {id_usuario}')
    recset = cur.fetchall()
    conexao.close()

    return recset



def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from usuarios')
    recset = cur.fetchall()
    conexao.close()

    return recset



