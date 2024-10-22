import random
import string
def generate_password(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(characters)for i in range(length))
    return password
length = 12
print_password = generate_password(length)
print(print_password)