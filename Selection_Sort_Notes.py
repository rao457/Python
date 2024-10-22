
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list
my_array = [45,6,734,8,45,7]
result = selection_sort(my_array)
print(result)