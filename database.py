from sqlalchemy import create_engine,text

db_connection_string = "mysql+pymysql://root:jaga@localhost/japcareer?charset=utf8mb4"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.fetchall()

  if result_all:
    column_names = result.keys()
    jobs = [dict(zip(column_names, row)) for row in result_all]
    return jobs
  else:
    print("No rows returned from the database.")

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :value"), {"value": id})
    rows = result.fetchall()
    if len(rows)==0:
      return None
    else:
      if rows:
        column_names = result.keys()
        jobs = [dict(zip(column_names, row)) for row in rows]
        return jobs[0]
  # Assuming you want to query for id = 3


