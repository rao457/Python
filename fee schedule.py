"""
1- Students of age 4 have no admission fee.
2- Students of age above than 4 and less than 18 have 25$ admission fee.
3- Students of age above than 18 and less than 20 have 50$ admission fee.
"""
def info():
    while True:
        name = input("Enter your name: ")
        age = input('Enter your age: ')                                                          
        if age.isdigit():
            age = int(age)
        
            if age == 0 and age<4:
                print("You are too young to get admitted.")
                break
            elif age >=4 and age<18 :
                print("Enter can take admission with no admission fee.")
                break
            elif age< 4 and age <= 18:
                print("You can take admission with 25$ admission fee.")
                break
            elif age>=18 and age <= 20:
                print("You can take admission with 50$ admission fee.")
                break
            elif age > 20:
                print("You cannot take admission.")
        else:
            print("Invalid Age!!")
            continue
info()

