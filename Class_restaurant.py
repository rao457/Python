class Restaurant:
    """ This class refers to dishes in a restaurant."""
    def __init__(self, restaurant_name, taste_type):
        self.restaurant_name = restaurant_name
        self.taste_type = taste_type
    def name(self):
        print(f"The name of restaurant is {self.restaurant_name}")
    def taste(self):
        print(f"{self.restaurant_name} has {self.taste_type}")
restaurant = Restaurant('Amigos', 'Italian taste')
restaurant.name()
restaurant.taste()
restaurant2 = Restaurant('Quetta Restaurant', 'Pakistani Taste')
restaurant2.name()
restaurant2.taste()
restaurant3 = Restaurant("Bismillah Hotel", "Darya Khan Taste")
restaurant3.name()
restaurant3.taste()