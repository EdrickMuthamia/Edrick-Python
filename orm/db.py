import psycopg2
from psycopg2 import pool

#Boiler Plate
class PG:
    def __init__(self):
        self.credentials = (
            "host= aws-0-us-east-1.pooler.supabase.com "
            "dbname= postgres "
            "user= postgres.ursqrsbmzwbgvhnblwsq "
            "password= Edrick.M.J2005 "
            "port=5432 "
        )
        #setting 
        #Optional
        self.pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=5,
            dsn=self.credentials
        )
    # query should be a string
    # Params should always be tuple
    def pg_query(self,query,params=()):
        #should execute our query  and return
        #any results
        conn = self.pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = None
                try:
                    result = cur.fetchall()
                except Exception:
                    pass
                conn.commit()
                return result
        finally:
            self.pool.putconn(conn)    