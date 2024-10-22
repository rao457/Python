def Quick_Sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        pivot = my_list[0]
        lesser = [x for x in my_list[1:] if x <= pivot]
        greater = [x for x in my_list[1:] if x > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater)

my_list = [1, 4, 6, 8, 3, 4, 56, 3, 43, 57]
result = Quick_Sort(my_list)
print(result)
