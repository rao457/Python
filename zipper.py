my_list = [1,2,3,4,5, 6]
your_list = [6,7,8,9,10]
my_zip = list(zip(my_list,your_list))
print(my_zip)
list_1, list_2 = zip(*my_zip)
print(list_1)
print(list_2)