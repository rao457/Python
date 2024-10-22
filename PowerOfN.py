def powerofn(x, n):
    """ Function to calculate power of x"""
    if x == 0: # base case 1
        return 0
    if n == 0: # base case 2
        return 1
    powerN_1 = powerofn(x, n-1) # Power of n-1 to call recursively
    powern = x*powerN_1 # calculating power of n
    return powern
def main():
    x = int(input("Enter the base component: "))
    n = int(input("Enter the power You want "+ str(x) +" to raise: "))
    ans = powerofn(x, n)
    print(ans)
if __name__ == "__main__": # to prevent auto running when import from some other file
    main()
