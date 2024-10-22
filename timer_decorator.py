def timer(func):
    import time
    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        t = t2-t1
        print(round(t))
    return wrapper_function