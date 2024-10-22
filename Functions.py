# Simple Function
def greet_users():
    """It is a simple greet function"""
    print("Hello User!")
greet_users()
# Passing some information to function
def hey(username):
    print(f"Hello! {username.title()}.")
hey('zohaib')
# Assessment
def learning():
    print("We are learning about functions in python in this chapter.")
learning()
def fav_book(titles):
    print(f"One of my favourite books is {titles.title()}")
fav_book('crash course in python')
# Positional Arguments
def pet_describe(pet_type, pet_name):
    print(f"{pet_name.title()} is a {pet_type}")
pet_describe('cat', 'jolly')
name = input("Enter the name of you pet? ")
type = input("Enter the pet_type? ")
pet_describe(type, name)
pet_describe(pet_type='Cock', pet_name='Jutt')
# Default Value
def my_info(job, name, religion = 'Islam' ):
    print(f"{name.title()} is a  {job} and he is a {religion} ")
my_info('software_engineer', 'zohaib')
# Assessment
def t_shirt(size = 'large', text = 'I Love Python'):
    print(f"T_shirt of {size} is ready with {text.title()} written on it.")
t_shirt('xxl', '(I am G*y A is missing)')
t_shirt(text='F*ck U is missing', size='xl')
t_shirt()
def describe_city(city, country = 'Pakistan'):
    print(f"{city} is in {country}")
describe_city('Islamabad')
describe_city('Mumbai', country='India')
describe_city('Khatmando', 'Nepal')
describe_city(city='Karachi', country='Pakistan')