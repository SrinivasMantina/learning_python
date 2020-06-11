# a class is a user-defined blueprint or prototype from which objects (instances) are created. 
# classes provide a means of bundling data and functionality together.
# class defines how a instance should be - what attributes, it

class Student:
    # constructor
    # constructors are generally used for instantiating an object.
    # the task of constructors is to initialize (assign values) to the data members of the class when an object of class is created.
    # in python __init__ method is constructor
    # self is the first argument in class which referes to the instance
    # arguments other than self are to initialize data members of the class
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def fullname(self):
        return f"{self.first_name} {self.last_name}"              # called f string. used in formating strings (>= python 3.6)


student_1 = Student("Srinivas", "Mantina", 5)

print(student_1.fullname)                                    # prints location of method. varies from execution to execution
print(student_1.fullname())                                 # prints returned value of method
print(Student.fullname(student_1))                      # using class to call a method
