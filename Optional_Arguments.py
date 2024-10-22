def my_optional(first, last, middle = ''):
    if middle:
        full_name = f"{first} {middle} {last}"
        return full_name.title()
    else:
        full_name = f"{first} {last}"
        return full_name.title()
first = input("Enter first name: ")
middle = input("Enter middle name: ")
last = input("Enter last name: ")
result = my_optional(first, last)
print(result)
# Returning Dictionary
def my_dict(first_name, last_name, age = None):
    person = {'F-Name' : first_name, 'L_Name' : last_name }
    if age:
        person['Age'] = age
    return person
musician = my_dict('Rahat', 'Fateh')
print(musician)