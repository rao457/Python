def findPower(x, n):
    ans = 1
    pow = x
    Bin_form = n
    while(Bin_form > 0):
        r = Bin_form % 2
        if (r == 1):
            ans *= pow
        pow *= pow
        Bin_form //= 2
    return ans
result = findPower(6.025, 23)
print(result)