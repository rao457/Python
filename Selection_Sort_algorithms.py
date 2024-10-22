""" This programme sorts the input data into ascending order using selection sort algorithms"""
def selection_sort(my_array):
    n = len(my_array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    return my_array
my_array = [45,6,734,8,45,7]
result = selection_sort(my_array)
print(result)
