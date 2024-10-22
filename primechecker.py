class Item:
    """ This class keeps a record of items in the store and their prices"""
    def __init__(self, item, price):
        self.item = item
        self.price = price

class ShoppingCart(Item):
    def __init__(self, item, price):
        super().__init__(item, price)
        self.my_item = 0
        self.total_item = 0
        self.my_price = 0
    def add(self):
        self.my_item += 1
        print(self.my_item)
    def total(self):
        self.total_item += self.my_item
        print(self.total_item)
    def total_price(self):
        if self.total_item == 1:
            self.my_price += self.price
        elif self.total_item != 1:
            self.my_price = self.total_item*self.price
        print(self.my_price)
headphones = ShoppingCart('headphones', 100)
headphones.add()
headphones.add()

headphones.add()
headphones.total()
headphones.total_price()


        
