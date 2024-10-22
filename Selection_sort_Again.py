def selection_sort(my_list):
    """ this programmes sorts the list in the ascending order"""

    n = len(my_list)
    # When we iterate over the len of some list or any iterable object 
    # we simply want to keep track of its index
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

my_list = [43,5,6,2,66,32,53]
result = selection_sort(my_list)
print(result)
    