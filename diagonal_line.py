import time
def hollowDiamond(n):
    # Top part of the diamond
    for i in range(n):
        # spaces
        spaces = n - i -1
        for j in range(spaces):
            print(" ",end="")
        print("*",end="")
        time.sleep(0.5)
        if (i != 0):
            newSpaces = (2 * i) - 1
            for j in range(newSpaces):
                print(" ",end="")
            print("*",end="")
            time.sleep(0.5)
        print()
    # bottom part
    for i in range(n-1):
        # spaces
        for j in range(i+1):
            print(" ", end="")
        print("*",end="")
        time.sleep(0.5)
        if (i != n-2):
            spaces = 2*(n - i) - 5
            for j in range(spaces):
                print(" ",end="")
            print("*",end="")
            time.sleep(0.5)
        print()
n = 10
hollowDiamond(n)