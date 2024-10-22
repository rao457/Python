# This programm simply takes two numbers and divide them
# and also handle valuerror and zerodivision error
def Take_Check_Divide():
    """ This function takes user input and check for error
    and divide"""
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    # Handling ValueError
    try:
        first_num = int(first_num)
        second_num = int(second_num) 
    except ValueError:
        print("Please provide integers for proper division.") 
    # Handling ZeroDivisionError
    try:
        answer = first_num / second_num
    except ZeroDivisionError:
        print("You cannot divide any number with zero!")
    else:
        return answer
result = Take_Check_Divide()
if result == None:
    pass
else:
    print(round(result, 2))