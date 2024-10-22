def outer_func():
    message = 'zohaib'
    def inner_func():
        print(message)
    return inner_func
var = outer_func()
print(var.__name__)