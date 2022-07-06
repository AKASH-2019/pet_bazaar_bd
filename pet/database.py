# import json 
import psycopg2
from psycopg2.extras import Json

con = psycopg2.connect(
    host = "localhost",
    database = "eofa",
    user = "postgres",
    password = "postgres"
)

from django.db import connection
import celery


class FaultTolerantTask(celery.Task):
    """ Implements after return hook to close the invalid connection.
    This way, django is forced to serve a new connection for the next
    task.
    """
    abstract = True
    # print("celery")

    def after_return(self, *args, **kwargs):
        # print("close celery")
        connection.close()


@celery.task(base=FaultTolerantTask)
def db(storeProcedure,payload):

    cur = con.cursor()

    sql = f"SELECT {storeProcedure}('{payload}'::jsonb)"
    # print(sql)
    
    cur.execute(sql)
    con.commit()

    data = cur.fetchone()

    # con.close()


    return data
