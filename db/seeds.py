import sys

sys.path.append('./db')
sys.path.append('./models')
from student import *


class Seeds:
    def __init__(self):
        pass

    def run_seeds():
        student1 = Student("John", "McCollum", 38)
        student2 = Student("David", "Bell", 35)
        student1.insert_student()
        student2.insert_student()





