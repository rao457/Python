cars =  ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper(), end='  ')
    else:
        print(car.title(), end='  ')
vhicle = 'toyota'
print(vhicle == 'bmw')
requested_pizza = 'papperoni'
if requested_pizza != 'vegeterian':
    print('Hold the vegeterian')

answer = 12
if answer != 23 and answer!= 22 and answer != 24:
    print("It is correct answer. Let's move on to next question.")
name = 'zohaib'
age = 20
if name == 'zohaib':
    print('OK')
if age> 18 and age<=20:
    print('You are eligible')
banned_users = ['ali', 'kaleem', 'nazia', 'asif', 'saleem']
username = input("Enter the username: ")
if username in banned_users:
    print('You cannot post a comment.')
if username not in banned_users:
    print(f'{username.title()}, You can post your comment.')