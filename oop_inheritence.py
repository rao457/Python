class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def action(self):
        return f"I am {self.name} and I am {self.age}"
class Dog(Pet):
    def __init__(self, name , age, color):
        super().__init__(name, age)
        self.color = color
    def cat_color(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.color} in color.")
    def speak(self):
        print("Bark")
class Cat(Pet):
    def speak(self):
        print("Meow")
dog1 = Dog('Jack', 10, 'Brown')
print(dog1.action())
dog1.cat_color()
cat1 = Cat('Jimmy', 12)
print(cat1.action())

cat1.speak()
        
        