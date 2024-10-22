while True:
    give = input("What is your favourite music now? ")
    if give != 'quit'.lower():
        print(give)
    else:
        break
prompt = "\n Please enter the name of city you've visited?"
prompt += "\n Enter quit when you are done: "
while True:
    city = input(prompt)
    if city != 'quit'.lower():
        print(city)
    else:
        break
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number, end=' ')
# Pizza Toppings again
Add = True
while Add:
    topping = input("Which topping do you want to add? ")
    if topping != 'quit'.lower():
        print(f"You {topping}'ll be added.")
    else:
        break
# Theater Tickets
Age = input("What is Your Age? ")
if Age.isdigit():
    Age = int(Age)
    while True:
        if Age <= 3:
            print("Your Ticket is free.")
        elif 12 >= Age > 3 :
            print("Your Ticket-fee is 10$.")
        elif Age > 12 :
            print('YOur Ticket-fee is 15$.')
else:
    print("Invalid Age.")        
