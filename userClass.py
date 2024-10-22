class User:
    """ This class is defined to show some of values associated to a user"""
    def __init__(self, name, employee_ID, salary, increases):
        self.name = name
        self.employee_ID = employee_ID
        self.salary = salary
        self.increases = increases
    def increment(self):
        print(f"new salary is {self.salary}*{self.increases}
              ")
    def info(self):
        print(f"{self.name} with {self.employee_ID} with salary {self.salary} \n is given an increase of {self.increases} ")
user = User('Zohaib', 1135, 12000, .5)
user.increment()
user.info()
        