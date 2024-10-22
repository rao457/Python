class Car:
    """ This class defines cars model menufacturer and year it was made and also there'd be a concept of inheritence"""
    def __init__(self, model, manufacturer, year):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.odometer_reading = 2000
    def describe_vehicle(self):
        formatted_car = f"{self.model} {self.manufacturer} {self.year}"
        return formatted_car
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"Car's odometer reading now {self.odometer_reading}")
        else:
            print("You can't roll back the odometer reading.")
    def increment_reading(self, mile):
        self.odometer_reading += mile
        print(f"new odometer reading is {self.odometer_reading}")
class Electric_Car(Car):
    """ Inheritence """
    def __init__(self, model, menufacturer, year):
        super().__init__(model, menufacturer, year)
        self.battery_status = 75
    def describe_batter(self):
        print(f"car's battery status now is {self.battery_status}%.")
my_tesla = Electric_Car('X_man', 'Elon_Musk', 2019)
print(my_tesla.describe_vehicle())
my_tesla.update_odometer(2000)
my_tesla.increment_reading(20)
my_tesla.describe_batter()