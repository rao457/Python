import random
my_list = list(range(1,100))
com_choice = random.choice(my_list)
start = True
while start:
    guess = int(input("Guess a number between 1-100: "))
    if guess > com_choice:
        print("Too High")
    elif guess < com_choice:
        print("Too low")
    elif guess == com_choice:
        print("***You got it.***")
        break