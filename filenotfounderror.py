filename = 'My_Name.txt'
try:
    with open(filename, encoding='utf-8') as f:
        f.read()
except FileNotFoundError:
    print(f"Sorry, Your file {filename} cannot be found.")
