class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name}, and Im {self.age} years old.")
class Student(Person):
     def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age) 
myStudent = Student(first_name="Jackton", last_name="Mboya", age="25")
myStudent.print_name()
myStudent2 = Student(first_name="John", last_name="Smith", age="22")
myStudent2.print_name()
myStudent3 = Student(first_name="Caleb", last_name="Mike", age="20")
myStudent3.print_name()
myStudent4 = Student(first_name="Sam", last_name="Andrew", age="19")
myStudent4.print_name()
