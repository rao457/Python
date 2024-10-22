def binary_triangle(n):
    for i in range(1, n):
        for j in range(1, i+1):
            sum = j+i
            if (sum%2==0):
                print("0",end='')
            else:
                print("1", end='')
        print()
binary_triangle(5)