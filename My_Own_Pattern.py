def main(n):
    
    for i in range(1,n+1):
        # for left stars
        for j in range(i):
            print("*",end="")
        
        # for spaces 
        for j in range(2*(n-i)):
            print(" ",end="")
        # for stars 
        for j in range(i):
            print("*", end="")
        print()
    i = n
    while(i!=0):
        # for stars
        for j in range(i):
            print("*",end="")
        # for spaces
        for j in range(2*(n-i)):
            print(" ",end="")
        # for stars
        for j in range(i):
            print("*",end="")
        print()
        i -= 1
n = 6
if __name__ == "__main__":
    main(n)