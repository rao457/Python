class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
    def describe_name(self):
        name = f"{self.make} {self.model} {self.color} {self.year}"
        return name
class Battery:
    """ This class gives information about battery of electric car"""
    def __init__(self):
        self.battery_status = 75
    def describe_battery_status(self, battery):
        self.battery_status = battery
        print("The battery status of car is", battery,'%')
    def get_range(self):
        """ This method tells the range of car based on battery"""
        if self.battery_status >= 25 and self.battery_status <50:
            range = '100-150'
        elif self.battery_status >= 50 and self.battery_status < 75:
            range = '150-200'
        elif self.battery_status >= 75 and self.battery_status <= 100:
            range = '200-315' 
        print(f"Car no can cover {range}km")
class Electric_Car(Car):
    """ This inherits from Car"""
    def __init__(self, make, model, year, color ):
        super().__init__(make, model, year, color)
        self.battery = Battery()
my_ece_car = Electric_Car('Tesla', 'X-man', '2019', 'black')
print(my_ece_car.describe_name())
my_ece_car.battery.describe_battery_status(100)
my_ece_car.battery.get_range()
# This line tells python look for battery attribute in instance my_ece_car and look for describe battery method in the associated with battery instace stored in attribute.