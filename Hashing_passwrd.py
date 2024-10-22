import hashlib
def hash_password(password):
    pas_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(pas_bytes)
    hashed_password = hash_object.hexdigest()
    return hashed_password
password = input("Enter password: ")
content = hash_password(password)

with open('hashed', 'w') as f:
    f.write(content)
with open('hashed','r') as f:
    for line in f.readlines():
        print(line )