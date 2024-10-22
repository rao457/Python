# This program can find open and count words in it.

filename = 'Python_Notes.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    content = content.split()
    words = len(content)
except FileNotFoundError:
    print(f"Sorry, your file {filename} does not exist.")

else:
    print(f"This file {filename} contains {words} words in it.")

