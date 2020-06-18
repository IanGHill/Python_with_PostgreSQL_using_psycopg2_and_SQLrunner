import psycopg2

class DBSetup:
    def __init__(self):
        pass

    def set_up_table():
        connection = psycopg2.connect(dbname="students_db", user="postgres", password="")
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("""
          CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            first_name TEXT,
            surname TEXT,
            age INTEGER
          )
        """)
        connection.commit()
        connection.close()
