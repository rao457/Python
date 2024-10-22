# this programm adds to number and catch any value error if occur
first_num = input("Enter first Number: ")
second_num = input("Enter second Number: ")
try: 
    answer = int(first_num) + int(second_num)
except ValueError:
    print("Please enter Integers not digits.")
else:
    print(f"The result is {answer}.")