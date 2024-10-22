# Zero Division
# Simple Division Method
print("Give me two numbers I'll divide them")
while True:
    print("***Press q any time to quit***")
    first_num = input("Enter first number: ")
    second_num = input("Enter secod number: ")
    if first_num == 'q':
        break
    elif second_num == 'q':
        break
    try:
        answer = int(first_num)/ int(second_num)
    except ZeroDivisionError:
        print("Numbers can't be divided by 0! ")
    else:
        print(answer)