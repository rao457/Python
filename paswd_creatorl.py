import string
import random

def generate_passwd(length):
    characters = string.ascii_letters+string.digits+string.punctuation+string.ascii_uppercase+string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    return password
creator = generate_passwd
length = int(input("Enter the length of password: "))
print(creator(length))