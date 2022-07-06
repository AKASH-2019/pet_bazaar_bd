# import json 
import psycopg2
from psycopg2.extras import Json

con = psycopg2.connect(
    host = "localhost",
    database = "eofa",
    user = "postgres",
    password = "postgres"
)

def db(storeProcedure,payload):

    cur = con.cursor()

    sql = f"SELECT {storeProcedure}('{payload}'::jsonb)"
    # print(sql)
    
    cur.execute(sql)
    con.commit()

    rows = cur.fetchone()

    con.close()

    # print(len(rows))

    # for r in rows:
    #     print(r[0])
    return rows
