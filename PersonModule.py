class Person:
    """ This class defines general persons in our game which move around our game"""
    def __init__(self, name, job, age, height, dress, doing):
        """ This method defining different attributes of person"""
        self.name = name
        self.job = job
        self.age = age
        self.height = height 
        self.dress = dress
        self.doing = doing
    def describe_person(self):
        print(f"Name : {self.name}\nJob : {self.job}\nAge : {self.age}\tHeight : {self.height}")
        print(f"{self.name} is wearing {self.dress} and he is {self.doing}\n")
first_person = Person('Zohaib', 'Hacker', 20, '5.6f', 'Paint-shirt', 'Jogging')
first_person.describe_person()
second_person = Person('Shoaib', 'Contractor', 22, '5.4f', 'Paint-coat', 'Calling')
second_person.describe_person()
third_person = Person("zubair", 'Farmer', 16, '5.4f', 'Shalwar-Qameez', 'Gaming')
third_person.describe_person()