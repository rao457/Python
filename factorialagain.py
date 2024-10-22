#Function to find factorial
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
# Taking user input to give factorial
def ask_user():
    while True:
        give_me = int(input("Enter a number: "))
        #handling invalid inputs
        if give_me < 0:
            print("Invalid Input.\n**Hint**\n Input must be greater than zero.")
        #Handling special case
        elif give_me == 1:
            print("Factorial is 1")
        else:
            result = print(factorial(give_me))
            break
    return result
#Making sure function is ran in main 
if __name__ == "__main__":
    ask_user()