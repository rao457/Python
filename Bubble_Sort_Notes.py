def Bubble_sort(my_list):
    """ This algorithm is comparison based and we sort arrays in it."""
    n = len(my_list)
    for first in range(n):
        swapped = False
        for second in range(0, n-first-1):
            if my_list[second] > my_list[second+1]:
                my_list[second], my_list[second+1] = my_list[second+1], my_list[second]
                swapped = True
    return my_list
my_array = [3,5,2,8,7]
result = Bubble_sort(my_array)
print(result)