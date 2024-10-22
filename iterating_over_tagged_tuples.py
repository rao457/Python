tagged_tuples = [
    ("apple", 10, True),
    ("banana", 5.5, False, "yellow"),
    (42, "pineapple", ["sweet", "tropical"]),
    ("orange",),
    (True, False, True),
    (3.14, "pie", {"flavor": "delicious", "size": "large"})
]
def do_apple(x,y):
    print('apple', x, y)
def do_banana(x,y,z):
    print('banana', x, y, z)
def do_pineapple(x,y,z):
    print('pineapple', x, y, z) # z is a list   
def do_orange():
    print('orange',)  
def do_pie(x,y):
    print('pie', x, y)  
for tag, *args in tagged_tuples:
    if tag == 'apple':
        do_apple(*args) 
    elif tag == 'banana':
        do_banana(*args)
    elif tag == 'pineapple':
        do_pineapple(*args)
    elif tag == 'orange':
        do_orange(*args)
    elif tag == 'pie':
        do_pie(*args)