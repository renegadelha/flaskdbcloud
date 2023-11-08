import psycopg2

con = psycopg2.connect(host='dpg-cl3coj1novjs73bg3gn0-a.oregon-postgres.render.com', database='loginuserflaskrene',
user='loginuserflaskrene_user', password='mXvVoPjsfETzCxaamaqFw6f8PEa0wYKG')

cur = con.cursor()

sql = "insert into usuarios values (3,'zeze88@gmail.com','minhasenha2')"
cur.execute(sql)
con.commit()

con.close()
