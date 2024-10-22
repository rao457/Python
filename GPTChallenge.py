class Person:
    """ This class defines person's name and age and prints a greet message to him"""
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet_person(self):
        print(f"Welcome sir {self.name}!\nYour age is {self.age} and you are eligible for this job post.")
candidate = Person('Zohaib', 20)
candidate.greet_person()