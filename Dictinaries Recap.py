# In this file i am gonna revieese all my dictionary concepts 
# Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

print(alien_0['points'])
#Adding New Key-Value Pairs
alien_0['name'] = 'zapada'
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#Empty dictionaries
empty = {}
empty['name'] = 'zohaib'
empty['age'] = 20
empty['religion'] = 'islam'
empty['location'] = 'Pakistan'

print(empty)
#Modifying the dictionary
empty['name'] = input("Enter Your name: ")
print(empty)
#Best Example in Modifying 
alien_0['speed'] = 'slow'
if alien_0['speed'] == 'slow':
    x_increment = 5
elif alien_0['speed'] == 'medium':
    x_increment = 10
elif alien_0['speed'] == 'fast':
    x_increment = 15
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'The new alien position is {alien_0['x_position']}')
#Removing A value
del alien_0['points']
print(alien_0)
# Dictionary of similar objects
languages = {
    'zohaib' : 'python',
    'sonia': 'java',
    'zubair': 'c++',
    'shoaib' : 'javascript'

}
#Get method to access elements
print(alien_0.get('points', 'element not found'))
#Looping throung key-value pairs
for key, value in alien_0.items():
    print(f"{key}", end=' | ')
    print(f"{value}", end='\n')
#Looping through keys
for kyes in alien_0.keys():
    print(f"The Keys in alien dictionaries are {kyes}")
# Looping through dictionaries keys in particular order
for key in sorted(alien_0.keys()):
    print(key)
# Looping through all keys and removing the repeated ones
for key in languages.keys():
    print(key)
# Looping Through all values 
for value in languages.values():
    print(value)
# A list of Dictionaries
my_alien = []
for alien_number in range(30):
    new_alien = {
        'name' : 'zapada',
        'points' : 10,
        'speed' : 'medium'
    }
    my_alien.append(new_alien)
print(my_alien[:3])
# List in a dictionary
person = {
    'friends' : ['zohaib', 'shoaib', 'sonia'],
    'parents' : ['Zenub', 'G Shabbir']
}
for key in person.keys():
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(key, " | " ,value)\
# Dictionary in Dictionary
my_info = {
    'me' : {
        'name' : 'zohaib',
        'age' : 20,
        'religion' : 'Islam',
        'speciality' : 'Inteligence'
    },
    'you' : {
        'name' : 'shoaib',
        'age' : 21,
        'religion' : 'Islam',
        'speciality' : 'Artist'
    }
}
for value in my_info.values():
    print(value)
    