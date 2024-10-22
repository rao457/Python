class Restaurant:
    """ This class defines the restaurants and their taste and some more modifications."""
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.name} restaurant has {self.taste} taste.")
    def open_restaurant(self):
        print(f'{self.name} restaurant is open now')
    def costumer_served(self, costumers):
        self.number_served = costumers
        print(f"{costumers} costumers are served till now.")
my_restaurant = Restaurant('Amigos', 'Italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.costumer_served(10)
class IceCreamStand(Restaurant):
    """ This method inherits from Restaurant"""
    def __init__(self, name, taste):
        super().__init__(name, taste)
    def flavor(self, flavors):
        print(f"This {self.name} offers following flavors: ")
        for index,f in enumerate(flavors, start=1):
            print(f"{index} : {f}")

my_ice = IceCreamStand('Cool 50', 'Vanilla')
my_ice.describe_restaurant()
flavors = ['vanilla', 'chocolate', 'strawberry', 'choco-chip']
my_ice.flavor(flavors)