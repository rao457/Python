requested_toppings = ['red peppers', 'garlic', 'chicken', 'green pepper', 'tomatoes', 'cheese']
available_toppings = []
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry Green Pepper is not available.")
    else:
        available_toppings.append(requested_toppings)
        print(f"{requested_topping} is added to your pizza.")
print("\nFinished making Pizza.")
requested_things = []
if requested_things:
    for requested_thing in requested_things:
        print(f"{requested_thing} is added to pizza.")
else:
    print("Are You sure you want to make a plain pizza?")