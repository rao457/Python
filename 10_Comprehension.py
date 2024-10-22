new_list = [x for x in range(10)]
print(new_list)
even_list = [x for x in range(20) if x % 2 == 0]
print(even_list)
valid_string = []
options = ['any', 'hello', 'world', 'albany', 'apple', '']
for string in options:
    if len(string) <= 1:
        continue
    if string[0] != 'a':
        continue
    if string[-1] != 'y':
        continue
    valid_string.append(string)
print(valid_string)
valid_compre = [
    string
    for string in options
    if len(string) > 0
    if string[0] == 'a'
    if string[-1] == 'y'

]
print(valid_compre)
matrix = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)
flattened_compre = [num for row in matrix for num in row]
print(flattened_compre)
category = []
for num in range(10):
    if num%2 ==0:
        category.append('Even')
    else:
        category.append('Odd')
print(category)
category_compre = [
    'Even' if x%2==0 else 'Odd' for x in range(20)
]
print(category_compre[:10])
import pprint
printer = pprint.PrettyPrinter()
lst = []
for a in range(5):
    lst1 = []
    for b in range(5):
        lst2 = []
        for num in range(5):
            lst2.append(num)
        lst1.append(lst2)
    lst.append(lst1)
lst_compre = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst_compre)
def square(x):
    return x ** 2
square_members =  [square(x) for x in range(10)]
print(square_members)
sum_squares = sum(x**2 for x in range(1000000))
print(sum_squares)