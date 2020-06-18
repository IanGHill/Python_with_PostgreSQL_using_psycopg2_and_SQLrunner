import psycopg2

class Sqlrunner:
    def __init__(self):
        pass

    def run(sql, mode, values = ()):

        connection = None
        result = None

        try:
        # connect to the PostgreSQL database
            connection = psycopg2.connect(dbname="students_db", user="postgres", password="")
        # create a new cursor
            cursor = connection.cursor()
        # execute the SQL statement
            cursor.execute(sql, values)
        # check mode to determine what to return
            if mode == "fetchone":
                result = cursor.fetchone()
            elif mode == "fetchall":
                result = cursor.fetchall()
            else:
                pass
        # Commit the changes to the database
            connection.commit()
        # Close communication with the PostgreSQL database
            connection.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()

        return result
