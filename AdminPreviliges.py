class User:
    """ This class explains user and his previliges in my office"""
    def __init__(self, name, employee_ID, job_post):
        self.name = name
        self.employee_ID = employee_ID
        self.job_post = job_post
    def describe_employee(self):
        details = f"\nName: {self.name}\nEmployee_ID: {self.employee_ID}\nJob_post: {self.job_post}"
        return details
class Admin(User):
    """ This class inherits from the user class and also tells us about admin previliges"""
    def __init__(self, name, employee_ID, job_post):
        super().__init__(name, employee_ID, job_post)
    def admin_previliges(self, previliges):
        print("Admin has following previlges: ")
        for index,previlige in enumerate(previliges, start=1):
            print(f"{index} : {previlige}")
new_admin = Admin('Junaid', 23434, 'Admin')
print(new_admin.describe_employee())
previlges = ['Can add user', 'Can delete user', 'Can add posts to portal', 'Can ban user']
new_admin.admin_previliges(previlges)

