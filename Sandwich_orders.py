ordered_sandwiches = ['pepperoni sandwich', 'pastrami sandwich', 'tomato sandwich', 'pastrami sandwich', 'chicken sandwich', 'potato sandwich', 'pastrami sandwich']

made_sandwiches = []
print("We ran out of Pastrami sandwiches.")
while 'pastrami sandwich' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami sandwich')
while ordered_sandwiches:
    current_sandwich = ordered_sandwiches.pop()
    print(f"Making sandwich: {current_sandwich}")
    made_sandwiches.append(current_sandwich)
print("Following sandwiches are ready: ")
for made_sandwiche in made_sandwiches:
    print(made_sandwiche)
