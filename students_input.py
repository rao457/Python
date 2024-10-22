while True:
    i = int(input("Enter (1) to continue and (0) to exit: "))
    if i == 1:
        marks = input("Enter the marks of student: ")
        try:
            marks = int(marks)
            if marks >= 90:
                print("Very Good")
            elif 50 <= marks <80:
                print("Good")
            elif marks < 50:
                print("Good as well.")
        except:
            print("Please enter an integer.")
            continue
       
    else:
        break
