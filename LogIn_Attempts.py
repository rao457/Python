class User:
    """ This class tell us the attributes of a user and his log in attempts."""
    def __init__(self, name, password, employee_ID):
        self.name = name
        self.password = password
        self.employee_ID = employee_ID

    def show_info(self):
        print(f"{self.name} employee's password is secret and employee_ID is {self.employee_ID}")
new_user = User('Zohaib', 'xijinping090', 234378)
new_user.show_info()
## I would repeat it through Chat GPT


