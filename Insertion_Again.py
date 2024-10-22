def insertion_sort(my_list):
    """ this programme simply sort the provided list with insetion algorithm
"""
    n = len(my_list)
    for i in range(1, n):
        key = my_list[i]
        j = i-1
        while j >= 0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
            my_list[j+1] = key
    return my_list
my_list = [5,4,6,9,3]
result = insertion_sort(my_list)
print(result)

