class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Example usage
my_car = Car('audi', 'a4', 2020, 'blue')
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modifying attributes
my_car.update_odometer(500)
my_car.read_odometer()

# Incrementing odometer
my_car.increment_odometer(100)
my_car.read_odometer()
class Electric_Car(Car):
    """ This Car inherits the attribute of car"""
    def __init__(self,make, model, year, color):
        super().__init__(make, model, year, color)
        self.battery_status = 75
        self.charging_time = '2 Hour'
    def battery_info(self):
        print(f"batter status is {self.battery_status} and it would take {self.charging_time} to get charged.")
my_elec_car = Electric_Car('Tesla', 'X_man', '2018', 'black')
print(my_elec_car.get_descriptive_name())
my_elec_car.battery_info()





















