def solid_rhombus(n):
    n_ = n+1
    for i in range(1, n_):
        # spaces 
        for j in range(1, n_-i):
            print(" ", end='')
        for k in range(1, n_):
            print("*", end='')
        print()
solid_rhombus(5)