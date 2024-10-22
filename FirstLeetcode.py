TARGET = 10
import random
FIRST_list = [1, 2, 3, 4, 5, 6, 7, 8]
selectio = []
for i in FIRST_list:
    selection = random.choices(FIRST_list, k=2)
    selectio.append(selection)

found = False
for pair in selectio:
    if sum(pair) == TARGET:
        print(f"pair found: {pair}")
    
        found = True
        break
if not found:
    print("Cannot find")