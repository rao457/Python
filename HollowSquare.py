def hollowSquare(n):
    for i in range(n):
        for j in range(n-2):
            if (j == 0):
                print("*",end="")
                print(" ",end="")
            if (i == 0):
                print("*",end="")
                print(" ",end="")
            if (i == n-1):
                print("*",end="")
                print(" ",end="")
            if (j != 0 and i != 0 and i != n-1):
                print("    ",end="")
            if (j == n-3):
                print("*",end="")
                # print(" ",end="")
            
        print()
n = 4
hollowSquare(n)