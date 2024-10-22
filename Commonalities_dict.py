b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}
a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
new_dict = {key:a[key] for key in a.keys()-{'z', 'w'}}
print(new_dict)