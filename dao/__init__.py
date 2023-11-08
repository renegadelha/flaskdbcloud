import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl5roh56fh7c73eu61hg-a.oregon-postgres.render.com', database='servicewebrene2',
                           user='servicewebrene2_user', password='hLTYAaa3l0YOM2LC41SWgLKNq9SuRnsp')

    return con

def inserirDB(login, senha, nome, conexao):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"insert into users values ('{login}','{senha}', '{nome}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito


def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from users')
    recset = cur.fetchall()
    conexao.close()

    return recset



