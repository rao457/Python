def BSTRec(arr, low, high, key):
    if (low == high):
        if (arr[low] == key):
            return low
        else:
            return 0
    else:
        mid = (low + high) // 2
        if (key < arr[mid]):
            BSTRec(arr, low, mid - 1, key)
        else:
            BSTRec(arr, mid+1, high, key)
arr = [23,4,3,6,12,45,8,45,2,12,3]
n = len(arr)
result = BSTRec(arr, 0, n-1, 45)
print(result)
