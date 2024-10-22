usernames_data = []
while True:
    Ask = input("What do you wanna do with database (Add, view)? ")
    if Ask.lower() == 'add':
        username = input("Enter username: ")
        if username in usernames_data:
            print("Username already exists.")
            continue
        
        else:
            usernames_data.append(username)
        
    if Ask.lower() == 'view':
        print(usernames_data)
        break