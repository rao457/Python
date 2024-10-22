import hashlib
def hash_password(password):
    hash_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(hash_bytes)
    hashed_password = hash_object.hexdigest()
    return hashed_password
def user_password():
    password = input("Enter a password: ")
    hashed = hash_password(password)
    print(hashed)
if __name__=="__main__":
    user_password()