def sort_quickly(arr):
    n = len(arr)
    pivot = arr[0]
    if (n <= 1):
        return arr
    lesser = [x for x in  arr[1:] if x <= pivot]
    greater = [x for x in
     arr[1:] if x> pivot]
    return sort_quickly(lesser) + [pivot] + sort_quickly(greater)
array = [23, 5, 19, 8, 12, 7, 31, 2, 45, 10]
result = sort_quickly(array)
print(result)