def print_diamond(n):
    # for i in range(1,n):
    #     spaces = n-i
    #     for j in range(1, spaces):
    #         print(" ", end='')
    #     for j in range(1, (2*i)-1):
    #         print("*", end='')
    #     print()
    #     i+=1
    for i in range(n,1):
        
        spaces = n-i
        for j in range(1, spaces ):
            print(" ", end='')
        for j in range(1, 2*i-1):
            print("*", end='')
        print()
        
print_diamond(6)