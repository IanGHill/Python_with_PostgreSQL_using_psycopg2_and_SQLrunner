import psycopg2
import sys

sys.path.append('../db')
from sqlrunner import *

class Student:
    def __init__(self, first_name, surname, age):
        self.id = 0
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def insert_student(self):
        sql = """
            INSERT INTO students (first_name, surname, age)
            VALUES (%s, %s, %s)
            RETURNING id;
        """
        values = (self.first_name, self.surname, self.age)
        result = Sqlrunner.run(sql, "fetchone", values)
        self.id = result[0]

    def get_all_students():
        sql = "SELECT * FROM students;"
        result = Sqlrunner.run(sql, "fetchall")
        student_array = []
        for student_row in result:
            fetched_student = Student(*student_row[1:])
            fetched_student.id = student_row[0]
            student_array.append(fetched_student)
        return student_array

    def student_search(surname):
        sql = "SELECT * FROM students WHERE surname= %s;"
        values = (surname,)
        student_row = Sqlrunner.run(sql, "fetchone", values)

        if student_row is not None:
            fetched_student = Student(*student_row[1:])
            fetched_student.id = student_row[0]
            return fetched_student
        else:
            return student_row

    def update_student(id, new_age):
        sql = "UPDATE students SET age=%s WHERE id=%s"
        values = (new_age, id)
        Sqlrunner.run(sql, "", values)
