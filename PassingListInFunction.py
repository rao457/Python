def greet_users(users):
    """ It is a function which takes a list as argument and greet each users"""
    
    for user in users:

        hello = f"Assalam-O-Alaikum {user}!"
        print(hello)

        
username = ['zohaib', 'shoaib', 'sonia', 'zubair']
greet_users(username)

