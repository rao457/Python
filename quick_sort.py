""" This programme sorts the list in the ascending order through quick_sort"""
def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    lesser = [x for x in my_list[1:] if x <= pivot]
    greater = [x for x in my_list[1:] if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
    array = [23, 5, 19, 8, 12, 7, 31, 2, 45, 10]

result = quick_sort(my_list)
print(result)