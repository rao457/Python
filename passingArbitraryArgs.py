# Arbitrary arguments are useful when we don't know how many argument a function 
# is gonna take. 
def make_pizza(*toppings):
    """ Function for making pizza with toppings that client ordered"""
    print("\n Following toppings are added to pizza")
    for topping in toppings:
        print(f"topping : {topping}")
make_pizza('mushrooms', 'green peppers', 'extra cheese')
