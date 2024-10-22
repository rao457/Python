records = [
    ('zoo', 3, 5),
    ('zu', 'Hello'),
    ('zoo', 5,2),
    ('zu', 'Done')
]
def do_zoo(x, y):
    print('zoo', x, y)
def do_zu(x):
    print('zu', x)
for tag, *args in records:
    if tag == 'zoo':
        do_zoo(*args)
    elif tag == 'zu':
        do_zu(*args)