import logging
logging.basicConfig(filename='my_file.log', level=logging.INFO)
def outer_func(func):
    def inner_func(*args):
        logging.info(f"Running {func.__name__} with argument {args}")
            

        
        print(func(*args))
    return inner_func
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
my_add = outer_func(add)
my_add(2,3)
my_sub = outer_func(sub)
my_sub(10, 6)