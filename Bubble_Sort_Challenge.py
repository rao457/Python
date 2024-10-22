""" This programe checks whether the provided list is sorted or not"""
def bubble_sort(my_array):
    sorted = True
    n = len(my_array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1]  = my_array[j+1], my_array[j]
                swapped = True
                sorted = False
        if not swapped:
            break
    return sorted

my_array = [1,2,3]
result = bubble_sort(my_array)
print(result)
