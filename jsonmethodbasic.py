import json
names = ['zohaib', 'shoaib', 'sonia', 'zubair']
with open('my_file.json', 'w') as f:
    json.dump(names, f)
with open('my_file.json', 'r') as file:
    content = json.load(file)
print(content)