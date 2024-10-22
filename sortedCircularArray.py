# Circular Sorted array approach for finding the target in the circular sorted arr
# by binary search With the time complexity O(logn)
def findInCircular(arr, target):
    start = 1
    end = len(arr) - 2
    while (start <= end):
        mid = start + (end - start)//2
        if (arr[mid] == target):
            return mid
        elif (arr[start] <= target <= arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return -1
arr = [3,4,5,6,7,0,1,2]
target = 0
result = findInCircular(arr, target)
print(result)