Age = input("Enter Your Age? ")
if Age.isdigit():
    Age = int(Age)
    if Age <= 2:
        print("You are a baby.")
    elif 2< Age < 18:
        print("You are a boy.")
    elif 18< Age <=40:
        print("You Are A man.")
    elif 40< Age < 50:
        print("YOu are sexy.")
    else:
        print("You are dead.")
else:
    print("Invalid Age.")