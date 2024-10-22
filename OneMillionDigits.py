# This method is gonna create a file containing one million digits in it.
content = ''
for number in range(1, 100):
    number = str(number)
    content += number
    with open('One_Million.txt', 'w') as f:
        for line in f.writelines(content):
            f.write(line)
if '20' in content:
    print("It is in the content")
else:
    print("No")
