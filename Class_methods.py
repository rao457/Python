class Car:
    model = 'Pakistani'
    def __init__(self, name , year, condition):
        self.name = name
        self.year = year
        self.condition = condition
        self.odo_meter_reading = []
    def show_info(self):
        return f"{self.name} is {self.year} years old and it is in {self.condition} condition."
    def increase_odo_reading(self, reading):
        self.odo_meter_reading.append(reading)
        return f"Now reading is {self.odo_meter_reading}"
    def len(self):
        return len(self.odo_meter_reading)
    def total(self):
        return sum(self.odo_meter_reading)
        
my_car = Car('Toyota', 4, "Good")
print(my_car.show_info())
print(my_car.increase_odo_reading(200))
print(my_car.increase_odo_reading(300))
print(my_car.increase_odo_reading(100))
print(my_car.len())
print(my_car.total())