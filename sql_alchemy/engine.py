from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

db_credentials={
       "host= aws-0-us-east-1.pooler.supabase.com "
        "dbname= postgres "
            "user= postgres.ursqrsbmzwbgvhnblwsq "
            "password= Edrick.M.J2005 "
            "port=5432 "
        
}
db_credentials={
    "drivername":"postgresql+psycopg2",
    "host":"aws-0-us-east-1.pooler.supabase.com",
    "username":"postgres.ursqrsbmzwbgvhnblwsq",
    "password":"Edrick.M.J2005",
    "database":"postgres",
    "port":5432
}
#Build DB URL
DATABASE_URL=URL.create(**db_credentials)

#create engine
engine=create_engine(DATABASE_URL,echo=True,future=True)

with engine.connect() as conn:
    result=conn.execute(text("SELECT * FROM employee"))
    rows=result.fetchall()

    for row in rows:
        print(row)