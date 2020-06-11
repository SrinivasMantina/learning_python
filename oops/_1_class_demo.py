# declaring a class
class Student:
    pass

# creating a class instance
student_1 = Student()
print(student_1)                # returns Student object

# declaring attributes
student_1.first_name = "Srinivas"
print(student_1.first_name)

# printing the object's (writable) attributes
print(Student.__dict__)
# output
# {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Student' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
print(student_1.__dict__)
# output 
# {'first_name': 'Srinivas'}