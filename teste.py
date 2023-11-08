import psycopg2

con = psycopg2.connect(host='dpg-cl5roh56fh7c73eu61hg-a.oregon-postgres.render.com', database='servicewebrene2',
user='servicewebrene2_user', password='hLTYAaa3l0YOM2LC41SWgLKNq9SuRnsp')



def teste1(conexao):
    cur = conexao.cursor()
    try:
        cur.execute("insert into users values ('tata@gmail.com','tata123', 'tata')")
    except psycopg2.IntegrityError:
        print('erro integ')
        conexao.rollback()
    else:
        print('comitou')
        conexao.commit()

    conexao.close()

teste1(con)
