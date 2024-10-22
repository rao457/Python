# This method actually opens a file and read the content 
#within that file
with open('learning python.txt', 'r') as file_object:
    # print(file_object.read())
    # for line in file_object.readlines():
    #     print(line.rstrip())
    lines = file_object.readlines()
print(''.join(lines).rstrip())

with open('learning python.txt', 'r') as f:
    my_lines = f.readlines()
my_string = ''
for my_line in my_lines:
    my_string += my_line.rstrip()
print(f"{my_string[:200
                   ]}")