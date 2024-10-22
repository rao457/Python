import json
with open('my_file.json') as file:
    content = json.load(file)
for name in content:
    print(f"Welcome Mr.{name} in the Meeting.")
