class Employee:
    hike = 1.04     # 4% hike of salary
    num_of_employees = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.salary = salary
        Employee.num_of_employees += 1

    # declaring instance method
    def get_full_name(self):
        return f"{self.first} {self.last}"

    def get_hike_percent(self):
        return self.hike

    # declaring class method
    # classmthod takes cls as an argument
    # classmethod has access to class variables
    # any updation in class variables, get reflected to all objects
    @classmethod
    def set_hike_percent(cls, hike):
        cls.hike = hike

    # declaring static method
    # has no relation to class variables or instance variables
    # completely independent
    @staticmethod
    def wish_employee():
        print("Greetings!\nWelcome to the Organisation!")

    

emp_1 = Employee("Name", "Surname", 10000)
emp_2 = Employee("Test", "User", 15000)

# regular method takes instance as first argument
# class methods takes class as first argument

print("%"*60)
Employee.set_hike_percent(1.05)
print(f"class variable: {Employee.hike}")
print(f"object_1 variable: {emp_1.hike}")
print(f"object_2 variable: {emp_2.hike}")
print("%"*60)

print(f"Total number of Employees: {Employee.num_of_employees}")
print("%"*60)