def powerCal(n, x):
    ans = 1
    binForm = n
    if (binForm == 0):
        return ans
    r = binForm % 2
    if (r == 0):
        x = x * x
    else:
        ans = x
        x = x * x

    binForm = binForm // 2

    return powerCal(binForm, x)
n = 5
x = 3

print(powerCal(n, x))
