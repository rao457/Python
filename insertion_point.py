# arr = [2,3,4,6]
# val = 5
# for i in range(len(arr)):
#     if arr[i] == val:
#         print(i)
#     elif i+1 < len(arr):
        
#             if arr[i+1] > val:
#                 print(i+1)

# Efficient Algo
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while (left <= right):
        mid = (left + right)// 2
        if arr[mid] == target:
            return mid
        elif mid < target:
            left = mid +1
        else:
            right = mid -1
    return left
arr = [1,2,3,4,5,7]
target = 6
result = binary_search(arr, target)
print(result)
