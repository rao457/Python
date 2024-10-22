Master_Password = 'xijinping090'
start = True
# Guess Section
while start:
    Guess = input("Guess the Password: ")
    if Guess.isdigit() and Guess != Master_Password:
        print("**Hint**\nTry alphabets and digits together to guess.")
        
    elif Guess.isalpha() and Guess != Master_Password:
        print("**Hint**\nTry using Alphabets followed by digits.")
        
    elif Guess == Master_Password:
        print("***Access Granted***")
        break