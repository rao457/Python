def quick_sort(my_list):
    if len(my_list)<= 1:
        return my_list
    pivot = my_list[0]
    lesser = [char for char in my_list[1:] if char <= pivot]
    greater = [char for char in my_list[1:] if char > pivot]
   
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
my_list = [2,311,76,3,21,47,3]
print(quick_sort(my_list))