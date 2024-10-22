class Default_Car:
    """ This class is specified to set a default value and then modify it"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_readings = 0
    def car_info(self):
        car_format = f"{self.make} {self.model} {self.year}"
        return car_format
    def odometer_reading(self):
        print(f"car's odometer_reading is {self.odometer_readings}")
my_car = Default_Car('Jack', 'Audi', 2018)
print(my_car.car_info())
my_car.odometer_readings = 23
my_car.odometer_reading()
class Car:
    """ This is just for odometer_reading to calcualte."""
    def __init__(self):
        self.odo_reading = 23
    def modified_odo(self, mileage):
        if (mileage>= self.odo_reading):
            self.odo_reading = mileage
            print(f"Car is {mileage} mileage now")

        else:
            print("You can't roll back reading.")
my_new_car = Car()
my_new_car.modified_odo(22)

