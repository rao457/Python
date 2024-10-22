
def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    pivot = array[n-1]
    lesser = [i for i in array[0:n-1] if i <= pivot]
    greater = [i for i in array[0:n-1] if i > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
array = [23, 5, 19, 8, 12, 7, 31, 2, 45, 10]
result = quick_sort(array)
print(result)