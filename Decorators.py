import time
def outer_func():
    message = 'Hi'
    def inner_func():
        print(f"{message} Zohaib")
    return inner_func()
outer_func()
def my_decorator(fun):
    def wrapper_func():
        
        print(f"The wrapper function is executing before the {fun.__name__}")
        t1 = time.time()
        fun()
        t2 = time.time()
        
        t = t2-t1
        print(t)
        print(f"This is after function")
    return wrapper_func()
@my_decorator
def display():
    print("This function is decorated.")
    time.sleep(1)
    print("After time")
def greet(func):
    def wrapper_function(*args, **kwargs):
        print("Hey Users!")
        func(*args, **kwargs)
        print("Have a good day")
    return wrapper_function
@greet
def users(user1, user2):
    print(f"{user1} and {user2}! You are advised to submit the result of the survey by tomorrow.")
users('Zohaib', 'Shoaib')