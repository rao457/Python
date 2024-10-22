
import random
# Generating a random number
Numbers = list(range(1,100))
Computer_choice = random.choice(Numbers)
# To keep track of number of guesses made by user
Guess_numbers = 0
while True:
    # User input
    Guess = int(input("Guess the Number: "))
    # Hints if wrong input
    if Guess > Computer_choice:
        print("\n**HINT**\nToo High")
        Guess_numbers += 1
    elif Guess < Computer_choice:
        print("\n**HINT**\nToo low")
        Guess_numbers += 1
    # Result if right input is given
    elif Guess == Computer_choice:
        print("**You Got it**")
        break
# printing guesses made by user
print(f"You guessed number in {Guess_numbers}")