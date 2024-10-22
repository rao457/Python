def product(arr):
    n = len(arr)
    ans = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if (i != j):
                ans[i] *= arr[j]
    return ans
arr = [1,2,3,4]
result = product(arr)
print(result)