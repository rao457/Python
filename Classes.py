class Dog:
    """ This class defines dog sitting and rolling over property."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is sitting.")
    def roll_over(self):
        print(f"{self.name} is rolling over.")
my_dog = Dog('Jack', 5)
print(f"Name of my dog is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('Willie', 5) 
your_dog.sit()
your_dog.roll_over()
