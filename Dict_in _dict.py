my_dict = {
    'first_person' : {
        'first_name' : 'rao',
        'second_name' : 'zohaib',
        'location' : 'pakistan'
    },
    'second_person' : {
        'first_name' : 'syed',
        'second_name' : 'noor hussain',
        'location' : 'pakistan'
    }
}
for person, info in my_dict.items():
    print(f"Identifier: {person}")
    print(f"Full Name: {info['first_name']} {info['second_name']}")
    print(f"Location: {info['location']}")
print(f"You are {info['first_name'].title()} {info['second_name'].title()} from {info['location']}")
