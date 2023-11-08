import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl3coj1novjs73bg3gn0-a.oregon-postgres.render.com', database='loginuserflaskrene',
    user='loginuserflaskrene_user', password='mXvVoPjsfETzCxaamaqFw6f8PEa0wYKG')

    return con


def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from usuarios')
    recset = cur.fetchall()
    conexao.close()

    return recset



