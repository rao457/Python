message = input("Enter something and I'll repeat it for you: ")
print(message*2)
car = input(">")
print("Let me check if i can find ", car, "for you.")
seats = int(input("How many seats do you want to have? "))
if seats > 8:
    print("you'd have to wait for a table.")
else: 
    print("Your table is ready.")
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(True)
else: 
    print(False)
# While Loops
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1
