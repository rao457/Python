import random

def game(choices):
    user_score = 0
    comp_score = 0
    user_choice = ""

    while user_choice != "q":
        user_choice = input("What would you choose (rock, paper, scissors) OR enter q to quit: ").lower()
        
        if user_choice == "q":
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        comp_choice = choices[random.randint(0, len(choices) - 1)]

        if user_choice == comp_choice:
            print("It's a draw!")
        else:
            if user_choice == "paper":
                userWin = comp_choice == "rock"
            elif user_choice == "rock":
                userWin = comp_choice == "scissors"
            elif user_choice == "scissors":
                userWin = comp_choice == "paper"
            
            if userWin:
                user_score += 1
                print(f"You won! Your score is {user_score}")
            else:
                comp_score += 1
                print(f"Computer won! Computer's score is {comp_score}")

choices = ["rock", "paper", "scissors"]
game(choices)
