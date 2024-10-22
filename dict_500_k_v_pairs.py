import string
import random
my_dict = {}
for _ in range(500):
    key = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
    value = random.randint(0, 100)
    my_dict[key] = value
print(my_dict)