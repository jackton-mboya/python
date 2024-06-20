class Student:
    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # method

    def display(self):
            print(self.first_name, self.last_name)

    # object
my_student = Student('John', 'Smith')
my_student.display()
my_student2 = Student('Johnson', 'Mark')
my_student2.display()
my_student3 = Student('Jack', 'Norris')
my_student3.display()
my_student4 = Student('Tony', 'Abraham')
my_student4.display()

