
def time(func):
    import time
    def calc(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        t = t2-t1
        print(f"This function ran in {t} seconds.")
    return calc
@time
def my_iteration(list1):
    for i in list1:
        print(i)
my_list = [x for x in range(1000)]

my_iteration(my_list)
