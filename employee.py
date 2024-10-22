class Employee:
    """ This class gives first name last name salary and raise to salary"""
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.raise_salary = 500
    def update_raise(self, update):
        self.raise_salary =  update
        self.salary += self.raise_salary
    
        
        print(f'Now, your salary is {self.salary}')
    def show_info(self):
        print(f"Your name is {self.first_name} {self.last_name}.")
        print(f"Your salary is {self.salary}")
        print(f"Raise in you salary is {self.raise_salary}")
new_employee = Employee('Rao', 'Zohaib', 100000)
new_employee.show_info()
new_employee.update_raise(10000)