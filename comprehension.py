# Comprehension is basically looping over iterable objects combined with 
# conditions in consice syntax
# List comprehension
my_list = [x for x in range(100) if x%2 == 0]
print(my_list)
my_dict = {x: x**2 for x in range(10) if x%2 == 0}
print(my_dict)