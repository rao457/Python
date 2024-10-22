def calcPower(n, x):
    ans = 1
    binForm = x
    
    while (binForm > 0):
        if (binForm % 2 == 1):
            ans *= n
        n *= n
        binForm //= 2
    return ans
n = 3
x = 5
result  = calcPower(3, 5)
print(f"The result is {result}")