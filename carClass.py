""" This class shows module """
class Car:
    """ This class simply defimes the make model and year of the car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_description(self):
        neat_format = f"{self.year} {self.make} {self.model}"
        return neat_format
my_car = Car('Jack', 'Audi', 2018)
print(my_car.get_description())