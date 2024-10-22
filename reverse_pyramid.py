def reverse_pyramid(n):
    for i in range(1,n):
        # spaces 
        for j in range(1, n-i):
            print(" ", end='')
        for k in range(1, i):
            print(k, end='')
        print()
reverse_pyramid(9)