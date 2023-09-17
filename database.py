from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Define the database connection string
db_connection_string = "mysql+pymysql://root:jaga@localhost/japcareer?charset=utf8mb4"

# Create the SQLAlchemy database engine
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))
            result_all = result.fetchall()

        if result_all:
            column_names = result.keys()
            jobs = [dict(zip(column_names, row)) for row in result_all]
            return jobs
        else:
            print("No rows returned from the database.")
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")

def load_job_from_db(job_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs WHERE id = :value"), {"value": job_id})
            row = result.fetchone()

        if row:
            column_names = result.keys()
            job = dict(zip(column_names, row))
            return job
        else:
            print(f"No job found with ID {job_id}.")
            return None
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")

def add_application_to_db(job_id, data):
    try:
        with engine.connect() as conn:
            query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
                         "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

            conn.execute(query, {
                "job_id": job_id,
                "full_name": data['full_name'],
                "email": data['email'],
                "linkedin_url": data.get('linkedin_url'),
                "education": data.get('education'),
                "work_experience": data.get('work_experience'),
                "resume_url": data.get('resume_url')
            })
        print("SQL Query:", query)
        print("job_id:", job_id)
        print("full_name:", data['full_name'])
        print("email:", data['email'])
# Add similar print statements for other fields

        print("Application added successfully.")
        conn.commit()
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")

# Additional functions and error handling can be added as needed.

if __name__ == "__main__":
    # You can add testing or example usage of the functions here.
    pass
