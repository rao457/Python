# Done in python as well

def findTarget(arr, target):
    start = 0
    n = len(arr)
    end = n - 1
    while(start <= end):
        mid = start + (end - start)//2
        if (arr[mid] == target):
            return mid
        elif(arr[start] <= arr[mid]): # Our left half is sorted
            if (arr[start]  <= target <= arr[mid]):
                end = mid - 1
            else:
                start = mid + 1
        else: # Our right half is sorted
            if (arr[mid] <= target <= arr[end]):
                start = mid + 1
            else: 
                end = mid - 1
    return -1
arr = [5,6,7,8,0,1,2,3,4]
target = 2
result = findTarget(arr, target)
print(f"Required number {target} is found at index {result}")
