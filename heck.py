def heck():
    i = 0
    negatives = []
    positives = []
    zeros = []
    while True:
        number = int(input("Enter a number: "))
        if (number<0):
            negatives.append(number)
        elif(number>0):
            positives.append(number)
        elif(number==0):
            zeros.append(number)
        i = int(input("Press (1) if you want to continue otherwis press (0) to exit: "))
        if i==0:
            continue
        else:
            break
    choice = input("What you want to look at: \n 1-Positives\n 2-Negatives\n 3-Zeroes\n >>>> ")
    if choice.lower()=='positives':
        print(len(positives))
    elif choice.lower()== 'negatives':
        print(len(negatives)) 
    elif choice.lower()== 'zeroes':
        print(len(zeros))
    else:
        print("Unknown command.")       
result = heck()
result
