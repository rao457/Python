def insertion_sort(my_list):
    """  this programme sorts the list by picking a key element at every iteration and comparing it with the previous and one and sorting the list at the end"""
    n = len(my_list)
    for i in range(1, n):
        key = my_list[i]
        j = i-1
        while j>=0 and key< my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
            my_list[j+1] = key
    return my_list
my_list = [1,4,6,8,3,4,56,3,43,57]
result = insertion_sort(my_list)
print(result)