unconfirmed_users = ['shoaib', 'sonia', 'zubair']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Varifying User: {current_user}")
    confirmed_users.append(current_user)
print("\n The following users are confirmed.")
for confirmed_user in confirmed_users:
    print(f"Confirmed User: {confirmed_user.title()}")
# removing all instaces of value in list
pets = ['dog', 'cat', 'goldfish', 'starfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
# Filling a dictionary via input from user
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    poll = input("Which mountain would you like to climb one day? ")
    responses[name] = poll
    ask =  input("Would you like to let another person poll (yes/no)? ")
    if ask == 'no':
        polling_active = False
    for name,poll in responses.items():
        print(f"{name} would like to climbe {poll}.")