def reverse_triangle(n):
    for i in range(0, n):
        # spaces 
        for j in range(1, n-i):
            print(" ", end='')
        for k in range(1, i+1):
            print("*", end='')
        print()
reverse_triangle(5)