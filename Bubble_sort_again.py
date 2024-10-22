def Bubble_sort(my_list):
    """ This programmes simply sorts the list by using the bubble sort algorithm"""
    # Length of list to iterate over
    n = len(my_list)
    # We iterate over the length of the list to keep account of loops ran over the list so that we can avoid unnecessary iteration over the list when it is sorted

    for i in range(n):
        swapped = False
        # We iterate over the elements of list 
        # from start to n-i-1 where i is number of passes and 1 minus means that the bigger element is now sorted and
        # we don't need to add it in the next iteration
        for j in range(0, n-i-1):
            # We swap the elements if bigger is not at the correct position
            if my_list[j]>my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True
    return my_list
my_list = [4,3,6,7,5,4]
result = Bubble_sort(my_list)
print(result)