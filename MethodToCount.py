def File_Count_Words(filename):
    """ This method counts words in it"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
        content = content.split()
        words = len(content)
    except FileNotFoundError:
         print(f"Sorry, file {filename} does not exist.")
    else:
        print(f"This file {filename} and it has {words} in it.")
with open('Numbers.txt', 'r') as f:
    content = f.read()
content = content.split(',')
my_sum = sum(int(num)for num in content)
print(my_sum)