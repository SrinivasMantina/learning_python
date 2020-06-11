class Employee:
    hike = 1.04     # 4% hike of salary
    num_of_emps = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.salary = salary
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def give_hike(self):
        self.salary = int(self.salary * self.hike)

    #declaring class method
    @classmethod
    def set_hike(cls, hike):
        cls.hike = hike

emp_1 = Employee("Srinivas", "Mantina", 10000)
emp_2 = Employee("Test", "User", 15000)

# regular method takes instance as first argument
# class methods takes class as first argument

Employee.set_hike(1.05)
print(Employee.hike)
print(emp_1.hike)
print(emp_2.hike)