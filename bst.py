def BinarySearch(arr, val):
    start = 0
    end = len(arr) -1
    while (start < end):
        mid = (start+end)// 2
        if (val == arr[mid]):
            return mid
        elif(val < arr[mid]):
            end = mid -1
        else:
            start = mid + 1
    return 0
    
arr = [1,2,4,5,6]
val = 4
result = BinarySearch(arr, val)
if (result != 0):
    print("Found the number.")
else:
    print("Number is not found")