# In this portion we are gonna mantain the space complexity for the program
def productSelf(arr):
    n = len(arr)
    suffix = [1] * n
    prefix = [1] * n
    for i in range(1,n):
        suffix[i] *= arr[i]
    for i in range(1,n):
        prefix[i] *= arr[i]
    for i in range(1,n):
        
