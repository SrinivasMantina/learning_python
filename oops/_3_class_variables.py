class Employee:
    # class variables - same for all instances
    hike = 1.04     # 4% hike of salary
    num_of_employees = 0

    def __init__(self, first, last, salary):
        # instance variables
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        # accessing class variable inside instance method
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def get_hike_percent(self):
        # without class variable
        # suppose we need to increase the hike by 4%,
        # we have to go inside the method, update the occurances
        # instead create a class variable and use this here
        # with class variable
        return self.hike

emp_1 = Employee("Srinivas", "Mantina", 10000)
emp_2 = Employee("Test", "User", 15000)


# to call class variable 
# <class_name>.<variable_name>
# <instance_name>.<variable_name>

# if called by <instance_name>.<variable_name>
# interpreter checks if <instance_name>.<variable_name> is available
# if doesn't exist, it checks <class_name>.<variable_name>
# either way it calls <class_name>.<variable_name>
print(Employee.hike)
print(emp_1.hike)

# print namespaces
print(emp_1.__dict__)
# output
# {'first': 'Srinivas', 'last': 'Mantina', 'email': 'srinivas.mantina@company.com', 'salary': 10000}
# there is no hike present in the instance
print(Employee.__dict__)
# output
# {'__module__': '__main__', 'hike': 1.1, '__init__': <function Employee.__init__ at 0x10e109c20>, 'fullname': <function Employee.fullname at 0x10e1095f0>, 'give_hike': <function Employee.give_hike at 0x10e109b90>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
# we can see hike in the class

# Employee.hike = 1.06        # updated hike
# print(emp_1.hike)              # we get new value
# print(emp_2.hike)              # we get new value

emp_1.hike = 1.07            # updated in instance
# print(emp_1.hike)
# print(emp_1.__dict__)
# output
# {'first': 'Srinivas', 'last': 'Mantina', 'email': 'srinivas.mantina@company.com', 'salary': 10000, 'hike': 1.07}
# we can see hike present in the instance as it is being declared
# print(emp_2.hike)             # change didn't reflect

print("%"*60)
Employee.hike = 1.06 
print(f"oject_1 instance: {emp_1.hike}")                   # refers to instance variable not class variable as it is defined
print(f"oject_2 instance: {emp_2.hike}")
print("%"*60)

print(f"total number of employees: {Employee.num_of_employees}")
print("%"*60)
