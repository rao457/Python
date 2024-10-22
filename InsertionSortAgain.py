def sort_array(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while (j>=0 and key < array[j]):
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array
my_array = [3,5,2,8,7]
result = sort_array(my_array)
print(result)