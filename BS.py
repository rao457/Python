def binary(arr,key):
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (low + high) // 2
        if (key == arr[mid]):
            return mid
            
        elif (arr[mid] > key):
            high = mid -1
        else:
            low = mid + 1
    return 0
arr =  [23,4,3,6,12] # I was making a mistake of not sorting the list

result = binary(arr, 6)
print(result)