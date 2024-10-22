def reverse_Pyramid(n):
    # UPPER DIAMOND
    i = n
    k = 1
    while(i!=0):
        for j in range(1,i):
            print(" ",end="")
        for j in range(k):
            print("*",end="")
        for j in range(1,k):
            print("*",end="")
        print()
        i-=1
        k += 1
    # LOWER DIAMOND
    for i in range(1, n):
        for j in range(i):
            print(" ",end="")
        for j in range(n+1):
            print("*", end="")
        for j in range(n+1):
            print("*",end="")
        print()
n = 4
if __name__ == "__main__":
    reverse_Pyramid(n)