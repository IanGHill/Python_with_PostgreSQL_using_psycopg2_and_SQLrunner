import sys

sys.path.append('./db')
sys.path.append('./models')
from student import *
from db_setup import *
from seeds import *

DBSetup.set_up_table()
Seeds.run_seeds()

choice = ""
while choice.casefold() != "q":
    print("""
        Select an option:
        1. Display all Students
        2. Search for a student
        3. Update student's age
        """)

    choice = input()

    if choice == "1":
        all_students = Student.find_all()
        for student in all_students:
            print(f"Student {student.id}: {student.first_name} {student.surname}, {student.age}")

    elif choice == "2":
        print("Enter Student Surname:")
        surname = input()
        student = Student.find_by_name(surname)
        if student is None:
            print("Student not found")
        else:
            print(f"Student {student.id}: {student.first_name} {student.surname}, {student.age}")

    elif choice == "3":
        print("Enter the student's surname:")
        surname = input()
        student = Student.find_by_name(surname)

        if student is not None:
            print("Enter the student's new age:")
            age = input()

            student.update(student.id, age)
            print(f"{student.first_name} {student.surname} updated!")
        else:
            print("Student not found")
